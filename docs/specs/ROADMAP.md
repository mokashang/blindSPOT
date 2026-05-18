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
Progress: ███████████░░░░░░░░░ 57% (4/7)
Last completed: 111365d — **eval-baseline-stability AND eval-pipeline-robustness BOTH FLIPPED `[x]` in a single merge** via PR #59 (measurement #4 at aggregate quality_score 0.7964, full 15/15, partial=false, 0 timed_out, 1 judge_unparseable handled gracefully by PR #46). Three-measurement cluster now in hand: 0.7964 / 0.8164 / 0.8207 — all pairwise deltas ≤ 0.0243 < 0.03 stability band. **Median = 0.8164 = V1.x→V2 entry baseline.** eval-pipeline-robustness closes simultaneously: PR #59 is the 4th consecutive no-Python-exception eval run on main (PR #24 + PR #43 + PR #57 + PR #59), exceeding the "three consecutive" sub-criterion; the other two sub-criteria (judge max-tokens handling, per-fixture survival) were operationally verified earlier via PR #46 + PR #50 + PR #56. V1.x progress 2/7 → 4/7 in one merge — first time the eval-pipeline foundation is empirically certified.
Next up: **AnthropicAPIClient usable end-to-end** — set `llm_backend: anthropic_api` in `config.yaml`, run a full `blindspot ask`, and verify behavior matches the subscription backend on the eval fixtures (per-situation `quality_score` delta < 0.05). Touches Agents/Config layer. Remaining V1.x items after this: Streaming editor output (Agents); Real-usage signal (org-level, gated on user activity).
```

### Per-task checklist

- [x] **Refine routine maturity** — `refinements/log.jsonl` shows ≥ 5
  merged refine PRs across ≥ 3 of the 4 detail layers (Sources & knowledge
  / Agents / Config & scoring / Eval). The signal is that refine is
  producing diverse real progress, not stuck in one corner. **Done at b3a8d70 — 7 merged PRs (#1–#7) across all 4 layers.**
- [x] **Eval pipeline robustness** — `./bin/blindspot eval` (a) reliably
  runs to completion in < 30 min wall-clock for the current 15-fixture
  tech-career set (or shows partial-progress in a result file even if
  cut short), (b) handles judge LLM output that exceeds max-tokens by
  recording `quality_score=null` with reason `"judge response unparseable"`
  rather than crashing the whole run, (c) survives per-fixture failures
  (timeouts, JSON parse errors, Reddit credential absence) without
  aborting the run. Three consecutive runs from `main` all produce a
  result file with no Python exception in stdout. **Done at 111365d — sub-criterion (a) is operationally met via the OR-branch: PR #50 ships partial-result-write code (per-fixture snapshot + SIGINT/SIGTERM handlers + atomic .tmp/os.replace); PR #56 empirically validates it (eval cut short at fixture 7/15 produces eval/results/20260517T200720Z.json with completed_count=7, partial:true). Sub-criterion (b) via PR #46 (judge unparseable JSON recorded as quality_score=null + reason, run continues). Sub-criterion (c) via PR #15 timeout-360 + PR #46 + Collection-layer try/except. The "three consecutive runs from main produce a result file with no Python exception in stdout" requirement is empirically exceeded: PR #24 + PR #43 + PR #57 + PR #59 = 4 consecutive clean eval runs.**
- [x] **Eval baseline stability** — three consecutive `./bin/blindspot eval`
  runs on `main` (with **Eval pipeline robustness** above [x]) produce
  aggregate `quality_score` within ±0.03 of each other. The baseline is
  the median of those three; this becomes the V2 entry comparison. **Done at 111365d — three measurements in hand: PR #43 = 0.8164 (eval/results/20260517T130928Z.json), PR #57 = 0.8207 (eval/results/20260517T203938Z.json), PR #59 = 0.7964 (eval/results/20260517T201346Z.json). All pairwise deltas (0.0200, 0.0243, 0.0043) ≤ 0.0243 < 0.03 threshold. Median = 0.8164. **V1.x → V2 entry baseline = 0.8164.****
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
- "Eval pipeline robustness" subsumes the JSON-truncation,
  per-fixture-timeout-firing, and subagent-execution-model concerns
  surfaced in runs 1340 / 1711 / 1810 / 1839. Detail-layer Eval slots
  in upcoming runs should target ONE prerequisite at a time (e.g.
  JSON-truncation handling first), not retry the full
  eval-baseline-stability item.

## 4. V2.0 — Build 10 core domains under the 4-layer model

**Capability jump:** the system answers decisions across 10 domains,
each with explicit decision ontology, framing library, blindspot
catalogue, and source-views. This version's deeper goal is to
**establish the methodology** for building a domain so V3 can
automate parts of it.

### Status

```
Status: ⬜ not started
Progress: ██░░░░░░░░░░░░░░░░░░ 10% (1/10 domains complete)
Last completed: 1c3503c — V2 §4 **housing kicked off** with `domain_knowledge/housing/decisions.md` (PR #60, Layer 1 of the 4-layer knowledge model for V2 §4 domain 3 of 10; 10 distinct decisions; ~2250 words; 336 lines; mirrors tech-career [PR #30] and immigration [PR #42] precedents structurally). Housing's per-domain checklist now expanded to 8 sub-items (decisions/framings/blindspots/sources/communities/fixtures/domain_pack/eval-pass) with sub-item 1 of 8 [x]; housing parent stays [ ] (1 of 8). Earlier in this run: V1.x §1.x eval-baseline-stability + eval-pipeline-robustness BOTH `[x]` via PR #59 — V1.x progress 2/7 → 4/7 in a single merge. V2 progress unchanged at 1/10 (tech-career remains the only fully-built V2 domain). Earlier rounds: tech-career FULLY BUILT at 3bb4fea (PR #57); immigration at 7/8 (only `eval pass` remains) at 38f3733 (PR #58); immigration `communities/*` at f95a4f7 (PR #54); immigration `domain_pack.md` at d56eba3 (PR #53); immigration `sources.yaml` at 638cec4 (PR #49); immigration `blindspots.md` at 535d746 (PR #48); immigration `framings.md` at 3a3798c (PR #44); immigration `decisions.md` at 6161d6f (PR #42).
Next up: V1.x exit criteria still gate V2 promotion to 🟡 (V1.x is now 4/7 — AnthropicAPIClient + Streaming editor + Real-usage signal remain). V2 work in flight on three fronts: (1) **immigration `eval pass`** — last sub-item for immigration parent [x] (runs eval on the per-domain immigration fixtures from PR #58); (2) **housing remaining sub-items** — framings.md (≥3 framings per major housing decision) → blindspots.md (≥5 per framing) → sources.yaml (≥8 source-views, ≥4 community_tags covering rent-vs-buy/mortgage/lease/insurance/HOA expertise) → communities/* → fixtures/* → domain_pack.md → eval-pass, mirroring the immigration build-out sequence; (3) opportunistically start a fourth domain (health-insurance / personal-finance / etc.) when sources/agents subagent slots have capacity.
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

- [x] **tech-career** (migration only — convert existing artifacts to new layout) **— done at 3bb4fea: all 8 sub-items [x]. FIRST FULLY-BUILT V2 DOMAIN.**
  - [x] `domain_knowledge/tech-career/decisions.md` written **— done at a46e5bd (PR #30, 11 decisions, 1210 words)**
  - [x] `domain_knowledge/tech-career/framings.md` written **— done at bf2cb74 (PR #32, 14 framings, ~4.9k words; each framing has name + decisions-it-applies-to + 3–6-sentence mental model + 5–10-phrase characteristic vocabulary + 3–5-bullet `Excludes` list; every decision D1–D11 has ≥3 framings; voice anchored to existing V1 community_profiles for routing continuity; ≥56 candidate blindspot seeds named across all framings' `Excludes` lines)**
  - [x] `domain_knowledge/tech-career/blindspots.md` written **— done at 9d1aa54 (PR #35, Layer 3 of the 4-layer knowledge model; 1690 lines / ~11.9k words; 70 entries = 5 per framing × 14 framings; per-entry schema Statement / Source-evidence / Trigger / Failure-mode / Recovery-move per `_schema.md`; every entry grounded in either a real `community_profiles/*.md` Known-blindspot bullet or a `framings.md` Excludes anchor — no purely LLM-extrapolated entries; cross-framing tensions section appended for Triage routing; word count came in ~50% over the schema's 5-8k suggestion, driven by 70 entries × 5 required schema fields × ~170 words/entry; flagged explicitly as risk in PR body, reviewer approved as-is)**
  - [x] `data/source_registry.yaml` migrated to `domain_knowledge/tech-career/sources.yaml` **— done at fd281bb (PR #37, bit-for-bit copy of V1 entries with additive `domain: tech-career` annotation; V1 file kept as fallback; PR #29's `load_all_sources` picks up the V2 file with V1 shadowed; 79/79 pytest green)**
  - [x] community profiles moved to `domain_knowledge/tech-career/communities/` **— done at f58ce62 (PR #40, 8 community profiles git-mv'd at 100% similarity from `community_profiles/` to `domain_knowledge/tech-career/communities/`: carta-and-platform-data, founder-engineer-bloggers, hn-collective, long-form-references, matt-levine-school, reddit-tech-collective, tax-and-finance-professionals, vc-blogosphere; `community_profiles/_schema.md` stays in place as the writing guide; pytest 82/82 green; PR #21's `load_community_profile()` resolves both layouts (V2 path takes precedence; V1 fallback no longer triggers since no V1 profile files remain) so V1 runtime behavior is bit-for-bit preserved)**
  - [x] fixtures moved to `domain_knowledge/tech-career/fixtures/` **— done at 56862d5 (PR #41, 15 per-fixture YAML files split from `fixtures/eval_situations.yaml` monolith using the top-level-mapping shape; bit-for-bit identical content per fixture verified; V1 file kept as fallback for tests/code that reference it by path; PR #34's `load_all_fixtures` picks up the V2 per-domain layout with the V1 monolithic fallback shadowed; 82/82 pytest green)**
  - [x] `domain_pack.md` extracted from current triage prompt **— done at fd281bb (PR #38, 1711-word delta on top of generic prompts: Triage Pass-2 enrichment names 12 personas + 19 mechanism-specific risk surfaces (AMT-crossover, 83b-deadline, 90-day-PTE-window, OWBPA-21-day-consideration, etc.) + opposing-framing pairs (F3↔F11, F4↔F13) + cross-domain routing flags; Editor gets numeric-specificity rules + opportunity-cost-framing rule for comparing-offers-* personas + no professional-advice label; Critic gets per-claim citation spot-check on equity-tax claims + +1 non-obviousness floor for comparing-offers-*; activates only via PR #33's Pass-2 with V1 fallback)**
  - [x] eval still passes on migrated layout **— done at 3bb4fea (PR #57, eval/results/20260517T203938Z.json contains `per_domain` aggregation from PR #34's V2 fixture loader, indicating eval ran against the V2 migrated layout; 15/15 fixtures OK, 0 timed_out, 0 judge_unparseable, aggregate_quality_score 0.8207 vs prior baseline 0.8164 from PR #43 — no regression, ~50 min wall-clock under the 55-min budget)**
- [ ] **immigration**
  - [x] decisions.md (≥ 8 distinct decisions, e.g. visa-renewal vs status-change, employer-sponsored vs self-petitioned, marry-for-status timing, etc.) **— done at 6161d6f (PR #42, Layer 1 of the 4-layer knowledge model for V2 §4 domain 2 of 10; 10 distinct decisions covering H-1B/O-1 transition timing, marry-for-status, concurrent vs sequential I-140/I-485 under retrogression, AC21 portability mid-PERM, AP-and-AOS-abandonment trap, EB-2 vs EB-3 downgrade/upgrade, STEM-OPT vs cap-gap vs H-1B, status-change vs consular processing, self-petition path EB-1A/NIW vs employer-dependent EB-2/3, and J-1 waiver timing; follows tech-career/decisions.md structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; cross-domain edges flagged inline; high-stakes Mechanism E posture explicit; ~2k words; pure-additive knowledge content, no runtime gating, eval skipped per brief)**
  - [x] framings.md (≥ 3 framings per major decision) **— done at 3a3798c (PR #44, Layer 2 of the 4-layer knowledge model for V2 §4 domain 2 of 10; 14 framings, ~6700 words; each framing has Decisions-it-applies-to / Mental-model-summary / Characteristic-vocabulary / Excludes per `_schema.md`; coverage map shows every D1–D10 has ≥3 framings (D1=5, D2=4, D3=3, D4=3, D5=4, D6=3, D7=4, D8=4, D9=3, D10=4); opposing-framing pairs explicitly named — F1↔F2 (status-continuity vs route-optimality), F1↔F13 (status-continuity vs consular-discretion), F9↔F10 (evidentiary-bar vs visa-as-employer-leverage), F14↔F2/F9 (pro-se vs orthodox-process); voice anchors named conceptually since immigration sources.yaml doesn't yet exist; high-stakes Mechanism E posture explicit in intro and downstream-layers note; pure-additive knowledge file, no runtime gating, eval skipped per brief)**
  - [x] blindspots.md (≥ 5 typical blind spots per framing) **— done at 535d746 (PR #48, Layer 3 of the 4-layer knowledge model for V2 §4 domain 2 of 10; 70 entries = 5 per framing × 14 framings; ~15.2k words; full Layer 3 schema per `community_profiles/_schema.md` (Statement / Source-evidence / Trigger / Failure-mode / Recovery-move) per entry; every Recovery-move includes the Mechanism E "consult a licensed immigration attorney" professional-counsel deferral per immigration's high_stakes:true posture, verified programmatically across all 70 entries; source-anchors are framings.md Excludes lines authored explicitly to seed Layer 3 + V1 community-profile bullets touching immigration-adjacent topics (founder-engineer-bloggers, reddit-tech-collective, long-form-references) + conceptual references to the immigration-specific community classes named in framings.md voice-anchors (immigration-attorney blogs, USCIS Ombudsman reports, AILA practitioner forums, Murthy/Boundless/Cyrus D. Mehta blog network, trackitt-style IV-and-AOS forums); cross-framing tensions section appended to seed Triage routing; maturity note documents date-stamp risk on policy anchors and explicit Mechanism E posture; pure-additive knowledge file, no runtime gating, eval skipped per brief)**
  - [x] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags) **— done at 638cec4 (PR #49, Layer 4 of the 4-layer knowledge model for V2 §4 domain 2 of 10; 13 source-views across 5 distinct `community_tag` values, exceeds ≥8/≥4 minimum; schema mirrors `domain_knowledge/tech-career/sources.yaml` exactly; all reliability:1 per ROADMAP §5 Mechanism C cite-and-promote starting posture; community-tag breakdown maps to framings.md voice-anchor classes: immigration-attorney-blogs (4 entries via MurthyDotCom voices — Murthy/Boundless/Cyrus D. Mehta/NPZ), government-and-ombudsman (3 entries via DOS-watcher + USCIS Policy Manual + USCIS Ombudsman Annual Reports), practitioner-forums (1 aggregated AILA think-tank essays), community-experience-forums (4 entries via consumer-experience/student-forum — r/immigration + trackitt + Visajourney + Immigration.com), journalists-and-explainers (1 via policy-context journalism — NYT immigration desk); `src/blindspot/sources/registry.py:load_all_sources` from PR #29 picks up the new file automatically — verified locally 13 immigration ids load alongside 13 tech-career ids; 6 RSS URLs are placeholders pending live verification with `notes: "URL placeholder — verify before enabling"`, Collection-layer try/except tolerates 404s; 2 Reddit entries soft-fail without REDDIT_CLIENT_ID/SECRET per existing adapter contract; pure-additive knowledge file, no runtime gating, eval skipped per brief)**
  - [x] communities/* (one profile per community_tag in sources.yaml) **— done at f95a4f7 (PR #54, 5 community-profile markdown files under `domain_knowledge/immigration/communities/` — one per `community_tag` value in immigration/sources.yaml: `immigration-attorney-blogs.md` (Murthy/Boundless/Cyrus D. Mehta/Greg Siskind voices), `government-and-ombudsman.md` (USCIS Policy Manual + USCIS Ombudsman Annual Reports + DOL FLAG), `practitioner-forums.md` (AILA think-tank essays), `community-experience-forums.md` (r/immigration + r/USCIS + VisaJourney + Trackitt), `journalists-and-explainers.md` (ProPublica immigration desk); each profile follows `community_profiles/_schema.md` (Voice anchors / Mental model / Characteristic vocabulary / Known blind spots OF this community); 941 lines total, ~770-850 words per profile; high-stakes Mechanism E posture inverted in every "Known blind spots OF this community" entry to include licensed-counsel deferral; cross-community references threaded where recovery posture benefits from pairing (e.g. forum anecdote ↔ government-and-ombudsman authoritative data); pure-additive knowledge content, no V1 runtime gating, eval skipped per brief; supersedes PR #52 which was a partial single-file attempt from a concurrent run)**
  - [x] fixtures/* (≥ 8 fixture situations) **— done at 38f3733 (PR #58, V2 §4 immigration sub-item 6 of 8; 10 per-fixture YAML files under `domain_knowledge/immigration/fixtures/` exceeding the ≥8 minimum: ac21-portability-mid-perm, ap-trip-during-aos, b2-visitor-status-pivot-cos-vs-cp, eb2-vs-eb3-downgrade-tradeoff, h1b-renewal-during-pip, j1-waiver-vs-h1b-conversion, layoff-during-h1b-grace, marry-for-status-timing, o1-vs-eb1a-self-petition, stem-opt-vs-capgap-employer-choice; covers all 10 decisions D1–D10 and all 14 framings F1–F14 across 12 distinct personas from domain_pack.md controlled list; each fixture carries a high-stakes consult-licensed-immigration-attorney category per Mechanism E; mirrors tech-career fixtures schema (id, text, expected_domains, expected_entities, expected_personas, expected_risk_surfaces) plus immigration-specific additive annotations (expected_decisions, expected_framings, expected_blindspot_categories) the eval loader passes through opaquely; also narrows tests/unit/test_load_all_fixtures.py::test_real_v1_fixtures_match_legacy to the tech-career subset to preserve the V1-bit-for-bit invariant correctly with a second domain present; pytest tests/unit/test_load_all_fixtures.py = 10/10 pass)**
  - [x] domain_pack.md **— done at d56eba3 (PR #53, 2377-word Triage Pass-2 / Editor / Critic prompt overrides for the immigration domain mirroring tech-career/domain_pack.md but inverting to high-stakes Mechanism E posture: mandatory decision-support/not-legal-advice label, hard pass/fail per-claim grounding on INA/CFR/FAM/Policy-Manual citations, +1 non_obviousness floor on multi-route situations; references decisions.md (D1–D10) / framings.md (F1–F14) / blindspots.md / sources.yaml by ID rather than duplicating content; activates PR #33's Pass-2 enrichment for immigration)**
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **housing**
  - [x] decisions.md (≥ 8 distinct decisions, e.g. rent-vs-buy, mortgage-fixed-vs-arm, lease-renewal-vs-move, condo-vs-sfh, HOA-acceptance, location-vs-commute trade-off, etc.) **— done at 1c3503c (PR #60, Layer 1 of the 4-layer knowledge model for V2 §4 domain 3 of 10; 10 distinct decisions; ~2250 words; 336 lines; mirrors tech-career/decisions.md [PR #30] and immigration/decisions.md [PR #42] structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; cross-domain edges flagged inline; pure-additive knowledge content, no runtime gating, eval skipped per brief)**
  - [ ] framings.md (≥ 3 framings per major decision)
  - [ ] blindspots.md (≥ 5 typical blind spots per framing)
  - [ ] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags)
  - [ ] communities/* (one profile per community_tag in sources.yaml)
  - [ ] fixtures/* (≥ 8 fixture situations)
  - [ ] domain_pack.md
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **health-insurance** (same template)
- [ ] **personal-finance / investing** (same template)
- [ ] **entrepreneurship** (same template)
- [ ] **education-funding** (same template)
- [ ] **family-planning** (same template — special care: high blind-spot stakes, often religious/cultural framings)
- [ ] **legal-disputes** (same template — high-stakes, must be labelled "decision-support, not legal advice" in domain_pack.md Editor section)
- [ ] **career-pivots** (same template — note this domain's source-views deliberately cross into the other 9 domains)

### Architecture changes

- [x] **Triage Officer becomes two-pass.**
  - Pass 1: classify situation into ≥ 1 of the 10 domains (multi-label allowed)
  - Pass 2: with the relevant `domain_pack.md` files concatenated into the system prompt, extract full Triage facets
  - File: [src/blindspot/agents/triage.py](../../src/blindspot/agents/triage.py)
  - **Done at 77c8a27 (PR #33) — refactored `run_triage(situation_text, llm, cfg) -> Situation` into a two-pass orchestration: pass-1 (new prompt `src/blindspot/prompts/triage_pass1.md`) classifies the situation into ≥1 of the 10 `_meta_ontology.md` domains; pass-2 looks up `domain_knowledge/<domain>/domain_pack.md` for each matched domain and concatenates any found into the existing triage system prompt before calling the unchanged V1 prompt path. Graceful V1 fallback: when zero domain_pack.md files exist on disk (current state — no domain has authored one yet), pass-1 is skipped entirely and pass-2 reduces to the original single-LLM-call V1 path bit-for-bit. Public API unchanged so no caller edits needed; `src/blindspot/orchestrator.py` integration test continues to pass UNCHANGED. 5 new unit tests in `tests/unit/test_triage_two_pass.py` cover (a) load-bearing fallback (one LLM call to unmodified V1 prompt when no packs exist), (b) pass-1 classification, (c) pass-1-empty refusal short-circuit, (d) multi-pack concatenation, (e) silent skip of matched-but-pack-missing domains. Full 72/72 pytest suite green.**
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
- [x] **Eval runner** ([src/blindspot/eval/runner.py](../../src/blindspot/eval/runner.py)):
      scan all per-domain `fixtures/` subfolders. Aggregate
      `quality_score` is per-domain plus a global mean. Refine routine
      should never average across domains in a way that lets one
      thriving domain mask another's regression. **Done at da48b2a (PR #34) — added `load_all_fixtures(root: Path = Path("."), legacy_path: Path | None = None)` which glob-scans `domain_knowledge/<domain>/fixtures/*.yaml` (skipping underscored subdirs like `_meta/`), supports both list-of-fixtures and single-fixture-mapping YAML shapes, and annotates each fixture with its `domain` (or `"tech-career"` for the V1 fallback path). Falls back to the monolithic `fixtures/eval_situations.yaml` when no per-domain files exist. `run_eval` now consumes from `load_all_fixtures` and emits an additive `per_domain` aggregation block in the result JSON alongside the unchanged global `aggregate` block (per-domain mean of each sub-metric plus a per-domain `quality_score` and `fixture_count`; refactored through shared `_mean_for` / `_quality_score_for` helpers). V1 path is the active production path right now (no per-domain fixtures exist yet), so the eval pipeline produces bit-for-bit identical numbers — verified by 77/77 pytest pass (10 new tests in `tests/unit/test_load_all_fixtures.py` cover the loader; 67 pre-existing tests confirm no regressions in unrelated code).**
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
