---
name: refine-blindspot
description: One iteration of autonomous refinement on the Blindspot project (scope-narrowed). Reads state, classifies previous PRs, picks up to 3 detail dimensions from the V2-narrow / V3-ui / V4-freeze checklist in ROADMAP.md, fans out parallel subagents in worktrees, auto-merges approved PRs, logs, and updates ROADMAP. Hard scope boundary: never touches voice-work files (decisions/framings/blindspots paragraph content), never adds new verticals, never edits archived content. Designed for the 2-week sprint to V4-freeze.
---

# Refine Blindspot — Scope-Narrowed

You are running ONE iteration of refinement on the Blindspot
project. The project is in a **portfolio-track, scope-narrow phase**
since 2026-05-18 — see `docs/specs/ROADMAP.md` for the V2-narrow /
V3-ui / V4-freeze checklist that is the *entire* scope of refinement
work. The hourly cron exists to help the user reach V4-freeze; once
V4-freeze lands, the cron is part of what gets disabled.

Each iteration fans out **up to 3 parallel refinement attempts**
across detail dimensions (the old skill's 4-layer model has been
collapsed and the "framework" 5th slot has been removed — scope is
frozen, no framework reflection).

Every change goes through a PR reviewed by a separate `claude -p`
session using `REVIEWER_PROMPT.md`. There is no direct-to-main
commit path except the orchestrator's single end-of-run log +
ROADMAP edit. Parallel fan-out + auto-review + auto-merge is the
unchanged design from the previous skill.

## What changed vs the pre-pivot skill

This is a deliberately shorter, narrower skill. Removed:

- 10-domain reasoning (`domain_knowledge/_meta_ontology.md` is
  collapsed to a single in-scope vertical).
- Roadmap candidate sourcing across multiple domains — the roadmap
  has 26 concrete sub-tasks across 3 fixed versions; just pick the
  next available ones in the current 🟡 section.
- Framework-level reflection (Step 2.5 in the old skill) — scope is
  frozen, framework changes are out-of-scope by definition.
- Detail-layer mapping with 4 slots — collapsed to 3 layers
  (knowledge-schema / agents-and-config / eval / web-infra) with at
  most 3 dispatched per run.
- "Pulled-forward from a future ⬜ section" fallback path — the
  three remaining version sections are small enough that there's
  always work in the active 🟡 section.

Kept:

- The orchestrator + parallel-subagents-in-worktrees + auto-review +
  auto-merge structure.
- Non-negotiables: never push to main except the log/ROADMAP commit;
  never bypass the pre-commit hook; never modify SKILL.md /
  REVIEWER_PROMPT.md / `.claude/settings.json` /
  `$HOME/.claude/hooks/`; never use `--force`.
- Recovery strategies for every failure mode — eval broken, sync
  drift, all subagents abandoned, push race, log conflicts.
- Auto-merge on auto-review approval. The user does not approve PRs
  manually unless one is held.
- No `HUMAN_REVIEW_REQUESTED` exit. Every run emits a final summary
  line.

Added:

- **Voice-work boundary** (§5 below). Refine never authors
  `decisions.md` / `framings.md` / `blindspots.md` paragraph
  content — those are insider voice work the user (or
  deliberately-scoped non-routine Claude conversations) authors.
- **V4-freeze awareness** (§9 below). When V4-freeze closes the
  routine logs `v4_freeze_reached` and recommends the user disable
  the cron.

## Fully autonomous — no human in the loop

Once this skill starts, it runs end-to-end without asking the user
anything. **The run always ends with a final summary line** — never
with `HUMAN_REVIEW_REQUESTED:`. Two paths:

- **Happy path** — approved PRs are merged automatically, the log
  is pushed, ROADMAP.md is updated. Summary names the merges and
  the `quality_score` delta.
- **Recovery path** — something went wrong. Follow the table in
  "Recovery strategies" below; log the anomaly as a
  `recovery_attempt`, take the safest progress-producing action,
  continue. Summary line still gets emitted; the run is "completed
  with anomalies" rather than "failed".

Make every detail decision yourself. The rules in this skill are
the decision boundary; when they're silent, use your judgment.
Never pause to ask.

---

## 1. The high-level loop

