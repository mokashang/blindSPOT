# Blindspot — Claude Code Context

Decision-aware advisor for **Chinese international students in the
US making SDE job-hunt and visa-coupled career decisions**. Single
vertical (`cn-sde-jobhunt`); six-agent pipeline (Triage → Collection
→ Community Analysts → Risk Officer → Critic → Editor) that grounds
blind spots in `[doc-X]` citations fetched from a curated source-view
registry.

**Portfolio-track project; target completion 2026-06-01, then
frozen as an archived artifact.** The original V1 → V5 plan for a
universal cross-domain blind-spot tool was scope-narrowed on
2026-05-18; see `docs/specs/ROADMAP.md`. The deprecated 10-domain
content lives under `domain_knowledge/_archive/` for reference.

## Read first

- **Roadmap (current)**: `docs/specs/ROADMAP.md` — V2-narrow /
  V3-ui / V4-freeze plan. 26 sub-tasks across 2 weeks then archive.
- **Design (still load-bearing)**: `docs/specs/2026-05-13-blindspot-v1-design.md`
  — the 6-agent pipeline architecture. The scope-narrow addendum
  at the top marks which sections survived the pivot and which
  did not.
- **Refine skill**: `.claude/skills/refine-blindspot/SKILL.md` +
  `REVIEWER_PROMPT.md` — autonomous refinement loop, rewritten
  for the narrow scope. Hourly schedule is the user's call, not
  the skill's.
- **Domain content**: `domain_knowledge/cn-sde-jobhunt/` — the
  only domain the runtime loads. Schema at
  `domain_knowledge/_schema.md`. Other domains under
  `domain_knowledge/_archive/` are out-of-runtime reference content.
- **Source registry**: `data/source_registry.yaml` — source-views
  for the 4 in-scope communities (一亩三分地, Reddit US tech-career,
  US immigration counsel, China-returnee voices).

## Run

```bash
source .venv/bin/activate
export VOYAGE_API_KEY=...          # required for ask / continue / eval
# Optional (Reddit adapter soft-fails without these):
export REDDIT_CLIENT_ID=... REDDIT_CLIENT_SECRET=...

blindspot ask "<situation>"
# or, if the editable .pth has been corrupted again (see Quirks):
./bin/blindspot ask "<situation>"
```

Other commands: `continue <session_id> <message>`, `history`,
`review`, `rate`, `stats`, `sources {list,gaps,stats}`, `eval`.

## Test

```bash
pytest          # all tests
pytest -q       # quiet
pytest tests/unit/test_<name>.py -v   # one file
```

`pytest` works regardless of editable-install state because
`pyproject.toml` sets `[tool.pytest.ini_options] pythonpath = ["src"]`.

## State locations

