"""LLM-as-judge: score an end-to-end response on specificity, non-obviousness, grounding."""

from __future__ import annotations

from blindspot.config import Config
from blindspot.llm.base import LLMClient

JUDGE_SYSTEM = """\
You are a quality judge for Blindspot responses. Given a user situation and
the system's response, score it on:

- specificity (1-5): concrete numbers, named entities, mechanisms
- non_obviousness (1-5): would a smart 25-year-old tech worker already know this
- grounding_pct (0-100): fraction of factual claims with [doc-X] citation
- diversity_count: distinct community sections present

Return JSON: {"specificity": n, "non_obviousness": n, "grounding_pct": n, "diversity_count": n, "feedback": "..."}
"""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "specificity": {"type": "integer", "minimum": 1, "maximum": 5},
        "non_obviousness": {"type": "integer", "minimum": 1, "maximum": 5},
        "grounding_pct": {"type": "integer", "minimum": 0, "maximum": 100},
        "diversity_count": {"type": "integer", "minimum": 0},
        "feedback": {"type": "string"},
    },
    "required": ["specificity", "non_obviousness", "grounding_pct", "diversity_count"],
}


async def judge_response(
    situation: str, response_md: str, llm: LLMClient, cfg: Config
) -> dict:
    out = await llm.complete(
        system=JUDGE_SYSTEM,
        user=f"# Situation\n{situation}\n\n# Response\n{response_md}",
        model=cfg.models.default,
        json_schema=JUDGE_SCHEMA,
    )
    assert isinstance(out, dict)
    return out