```
Orchestrator (this session):
  Step 1: Read state
  Step 2: Classify previous run's PRs
  Step 3: Decide up to 3 detail dimensions
  Step 4: Fan out N parallel subagents in worktrees
  Step 10: Sync, merge approved PRs, append log + ROADMAP edits,
           push, verify, prune

Each subagent (isolated worktree, runs in parallel with peers):
  Step 5: Apply on a fresh refine/<ts>-<slug> branch
  Step 6: Run eval on the branch
  Step 7: Push + open PR
  Step 8: Auto-review iteration loop (up to 3 fix-and-retry rounds)
  Step 9: Return JSON verdict to orchestrator (no merge here)
```

## 2. Step 1 — Read state (orchestrator)

Use Bash + Read to collect:

- `git log --oneline -30` to see what changed recently.
- Last 10 entries of `refinements/log.jsonl` (most recent first).
- The most recent file in `eval/results/*.json`; the one before it
  too (for delta math).
- `gh pr list --state open --search "head:refine/"` — see if prior
  refine PRs are still open.
- `docs/specs/ROADMAP.md` — find the currently 🟡 section
  (V2-narrow until its 13 items are `[x]`; then V3-ui; then
  V4-freeze).

Build a short mental summary: what did the last run change, did
predictions match deltas, what's the current eval score, what's the
next concrete sub-task in the active version section.

If `refinements/log.jsonl` has no entries newer than the pivot
commit, this is a **POST-PIVOT BASELINE** run: skip Step 2 and pick
any concrete improvement in the active version's checklist to start
the loop.

## 3. Step 2 — Classify previous run's PRs (orchestrator)

For each previous attempt, compare the predicted
`expected_signal_delta` to the actual delta from eval scores:

- **POSITIVE** — actual delta same sign, similar magnitude.
- **NEUTRAL** — `|actual_delta| < 0.02` on aggregate `quality_score`.
- **NEGATIVE** — actual delta opposite sign to predicted, OR much
  smaller in magnitude.
- **HELD** — PR rejected by auto-reviewer or held due to conflict.
- **REJECTED** — rejected by auto-reviewer (read the reason).

These classifications inform Step 3 dimension choice.

## 4. Step 3 — Decide dimensions this run (orchestrator)

Dimensions are layer-based. Pick up to 3 (was 4 in the old skill).
Per layer, two candidate streams; the strongest gets the slot:

- **Roadmap-driven** — the next open sub-task in the active 🟡
  version that lives in this layer.
- **Reactive** — measured signal that something is wrong now (low
  eval, recurring critic complaint, missing fixture coverage).

When both point at the same change, that's the strongest candidate.
When they conflict, prefer roadmap-driven unless reactive signal is
severe.

### 4.1 The 3 layers

**1. knowledge-schema** — `domain_knowledge/cn-sde-jobhunt/`
   schema-driven content + `data/source_registry.yaml` +
   `data/tag_taxonomy_seed.yaml` + community-profile files.
   Refine MAY edit:
   - `sources.yaml` (add / retire / re-annotate source-views)
   - `communities/<name>.md` (Voice / Mental model / Typical
     concerns / Known blind spots OF this community — schema-driven
     sections per `community_profiles/_schema.md`)
   - `domain_pack.md` (Triage / Editor / Critic prompt overrides)
   - `data/tag_taxonomy_seed.yaml` (add new entities / personas /
     risk-surfaces)
   - **Empty entry skeletons** in `decisions.md` / `framings.md` /
     `blindspots.md` (name + scope-axes placeholders only — never
     paragraph content)
   - **Front-matter indexes** of `framings.md` / `blindspots.md`
     (the table-of-framings or table-of-blindspots at the top of
     each file)

   Refine MUST NOT edit:
   - Paragraph content under any entry in `decisions.md` /
     `framings.md` / `blindspots.md` (voice work; see §5)
   - Anything under `domain_knowledge/_archive/` or
     `domain_knowledge/_legacy/`

**2. agents-and-config** — `src/blindspot/prompts/*.md` +
   `config.yaml`.
   Refine MAY edit:
   - Agent prompt phrasing (Triage / Risk Officer / Critic / Editor
     / Community Analyst) — for clarity, instruction-following,
     persona handling, banlist additions.
   - Tunable keys in `config.yaml` per the `tunable_keys` whitelist
     at the bottom of the file (scoring weights, top-n,
     diversity-cap, critic thresholds, normalization threshold).

   Refine MUST NOT:
   - Change the LLM backend (`config.yaml: llm_backend`).
   - Change DB paths, cache TTLs, model selections (out of
     whitelist).
   - Touch `triage_pass1.md` to re-broaden the in-scope domain list
     beyond `cn-sde-jobhunt`.

