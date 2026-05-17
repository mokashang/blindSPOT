"""Run all eval situations and write a JSON results file."""

from __future__ import annotations

import asyncio
import json
import os
import signal
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.session import get_engine, init_schema
from blindspot.eval.judge import judge_response
from blindspot.llm.base import Embedder, LLMClient
from blindspot.orchestrator import Orchestrator

# V1 domain name used to annotate fixtures loaded from the legacy
# monolithic file. The migration from `fixtures/eval_situations.yaml`
# to `domain_knowledge/tech-career/fixtures/*.yaml` is tracked as a
# separate roadmap item (v2/tech-career/fixtures); until that migration
# lands, every V1 fixture is treated as belonging to this domain so
# per-domain aggregation has a stable bucket.
V1_LEGACY_DOMAIN = "tech-career"

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
#
# Empirical calibration: the eval at eval/results/20260517T131728Z.json
# (run with --per-fixture-timeout 180) had 8 of 15 fixtures hit the cap.
# 240s offered modest headroom but the data shows genuinely-slow
# fixtures need more than that. 360s gives the slow fixtures room to
# complete without padding the fast ones (which complete in well under
# the cap regardless). Trade-off: worst-case wall-clock per eval grows
# from 8*180 = 1440s of waited-then-discarded work to 8*360 = 2880s if
# none of the slow fixtures rescue from the higher cap; if rescues
# happen, wall-clock per fixture-completed drops.
DEFAULT_PER_FIXTURE_TIMEOUT_SECONDS = 360


def _coerce_fixture_payload(raw) -> list[dict]:
    """Normalize a parsed YAML fixture file into a list of fixture dicts.

    A fixture YAML file may contain either a single fixture (top-level
    mapping with at minimum ``id`` and ``text``) or a list of such
    fixtures — both shapes are produced by hand-written authors and
    must be supported transparently. Returns ``[]`` when the file
    parses to ``None`` (empty / comments-only).
    """
    if raw is None:
        return []
    if isinstance(raw, list):
        return list(raw)
    if isinstance(raw, dict):
        return [raw]
    raise ValueError(
        f"fixture YAML must be a list or mapping, got {type(raw).__name__}"
    )


def load_all_fixtures(
    root: Path | str = ".",
    legacy_path: Path | str = "fixtures/eval_situations.yaml",
) -> list[dict]:
    """Load eval fixtures, preferring per-domain YAML over the legacy monolithic file.

    Lookup order (V2 preferred, V1 fallback during migration — same
    architectural pattern as
    ``blindspot.sources.registry.load_all_sources``):

    1. Glob ``<root>/domain_knowledge/<domain>/fixtures/*.yaml`` where
       ``<domain>`` is any subdirectory whose name does NOT start with
       ``_`` (excludes ``_meta_*`` / ``_schema.md`` style scaffolding).
       Every match is loaded; each fixture dict is annotated with a
       ``domain`` key set to the parent folder name. Domains and files
       are iterated in sorted order for deterministic output.
    2. If no per-domain fixture files are found, fall back to
       ``<root>/<legacy_path>`` — the V1 monolithic file. Each fixture
       loaded from there is annotated with ``domain: "tech-career"``
       (V1's only domain).

    Bit-for-bit V1 preservation: when no per-domain files exist,
    ``load_all_fixtures()`` returns exactly the same list of dicts as
    the prior inline ``yaml.safe_load(fixtures_path.read_text())`` call
    in ``run_eval``, with one added key per dict (``domain``). The
    ``domain`` key is purely additive — existing consumers (``judge_response``,
    ``_run_single_fixture``) only read ``id`` and ``text`` and never
    inspect ``domain``, so V1 behavior is preserved.

    If BOTH layouts exist, V2 wins and a one-line warning naming the
    shadowed V1 file is printed to stderr.
    """
    root_path = Path(root)
    domain_knowledge_dir = root_path / "domain_knowledge"

    per_domain_files: list[tuple[str, Path]] = []
    if domain_knowledge_dir.is_dir():
        for child in sorted(domain_knowledge_dir.iterdir()):
            # Only scan real domain subdirectories — skip files (e.g.
            # ``_schema.md``) and underscored scaffolding directories
            # (``_meta_ontology``, etc.).
            if not child.is_dir():
                continue
            if child.name.startswith("_"):
                continue
            fixtures_dir = child / "fixtures"
            if not fixtures_dir.is_dir():
                continue
            for fx_file in sorted(fixtures_dir.glob("*.yaml")):
                per_domain_files.append((child.name, fx_file))

    legacy_full_path = root_path / legacy_path

    if per_domain_files:
        if legacy_full_path.is_file():
            print(
                f"warning: per-domain fixtures take precedence; "
                f"shadowing legacy {legacy_full_path}",
                file=sys.stderr,
            )
        fixtures: list[dict] = []
        for domain_name, fx_file in per_domain_files:
            with open(fx_file) as fh:
                raw = yaml.safe_load(fh)
            for fx in _coerce_fixture_payload(raw):
                fx = dict(fx)  # don't mutate caller's parsed structure
                fx["domain"] = domain_name
                fixtures.append(fx)
        return fixtures

    # V1 fallback — no per-domain fixture files found.
    if not legacy_full_path.is_file():
        return []
    raw = yaml.safe_load(legacy_full_path.read_text())
    fixtures = []
    for fx in _coerce_fixture_payload(raw):
        fx = dict(fx)
        fx["domain"] = V1_LEGACY_DOMAIN
        fixtures.append(fx)
    return fixtures


