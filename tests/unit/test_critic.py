import pytest

from blindspot.agents.critic import run_critic
from blindspot.config import Config
from blindspot.types import RiskOfficerOutput


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {
            "specificity": "pass",
            "non_obviousness": 4,
            "grounding_pct": 92,
            "regenerate_required": False,
            "feedback": "good",
        }


@pytest.mark.asyncio
async def test_critic_returns_verdict():
    v = await run_critic("s", [], RiskOfficerOutput([]), StubLLM(), Config())
    assert v.specificity_pass is True
    assert v.non_obviousness == 4
    assert v.regenerate_required is False
