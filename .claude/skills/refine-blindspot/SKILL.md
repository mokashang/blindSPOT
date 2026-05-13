---
name: refine-blindspot
description: One iteration of autonomous refinement on the Blindspot project. Evaluate the previous change, decide a concrete direction, apply on a fresh branch, run eval, open a PR, auto-review with a separate Claude session, merge if approved. Designed to run hourly via the `schedule` skill once trust is established — but ALWAYS invokable manually. The skill never schedules itself; that is a user action.
---

# Refine Blindspot

You are running one iteration of refinement on the Blindspot project. The
loop is: read state → evaluate previous change → decide direction → apply
on branch → eval → open PR → auto-review → merge or hold → log.

Every change goes through a PR that is reviewed by a separate Claude
session before merging. There is no direct-to-main commit path — uniform
PR flow with two layers of review (the per-commit code-review hook plus
the PR-level auto-reviewer).

## Step 1 — Read state

Use Bash + Read to collect:

- Last 30 entries of `git log --oneline` to see what changed recently
- Last 10 entries of `refinements/log.jsonl` (most recent first)
- The most recent file in `eval/results/*.json`
- The eval result from immediately before the most recent (for delta math)
- If it exists, `data/feedback.jsonl` (real user ratings, post-V1)
- `gh pr list --state open --search "head:refine/"` — see if any prior
  refine PRs are still open (rejected by auto-review). If so, that's a
  signal something needs human attention.

Build a short mental summary:
- What did the last refinement run change? Was it merged or held?
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

If the previous PR was REJECTED by the auto-reviewer (not merged),
classify as **REJECTED** and read the rejection reason — adjust this
run's approach to avoid the same rejection cause.

## Step 3 — Decide direction

Cycle through these four dimensions in order. For each, ask: "Is there a
*specific* and *concrete* improvement available here right now?" Stop at
the first yes.

1. **Prompt clarity** — Look at the lowest-scoring eval situation. Read
   the prompts of the agents that handled it. Find one specific ambiguity
   or missing instruction.

2. **Coverage gaps** — Check `ungrounded_claims` rows from recent turns.
   Group by topic. Is there a cluster pointing at a topic that no current
   source-view covers? (If yes, plan a PR to add a new source-view.)

3. **Signal-to-noise** — Check `source_view_stats`. Are any source-views
   consistently producing low-rated blind spots? Consider lowering their
   `reliability` field, or improving the `keyword_filter`.

4. **Failure-mode patterns** — Look at the critic's recent feedback
   strings. Are there recurring categories (e.g. "too generic", "no
   concrete numbers", "missing citations")? The fix usually goes into
   the agent's system prompt.

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

- **POSITIVE** → continue along the same dimension. Refine further.
- **NEUTRAL** → switch to a different dimension. The path isn't producing signal.
- **NEGATIVE** → If the previous merged change caused a regression that
  wasn't caught by branch-eval (rare), open a `git revert` PR.
- **REJECTED** → read the auto-reviewer's reason. Address it (don't just
  retry the same thing). If the rejection seems wrong, escalate via
  `HUMAN_REVIEW_REQUESTED:` rather than gaming the reviewer.
- **BASELINE** → start anywhere reasonable.

## Step 4 — Apply on a fresh branch

```bash
ts="$(date -u +%Y%m%d-%H%M%S)"
slug="<derive a short kebab-case slug from your intent>"
branch="refine/${ts}-${slug}"
git checkout -b "$branch"
```