def _write_report_atomic(path: Path, report: dict) -> None:
    """Write ``report`` to ``path`` atomically.

    Concrete steps: dump JSON to ``<path>.tmp`` then ``os.replace()`` it
    onto ``path``. ``os.replace`` is atomic on POSIX (and on NTFS in
    practice) so a concurrent reader can never observe a half-written
    file — they either see the previous full snapshot or the new full
    snapshot. The ``.tmp`` file never lingers after a successful run.
    """
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(report, indent=2))
    os.replace(tmp, path)


def _build_report(
    per_situation: list[dict],
    timed_out_ids: list[str],
    judge_unparseable_ids: list[str],
    per_fixture_timeout_seconds: int,
    cfg: Config,
    *,
    partial: bool,
    completed_count: int,
    total_count: int,
) -> dict:
    """Assemble the eval result dict from accumulated per-situation rows.

    Same shape whether ``partial`` is ``True`` (eval was cut short) or
    ``False`` (full run completed). Aggregates and per-domain rollups
    are computed over the records present in ``per_situation`` at call
    time — for partial reports this is the subset that ran to a verdict
    before interruption; for a final report this is every fixture. The
    ``partial`` / ``completed_count`` / ``total_count`` fields let a
    consumer distinguish the two modes without inspecting list lengths.
    """

    def _mean_for(records: list[dict], key: str) -> float:
        # Aggregate only over fixtures that produced a real verdict —
        # timed-out and judge-unparseable fixtures don't have rubric
        # scores so including them as zeros would falsely lower the
        # mean. Both error paths set ``quality_score: null`` upstream;
        # the same skip rule applies symmetrically here so the
        # refine-routine delta math sees the average of fixtures that
        # actually scored, not a punitive average diluted by failures.
        vals = [
            r[key]
            for r in records
            if not r.get("timed_out", False)
            and not r.get("judge_unparseable", False)
            and key in r
        ]
        return sum(vals) / len(vals) if vals else 0.0

    def _quality_score_for(records: list[dict]) -> float:
        # Same weighted formula the global aggregate uses, just scoped
        # to a subset of per_situation records.
        return (
            cfg.refine.quality_score_weights.specificity
            * (_mean_for(records, "specificity") / 5)
            + cfg.refine.quality_score_weights.non_obviousness
            * (_mean_for(records, "non_obviousness") / 5)
            + cfg.refine.quality_score_weights.grounding_pct
            * (_mean_for(records, "grounding_pct") / 100)
            + cfg.refine.quality_score_weights.source_diversity
            * (_mean_for(records, "diversity_count") / 5)
        )

    # Global aggregate — UNCHANGED behavior for a complete run. Scoped
    # to whatever records exist for a partial run (mean over what we
    # got, not what we expected).
    quality_score = _quality_score_for(per_situation)

    # Per-domain aggregate — additive, same sub-metric computation as
    # the global block, scoped per domain bucket. Lets the refine
    # routine spot regressions in one domain that a global mean would
    # mask once V2 spans more than one domain.
    domains_seen: list[str] = []
    domain_records: dict[str, list[dict]] = {}
    for r in per_situation:
        d = r.get("domain", V1_LEGACY_DOMAIN)
        if d not in domain_records:
            domain_records[d] = []
            domains_seen.append(d)
        domain_records[d].append(r)

    per_domain: dict[str, dict] = {}
    for d in domains_seen:
        recs = domain_records[d]
        per_domain[d] = {
            "specificity_mean": _mean_for(recs, "specificity"),
            "non_obviousness_mean": _mean_for(recs, "non_obviousness"),
            "grounding_pct_mean": _mean_for(recs, "grounding_pct"),
            "diversity_mean": _mean_for(recs, "diversity_count"),
            "quality_score": _quality_score_for(recs),
            "fixture_count": len(recs),
            "timed_out_count": sum(1 for r in recs if r.get("timed_out", False)),
            "judge_unparseable_count": sum(
                1 for r in recs if r.get("judge_unparseable", False)
            ),
        }

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "per_situation": per_situation,
        "aggregate": {
            "specificity_mean": _mean_for(per_situation, "specificity"),
            "non_obviousness_mean": _mean_for(per_situation, "non_obviousness"),
            "grounding_pct_mean": _mean_for(per_situation, "grounding_pct"),
            "diversity_mean": _mean_for(per_situation, "diversity_count"),
            "quality_score": quality_score,
        },
        "per_domain": per_domain,
        # Top-level summary / progress fields. ``timed_out_*`` and
        # ``judge_unparseable_*`` are existing; ``partial`` /
        # ``completed_count`` / ``total_count`` are new and let a
        # consumer distinguish "killed mid-run" from "successful
        # complete run" without comparing list lengths.
        "timed_out_count": len(timed_out_ids),
        "timed_out_ids": timed_out_ids,
        "judge_unparseable_count": len(judge_unparseable_ids),
        "judge_unparseable_ids": judge_unparseable_ids,
        "per_fixture_timeout_seconds": per_fixture_timeout_seconds,
        "partial": partial,
        "completed_count": completed_count,
        "total_count": total_count,
    }


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
        print(f"[eval]   {fix['id']}: orchestrator.create", flush=True)
        orch = Orchestrator.create(eval_cfg, llm, embedder, db)
        print(f"[eval]   {fix['id']}: orch.run", flush=True)
        resp = await orch.run(fix["text"])
    print(f"[eval]   {fix['id']}: judge_response", flush=True)
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

    The same continue-on-error contract applies when the judge LLM
    returns a string that ``_parse_json_object`` cannot recover
    (typically a truncated response that hit max_tokens mid-JSON,
    leaving an unclosed string literal). The fixture's record carries
    `quality_score: null`, `judge_unparseable: true`, a `reason` that
    contains the first 200 chars of the exception message, and the run
    continues. Aggregates (`quality_score`, sub-metric means, per-domain
    block) skip these rows the same way they skip `timed_out: true`
    rows so a single parse failure doesn't poison the running mean.
    """
    print(
        f"[eval] starting; fixtures_path={fixtures_path} out_dir={out_dir} "
        f"timeout={per_fixture_timeout_seconds}s",
        flush=True,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    # V2-first / V1-fallback fixture discovery. The ``fixtures_path``
    # kwarg is retained for backward compatibility — it sets the
    # legacy fallback file used when no per-domain fixtures exist.
    # When per-domain `domain_knowledge/<domain>/fixtures/*.yaml` files
    # are present, they take precedence and the legacy path is ignored
    # (with a stderr warning). Each loaded fixture carries an added
    # ``domain`` key, used purely for the per-domain aggregation block
    # below; the existing pipeline / judge call still only inspects
    # ``id`` and ``text``.
    fixtures = load_all_fixtures(root=Path("."), legacy_path=fixtures_path)
    print(
        f"[eval] loaded {len(fixtures)} fixtures: "
        f"{[(f['id'], f.get('domain')) for f in fixtures]}",
        flush=True,
    )

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
    print(f"[eval] init_schema + engine ready (db={eval_db_path})", flush=True)

    per_situation: list[dict] = []
    timed_out_ids: list[str] = []
    judge_unparseable_ids: list[str] = []
    total_count = len(fixtures)

    # Pin the result-file path up front so every incremental write
    # lands in the SAME file. Previously the timestamp was sampled at
    # the very end of the run; now we need a stable target so that a
    # SIGTERM mid-run can write a partial snapshot that a later reader
    # (the refine routine, an operator, or a sibling eval invocation)
    # can still locate by `ls -t eval/results/`.
    path = out_dir / f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"

    # Signal-handler plumbing. The handler MUST be lightweight (signal
    # handlers run in the main thread and can re-enter arbitrary code);
    # we just flip a flag and write whatever snapshot we have on hand,
    # then re-raise the default behavior. Two reasons to write here
    # rather than relying solely on the per-fixture writes:
    #
    # 1. SIGTERM may arrive *between* fixtures, after the per-fixture
    #    write already happened — that's fine, but the flag-flip
    #    ensures we mark ``partial: true`` honestly even if the
    #    last-fixture write happened to land moments before the
    #    signal.
    # 2. SIGINT (Ctrl-C) from a developer or a wrapper script needs
    #    the same treatment — they want the partial snapshot too.
    #
    # The handler is registered only when running on the main thread
    # of the main interpreter (Python's signal module raises
    # ``ValueError`` otherwise — e.g. when run_eval is invoked from a
    # worker thread under pytest). The try/except below makes the
    # signal path opt-in but the per-fixture incremental writes still
    # fire in every environment.
    _state = {"interrupted": False}

    def _snapshot_partial() -> None:
        report_partial = _build_report(
            per_situation,
            timed_out_ids,
            judge_unparseable_ids,
            per_fixture_timeout_seconds,
            cfg,
            partial=True,
            completed_count=len(per_situation),
            total_count=total_count,
        )
        _write_report_atomic(path, report_partial)

    def _on_signal(signum, frame):  # noqa: ARG001 — signal-handler signature
        _state["interrupted"] = True
        try:
            _snapshot_partial()
            print(
                f"[eval] received signal {signum}; wrote partial result: "
                f"{path} ({len(per_situation)}/{total_count} fixtures)",
                flush=True,
            )
        finally:
            # Re-raise as KeyboardInterrupt so the asyncio event loop
            # unwinds cleanly. SIGTERM normally terminates immediately;
            # converting to KeyboardInterrupt lets the ``finally``
            # blocks in any in-flight orchestrator code run.
            raise KeyboardInterrupt(
                f"eval interrupted by signal {signum}; partial result at {path}"
            )

    previous_handlers: dict[int, object] = {}
    for _sig in (signal.SIGINT, signal.SIGTERM):
        try:
            previous_handlers[_sig] = signal.signal(_sig, _on_signal)
        except (ValueError, OSError):
            # Not on main thread (pytest worker, threaded host, etc.)
            # or signal not supported on this platform — fall back to
            # per-fixture incremental writes only.
            pass

    try:
        for i, fix in enumerate(fixtures):
            print(
                f"[eval] fixture {i+1}/{total_count} start: {fix['id']}",
                flush=True,
            )
            domain = fix.get("domain", V1_LEGACY_DOMAIN)
            try:
                result = await asyncio.wait_for(
                    _run_single_fixture(fix, eval_cfg, cfg, llm, embedder, engine),
                    timeout=per_fixture_timeout_seconds,
                )
                # Existing fields preserved; explicitly mark non-timed-out
                # records so downstream tooling never has to disambiguate
                # "missing" from "false". ``domain`` carried through so the
                # per-domain aggregation block can group below.
                result["timed_out"] = False
                result["domain"] = domain
                per_situation.append(result)
                print(
                    f"[eval] fixture {i+1}/{total_count} done: {fix['id']} "
                    f"timed_out={result.get('timed_out', False)}",
                    flush=True,
                )
            except asyncio.TimeoutError:
                timed_out_ids.append(fix["id"])
                per_situation.append(
                    {
                        "id": fix["id"],
                        "domain": domain,
                        "timed_out": True,
                        "timeout_seconds": per_fixture_timeout_seconds,
                        "quality_score": None,
                        "reason": (
                            f"fixture exceeded {per_fixture_timeout_seconds}s timeout "
                            f"(pipeline or judge hung)"
                        ),
                    }
                )
                print(
                    f"[eval] fixture {i+1}/{total_count} done: {fix['id']} "
                    f"timed_out=True",
                    flush=True,
                )
            except (ValueError, json.JSONDecodeError) as exc:
                # Judge LLM (or any pipeline LLM call) returned a string the
                # ``_parse_json_object`` recovery couldn't repair — typically
                # a truncated response that hit max_tokens mid-JSON, leaving
                # an unclosed string literal that the ``last_close_brace``
                # fallback can't recover from. Before this branch, any such
                # ValueError aborted the whole eval run with EVAL_EXIT:1 and
                # no result file was written; now we record the parse failure
                # honestly on this fixture and continue, mirroring the
                # asyncio.TimeoutError handling above. We catch the bare
                # ``ValueError`` because that is what ``_parse_json_object``
                # raises (it wraps the underlying ``json.JSONDecodeError``);
                # ``json.JSONDecodeError`` is included defensively in case
                # other callsites surface it directly. ``JSONDecodeError`` is
                # itself a ``ValueError`` subclass, so listing it second is
                # only documentation — the order matches the bug-report flow.
                judge_unparseable_ids.append(fix["id"])
                per_situation.append(
                    {
                        "id": fix["id"],
                        "domain": domain,
                        "timed_out": False,
                        "judge_unparseable": True,
                        "quality_score": None,
                        "reason": (
                            f"judge response unparseable: {str(exc)[:200]}"
                        ),
                    }
                )
                print(
                    f"[eval] fixture {i+1}/{total_count} done: {fix['id']} "
                    f"judge_unparseable=True",
                    flush=True,
                )

            # Incremental write: after every fixture (K=1) the result
            # file reflects the completed-so-far set with
            # ``partial: true``. If eval is killed (SIGTERM, OOM,
            # power loss) the file already on disk is a valid partial
            # snapshot — the refine routine reading
            # ``ls -t eval/results/`` will see it and know to
            # interpret it via ``partial``/``completed_count``. This
            # closes the OR-branch of v1.x/eval-pipeline-robustness
            # sub-criterion (a): "shows partial-progress in a result
            # file even if cut short".
            _snapshot_partial()

        print(f"[eval] all fixtures done; computing aggregate", flush=True)

        # Final write: ``partial: false``, ``completed_count == total_count``.
        # Atomic replace means the file's previous (partial) snapshot
        # is overwritten as a single filesystem operation — no
        # ``.tmp`` leftover, no half-written state visible to readers.
        report = _build_report(
            per_situation,
            timed_out_ids,
            judge_unparseable_ids,
            per_fixture_timeout_seconds,
            cfg,
            partial=False,
            completed_count=len(per_situation),
            total_count=total_count,
        )
        print(f"[eval] writing result file: {path}", flush=True)
        _write_report_atomic(path, report)
        print(
            f"[eval] wrote result file: {path}; "
            f"quality_score={report['aggregate']['quality_score']:.4f}",
            flush=True,
        )
        return path
    finally:
        # Restore prior signal handlers regardless of how we exit
        # (normal return, exception, KeyboardInterrupt from the
        # signal handler). This matters when run_eval is invoked
        # repeatedly in the same process (the CLI does this once per
        # invocation, but pytest invokes it many times in a single
        # interpreter — leaving our handler installed would break
        # other tests' SIGINT semantics).
        for _sig, _prev in previous_handlers.items():
            try:
                signal.signal(_sig, _prev)
            except (ValueError, OSError):
                pass
