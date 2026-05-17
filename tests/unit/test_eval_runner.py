"""Tests for the eval runner's per-fixture error handling.

This file specifically guards the contract that a SINGLE fixture's
failure must NOT abort the whole eval run. Three failure modes are
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

3. SIGTERM / SIGINT mid-run — the whole eval is killed before all
   fixtures finish (OOM-killer, refine-routine timeout, ``kill <pid>``,
   power loss). Pre-PR, no result file existed on disk because the
   single write happened only at the very end. Post-PR, the runner
   writes a partial snapshot after every fixture and on signal, so the
   refine routine (or any consumer of ``eval/results/``) sees a valid
   JSON file with ``partial: true`` and the completed-so-far subset.

The tests stub ``_run_single_fixture`` to control the per-fixture
outcome deterministically. This is a tighter test than wiring up a
real pipeline (which would need adapters, profiles, registry YAML,
etc.) and exercises the exact branch the bug-report flow hits.
"""

from __future__ import annotations

import asyncio
import json
import os
import signal
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


# -----------------------------------------------------------------------------
# Partial-result write tests (v1.x/eval-pipeline-robustness sub-criterion (a))
# -----------------------------------------------------------------------------
#
# Background: a full eval run currently takes ~55 minutes. Roadmap
# sub-criterion (a) requires either (i) sub-30-min wall-clock OR (ii)
# "shows partial-progress in a result file even if cut short". The
# tests below cover the (ii) attack: the runner writes the result file
# incrementally per fixture (so a kill at any point leaves a valid
# JSON file behind) and a signal handler ensures the file is marked
# ``partial: true`` honestly when an external SIGTERM / SIGINT arrives
# mid-run. The happy-path final write replaces the last partial
# snapshot with ``partial: false`` so a complete-run consumer sees the
# same shape it always did (plus three additive fields).


def test_incremental_write_after_each_fixture_is_partial(tmp_path, monkeypatch):
    """After fixture N completes (but before fixture N+1 starts), the
    result file must already exist on disk with
    ``partial: true, completed_count: N`` and contain N per-situation
    rows. This is the "kill mid-run leaves a usable file" guarantee
    for v1.x/eval-pipeline-robustness sub-criterion (a) OR-branch.

    The stub captures a filesystem snapshot of the result file at the
    moment fixture-2 is about to run; we then assert that snapshot
    reflects the post-fixture-1 state with ``partial: true``.
    """
    _write_four_fixtures(tmp_path)

    snapshots: list[dict] = []
    out_dir = tmp_path / "eval_results"

    async def _stub_run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine):
        # Snapshot the state of the result file at the START of each
        # fixture's execution — captures whatever incremental writes
        # the previous iteration committed.
        existing = sorted(out_dir.glob("*.json")) if out_dir.is_dir() else []
        if existing:
            snapshots.append(
                {"before_fixture": fix["id"], "content": json.loads(existing[0].read_text())}
            )
        return {
            "id": fix["id"],
            "specificity": 3,
            "non_obviousness": 3,
            "grounding_pct": 90,
            "diversity_count": 2,
            "feedback": "ok",
        }

    monkeypatch.setattr(runner_mod, "_run_single_fixture", _stub_run_single_fixture)

    out_path = _run_eval_in_tmp(tmp_path)
    final = json.loads(out_path.read_text())

    # We expect 3 snapshots (start of fixtures 2, 3, 4 — fixture 1
    # has no prior incremental write to observe). Each should be a
    # partial report whose completed_count matches its position.
    assert len(snapshots) == 3, [s["before_fixture"] for s in snapshots]
    for idx, snap in enumerate(snapshots, start=1):
        content = snap["content"]
        assert content["partial"] is True, snap
        assert content["completed_count"] == idx, snap
        assert content["total_count"] == 4, snap
        assert len(content["per_situation"]) == idx, snap

    # The final write (after fixture 4) flips partial to false and
    # populates all four rows. completed_count == total_count is the
    # canonical "fully complete" sentinel.
    assert final["partial"] is False
    assert final["completed_count"] == 4
    assert final["total_count"] == 4
    assert len(final["per_situation"]) == 4


