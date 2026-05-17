# Eval baseline measurement attempt — 2026-05-17

Status: **FAILED to produce a baseline.** No `eval/results/*.json` files
written across two attempts. `v1.x/eval-baseline-stability` roadmap item
remains OPEN with a sharper failure point.

## Goal

Per roadmap (`docs/specs/ROADMAP.md` v1.x → "Eval baseline stability"):
three consecutive `./bin/blindspot eval` runs on `main` produce
aggregate `quality_score` within ±0.03 of each other. The median of
those three is the new V1.x→V2.0 entry baseline.

The trifecta of fixes — PR #11 (JSON-parse hardening), PR #15 (per-
fixture 240s timeout), PR #16 (`bin/blindspot` finds the main `.venv/`
from a worktree) — was supposed to make eval runnable inside refine
subagents. This attempt tested whether all three landed correctly by
trying to run eval three times from a subagent worktree.

## What I ran

From worktree `/Users/moka/Documents/blindspot/.claude/worktrees/agent-a488d0e5db5f3e1ae/`
on branch `refine/20260517-121240-eval-baseline-measurement`:

1. Sourced `~/.blindspot/.env` (exports `VOYAGE_API_KEY`, `REDDIT_*`)
2. Verified `bin/blindspot` resolves the main `.venv/bin/python` via
   `git rev-parse --git-common-dir` (PR #16 logic — confirmed working;
   no "cannot locate a Python interpreter" error).
3. Launched two concurrent eval runs:
   - PID 89694 — `./bin/blindspot eval` (background, via `run_in_background`)
   - PID 89948 — `./bin/blindspot eval` (foreground tee'd into log)

## Outcome

Both processes ran for 15–17 minutes of wall time with effectively
**zero CPU usage** (0.0% sustained; ~2.6 seconds of total CPU after
17 minutes elapsed). Neither produced an `eval/results/*.json` file.
I killed both at 12:30 UTC after exceeding the 25-min total wall-clock
budget the subagent brief allows.

| PID   | Wall elapsed | CPU time | Result file |
|-------|--------------|----------|-------------|
| 89694 | 16:46        | 0:02.62  | none        |
| 89948 | 15:55        | 0:02.59  | none        |

Stderr from each run captured only the expected `WARNING:root:source
reddit-* failed: 'REDDIT_CLIENT_ID'` lines (the Reddit creds soft-fail
documented in `CLAUDE.md`). No `ValueError` from PR #11's JSON-parse
diagnostic. No `asyncio.TimeoutError` from PR #15's per-fixture
240s wrap. No wrapper error from PR #16. The processes were simply
**hung on async I/O** the entire time.

## Stack-trace evidence

`sample` on PID 89694 at the 5-minute mark showed the main thread
parked in `kevent` under an `asyncio` event loop, several frames deep
into `async_gen_asend_send` → `gen_send_ex2` → `task_step_impl`.
Re-sampled 1 minute later: same stack. This is consistent with a
subprocess pipe read that never returns — i.e. a hung
`claude-agent-sdk` query, exactly the failure mode `CLAUDE.md`'s
"Quirks" section describes (`error result: success` is the SDK's
misleading surface for a deeper auth/network failure).

But there's a wrinkle: standalone `claude -p "hi"` succeeded in
~5 seconds from this same shell (verified mid-attempt), and
`claude auth status` reports `loggedIn: true` (max subscription).
So the SDK itself is reachable. The hang is specific to how the
eval runner drives the SDK — likely concurrent contention.

## Why I think this is a CONCURRENCY problem, not a per-call hang

Three eval processes were running simultaneously when the symptom
appeared:
- PID 89092 — orphan from another worktree (`agent-ad4c599bde635880c`),
  started at 12:11 UTC, also at 0% CPU.
- PID 89694 — my background run, started 12:13.
- PID 89948 — my foreground run, started 12:14.

The orchestrator dispatches up to 4–5 refine subagents in parallel via
worktrees, and each subagent may run eval (Step 6 of `SKILL.md`).
Each eval spawns the claude-agent-sdk subprocess. When N subagents
concurrently each drive their own claude subprocess, **all of them
appear to deadlock**. The Anthropic SDK or the local OAuth-cached
session may serialize at a layer the eval doesn't anticipate.

If this hypothesis is right, then PRs #11/#15/#16 are all correctly
landed and eval is single-run-able; the bug is in concurrent
multi-subagent eval. PR #15's per-fixture timeout doesn't help because
the asyncio task never makes it past the first fixture (the timeout
clock is started but the awaited subprocess never even produces its
first token).

## Reproduce / verify

To distinguish concurrent-deadlock from per-run-hang, the next
attempt should:

1. From a clean shell on `main` with no other eval running anywhere,
   run `./bin/blindspot eval` ONCE and time it.
2. If it completes in < 5 min: concurrent contention is the root
   cause. Mitigation options:
   - Sequence eval inside the refine orchestrator (no parallel
     `Step 6`s in the same wall-clock window).
   - Add a process-level lockfile around the claude-agent-sdk
     subprocess launch in `claude_agent_client.py`.
   - Run eval against the `AnthropicAPIClient` backend (which uses
     HTTP, not subprocesses) when more than one is in flight.
3. If it still hangs: the bug is per-run. Capture a `sample` dump
   of the hung Python plus `claude -p` debug log
   (`claude -p "<test>" --debug-file /tmp/claude.log` in a separate
   shell) and grep for `oauth\|401\|auth`.

## Next concrete fix

**File:** `src/blindspot/llm/claude_agent_client.py` (and/or the eval
runner's launch path).

**Change:** Either (a) acquire a filesystem lock at the start of each
`ClaudeAgentClient` query so concurrent worktrees serialize, or (b)
switch the eval runner to `AnthropicAPIClient` when `EVAL_PARALLEL=1`
in env, on the theory that the API-key client doesn't depend on the
shared OAuth subprocess. Option (b) is more invasive but doesn't pay
serialization latency.

The roadmap item stays open. v1.x/eval-baseline-stability should now
be split (Step 2.5 framework-level edit candidate) into:
- `v1.x/eval-baseline-stability-single-run` — first prove eval
  completes once in isolation
- `v1.x/eval-baseline-stability-concurrent` — then prove N concurrent
  subagent evals each complete

The original item conflated both. The trifecta (PR #11+#15+#16)
addressed the single-run path but the data-driven question "does
3 in a row produce ±0.03 agreement" was never measured because
concurrent eval blocks the measurement from running at all.

## Files touched

- `docs/evals/baseline-attempt-20260517.md` (this file — evidence-only)

## What was NOT touched

No code changes, no config edits, no prompt edits. This attempt
is purely diagnostic — it converts an open roadmap question
("can we measure ±0.03?") into a sharper open roadmap question
("can two evals run concurrently?") with the failure mode pinned
to a specific layer (asyncio + claude-agent-sdk under concurrent
subagent worktrees).
