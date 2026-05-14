# Blindspot — Claude Code Context

Decision-aware advisor surfacing unknown unknowns from curated community
sources. Six-agent pipeline (Triage → Collection → Community Analysts →
Risk Officer → Critic → Editor) that grounds blind spots in `[doc-X]`
citations fetched from a curated source-view registry.

## Read first

- **Design**: `docs/specs/2026-05-13-blindspot-v1-design.md` — the single
  source of truth for what V1 is and why.
- **Plan**: `docs/superpowers/plans/2026-05-13-blindspot-v1.md` — task-by-
  task implementation plan (already executed for V1.0).
- **Refine skill**: `.claude/skills/refine-blindspot/SKILL.md` +
  `REVIEWER_PROMPT.md` — autonomous refinement loop (written, not yet
  scheduled).
- **Source registry**: `data/source_registry.yaml` — 13 curated source-views
  across 8 community tags.
- **Community profiles**: `community_profiles/*.md` — per-community
  analyst voice / mental model / known blind spots. Schema at
  `community_profiles/_schema.md`.

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

Other commands: `continue <session_id> <message>`, `history`, `review`,
`rate`, `stats`, `sources {list,gaps,stats}`, `eval`.

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

- `cli.py` — typer entry. `_bootstrap_readonly()` vs `_bootstrap_full()`
  split: read-only commands skip building the embedder so they don't fail
  without `VOYAGE_API_KEY`.
- `orchestrator.py` — wires the 6 agents. `run(situation, session_id=None)`
  appends to an existing session if `session_id` is provided, otherwise
  creates a new one.
- `agents/*` — one file per agent role + `base.py` for shared helpers
  (prompt loader, profile loader, doc serializer).
- `sources/` — `base.py` defines `SourceAdapter` + `SourceView` dataclass.
  `registry.py` loads the YAML. `tag_match.py` does weighted scoring +
  diversity cap. `adapters/{rss,reddit_search,hn_search,static_corpus}.py`.
- `tags/taxonomy.py` — embedding-based normalization: new tags merge into
  the nearest existing one (cosine > 0.85) or get inserted, with a
  `TagAuditRow` written in both cases.
- `filters/grounding.py` — parses `[doc-X]` markers; `find_unmarked_claims`
  populates `ungrounded_claims` table for the refine routine.
- `db/models.py` — 10 SQLAlchemy 2.x models. `source_view_id` columns are
  STRING slugs referencing `data/source_registry.yaml`, NOT FKs.
- `llm/base.py` — `LLMClient` Protocol + `Embedder` Protocol. Two
  concrete LLM clients: `ClaudeAgentClient` (default, subscription via
  claude-agent-sdk) and `AnthropicAPIClient` (production, API key).
  `_bootstrap_full()` picks one per `config.llm_backend`.
- `eval/judge.py` + `eval/runner.py` — LLM-as-judge over the 12 fixture
  situations; writes aggregated `quality_score` per refine signal weights.

## Conventions

- **Language**: English in code / prompts / commits / comments / docs.
  Chinese is fine for chat with the user (see user memory in
  `~/.claude/projects/-Users-moka-Documents-blindspot/memory/`).
- **Git**: push to `origin/main` after every successful commit (durable
  user authorization). Never `--force` push without explicit ask.
- **Pre-commit hook**: `.claude/settings.json` configures a code-review
  hook that fires on `git commit` and runs `claude -p` on the staged diff.
  Hook reviews `.py / .ts / .tsx / .js / .jsx / .sh / .rs / .go / .java / .c / .cpp / .h / .rb` and lets non-code files through. Never bypass
  (no `--no-verify`, no `BLINDSPOT_SKIP_REVIEW=1`).
- **Tests**: TDD for non-trivial logic. Stub LLMs and Embedders in tests
  via the protocols — do NOT make HTTP calls. The orchestrator
  integration test (`tests/integration/test_orchestrator.py`) exercises
  the full 6-agent pipeline with stubs.
