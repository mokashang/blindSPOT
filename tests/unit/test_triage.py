import pytest

from blindspot.agents.triage import run_triage
from blindspot.config import Config
from blindspot.types import Facet


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {
            "domains": ["tech-career/equity"],
            "entities": ["ISO", "series-B"],
            "risk_surfaces": ["tax"],
            "personas": ["first-time-offer"],
        }


@pytest.mark.asyncio
async def test_triage_returns_situation_with_tags():
    sit = await run_triage("I got a Series B offer with 0.1% ISOs", StubLLM(), Config())
    assert sit.tags[Facet.DOMAIN] == ["tech-career/equity"]
    assert "ISO" in sit.tags[Facet.ENTITY]
    assert sit.tags[Facet.PERSONA] == ["first-time-offer"]