Make the change using Edit/Write tools. The pre-commit code-review hook
will fire on each commit (catches code-quality issues for `.py`, `.ts`,
etc; allows `.md`/`.yaml`/`.json` through). If the hook blocks your
commit on a code file, address the feedback or abandon (don't bypass).

```bash
git add <files>
git commit -m "<concise message starting with 'refine:'>"
```

## Step 5 — Run eval on the branch

```bash
blindspot eval     # writes eval/results/<timestamp>.json
```

Compute `new_quality_score - baseline_quality_score` from the report.

- If delta `< -0.02` (clear regression):
  ```bash
  git checkout main
  git branch -D "$branch"
  ```
  Log NEGATIVE with the regression delta, exit.
- If delta `>= -0.02`, proceed.

## Step 6 — Push branch + open PR

```bash
git push -u origin "$branch"

gh pr create --title "refine: <short summary>" --body "$(cat <<EOF
## What changed
<one-sentence description>

## Why
<dimension from Step 3 + rationale>

## Predicted signal delta
- specificity: ±X
- non_obviousness: ±X
- grounding_pct: ±X%
- diversity: ±X

## Eval result on this branch
- baseline quality_score: <previous>
- branch quality_score: <new>
- delta: <delta>

## Files touched
<list>

## Risk assessment
<honest one-paragraph assessment of what could go wrong>

🤖 Generated by refine-blindspot skill
EOF
)"
```

Capture the PR number (e.g. `pr_number=$(gh pr view --json number -q .number)`).

## Step 7 — Auto-review

Get the diff and invoke the reviewer:

```bash
diff_text="$(gh pr diff $pr_number)"
pr_body="$(gh pr view $pr_number --json body -q .body)"

reviewer_prompt="$(cat .claude/skills/refine-blindspot/REVIEWER_PROMPT.md)

---

# PR description
$pr_body

# Diff
\`\`\`diff
$diff_text
\`\`\`

Now output your verdict as a single JSON object on one line, nothing else."

verdict_json="$(timeout 180 claude -p "$reviewer_prompt")"
```

Parse `verdict_json` for `{"approve": bool, "reason": "..."}`.

**Robustness:** If `claude -p` fails or output is unparseable, treat as
reject and leave the PR open (do not auto-merge on broken parsing).

## Step 8 — Merge or hold

**If approved:**

```bash
gh pr merge $pr_number --squash --delete-branch
```

(The `gh pr merge` will land the squashed change on main. The pre-commit
hook does not fire on merges, but the per-commit hook already reviewed
the underlying commits when they were made on the branch.)

**If rejected:**

```bash
gh pr comment $pr_number --body "🤖 Auto-review rejected: <reason>"
git checkout main
# Do NOT delete the branch — leave it for human review.
```

The PR stays open. The next refine run will see it via `gh pr list` and
adjust strategy.

## Step 9 — Log

Append exactly one JSON line to `refinements/log.jsonl`:

```json
{
  "timestamp": "2026-05-13T14:00:00Z",
  "run_id": "<short branch SHA, or 'pr-<n>' for held PRs>",
  "pr_number": 42,
  "pr_status": "merged|held|abandoned-pre-pr",
  "classification_of_previous": "POSITIVE|NEUTRAL|NEGATIVE|REJECTED|BASELINE",
  "dimension": "prompt-clarity|coverage|signal-noise|failure-pattern",
  "files_touched": ["src/blindspot/prompts/risk_officer.md"],
  "summary": "<one-sentence what changed>",
  "rationale": "<one-paragraph why>",
  "baseline_quality_score": 0.71,
  "branch_quality_score": 0.74,
  "expected_signal_delta": {
    "specificity": 0.05,
    "non_obviousness": 0.00,
    "grounding_pct": 0,
    "diversity": 0.00
  },
  "auto_review_verdict": "approve|reject",
  "auto_review_reason": "<reviewer's reason verbatim>",
  "next_suggested_path": "Try tuning entity_weight if specificity holds gains."
}
```

The log itself lives on main. Append + commit + push in one small commit:

```bash
git add refinements/log.jsonl
git commit -m "refine: log iteration $ts"
git push origin main
```

## Boundaries — when to bail out

Output a single line starting with `HUMAN_REVIEW_REQUESTED:` followed by
a short explanation, and exit without making further changes, if:

- The eval suite fails to run at all (broken pipeline upstream).
- Three consecutive `refinements/log.jsonl` entries classify previous as
  NEGATIVE or REJECTED.
- The same `dimension` has been tried 5+ times in the last 10 runs with
  no POSITIVE merge.
- Three consecutive PRs have been rejected by the auto-reviewer.
- A git operation fails (push rejected, merge conflict, branch already
  exists).
- The code-review hook blocks a commit you expected to pass.
- The auto-reviewer's verdict output is unparseable on two consecutive
  attempts.

These conditions mean either refine's judgment, the reviewer's
calibration, or the project state has drifted into a place that needs
human eyes. Bailing out is the correct behavior.

## Non-negotiables

- Never push directly to `main` from a refine session. All changes go
  through PR + auto-review. The only direct-to-main commit is the
  single log-append in Step 9.
- Never use `git push --force` or any destructive git operation.
- Never schedule yourself. Scheduling is a deliberate user action via
  the separate `schedule` skill, after the user has watched this skill
  run 3–5 times manually.
- Never modify `REVIEWER_PROMPT.md`, this `SKILL.md`, or any file under
  `.claude/hooks/` or `.claude/settings.json` — the auto-reviewer is
  instructed to reject any PR touching these, but you should also not
  attempt them. If you think they need a change, output
  `HUMAN_REVIEW_REQUESTED:` and explain.
- Never bypass the pre-commit code-review hook (no `--no-verify`,
  `BLINDSPOT_SKIP_REVIEW=1`, or similar). If the hook blocks a commit,
  abandon and try a different change.
- If the auto-reviewer rejects, do not retry the same idea. Either
  address the reviewer's concern or move to a different dimension.
