# Blindspot — Long-Range Technical Roadmap

**Date:** 2026-05-16 (initial); update on every version transition.
**Status:** Active.

This document has **no time estimates**. It tracks progress, not
schedule. Any Claude session reading this should be able to answer
in 30 seconds: *what version are we on, what sub-task is next, what
was last completed*.

## 0. The end-state we are building toward

A decision-aware advisor that, given **any decision in any life
domain**, surfaces the blind spots the user has not considered —
**including blind spots from outside the framing the user posed the
question in.**

Two capability axes define "done":

1. **Domain coverage** — any decision domain a person might face.
   V1 covers one (US tech career & equity).
2. **Frame-breaking** — when the user poses a narrow question
   ("how do I earn more as an SDE?"), the system surfaces blind
   spots *across alternative framings of the same deep goal*
   ("you're optimizing within SDE; here's what high-skill trades /
   founding / domain-switch look like for the deep goal of
   earning more in the US"). V1 does not do this.

These axes are not the same problem and the roadmap sequences them
**coverage-first**. Frame-breaking cannot pivot to a domain whose
knowledge the system does not have. You must have all the knowledge
before you can architect crossings between pieces of it.

## 1. Versioning strategy

Capability-jump versioning. Each major (V2/V3/V4/V5) corresponds to
one capability the previous version did not have. V1.x patch
releases harden foundations without expanding scope.

| Version | Capability jump | Status |
|---|---|---|
| V1.0 | Single-domain 6-agent pipeline works end-to-end | ✅ shipped |
| V1.x | Refine loop in production; API backend; eval stable | 🟡 in progress |
| V2.0 | 10 core domains, each fully built across the 4-layer knowledge model in §3 | ⬜ proposed |
| V3.0 | Scaled curation: 10 → all indexable domains via semi-automated discovery | ⬜ proposed |
| V4.0 | Frame-breaking: cross-domain blind spots from alternative framings | ⬜ proposed |
| V5.0 | Universal access: multi-user, web/mobile UI, personalization, productionization | ⬜ proposed |

**Key reorder vs an earlier draft:** scaled curation (V3) now
precedes frame-breaking (V4). Reason: you cannot pivot a question
into framings whose domain knowledge does not yet exist. V4 must
inherit a populated knowledge base from V3.

## 2. How to read the progress tracker

Each version section in §§4–8 contains:

```
Status: ⬜ not started | 🟡 in progress | ✅ complete
Progress: ████░░░░░░░░░░░░░░░░ 20% (2/10)
Last completed: <git SHA or task ID>
Next up: <single concrete sub-task>
```

The progress bar **is the contract**: it is what tells the next
Claude session where to resume. Update it every time a sub-task
moves from `[ ]` to `[x]`. The "Last completed" / "Next up" lines
are redundant with the checkbox state but exist as a quick read
without scanning the full checklist.

Sub-tasks live as markdown checkboxes inside each version section.
A sub-task is "done" only when its definition-of-done bullets are
all checked. Partial sub-tasks stay `[ ]` with a `(in progress)`
suffix and a 1-line note of what's left.

When a refine routine or a manual Claude session does work toward
a version, the workflow is:

1. Find the version section with status 🟡.
2. Find the first `[ ]` sub-task. Read its definition of done.
3. Do that sub-task. When done, change `[ ]` → `[x]`, update
   "Last completed" and "Next up", recompute the percentage,
   commit.
4. Push.

## 3. The 4-layer knowledge model

This is the most load-bearing decision in the whole roadmap.
V1 built only Layer 4 explicitly. V2+ build all four.

| Layer | What it is | V1 status |
|---|---|---|
| 1. Decision ontology | The set of decisions that exist in a domain | implicit (in author's head) |
| 2. Framing library | The lenses through which each decision can be viewed | implicit (encoded in community_profiles) |
| 3. Blindspot catalogue | What each framing typically misses | partially implicit (in community_profiles' "blind spots OF this community" sections) |
| 4. Source-view | Where each of layers 1–3 can be cited from | explicit ([data/source_registry.yaml](../../data/source_registry.yaml)) |

### Why this model

V1 ran fine without layers 1–3 being explicit because the author
*is* the tech-career domain expert. He could write a community
profile that implicitly encodes which decisions matter, which
framings are standard, and which blind spots are typical. None
of this scales to domains the author is not personally inside.

Worse: the V1 pipeline implicitly assumes a one-shot mapping —
the user's situation → relevant source-views → community
analysts → blind spots. That works when "relevant" is a small,
known graph. Across all domains, "relevant" is enormous, and
the pipeline has no model of *which decisions in which domains
the user is actually navigating*. Layer 1 makes that explicit.

### File layout (V2 introduces this)

```
domain_knowledge/
  _schema.md                      # writing guide
  _meta_ontology.md               # top-level taxonomy of life decisions
  <domain>/
    decisions.md                  # Layer 1
    framings.md                   # Layer 2
    blindspots.md                 # Layer 3
    sources.yaml                  # Layer 4 — per-domain source-views
    communities/                  # community_profiles scoped to this domain
      <community-tag>.md
    fixtures/                     # eval situations for this domain
      <fixture-id>.yaml
    domain_pack.md                # Triage/Editor/Critic prompt overrides
```

Migration of V1: the current
[data/source_registry.yaml](../../data/source_registry.yaml) gets
split into `domain_knowledge/tech-career/sources.yaml`. The current
[community_profiles/](../../community_profiles/) entries move into
`domain_knowledge/tech-career/communities/`. The registry loader
([src/blindspot/sources/registry.py](../../src/blindspot/sources/registry.py))
gets a merge step that concatenates per-domain files. The current
flat [fixtures/](../../fixtures/) directory splits the same way.

Why per-domain folders rather than a flat schema: it keeps all
artifacts for one domain co-located, so adding a new domain is "fork
the folder, fill it in." It also makes the progress tracker in §4
trivially correspond to "is this folder complete."

## V1.x — Stabilize foundations before scaling

**Capability jump:** V1 reaches a state where (a) the refinement loop
runs reliably enough that the hourly cron can be trusted to make
real progress, (b) the LLM backend swap from subscription to API
key is fully usable, (c) the eval suite gives a stable baseline
against which V2 per-domain work can measure regressions. V1.x is
hardening, not new features; it makes V2's scale-up safe to begin.

### Status

```
Status: 🟡 in progress
Progress: ███████░░░░░░░░░░░░░ 33% (2/6)
Last completed: ee159d2 — v1.x/source-view-audit CLOSES at 8/8 via PR #27 (long-form-references) at e0c6278. Full chain: PRs #9 vc-blogosphere / #12 tax-and-finance / #14 reddit-tech-collective / #17 founder-engineer-bloggers / #18 matt-levine-school / #22 hn-collective / #26 carta-and-platform-data / #27 long-form-references — every V1 community profile now has mechanic-trigger-failure-mode bullets. Eval baseline stability advanced this run via PR #28 (9ddf1d0) raising the per-fixture timeout default 240s → 360s in both runner.py and config.yaml — addresses the 8/15 timeout rate from PR #24's eval; falsifiable on next measured eval (≥ 10 OK fixtures expected). Concurrent V2 architecture-changes work: PR #29 (ee159d2) extended `src/blindspot/sources/registry.py` with `load_all_sources()` — V2 per-domain preference + V1 monolithic fallback, bit-for-bit preservation verified by 7 unit tests; V2 architecture-changes 2/6 → 3/6.
Next up: Eval baseline stability — with the 360s default in place, run eval (single-subagent foreground) to gather RUN-2 of the 3-consecutive ±0.03 target. Verify the timeout bump rescues genuinely-slow fixtures (success threshold ≥ 10 OK of 15). Then RUN-3 to close the item. After eval-baseline-stability, the AnthropicAPIClient end-to-end item is next, since BLINDSPOT_LLM_BACKEND override (PR #23) already proved the API path works mechanically.
```

### Per-task checklist

- [x] **Refine routine maturity** — `refinements/log.jsonl` shows ≥ 5
  merged refine PRs across ≥ 3 of the 4 detail layers (Sources & knowledge
  / Agents / Config & scoring / Eval). The signal is that refine is
  producing diverse real progress, not stuck in one corner. **Done at b3a8d70 — 7 merged PRs (#1–#7) across all 4 layers.**
- [ ] **Eval baseline stability** — three consecutive `./bin/blindspot eval`
  runs on `main` produce aggregate `quality_score` within ±0.03 of
  each other. The baseline is the median of those three; this becomes
  the V2 entry comparison.
- [ ] **AnthropicAPIClient usable end-to-end** — set `llm_backend:
  anthropic_api` in `config.yaml`, run a full `blindspot ask`, and
  verify behavior matches the subscription backend on the eval
  fixtures (per-situation `quality_score` delta < 0.05).
- [ ] **Streaming editor output** — Editor agent streams tokens as
  they arrive instead of buffering the whole response. Cuts the
  30–60s perceived latency from
  [V1 design §13](./2026-05-13-blindspot-v1-design.md).
- [ ] **Real-usage signal** — ≥ 10 `blindspot ask` turns logged in
  `~/.blindspot/blindspot.db` with at least one `rate hit/meh/obvious`
  per turn. This populates the rating distributions V2's per-domain
  quality tracking will inherit.
- [x] **Source-view audit** — review `source_view_stats`: any
  source-view with `hits >= 10` and `ratings_hit / total < 0.3` either
  gets its `keyword_filter` retuned, its `notes` rewritten, or is
  retired. Record results in `data/source_registry.yaml`'s per-source
  `notes`. **Done at ee159d2 — 8/8 V1 community profiles audited under the mechanic-trigger-failure-mode pattern via PRs #9 (vc-blogosphere), #12 (tax-and-finance), #14 (reddit-tech-collective), #17 (founder-engineer-bloggers), #18 (matt-levine-school), #22 (hn-collective), #26 (carta-and-platform-data), #27 (long-form-references). Each profile's "Known blind spots OF this community" section now anchors a concrete mechanic + trigger threshold + Risk-Officer-checkable failure mode. The original `source_view_stats`-based criterion remained statistically unmeetable (zero source-views hit ≥10 hits because real-usage signal hasn't started yet), so the audit pivoted to a structural quality criterion that is checkable today and the right thing to do regardless of usage volume.**

### Entry gate

(None — V1.0 already shipped; V1.x is the post-ship hardening phase.)

### Exit criteria

All checklist items are `[x]`. Then promote V2.0 from `⬜` to `🟡`
and set its `Next up:` to the first sub-task of `tech-career`
migration.

### Notes for refine

- Most V1.x items are infra / quality, not new product features.
  Refine can scope work into any of the 4 detail layers (Sources,
  Agents, Config, Eval) and find relevant items here without
  pulling forward from V2.
- "Refine routine maturity" is the meta-item — its completion is
  determined by reading the log, not by any single PR. Mark it
  `[x]` when the orchestrator detects ≥ 5 merged PRs spanning ≥ 3
  layers.
- "Source-view audit" is Sources-layer; "AnthropicAPIClient usable"
  touches Agents/Config; "Streaming editor" is Agents. Refine
  tackles them in whatever order data signals + roadmap-driven
  priorities pick this hour.

## 4. V2.0 — Build 10 core domains under the 4-layer model

**Capability jump:** the system answers decisions across 10 domains,
each with explicit decision ontology, framing library, blindspot
catalogue, and source-views. This version's deeper goal is to
**establish the methodology** for building a domain so V3 can
automate parts of it.

### Status

```
Status: ⬜ not started
Progress: ░░░░░░░░░░░░░░░░░░░░ 0% (0/10 domains complete)
Last completed: ee159d2 — V2 architecture-change: PR #29 extended `src/blindspot/sources/registry.py` with `load_all_sources(root)` that prefers per-domain `domain_knowledge/<domain>/sources.yaml` (glob-scan, excludes underscored subdirs) with a clean V1 fallback to the monolithic `data/source_registry.yaml`. `load_registry(path)` signature preserved bit-for-bit; production callers (Orchestrator.create default, sources-list CLI) routed through the new loader. 7 new unit tests in `tests/unit/test_load_all_sources.py` verify V1 fallback returns the same 13 SourceViews, the V2 path with single + multi per-domain files, underscored-dir exclusion, and real-repo bit-for-bit preservation. Architecture-changes checklist now 3/6 (joins replace-hard-coded-scope-refusal at f098f7a and community-profile-loader at 6fd16d3). Earlier: `_schema.md` at 76e3c32, `_meta_ontology.md` at 2026cba.
Next up: V1.x exit criteria must be met before per-domain work begins; meanwhile V2 architecture-changes work continues (next: Eval runner per-domain `fixtures/` scanning in `src/blindspot/eval/runner.py`, or Triage two-pass split in `src/blindspot/agents/triage.py`). Then `tech-career` migration is the first `[ ]` in the Per-domain checklist.
```

### Entry gate

- V1.x exit criteria met (refine stable, eval flat-or-up, streaming
  output landed, API backend usable).
- Author has drafted `_meta_ontology.md` naming the 10 chosen
  domains. **✅ Done — [domain_knowledge/_meta_ontology.md](../../domain_knowledge/_meta_ontology.md) (2026cba)**

### Choosing the 10 domains

Selection criteria, in priority order:

1. **High personal-stakes decisions a typical US-resident
   knowledge-worker faces** (this is V1's user — start there, expand
   later in V3).
2. **Decisions where blind spots are known to be costly** —
   i.e. where "I didn't know I needed to ask" is a common regret.
3. **Domains with reachable source-views** (active English
   communities, RSS-able blogs, or static corpora we can ingest).
   Domains where the real expertise lives in private channels are
   deferred — see §10.
4. **Coverage diversity** — don't pick 10 versions of the same
   underlying domain (e.g. "RSU comp" and "ISO comp" are one
   domain). Spread across life areas.

Author's draft list, to be confirmed in `_meta_ontology.md`:

1. tech-career (V1, migrated)
2. immigration / visa (US-resident perspective)
3. housing (rent vs buy, lease, mortgage, location)
4. health-insurance (US-specific complexity)
5. personal-finance / investing (retirement, tax-advantaged accounts, brokerage)
6. entrepreneurship (founding, side-business, freelancing)
7. education-funding (student debt, grad-school, kids' college)
8. family-planning (marriage, kids, eldercare, divorce)
9. legal-disputes (contracts, employment, small-claims)
10. career-pivots (cross-domain professional moves — note this is
    a "decision type" not a content domain, included because it
    is exactly the kind of thing V4 frame-breaking will lean on)

The 10th is deliberately a meta-domain — its presence sharpens
the 4-layer model because "career pivot" itself crosses several of
the other 9.

### Per-domain checklist

Each of the 10 domains independently requires this checklist.
**A domain is `[x]` only when all sub-items below are `[x]`.**

- [ ] **tech-career** (migration only — convert existing artifacts to new layout)
  - [ ] `domain_knowledge/tech-career/decisions.md` written
  - [ ] `domain_knowledge/tech-career/framings.md` written
  - [ ] `domain_knowledge/tech-career/blindspots.md` written
  - [ ] `data/source_registry.yaml` migrated to `domain_knowledge/tech-career/sources.yaml`
  - [ ] community profiles moved to `domain_knowledge/tech-career/communities/`
  - [ ] fixtures moved to `domain_knowledge/tech-career/fixtures/`
  - [ ] `domain_pack.md` extracted from current triage prompt
  - [ ] eval still passes on migrated layout
- [ ] **immigration**
  - [ ] decisions.md (≥ 8 distinct decisions, e.g. visa-renewal vs status-change, employer-sponsored vs self-petitioned, marry-for-status timing, etc.)
  - [ ] framings.md (≥ 3 framings per major decision)
  - [ ] blindspots.md (≥ 5 typical blind spots per framing)
  - [ ] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags)
  - [ ] communities/* (one profile per community_tag in sources.yaml)
  - [ ] fixtures/* (≥ 8 fixture situations)
  - [ ] domain_pack.md
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **housing** (same template as immigration)
- [ ] **health-insurance** (same template)
- [ ] **personal-finance / investing** (same template)
- [ ] **entrepreneurship** (same template)
- [ ] **education-funding** (same template)
- [ ] **family-planning** (same template — special care: high blind-spot stakes, often religious/cultural framings)
- [ ] **legal-disputes** (same template — high-stakes, must be labelled "decision-support, not legal advice" in domain_pack.md Editor section)
- [ ] **career-pivots** (same template — note this domain's source-views deliberately cross into the other 9 domains)

### Architecture changes

- [ ] **Triage Officer becomes two-pass.**
  - Pass 1: classify situation into ≥ 1 of the 10 domains (multi-label allowed)
  - Pass 2: with the relevant `domain_pack.md` files concatenated into the system prompt, extract full Triage facets
  - File: [src/blindspot/agents/triage.py](../../src/blindspot/agents/triage.py)
- [x] **Replace hard-coded scope refusal** at [src/blindspot/prompts/triage.md:46](../../src/blindspot/prompts/triage.md):
      "If the situation is clearly outside US tech career & equity scope, return all-empty arrays."
      Becomes: "If the situation does not match any domain in
      `_meta_ontology.md`, return all-empty arrays." **Done at f098f7a (PR #13) — added a `# Scope (in-scope domains)` section to triage.md that lists all 10 `_meta_ontology.md` domains (inlined for self-containment), and rewrote the refusal bullet from the V1 tech-career-only language to "If the situation does not match any of the 10 in-scope domains named in the Scope section above, return all-empty arrays." Tech-career is item 1 on the list so V1 fixtures behave identically; only genuinely out-of-ontology requests (medical diagnosis, voting, etc.) refuse.**
- [x] **Registry loader** ([src/blindspot/sources/registry.py](../../src/blindspot/sources/registry.py)):
      load and merge per-domain `sources.yaml` files into the same
      runtime structure as today's monolithic registry. **Done at ee159d2 (PR #29) — added `load_all_sources(root: Path = Path("."))` which glob-scans `domain_knowledge/<domain>/sources.yaml` (skipping any underscored subdirs like `_meta/`), falls back to the monolithic `data/source_registry.yaml` when no per-domain files exist, and returns a single merged `list[SourceView]` in the same runtime structure as `load_registry`. `load_registry(path)` signature preserved bit-for-bit so existing tests continue to pass unchanged. Production callers in `src/blindspot/orchestrator.py` and `src/blindspot/cli.py` routed through the new loader. 7 new unit tests in `tests/unit/test_load_all_sources.py` cover the V1 fallback path (returns same 13 SourceViews as today), the V2 path (single + multi per-domain file), the underscored-dir exclusion, and the bit-for-bit V1 preservation on the real repo state.**
- [x] **Community-profile loader** in
      [src/blindspot/agents/base.py](../../src/blindspot/agents/base.py):
      look up profiles under `domain_knowledge/<domain>/communities/`
      with fallback to the legacy top-level path during migration. **Done at 6fd16d3 (PR #21) — added `DOMAIN_KNOWLEDGE_DIR` module constant; `load_community_profile(community_tag)` glob-scans `domain_knowledge/*/communities/<tag>.md` first (deterministic alphabetically-first resolution on multi-match with stderr warning), falls back to `community_profiles/<tag>.md`, raises a clearer FileNotFoundError naming both attempted paths when neither exists. V1 behavior preserved bit-for-bit on the current 8 V1 communities, verified by the orchestrator integration test plus 4 new unit tests in `tests/unit/test_load_community_profile.py`.**
- [ ] **Eval runner** ([src/blindspot/eval/runner.py](../../src/blindspot/eval/runner.py)):
      scan all per-domain `fixtures/` subfolders. Aggregate
      `quality_score` is per-domain plus a global mean. Refine routine
      should never average across domains in a way that lets one
      thriving domain mask another's regression.
- [ ] **Refine routine** ([.claude/skills/refine-blindspot/SKILL.md](../../.claude/skills/refine-blindspot/SKILL.md)):
      teach it to scope changes to one domain at a time, and to read
      per-domain `quality_score` rather than the global mean.

### Methodology output (the real V2 deliverable)

V2's hidden product is not "10 domains" — it is the **playbook for
building domain N+1** that V3 will partially automate. By the time
the 10th domain is done, this file must exist:

- [ ] `domain_knowledge/_playbook.md` — a step-by-step writeup of
      how each of the 10 domains was actually built. What worked
      first try; where the LLM was reliable; where it produced
      shallow output; where human judgement was non-negotiable;
      typical time-spent breakdown. This is the input to V3.

### Open questions answered by V2

- **Q1 (from earlier draft):** Are agents domain-pluggable, or
  domain-specificity lives in prompts only? V2 answers: prompts
  only (via domain packs). If this breaks under 10 domains, V3
  revisits.
- **Q3:** `community_tag` stays flat (one tag per source-view).
  V2 confirms this is sufficient under domain-scoping (because the
  *folder* now provides the hierarchy).

### Exit risk

If by domain 4 the per-domain `quality_score` is consistently
worse than the V1 tech-career baseline (i.e. domain-pack prompts
can't reach V1's quality), the "specialization lives in prompts,
not code abstractions" thesis breaks. Pause; reconsider whether
some agents (Risk Officer especially) need domain-specific
sub-classes. Q1 reopens.

## 5. V3.0 — Scaled curation to all indexable domains

**Capability jump:** the system grows from 10 domains to all
domains for which usable source-views exist on the public web,
without the author manually writing each domain's 4 layers.

### Status

```
Status: ⬜ not started
Progress: ░░░░░░░░░░░░░░░░░░░░ 0%
Last completed: (none)
Next up: V2 must reach 100% first
```

### Entry gate

- V2.0 at 100% (all 10 domains complete).
- `domain_knowledge/_playbook.md` exists and is judged by the
  author to capture the methodology accurately.
- ≥ 100 real user turns logged across the V2 domains, producing
  enough `ungrounded_claims` data to seed coverage-gap detection.

### The core problem: collecting knowledge ≠ collecting sources

V1's intuition "source-views are the moat" stays correct, but V3
needs to be honest about a deeper bottleneck. The 4-layer model
in §3 makes this explicit:

- **Layers 1–2 (decisions, framings) are LLM-strong**: well-known,
  documented, mainstream. LLM-assisted scaffolding works.
- **Layer 3 (blindspots) is LLM-weak**: blind spots are precisely
  what's underrepresented in the training distribution. Cannot
  be generated reliably — must emerge from real source-view
  evidence and user feedback.
- **Layer 4 (source-views) has two failure modes for LLMs**:
  (a) LLM lists popular sources (HomeDepot.com / r/HomeImprovement)
  but misses the small high-signal ones (specialist trade
  forums, regional union sub-boards, paywalled newsletters) where
  Blindspot's real value lives;
  (b) Many real domain experts share knowledge in private channels
  (DMs, paid newsletters, oral transmission) that no crawler will
  reach — this is a hard ceiling, not an engineering problem.

V3 must build mechanisms that work *with* these constraints, not
mechanisms that pretend the constraints don't exist.

### Mechanism A — Domain discovery (Layer 0 work)

A new subsystem `src/blindspot/discovery/`, runs separately from
the ask pipeline.

- [ ] **Coverage-gap detector.** Cluster `ungrounded_claims` rows
      by embedding similarity. Each large cluster surfaces a
      missing domain or sub-domain. Output: a queue of
      `candidate_domains.yaml` entries with sample situations and
      suggested boundaries.
- [ ] **Domain boundary refinement.** For each candidate, an LLM
      pass proposes: domain name, scope statement, parent domain
      (or "new top-level"), and a small set of representative
      decisions. Human ratifies before promotion — domain creation
      is too consequential to fully automate (it shapes the meta
      ontology forever).

### Mechanism B — Layers 1–2 generation (decisions + framings)

For a ratified new domain:

- [ ] **LLM breadth-scan**: prompted with the domain scope and
      sample situations from the coverage-gap detector, produce a
      draft `decisions.md` and `framings.md`. Use a prompt template
      derived from the V2 `_playbook.md`.
- [ ] **Self-critique pass**: a second LLM call (different prompt,
      ideally different model in the Haiku/Opus mix) reviews the
      draft for: missing major decisions, redundant or overlapping
      framings, framings that are actually blind spots in disguise.
- [ ] **Human ratify**: drafts land in `domain_knowledge/<domain>/`
      with a frontmatter `maturity: experimental`. They are usable
      at runtime but the Editor surfaces a caveat in any answer
      sourced from `experimental` knowledge. Promotion to
      `maturity: stable` requires either explicit human approval
      or N positive user ratings over M turns.

### Mechanism C — Layer 4 source-view discovery

This is where the LLM is least reliable. Discovery happens through
**multiple weak signals combined**, not LLM listing alone:

- [ ] **Decision-driven discovery (not community-driven).**
      Invert V1's mental model: instead of asking "what communities
      exist for this domain", ask "given decision D in this domain,
      who has actually made D and lived with the outcome — where do
      those people talk?" This produces better source-views because
      it grounds discovery in the decision, which is what the user
      actually faces.
- [ ] **Meta-community mining.** Scrape "best forum for X" /
      "where do I learn Y" threads from existing covered
      communities (HN, Reddit, Stack Overflow) and from search
      engines. People recommend sources to each other constantly;
      use that recommendation graph instead of asking an LLM cold.
- [ ] **Cite-and-promote.** Source candidates start at
      `reliability: 1`. They enter the pipeline only when the
      situation matches strongly AND no `reliability >= 3` source
      covers that situation. Their reliability climbs only if (a)
      their cited documents survive the Critic agent's grounding
      check, and (b) blind-spots citing them get user `hit` ratings.
      Bad sources self-eject because they never accumulate.
- [ ] **Snapshot reliability over time.** A source can decay
      (subreddit goes private, blog stops updating, paywall
      installed). Track `last_successful_fetch` and
      `last_useful_citation`. Auto-demote stale sources.

### Mechanism D — Layer 3 blindspot catalogue growth

Blindspots can't be generated; they must accumulate from real use.

- [ ] **Blindspot mining from approved turns.** After a turn where
      a blind spot got a `hit` rating, the Editor's exact phrasing
      of that blind spot, plus the framing it was situated in,
      gets considered for promotion into the domain's
      `blindspots.md`. Promotion is gated by: ≥ 3 independent hits
      across different situations + a dedup check against existing
      catalogue entries.
- [ ] **Negative learning.** Blindspots that consistently get
      `obvious` ratings get pulled. The catalogue is a living
      file — V3 is when refine routine starts editing
      `blindspots.md`, not just system prompts.

### Mechanism E — High-stakes domain gating

A subset of domains must never run under `maturity: experimental`
without human review of every promotion: medical diagnosis,
specific legal advice, immigration filings, investment advice with
dollar-amount specificity, child welfare, anything where wrong
output causes provable harm.

- [ ] **`high_stakes: true` flag** in `_meta_ontology.md` per
      domain. For these:
  - Mechanism C source promotions require human approval.
  - The Editor's domain_pack appends a "decision-support, not
    professional advice" framing to every answer.
  - The Critic agent gets stricter grounding thresholds.

### Ceiling — what V3 cannot reach

The roadmap is honest that V3 does not deliver "all knowledge."
It delivers "all indexable knowledge." The gap:

- Tacit knowledge held in private channels (DMs, paid groups,
  oral transmission from senior tradespeople, in-person mentorship).
- Knowledge fenced behind login walls the system cannot ethically
  scrape.
- Knowledge that exists only in non-English communities the system
  hasn't expanded into yet (bilingual is its own work, see §9).

V5 is the version where this ceiling could potentially be lifted
through expert partnerships (paid curators, "expert as a service").
V3's job is to honestly mark where its coverage stops.

### Per-task checklist

- [ ] discovery/ subsystem scaffolded with the 5 mechanisms above
- [ ] First 10 V3-grown domains (beyond the V2 manual 10)
- [ ] Per-domain checklist same as V2's, but most fields populated
      by Mechanism B/C drafts that human ratifies
- [ ] `_playbook.md` updated with which V2 steps automated cleanly
      and which kept needing human intervention
- [ ] Eval suite includes per-maturity-level breakdown:
      `experimental` domains' quality_score is tracked separately
      from `stable` ones; users are shown maturity in answers

### Open questions answered by V3

- **Q4:** Global decision ontology — V3 makes it concrete by
  populating `_meta_ontology.md` to ~50+ entries. Hierarchy emerges
  empirically.

### Exit risk

If after 10 V3-grown domains the `experimental → stable`
promotion rate is below ~30%, the LLM-assisted scaffolding is
producing material that doesn't meet quality. Pause; consider
the "expert as a service" model (paid human curators per domain
type) earlier than V5.

## 6. V4.0 — Frame-breaking

**Capability jump:** when the user poses a narrow question, the
system surfaces blind spots from framings the user did not pose,
grounded in real source-views across other domains.

### Status

```
Status: ⬜ not started
Progress: ░░░░░░░░░░░░░░░░░░░░ 0%
Last completed: (none)
Next up: V3 must produce sufficient domain coverage first
```

### Entry gate

- V3 has populated ≥ 30 domains at `maturity: stable`.
- The 4-layer knowledge model contains enough breadth that, for
  most situations, there exist alternative-framing domains with
  real sources. (Without this, V4 can only point at gaps, not
  fill them.)

### Core problem restated

When a user asks "how do I earn more as an SDE?", their **surface
intent** is "increase SDE comp" but their **deep intent** is more
like "earn more in the US, given my skills and risk tolerance."
V1–V3 work only at the surface intent. V4 lifts to the deep intent
and surveys alternative surface intents that serve the same deep
goal — high-skill trades, founding, investing income, geographic
relocation, domain switch.

Frame-breaking can only land alternative-framing blind spots that
are *cited from real sources in those framings' domains*. That is
why V3 must come first: without breadth, frame-breaking is
hallucination.

### Architecture decision (delayed, but constrained)

Three designs are on the table (carried over from earlier draft):

- **Design A — Goal-tree Officer (new agent before Triage)**:
  explicit deep-intent → alternative surface-intent enumeration.
- **Design B — Lateral Officer (new agent after Risk Officer)**:
  within-frame pipeline runs unchanged; Lateral Officer reaches
  laterally with explicit cross-domain fetches.
- **Design C — Deep-intent injection in Triage**: Triage outputs
  both `surface_domains` and `deep_domains`; source matching uses
  the union.

V4 entry includes a spike across all 3 on the same fixture set;
production choice may be hybrid (default C; escalate to A on
high-ambiguity Triage). Do not pre-commit until the spike.

### Per-task checklist

- [ ] Design spike: implement A, B, C as branches on the same
      fixture set; measure frame_breaking_score on each
- [ ] Choose architecture, write design note as
      `docs/specs/<date>-frame-breaking-design.md`
- [ ] Implement chosen design
- [ ] New fixture class: "narrow-framing situations" — questions
      posed as if there's only one path, gold standard answer
      surfaces ≥ 2 alternative framings
- [ ] Judge prompt gets `frame_breaking_score` dimension (0–5)
- [ ] `quality_score` rebalanced with `+ 0.20 × frame_breaking_score_mean`
- [ ] Hard safeguard: every frame-breaking blind spot must
      `[doc-X]` cite a source in the alternative domain's
      stable-maturity sources. No citation, no pivot. Falls back
      to "the system might also consider <domain>, but does not
      yet have confident knowledge there."
- [ ] Frame-breaking ablation test: turn the feature off and
      verify within-frame quality_score does not regress (i.e.
      V4 did not damage V3's strength)

### Open questions answered by V4

- **Q2:** Frame-breaking architecture — decided by spike.
- **Q5 (partial):** Memory — V4 starts touching user-level deep
  intent. V5 will productize this further.

### Exit risk

If frame-breaking blind spots fail user ratings (mostly `meh`
or `obvious`), the deep-intent inference is producing irrelevant
pivots. Mitigate by raising the citation threshold for cross-
frame answers (require ≥ 2 supporting sources from the alternative
domain, not 1), or by gating frame-breaking on explicit user
opt-in ("Want me to also consider other paths to this goal?").

## 7. V5.0 — Universal access

**Capability jump:** the system becomes usable by people who are
not the author.

### Status

```
Status: ⬜ not started
Progress: ░░░░░░░░░░░░░░░░░░░░ 0%
Last completed: (none)
Next up: requires V4 stable
```

### Per-task checklist

- [ ] Multi-user data model — actually use the `user_id` column
      already plumbed at
      [V1-design §8:220](./2026-05-13-blindspot-v1-design.md)
- [ ] Postgres migration (SQLite → Postgres)
- [ ] Web UI (mobile-responsive, inline citation clicks)
- [ ] AuthN/AuthZ (OAuth + per-user data isolation)
- [ ] Personalization memory (per-user retained context: visa
      status, financial profile, family situation, etc., to
      avoid re-explaining)
- [ ] Production observability — per-agent latency, cost per
      turn, refine-routine activity
- [ ] Business-model decision and pricing
- [ ] (Optional) Expert-curator partnerships for the V3 ceiling
      gap — paid curators for high-stakes domains, private-knowledge
      domains

## 8. Cross-cutting concerns (always-on)

These run alongside every version, not as separate versions.

- **Refine routine.** The
  [skill at .claude/skills/refine-blindspot/SKILL.md](../../.claude/skills/refine-blindspot/SKILL.md)
  is the system's own learning loop. Every version's prompt /
  eval / scoring work must preserve refine compatibility. If a
  prompt change breaks refine's ability to score prior changes,
  that's a bug, not a feature.
- **Grounding discipline.** The `[doc-X]` citation requirement
  from [V1-design §7:176](./2026-05-13-blindspot-v1-design.md)
  applies to every version, every layer. Frame-breaking output
  (V4+) must cite. Auto-discovered sources (V3+) must produce
  citable documents. Never relax this — it is what separates
  this system from a confident-sounding LLM.
- **Per-domain quality tracking.** From V2 on, never collapse
  quality_score across domains in a way that lets a strong domain
  mask a weak one's regression. Aggregate views are fine; the
  refine routine reads per-domain.

## 9. Bilingual (cross-cutting flag, not a version)

Listed as "explicitly deferred" at
[V1-design §2:26](./2026-05-13-blindspot-v1-design.md). Lands as
a flag during V2 or V3 — not its own version. Triage detects
language; Editor outputs in same language; community profiles get
a `language:` field; source-views get a `language:` field; the
diversity constraint at
[V1-design §5:109](./2026-05-13-blindspot-v1-design.md) extends to
"max 2 per `community_tag` AND not all from the same language".

Trigger: when adding a domain whose best sources are in non-English
communities (Chinese diaspora forums for immigration; some
specialist trade communities; etc.). The first domain that hits
this trigger pulls the work in.

## 10. Honest limits

Things the roadmap explicitly does not claim to solve:

- **Knowledge in private channels.** DMs, paid groups, oral
  transmission. The system's ceiling is "indexable knowledge."
  V5's expert-curator path is the partial mitigation but not a
  full solution.
- **Domains where the right answer is "consult a professional."**
  Medical diagnosis, specific legal cases. The system should
  surface what the user is missing about *the decision to consult
  whom and when*, not replace the professional. High-stakes gating
  in §5 enforces this.
- **Adversarial users.** Users who try to use Blindspot for
  decisions where their goal is harmful to others. Out of scope
  for the roadmap; needs separate policy work.

## 11. Risks specific to the long-range plan

- **The V2 methodology may not generalize.** V3 leans heavily on
  the V2 `_playbook.md`. If domains 11–20 require fundamentally
  different approaches per domain, V3's automation premise breaks.
  Mitigation: pick V2's 10 domains diverse enough to surface
  generality vs specificity. The 10th (career-pivots, deliberately
  meta) is the stress test.
- **The curation moat erodes.** If a future Claude becomes good
  enough at "knowing which community knows what" without curated
  source-views, the entire source-view layer becomes redundant.
  Mitigation: run a "no-sources baseline" through eval once per
  quarter from V1.x on. If its quality_score climbs above the
  curated baseline, pivot the moat from "which sources" to "which
  framings" — i.e. lean harder into Layers 1–3 of §3, which encode
  judgement the LLM lacks regardless of source access.
- **Single-author bottleneck through V3.** V2 is one human curating
  10 domains. Burnout is real. Mitigation: V3 isn't optional. It
  is the path off the bottleneck. Sequence is critical: V2 must
  finish even if slowly, because V3's automation needs V2's
  playbook as input.
- **High-stakes failure visibility.** The first publicly-confident
  wrong answer in medical / legal / immigration is a reputation
  event. V3's high-stakes gating is necessary; V5's product
  launch needs an explicit "decision-support, not decision-making"
  framing in product copy from day one.

## 12. Open design questions tracked across versions

- ~~**Q1.**~~ Agents domain-pluggable vs prompts-only?
  *Answered in V2: prompts-only. Revisit if V2 exit risk fires.*
- **Q2.** Frame-breaking architecture: A vs B vs C from §6.
  *Open. V4 entry decision; requires spike.*
- ~~**Q3.**~~ `community_tag` flat vs hierarchical?
  *Answered in V2: flat, because folder structure supplies hierarchy.*
- **Q4.** Global decision ontology shape — how does
  `_meta_ontology.md` grow without becoming a mess?
  *Open. V3 will pressure this.*
- **Q5.** User memory: each session independent vs compounded?
  *Open. V4 starts touching it; V5 productizes.*

## 13. When this document is wrong

Update it. Specifically:

- Every time a sub-task checkbox flips `[ ]` → `[x]`, recompute
  the progress bar and update "Last completed" / "Next up". This
  is what makes the document useful to the next Claude session.
- Any time a version's exit risk fires, write what fired and what
  was done.
- Any time an "open question" gets answered, move the answer into
  the relevant version section and strike through the Q in §12.
- The version *ordering* is the load-bearing part. Sub-task
  ordering inside a version is reorderable; capability sequencing
  across versions is not.
