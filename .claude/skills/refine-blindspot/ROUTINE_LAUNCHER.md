# Refine Routine Launcher — copy to user home

This is the content that should live at
`~/.claude/scheduled-tasks/refine_blindspot/SKILL.md` — it's the
prompt the hourly cron invokes. Claude Code's harness blocks the
assistant from writing user-home paths directly, so the file is
staged here. After the scope-narrow pivot PR is merged, copy this
file into place:

```bash
cp .claude/skills/refine-blindspot/ROUTINE_LAUNCHER.md \
   ~/.claude/scheduled-tasks/refine_blindspot/SKILL.md
```

Also: until the pivot PR is merged on `main`, pause the cron
manually:

1. Run `mcp__scheduled-tasks__list_scheduled_tasks` to confirm
   `refine_blindspot.enabled == true`.
2. Call `mcp__scheduled-tasks__update_scheduled_task` with
   `taskId: refine_blindspot, enabled: false`.

The new launcher below is also defensive — it self-pauses if the
ROADMAP sentinel is missing — but disabling the cron is cleaner
during the transition.

---

(The file below this marker is the launcher proper. Everything
above this marker is meta-context; the cron should never see it.
Delete everything down to and including the `==== LAUNCHER ====`
marker before saving to user home, OR copy literally — the launcher
content below tolerates the preamble being present because the
sentinel check runs early.)

==== LAUNCHER ====

---
name: refine_blindspot
description: refine blindspot (scope-narrowed; portfolio-track; V2-narrow / V3-ui / V4-freeze checklist only)
---

Run one iteration of the refine-blindspot skill on the Blindspot
project.

## Project orientation (read every run)

Blindspot was scope-narrowed on **2026-05-18**. The original V1 → V5
plan (universal cross-domain blind-spot tool) is **deprecated**. The
project is now a single-vertical advisor — **Chinese international
students in the US making SDE job-hunt and visa-coupled career
decisions** — being completed as a portfolio artifact, then frozen.

The trajectory lives in `docs/specs/ROADMAP.md`:

- **V2-narrow** (🟡 in progress) — build the `cn-sde-jobhunt` vertical
  to depth across the 4-layer knowledge model.
- **V3-ui** (⬜ pending) — minimal browsable web UI (Next.js + React +
  TS recommended; FastAPI backend) with streaming and citation
  rendering.
- **V4-freeze** (⬜ pending) — pin deps, write the portfolio README,
  disable this cron, tag `v1.0-final`.

The hourly cron exists to help the user reach V4-freeze. Once
V4-freeze is reached, the cron is part of what gets disabled.

## Pre-flight: pivot sentinel check

The 2026-05-18 pivot is large. Until the pivot PR is merged to
`main`, this routine **must not run** — running the new procedure
against the old ROADMAP / data layer would produce nonsense PRs and
waste eval cycles.

Before doing anything, run this check from a fresh worktree of the
project:

1. `cd` into the project repo (`/Users/moka/Documents/blindspot/`)
2. `git fetch --prune origin` → ensure latest main is local
3. `git -C . show origin/main:docs/specs/ROADMAP.md | head -5`
4. If the output contains the literal string
   `Scope-Narrowed, Portfolio-Track` (the new ROADMAP's H1
   subtitle), proceed with the run.
5. **Otherwise**, log `routine_paused_pivot_unmerged` to
   `refinements/log.jsonl` on a fresh worktree branch (no merge,
   no PR — just append + push), emit a one-line summary:
   `run-<ts>: routine paused — 2026-05-18 pivot not yet merged on main`,
   and exit cleanly.

The sentinel is intentionally simple. If a later refactor changes
the H1 subtitle, this check no-ops and the routine pauses until the
user manually verifies and updates the sentinel — that is a feature,
not a bug.

## When the pivot is merged

Invoke the project-local skill at
`.claude/skills/refine-blindspot/SKILL.md` and follow it exactly.
The narrow-scope skill is much shorter than the previous version —
no 10-domain reasoning, no framework reflection, hard-coded scope
to the V2-narrow / V3-ui / V4-freeze checklists in ROADMAP.md.

The high-level loop:

1. **Step 1 — Read state.** `git log --oneline -30`; last 10
   `refinements/log.jsonl` entries; most recent eval result; any
   open `refine/...` PRs.
