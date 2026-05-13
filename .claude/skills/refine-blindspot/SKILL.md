---
name: refine-blindspot
description: One iteration of autonomous refinement on the Blindspot project. Evaluate the previous change, decide a concrete direction, apply within scope, verify, log, commit (or open a PR). Designed to run hourly via the `schedule` skill once trust is established — but ALWAYS invokable manually. The skill never schedules itself; that is a user action.
---

# Refine Blindspot

You are running one iteration of refinement on the Blindspot project. The
loop is: read state → evaluate previous change → decide direction → apply →
verify → log → commit (or open PR). Stay strictly within the scope tiers
defined below. The user trusts this skill because of those tiers, not in
spite of them.

## Step 1 — Read state

Use Bash + Read to collect:

- Last 30 entries of `git log --oneline` to see what changed recently
- Last 10 entries of `refinements/log.jsonl` (most recent first)
- The most recent file in `eval/results/*.json`
- The eval result from immediately before the most recent (for delta math)
- If it exists, `data/feedback.jsonl` (real user ratings, post-V1)

Build a short mental summary:
- What did the last refinement run change?
- What signal delta did it predict?
- What is the current eval score?
- Are there clusters in recent `ungrounded_claims` rows?

If `refinements/log.jsonl` is empty or missing, this is a **BASELINE** run:
skip Step 2 and pick any concrete improvement to start the loop.

## Step 2 — Evaluate the previous change

Compare the predicted `expected_signal_delta` (from the last log entry) to
the actual delta computed from eval scores. Classify:

- **POSITIVE** — actual delta has the same sign and similar magnitude to predicted
- **NEUTRAL** — `|actual_delta| < 0.02` on the aggregate quality_score (below noise)
- **NEGATIVE** — actual delta is opposite sign to predicted, OR much smaller than predicted

## Step 3 — Decide direction

Cycle through these four dimensions in order. For each, ask: "Is there a
*specific* and *concrete* improvement available here right now?" Stop at
the first yes.

1. **Prompt clarity** — Look at the lowest-scoring eval situation. Read
   the prompts of the agents that handled it. Find one specific ambiguity
   or missing instruction.

2. **Coverage gaps** — Check `ungrounded_claims` rows from recent turns.
   Group by topic. Is there a cluster pointing at a topic that no current
   source-view covers? (If yes, plan a 🟡 PR to add a source-view.)

3. **Signal-to-noise** — Check `source_view_stats`. Are any source-views
   consistently producing low-rated blind spots? Consider lowering their
   `reliability` field (🟢 direct edit) or improving the `keyword_filter`.

