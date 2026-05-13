import pytest

from blindspot.agents.risk_officer import run_risk_officer
from blindspot.config import Config
from blindspot.types import Facet, Situation


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {
            "cross_community_blind_spots": [
                {
                    "hook": "Adverse selection",
                    "body": "Why is this offer in front of you... [doc-3]",
                    "citation_doc_ids": ["doc-3"],
                }
            ]
        }


@pytest.mark.asyncio
async def test_risk_officer_returns_marquee():
    out = await run_risk_officer(
        Situation(raw_text="s", tags={Facet.DOMAIN: []}),
        analyst_outputs=[],
        docs=[],
        llm=StubLLM(),
        cfg=Config(),
    )
    assert len(out.cross_community_blind_spots) == 1
    assert out.cross_community_blind_spots[0].hook == "Adverse selection"
