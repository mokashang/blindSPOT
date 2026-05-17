---
name: refine-blindspot
description: One iteration of autonomous refinement on the Blindspot project. The orchestrator reads state, then ALWAYS reflects on whether the project's framework itself needs change (high-conviction bar; usually no), then picks up to 4 concrete detail-level improvements (one per dimension). Fans out parallel subagents — each in its own git worktree — to apply, eval, PR, and auto-review independently, including an optional 5th "framework" slot when conviction is high. Merges approved PRs sequentially and logs each. Designed to run hourly via the scheduled-tasks system once trust is established — but ALWAYS invokable manually. The skill never schedules itself; that is a user action.
---

# Refine Blindspot

You are running one iteration of refinement on the Blindspot project.
Each iteration fans out **up to 5 parallel refinement attempts** — four
detail-level dimensions plus an optional framework-level slot — and
integrates the approved ones back to `main`.

Every change goes through a PR that is reviewed by a separate Claude
session before merging. There is no direct-to-main commit path. Parallel
fan-out gives N attempts per hour instead of one, while preserving the
uniform PR + auto-review flow with two layers of review (the per-commit
code-review hook plus the PR-level auto-reviewer).

## Project north star

Blindspot's long-term goal is a **universal blind-spot tool with
cross-domain reasoning** — ask about any domain and get the blind
spots someone inside that community would flag, *plus* the
alternatives from adjacent domains the asker's framing excluded.
The asker's framing is itself a blind spot the tool should fight.

The V1 design doc (`docs/specs/2026-05-13-blindspot-v1-design.md`)
narrow-scopes to "US tech career & equity" as a **tactical milestone**,
not a permanent boundary. The path from V1 to north star is encoded
in `docs/specs/ROADMAP.md`. This skill does not bake in any specific
expansion order, target domain, or capability milestone — **those
live in the roadmap**, which the orchestrator reads every run
(Step 1.5). The skill's job is to read the roadmap, advance whichever
of its bounded items has the most-leveraged concrete change available
this hour, and log progress so the next run picks up cleanly.

Specifics — which domain comes next, which cross-domain capability
to add, which deferred V1 item to promote — are roadmap decisions,
not skill decisions. If the roadmap is missing or empty, **recover**
(see "Recovery strategies" below): work on infrastructure tasks
(refresh source notes, fix a docstring, add an eval fixture) and
log the anomaly. The run still completes; the next hour tries again.

## Fully autonomous — no human in the loop

Once this skill starts, it runs end-to-end without asking the user
anything. No confirmations, no clarifying questions, no waiting for
approval. **The run always ends with a final summary line** — never
with `HUMAN_REVIEW_REQUESTED:`, never silently. The two paths:

- **Happy path** — approved PRs are merged automatically, the log is
  pushed, ROADMAP.md is updated (see Step 10). Summary line names
  the merges and the `quality_score` delta.
- **Recovery path** — something went wrong (eval broken, sync drifted,
  no candidates, all subagents abandoned, etc.). The orchestrator
  follows the table in "Recovery strategies" below: log the anomaly
  as a `recovery_attempt` entry, take the safest progress-producing
  action, continue. Summary line still gets emitted; the run is
  "completed with anomalies" rather than "failed / blocked".

The "human review" step in the workflow is **not** the user — it is a
separate `claude -p` session invoked at Step 8 with `REVIEWER_PROMPT.md`.
That session is the only reviewer. If it approves, the orchestrator
**auto-merges** the PR in Step 10b via
`gh pr merge $pr_number --squash --delete-branch`, then syncs local
main to the new remote tip (Step 10c) and pushes the run log
(Step 10d). The user does NOT
manually merge anything; the user does NOT click an "approve" button;
the user does NOT see PRs queued up for their attention (except when a
PR is left open because it was held / abandoned / conflicted, which is the
exception path, not the happy path).

Make every detail decision yourself: which dimensions to try, which
specific change to make in each, how to interpret a marginal eval
delta, how to resolve a reviewer's ambiguous feedback. The rules in
this skill are the decision boundary — when they say "if X then Y," do
Y; when they're silent, use your judgment. Never pause to ask.

## The high-level loop

```
Orchestrator (this session):
  Step 1:   Read state
  Step 1.5: Read roadmap + roadmap-progress log
  Step 2:   Evaluate previous run's PRs
  Step 2.5: Framework-level reflection (always think; rarely act)
  Step 3:   Decide which detail dimensions to attempt this run (up to 4)
  Step 4:   Fan out N parallel subagents in worktrees (one per dimension,
            plus a framework slot if Step 2.5 cleared the conviction bar)
  Step 10:  Pre-flight sync → auto-merge approved PRs → sync local
            main → append log + push → verify local==remote → prune
            worktrees

Each subagent (isolated worktree, runs in parallel with peers):
  Step 5: Apply on a fresh refine/<ts>-<slug> branch
  Step 6: Run eval on the branch
  Step 7: Push branch + open PR
  Step 8: Auto-review iteration loop (up to 3 fix-and-retry rounds)
  Step 9: Return verdict + PR number to the orchestrator (no merge here)
```

## Why parallel

Sequential refinement bottlenecks on eval. Each subagent in its own git
worktree on its own branch runs eval in parallel — N candidates per
hour. Worktrees give filesystem isolation (no agent sees another's
edits), so dimensions that touch unrelated files cleanly produce
independent PRs. Merge conflicts (when two PRs touch the same file) are
handled sequentially by the orchestrator at the end — first PR wins,
later conflicting PRs are held open.

---

## Step 1 — Read state (orchestrator)

Use Bash + Read to collect:

- Last 30 entries of `git log --oneline` to see what changed recently
- Last 10 entries of `refinements/log.jsonl` (most recent first) —
  note: the last iteration produced up to 4 lines, not just one
- The most recent file in `eval/results/*.json`
- The eval result from immediately before the most recent (for delta math)
- If it exists, `data/feedback.jsonl` (real user ratings, post-V1)
- `gh pr list --state open --search "head:refine/"` — see if any prior
  refine PRs are still open (rejected by auto-review or held by merge
  conflict). If many are open, that's a signal something needs human
  attention.

Build a short mental summary:
- What did the last refinement run change (across all parallel attempts)? How many merged vs held?
- What signal delta did each predict vs actually deliver?
- What is the current eval score?
- Are there clusters in recent `ungrounded_claims` rows?

If `refinements/log.jsonl` is empty or missing, this is a **BASELINE**
run: skip Step 2 and pick any concrete improvement to start the loop.

## Step 1.5 — Read roadmap + roadmap progress (orchestrator)

The roadmap is the source of truth for *what to build next* on the
path from V1 to the universal + cross-domain north star. The skill
does not bake in priorities — they live in the roadmap.

### What to read

