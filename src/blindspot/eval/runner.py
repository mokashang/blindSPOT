"""Run all eval situations and write a JSON results file."""

from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.session import get_engine, init_schema
from blindspot.eval.judge import judge_response
from blindspot.llm.base import Embedder, LLMClient
from blindspot.orchestrator import Orchestrator

# Default per-fixture timeout (seconds). Wraps each fixture's full
# pipeline + judge call. Rationale: 5 consecutive refine runs have been
# unable to measure eval because the claude-agent-sdk pipeline hangs
# indefinitely (>8 min, no stdout) on at least one fixture. PR #11
# (1357c03) hardened _parse_json_response against malformed JSON, which
# closed ONE failure mode; another hang mode persists upstream. Until
# the upstream hang is fixed in the LLM/agent layer, this timeout is a
# safety net at the eval-orchestrator level: a single hung fixture no
# longer sinks the entire eval run. We intentionally do NOT cap
# `blindspot ask` turns — real user-facing pipeline runs are allowed to
# take arbitrarily long; only the eval loop has the cap, so refine
# delta math always has a numeric answer to compute against. Override
# via config (`eval.per_fixture_timeout_seconds`) or CLI flag.
DEFAULT_PER_FIXTURE_TIMEOUT_SECONDS = 240


async def _run_single_fixture(
    fix: dict,
    eval_cfg: Config,
    cfg: Config,
    llm: LLMClient,
    embedder: Embedder,
    engine,
) -> dict:
    """Run the pipeline + judge for one fixture, return its result dict.

    Raises any exception the underlying pipeline / judge raises — the
    caller wraps this in `asyncio.wait_for` and catches asyncio.TimeoutError
    plus generic Exception separately.
    """
    with Session(engine) as db:
        orch = Orchestrator.create(eval_cfg, llm, embedder, db)
        resp = await orch.run(fix["text"])
    verdict = await judge_response(fix["text"], resp.rendered_markdown, llm, cfg)
    return {"id": fix["id"], **verdict}


async def run_eval(
    cfg: Config,
    llm: LLMClient,
    embedder: Embedder,
    fixtures_path: Path = Path("fixtures/eval_situations.yaml"),
    out_dir: Path = Path("eval/results"),
    per_fixture_timeout_seconds: int | None = None,
) -> Path:
    """Run all eval fixtures sequentially and write a JSON results file.

    Each fixture is wrapped with `asyncio.wait_for` at
    `per_fixture_timeout_seconds`. On timeout, the fixture's record carries
    `quality_score: null`, `timed_out: true`, and the eval CONTINUES to
    the next fixture rather than aborting the whole run. The aggregate
    `quality_score` is computed over only non-timed-out fixtures so that
    a single hang doesn't poison the running mean.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    fixtures = yaml.safe_load(fixtures_path.read_text())

    # Resolve timeout: explicit arg > config > module default.
    if per_fixture_timeout_seconds is None:
        per_fixture_timeout_seconds = getattr(
            cfg.eval, "per_fixture_timeout_seconds", DEFAULT_PER_FIXTURE_TIMEOUT_SECONDS
        )

    # Eval runs use a separate SQLite file so synthetic sessions, turns,
    # blind_spots, and ungrounded_claims don't pollute the user's live
    # history / ratings.
    eval_cfg = cfg.model_copy(deep=True)
    eval_db_path = Path(cfg.db.path).expanduser().with_name("blindspot-eval.db")
    eval_cfg.db.path = str(eval_db_path)
    init_schema(eval_cfg)
    engine = get_engine(eval_cfg)

    per_situation: list[dict] = []
    timed_out_ids: list[str] = []
    for fix in fixtures:
        try:
            result = await asyncio.wait_for(
                _run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine),
                timeout=per_fixture_timeout_seconds,
            )
            # Existing fields preserved; explicitly mark non-timed-out
            # records so downstream tooling never has to disambiguate
            # "missing" from "false".
            result["timed_out"] = False
            per_situation.append(result)
        except asyncio.TimeoutError:
            timed_out_ids.append(fix["id"])
            per_situation.append(
                {
                    "id": fix["id"],
                    "timed_out": True,
                    "timeout_seconds": per_fixture_timeout_seconds,
                    "quality_score": None,
                    "reason": (
                        f"fixture exceeded {per_fixture_timeout_seconds}s timeout "
                        f"(pipeline or judge hung)"
                    ),
                }
            )

    def m(key: str) -> float:
        # Aggregate only over fixtures that produced a real verdict —
        # timed-out fixtures don't have rubric scores so including them
        # as zeros would falsely lower the mean.
        vals = [
            r[key]
            for r in per_situation
            if not r.get("timed_out", False) and key in r
        ]
        return sum(vals) / len(vals) if vals else 0.0

    quality_score = (
        cfg.refine.quality_score_weights.specificity * (m("specificity") / 5)
        + cfg.refine.quality_score_weights.non_obviousness * (m("non_obviousness") / 5)
        + cfg.refine.quality_score_weights.grounding_pct * (m("grounding_pct") / 100)
        + cfg.refine.quality_score_weights.source_diversity * (m("diversity_count") / 5)
    )

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "per_situation": per_situation,
        "aggregate": {
            "specificity_mean": m("specificity"),
            "non_obviousness_mean": m("non_obviousness"),
            "grounding_pct_mean": m("grounding_pct"),
            "diversity_mean": m("diversity_count"),
            "quality_score": quality_score,
        },
        # New top-level fields, additive — existing consumers ignore them.
        "timed_out_count": len(timed_out_ids),
        "timed_out_ids": timed_out_ids,
        "per_fixture_timeout_seconds": per_fixture_timeout_seconds,
    }
    path = out_dir / f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    path.write_text(json.dumps(report, indent=2))
    return path