**3. eval** — `fixtures/eval_situations.yaml` +
   `src/blindspot/eval/runner.py` (`quality_score` aggregation
   inline) + `src/blindspot/eval/judge.py` (judge prompts).
   Refine MAY edit:
   - Add new fixture situations covering uncovered personas / risk
     surfaces named in `ROADMAP.md` V2-narrow checklist.
   - Tighten judge prompts for clearer scoring criteria.
   - Adjust `quality_score` aggregation when sub-metric weights
     drift away from what `config.yaml: refine.quality_score_weights`
     declares.

   Refine MUST NOT:
   - Delete fixture entries (the auto-reviewer rejects on test/eval
     deletion).
   - Remove a sub-metric the weights still reference.

**4. web-infra** (only active when V2-narrow is `≥ 10/13` items
   `[x]` AND V3-ui is the 🟡 section) — `src/blindspot/web/`,
   `Dockerfile`, `docker-compose.yml`, frontend stubs.
   Refine MAY edit:
   - FastAPI route scaffolding (`src/blindspot/web/app.py`).
   - SSE streaming wrapper around the Editor agent.
   - Next.js / React component scaffolding (or HTMX equivalents if
     the user picked that stack).
   - Docker / compose infrastructure for the demo.

   This layer is dormant during V2-narrow. The orchestrator skips
   it until the entry condition above is met. (This is a deliberate
   simplification: V2-narrow needs knowledge depth, V3-ui needs web
   infra, and bouncing between them within a run dilutes signal.)

### 4.2 Concreteness

For each candidate:

- File path(s) touched.
- Exact edit intent.
- Predicted signal delta with mechanism.
- The roadmap `item_id` it advances (every chosen candidate must
  map to a specific checkbox in ROADMAP.md).

Examples:

- "Add 3 source-view entries to `domain_knowledge/cn-sde-jobhunt/sources.yaml`:
  Murthy Law Firm RSS, Boundless H-1B blog, r/h1b. Roadmap item:
  `v2-narrow/cn-sde-jobhunt/sources-yaml`. Predicted delta:
  `source_diversity` +0.05 (4th community tag activated)."
- "Edit `src/blindspot/prompts/critic.md`: tighten the per-claim
  citation spot-check to also flag claims about visa-status
  timelines (e.g. 'OPT extension lasts 24 months'). Roadmap item:
  `v2-narrow/agents/critic-tightening` (NEW — promote in Step 3
  via reactive signal: 3 of last 5 eval fixtures showed uncited
  visa-timeline claims). Predicted delta: `grounding_pct` +0.04."

Unacceptable (too vague): "improve coverage", "make prompts
clearer", "add more sources".

### 4.3 Per-layer direction rules

- **POSITIVE** → continue same layer with next candidate.
- **NEUTRAL** → switch this layer's candidate.
- **NEGATIVE** → revert PR (this slot becomes a `git revert` PR).
- **REJECTED** → address reviewer's reason or pick a different
  change. Don't game the reviewer.
- **HELD (conflict)** → rebase + retry, or pick different candidate.
- **BASELINE** → start in `knowledge-schema` (source registry +
  communities are the most leveraged early in V2-narrow).

### 4.4 Recovery when no candidate exists

If zero layers have a concrete candidate, pick a low-bar
maintenance task in `knowledge-schema` or `eval`: refresh a
source-view's `notes`, tighten a fixture's `expected_*` annotation,
add a docstring. Dispatch one subagent on that change. Log
`recovery_attempt: no_candidates`.

## 5. Voice-work boundary — what refine MUST NOT author

The single most important constraint in the narrow-scope skill is
that **refine does not write voice work**. Voice work is content
that requires insider authority — the author's lived experience as
a Chinese international student in the US tech job market — and is
not derivable from public corpora.

Voice-work files (the auto-reviewer rejects any PR adding paragraph
content under these):

- `domain_knowledge/cn-sde-jobhunt/decisions.md` — entry paragraph
  content (the `Scope` / `Sample situations` body sentences)
- `domain_knowledge/cn-sde-jobhunt/framings.md` — entry paragraph
  content (the `Mental model summary` / `Excludes` body sentences)
- `domain_knowledge/cn-sde-jobhunt/blindspots.md` — entry paragraph
  content (the `Statement` / `Failure-mode` / `Recovery-move` body
  sentences)

Refine MAY edit these files only to add **empty entry skeletons**
(structural placeholders the user fills) or **front-matter
indexes** (the cross-reference tables at the top of each file).