2. **Step 2 — Classify previous run's PRs.** POSITIVE / NEUTRAL /
   NEGATIVE / REJECTED / HELD per their eval delta and reviewer
   verdicts. (No framework reflection — scope is frozen.)
3. **Step 3 — Pick UP TO 3 detail dimensions.** Layers:
   - **knowledge-schema** — schema-driven content the refine loop
     may author: source-view YAML entries, community profile
     sections (Voice / Mental model / Typical concerns / Known blind
     spots OF this community), tag-taxonomy additions, fixture
     entries. **NOT** decisions/framings/blindspots *paragraph
     content* — that is voice work the user authors.
   - **agents-and-config** — prompt tweaks
     (`src/blindspot/prompts/*.md`), scoring weights
     (`config.yaml`), critic thresholds, banlist additions.
   - **eval** — `fixtures/eval_situations.yaml` additions, judge
     prompts, `quality_score` aggregation tweaks.
   - **web-infra** (only when V2-narrow is mostly done and V3-ui is
     active) — `src/blindspot/web/` scaffolding, FastAPI routes,
     streaming wrapper, Next.js / React surfaces, citation hover
     rendering.
4. **Step 4 — Fan out** parallel subagents in worktrees, one per
   dimension. Single Agent-tool message with parallel calls.
5. **Step 5–9 (subagent)** — branch → apply → eval → push → open PR
   → auto-review loop (max 3 iterations) → return JSON verdict.
6. **Step 10 (orchestrator)** — pre-flight sync, auto-merge approved
   PRs by `branch_quality_score` desc, sync local main, append log
   lines + update ROADMAP checkbox/progress/Last-completed/Next-up,
   push, verify, prune worktrees.

## Hard limits — voice-work boundary

The refine routine **never authors**:
- `domain_knowledge/cn-sde-jobhunt/decisions.md` paragraph content
- `domain_knowledge/cn-sde-jobhunt/framings.md` paragraph content
- `domain_knowledge/cn-sde-jobhunt/blindspots.md` paragraph content

These three files are *voice work* — they encode the author's
insider knowledge of the Chinese international student SDE
community. Refine cannot fake that voice; the user authors them
manually or via deliberately-scoped Claude conversations outside
this routine.

Refine MAY:
- Add an *empty* entry skeleton (decision name + scope + framing
  axes placeholders) that the user fills in.
- Tighten the *schema* of an existing entry without changing content.
- Add new framings to the **front-matter index** of `framings.md`
  when `sources.yaml` references one not yet listed.

The auto-reviewer enforces this — any PR that adds paragraph
content under those three files is rejected with
`voice_work_violation`.

## Hard limits — out of scope

The auto-reviewer always rejects PRs that:
- Add a new vertical domain (scope is frozen at `cn-sde-jobhunt`).
- Edit anything under `*_archive/`, `*_legacy/`, or `archive/**`.
- Modify `.claude/settings.json`, `.claude/hooks/**`, the skill
  files themselves, or `$HOME/.claude/hooks/`.
- Add new runtime dependencies in `pyproject.toml`.
- Delete tests or eval fixtures.
- Author paragraph content in the three voice-work files.

## No human in the loop, no `HUMAN_REVIEW_REQUESTED`

Operate fully autonomously. Make every detail decision yourself.
The non-negotiables and recovery strategies in the project SKILL.md
keep the run progressing through any failure mode — eval broken,
sync drift, all subagents abandoned, push race, etc. End-of-run
sync (`local main == origin/main`) is best-effort, not a gate.

End the run with a one-line summary:

```
run-<ts>: N layers attempted (...) → M merged, K held, J abandoned;
  V2-narrow P/13 advanced; V3-ui Q/7 advanced; V4-freeze R/6 advanced;
  aggregate quality_score <prev> → <new>
  [recovery: <count> anomalies, see log]
```

## When V4-freeze completes

When all V4-freeze checklist items in ROADMAP.md are `[x]`, this
routine logs `v4_freeze_reached` and emits a summary line
recommending the user disable the cron via
`mcp__scheduled-tasks__update_scheduled_task` with `enabled: false`.
The routine continues to run hourly (still doing nothing) until the
user disables it; this is intentional — the routine cannot disable
itself per the non-negotiables.