- Live SQLite DB: `~/.blindspot/blindspot.db`
- Eval SQLite DB (separate so eval runs don't pollute live history):
  `~/.blindspot/blindspot-eval.db`
- Eval reports: `eval/results/<UTC-timestamp>.json`
- Refine routine log: `refinements/log.jsonl`
- Config: `config.yaml` in the project root (read from cwd by the CLI)

## Architecture (one-liners)

- `cli.py` — typer entry. `_bootstrap_readonly()` vs
  `_bootstrap_full()` split: read-only commands skip building the
  embedder so they don't fail without `VOYAGE_API_KEY`.
- `orchestrator.py` — wires the 6 agents. `run(situation,
  session_id=None)` appends to an existing session if `session_id`
  is provided, otherwise creates a new one.
- `agents/*` — one file per agent role + `base.py` for shared
  helpers (prompt loader, profile loader, doc serializer).
- `sources/` — `base.py` defines `SourceAdapter` + `SourceView`
  dataclass. `registry.py` loads YAML (top-level
  `data/source_registry.yaml` plus
  `domain_knowledge/cn-sde-jobhunt/sources.yaml` once authored).
  `tag_match.py` does weighted scoring + diversity cap.
  `adapters/{rss,reddit_search,hn_search,static_corpus}.py`.
- `tags/taxonomy.py` — embedding-based normalization: new tags
  merge into the nearest existing one (cosine > 0.85) or get
  inserted, with a `TagAuditRow` written in both cases.
- `filters/grounding.py` — parses `[doc-X]` markers;
  `find_unmarked_claims` populates `ungrounded_claims` table for
  the refine routine.
- `db/models.py` — 10 SQLAlchemy 2.x models. `source_view_id`
  columns are STRING slugs referencing the YAML registry, NOT FKs.
- `llm/base.py` — `LLMClient` Protocol + `Embedder` Protocol. Two
  concrete LLM clients: `ClaudeAgentClient` (default, subscription
  via claude-agent-sdk) and `AnthropicAPIClient` (production,
  API key). `_bootstrap_full()` picks one per `config.llm_backend`.
- `eval/judge.py` + `eval/runner.py` — LLM-as-judge over the
  fixture situations; writes aggregated `quality_score` per refine
  signal weights.

## Conventions

- **Language**: English in code / prompts / commits / comments /
  docs (English is the project's lingua franca regardless of the
  CN-student vertical). The Editor agent responds in the user's
  input language — Chinese in → Chinese out, English in → English
  out — but the codebase and all metadata stay English. Chinese is
  fine for chat with the user (see user memory in
  `~/.claude/projects/-Users-moka-Documents-blindspot/memory/`).
- **Git**: push to `origin/main` after every successful commit
  (durable user authorization). Never `--force` push without
  explicit ask.
- **Pre-commit hook**: `.claude/settings.json` configures a
  code-review hook that fires on `git commit` and runs `claude -p`
  on the staged diff. Hook reviews `.py / .ts / .tsx / .js / .jsx
  / .sh / .rs / .go / .java / .c / .cpp / .h / .rb` and lets
  non-code files through. Never bypass (no `--no-verify`, no
  `BLINDSPOT_SKIP_REVIEW=1`).
- **Tests**: TDD for non-trivial logic. Stub LLMs and Embedders
  in tests via the protocols — do NOT make HTTP calls. The
  orchestrator integration test
  (`tests/integration/test_orchestrator.py`) exercises the full
  6-agent pipeline with stubs.
- **Type hints**: pep-604 `X | None` unions, `from __future__ import
  annotations` at the top.
- **Stub LLM routing in tests**: route by `"You are the <Role>"`
  unique opening phrase, NOT by bare role name. The editor prompt
  mentions "Risk Officer" in its body and would false-match a
  bare-name check.

## Scope discipline (post-pivot)

The 2026-05-18 scope narrow is the project's central commitment.
When in doubt, refuse to expand beyond it:

- **In runtime scope**: `cn-sde-jobhunt` only. Triage refuses
  everything else with all-empty arrays; orchestrator emits a
  refusal message.
- **In repo scope**: anything under `domain_knowledge/cn-sde-jobhunt/`,
  `data/`, `fixtures/`, `src/`, `tests/`, `docs/`, `.claude/`
  is live. Anything under `*_archive/` or `archive/*` is
  out-of-runtime reference content; do not load it, do not link
  to it from active prompts, do not edit it.
- **In refine scope**: V2-narrow / V3-ui / V4-freeze checklist
  items only. The refine skill never proposes new vertical
  domains, never edits archived content, never adds dependencies.

When a request would expand the project beyond the sunset
trajectory in `ROADMAP.md`, the right move is to flag the
expansion in chat and ask the user to confirm rather than
silently complying.

## Quirks (real, hit during V1 dev)

- **macOS Python 3.13 silently skips our editable `.pth`.**
  Symptom: `import blindspot` raises `ModuleNotFoundError` even
  though `pip install -e .` reported success and the `.pth` file
  is present with correct content. Root cause: every file pip
  writes under `.venv/` on macOS gets the BSD `UF_HIDDEN` flag
  (visible as the `hidden` column in `ls -lO`). Python 3.13's
  `site.py` was hardened to skip `.pth` files with that flag —
  see `site.py:177` (`st_flags & UF_HIDDEN`). Verify with
  `python -v -c pass 2>&1 | grep blindspot`: you'll see
  `Skipping hidden .pth file: ...`. The `com.apple.provenance`
  xattr rides along on the same files and earlier diagnoses
  pinned the blame on it, but `site.py` doesn't check xattrs
  — only `UF_HIDDEN`. Two fixes:
  - One-shot (must run *after* `pip install`, not before — pip
    re-flags every file it writes): `chflags -R nohidden .venv`.
    Sticks until the next pip operation; macOS does not auto-
    re-apply.
  - Permanent: use `./bin/blindspot` instead of system-PATH
    `blindspot` — the wrapper exports `PYTHONPATH=src` and runs
    `python -m blindspot.cli`, bypassing `.pth` resolution
    entirely.

- **claude-agent-sdk surfaces auth failures as `error result:
  success`.** If the locally cached OAuth refresh token has been
  invalidated server-side (happens silently — token TTL, password
  change, etc.), every `blindspot ask` ends with `Exception:
  Claude Code returned an error result: success` from
  `claude_agent_sdk/_internal/query.py:852`. The word `success`
  is the `subtype` field of the trailing `result` message; the
  SDK's fallback formatter reaches for `subtype` when the
  structured `errors` array is empty, which is wildly misleading.
  The real cause is one layer deeper — capture it with
  `claude -p "hi" --debug-file /tmp/claude.log` and grep
  `oauth\|401\|auth`: you'll see `POST
  https://platform.claude.com/v1/oauth/token → 400` followed by
  `api.anthropic.com/... → 401 authentication_error`. Recovery:
  `claude auth login --claudeai` interactively (browser flow)
  from a real terminal. Don't trust `claude auth status` — it
  reports `loggedIn: true` even while refresh is broken because
  it only checks the local config. Stand-alone `claude -p "hi"`
  is the actual oracle.

- **Reddit adapter constructs PRAW in `__init__`.** Missing
  `REDDIT_CLIENT_ID/SECRET` env vars cause a `KeyError` at adapter
  instantiation. The Collection layer wraps every per-source
  fetch in `try / except` so the turn proceeds without Reddit if
  creds are unset; expect a warning in stderr.

- **Concurrent `./bin/blindspot eval` invocations deadlock under
  the `claude_agent_sdk` backend.** Symptom: two or more `eval`
  runs from sibling worktrees hang at 0% CPU for 15+ minutes
  while a standalone `claude -p "hi"` from the same shell returns
  in ~5s. Root cause: `claude_agent_sdk.query()` spawns a
  subprocess that talks to the local Claude Code CLI; the CLI's
  OAuth / IPC machinery serializes on a single user-home lock or
  socket that doesn't tolerate concurrent callers from sibling
  processes. Escape hatch:
  `BLINDSPOT_LLM_BACKEND=anthropic_api ANTHROPIC_API_KEY=...
  ./bin/blindspot eval` routes through `AnthropicAPIClient` which
  uses direct HTTP and has no subprocess contention. The env var
  overrides `config.yaml`'s `llm_backend` for the current process
  only; a stderr notice prints so it's visible which backend
  you're on. Refine implication: parallel refine subagents can
  finally measure `branch_quality_score` instead of recording
  `eval_status: pipeline-unavailable` indefinitely, once the
  refine routine sets this env var for its eval invocations.

- **1point3acres is hostile to automated scraping.** Their ToS
  forbids it, their bot detection is aggressive, and the
  community deeply values its walled-garden nature. Sources from
  1p3a are therefore loaded as `static_corpus` only — the author
  manually curates representative threads into
  `data/static/oneponethreeacres-curated.md` (similar to how V1
  loaded the Holloway Equity Guide). This is the right call
  ethically and operationally; do not try to automate it. The
  same posture applies to Zhihu (well-known long-form posts get
  copied into `data/static/zhihu-haigui-curated.md`) — Zhihu's
  ToS allows individual citation but forbids systematic scraping.

## Refine routine (autonomous, scope-narrowed)

The skill at `.claude/skills/refine-blindspot/SKILL.md` is written
and scoped to the V2-narrow / V3-ui / V4-freeze checklist in
`ROADMAP.md`. It is NOT yet scheduled — invoke manually via
`/refine-blindspot` from Claude Code first 3-5 times to verify
judgment, then use the `schedule` skill to mount it hourly. The
skill opens a PR per change, auto-reviews it with
`REVIEWER_PROMPT.md` (a separate `claude -p` invocation), and
iterates up to 3 times on rejections before bailing out.

Hard-rejection list (the auto-reviewer always rejects on these):
- `.claude/settings.json`, `.claude/hooks/**`
- The skill files themselves (`SKILL.md`, `REVIEWER_PROMPT.md`)
- Dependency additions in `pyproject.toml`
- Anything under `domain_knowledge/_archive/`, `data/_archive/`,
  `fixtures/_archive/`, `archive/**`
- Tests being deleted
- New vertical domains being added (scope is frozen at
  `cn-sde-jobhunt`)
- Anything outside the V2-narrow / V3-ui / V4-freeze checklist
  in `ROADMAP.md` without an explicit user-authored PR

The skill never schedules itself; that is a user action via the
`schedule` skill or a `scheduled-tasks` MCP entry.

## When in doubt

- Test before committing (`pytest`).
- Read `docs/specs/ROADMAP.md` rather than guess what's in scope.
- For prompt changes, run `blindspot eval` before and after to
  see the delta — this is how the refine routine judges its own
  changes.
- For scope creep, flag in chat and confirm with the user before
  acting.