1. **The roadmap itself** — `docs/specs/ROADMAP.md`. Read the full file.
   It is **version-sectioned**: V1.x / V2.0 / V3.0 / V4.0 / V5.0 each
   live in their own `##` section. Inside each version section:

   - A `Status:` line — `⬜ not started` | `🟡 in progress` | `✅ complete`
   - A `Progress: ████░░░░ X% (N/M)` bar where `N/M` is checked-vs-total
     `[ ]` checkboxes in that section
   - A `Last completed:` line (git SHA or short task id)
   - A `Next up:` line (text of the first remaining `[ ]` item)
   - **Markdown checkbox sub-tasks** (`- [ ]` / `- [x]`) — these are
     the bounded items refinement attempts. Some checkboxes nest
     sub-checkboxes for per-item definition-of-done; a parent flips
     to `[x]` only when all its children are `[x]`.
   - Sub-bullets under a checkbox (without their own `[ ]`) are the
     acceptance criteria.

   **Finding the active item:**
   - The section currently marked `🟡` is the active version.
   - The first `- [ ]` checkbox in that section is the next concrete
     item; its nested children / sub-bullets define done.

   **Fallback when the active 🟡 section has no `[ ]` items of its own**
   (e.g. V1.x in the current roadmap — it's tracked only in the §1
   version table with no enumerated checklist): scan ahead into the
   next ⬜ section's `### Per-task checklist` and `### Architecture
   changes` lists. Pick items that do NOT depend on the next
   version's `### Entry gate` conditions — typically infra refactors,
   registry-loader prep, eval-runner extensions, refine-routine
   self-improvements. These unblock the version transition and are
   concrete enough to attempt now. Tag the resulting
   `roadmap_progress` entry with `pulled_forward: true` so future
   runs see what was promoted.

   **Items too vague to drive one refinement run**: either skip
   (record `deferred` with reason in Step 10d) or propose splitting
   in Step 2.5 — roadmap edits are framework-level changes.

2. **Progress log** — filter `refinements/log.jsonl` for entries with
   `type: "roadmap_progress"`. Read at least the last 20 such entries.
   They tell you which roadmap items have been:
   - **advanced** — concrete change merged in service of this item
   - **completed** — item finished
   - **blocked** — attempted but couldn't advance; reason recorded
   - **deferred** — orchestrator chose to skip this run; reason recorded

### What to compute

For each open (not-yet-completed) roadmap item, build a short mental
record:

- `item_id` — derive stably as `<version>/<kebab-case of checkbox text,
  truncated to ~60 chars, stop-words removed>`. The roadmap doesn't
  assign ids, so consistency comes from this rule. Examples:
  - `- [ ] **Triage Officer becomes two-pass.**` in V2 §4 "Architecture
    changes" → `v2/arch/triage-officer-two-pass`.
  - `- [ ] decisions.md (≥ 8 distinct decisions ...)` under V2's
    `immigration` domain → `v2/immigration/decisions-md`.
  - `- [ ] domain_knowledge/_playbook.md ...` → `v2/playbook`.

  Slugs MUST be deterministic so future runs find the same item
  even when surrounding text drifts.
- `version` — `v1.x` | `v2` | `v3` | `v4` | `v5`.
- `pulled_forward` — `true` if the item came from the fallback path
  (active 🟡 section had no checklist; item was picked from a future
  ⬜ section).
- `layer` — which layer of the codebase advancing this item touches
  (sources / agents / config / eval / framework; see Step 3).
- `last_advanced_run_id` — most recent run that advanced or completed
  it (None if never).
- `recent_attempts` — count of advanced + blocked entries in the last
  10 runs.
- `dependencies` — other open items this depends on (only if the
  roadmap declares dependencies, typically via "after V2 reaches X%"
  language or explicit Entry gate lines).
- `status` — `open` | `in-progress` | `blocked` | `completed`.

### How this feeds Step 3 and Step 2.5

- **Step 3 (detail dimensions)** uses the open roadmap items as the
  proactive candidate pool. Each layer (sources/agents/config/eval)
  pulls candidates from: (a) the next roadmap item that lives in
  that layer and isn't blocked, plus (b) reactive eval signals.
  Step 3 picks the strongest candidate per layer.
- **Step 2.5 (framework reflection)** considers whether the roadmap
  itself needs amendment — items mis-scoped, gating wrong, north-star
  alignment drifting. Roadmap edits are framework-level changes.

### Recovery when the roadmap is in bad shape

- **`docs/specs/ROADMAP.md` does not exist** → fall back to the V1.x
  table from §1 of the missing roadmap (synthesized from this skill's
  description: refine routine maturity / API backend / eval baseline
  / streaming editor / source-view audit). Pick the most data-driven
  item this hour; log `recovery_attempt: roadmap_missing` with the
  chosen work-around. A future Step 2.5 outcome B can propose
  bootstrapping the roadmap file itself.
- **Roadmap exists but every concrete `[ ]` item is `[x]`** → pick a
  low-bar maintenance task (refresh notes, tighten docs, add an eval
  fixture). Log `recovery_attempt: roadmap_consumed`. A future
  Step 2.5 can propose adding more items as a framework-level
  roadmap edit.
- **Roadmap exists but contains no concrete `[ ]` items** (only vague
  prose intent) → same recovery: pick maintenance work. Log
  `recovery_attempt: roadmap_no_bounded_items`. Step 2.5 can promote
  some prose intent to checkboxes (≤ 2 files scope).

These recoveries replace the old "bail and ask human" path. The
roadmap is still the source of truth for priorities; refine recovers
gracefully when the file is in transition.

## Step 2 — Evaluate previous run's PRs (orchestrator)

The previous iteration may have produced multiple log entries (one per
dimension attempted). For each one, compare the predicted
`expected_signal_delta` to the actual delta computed from eval scores.
Classify each:

- **POSITIVE** — actual delta has the same sign and similar magnitude to predicted
- **NEUTRAL** — `|actual_delta| < 0.02` on the aggregate quality_score (below noise)
- **NEGATIVE** — actual delta is opposite sign to predicted, OR much smaller than predicted
- **HELD** — PR was rejected by the auto-reviewer or held due to merge conflict
- **REJECTED** — PR was rejected by the auto-reviewer (read the reason)

Use the per-dimension classifications to inform Step 3 (which
dimensions are worth trying again, which need a different angle).

## Step 2.5 — Framework-level reflection (orchestrator)

Before picking detail-level dimensions in Step 3, ask: **is the
project's framework itself in the right shape?** The four detail
dimensions all optimize *within* the current architecture (prompts,
sources, weights, agent system prompts). If the architecture itself is
miscalibrated, every detail tune is rearranging deck chairs.

This step lives BEFORE detail dimensions because: framework changes
invalidate prior eval baselines and ripple through everything; doing
this first stops detail-level subagents from wasting eval cycles on a
structure we're about to change anyway.

**You MUST do the reflection every run.** The output is usually "no
framework change this run" — that's fine. The discipline is to *seriously
consider* it every time, not to *act* every time. The bar for action is
high (below).

### Inputs to consider, in this order

1. **Trends from `refinements/log.jsonl`** — read the last 20+ entries:
   - Quality_score trajectory. Plateaued? Oscillating? Monotonic? A
     flat plateau across many runs and dimensions is the strongest
     framework-change signal — it means the detail-level surface has
     been picked clean.
   - Per-dimension batting average. Which dimensions reliably produce
     POSITIVE merges? Which produce mostly NEUTRAL/NEGATIVE/HELD?
   - Auto-reviewer rejection patterns. The same complaint recurring
     across different dimensions (e.g. "out of scope", "ungrounded",
     "no measurable signal") is a framework-level signal — agents
     themselves may be mis-scoped, or the eval may be measuring the
     wrong thing.

2. **Recent eval results** — aggregate `eval/results/*.json` over ~10
   recent runs:
   - Per-agent and per-source-view error distribution. Are errors
     concentrated on agents/sources that are structurally wrong rather
     than poorly tuned?
   - Sub-metric correlations. Are specificity / non_obviousness /
     grounding_pct / diversity moving independently, or are they
     coupled in ways that suggest the dimensions overlap?