- **Type hints**: pep-604 `X | None` unions, `from __future__ import
  annotations` at the top.
- **Stub LLM routing in tests**: route by `"You are the <Role>"` unique
  opening phrase, NOT by bare role name. The editor prompt mentions
  "Risk Officer" in its body and would false-match a bare-name check.

## Quirks (real, hit during V1 dev)

- **macOS Python 3.13 silently skips our editable `.pth`.** Symptom:
  `import blindspot` raises `ModuleNotFoundError` even though
  `pip install -e .` reported success and the `.pth` file is present
  with correct content. Root cause: every file pip writes under `.venv/`
  on macOS gets the BSD `UF_HIDDEN` flag (visible as the `hidden` column
  in `ls -lO`). Python 3.13's `site.py` was hardened to skip `.pth`
  files with that flag — see `site.py:177` (`st_flags & UF_HIDDEN`).
  Verify with `python -v -c pass 2>&1 | grep blindspot`: you'll see
  `Skipping hidden .pth file: ...`. The `com.apple.provenance` xattr
  rides along on the same files and earlier diagnoses pinned the blame
  on it, but `site.py` doesn't check xattrs — only `UF_HIDDEN`. Two
  fixes:
  - One-shot (must run *after* `pip install`, not before — pip re-flags
    every file it writes): `chflags -R nohidden .venv`. Sticks until
    the next pip operation; macOS does not auto-re-apply.
  - Permanent: use `./bin/blindspot` instead of system-PATH `blindspot`
    — the wrapper exports `PYTHONPATH=src` and runs
    `python -m blindspot.cli`, bypassing `.pth` resolution entirely.

- **claude-agent-sdk surfaces auth failures as `error result: success`.**
  If the locally cached OAuth refresh token has been invalidated
  server-side (happens silently — token TTL, password change, etc.),
  every `blindspot ask` ends with
  `Exception: Claude Code returned an error result: success` from
  `claude_agent_sdk/_internal/query.py:852`. The word `success` is the
  `subtype` field of the trailing `result` message; the SDK's fallback
  formatter reaches for `subtype` when the structured `errors` array is
  empty, which is wildly misleading. The real cause is one layer
  deeper — capture it with
  `claude -p "hi" --debug-file /tmp/claude.log` and grep
  `oauth\|401\|auth`: you'll see `POST
  https://platform.claude.com/v1/oauth/token → 400` followed by
  `api.anthropic.com/... → 401 authentication_error`. Recovery:
  `claude auth login --claudeai` interactively (browser flow) from a
  real terminal. Don't trust `claude auth status` — it reports
  `loggedIn: true` even while refresh is broken because it only checks
  the local config. Stand-alone `claude -p "hi"` is the actual oracle.

- **Reddit adapter constructs PRAW in `__init__`.** Missing
  `REDDIT_CLIENT_ID/SECRET` env vars cause a `KeyError` at adapter
  instantiation. The Collection layer wraps every per-source fetch in
  `try / except` so the turn proceeds without Reddit if creds are unset;
  expect a warning in stderr.

## Refine routine (autonomous)

The skill at `.claude/skills/refine-blindspot/SKILL.md` is written but
NOT scheduled — invoke manually via `/refine-blindspot` from Claude Code
first 3-5 times to verify judgment, then use the `schedule` skill to
mount it hourly. The skill opens a PR per change, auto-reviews it with
`REVIEWER_PROMPT.md` (a separate `claude -p` invocation), and iterates
up to 3 times on rejections before bailing out. Hard-rejection list
includes `.claude/settings.json`, `.claude/hooks/**`, modifications to
`SKILL.md` / `REVIEWER_PROMPT.md` themselves, dependency additions, and
deletions — those always sit for human review.

## When in doubt

- Test before committing (`pytest`).
- Read the spec doc rather than guess design intent.
- For prompt changes, run `blindspot eval` before and after to see the
  delta — this is how the refine routine judges its own changes.