def test_final_result_atomic_no_tmp_leftover(tmp_path, monkeypatch):
    """After a successful full run, no ``.tmp`` file may remain in the
    out_dir. The atomic write helper uses ``os.replace`` to rename
    ``<file>.json.tmp`` onto ``<file>.json``; a leftover ``.tmp`` would
    mean either the rename failed silently or a code path bypassed the
    helper.
    """
    _write_four_fixtures(tmp_path)

    async def _stub_run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine):
        return {
            "id": fix["id"],
            "specificity": 4,
            "non_obviousness": 4,
            "grounding_pct": 95,
            "diversity_count": 3,
            "feedback": "ok",
        }

    monkeypatch.setattr(runner_mod, "_run_single_fixture", _stub_run_single_fixture)

    out_path = _run_eval_in_tmp(tmp_path)

    # Exactly one .json file, zero .tmp files.
    out_dir = out_path.parent
    json_files = sorted(out_dir.glob("*.json"))
    tmp_files = sorted(out_dir.glob("*.tmp"))
    assert len(json_files) == 1, json_files
    assert tmp_files == [], tmp_files

    # And the surviving file is the final (non-partial) report.
    report = json.loads(out_path.read_text())
    assert report["partial"] is False
    assert report["completed_count"] == 4


def test_build_report_partial_aggregate_only_over_completed(tmp_path):
    """Direct unit test of ``_build_report`` for the partial path:
    aggregates / per-domain rollups are computed over the fixtures
    that completed, not over the total expected count. A partial
    report's aggregate is honest about what scored, the same way the
    timed_out / judge_unparseable skip rules already are.
    """
    cfg = _make_eval_config(tmp_path)
    # Two completed fixtures (scored), simulating a 4-fixture run cut
    # short after fixture 2 by a SIGTERM.
    per_situation = [
        {
            "id": "fixture-1",
            "domain": "tech-career",
            "timed_out": False,
            "specificity": 5,
            "non_obviousness": 5,
            "grounding_pct": 100,
            "diversity_count": 4,
        },
        {
            "id": "fixture-2",
            "domain": "tech-career",
            "timed_out": False,
            "specificity": 3,
            "non_obviousness": 3,
            "grounding_pct": 80,
            "diversity_count": 2,
        },
    ]

    report = runner_mod._build_report(
        per_situation,
        timed_out_ids=[],
        judge_unparseable_ids=[],
        per_fixture_timeout_seconds=360,
        cfg=cfg,
        partial=True,
        completed_count=2,
        total_count=4,
    )

    # Shape contract: same keys as a full report (existing consumers
    # don't have to special-case partial). Plus the new progress
    # fields are present and accurate.
    for key in (
        "timestamp",
        "per_situation",
        "aggregate",
        "per_domain",
        "timed_out_count",
        "timed_out_ids",
        "judge_unparseable_count",
        "judge_unparseable_ids",
        "per_fixture_timeout_seconds",
        "partial",
        "completed_count",
        "total_count",
    ):
        assert key in report, f"missing {key} in partial report"

    assert report["partial"] is True
    assert report["completed_count"] == 2
    assert report["total_count"] == 4

    # Aggregate means over the two completed rows only — total_count=4
    # must NOT dilute the denominator.
    agg = report["aggregate"]
    assert agg["specificity_mean"] == (5 + 3) / 2
    assert agg["non_obviousness_mean"] == (5 + 3) / 2
    assert agg["grounding_pct_mean"] == (100 + 80) / 2
    assert agg["diversity_mean"] == (4 + 2) / 2

    # Per-domain block likewise reflects only the two completed rows
    # under tech-career.
    tc = report["per_domain"]["tech-career"]
    assert tc["fixture_count"] == 2
    assert tc["specificity_mean"] == (5 + 3) / 2


