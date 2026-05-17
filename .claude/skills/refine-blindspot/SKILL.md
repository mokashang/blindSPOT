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
./bin/blindspot eval     # writes eval/results/<timestamp>.json
```

(Use `./bin/blindspot` not the system-PATH `blindspot` — the wrapper
exports `PYTHONPATH=src` and bypasses the editable `.pth` file, which
on macOS Python 3.13 keeps getting `chflags hidden` re-applied by pip
and silently skipped by `site.py`. Bare `blindspot` is unreliable.)

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

## Step 7 — Auto-review iteration loop

Auto-review iterates: if rejected, address the feedback, push the fix,
re-review. Cap at **MAX_ITERATIONS = 3**. On each iteration the reviewer
sees the prior rejection reasons so it can verify the fix actually
addresses them.

```
prior_rejections = []
for iteration in 1..MAX_ITERATIONS:
    diff_text = gh pr diff $pr_number
    pr_body  = gh pr view $pr_number --json body -q .body

    prior_section = ""
    if prior_rejections:
        prior_section = "\n\n# Prior rejection reasons (this is iteration N)\n" \
                        + "\n".join(f"- {r}" for r in prior_rejections)

    reviewer_input = REVIEWER_PROMPT.md  +
                     "\n\n---\n\n# PR description\n" + pr_body +
                     prior_section +
                     "\n\n# Diff\n```diff\n" + diff_text + "\n```" +
                     "\n\nOutput your verdict as a single JSON object on one line."

    verdict = parse(timeout 180 claude -p "$reviewer_input")
    # verdict: {"approve": bool, "reason": "..."}

    if not parsable(verdict):
        # On TWO consecutive unparseable verdicts, bail out (see Boundaries).
        if previous_was_unparseable: bail HUMAN_REVIEW_REQUESTED
        previous_was_unparseable = True
        continue

    gh pr comment $pr_number --body "🤖 Iteration ${iteration}: ${verdict.approve ? 'APPROVE' : 'REJECT'} — ${verdict.reason}"

    if verdict.approve:
        break  # proceed to Step 8 merge

    # Anti-gaming: if this rejection looks substantively similar to a prior
    # one (first 10 words match, or same noun phrase), the loop isn't
    # converging — bail out.
    if iteration > 1 and similar_to_any(verdict.reason, prior_rejections):
        bail HUMAN_REVIEW_REQUESTED \
             "reviewer rejected with the same complaint twice (iteration ${iteration}); not converging"

    prior_rejections.append(verdict.reason)

    # Apply fix addressing the rejection
    # (use Edit/Write tools targeting the specific files / lines the reviewer flagged;
    #  if the rejection is structural — e.g. "out of scope" — narrow the diff
    #  rather than expand it)
    git add <fixed-files>
    git commit -m "refine: address review feedback (iteration ${iteration})"
    git push origin "$branch"
else:
    # MAX_ITERATIONS exhausted
    bail HUMAN_REVIEW_REQUESTED "reviewer rejected ${MAX_ITERATIONS} consecutive times"
```

**Robustness:** if `claude -p` fails outright (network, timeout) for two
consecutive iterations, bail with `HUMAN_REVIEW_REQUESTED:` — don't merge
on broken parsing.

## Step 8 — Merge

If the iteration loop above broke on `approve`, merge:

```bash
gh pr merge $pr_number --squash --delete-branch
```

The `--squash` collapses all iteration commits into a single commit on
`main`, keeping history clean. The pre-commit code-review hook does not
fire on the squash-merge commit, but each underlying iteration commit
already passed the per-commit hook when made on the branch.

If the iteration loop bailed (any `HUMAN_REVIEW_REQUESTED:` path above):
do NOT merge. Leave the PR open with all iteration history visible via
`gh pr comment` entries.

## Step 9 — Log

Append exactly one JSON line to `refinements/log.jsonl`:

```json
{
  "timestamp": "2026-05-13T14:00:00Z",
  "run_id": "<short branch SHA, or 'pr-<n>' for held PRs>",
  "pr_number": 42,
  "pr_status": "merged|held|abandoned-pre-pr",
  "classification_of_previous": "POSITIVE|NEUTRAL|NEGATIVE|HELD|BASELINE",
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
  "auto_review_iterations": 2,
  "auto_review_history": [
    {"iteration": 1, "verdict": "reject", "reason": "Out of scope: diff touches src/blindspot/cli.py which wasn't in the PR description"},
    {"iteration": 2, "verdict": "approve", "reason": "Scope narrowed to just the prompt edit; addresses prior rejection"}
  ],
  "final_verdict": "approve|held",
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
  NEGATIVE or HELD.
- The same `dimension` has been tried 5+ times in the last 10 runs with
  no POSITIVE merge.
- A single PR exhausts MAX_ITERATIONS (= 3) of auto-review fix-and-retry.
- Within one PR, the reviewer rejects with a substantively similar
  complaint to a prior iteration (anti-gaming guard — fix isn't actually
  addressing what was flagged).
- Across runs, three consecutive PRs have been held (not merged).
- A git operation fails (push rejected, merge conflict, branch already
  exists).
- The code-review hook blocks a commit you expected to pass.
- The auto-reviewer's verdict output is unparseable on two consecutive
  iterations within a single PR.

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