3. **The current pipeline structure** (skim, don't deep-dive every run):
   - `src/blindspot/` — agents, prompts, scoring
   - `community_profiles/` — source views
   - `config.yaml` — weights, filters
   - `docs/specs/2026-05-13-blindspot-v1-design.md` — original design
     intent. Has reality drifted from intent? If yes, drift is either
     debt (fix the code) or learning (update the spec).

4. **External research (optional, only if a hypothesis is forming)** —
   use Bash with `gh`/`curl`/web tools to look at specific, scoped
   questions:
   - LLM-as-judge calibration literature (if questioning the eval metric)
   - Multi-agent pipeline architecture (if questioning agent topology)
   - Source-attribution / grounding methods (if questioning how the
     critic checks claims)
   - Domain-specific knowledge for tax/finance/comp (if a hypothesis is
     about missing domain context)

   Do not search exhaustively. Research a specific hypothesis, not a
   vague "what's new in LLMs". If no hypothesis has formed, skip
   research and proceed.

5. **Roadmap health check** — read alongside Step 1.5. The roadmap
   describes the path from V1 to north star; framework reflection
   asks whether the *roadmap itself* is in good shape:
   - Are open items still concrete and bounded, or have they drifted
     into vague intent?
   - Does the ordering still make sense given what's been merged?
     (E.g. an item earlier in the roadmap might now be moot because
     a later merge subsumed it.)
   - Is anything missing — a capability the north star clearly needs
     but the roadmap doesn't name yet?
   - Are detail-level runs repeatedly stuck on the same item (Step 1.5
     shows N blocked attempts on item X)? That's evidence the item is
     under-specified or depends on a structural change that should be
     promoted to framework level.

   Framework-level outcome B can include *editing the roadmap itself*
   (split an item, reorder, add a missing capability). Roadmap edits
   are framework changes because they alter what every subsequent run
   will treat as priority.

### Decision — one of two outcomes

**A. No framework change this run.** Most common. Note in your mental
state *what you considered and why you rejected it* so Step 10 can log
a one-line summary; this knowledge is then available to future runs via
the log (avoiding re-litigating the same rejected idea). Proceed to
Step 3 normally.

**B. High-conviction framework change.** Becomes a 5th parallel slot in
Step 4 alongside detail-level subagents.

### Bar for choosing B — ALL of these must be true

- **Specific data signal**. You can point at a concrete pattern in
  `log.jsonl` or `eval/results` showing the current framework is
  hitting a ceiling. Example: "quality_score has been within
  [0.71, 0.73] for the last 15 runs across all 4 dimensions"; or
  "every coverage-dimension PR in the last 6 runs got REJECTED with
  reviewer complaint 'out of scope', suggesting source-view as an
  abstraction is too narrow."
- **Specific theoretical reason** the proposed change will lift the
  ceiling, not just move it around. If derived from web research,
  include the citation in your reasoning.
- **Bounded change**. Touches ≤ ~5 files; additive when possible (add
  a new agent / new sub-metric / new fixture set, rather than rewrite
  existing). If the change is structurally invasive (refactor agent
  dispatching, change data model, swap LLM provider), it's too big for
  this loop — **don't dispatch it**. Instead, the framework slot for
  this run becomes a tiny roadmap edit (≤ 2 files: usually just
  ROADMAP.md) that **splits** the invasive change into smaller bounded
  checklist items. Those split items become future runs' detail-level
  work. Log `framework_split_proposed` in the run summary. Never
  attempt large changes silently.
- **Predicted eval delta with rationale**. Not "this should help" but
  "this should lift specificity from 0.6 to 0.65 because <causal
  mechanism>". A prediction without a falsifiable mechanism doesn't
  clear the bar.

If ANY of the four is missing, default to A. The conservatism is
intentional — framework changes are higher-risk than detail tunes and
can cause regressions that branch-eval misses (e.g. by overfitting to
the eval set).

### Examples — illustrative shapes only

The *content* of any framework change must come from data signals
plus the roadmap, not from this list. The examples below show what
kind of *shape* a bar-clearing change has — bounded, additive,
falsifiable:

- A new agent inserted at a clear seam (e.g. between triage and
  analysis), justified by a recurring failure pattern that no prompt
  edit fixes.
- A new scoring sub-metric, justified by a recurring critic complaint
  that maps to a capability the current metric can't measure.
- A new fixture set targeting a persona / situation with zero current
  coverage, justified by a real-user query pattern or roadmap item.
- An edit to `docs/specs/ROADMAP.md` itself — splitting an over-broad item,
  reordering when a merge changed the dependency graph, adding a
  missing capability the data is pointing at.

A change is in-shape if you can name (a) what file or two it touches,
(b) the data signal motivating it, (c) the predicted eval delta with
mechanism. The specific *what* — which agent, which sub-metric, which
fixture domain — comes from the roadmap and the data, not from this
file.

### Examples that do NOT clear the bar

- "Refactor the agent dispatcher" — too vague; too invasive.
- "Try a different LLM" — not falsifiable in one eval; ripples through
  everything.
- "Switch from JSON-Lines logs to a database" — orthogonal to
  refinement quality.
- "Add unit tests" — infra work, not refinement; pursue separately.
- "Reword the spec" — documentation drift fix, not framework change.

### If B is chosen — how it flows through the rest of the skill

Treat the framework change as the 5th dimension named `framework` in
Step 3's list. In Step 4 it gets its own parallel subagent with
`isolation: "worktree"`. The subagent prompt MUST include:

- An explicit `## Framework change` section in the PR description
  explaining the data signal that motivated this attempt, with
  references to specific log entries / eval files
- A note for the auto-reviewer that this is intentionally architectural
  (so "out of scope" rejections are pre-empted — the scope is the
  framework, and the PR description must make that scope explicit)
- A heightened bar for the subagent itself: if branch-eval shows
  ANY regression on quality_score (not just `< -0.02`), the framework
  subagent should abandon. The bar for framework changes is "must
  improve", not "must not clearly regress".

The reviewer at `REVIEWER_PROMPT.md` is NOT modified for framework PRs
(non-negotiable). The PR description must do the work of explaining why
the wider scope is intentional.

## Step 3 — Decide dimensions this run (orchestrator)

Detail dimensions are **named by codebase layer**, not by failure
pattern — this keeps the mapping from "what to change" to "where it
lives" unambiguous, and avoids the old overlap where two named
dimensions both touched prompts.

For each detail layer below, ask: "Is there a *specific* and
*concrete* improvement available in this layer right now?" Collect
every layer that has a concrete candidate (up to 4). If Step 2.5
chose outcome B, add `framework` as a 5th slot (its concrete change
was already specified there).

### How candidates are sourced (applies to every layer)

Each layer has two candidate streams. The strongest gets the slot:

- **Roadmap-driven** (from Step 1.5) — the next open roadmap item
  that lives in this layer and isn't blocked. The roadmap is the
  strategic priority; prefer it when there's a concrete item available.
- **Reactive** (from Step 1 + Step 2) — a measured signal showing
  something in this layer is wrong right now (low eval scores,
  recurring critic complaint, dud source-view, etc.). This is the
  tactical override when data points at something clearly broken.

When both streams point at the same layer, look for a single change
that *addresses both* (best — strategic + tactical aligned). When
they point at different things, prefer the roadmap-driven candidate
unless the reactive signal is severe (regression, broken behavior).
Record any deferred reactive issue in `next_suggested_path` so a
future run can pick it up.

### Layers

1. **Sources & knowledge** — `community_profiles/`,
   `data/source_registry.yaml`, plus (once V2 migration begins)
   `domain_knowledge/<domain>/{decisions,framings,blindspots,sources}.{md,yaml}`
   files representing Layers 1–4 of the knowledge model from
   `docs/specs/ROADMAP.md` §3. Changes: add a source-view, retire a
   low-signal one, retune `keyword_filter` / `reliability`, add
   cross-link annotation to `_schema.md`, author or extend a domain's
   decisions / framings / blindspots files (V2+). Reactive signals:
   `ungrounded_claims` clustering on uncovered topics,
   `source_view_stats` dud sources. Roadmap signals:
   coverage-expansion items, per-domain checklist sub-tasks
   (V2 §4 per-domain block), source-backlog items.

2. **Agents** — `src/blindspot/prompts/`. Changes: refine an agent's
   system prompt for clarity, instruction-following, framing breadth,
   persona handling. Reactive signals: recurring critic-feedback
   categories ("too generic", "no concrete numbers", "no alternatives
   considered", etc.) that map cleanly to a single agent. Roadmap
   signals: items like "agent X should also do Y".

3. **Config & scoring** — `config.yaml` (top-level knobs:
   `refine.quality_score_weights`, `tag_match.*`, `diversity.*`,
   `critic.thresholds`, etc.), plus the `quality_score` computation
   in `src/blindspot/eval/runner.py` (currently inline — no separate
   scoring module). Changes: tune weights / filters / thresholds,
   adjust how sub-metrics combine into `quality_score` (when the
   sub-metric itself already exists; *adding* a new sub-metric is
   framework-level). Reactive signals: signal-to-noise observations,
   sub-metric saturation. Roadmap signals: gated tuning items.

4. **Eval** — `fixtures/eval_situations.yaml` (the fixture file),
   `src/blindspot/eval/runner.py` (the runner + `quality_score`
   aggregation), `src/blindspot/eval/judge.py` (the LLM-as-judge
   prompts and parsing). Changes: add fixtures (especially as the
   roadmap advances into new personas / domains / cross-domain
   situations), refine judge prompts, fix scoring bugs in the runner.
   Reactive signals: persona / situation coverage gaps. Roadmap
   signals: items like "add fixture set for X".

5. **Framework** (only if Step 2.5 chose outcome B) — the
   architectural change specified in Step 2.5. May include editing
   `docs/specs/ROADMAP.md` itself. Higher bar, higher scrutiny; see Step 2.5.

### Concreteness

For each candidate, write down:

- File path(s) touched
- Exact edit intent
- Predicted signal delta with mechanism
- If roadmap-driven: the roadmap `item_id` it advances

The roadmap item supplies "why this", the data supplies "why now",
the prediction supplies "what we expect to learn". Examples of
acceptable concreteness:

- "Edit `community_profiles/<name>.md`: add to 'Known blind spots'
  that ... . Roadmap item: `<item_id>`. Predicted delta: +0.03
  specificity on `<persona>` fixtures."
- "Edit `config.yaml`: bump `entity_weight` from 2.0 to 2.5.
  Reactive: entity-heavy fixtures score 0.08 higher when entity
  matches dominate. Predicted aggregate quality_score delta: +0.03."

Unacceptable (too vague): "improve coverage", "make prompts clearer",
"add more sources".

### Per-layer direction rules (based on previous-run classification)

- **POSITIVE** → continue in the same layer with the next candidate
  (roadmap or reactive).
- **NEUTRAL** → switch this layer's candidate. The current line of
  attack isn't producing signal.
- **NEGATIVE** → if the previous merged change caused a regression
  that branch-eval missed, plan a `git revert` PR in this slot.
- **REJECTED** → read the auto-reviewer's reason. Address it (don't
  retry the same thing). If the rejection seems wrong, abandon this
  candidate and pick a different change rather than gaming the
  reviewer; log the reviewer-disagreement as `reviewer_disputed: <reason>`
  for weekly human audit, then continue.
- **HELD (merge conflict)** → rebase and retry in this slot, OR pick
  a different candidate for this layer.
- **BASELINE** → start anywhere reasonable (typically Sources or Eval
  first, to establish ground truth before tuning Agents or Config).

### Recovery at this step

If Step 2.5 chose outcome A AND zero detail layers have a concrete
candidate (rare — the roadmap should usually supply at least one in
some layer), don't quit. Pick a maintenance task in the Sources or
Eval layer: refresh a source-view's `notes`, tighten a fixture's
expected-output annotation, format a YAML file, add a code comment
flagging a known dud. Dispatch one subagent on that single
maintenance change. Log `recovery_attempt: no_candidates` in the
run summary. (If Step 2.5 chose B, the framework slot alone is
enough to proceed — no recovery needed.)

## Step 4 — Fan out parallel subagents (orchestrator)

For each chosen dimension (1–5, including the `framework` slot if
Step 2.5 chose B), dispatch a subagent with `isolation: "worktree"`.
**Dispatch all subagents in a single message (parallel Agent tool
calls)** so they run concurrently.

Each subagent gets a self-contained brief — it has no memory of this
orchestrator session. The brief tells it: the dimension, the specific
concrete change, the predicted delta, and points it at this SKILL.md
(Steps 5–9) for the detailed procedure (the worktree contains the same
file tree, so the subagent can `Read .claude/skills/refine-blindspot/SKILL.md`).

Use the Agent tool like this (illustrative — issue these in parallel):

```
Agent({
  description: "refine: prompt-clarity attempt",
  subagent_type: "general-purpose",
  isolation: "worktree",
  prompt: """
You are a refine-blindspot subagent. You are running ONE refinement
attempt in an isolated git worktree, in parallel with up-to-3 sibling
subagents.

## Your dimension
prompt-clarity

## Your specific change
Edit `src/blindspot/prompts/risk_officer.md`: add explicit instruction
to consider opportunity-cost framing for any situation with persona
`comparing-offers`.

## Predicted signal delta
specificity: +0.04, non_obviousness: +0.02, grounding_pct: 0, diversity: 0

## Procedure
Read `.claude/skills/refine-blindspot/SKILL.md` and follow Steps 5–9
exactly. Skip Steps 1–4 (the orchestrator already did them) and
Steps 10+ (the orchestrator will do them after you return).

Do NOT merge the PR. Do NOT push to main. Return a single JSON object
in the shape described in Step 9 — that is your only output to the
orchestrator. If you hit any abandon condition listed in "Recovery
strategies" (subagent-level), return the JSON with verdict
"abandoned" and a short reason. Try the recoveries first (smaller
change for eval regression, parse + fix for hook block, etc.) before
giving up.

The non-negotiables (see SKILL.md "Non-negotiables") apply to you too:
never push to main, never use --force, never bypass the pre-commit
hook, never modify SKILL.md / REVIEWER_PROMPT.md / .claude/settings.json
/ $HOME/.claude/hooks/blindspot-code-review-on-commit.py (the actual
hook script lives in user-home, NOT in the project tree).
"""
})
```

For a framework subagent (Step 2.5 outcome B), the brief MUST also
include: the data signal that motivated this attempt, the theoretical
reason it will lift the ceiling, the bounded scope (file list), the
heightened abandon bar ("abandon on ANY regression, not just `< -0.02`"),
and the requirement to write an explicit `## Framework change` section
in the PR description.

After all subagents are dispatched in parallel, wait for all of them to
return. Each returns one JSON object (Step 9 shape). Collect them.

## Step 5 — Apply on a fresh branch (inside subagent)

You are running inside an isolated worktree. The orchestrator already
told you the dimension and the specific change. Create your branch:

```bash
ts="$(date -u +%Y%m%d-%H%M%S)"
slug="<derive a short kebab-case slug from your intent>"
branch="refine/${ts}-${slug}"
git checkout -b "$branch"
```

(Branch names are global across the repo, but `ts` includes seconds and
each subagent's slug differs, so collisions are vanishingly unlikely.
If `git checkout -b` fails with "branch already exists", append a
2-char random suffix to the slug and retry once.)

Make the change using Edit/Write tools. The pre-commit code-review hook
will fire on each commit (catches code-quality issues for `.py`, `.ts`,
etc; allows `.md`/`.yaml`/`.json` through). If the hook blocks your
commit on a code file, address the feedback or abandon (don't bypass).

```bash
git add <files>
git commit -m "<concise message starting with 'refine:'>"
```

## Step 6 — Run eval on the branch (inside subagent)

```bash
./bin/blindspot eval     # writes eval/results/<timestamp>.json
```

(Use `./bin/blindspot` not the system-PATH `blindspot` — the wrapper
exports `PYTHONPATH=src` and bypasses the editable `.pth` file, which
on macOS Python 3.13 keeps getting `chflags hidden` re-applied by pip
and silently skipped by `site.py`. Bare `blindspot` is unreliable.)

Compute `new_quality_score - baseline_quality_score` from the report.

- If delta `< -0.02` (clear regression):
  - Abandon. Return JSON with verdict `abandoned`, reason
    `branch-eval regression: delta=<n>`. The orchestrator will not
    merge anything from this attempt.
- If delta `>= -0.02`, proceed.

## Step 7 — Push branch + open PR (inside subagent)

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

🤖 Generated by refine-blindspot skill (parallel attempt)
EOF
)"
```

Capture the PR number (e.g. `pr_number=$(gh pr view --json number -q .number)`).

## Step 8 — Auto-review iteration loop (inside subagent)

Auto-review iterates: if rejected, address the feedback, push the fix,
re-review. Cap at **MAX_ITERATIONS = 3**. On each iteration the
reviewer sees the prior rejection reasons so it can verify the fix
actually addresses them.

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
        # On TWO consecutive unparseable verdicts, abandon this attempt.
        if previous_was_unparseable:
            return {verdict: "abandoned", reason: "reviewer output unparseable twice"}
        previous_was_unparseable = True
        continue

    gh pr comment $pr_number --body "🤖 Iteration ${iteration}: ${verdict.approve ? 'APPROVE' : 'REJECT'} — ${verdict.reason}"

    if verdict.approve:
        break  # proceed to Step 9 return-verdict

    # Anti-gaming: if this rejection looks substantively similar to a
    # prior one (first 10 words match, or same noun phrase), the loop
    # isn't converging — abandon this PR (anti-gaming guard).
    if iteration > 1 and similar_to_any(verdict.reason, prior_rejections):
        return {verdict: "abandoned", reason: "reviewer rejected with same complaint twice; not converging"}

    prior_rejections.append(verdict.reason)

    # Apply fix addressing the rejection
    git add <fixed-files>
    git commit -m "refine: address review feedback (iteration ${iteration})"
    git push origin "$branch"
else:
    # MAX_ITERATIONS exhausted
    return {verdict: "abandoned", reason: "reviewer rejected ${MAX_ITERATIONS} consecutive times"}
```

**Robustness:** if `claude -p` fails outright (network, timeout) for
two consecutive iterations, return verdict `abandoned` —
don't approve on broken parsing.

## Step 9 — Return verdict to orchestrator (inside subagent)

When auto-review approves OR an abandon condition triggers, return a
single JSON object to the orchestrator (this is the subagent's final
output to the Agent tool). The subagent does **not** merge and does
**not** push to main.

Shape:

```json
{
  "dimension": "prompt-clarity",
  "pr_number": 42,
  "branch": "refine/20260516-220000-risk-officer-clarity",
  "verdict": "approved" | "held" | "abandoned",
  "reason": "<for held/abandoned: explain. for approved: leave empty or short note>",
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
    {"iteration": 1, "verdict": "reject", "reason": "Out of scope: ..."},
    {"iteration": 2, "verdict": "approve", "reason": "Scope narrowed; addresses prior rejection"}
  ],
  "files_touched": ["src/blindspot/prompts/risk_officer.md"],
  "summary": "<one-sentence what changed>",
  "rationale": "<one-paragraph why>"
}
```

`verdict` values:
- `approved` — auto-reviewer approved. Orchestrator should attempt merge.
- `abandoned` — abandoned pre-PR or during PR (branch-eval regression
  the subagent couldn't recover from, hook block it couldn't fix,
  reviewer-unparseable, etc.). PR may or may not exist; if it does,
  it's left open as evidence rather than blocking next run.
- `held` — reviewer rejected after MAX_ITERATIONS or anti-gaming
  triggered. PR is open with iteration history visible.

## Step 10 — Collect, merge, sync, log (orchestrator)

After all subagents return, you have a list of JSON verdicts. The
goal of this step is to end the run with **local main and remote main
identical**, containing all the changes from this run plus the log
append. Sync is treated as an invariant, not a best-effort cleanup.

### 10a — Pre-flight: orchestrator on clean main

Before merging anything, make sure the orchestrator's working tree
is on `main` and clean:

```bash
git checkout main

# Working tree must be clean. If it's not (untracked files / unstaged
# edits from a previous run that didn't fully clean up), auto-stash
# and proceed — see "Recovery strategies" for the unpop-at-end logic.
if [ -n "$(git status --porcelain)" ]; then
    git stash push -u -m "refine: auto-stash $ts"
    auto_stashed=1
fi

git fetch --prune origin    # update remote refs, prune deleted branches

# Replay any pending-push files from prior stuck runs (see Recovery).
for pending in refinements/pending-push-*.json; do
    [ -f "$pending" ] || continue
    apply_pending "$pending" && rm "$pending"
done

git pull --ff-only origin main   # try fast-forward to remote tip
```

If `git pull --ff-only` fails (local main has commits not on remote —
something earlier in this run pushed local-only commits, OR an outside
push happened), don't quit. Switch to `git pull --rebase origin main`.
If clean, continue. If conflict on `refinements/log.jsonl` or
`docs/specs/ROADMAP.md`, auto-resolve as described in "Recovery
strategies". If conflict on a real code file, drop the local commit
(`git reset --keep ORIG_HEAD`) and log `local_code_diverged_dropped`
with the file list, then continue.

### 10b — Auto-merge approved PRs (remote main)

Once Step 8's auto-reviewer has approved a subagent's PR, the
orchestrator merges it automatically here — no human approval
required. Sort approved PRs by `branch_quality_score` descending
(best first). For each one in order:

```bash
gh pr merge $pr_number --squash --delete-branch
```

`gh pr merge` updates **remote** main on GitHub and deletes the
remote branch. Local main is still at the pre-merge tip; we'll sync
it in 10c.

If merge fails because of a conflict (a prior PR in this run landed
an overlapping change):

- Add a PR comment explaining the conflict.
- Mark this PR's final outcome as `held` in the log (overriding the
  subagent's `approved`).
- Do not retry inside this iteration — continue to the next PR.

### 10c — Sync local main with remote (post-merges)

After ALL `gh pr merge` calls complete (whether 0 or many succeeded),
pull the new remote tip into local main:

```bash
git fetch --prune origin
git pull --ff-only origin main
```

`--ff-only` is the preferred path: if local has any commit not on
remote, fast-forward fails and we don't create a merge commit on
main. The orchestrator's only commit to main is the log + ROADMAP
append in 10d, which hasn't happened yet — so at this point local
should cleanly fast-forward over the squash-merge commits gh
created.

If `git pull --ff-only` fails (rare — would mean someone pushed
between Step 10b's `gh pr merge` and now), don't quit. Switch to
`git pull --rebase origin main`; auto-resolve any log.jsonl /
ROADMAP.md conflicts (see "Recovery strategies"). Continue to 10d.

### 10d — Append log + push (atomic both-side sync)

Now local main is at the post-merge remote tip. Build the log entries
(below) and push them as a single commit. This is the orchestrator's
ONLY direct-to-main commit per run.

Append one JSON line per subagent attempt to `refinements/log.jsonl`.
Use the subagent's returned JSON, plus:

- `timestamp`: orchestrator's start-of-run timestamp (UTC, ISO 8601)
- `run_id`: orchestrator-assigned run id (e.g. `run-20260516-2200`)
- `final_verdict`: `merged` | `held` | `abandoned` (orchestrator's call,
  not the subagent's — reflects what actually happened after merge attempt)
- `pr_status`: `merged` | `held` | `abandoned-pre-pr`
- `classification_of_previous`: from Step 2
- `next_suggested_path`: one-sentence hint for the next iteration's
  Step 3 (optional)

Append one JSON line per subagent attempt to `refinements/log.jsonl`.
Use the subagent's returned JSON, plus:

- `timestamp`: orchestrator's start-of-run timestamp (UTC, ISO 8601)
- `run_id`: orchestrator-assigned run id (e.g. `run-20260516-2200`)
- `final_verdict`: `merged` | `held` | `abandoned` (orchestrator's call,
  not the subagent's — reflects what actually happened after merge attempt)
- `pr_status`: `merged` | `held` | `abandoned-pre-pr`
- `classification_of_previous`: from Step 2
- `next_suggested_path`: one-sentence hint for the next iteration's
  Step 3 (optional)

**Additionally, append exactly one line per run** describing the
framework reflection from Step 2.5, so future runs can see what was
considered and rejected (avoids re-litigation):

```json
{
  "timestamp": "...",
  "run_id": "run-20260516-2200",
  "type": "framework_reflection",
  "outcome": "A" | "B",
  "considered": "<one-sentence summary of the hypothesis you evaluated>",
  "decision_reason": "<one-sentence why you chose A or B — which bar item failed (A) or which signals cleared the bar (B)>",
  "data_signals_examined": ["log trajectory: <observation>", "auto-reviewer rejections: <pattern>", "..."]
}
```

If outcome B, this line goes in addition to the dimension's regular
log line (Step 9 shape with `dimension: "framework"`).

**Additionally, for each roadmap item touched this run** (either
advanced, completed, blocked, or deferred), append one
`roadmap_progress` line so the next run's Step 1.5 can read it:

```json
{
  "timestamp": "...",
  "run_id": "run-20260516-2200",
  "type": "roadmap_progress",
  "item_id": "<roadmap item id>",
  "layer": "sources" | "agents" | "config" | "eval" | "framework",
  "action": "advanced" | "completed" | "blocked" | "deferred",
  "pr_number": 42,
  "final_verdict": "merged" | "held" | "abandoned",
  "summary": "<one-sentence what this run did toward the item>",
  "reason": "<for blocked/deferred: why; for advanced/completed: empty or short note>",
  "next_step_hint": "<optional one-sentence pointer for the next run>"
}
```

Action semantics:
- `advanced` — concrete change merged in service of this item; item
  still has more work.
- `completed` — item finished. The next Step 1.5 should treat this
  item as done.
- `blocked` — attempted, subagent abandoned / held / the auto-reviewer
  flagged something the orchestrator can't fix in this run.
- `deferred` — orchestrator chose not to attempt this item this run
  (e.g. reactive signal preempted it, or another item was
  higher-leverage). Not a failure, just sequencing.

If a roadmap item was the source of a subagent's slot but the
subagent abandoned/held without an advanced merge, emit a `blocked`
entry. If the item was named in Step 3 but skipped in favor of a
reactive candidate, emit a `deferred` entry.

### Update ROADMAP.md when items advance or complete

For every `roadmap_progress` entry written above with
`action: "advanced"` or `"completed"`, ALSO edit
`docs/specs/ROADMAP.md` so its checkbox / progress / last-completed /
next-up state matches reality. ROADMAP §2 declares "the progress bar
is the contract" — without these edits a human reader has no way to
see what's done. ROADMAP.md edits go into the SAME commit as the log
append below.

For each such entry, in the relevant version section:

1. **Checkbox**. If `action: "completed"`, change the matching
   `- [ ]` to `- [x]`. Match by the slug used in `item_id` — if the
   checkbox text drifted since the run started and the slug no
   longer round-trips, search by fuzzy substring of the original
   checkbox text (case-insensitive, ignore punctuation). If still no
   match (item heading changed substantively), record
   `roadmap_drift: item <id> no longer locatable` in the log instead
   of editing ROADMAP.md, and skip the rest of this entry's ROADMAP
   updates. The log still captures progress; humans can reconcile
   later. For `action: "advanced"` (item still has more work), leave
   the box unchecked but still update Last completed / Next up.
2. **Progress bar**. Recompute the version's
   `Progress: ████░░░░ X% (N/M)` line. `N` = count of `[x]` in that
   section, `M` = count of `[ ]` + `[x]`. Render exactly 20
   characters: `█` × round(X / 5), then `░` for the remainder. Show
   the percentage rounded to nearest integer.
3. **Last completed**. Replace with the squash-merge short SHA of
   the PR that advanced this item (`git rev-parse --short
   origin/main` after Step 10c). If multiple items in the same
   section advanced this run, use the SHA of the highest-leverage
   advance (or the most recent).
4. **Next up**. Replace with the text of the first remaining
   `- [ ]` checkbox in the same section. If the section has no
   remaining `[ ]`, write `(none — version complete)`.
5. **Status promotion**. If every sub-task in a `🟡 in progress`
   section is now `[x]`, change `Status: 🟡 in progress` to
   `Status: ✅ complete` AND promote the next `⬜ not started`
   section to `🟡 in progress`.

If the item was `pulled_forward: true` (the fallback path picked it
from a future ⬜ section), flip the checkbox in that future
section. Its progress bar will start showing non-zero. Do NOT
promote that future section to `🟡` yet — promotion only happens
once the currently-active 🟡 version's checkboxes are all `[x]`.

Commit and push the log + ROADMAP.md edits atomically (one commit
total per run, regardless of how many attempts), with one rebase-
retry on push race:

```bash
git add refinements/log.jsonl docs/specs/ROADMAP.md
git commit -m "refine: log iteration $ts (N attempts, M merged, K held; framework: A|B; roadmap: P advanced, Q completed)"

# Push, with up to 5 attempts and exponential backoff on race
# (someone else pushed between our pull and now). On each retry,
# rebase onto the new remote tip and try again.
attempt=1
backoff=2
while ! git push origin main; do
    if [ $attempt -ge 5 ]; then
        # All 5 push attempts failed. Save pending log + ROADMAP edits
        # to a side file so the next run can replay them at Step 10a.
        # Don't quit the run — emit a final summary line saying push
        # deferred and exit cleanly.
        save_pending_push "refinements/pending-push-$ts.json"
        log_anomaly "push_deferred" "after 5 attempts, $attempt × backoff"
        break
    fi
    sleep $backoff
    backoff=$((backoff * 2))
    attempt=$((attempt + 1))
    git fetch origin
    if ! git pull --rebase origin main; then
        # Rebase conflict on log.jsonl or ROADMAP.md (auto-resolvable;
        # see Recovery strategies — log.jsonl is append-only, ROADMAP
        # checkbox flips union). If auto-resolve also fails, save
        # pending and break out.
        if ! auto_resolve_rebase_conflict; then
            save_pending_push "refinements/pending-push-$ts.json"
            log_anomaly "rebase_unresolvable" "$(git status --porcelain)"
            git reset --keep origin/main   # safe — fails if would lose work
            break
        fi
    fi
done
```

The `save_pending_push` / `apply_pending` / `auto_resolve_rebase_conflict`
helpers are conceptual — implement them inline as needed. The
invariant is: **the run always completes**, even if push couldn't
land this hour; pending files get replayed at the next run's
Step 10a (see Recovery strategies).

### 10e — Sync verification (invariant check)

After 10d, verify local and remote main are identical. This is the
end-of-run invariant:

```bash
git fetch origin
local_sha=$(git rev-parse main)
remote_sha=$(git rev-parse origin/main)
if [ "$local_sha" != "$remote_sha" ]; then
    # Re-fetch once in case the prior fetch hit a transient hiccup,
    # then log the observed divergence and continue. The run still
    # completes; the next run's Step 10a will reconcile via stash +
    # rebase recovery.
    git fetch origin
    local_sha=$(git rev-parse main)
    remote_sha=$(git rev-parse origin/main)
    if [ "$local_sha" != "$remote_sha" ]; then
        log_anomaly "sync_divergence_observed" "local=$local_sha remote=$remote_sha"
    fi
fi
```

The happy path is local SHA == remote SHA. The recovery path logs
the divergence and continues; the run still emits its final summary
line.

### 10f — Worktree cleanup (best-effort)

Subagent worktrees aren't auto-cleaned when the agent makes commits.
Prune them at end of run:

```bash
git worktree prune
git worktree list  # sanity check — should only show main
```

If stale worktree dirs remain (rare), the next `prune` will catch them.
Don't block the run on cleanup failure — but note: stale worktrees
themselves don't affect the local↔remote main sync invariant.

## Final summary line

End the orchestrator run with one line, e.g.:

```
run-20260516-2200: 3 dimensions attempted (prompt-clarity, coverage, signal-noise) → 2 merged, 1 held (merge conflict); aggregate quality_score 0.71 → 0.76
```

---

## Recovery strategies — never stop, always make progress

The orchestrator NEVER terminates the run early. Every run ends with
the final summary line + log appends + ROADMAP.md update (if any
item advanced or completed) — never with a `HUMAN_REVIEW_REQUESTED:`
line. When a situation in the tables below applies, do the recovery
action; when none applies, fall back to: **log the anomaly as a
`recovery_attempt` entry, take the safest action that still produces
some progress, continue the run.**

The hourly cron makes this design choice non-negotiable: a stuck run
blocks the entire automation pipeline for an hour. Recovering from a
problem and trying alternatives is always better than stopping. The
log captures what was tried so weekly human review can spot patterns
that need real attention.

### Orchestrator-level recoveries

| Situation | Recovery action |
|---|---|
| Eval suite fails to run at all (Step 1 sanity check) | Try `pip install -e .`; on macOS Python 3.13 also `chflags -R nohidden .venv` (see CLAUDE.md "Quirks"); re-run eval. If still broken, scope this run to dimensions that don't need eval (e.g. doc/comment refinement) and queue "fix eval pipeline" as a V1.x roadmap item via Step 2.5 outcome B. Log `recovery_attempt: eval_broken`. |
| Step 2.5 = A AND zero detail layers have a concrete candidate (Step 3) | Pick a low-bar maintenance task: refresh a source-view's `notes`; tighten a docstring; add an eval fixture; lint a YAML file. Log `recovery_attempt: no_candidates`. |
| All subagents in this run returned `abandoned` or `held` | Don't quit. Run a second round with cheaper attempts — smaller scope, lower-bar dimensions (cosmetic doc edits, formatting). If round two also produces 0 merges, log `recovery_attempt: round_two_empty` and finish the run with a summary "0 merged, recovery rounds exhausted". Cron retries next hour. |
| Same `dimension` produced 5+ `held` / `abandoned` in last 10 log lines (no `merged` interspersed) | Don't attempt that dimension this run; pick others. Log `dimension_paused: <dim>` once. Resumes automatically when stale entries roll off the 10-line window. |
| Framework change identified in Step 2.5 is structurally invasive (> ~5 files, refactor-style, LLM-provider swap, etc.) | Don't dispatch the large change. Instead: propose a roadmap edit (a tiny Step 2.5 outcome B with scope ≤ 2 files) that **splits** the large item into smaller bounded checklist items in ROADMAP.md. The split items become future runs' detail-level work. Log `framework_split_proposed`. |
| **Step 10a — orchestrator's working tree not clean** | `git stash push -u -m "refine: auto-stash $ts"`, proceed. At end of 10d, attempt `git stash pop`; on conflicts, leave the stash entry in place (don't drop), log `auto_stash_unpopped`. Manual cleanup becomes a no-rush task; the run still completed. |
| **Step 10a / 10c — `git pull --ff-only` fails** (local diverged from remote) | Switch to `git pull --rebase origin main`. If clean, continue. If conflict on `refinements/log.jsonl` or `docs/specs/ROADMAP.md`, auto-resolve: log.jsonl is append-only — take both sides sorted by `timestamp`; ROADMAP.md — prefer the union of `[x]` flips and recompute the progress bar afterward. If conflict on a real code file (unexpected — orchestrator shouldn't have local code changes), drop the local commit (`git reset --keep ORIG_HEAD`) and log `local_code_diverged_dropped` with the file list. |
| **Step 10d — log push fails after first rebase-retry** | Retry up to 5 total attempts with exponential backoff (2 s, 4 s, 8 s, 16 s, 32 s — ~62 s max). On each retry: `git fetch origin && git rebase origin/main`, then push. If all 5 fail, save the pending log + ROADMAP edits to `refinements/pending-push-<ts>.json` (one file per stuck attempt), log `push_deferred`, continue. Next run's Step 10a / 10c detects `refinements/pending-push-*.json` files and replays them before doing its own work. |
| **Step 10d — rebase auto-resolve impossible** (extremely rare) | Save changes to `refinements/pending-push-<ts>.json`; log `rebase_unresolvable` with the rebase stderr. Reset local to `origin/main` (`git reset --keep origin/main` is safe — only succeeds if no local changes would be lost). Continue. |
| **Step 10d — cannot locate ROADMAP.md checkbox for an `item_id`** (slug round-trip failure) | Search by fuzzy substring of the original checkbox text (case-insensitive, ignore punctuation). If still no match (item heading changed substantively between runs), record `roadmap_drift: item <id> no longer locatable` in the log instead of editing ROADMAP.md. The log + the unedited ROADMAP.md still capture progress; humans can reconcile later. |
| **Step 10e — SHA mismatch** (local main ≠ remote main at end) | Re-fetch (`git fetch origin`), re-compare. If still mismatched, log `sync_divergence_observed: local=<sha> remote=<sha>` and continue. Next run's 10a sees a non-clean tree and uses the stash recovery. |
| Git op fails for unknown reason (network, permission, transient) | Retry once with 3× timeout. If still failing, log `git_op_failed: <op> <error>` and continue with the next operation in the sequence. Skip the failed one; orchestrator does its best to make the rest of the run still produce a summary. |
| Across runs, the last 3 produced zero merged PRs | A trend, not an event. Log `cold_streak_observed` (a marker entry, NOT an exit signal). Continue this run normally. The trend will self-correct or weekly human review will catch it via the log. |
| **Pending push files exist at Step 10a start** (`refinements/pending-push-*.json` from a prior stuck run) | Before this run's own work, attempt to replay each pending file in chronological order: load its log entries + ROADMAP edits, apply on top of current local main, push. On success, delete the pending file. On failure, leave it and log `pending_replay_failed: <file>`. Then proceed with this run's normal work. |
| Catastrophic unexpected error (uncaught exception anywhere) | Wrap `try / except Exception` at the orchestrator's top level. On any uncaught exception: log `unexpected_error: <type> <reason>` with traceback to `refinements/log.jsonl`, emit a final summary line saying "errored; see log", exit cleanly. The run produces SOMETHING the user can read — never a silent dead end. |

### Subagent-level recoveries

Subagents return verdicts (`approved` / `held` / `abandoned`) for
per-attempt outcomes. These are NOT run terminations — the
orchestrator absorbs them and counts in the summary. Before returning
`abandoned`, a subagent should TRY:

- **Branch eval regression `< -0.02`** (or any regression for a
  framework subagent): try ONE smaller version of the change — cut
  the knob delta in half, or pick a narrower file scope. If that
  still regresses, return `abandoned` with reason.
- **Pre-commit hook block**: parse the hook's stderr. If it names a
  specific fixable issue (style, missing type hint, unused import),
  apply the fix and retry the commit. If the same block fires twice
  in a row on the same file, return `abandoned`. Never bypass with
  `--no-verify` or env-var skips.
- **MAX_ITERATIONS (= 3) auto-review exhausted**: return `held`. The
  PR stays open; orchestrator's next-run Step 3 picks a different
  candidate in this layer.
- **Reviewer rejects with substantively similar complaint** to a
  prior iteration: return `held` with reason `not_converging`.
  Anti-gaming guard. (This is the one place "trying harder to fix
  it" is actively wrong — if the same complaint recurs, the loop
  has stopped making real progress and should stop spinning.)
- **Reviewer verdict unparseable twice in a row**: return `abandoned`
  with reason `reviewer_unparseable`. The reviewer may be in a bad
  state; orchestrator can retry this layer next run with a fresh
  reviewer invocation.

The verdict name is `abandoned` (renamed from `bailed` in earlier
versions of this skill — the new name reflects the design intent:
this specific change didn't work, the run continues). "Abandon this attempt"
captures the intent: this specific change didn't work, but the run as
a whole continues with other attempts.

### What stays as hard "don't do"

These are constraints, not recovery conditions. The orchestrator and
subagents must refuse to attempt them in the first place; the PR
auto-reviewer rejects any PR that tries them, which makes the subagent
abandon that attempt (not retry harder):

- **Push directly to `main`** from anywhere — only Step 10d's single
  log + ROADMAP commit is allowed, and only on `main` itself.
- **`git push --force`** or any destructive git operation (`reset
  --hard`, `branch -D` on a branch with unpushed commits, `clean -f -d`,
  etc.).
- **Bypass the pre-commit code-review hook** (`--no-verify`,
  `BLINDSPOT_SKIP_REVIEW=1`, deleting / disabling the hook script,
  removing the matcher in `.claude/settings.json`, etc.).
- **Modify any of:** `REVIEWER_PROMPT.md`, this `SKILL.md`,
  `.claude/settings.json` (repo-level hook config), OR the hook
  scripts at `$HOME/.claude/hooks/blindspot-code-review-on-commit.py`
  (and any sibling files under `$HOME/.claude/hooks/`). The hook
  system spans both: repo `settings.json` wires it up, user-home
  script does the actual review. Modifying either silently weakens
  pre-commit safety. The reviewer rejects PRs that touch any of
  these paths.
- **Schedule itself.** Scheduling is a deliberate user action via the
  `schedule` skill, after the user watches this skill run 3–5 times
  manually.
- **Modify a closed or merged PR.**

If a PR or commit attempts any of these, the reviewer rejects it,
the subagent abandons that attempt, and the orchestrator picks a
different change. No bail, just routing.

## Non-negotiables

These apply to BOTH the orchestrator and every subagent.

- **Never ask the user any question during the run.** Make every
  detail decision yourself. The rules in this skill are the decision
  boundary; when they say "if X then Y," do Y; when silent, use your
  judgment. The only user-facing output is the final summary line at
  end of run.
- **Never emit `HUMAN_REVIEW_REQUESTED:`.** Every situation that
  would historically have bailed now has a recovery action above. If
  none applies, log the anomaly and continue with the safest
  progress-producing action. Cron must never get stuck.
- **Auto-merge on auto-review approval.** When the Step 8 reviewer
  (`claude -p` with `REVIEWER_PROMPT.md`) approves a PR, the
  orchestrator merges it in Step 10b via `gh pr merge --squash
  --delete-branch` without any further confirmation. Never leave an
  approved PR open waiting for a human.
- **End-of-run sync is best-effort, not a gate.** On the happy path,
  local `main` and remote `origin/main` end at the same commit SHA.
  Step 10's fetch / fast-forward-only pull / push-with-rebase-retry /
  end-of-run SHA check are the mechanisms. When something goes wrong,
  the recovery strategies above keep the run going even if perfect
  sync isn't achievable this hour — the next run reconciles. Sync is
  a goal, not a termination gate.
- Never push directly to `main` from any session. All code changes go
  through PR + auto-review. The orchestrator's only direct-to-main
  commit is the single log + ROADMAP commit in Step 10d.
- Never use `git push --force` or any destructive git operation.
- Never schedule yourself. Scheduling is a deliberate user action via
  the separate `schedule` skill.
- Never modify `REVIEWER_PROMPT.md`, this `SKILL.md`,
  `.claude/settings.json`, or any file under `$HOME/.claude/hooks/`
  (where the pre-commit review script actually lives). The
  auto-reviewer rejects PRs touching these; if a subagent thinks one
  of these needs a change, it abandons and the orchestrator picks a
  different change. Roadmap edits to `docs/specs/ROADMAP.md` are
  explicitly allowed (Step 2.5 outcome B for content, Step 10d for
  automatic checkbox / progress / Last completed / Next up).
- Never bypass the pre-commit code-review hook (no `--no-verify`,
  `BLINDSPOT_SKIP_REVIEW=1`, no deleting the hook script). If the
  hook blocks a commit, address the issue or abandon.
- If the auto-reviewer rejects, do not retry the same idea. Either
  address the reviewer's concern or move to a different dimension.
- Subagents do not merge their own PRs and do not push to `main`.
  Sequential merge + conflict handling is the orchestrator's job —
  this avoids races between parallel subagents on `main`.
- Subagents do not write to `refinements/log.jsonl` or
  `docs/specs/ROADMAP.md`. The orchestrator appends all log lines and
  applies ROADMAP edits at end of run in a single commit (Step 10d).
