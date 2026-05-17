"""Orchestrator: wires the 6-agent pipeline together and persists results."""

from __future__ import annotations

import asyncio
import hashlib
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session as SQLSession

from blindspot.agents.collection import collect
from blindspot.agents.community_analyst import run_community_analyst
from blindspot.agents.critic import run_critic
from blindspot.agents.editor import run_editor
from blindspot.agents.risk_officer import run_risk_officer
from blindspot.agents.triage import run_triage
from blindspot.config import Config
from blindspot.db.models import (
    BlindSpotRow,
    BlindSpotSourceRow,
    DocumentRow,
    SessionRow,
    TurnRow,
    TurnTagRow,
    UngroundedClaimRow,
)
from blindspot.filters.grounding import find_unmarked_claims
from blindspot.llm.base import Embedder, LLMClient
from blindspot.sources.base import SourceView
from blindspot.sources.registry import load_all_sources, load_registry
from blindspot.sources.tag_match import select_top_n
from blindspot.tags.taxonomy import add_or_merge_tag
from blindspot.types import (
    Facet,
    FinalResponse,
    RiskOfficerOutput,
    SearchContext,
    Situation,
)


@dataclass
class Orchestrator:
    cfg: Config
    llm: LLMClient
    embedder: Embedder
    db: SQLSession
    registry: list[SourceView]

    @classmethod
    def create(cls, cfg, llm, embedder, db, registry_path=None):
        """Build an Orchestrator with its source-view registry loaded.

        - ``registry_path=None`` (production default): use
          ``load_all_sources()`` which prefers per-domain
          ``domain_knowledge/<domain>/sources.yaml`` files and falls
          back to ``data/source_registry.yaml`` when none exist.
        - ``registry_path=<path>``: load that single YAML file via the
          legacy ``load_registry`` path. Used by the orchestrator
          integration test to feed a tmp_path registry.
        """
        if registry_path is None:
            registry = load_all_sources()
        else:
            registry = load_registry(registry_path)
        return cls(
            cfg=cfg, llm=llm, embedder=embedder, db=db,
            registry=registry,
        )

    async def run(
        self,
        situation_text: str,
        user_id: str = "local",
        session_id: int | None = None,
    ) -> FinalResponse:
        # Step 1: Triage.
        situation = await run_triage(situation_text, self.llm, self.cfg)

        # Step 1.5: Normalize tags via the tag taxonomy. Embed every candidate
        # tag in one batched request — the Voyage free tier is 3 RPM, so a
        # request per tag rate-limits the run.
        candidates = [v.strip() for values in situation.tags.values() for v in values]
        candidates = [c for c in candidates if c]
        emb_by_tag: dict[str, list[float]] = {}
        if candidates:
            vectors = await self.embedder.embed(candidates)
            emb_by_tag = dict(zip(candidates, vectors, strict=True))

        normalized: dict[Facet, list[str]] = {}
        for facet, values in situation.tags.items():
            # Distinct candidates can merge to the same canonical tag; dedupe
            # per facet (preserving order) so TurnTagRow's UNIQUE constraint
            # on (turn_id, facet, tag) holds.
            seen: set[str] = set()
            normalized[facet] = []
            for v in values:
                res = await add_or_merge_tag(
                    self.db,
                    self.embedder,
                    self.cfg,
                    facet.value,
                    v,
                    candidate_embedding=emb_by_tag.get(v.strip()),
                )
                if res.accepted_tag and res.accepted_tag not in seen:
                    seen.add(res.accepted_tag)
                    normalized[facet].append(res.accepted_tag)
        situation.tags = normalized

        # Step 2: Source matching.
        selected = await select_top_n(
            self.registry, situation, self.cfg, self.embedder
        )
        if not selected:
            return self._empty_response(
                situation,
                "No relevant sources matched this situation. "
                "Blindspot V1 only covers US tech career & equity decisions.",
            )

        # Step 3: Collection.
        ctx = SearchContext(
            situation=situation,
            entity_terms=situation.tags.get(Facet.ENTITY, []),
        )
        docs = await collect(selected, ctx, self.embedder)

        # Step 4: Community analysts (parallel, one per active community).
        by_community: dict[str, list] = {}
        for d in docs:
            by_community.setdefault(d.community_tag, []).append(d)
        analyst_tasks = [
            run_community_analyst(tag, situation, c_docs, self.llm, self.cfg)
            for tag, c_docs in by_community.items()
        ]
        analyst_outputs = await asyncio.gather(*analyst_tasks)

        # Step 5: Risk Officer.
        risk_output = await run_risk_officer(
            situation, analyst_outputs, docs, self.llm, self.cfg
        )

        # Step 6: Critic. Single retry if regenerate_required — the retry
        # feeds the critic's feedback back into Risk Officer so the new
        # generation actually has signal about what to fix.
        verdict = await run_critic(
            situation_text, analyst_outputs, risk_output, self.llm, self.cfg
        )
        if verdict.regenerate_required:
            risk_output = await run_risk_officer(
                situation,
                analyst_outputs,
                docs,
                self.llm,
                self.cfg,
                prior_critic_feedback=verdict.feedback,
            )
            verdict = await run_critic(
                situation_text, analyst_outputs, risk_output, self.llm, self.cfg
            )

        # Step 7: Editor.
        rendered = await run_editor(
            situation, analyst_outputs, risk_output, docs, self.llm, self.cfg
        )

        # Step 8: Persist.
        self._persist(
            user_id, situation_text, rendered, situation, docs,
            analyst_outputs, risk_output, session_id=session_id,
        )
        return FinalResponse(
            situation=situation,
            community_outputs=list(analyst_outputs),
            risk_output=risk_output,
            critic_verdict=verdict,
            rendered_markdown=rendered,
            documents_used=docs,
        )

    def _empty_response(self, situation: Situation, reason: str) -> FinalResponse:
        return FinalResponse(
            situation=situation,
            community_outputs=[],
            risk_output=RiskOfficerOutput([]),
            critic_verdict=None,
            rendered_markdown=f"## Unable to help\n\n{reason}",
            documents_used=[],
        )

    def _persist(
        self,
        user_id,
        raw,
        rendered,
        situation,
        docs,
        analyst_outputs,
        risk_output,
        session_id: int | None = None,
    ):
        if session_id is not None:
            sess = self.db.get(SessionRow, session_id)
            if sess is None:
                # Fall through to creating a new session if the requested
                # one doesn't exist (defensive — the CLI validates first,
                # but tests and library callers may not).
                sess = SessionRow(user_id=user_id, situation=raw, language="en")
                self.db.add(sess)
                self.db.flush()
                next_turn = 1
            else:
                # Continue an existing session: next turn_number = max + 1.
                existing_max = (
                    self.db.query(TurnRow)
                    .filter_by(session_id=sess.id)
                    .order_by(TurnRow.turn_number.desc())
                    .first()
                )
                next_turn = (existing_max.turn_number + 1) if existing_max else 1
        else:
            sess = SessionRow(user_id=user_id, situation=raw, language="en")
            self.db.add(sess)
            self.db.flush()
            next_turn = 1

        turn = TurnRow(
            session_id=sess.id,
            turn_number=next_turn,
            user_input=raw,
            assistant_response=rendered,
        )
        self.db.add(turn)
        self.db.flush()

        for facet, tags in situation.tags.items():
            facet_val = facet.value if hasattr(facet, "value") else facet
            for t in tags:
                self.db.add(TurnTagRow(turn_id=turn.id, facet=facet_val, tag=t))

        now = datetime.now(timezone.utc)
        doc_id_map: dict[str, int] = {}
        for d in docs:
            ch = hashlib.sha256(d.content.encode()).hexdigest()
            existing = (
                self.db.query(DocumentRow).filter_by(content_hash=ch).first()
            )
            if existing is not None:
                doc_id_map[d.doc_id] = existing.id
                continue
            ttl_days = (
                self.cfg.cache.fresh_ttl_days
                if any(
                    v.id == d.source_view_id and v.freshness_required
                    for v in self.registry
                )
                else self.cfg.cache.evergreen_ttl_days
            )
            row = DocumentRow(
                source_view_id=d.source_view_id,
                fetched_at=now,
                expires_at=now + timedelta(days=ttl_days),
                url=d.url,
                title=d.title,
                content=d.content,
                content_hash=ch,
                language="en",
            )
            self.db.add(row)
            self.db.flush()
            doc_id_map[d.doc_id] = row.id

        for output in [*analyst_outputs, risk_output]:
            blindspots = (
                output.blind_spots
                if hasattr(output, "blind_spots")
                else output.cross_community_blind_spots
            )
            tag = getattr(output, "community_tag", "cross")
            for bs in blindspots:
                bs_row = BlindSpotRow(
                    turn_id=turn.id,
                    hook=bs.hook,
                    body=bs.body,
                    community_tag=tag,
                )
                self.db.add(bs_row)
                self.db.flush()
                for cid in bs.citation_doc_ids:
                    if cid in doc_id_map:
                        self.db.add(
                            BlindSpotSourceRow(
                                blind_spot_id=bs_row.id,
                                document_id=doc_id_map[cid],
                            )
                        )

        unmarked = find_unmarked_claims(rendered)
        for claim in unmarked:
            self.db.add(
                UngroundedClaimRow(
                    turn_id=turn.id,
                    claim_text=claim,
                    context=raw[:500],
                    logged_at=now,
                )
            )

        self.db.commit()