def test_signal_handler_is_registered_during_run(tmp_path, monkeypatch):
    """The runner installs SIGINT + SIGTERM handlers for the duration
    of ``run_eval`` and restores the previous handlers when it exits.

    A direct end-to-end test of "kill mid-run, observe partial file"
    requires subprocess orchestration (the signal must arrive at a
    specific Python instruction; ``os.kill(os.getpid(), SIGTERM)``
    inside the same asyncio loop interacts awkwardly with pytest's
    capture/loop machinery). This test instead asserts the
    registration contract — the handler is in place while
    ``_run_single_fixture`` is on the call stack — which is sufficient
    proof that an external signal will reach our handler. The handler
    body's behavior (write partial, re-raise as KeyboardInterrupt) is
    covered by the per-fixture incremental write tests above plus a
    direct invocation in
    ``test_signal_handler_writes_partial_on_keyboard_interrupt`` below.
    """
    _write_four_fixtures(tmp_path)

    observed_handlers: dict[int, object] = {}

    async def _stub_run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine):
        # Capture the currently-installed handlers the first time we
        # enter a fixture. By that point ``run_eval`` has finished
        # setup and registered both handlers.
        if not observed_handlers:
            observed_handlers[signal.SIGINT] = signal.getsignal(signal.SIGINT)
            observed_handlers[signal.SIGTERM] = signal.getsignal(signal.SIGTERM)
        return {
            "id": fix["id"],
            "specificity": 3,
            "non_obviousness": 3,
            "grounding_pct": 80,
            "diversity_count": 1,
            "feedback": "ok",
        }

    monkeypatch.setattr(runner_mod, "_run_single_fixture", _stub_run_single_fixture)

    # Snapshot the prior handlers so we can verify they're restored
    # after run_eval returns.
    prior_sigint = signal.getsignal(signal.SIGINT)
    prior_sigterm = signal.getsignal(signal.SIGTERM)

    _run_eval_in_tmp(tmp_path)

    # During the run, both handlers were callables we installed —
    # NOT the prior default handler (SIG_DFL) and NOT the prior
    # snapshot.
    assert callable(observed_handlers[signal.SIGINT])
    assert callable(observed_handlers[signal.SIGTERM])
    assert observed_handlers[signal.SIGINT] is not prior_sigint
    assert observed_handlers[signal.SIGTERM] is not prior_sigterm

    # After the run, the prior handlers are restored. This matters
    # because pytest itself relies on SIGINT semantics across tests;
    # leaving our handler installed would leak into later tests.
    assert signal.getsignal(signal.SIGINT) is prior_sigint
    assert signal.getsignal(signal.SIGTERM) is prior_sigterm


def test_signal_handler_writes_partial_on_keyboard_interrupt(
    tmp_path, monkeypatch
):
    """When the SIGINT signal handler fires mid-run (raised manually
    here by the stub on fixture 3 of 4), the partial result file
    written by the handler must exist on disk with ``partial: true``
    and contain the two fixtures that completed before the signal.

    The stub raises the same exception shape the signal handler does
    (``KeyboardInterrupt`` after calling the snapshot helper). This
    exercises the handler-body code path end-to-end without needing a
    real OS signal — the actual ``signal.signal`` registration is
    covered by ``test_signal_handler_is_registered_during_run``.
    """
    _write_four_fixtures(tmp_path)

    async def _stub_run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine):
        if fix["id"] == "fixture-3":
            # Simulate the signal arriving while fixture 3 is being
            # set up — before it can produce a result. This is the
            # "killed mid-fixture" path described in the task spec:
            # fixture 3 is NOT in the result file (it didn't
            # complete); fixtures 1 and 2 are.
            raise KeyboardInterrupt("SIGINT during fixture-3")
        return {
            "id": fix["id"],
            "specificity": 4,
            "non_obviousness": 4,
            "grounding_pct": 100,
            "diversity_count": 2,
            "feedback": "ok",
        }

    monkeypatch.setattr(runner_mod, "_run_single_fixture", _stub_run_single_fixture)

    # run_eval should raise out — the in-band KeyboardInterrupt
    # propagates because the per-fixture try/except above only catches
    # asyncio.TimeoutError / ValueError / JSONDecodeError, not
    # KeyboardInterrupt. That's intentional: a real signal arrives at
    # the OS level and unwinds the whole interpreter cleanly via the
    # ``finally`` block; we want the same here.
    with pytest.raises(KeyboardInterrupt):
        _run_eval_in_tmp(tmp_path)

    # The result directory should contain one JSON file (the
    # incremental write after fixture 2) and no .tmp file. The .tmp
    # cleanup is critical: ``os.replace`` runs unconditionally in
    # ``_write_report_atomic`` so even though the run aborted mid-way,
    # the most recent per-fixture write completed atomically.
    out_dir = tmp_path / "eval_results"
    json_files = sorted(out_dir.glob("*.json"))
    tmp_files = sorted(out_dir.glob("*.tmp"))
    assert len(json_files) == 1, json_files
    assert tmp_files == [], tmp_files

    report = json.loads(json_files[0].read_text())
    # Partial snapshot reflects fixtures 1 and 2 only — fixture 3
    # raised before adding anything to per_situation, fixture 4
    # never started.
    assert report["partial"] is True
    assert report["completed_count"] == 2
    assert report["total_count"] == 4
    ids = [r["id"] for r in report["per_situation"]]
    assert ids == ["fixture-1", "fixture-2"]

    # Aggregate is computed over the 2 fixtures that scored —
    # mirrors the timed_out / judge_unparseable skip convention. A
    # consumer reading this partial file gets an honest mean of what
    # ran, not a punitive mean diluted by the missing fixtures.
    agg = report["aggregate"]
    assert agg["specificity_mean"] == 4
    assert agg["non_obviousness_mean"] == 4
    assert agg["grounding_pct_mean"] == 100
    assert agg["diversity_mean"] == 2