4. **Failure-mode patterns** — Look at the critic's recent feedback strings.
   Are there recurring categories (e.g. "too generic", "no concrete
   numbers", "missing citations")? The fix usually goes into the agent's
   system prompt.

Pick **ONE** concrete change. Examples of acceptable concreteness:

- "Edit `community_profiles/reddit-tech-collective.md`: add to 'Known
  blind spots' that this community over-indexes on quitting as a default
  response."
- "Edit `config.yaml`: bump `entity_weight` from 2.0 to 2.5. Recent
  eval shows entity-heavy situations score 0.08 higher when entity
  matches dominate. Predicted aggregate quality_score delta: +0.03."
- "Edit `src/blindspot/prompts/risk_officer.md`: add explicit instruction
  to consider opportunity-cost framing for any situation with persona
  `comparing-offers`."

Unacceptable (too vague): "improve coverage", "make prompts clearer",
"add more sources".

### Direction selection based on previous-run classification:

- **POSITIVE** → continue along the same dimension as the last run. Refine
  further in the same area.
- **NEUTRAL** → switch to a different dimension. The current path isn't
  producing signal.
- **NEGATIVE** → if the last commit was a 🟢 direct commit, consider
  `git revert` of that commit and try a different angle. If the last
  action was a 🟡 PR (still pending), DO NOT make another related change
  this turn — the user hasn't reviewed yet.

## Step 4 — Apply the change

There is no "never touch" tier. The worst case is always 🟡 (a PR).

### 🟢 Auto-commit to `main` (no PR)

Allowed only for these paths:

- `src/blindspot/prompts/*.md` — agent system prompts
- `community_profiles/*.md` — community-analyst profiles
- `data/source_registry.yaml` — but ONLY the `notes`, `reliability`, or
  `freshness_required` field of an **existing** entry. Adding a new entry
  is 🟡.
- `fixtures/eval_situations.yaml` — additive only (do not modify or
  delete existing situations)
- `docs/**/*.md`
- `config.yaml` — only fields listed under `tunable_keys` in the config
  schema, and only within their declared min/max ranges

Use Edit / Write tools. After editing, go to Step 5.

### 🟡 Branch + open PR (anything else)

Required for:

- `src/**/*.py` — any code change
- `db/migrations/**`
- `pyproject.toml`
- `.claude/settings.json`
- `.claude/hooks/**`
- `tests/**`
- New entries in `source_registry.yaml` or `tag_taxonomy_seed.yaml`
- New community profile files
- Config schema additions
- **Any file deletion**

Steps:

```bash
# Branch name format: refine/YYYYMMDD-HHMMSS-<short-slug>
ts="$(date -u +%Y%m%d-%H%M%S)"
slug="<derive a short kebab-case slug from your intent>"
git checkout -b "refine/${ts}-${slug}"

# Make the edits via Edit/Write tools.

git add <files>
git commit -m "<concise message>"     # pre-commit code-review hook runs
git push -u origin "refine/${ts}-${slug}"

gh pr create --title "refine: <short>" --body "$(cat <<EOF
## What changed
<description>

## Why
<reasoning, including which dimension from Step 3 this addresses>

## Predicted signal delta
- specificity: +X
- non_obviousness: +X
- grounding_pct: +X%
- diversity: +X

## Risk of regression
<honest assessment>

## Security-sensitive flag
$( if echo "<files>" | grep -qE "\.claude/(settings\.json|hooks/)|pyproject\.toml"; then
     echo "⚠️ This PR touches a security-sensitive file. Please review carefully."
   else
     echo "None."
   fi )

🤖 Generated by refine-blindspot skill
EOF
)"
```

Never merge the PR yourself. The user reviews and merges.

## Step 5 — Verify (🟢 only)

For 🟢 commits:

1. Run `blindspot eval` with a 600-second timeout.
2. Compute `new_quality_score - baseline_quality_score`.
3. If the delta is `< -0.02` (clear regression), `git restore` the file
   and log this as NEGATIVE in Step 6.
4. If the delta is `>= -0.02`, proceed to Step 6 + 7.

For 🟡 PRs, Step 5 is skipped — verification is the user's review +
whatever CI you set up later.

## Step 6 — Log to `refinements/log.jsonl`

Append exactly one JSON line:

```json
{
  "timestamp": "2026-05-13T14:00:00Z",
  "run_id": "<git short SHA, or PR number with 'pr-' prefix>",
  "classification_of_previous": "POSITIVE|NEUTRAL|NEGATIVE|BASELINE",
  "dimension": "prompt-clarity|coverage|signal-noise|failure-pattern",
  "tier": "🟢|🟡",
  "files_touched": ["src/blindspot/prompts/risk_officer.md"],
  "summary": "<one-sentence what changed>",
  "rationale": "<one-paragraph why>",
  "baseline_quality_score": 0.71,
  "new_quality_score": 0.74,
  "expected_signal_delta": {
    "specificity": 0.05,
    "non_obviousness": 0.00,
    "grounding_pct": 0,
    "diversity": 0.00
  },
  "verify_outcome": "passed|regression|skipped-pr",
  "next_suggested_path": "Try tuning entity_weight if specificity holds gains."
}
```

## Step 7 — Commit & push

### For 🟢

```bash
git add <files> refinements/log.jsonl
git commit -m "refine: <summary from Step 6>"     # hook will run, should pass
git push origin main                              # durable user auth
```

If the pre-commit code-review hook blocks the commit (it shouldn't — 🟢
files are all non-code), abort and `HUMAN_REVIEW_REQUESTED` (see below).

### For 🟡

The PR is already open. Just append the log entry as a single commit on
`main` (the log itself is 🟢):

```bash
git checkout main
git add refinements/log.jsonl
git commit -m "refine: log iteration (PR #<n>)"
git push origin main
```

## Boundaries — when to bail out

Output a single line starting with `HUMAN_REVIEW_REQUESTED:` followed by a
short explanation, and exit without making further changes, if:

- The eval suite fails to run at all (broken pipeline upstream).
- Three consecutive `refinements/log.jsonl` entries classify previous as NEGATIVE.
- The same `dimension` has been tried 5+ times in the last 10 runs with no POSITIVE.
- A git operation fails (push rejected, merge conflict, branch already exists).
- The code-review hook blocks a commit you expected to be 🟢.

The skill is meant to compose with human oversight, not replace it. Bailing
out is the correct behavior when it's stuck.

## Non-negotiables

- Never disable, modify, or bypass the pre-commit code-review hook.
- Never use `git push --force` or any destructive git operation.
- Never schedule yourself. Scheduling is a deliberate user action via the
  separate `schedule` skill, after they've watched this skill run 3–5 times
  manually and inspected the log.
- Never merge a PR opened by this skill.
- Never modify `.claude/settings.json` or `.claude/hooks/**` without going
  through 🟡 PR — even though those are technically in scope.
