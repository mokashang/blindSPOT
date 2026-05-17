"""Tests for the eval runner's per-fixture error handling.

This file specifically guards the contract that a SINGLE fixture's
failure must NOT abort the whole eval run. Two failure modes are
covered today:

1. ``asyncio.TimeoutError`` — the fixture's pipeline or judge hangs;
   the runner records ``timed_out: true`` and continues. (Behavior
   already present pre-PR; not re-tested exhaustively here — there are
   end-to-end eval result files in ``eval/results/`` showing it works.)

2. ``ValueError`` raised by ``llm.claude_agent_client._parse_json_object``
   when the judge LLM returns a string that can't be parsed (typically
   truncated mid-JSON after hitting max_tokens). Pre-PR, this killed
   the whole eval run with ``EVAL_EXIT:1`` and no result file was
   written. Post-PR, the runner records ``judge_unparseable: true`` on
   that fixture and continues. The aggregate ``quality_score`` and
   sub-metric means are computed over only the fixtures that produced
   real verdicts — same rule that already applies to ``timed_out: true``
   rows.

The tests stub ``_run_single_fixture`` to control the per-fixture
outcome deterministically. This is a tighter test than wiring up a
real pipeline (which would need adapters, profiles, registry YAML,
etc.) and exercises the exact branch the bug-report flow hits.
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import pytest

from blindspot.config import Config
from blindspot.eval import runner as runner_mod


class _StubLLM:
    """LLM client that is never called in these tests.

    ``_run_single_fixture`` is monkeypatched in every test below, so
    the real LLM client is never reached. We still need an object
    satisfying the ``LLMClient`` protocol because ``run_eval`` accepts
    one positionally and threads it through.
    """

    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        raise AssertionError(
            "stub LLM should not be called — _run_single_fixture is patched"
        )


class _StubEmbedder:
    async def embed(self, texts):
        raise AssertionError(
            "stub embedder should not be called — _run_single_fixture is patched"
        )


def _write_four_fixtures(root: Path) -> None:
    """Write a 4-fixture legacy YAML at ``<root>/fixtures/eval_situations.yaml``.

    Domain-knowledge directory is intentionally absent so the loader
    takes the V1 fallback path and all four fixtures end up annotated
    with ``domain: "tech-career"``. Order is the order in which the
    runner iterates them, which matters for "raise on the third
    fixture" routing.
    """
    legacy = root / "fixtures" / "eval_situations.yaml"
    legacy.parent.mkdir(parents=True, exist_ok=True)
    legacy.write_text(
        "\n".join(
            [
                "- id: fixture-1",
                "  text: First situation.",
                "- id: fixture-2",
                "  text: Second situation.",
                "- id: fixture-3",
                "  text: Third situation — judge will fail to parse this one.",
                "- id: fixture-4",
                "  text: Fourth situation.",
                "",
            ]
        )
    )


def _make_eval_config(tmp_path: Path) -> Config:
    """Build a Config whose db path is inside tmp_path so eval doesn't touch ~/.blindspot."""
    cfg = Config()
    # run_eval derives ``blindspot-eval.db`` next to ``db.path`` —
    # repoint into tmp_path so a unit-test run never writes the user's
    # live eval db.
    cfg.db.path = str(tmp_path / "blindspot.db")
    return cfg


def _run_eval_in_tmp(tmp_path: Path) -> Path:
    """Helper: chdir into tmp_path, invoke run_eval, return result-file path."""
    import os

    prev_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        cfg = _make_eval_config(tmp_path)
        path = asyncio.run(
            runner_mod.run_eval(
                cfg,
                _StubLLM(),
                _StubEmbedder(),
                fixtures_path=Path("fixtures/eval_situations.yaml"),
                out_dir=tmp_path / "eval_results",
                # Generous so the stubbed _run_single_fixture's
                # instant return / instant raise never trips the
                # timeout branch.
                per_fixture_timeout_seconds=60,
            )
        )
    finally:
        os.chdir(prev_cwd)
    return path


