# Blindspot

Decision-aware advisor surfacing unknown unknowns from curated community sources.

Given a decision (job offer, equity package, etc.) the CLI runs a 6-agent
pipeline that fetches documents from curated community source-views, has a
specialized analyst per community write their take, has a Risk Officer
synthesize the cross-community blind spots, critiques the result, and
assembles the final response with inline `[doc-X]` citations.

Full design: `docs/specs/2026-05-13-blindspot-v1-design.md`.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

**macOS quirk:** if `import blindspot` fails after install (Python 3.13 +
`com.apple.provenance` xattr corruption on the editable .pth), strip the
xattrs and reinstall:

```bash
xattr -cr .venv && pip install -e ".[dev]" --force-reinstall --no-deps
```

This may also need to be re-run after adding new modules under
`src/blindspot/`.

## Configure

Run commands from the project root — `config.yaml` is read from `./config.yaml`.

Adjust `config.yaml` if needed:

- `llm_backend: claude_agent_sdk` — default. Goes through your local
  `claude` CLI subscription. No API key needed.
- `llm_backend: anthropic_api` — production. Requires `ANTHROPIC_API_KEY`.

## Environment variables

Set in your shell (or a `.env` file you source):

| Variable | Required for | Why |
|---|---|---|
| `VOYAGE_API_KEY` | `ask`, `continue`, `eval` | embedding-based tag normalization + source matching |
| `ANTHROPIC_API_KEY` | only if `llm_backend: anthropic_api` | direct API access |
| `REDDIT_CLIENT_ID` | Reddit source adapter | PRAW auth |
| `REDDIT_CLIENT_SECRET` | Reddit source adapter | PRAW auth |
| `REDDIT_USER_AGENT` | optional | defaults to `blindspot/0.1 by /u/local` |

If Reddit credentials are unset, the Reddit adapter soft-fails — the system
runs without Reddit sources. The other read-only commands (`history`,
`review`, `sources list / gaps / stats`, `stats`) do not require any
environment variable.

## Use

```bash
# One-shot
blindspot ask "I got a Series B offer with 0.1% in ISOs..."

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

# Eval suite (12 fixture situations, writes eval/results/<ts>.json)
blindspot eval
```

State lives at `~/.blindspot/blindspot.db` (live) and
`~/.blindspot/blindspot-eval.db` (eval — kept separate so eval runs don't
pollute your history).

## Develop

```bash
pytest
```

## Auto-refinement

`.claude/skills/refine-blindspot/SKILL.md` defines an autonomous skill that
evaluates the eval suite, picks one concrete improvement, opens a PR,
auto-reviews it (with another Claude session per
`.claude/skills/refine-blindspot/REVIEWER_PROMPT.md`), merges or holds.
Manually invokable; not yet scheduled.