Why this matters: an earlier iteration of the routine produced 70+
blindspot entries per domain across 6 domains, totaling ~200k words
of LLM-generated voice. The author's reflection on 2026-05-18 was
that this content, while structurally compliant, did not have
insider authority and would not pass the "would an insider nod"
quality bar from `domain_knowledge/_schema.md`. The voice-work
boundary makes that lesson durable: the routine focuses on what it
*can* do well (schema-driven structure, prompts, eval, infra) and
leaves authorship of the actual insight to the user.

## 6. Step 4 — Fan out parallel subagents (orchestrator)

For each chosen dimension (1–3), dispatch a subagent with
`isolation: "worktree"`. **All subagents in a single Agent-tool
message (parallel calls)** so they run concurrently.

Each subagent gets a self-contained brief — it has no memory of
this orchestrator session. The brief tells it: the dimension, the
specific concrete change, the predicted delta, and points it at
this SKILL.md (Steps 5–9) for the detailed procedure.

Subagent brief shape:

```
You are a refine-blindspot subagent. You are running ONE refinement
attempt in an isolated git worktree, in parallel with peer
subagents.

## Your dimension
<knowledge-schema | agents-and-config | eval | web-infra>

## Your specific change
<one paragraph: file path(s), exact edit intent, predicted delta>

## Roadmap item being advanced
<item slug from ROADMAP.md>

## Voice-work boundary reminder
<copy §5 from SKILL.md verbatim if dimension touches
 domain_knowledge/cn-sde-jobhunt/{decisions,framings,blindspots}.md>

## Procedure
Read `.claude/skills/refine-blindspot/SKILL.md` and follow
Steps 5–9 exactly. Skip Steps 1–4 (orchestrator did them) and
Steps 10+ (orchestrator will do them after you return).

Do NOT merge the PR. Do NOT push to main. Return a single JSON
object in the shape described in Step 9. Try the recoveries in
"Recovery strategies — subagent-level" first before returning
"abandoned".

Non-negotiables: never push to main, never `--force`, never bypass
the pre-commit hook, never modify SKILL.md / REVIEWER_PROMPT.md /
.claude/settings.json / $HOME/.claude/hooks/.
```

After all subagents are dispatched in parallel, wait for all to
return. Each returns one JSON object (Step 9 shape). Collect them.

## 7. Step 5 — Apply on a fresh branch (inside subagent)

```bash
ts="$(date -u +%Y%m%d-%H%M%S)"
slug="<short kebab-case from your edit intent>"
branch="refine/${ts}-${slug}"
git checkout -b "$branch"
```

