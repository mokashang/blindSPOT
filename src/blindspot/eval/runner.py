"""Run all eval situations and write a JSON results file."""

from __future__ import annotations

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


async def run_eval(
    cfg: Config,
    llm: LLMClient,
    embedder: Embedder,
    fixtures_path: Path = Path("fixtures/eval_situations.yaml"),
    out_dir: Path = Path("eval/results"),
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    fixtures = yaml.safe_load(fixtures_path.read_text())

    # Eval runs use a separate SQLite file so synthetic sessions, turns,
    # blind_spots, and ungrounded_claims don't pollute the user's live
    # history / ratings.
    eval_cfg = cfg.model_copy(deep=True)
    eval_db_path = Path(cfg.db.path).expanduser().with_name("blindspot-eval.db")
    eval_cfg.db.path = str(eval_db_path)
    init_schema(eval_cfg)
    engine = get_engine(eval_cfg)

    per_situation = []
    for fix in fixtures:
        with Session(engine) as db:
            orch = Orchestrator.create(eval_cfg, llm, embedder, db)
            resp = await orch.run(fix["text"])
        verdict = await judge_response(fix["text"], resp.rendered_markdown, llm, cfg)
        per_situation.append({"id": fix["id"], **verdict})

    def m(key: str) -> float:
        vals = [r[key] for r in per_situation if key in r]
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
    }
    path = out_dir / f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    path.write_text(json.dumps(report, indent=2))
    return path
