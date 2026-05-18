# Blindspot

A decision-aware advisor for **Chinese international students in the US
making SDE job-hunt and visa-coupled career decisions**. Given a
situation (e.g. "I have offers from a FAANG and a Series C startup,
the startup hasn't sponsored before — which is safer for my OPT
expiring next year?"), it runs a 6-agent pipeline that fetches
documents from curated community sources (1point3acres, Reddit
tech-career, US immigration counsel, 海归 voices), has a specialized
analyst per community write their take, has a Risk Officer synthesize
cross-community blind spots, critiques the result, and assembles the
final response with inline `[doc-X]` citations.

> **Portfolio-track project.** Blindspot is a personal tech-showcase
> project, not a product. The scope was narrowed from a universal
> blind-spot tool to this single vertical on 2026-05-18 and the
> project is being completed as a frozen artifact. See
> [`docs/specs/ROADMAP.md`](docs/specs/ROADMAP.md) for the
> 2-week sprint plan and sunset path; see
> [`docs/specs/2026-05-13-blindspot-v1-design.md`](docs/specs/2026-05-13-blindspot-v1-design.md)
> for the original V1 design (note: the scope-narrow addendum at
> the top of that file marks what's still current).

## What's interesting to a reviewer

- **Six-agent pipeline.** Triage → Collection → Community Analysts
  (4, parallel) → Risk Officer → Critic → Editor. Each agent is a
  single async function; specialization lives in system prompts loaded
  from `src/blindspot/prompts/*.md`, not in framework classes.
- **Source grounding by `[doc-X]` citation markers.** Synthesizer
  agents must attach a marker to each substantive claim. The Editor
  parses them; the Critic spot-checks per-claim density. Unmarked
  claims go to `ungrounded_claims` for review.
- **4-layer knowledge model.** Decisions / framings / blindspots /
  source-views. The interesting layer is **blindspots** — what each
  community-framing typically misses. Hand-authored from real
  evidence; this is the moat over generic LLM advice.
- **Autonomous refine loop.** An hourly skill (currently invoked
  manually) reads eval results, picks up to 4 parallel
  refinement attempts, opens PRs reviewed by a *separate* Claude
  session, and merges approved ones. Defined at
  [`.claude/skills/refine-blindspot/SKILL.md`](.claude/skills/refine-blindspot/SKILL.md).
- **LLM-as-judge eval suite.** `./bin/blindspot eval` runs the
  pipeline over fixture situations and produces an aggregate
  `quality_score` that the refine loop optimizes.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

**macOS quirk:** if `import blindspot` fails after install (Python
3.13 + `com.apple.provenance` xattr corruption on the editable
.pth), use `./bin/blindspot` instead of system-PATH `blindspot`,
or add this to your shell rc:

```bash
alias blindspot="cd /Users/moka/Documents/blindspot && PYTHONPATH=src .venv/bin/python -m blindspot.cli"
```

Trade-off: this alias `cd`s into the project dir. If you'd rather
keep cwd, use the function form:

```bash
blindspot() {
    ( cd /Users/moka/Documents/blindspot && PYTHONPATH=src .venv/bin/python -m blindspot.cli "$@" )
}
```

There's also `./bin/blindspot` in the repo as a no-shell-config
option that works from any cwd inside this project.

## Configure

Run commands from the project root — `config.yaml` is read from
`./config.yaml`.

- `llm_backend: claude_agent_sdk` — default. Uses the local
  `claude` CLI subscription. No API key needed.
- `llm_backend: anthropic_api` — production. Requires
  `ANTHROPIC_API_KEY`.

## Environment variables

| Variable | Required for | Why |
|---|---|---|
| `VOYAGE_API_KEY` | `ask`, `continue`, `eval` | embedding-based tag normalization + source matching |
| `ANTHROPIC_API_KEY` | only if `llm_backend: anthropic_api` | direct API access |
| `REDDIT_CLIENT_ID` | Reddit source adapter | PRAW auth |
| `REDDIT_CLIENT_SECRET` | Reddit source adapter | PRAW auth |
| `REDDIT_USER_AGENT` | optional | defaults to `blindspot/0.1 by /u/local` |

Read-only commands (`history`, `review`, `sources list / gaps /
stats`, `stats`) do not require any env var.

## Use

```bash
# One-shot
blindspot ask "I'm a F1 final-year CS PhD, two FAANG offers — Google in MTV vs Meta in NYC; both willing to sponsor. NYC has my partner. Pick?"

# Interactive (will prompt for situation)
blindspot ask

# Continue a past session (adds a turn — same SessionRow)
blindspot continue <session_id> "follow-up question"

# Inspection
blindspot history
blindspot review <session_id>
blindspot rate <session_id> <turn> <blind_spot_idx> <hit|meh|obvious>
blindspot stats

# Sources
blindspot sources list
blindspot sources gaps          # recent ungrounded_claims, signals coverage gaps
blindspot sources stats         # per-source-view performance

# Eval suite (writes eval/results/<timestamp>.json)
blindspot eval
```

State lives at `~/.blindspot/blindspot.db` (live) and
`~/.blindspot/blindspot-eval.db` (eval — kept separate so eval runs
don't pollute your history).

## Develop

```bash
pytest          # all tests
pytest -q       # quiet
```

`pytest` works regardless of editable-install state because
`pyproject.toml` sets `[tool.pytest.ini_options] pythonpath = ["src"]`.

## Auto-refinement

[`.claude/skills/refine-blindspot/SKILL.md`](.claude/skills/refine-blindspot/SKILL.md)
defines an autonomous skill that evaluates the eval suite, picks
concrete improvements to the V2-narrow checklist in `ROADMAP.md`,
opens PRs, auto-reviews them (a separate `claude -p` session per
[`REVIEWER_PROMPT.md`](.claude/skills/refine-blindspot/REVIEWER_PROMPT.md)),
merges approved ones. Manually invokable; not yet scheduled.

The skill is scoped tightly to the V2-narrow roadmap: it does not
propose new domains, does not touch archived content, does not
expand scope beyond the sprint plan.

## What this project does NOT do

Honest limits, intentionally:

- **General-purpose advice.** Triage refuses anything outside
  `cn-sde-jobhunt`. Ask Claude or ChatGPT for general questions.
- **Real-time chat.** Each turn runs the full pipeline; expect
  30–60 seconds per response. The web UI streams the Editor's
  output to make the wait visible.
- **Legal advice.** The Editor explicitly labels visa decisions
  as "decision-support, not legal advice" and routes to a named
  attorney channel for actionable steps.
- **Other student populations.** The community knowledge is
  CN-student-specific. Indian, European, etc. students would
  benefit from the same architecture filled with their own
  community knowledge; this repo is not that.
- **Production reliability.** Single-user local SQLite, no auth,
  no rate limiting, no observability beyond `refinements/log.jsonl`.
