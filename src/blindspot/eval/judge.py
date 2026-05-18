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
  - 5 = many concrete dollar amounts, named clauses, INA / 8 CFR section
    numbers, USCIS PM references; specific deadline-counts (24-month
    STEM-OPT, 60-day grace, 90-day unemployment); specific dates /
    horizons; reader could act without further lookup
  - 3 = some concrete terms (e.g. "OPT", "STEM-OPT", "AC21 portability")
    but few numbers or specific clauses; reader still needs lookup
  - 1 = generic advice with no named mechanism or number

- non_obviousness (1-5):
  - 5 = response surfaces blind spots the reader almost certainly didn't
    know to ask about (e.g. AC21 §106(c) portability after I-140
    approval preserves priority date even on employer switch; H-4 EAD
    validity tracks principal's I-140 approval, not just H-1B status;
    day-1-CPT carries higher SEVIS scrutiny than STEM-OPT)
  - 3 = mix — some new angles plus baseline content
  - 1 = entirely things the reader would think of unprompted (e.g.
    "negotiate", "consult an immigration attorney", "talk to HR")

- grounding_pct (0-100): integer percent of factual claims that carry at
  least one [doc-X] citation marker. A "factual claim" is any sentence
  asserting a real-world fact, mechanism, or rate — including visa /
  immigration mechanics (deadline counts, statutory cross-references,
  USCIS policy guidance), typically cited from sources like
  us-immigration-counsel or curated 一亩三分地 threads. Frame comments
  and meta-language ("here's what to consider") do not count as claims.
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
