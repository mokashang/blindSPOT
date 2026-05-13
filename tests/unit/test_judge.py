import pytest

from blindspot.config import Config
from blindspot.eval.judge import judge_response


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {
            "specificity": 4,
            "non_obviousness": 4,
            "grounding_pct": 90,
            "diversity_count": 3,
            "feedback": "ok",
        }


@pytest.mark.asyncio
async def test_judge_returns_scores():
    out = await judge_response("s", "r", StubLLM(), Config())
    assert out["specificity"] == 4
    assert out["grounding_pct"] == 90
