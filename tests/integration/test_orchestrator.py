from datetime import datetime, timezone

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.models import Base
from blindspot.orchestrator import Orchestrator
from blindspot.types import Document


class StubLLM:
    """Routes by unique opening phrase in each agent's system prompt.

    "Role" alone is too loose because e.g. editor.md mentions Risk Officer in
    its instructions; "You are the/a <Role>" only appears in that agent's own
    prompt.
    """

    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        if "You are the Triage Officer" in system:
            # Two domain tags that the StubEmbedder (identical vectors) will
            # merge to one canonical tag — exercises tag de-duplication.
            return {
                "domains": ["tech-career/equity", "tech-career/negotiation"],
                "entities": ["ISO"],
                "risk_surfaces": ["tax"],
                "personas": ["first-time-offer"],
            }
        if "You are a Community Analyst" in system:
            return {
                "prose": "Tech veterans... [doc-1]",
                "blind_spots": [
                    {
                        "hook": "AMT",
                        "body": "spread tax [doc-1]",
                        "citation_doc_ids": ["doc-1"],
                    }
                ],
            }
        if "You are the Risk Officer" in system:
            return {
                "cross_community_blind_spots": [
                    {
                        "hook": "Adverse selection",
                        "body": "Why now [doc-1]",
                        "citation_doc_ids": ["doc-1"],
                    }
                ]
            }
        if "You are the Critic" in system:
            return {
                "specificity": "pass",
                "non_obviousness": 4,
                "grounding_pct": 95,
                "regenerate_required": False,
                "feedback": "ok",
            }
        if "You are the Editor" in system:
            return (
                "## Situation\n...\n"
                "## Blind spots\n1. AMT [doc-1]\n"
                "## Sources\n- (doc-1) https://x"
            )
        raise AssertionError(f"unrouted stub call; system starts with: {system[:80]}")


class StubEmbedder:
    def __init__(self):
        self.calls: list[list[str]] = []

    async def embed(self, texts):
        self.calls.append(list(texts))
        return [[0.0, 1.0]] * len(texts)


class StubAdapter:
    async def fetch(self, view, ctx):
        return [
            Document(
                doc_id="doc-1",
                source_view_id=view.id,
                community_tag=view.community_tag,
                url="https://x",
                title="Equity 101",
                content="ISO spread tax",
                fetched_at=datetime.now(timezone.utc),
            )
        ]


@pytest.mark.asyncio
async def test_orchestrator_runs_full_pipeline_with_stubs(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "blindspot.agents.collection.build_adapter",
        lambda name, emb: StubAdapter(),
    )

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    registry_yaml = tmp_path / "reg.yaml"
    registry_yaml.write_text(
        """
- id: pmck-equity
  adapter: rss
  fetch_config: {}
  domains: [tech-career/equity]
  community_tag: founder-engineer-bloggers
  reliability: 5
  notes: Equity and ISO mechanics.
"""
    )

    embedder = StubEmbedder()
    with Session(engine) as db:
        orch = Orchestrator.create(
            Config(), StubLLM(), embedder, db,
            registry_path=str(registry_yaml),
        )
        resp = await orch.run("Series B offer with ISOs")

    # Reaching here at all means tag de-duplication worked: the two domain
    # tags merge to one canonical tag, and inserting both as TurnTagRows
    # would trip UNIQUE(turn_id, facet, tag) without the dedup.
    assert "Situation" in resp.rendered_markdown
    assert len(resp.documents_used) == 1

    # Tag normalization must batch: every triage tag goes out as one Voyage
    # request, not one request per tag (free tier is 3 RPM).
    triage_tags = {
        "tech-career/equity",
        "tech-career/negotiation",
        "ISO",
        "tax",
        "first-time-offer",
    }
    assert any(
        set(call) == triage_tags for call in embedder.calls
    ), f"tags were not batched into a single embed() call: {embedder.calls}"
