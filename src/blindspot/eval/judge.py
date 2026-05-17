"""LLM-as-judge: score an end-to-end response on specificity, non-obviousness, grounding."""

from __future__ import annotations

from blindspot.config import Config
from blindspot.llm.base import LLMClient

JUDGE_SYSTEM = """\
You are a quality judge for Blindspot responses. Given a user situation and
the system's response, score it on the four dimensions below. Use the
anchored rubric points as calibration: a "3" should look like a "3" across
runs, not drift toward "4" when the response is wordy or "2" when it is
terse.

- specificity (1-5):
  - 5 = many concrete dollar amounts, named clauses, IRS section numbers,
    specific dates / horizons; reader could act without further lookup
  - 3 = some concrete terms (e.g. "AMT", "double-trigger") but few numbers
    or specific clauses; reader still needs lookup
  - 1 = generic advice with no named mechanism or number

- non_obviousness (1-5):
  - 5 = response surfaces blind spots the reader almost certainly didn't
    know to ask about (e.g. AMT credit carry-forward, secondary sale
    timing-vs-tender mechanics)
  - 3 = mix — some new angles plus baseline content
  - 1 = entirely things the reader would think of unprompted (e.g.
    "negotiate", "consult a CPA")

- grounding_pct (0-100): integer percent of factual claims that carry at
  least one [doc-X] citation marker. A "factual claim" is any sentence
  asserting a real-world fact, mechanism, or rate. Frame comments and
  meta-language ("here's what to consider") do not count as claims.
  100 = every claim cited; 0 = no citations on any.

- diversity_count: integer count of distinct "What [community] would tell
  you" sections present in the response.

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