def test_judge_parse_failure_on_one_fixture_does_not_abort_run(
    tmp_path, monkeypatch
):
    """A ValueError from the judge on fixture 3 of 4 must:
    - not raise out of run_eval
    - produce a result file with 4 per-situation entries
    - mark the failing fixture with judge_unparseable=true and quality_score=null
    - leave the aggregate quality_score computed over the 3 successful fixtures
      (matching the existing convention for timed_out rows: skip them entirely
      in the mean, not include them as zeros).
    """
    _write_four_fixtures(tmp_path)

    # Deterministic per-fixture stub. The third fixture (id ``fixture-3``)
    # raises the EXACT ValueError shape that ``_parse_json_object`` in
    # ``claude_agent_client.py`` raises when the judge returns a string
    # whose JSON can't be recovered (truncated mid-object); the other
    # three return a passing rubric.
    async def _stub_run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine):
        if fix["id"] == "fixture-3":
            raise ValueError(
                "could not parse JSON object from model response: "
                "'{\\n  \"cross_community_blind_spots\": [{\"hook\": ...truncated"
            )
        # The other fixtures all score 4/4/100/2. Real ``judge_response``
        # returns ``{**verdict}`` merged with ``{"id": fix["id"]}``; the
        # stub mirrors that shape.
        return {
            "id": fix["id"],
            "specificity": 4,
            "non_obviousness": 4,
            "grounding_pct": 100,
            "diversity_count": 2,
            "feedback": "ok",
        }

    monkeypatch.setattr(
        runner_mod, "_run_single_fixture", _stub_run_single_fixture
    )

    out_path = _run_eval_in_tmp(tmp_path)
    report = json.loads(out_path.read_text())

    # All four fixtures end up in per_situation — no abort, no skip.
    per_situation = report["per_situation"]
    assert len(per_situation) == 4, per_situation
    by_id = {row["id"]: row for row in per_situation}
    assert set(by_id) == {"fixture-1", "fixture-2", "fixture-3", "fixture-4"}

    # The unparseable fixture is recorded honestly.
    bad = by_id["fixture-3"]
    assert bad["judge_unparseable"] is True
    assert bad["quality_score"] is None
    assert bad["timed_out"] is False
    assert "unparseable" in bad["reason"]
    # The reason carries the truncated exception text so a human reading
    # the result file can grep for the specific failure shape.
    assert "could not parse JSON object" in bad["reason"]

    # Top-level summary fields are surfaced for downstream tooling.
    assert report["judge_unparseable_count"] == 1
    assert report["judge_unparseable_ids"] == ["fixture-3"]
    # timed_out_* stays at zero in this scenario.
    assert report["timed_out_count"] == 0
    assert report["timed_out_ids"] == []

    # Aggregate mean is over the 3 non-unparseable rows (4/5, 4/5, 100, 2)
    # — same skip rule as timed_out. With identical scores on all three,
    # the means are exactly the per-row values.
    agg = report["aggregate"]
    assert agg["specificity_mean"] == 4
    assert agg["non_obviousness_mean"] == 4
    assert agg["grounding_pct_mean"] == 100
    assert agg["diversity_mean"] == 2
    # quality_score uses cfg.refine.quality_score_weights defaults:
    # 0.35 * 4/5 + 0.25 * 4/5 + 0.20 * 100/100 + 0.20 * 2/5
    expected_q = 0.35 * (4 / 5) + 0.25 * (4 / 5) + 0.20 * 1.0 + 0.20 * (2 / 5)
    assert agg["quality_score"] == pytest.approx(expected_q)

    # Per-domain block: V1 fallback puts all four fixtures under
    # "tech-career"; fixture_count counts every row (including the
    # unparseable one — same convention as timed_out_count), and the
    # new judge_unparseable_count surfaces the failure.
    pd = report["per_domain"]
    assert set(pd) == {"tech-career"}
    tc = pd["tech-career"]
    assert tc["fixture_count"] == 4
    assert tc["judge_unparseable_count"] == 1
    assert tc["timed_out_count"] == 0
    # Means inside the per-domain block must also skip the bad row.
    assert tc["specificity_mean"] == 4
    assert tc["quality_score"] == pytest.approx(expected_q)


def test_judge_parse_failure_records_json_decode_error_subclass(
    tmp_path, monkeypatch
):
    """A bare ``json.JSONDecodeError`` (subclass of ValueError) from a
    callsite that didn't wrap it must also be caught — defensive.

    ``_parse_json_object`` itself always wraps in a plain ``ValueError``,
    but other LLM callsites in the pipeline could surface
    ``json.JSONDecodeError`` directly; the runner should treat both
    identically.
    """
    _write_four_fixtures(tmp_path)

    async def _stub_run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine):
        if fix["id"] == "fixture-3":
            # Match the exact signature: msg, doc, pos.
            raise json.JSONDecodeError("Expecting value", "not-json", 0)
        return {
            "id": fix["id"],
            "specificity": 3,
            "non_obviousness": 3,
            "grounding_pct": 80,
            "diversity_count": 1,
            "feedback": "ok",
        }

    monkeypatch.setattr(
        runner_mod, "_run_single_fixture", _stub_run_single_fixture
    )

    out_path = _run_eval_in_tmp(tmp_path)
    report = json.loads(out_path.read_text())

    by_id = {row["id"]: row for row in report["per_situation"]}
    assert by_id["fixture-3"]["judge_unparseable"] is True
    assert by_id["fixture-3"]["quality_score"] is None
    assert "unparseable" in by_id["fixture-3"]["reason"]
    assert report["judge_unparseable_count"] == 1