(Branch names are global; `ts` includes seconds so collisions are
vanishingly unlikely. If `checkout -b` fails with "branch already
exists", append a 2-char random suffix and retry once.)

Make the change with Edit/Write tools. The pre-commit code-review
hook fires on each commit. If it blocks on a code file, address the
feedback or abandon — never bypass.

```bash
git add <files>
git commit -m "<concise message starting with 'refine:'>"
```

## 8. Step 6 — Run eval on the branch (inside subagent)

```bash
./bin/blindspot eval     # writes eval/results/<timestamp>.json
```

Use `./bin/blindspot` not the system-PATH `blindspot` (the wrapper
exports `PYTHONPATH=src` and bypasses the editable `.pth` file,
which on macOS Python 3.13 keeps getting `chflags hidden`
re-applied by pip and silently skipped by `site.py`).

Compute `new_quality_score - baseline_quality_score` from the report.

- If delta `< -0.02` (clear regression): try ONE smaller version of
  the change (cut the knob delta in half, narrow the file scope).
  If still regresses, abandon. Return JSON with `verdict:
  "abandoned"`, reason `branch-eval regression: delta=<n>`.
- If delta `>= -0.02`, proceed.

(Eval is dimension-aware: schema-only changes that don't run
through the pipeline can skip eval and report `eval_status:
schema_only_skipped`. The auto-reviewer accepts schema-only PRs
without an eval delta when this status is set and the PR
description justifies it.)

## 9. Step 7 — Push + open PR (inside subagent)

```bash
git push -u origin "$branch"

gh pr create --title "refine: <short summary>" --body "$(cat <<EOF
## What changed
<one-sentence description>

## Why
<dimension + rationale; cite the ROADMAP item slug being advanced>

## Predicted signal delta
- specificity: ±X
- non_obviousness: ±X
- grounding_pct: ±X%
- diversity: ±X

## Eval result on this branch
- baseline quality_score: <previous>
- branch quality_score: <new>
- delta: <delta>
- (or: eval_status: schema_only_skipped — <reason>)

## Files touched
<list>

## Voice-work boundary check
<if PR touches decisions.md / framings.md / blindspots.md:
 confirm it only edits empty skeletons or front-matter indexes,
 NOT paragraph content. Otherwise: "N/A".>

🤖 Generated by refine-blindspot skill (scope-narrowed)
EOF
)"
```

Capture the PR number:
`pr_number=$(gh pr view --json number -q .number)`.

## 10. Step 8 — Auto-review iteration loop (inside subagent)

Auto-review iterates: if rejected, address the feedback, push the
fix, re-review. Cap at **MAX_ITERATIONS = 3**. On each iteration
the reviewer sees prior rejection reasons so it can verify the fix
addresses them.

```
prior_rejections = []
for iteration in 1..MAX_ITERATIONS:
    diff_text = gh pr diff $pr_number
    pr_body  = gh pr view $pr_number --json body -q .body

    prior_section = ""
    if prior_rejections:
        prior_section = "\n\n---\n\n# Prior rejection reasons (iteration N)\n" +
                        "\n".join(f"- {r}" for r in prior_rejections)

    reviewer_input = REVIEWER_PROMPT.md +
                     "\n\n---\n\n# PR description\n" + pr_body +
                     prior_section +
                     "\n\n# Diff\n```diff\n" + diff_text + "\n```" +
                     "\n\nOutput your verdict as a single JSON object on one line."

    verdict = parse(timeout 180 claude -p "$reviewer_input")
    # verdict: {"approve": bool, "reason": "..."}

    if not parsable(verdict):
        if previous_was_unparseable:
            return {verdict: "abandoned", reason: "reviewer output unparseable twice"}
        previous_was_unparseable = True
        continue

    gh pr comment $pr_number --body "🤖 Iteration ${iteration}: ${verdict.approve ? 'APPROVE' : 'REJECT'} — ${verdict.reason}"

    if verdict.approve:
        break

    # Anti-gaming: if this rejection looks substantively similar to
    # a prior one (first 10 words match, or same noun phrase),
    # the loop isn't converging — abandon.
    if iteration > 1 and similar_to_any(verdict.reason, prior_rejections):
        return {verdict: "abandoned", reason: "reviewer rejected with same complaint twice; not converging"}

    prior_rejections.append(verdict.reason)

    git add <fixed-files>
    git commit -m "refine: address review feedback (iteration ${iteration})"
    git push origin "$branch"
else:
    return {verdict: "abandoned", reason: "reviewer rejected ${MAX_ITERATIONS} consecutive times"}
```

If `claude -p` fails outright (network / timeout) for two
consecutive iterations, return `abandoned` — don't approve on
broken parsing.

## 11. Step 9 — Return verdict to orchestrator (inside subagent)

When auto-review approves OR an abandon condition triggers, return
a single JSON object (the subagent's final output). The subagent
does NOT merge and does NOT push to main.

```json
{
  "dimension": "knowledge-schema",
  "pr_number": 42,
  "branch": "refine/20260520-220000-add-1p3a-sources",
  "verdict": "approved" | "held" | "abandoned",
  "reason": "<for held/abandoned: explain. for approved: short note or empty>",
  "baseline_quality_score": 0.71,
  "branch_quality_score": 0.74,
  "eval_status": "ran" | "schema_only_skipped",
  "roadmap_item": "v2-narrow/cn-sde-jobhunt/sources-yaml",
  "expected_signal_delta": {
    "specificity": 0.05,
    "non_obviousness": 0.00,
    "grounding_pct": 0,
    "diversity": 0.05
  },
  "auto_review_iterations": 2,
  "auto_review_history": [
    {"iteration": 1, "verdict": "reject", "reason": "..."},
    {"iteration": 2, "verdict": "approve", "reason": "..."}
  ],
  "files_touched": ["domain_knowledge/cn-sde-jobhunt/sources.yaml"],
  "summary": "<one-sentence what changed>",
  "rationale": "<one-paragraph why>"
}
```

`verdict` values:
- `approved` — auto-reviewer approved; orchestrator attempts merge.
- `abandoned` — abandoned pre-PR or during PR for any reason the
  subagent couldn't recover from.
- `held` — reviewer rejected after MAX_ITERATIONS or anti-gaming
  triggered. PR stays open.

## 12. Step 10 — Collect, merge, sync, log (orchestrator)

Goal: end the run with **local main and remote main identical**,
containing all merges from this run plus the log + ROADMAP append.
Sync is treated as an invariant, not best-effort cleanup.

### 12a — Pre-flight on clean main

```bash
git checkout main

# Working tree must be clean.
if [ -n "$(git status --porcelain)" ]; then
    git stash push -u -m "refine: auto-stash $ts"
    auto_stashed=1
fi

git fetch --prune origin

# Replay pending-push files from prior stuck runs
for pending in refinements/pending-push-*.json; do
    [ -f "$pending" ] || continue
    apply_pending "$pending" && rm "$pending"
done

git pull --ff-only origin main
```

If `git pull --ff-only` fails (local diverged): switch to
`git pull --rebase origin main`. If conflict on
`refinements/log.jsonl` or `docs/specs/ROADMAP.md`, auto-resolve
(see Recovery strategies). On a real code-file conflict, drop the
local commit (`git reset --keep ORIG_HEAD`), log
`local_code_diverged_dropped`.

### 12b — Auto-merge approved PRs (remote main)

Sort approved PRs by `branch_quality_score` desc (best first; ties
break by smaller diff). For each:

```bash
gh pr merge $pr_number --squash --delete-branch
```

If a merge fails because of conflict, comment on the PR, mark its
final outcome as `held` in the log (override the subagent's
`approved`), continue to next PR.

### 12c — Sync local main with remote

After ALL `gh pr merge` calls complete:

```bash
git fetch --prune origin
git pull --ff-only origin main
```

If `--ff-only` fails, switch to rebase with the same auto-resolve
logic as 12a.

### 12d — Append log + push (atomic both-side sync)

Build log entries + ROADMAP edits, push as a single commit. This is
the orchestrator's ONLY direct-to-main commit per run.

**Per subagent attempt**, append one line to `refinements/log.jsonl`:

```json
{
  "timestamp": "<orchestrator UTC start>",
  "run_id": "run-YYYYMMDD-HHMM",
  "type": "attempt",
  "dimension": "knowledge-schema",
  "roadmap_item": "v2-narrow/cn-sde-jobhunt/sources-yaml",
  "pr_number": 42,
  "branch": "refine/...",
  "subagent_verdict": "approved",
  "final_verdict": "merged" | "held" | "abandoned",
  "pr_status": "merged" | "held" | "abandoned-pre-pr",
  "baseline_quality_score": ...,
  "branch_quality_score": ...,
  "eval_status": "ran" | "schema_only_skipped",
  "expected_signal_delta": {...},
  "auto_review_iterations": N,
  "summary": "...",
  "next_suggested_path": "..."
}
```

**Per roadmap item touched**, append one `roadmap_progress` line:

```json
{
  "timestamp": "...",
  "run_id": "...",
  "type": "roadmap_progress",
  "item_id": "<roadmap slug>",
  "version_section": "v2-narrow" | "v3-ui" | "v4-freeze",
  "action": "advanced" | "completed" | "blocked" | "deferred",
  "pr_number": 42,
  "final_verdict": "merged" | "held" | "abandoned",
  "summary": "<one-sentence>",
  "reason": "<for blocked/deferred>",
  "next_step_hint": "<optional>"
}
```

**Update ROADMAP.md** for every `roadmap_progress` entry with
action `advanced` or `completed`:

1. **Checkbox**. `[ ]` → `[x]` for completed; leave unchecked for
   advanced (item has more work). Match by item slug; if drift,
   fuzzy-match the checkbox text. If still no match, log
   `roadmap_drift: item <id> no longer locatable`.
2. **Progress bar**. Recompute `Progress: ████░░░░ X% (N/M)` for
   the version section. `N` = count of `[x]`, `M` = total checkboxes.
   Render 20 chars: `█` × round(X/5), `░` × remainder.
3. **Last completed**. Replace with the squash-merge short SHA
   (`git rev-parse --short origin/main`).
4. **Next up**. Replace with the text of the first remaining `[ ]`
   in the section. If none, write `(none — version complete)`.
5. **Status promotion**. If a 🟡 version's items are all `[x]`,
   flip its Status to `✅ complete` AND promote the next `⬜`
   version to `🟡 in progress`.

Commit + push (with up to 5 retries on push race + auto-resolve on
log.jsonl / ROADMAP.md rebase conflicts):

```bash
git add refinements/log.jsonl docs/specs/ROADMAP.md
git commit -m "refine: log iteration $ts (N attempts, M merged, K held; roadmap P advanced, Q completed)"

attempt=1; backoff=2
while ! git push origin main; do
    if [ $attempt -ge 5 ]; then
        save_pending_push "refinements/pending-push-$ts.json"
        log_anomaly "push_deferred" "after 5 attempts"
        break
    fi
    sleep $backoff
    backoff=$((backoff * 2))
    attempt=$((attempt + 1))
    git fetch origin
    if ! git pull --rebase origin main; then
        if ! auto_resolve_rebase_conflict; then
            save_pending_push "refinements/pending-push-$ts.json"
            log_anomaly "rebase_unresolvable" "$(git status --porcelain)"
            git reset --keep origin/main
            break
        fi
    fi
done
```

### 12e — Sync verification

```bash
git fetch origin
local_sha=$(git rev-parse main)
remote_sha=$(git rev-parse origin/main)
if [ "$local_sha" != "$remote_sha" ]; then
    git fetch origin
    local_sha=$(git rev-parse main)
    remote_sha=$(git rev-parse origin/main)
    if [ "$local_sha" != "$remote_sha" ]; then
        log_anomaly "sync_divergence_observed" "local=$local_sha remote=$remote_sha"
    fi
fi
```

### 12f — Worktree cleanup

```bash
git worktree prune
git worktree list  # should only show main
```

Don't block on cleanup failure.

## 13. Final summary line

```
run-20260520-2200: 3 layers attempted (knowledge-schema, agents-and-config, eval)
  → 2 merged, 1 held; V2-narrow 5/13 → 7/13; aggregate quality_score 0.71 → 0.76
```

When V4-freeze closes its last item, append:
`v4_freeze_reached — recommend disabling cron`.

---

## 14. Recovery strategies — never stop, always make progress

The orchestrator NEVER terminates a run early. Every run ends with
the final summary line + log appends + ROADMAP update (if any item
advanced). When a situation in the tables below applies, do the
recovery action; when none applies, log `recovery_attempt` and take
the safest progress-producing action.

### Orchestrator-level recoveries

| Situation | Recovery action |
|---|---|
| Eval suite fails (Step 1 sanity check) | Try `pip install -e .`; on macOS Python 3.13 also `chflags -R nohidden .venv`; re-run. If still broken, scope this run to schema-only changes (skip eval); queue "fix eval pipeline" as a reactive candidate. Log `recovery_attempt: eval_broken`. |
| Zero detail layers have a concrete candidate | Pick a low-bar maintenance task: refresh a `notes` field, tighten a fixture annotation, add a docstring. Log `recovery_attempt: no_candidates`. |
| All subagents returned `abandoned` or `held` | Don't quit. Run a cheaper second round (smaller scope, doc edits, schema-only fixes). If round two also produces 0 merges, log `recovery_attempt: round_two_empty`. |
| Same dimension produced 5+ `held` / `abandoned` in last 10 log lines (no `merged` interspersed) | Don't attempt that dimension this run. Log `dimension_paused: <dim>` once. Resumes when stale entries roll off. |
| **Step 12a — working tree not clean** | `git stash push -u`, proceed. At end of 12d, `git stash pop`; on conflict, leave the stash entry, log `auto_stash_unpopped`. |
| **Step 12a / 12c — `git pull --ff-only` fails** | `git pull --rebase`. If conflict on `log.jsonl` (append-only) or `ROADMAP.md`, auto-resolve: log.jsonl take both sides sorted by `timestamp`; ROADMAP.md take union of `[x]` flips and recompute progress bar. Real code conflict → `git reset --keep ORIG_HEAD`; log `local_code_diverged_dropped`. |
| **Step 12d — push fails after rebase-retry** | Up to 5 total attempts, exponential backoff (2/4/8/16/32 s). On all-fail, save `refinements/pending-push-$ts.json`; log `push_deferred`; continue. |
| **Step 12d — rebase auto-resolve impossible** | Save pending, log `rebase_unresolvable`, `git reset --keep origin/main`, continue. |
| **Step 12d — can't locate ROADMAP.md checkbox for item_id** | Fuzzy-match by checkbox text. If still no match, log `roadmap_drift` and skip the ROADMAP edits for that item. Log still captures progress. |
| **Step 12e — SHA mismatch** | Re-fetch, recompare. If still mismatched, log `sync_divergence_observed`. Next run's 12a reconciles. |
| Git op fails for unknown reason | Retry once with 3× timeout. If still failing, log `git_op_failed`, skip and continue. |
| Last 3 runs produced zero merged PRs | Log `cold_streak_observed` (marker, NOT an exit). Continue normally. |
| Pending push files exist at 12a start | Replay each in chronological order. On success delete; on failure log `pending_replay_failed` and continue. |
| Catastrophic uncaught exception | Wrap top-level `try / except`. Log `unexpected_error: <type> <reason>` with traceback. Emit summary "errored; see log". Exit cleanly. |
| **V4-freeze last item closes** | Append `v4_freeze_reached` log entry. Emit summary with disable-recommendation. Continue running each hour (cron can't disable itself) until user disables. |

### Subagent-level recoveries

| Situation | Recovery action |
|---|---|
| Branch eval regression `< -0.02` | Try ONE smaller version of the change. If still regresses, return `abandoned` with reason. |
| Pre-commit hook block | Parse hook stderr. If it names a fixable issue (style, missing type hint), apply the fix and retry. If same block fires twice on same file, return `abandoned`. NEVER bypass with `--no-verify`. |
| MAX_ITERATIONS auto-review exhausted | Return `held`. |
| Reviewer rejects with substantively similar complaint to prior iteration | Return `held` with reason `not_converging`. Anti-gaming guard. |
| Reviewer verdict unparseable twice in a row | Return `abandoned` with reason `reviewer_unparseable`. |
| Voice-work boundary violation flagged by reviewer (paragraph-content edit in decisions/framings/blindspots.md) | Return `abandoned` with reason `voice_work_violation`. Do not retry — the change is structurally out of scope. |

### Hard "don't do"

These are constraints, not recovery conditions. The PR
auto-reviewer rejects any PR that tries them:

- **Push directly to `main`** from anywhere — only Step 12d's
  single log + ROADMAP commit is allowed on `main` itself.
- **`git push --force`** or any destructive git op (`reset --hard`,
  `branch -D` on unpushed-commit branch, `clean -f -d`).
- **Bypass the pre-commit hook** (`--no-verify`,
  `BLINDSPOT_SKIP_REVIEW=1`, deleting / disabling the hook script,
  removing the matcher in `.claude/settings.json`).
- **Modify any of**: `REVIEWER_PROMPT.md`, this `SKILL.md`,
  `.claude/settings.json`, hook scripts under
  `$HOME/.claude/hooks/`, the routine launcher at
  `$HOME/.claude/scheduled-tasks/refine_blindspot/SKILL.md`.
- **Add a new vertical** (scope frozen at `cn-sde-jobhunt`).
- **Edit anything under** `domain_knowledge/_archive/`,
  `domain_knowledge/_legacy/`, `data/_archive/`,
  `fixtures/_archive/`, `archive/**`.
- **Author paragraph content** in the three voice-work files
  (see §5).
- **Schedule itself** — scheduling is a deliberate user action via
  the `schedule` skill.
- **Add a new runtime dependency** in `pyproject.toml`.

The reviewer rejects PRs that try any of these; the subagent
abandons that attempt; the orchestrator picks a different change.

## 15. Non-negotiables

Apply to BOTH orchestrator and every subagent.

- **Never ask the user any question during the run.**
- **Never emit `HUMAN_REVIEW_REQUESTED:`.** Every situation has a
  recovery action.
- **Auto-merge on auto-review approval.** Step 12b's `gh pr merge
  --squash --delete-branch` runs without further confirmation.
- **End-of-run sync is best-effort, not a gate.** When sync fails,
  recover and continue; next run reconciles.
- **Never push directly to `main`** except the single log/ROADMAP
  commit in 12d.
- **Never `--force`** or any destructive git op.
- **Never schedule yourself.**
- **Never modify** SKILL.md / REVIEWER_PROMPT.md /
  `.claude/settings.json` / `$HOME/.claude/hooks/` / the routine
  launcher at `$HOME/.claude/scheduled-tasks/refine_blindspot/`.
  ROADMAP.md edits are explicitly allowed (Step 12d's automatic
  checkbox / progress / Last completed / Next up updates).
- **Never bypass the pre-commit hook.**
- **Never retry the same idea after auto-review rejection** —
  either address the concern or move to a different dimension.
- **Subagents do not merge their own PRs.** Sequential merge +
  conflict handling is the orchestrator's job — avoids races.
- **Subagents do not write to** `refinements/log.jsonl` or
  `docs/specs/ROADMAP.md`. The orchestrator appends all log lines
  and applies ROADMAP edits at end of run in a single commit.
- **Voice-work boundary** — refine NEVER authors paragraph content
  in `decisions.md` / `framings.md` / `blindspots.md`. Only
  skeletons and front-matter indexes.
