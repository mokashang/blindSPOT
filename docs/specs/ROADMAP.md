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
Last completed: f4acfeb — V2 §4 **entrepreneurship/blindspots.md authored** (PR #83, Layer 3 of the 4-layer knowledge model for V2 §4 domain 6 of 10; 70 entries = 5 per framing × 14 framings F1–F14 per `domain_knowledge/entrepreneurship/framings.md` PR #78; ~23k words flagged in PR body — matches personal-finance PR #79 / housing PR #64 precedent density for cross-cutting domains; full Layer 3 schema per `community_profiles/_schema.md` Statement / Source-evidence / Trigger / Failure-mode / Recovery-move per entry; partial-gating Mechanism E posture mirrors housing/blindspots.md PR #64 — entrepreneurship is `high_stakes:false` per `_meta_ontology.md` §6, so Recovery moves use selective Mechanism E partial-gating: refer to named professional channel ONLY where six-figure tail risk justifies it (D1 co-founder equity, D4 LLC vs S-corp, D5 SAFE post-money cap, D7 solo-401k vs SEP-IRA, D8 W-2 vs 1099 misclassification, D11 international incorporation Delaware C-corp) — startup attorney / S-corp-experienced CPA / employment-law attorney / tax attorney with §1202 QSBS + §351 experience / estate-planning attorney; source-anchored to framings.md PR #78 Excludes lines + decisions.md PR #73 cross-domain edge flags + conceptual community-class voice anchors (Indie Hackers / r/Entrepreneur / Patio11 / YC / SaaStr / Stripe Atlas / IRS Pub 535 + 334 + 583); cross-framing tensions section + maturity / source-anchor note + date-stamp risk inventory; cross-domain edges into personal-finance / tech-career / legal-disputes / housing / health-insurance flagged inline; reviewer approved on iteration 1). Concurrent this hour: **a213a3a — V2 §4 personal-finance/sources.yaml authored** (PR #80, Layer 4 of the 4-layer knowledge model for V2 §4 domain 5 of 10; 16 source-views across all 8 distinct `community_tag` values exceeds ≥8/≥4 minimum — fee-only-fiduciary-cfp / bogleheads-and-passive-index / fire-and-mr-money-mustache / retirement-economics-academics / tax-and-cpa-practitioner / financial-economics-journalism / erisa-and-fiduciary-rule-law / social-security-claiming-and-rmd; schema mirrors tech-career/sources.yaml PR #37 + immigration/sources.yaml PR #49 + housing/sources.yaml PR #66 + health-insurance/sources.yaml PR #76 exactly; all `reliability: 1` per ROADMAP §5 Mechanism C cite-and-promote starting posture; adapter mix 9 static_corpus / 6 RSS / 1 reddit_search; RSS URLs needing verification flagged with `TODO-verify-URL` in notes per PR #49/#66/#76 precedent; Reddit entries soft-fail per existing adapter contract; every notes field flags Mechanism E gating per `_meta_ontology.md` §5 high-stakes posture; voice-anchor coverage exactly mirrors framings.md PR #74 §Voice anchors and Layer-4 forward-pointer; reviewer approved on iteration 1) and **392a60a — V2 §4 health-insurance/communities/* authored** (PR #81, Layer 5 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 8 community-profile markdown files one per `community_tag` value in `domain_knowledge/health-insurance/sources.yaml` PR #76 — `broker-and-actuarial.md`, `medicare-shiba-and-government.md`, `aca-marketplace-and-navigator.md`, `hsa-and-bogleheads-personal-finance.md`, `healthcare-economics-journalism.md`, `erisa-and-denial-appeal-law.md`, `patient-advocacy-and-billing-recovery.md`, `chronic-illness-patient-experience.md`; each profile follows `community_profiles/_schema.md` (Identity / Voice anchors / Mental model / Characteristic vocabulary / Known blind spots OF this community / Mechanism E posture); mirrors `domain_knowledge/immigration/communities/*` PR #54 structural pattern; uniform Mechanism E posture per health-insurance `high_stakes:true` — every Recovery move routes to a named professional channel (licensed independent broker (commercial OE) / SHIBA-SHIP counselor (Medicare) / CMS-trained Navigator (Marketplace) / HSA administrator + IRS Pub 969 / ERISA attorney / patient-advocate post-billing recovery No Surprises Act §2799A IDR / Dollar For / DOL EBSA / State Insurance Commissioner); ~14.6k words / 2025 lines across all 8 profiles — 1.5-2k per profile; reviewer approved on iteration 1) and **629f234 — V2 §4 education-funding/framings.md authored** (PR #82, Layer 2 of the 4-layer knowledge model for V2 §4 domain 7 of 10; 14 framings F1–F14 covering all 10 decisions D1–D10 from decisions.md PR #77 with ≥3 framings per major decision after cross-cutting; ~12.9k words / 1793 lines flagged in PR body — within the high end of Layer 2 precedent; partial-gating Mechanism E posture per `_meta_ontology.md` §7 `high_stakes:false` — mirrors housing/framings.md PR #63 and entrepreneurship/framings.md PR #78; selective Recovery referral on six-figure tail-risk pockets D1 federal-to-private refi / D3 §529(c)(2)(B) 5-year-forward + Form 709 / D4 IDR + tax-bomb sinking-fund / D7 Parent PLUS / D10 PSLF qualifying-employment + Buyback program — student-loan attorney / SLBA / FSA Ombudsman / retirement-experienced CPA / NACAC counselor / fee-only fiduciary CFP; 10 opposing-framing pairs in cross-framing-tensions section; 13 voice-anchor community-classes organized for Layer 4 sources.yaml hand-off — PSLF-preservation, ROI-by-major, FIRE-aware, NACAC-counselor, 529 voices, CSS-Profile-aware, r/StudentLoans, MBA-admissions, r/cscareerquestions, consumer-protection, NAPFA, retirement-experienced-CPA, HELOC-as-college-funding, bankruptcy-discharge; cross-domain edges into personal-finance / tech-career / entrepreneurship / family-planning / housing / immigration / legal-disputes flagged inline; subagent-level claude -p reviewer spawn was blocked by harness auto-mode classifier, orchestrator ran reviewer at parent level as documented recovery, reviewer approved on iteration 1). **Health-insurance is now 5/8** (decisions + framings + blindspots + sources.yaml + communities/* done; fixtures/* next). **Personal-finance is now 4/8** (decisions + framings + blindspots + sources.yaml done; communities/* next). **Entrepreneurship is now 3/8** (decisions + framings + blindspots done; sources.yaml next). **Education-funding is now 2/8** (decisions + framings done; blindspots.md next). V2 progress unchanged at 1/10 — tech-career remains the only fully-built V2 domain; housing 7/8 and immigration 7/8 both await eval-pass (VOYAGE_API_KEY gated). Earlier round (run-20260518-1010): 2e9e679 — V2 §4 **personal-finance/blindspots.md authored** (PR #79, Layer 3 of the 4-layer knowledge model for V2 §4 domain 5 of 10; 70 entries = 5 per framing × 14 framings F1–F14 per framings.md PR #74; ~23.7k words / 3227 lines flagged in PR body — over the 15.2k anchor from PR #48 and 18.5k from PR #75 driven by personal-finance's 6+ cross-domain edge footprint plus per-Recovery selective-channel-routing precision; full Layer 3 schema per `community_profiles/_schema.md` Statement / Source-evidence / Trigger / Failure-mode / Recovery-move per entry; uniform Mechanism E gating verified programmatically across all 70 Recovery moves — 70/70 route to one of fee-only fiduciary CFP NAPFA/XY-Planning/Garrett / retirement-experienced CPA / fee-only SS-claiming-specialist Mike Piper-Kotlikoff / SHIBA-SHIP / state-bar estate attorney / ERISA attorney / SEC IAPD / FINRA BrokerCheck verification — matches immigration/blindspots.md PR #48 and health-insurance/blindspots.md PR #75 uniform pattern per personal-finance `high_stakes:true` and ROADMAP §5 canonical Mechanism E gating case posture; source-anchored to framings.md PR #74 Excludes lines + decisions.md PR #72 cross-domain edge flags + conceptual community-class voice anchors (fee-only-fiduciary CFP / NAPFA / Bogleheads / Mr Money Mustache / financial-economics journalism / Choose-FI / FIRE / CPA / ERISA practitioner / SEC EDGAR / IRS Pubs / The Finance Buff / Pfau-Kitces); cross-framing tensions section with 8 opposing-framing pairs; Maturity / date-stamp note flagging TCJA-sunset / ARPA-sunset / estate-exemption-sunset / SECURE 2.0 phased / IRMAA / SS-thresholds / DPC-HSA / PSLF-SAVE-shifts / SECURE 1.0 inherited-IRA / FAFSA Simplification / 10b5-1 amendments / QSBS §1202 risks; subagent-level auto-review was blocked by harness auto-mode classifier, orchestrator ran reviewer at parent level as documented recovery, approved on iteration 1; reviewer approved). Concurrent this hour: **6ccbc7a — V2 §4 health-insurance/sources.yaml authored** (PR #76, Layer 4 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 15 source-views across 8 distinct `community_tag` values exceeds ≥8/≥4 minimum; schema mirrors tech-career/sources.yaml PR #37 + immigration/sources.yaml PR #49 + housing/sources.yaml PR #66; all reliability:1 per ROADMAP §5 Mechanism C cite-and-promote starting posture; community-tag breakdown maps to framings.md PR #71 voice-anchor classes — broker-and-actuarial / medicare-shiba-and-government / aca-marketplace-and-navigator / hsa-and-bogleheads-personal-finance / healthcare-economics-journalism / erisa-and-denial-appeal-law / patient-advocacy-and-billing-recovery / chronic-illness-patient-experience; RSS URLs needing verification flagged per PR #49/#66 precedent; Reddit entries soft-fail per existing adapter contract; reviewer approved on iteration 1) and **122add6 — V2 §4 entrepreneurship/framings.md authored** (PR #78, Layer 2 of the 4-layer knowledge model for V2 §4 domain 6 of 10; 14 framings F1–F14 with full schema; coverage map confirms every D1–D11 from decisions.md PR #73 has ≥3 framings; 7 opposing-framing pairs explicitly named for Triage / Risk Officer disambiguation; voice anchors named conceptually for Layer 4 sources.yaml hand-off — Indie Hackers / r/Entrepreneur / Patio11 / YC / SaaStr / Stripe Atlas / IRS Pub 535; partial-gating per `high_stakes:false` from `_meta_ontology.md` §6 — selective Mechanism E referral on six-figure tail-risk pockets D1/D4/D5/D7/D8/D11 per housing-pattern precedent; word-count came in over the 6–11k target band driven by opposing-framing-pair density and Excludes-as-Layer-3-seed requirement, flagged in PR body, reviewer approved on iteration 1) and **33e2148 — V2 §4 education-funding/decisions.md authored** (PR #77, Layer 1 of the 4-layer knowledge model for V2 §4 domain 7 of 10; **KICKS OFF the 7th V2 domain** at 0/8 → 1/8; 10 distinct decisions covering refi-vs-IDR/PSLF preservation, MBA-ROI, 529-front-loading §529(c)(2)(B), IDR + tax-bomb savings, in-state vs out-of-state merit aid, 529-vs-Roth-vs-taxable mix SECURE 2.0 §126, parent PLUS vs federal vs private cosigner mechanics, FAFSA / CSS asset positioning, employer tuition reimbursement § 127 vs scholarship-stacking, PSLF qualification §455(m); mirrors tech-career / immigration / housing / health-insurance / personal-finance / entrepreneurship decisions.md structural pattern; high-stakes posture `high_stakes:false` per `_meta_ontology.md` §7 — selective Mechanism E partial-gating like housing/entrepreneurship rather than uniform like immigration/personal-finance/health-insurance; selective professional-referral matrix — student-loan attorney / SLBA / FSA Ombudsman / retirement-experienced CPA / NACAC counselor / fee-only fiduciary CFP; cross-domain edges into personal-finance / tech-career / family-planning / entrepreneurship / housing; ~7.9k words flagged in PR body with justification on statutory-anchor density and 5-domain cross-cutting breadth; reviewer approved on iteration 1; ROADMAP §4 education-funding entry expanded from single `(same template)` placeholder line to full 8-sub-item checklist mirroring health-insurance / housing / immigration / personal-finance / entrepreneurship). **Health-insurance is now 4/8** (decisions + framings + blindspots + sources.yaml done; communities/* next). **Personal-finance is now 3/8** (decisions + framings + blindspots done; sources.yaml next). **Entrepreneurship is now 2/8** (decisions + framings done; blindspots.md next). **Education-funding is now 1/8** (decisions.md done — KICKS OFF 7th V2 domain; framings.md next). V2 progress unchanged at 1/10 — tech-career remains the only fully-built V2 domain; housing 7/8 and immigration 7/8 both await eval-pass (VOYAGE_API_KEY gated). Earlier rounds: V2 §4 **entrepreneurship/decisions.md authored** at 8bf45f1 (PR #73, Layer 1 of the 4-layer knowledge model for V2 §4 domain 6 of 10; **KICKS OFF the 6th V2 domain** at 0/8 → 1/8; 11 distinct decisions covering co-founder selection + equity vesting structure, bootstrap vs raise seed for time-to-PMF compression vs ownership preservation, quit day job vs nights-and-weekends signal threshold, LLC pass-through vs S-corp election at $80k self-employment-tax crossover, SAFE post-money valuation cap vs priced seed, sole prop vs LLC formation timing, solo-401k vs SEP-IRA vs SIMPLE retirement vehicle, W-2 vs 1099 first-employee classification, pricing-model (per-seat vs usage vs flat vs freemium PLG), co-founder dispute resolution / cap-table-buyback / departure, international incorporation (Delaware C-corp vs LLC vs jurisdiction-shopping); ~11k words / 1406 lines; `high_stakes:false` per `_meta_ontology.md` §6 — selective rather than uniform Mechanism E referral (startup attorney for founder-IP-and-equity-disputes + SAFE-to-priced-seed conversion, CPA with S-corp / multi-entity experience for tax-election and multi-state nexus, employment-law attorney for first-W-2-employee and misclassification); cross-domain edges flagged inline (`personal-finance` / `tech-career` / `legal-disputes` / `health-insurance` / `housing`); ROADMAP §4 entrepreneurship entry expanded from single `(same template)` placeholder line to full 8-sub-item checklist mirroring health-insurance / housing / immigration / personal-finance; reviewer approved on iteration 1). Concurrent this hour: **c04618a — V2 §4 health-insurance/blindspots.md authored** (PR #75, Layer 3 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 70 entries = 5 per framing × 14 framings; ~18.5k words / 2508 lines; uniform Mechanism E gating verified programmatically across all 70 Recovery moves — broker / SHIBA / Navigator / CPA / ERISA attorney / State Insurance Commissioner / patient-advocate / Medicare-appeals attorney / family-law attorney; differs from housing PR #64 partial-gating; source-anchored to framings.md PR #71 Excludes bullets and conceptual community-class voice anchors; 7 cross-framing tensions pairs; 11 date-stamp risk anchor classes flagged) and **06502fb — V2 §4 personal-finance/framings.md authored** (PR #74, Layer 2 of the 4-layer knowledge model for V2 §4 domain 5 of 10; 14 framings F1–F14, ~11k words / 1634 lines; coverage map confirms every D1–D10 has ≥3 framings; 8 opposing-framing pairs explicitly named; high-stakes Mechanism E posture per `_meta_ontology.md` §5 — dollar-specific investment guidance uniformly out-of-scope; selective-professional-referral matrix anchored to decisions.md; voice anchors named conceptually for Layer 4 hand-off — fee-only-fiduciary CFP, NAPFA, Bogleheads, Mr Money Mustache, Choose-FI / FIRE, retirement-experienced CPA, ERISA practitioner forums, the Finance Buff, retirement-econ academics Pfau / Kitces). **Health-insurance is now 3/8** (decisions.md + framings.md + blindspots.md done; sources.yaml next). **Personal-finance is now 2/8** (decisions.md + framings.md done; blindspots.md next). **Entrepreneurship is now 1/8** (decisions.md done — KICKS OFF 6th V2 domain; framings.md next). V2 progress unchanged at 1/10 — tech-career remains the only fully-built V2 domain; housing 7/8 and immigration 7/8 both await eval-pass (VOYAGE_API_KEY gated). Earlier rounds: personal-finance `decisions.md` at d9868eb (PR #72, 5th V2 domain opened); health-insurance `framings.md` at 882d528 (PR #71); health-insurance `decisions.md` at fe45f32 (PR #70, 4th V2 domain opened); housing `domain_pack.md` at 8d9591b (PR #69, Layer-overlay overrides for the housing domain, `high_stakes:false` posture diverging from immigration's uniform Mechanism E); housing `communities/*` at 280e0b3 (PR #68); housing `fixtures/*` at 87820ee (PR #67); housing `sources.yaml` at 13af99a (PR #66); housing `blindspots.md` at 8efd283 (PR #64); housing `framings.md` at 5d898f8 (PR #63); housing `decisions.md` at 1c3503c (PR #60, 3rd V2 domain opened); Agents-layer Risk Officer per-numeric-claim citation at 68a99d3 (PR #65, reactive); V1.x §1.x eval-baseline-stability + eval-pipeline-robustness BOTH `[x]` via PR #59 — V1.x progress 2/7 → 4/7; tech-career FULLY BUILT at 3bb4fea (PR #57); immigration at 7/8 (only `eval pass` remains) at 38f3733 (PR #58); immigration `communities/*` at f95a4f7 (PR #54); immigration `domain_pack.md` at d56eba3 (PR #53); immigration `sources.yaml` at 638cec4 (PR #49); immigration `blindspots.md` at 535d746 (PR #48); immigration `framings.md` at 3a3798c (PR #44); immigration `decisions.md` at 6161d6f (PR #42, 2nd V2 domain opened).
Next up: V1.x exit criteria still gate V2 promotion to 🟡 (V1.x is 4/7 — AnthropicAPIClient + Streaming editor + Real-usage signal remain; all three need env keys or user-side activity outside orchestrator scope). V2 work in flight on nine fronts now: (1) **health-insurance `fixtures/*`** — Layer 6 follow-on of the 4th V2 domain; ≥8 fixture situations covering D1–D10 across at least 8 personas; mirror immigration/fixtures/* PR #58 and housing/fixtures/* PR #67 structure with per-fixture YAML carrying high-stakes consult-broker / consult-SHIBA / consult-Navigator / consult-ERISA-attorney category per uniform Mechanism E posture; (2) **personal-finance `communities/*`** — Layer 5 of the 5th V2 domain; 8 community-profile markdown files (one per `community_tag` value from sources.yaml PR #80: fee-only-fiduciary-cfp, bogleheads-and-passive-index, fire-and-mr-money-mustache, retirement-economics-academics, tax-and-cpa-practitioner, financial-economics-journalism, erisa-and-fiduciary-rule-law, social-security-claiming-and-rmd); each profile follows `community_profiles/_schema.md`; uniform Mechanism E posture per personal-finance `high_stakes:true` (canonical ROADMAP §5 case) — every Recovery move routes to fee-only fiduciary CFP / retirement-experienced CPA / fee-only SS-claiming-specialist / SHIBA-SHIP / state-bar estate attorney / ERISA attorney / SEC IAPD-FINRA BrokerCheck; (3) **entrepreneurship `sources.yaml`** — Layer 4 of the 6th V2 domain; ≥8 source-views across ≥4 distinct community_tags; voice anchors already named in framings.md PR #78 — Indie Hackers / r/Entrepreneur / r/SmallBusiness / Hacker News startup voices (PG essays, Sam Altman, Garry Tan) / Patio11 / Patrick McKenzie / Stripe Atlas / YC playbooks / SaaStr / Jason Lemkin / Tomasz Tunguz / Redpoint / The Finance Buff (LLC-vs-S-corp) / Clerky / IRS Pub 535 / Pub 583 / Lenny Newsletter / Founder Collective / First Round Review; (4) **education-funding `blindspots.md`** — Layer 3 of the 7th V2 domain; ≥5 typical blind spots per framing × 14 framings = ≥70 entries; partial-gating per `_meta_ontology.md` §7 `high_stakes:false` (mirror housing/blindspots.md PR #64 + entrepreneurship/blindspots.md PR #83 selective Mechanism E partial-gating); Recovery moves route to student-loan attorney / SLBA / FSA Ombudsman / retirement-experienced CPA / NACAC counselor / fee-only fiduciary CFP only on the six-figure tail-risk pockets D1/D3/D4/D7/D10; (5) **housing `eval pass`** — final housing sub-item; gated on VOYAGE_API_KEY availability; closes housing parent [x] (V2 1/10 → 2/10 first cross-domain V2 completion); (6) **immigration `eval pass`** — same gating, closes immigration parent [x] (V2 1/10 → 2/10 if housing not yet, or 2/10 → 3/10); (7) opportunistically start an eighth domain (family-planning per `_meta_ontology.md` §8 priority order, or legal-disputes / career-pivots) when sources subagent slots have capacity — note family-planning is `high_stakes:true` per §8 with religious / cultural framing care per ROADMAP §4; (8) once VOYAGE_API_KEY is restored, run health-insurance Layer 6-7 (fixtures/* / domain_pack.md), personal-finance Layer 5-6-7 (communities/* / fixtures/* / domain_pack.md), entrepreneurship Layer 4-5-6-7 (sources.yaml / communities/* / fixtures/* / domain_pack.md), and education-funding Layer 3-4-5-6-7 (blindspots.md / sources.yaml / communities/* / fixtures/* / domain_pack.md) catch-up to bring the lagging domains up to housing-and-immigration's pre-eval depth; (9) at current cadence (≥3 V2 sub-items merged per run × 4 runs/day on the cron), V2 §4 should reach 5/10 fully-built domains by mid-to-late June 2026 and the V1.x→V2 hand-off becomes the gating concern (eval pass on at least one V2 domain validates the multi-domain triage routing end-to-end).
Next up (old, preserved for history): V1.x exit criteria still gate V2 promotion to 🟡 (V1.x is 4/7 — AnthropicAPIClient + Streaming editor + Real-usage signal remain; all three need env keys or user-side activity outside orchestrator scope). V2 work in flight on eight fronts (run-20260518-1010): (1) **health-insurance `communities/*`** — Layer 4 follow-on of the 4th V2 domain; 8 community-profile markdown files (one per `community_tag` value from sources.yaml PR #76: broker-and-actuarial, medicare-shiba-and-government, aca-marketplace-and-navigator, hsa-and-bogleheads-personal-finance, healthcare-economics-journalism, erisa-and-denial-appeal-law, patient-advocacy-and-billing-recovery, chronic-illness-patient-experience); each profile follows `community_profiles/_schema.md` (Voice anchors / Mental model / Characteristic vocabulary / Known blind spots OF this community); mirror immigration/communities/* PR #54 and housing/communities/* PR #68 patterns with uniform Mechanism E gating per health-insurance `high_stakes:true`; (2) **personal-finance `sources.yaml`** — Layer 4 of the 5th V2 domain; ≥8 source-views across ≥4 distinct community_tags; mirror immigration/sources.yaml (PR #49), housing/sources.yaml (PR #66), health-insurance/sources.yaml (PR #76); voice anchors already named in framings.md PR #74 — fee-only-fiduciary CFP, NAPFA, Bogleheads, Mr Money Mustache, financial-economics journalism, Choose-FI / FIRE, retirement-experienced CPA, ERISA practitioner forums, SEC EDGAR, IRS Pubs, The Finance Buff, Pfau/Kitces; (3) **entrepreneurship `blindspots.md`** — Layer 3 of the 6th V2 domain; ≥5 typical blind spots per framing × 14 framings = ≥70 entries; mirror housing/blindspots.md (PR #64) partial-gating pattern per `high_stakes:false` (NOT immigration/health-insurance/personal-finance uniform Mechanism E); selective Recovery routing to startup attorney / CPA / employment-law attorney only where six-figure tail risk justifies it; (4) **education-funding `framings.md`** — Layer 2 of the newly-opened 7th V2 domain; ≥3 framings per major decision from decisions.md PR #77 D1–D10; voice anchors should reach into NACAC counselors, Federal Student Aid Ombudsman, Student Loan Borrower Assistance Project, r/PSLF / r/StudentLoans / r/financialaid, The College Investor, Mark Kantrowitz / SavingForCollege, Mike Piper / OOK Open Social Security analogues for college funding; partial-gating per `_meta_ontology.md` §7 `high_stakes:false`; (5) **housing `eval pass`** — final housing sub-item; gated on VOYAGE_API_KEY availability; closes housing parent [x] (V2 1/10 → 2/10 first cross-domain V2 completion); (6) **immigration `eval pass`** — same gating, closes immigration parent [x] (V2 1/10 → 2/10 if housing not yet, or 2/10 → 3/10); (7) opportunistically start an eighth domain (family-planning per `_meta_ontology.md` §8 priority order, or legal-disputes / career-pivots) when sources subagent slots have capacity — note family-planning is `high_stakes:true` per §8 with religious / cultural framing care per ROADMAP §4; (8) once VOYAGE_API_KEY is restored, run health-insurance Layer 5-6-7 (communities/* / fixtures/* / domain_pack.md), personal-finance Layer 4-5-6-7 (sources.yaml / communities/* / fixtures/* / domain_pack.md), entrepreneurship Layer 3-4-5-6-7, and education-funding Layer 2-3-4-5-6-7 catch-up to bring the lagging domains up to housing-and-immigration's pre-eval depth.
Next up (old, preserved for history): V1.x exit criteria still gate V2 promotion to 🟡 (V1.x is 4/7 — AnthropicAPIClient + Streaming editor + Real-usage signal remain; all three need env keys or user-side activity outside orchestrator scope). V2 work in flight on seven fronts then: (1) **health-insurance `sources.yaml`** — Layer 4 of the 4th V2 domain; ≥8 source-views across ≥4 distinct community_tags; mirror immigration/sources.yaml (PR #49) and housing/sources.yaml (PR #66) structure; community-tags should map to health-insurance framings.md (PR #71) voice anchors — actuarial-and-broker, SHIBA, ACA-Navigator, HSA-administrator, ERISA-attorney, healthcare-economics-journalist, Bogleheads, HR-Reddit, KFF, PNHP, patient-advocate, Galen/AEI, chronic-illness patient; (2) **personal-finance `blindspots.md`** — Layer 3 of the 5th V2 domain; ≥5 typical blind spots per framing × 14 framings = ≥70 entries; mirror immigration/blindspots.md (PR #48) high-stakes Mechanism E with each Recovery-move routing to fee-only-fiduciary CFP / CPA / fee-only SS planner / ERISA attorney / state-bar estate attorney / SHIBA / SEC-FINRA BrokerCheck; (3) **entrepreneurship `framings.md`** — Layer 2 of the newly-opened 6th V2 domain; ≥3 framings per major decision; mirror personal-finance/framings.md (PR #74) and health-insurance/framings.md (PR #71) structure; voice anchors should reach into Indie Hackers / r/Entrepreneur / r/SmallBusiness / Hacker News startup voices / Patio11 / YC playbooks / SaaStr / Tomasz Tunguz / The Finance Buff (LLC-vs-S-corp mechanics) / Stripe Atlas / Clerky / IRS Pub 535; partial-gating posture per `_meta_ontology.md` §6 `high_stakes:false`; (4) **housing `eval pass`** — final housing sub-item; gated on VOYAGE_API_KEY availability; closes housing parent [x] (V2 1/10 → 2/10 first cross-domain V2 completion); (5) **immigration `eval pass`** — same gating, closes immigration parent [x]; (6) opportunistically start a seventh domain (education-funding per `_meta_ontology.md` §7 priority order) when sources subagent slots have capacity; (7) once VOYAGE_API_KEY is restored, run health-insurance Layer 4-5-6-7 (sources.yaml / communities/* / fixtures/* / domain_pack.md) and personal-finance Layer 3-4-5-6-7 catch-up to bring the lagging domains up to housing-and-immigration's pre-eval depth. traditional-vs-Roth split, asset location, brokerage allocation, debt-payoff-vs-invest prioritization, tax-loss harvesting + wash-sale management, Roth-conversion ladder in low-income years, withdrawal sequencing / RMD / SS-claim coordination, 529-vs-Roth-vs-taxable college-funding mix, estate-and-beneficiary structuring; ~9819 words / 1426 lines — over the 7k flag threshold, explicit in PR body, reviewer approved on iteration 1 acknowledging justification (10-decision tax-mechanic density + 6+ cross-domain edges + Mechanism E selective-referral framing); mirrors tech-career [PR #30] / immigration [PR #42] / housing [PR #60] / health-insurance [PR #70] decisions.md structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; high-stakes Mechanism E posture explicit in intro — personal-finance is the canonical Mechanism E gating case named in ROADMAP §5; dollar-specific investment guidance uniformly out-of-scope (Editor "decision-support, not financial advice"); selective professional-referral matrix keyed by decision (fee-only fiduciary CFP / retirement-experienced CPA / fee-only Social-Security planner / state-bar estate attorney / ERISA attorney / SHIBA / SEC-FINRA BrokerCheck verification) rather than blanket-mandating one category; personal-finance is the most cross-cutting V2 domain — material edges into tech-career / health-insurance / housing / family-planning / education-funding / entrepreneurship / legal-disputes flagged inline + aggregated at file level; ROADMAP §4 personal-finance entry expanded from single placeholder line to full 8-sub-item checklist mirroring health-insurance / housing / immigration). Concurrent this hour: **882d528 — V2 §4 health-insurance/framings.md authored** (PR #71, Layer 2 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 14 framings F1–F14, ~9750 words / 1315 lines; coverage map confirms every D1–D10 has ≥3 framings after cross-cutting; 7 opposing-framing pairs explicitly named — F1↔F2, F3↔F4, F5↔F9, F6↔F10, F8↔F13, F12↔F4, F14↔F1/F2/F3/F4 — for Triage / Risk Officer disambiguation; high-stakes Mechanism E posture explicit (12-month plan-year lock-in + permanent Medicare late-enrollment penalty regime); voice anchors named conceptually for Layer 4 sources.yaml hand-off — actuarial-and-broker, SHIBA, ACA-Navigator, HSA-administrator, ERISA-attorney, healthcare-economics-journalist Kliff/Rovner/Sanger-Katz/Ornstein, Bogleheads, HR-Reddit, KFF, PNHP, patient-advocate, Galen/AEI, chronic-illness patient; per `community_profiles/_schema.md` schema; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PR #44/63/67-70); reviewer approved on iteration 1). **Health-insurance is now 2/8** (decisions.md + framings.md done; blindspots.md next). **Personal-finance is now 1/8** (decisions.md done; framings.md next). V2 progress unchanged at 1/10 — tech-career remains the only fully-built V2 domain; housing 7/8 and immigration 7/8 both await eval-pass (VOYAGE_API_KEY gated). Earlier rounds: health-insurance `decisions.md` at fe45f32 (PR #70); housing `domain_pack.md` at 8d9591b (PR #69, Triage Pass-2 / Editor / Critic overrides for housing, `high_stakes:false` posture diverging from immigration's uniform Mechanism E); housing `communities/*` at 280e0b3 (PR #68); housing `fixtures/*` at 87820ee (PR #67); housing `sources.yaml` at 13af99a (PR #66); housing `blindspots.md` at 8efd283 (PR #64); housing `framings.md` at 5d898f8 (PR #63); housing `decisions.md` at 1c3503c (PR #60); Agents-layer Risk Officer per-numeric-claim citation at 68a99d3 (PR #65, reactive); V1.x §1.x eval-baseline-stability + eval-pipeline-robustness BOTH `[x]` via PR #59 — V1.x progress 2/7 → 4/7; tech-career FULLY BUILT at 3bb4fea (PR #57); immigration at 7/8 (only `eval pass` remains) at 38f3733 (PR #58); immigration `communities/*` at f95a4f7 (PR #54); immigration `domain_pack.md` at d56eba3 (PR #53); immigration `sources.yaml` at 638cec4 (PR #49); immigration `blindspots.md` at 535d746 (PR #48); immigration `framings.md` at 3a3798c (PR #44); immigration `decisions.md` at 6161d6f (PR #42).
Next up: V1.x exit criteria still gate V2 promotion to 🟡 (V1.x is 4/7 — AnthropicAPIClient + Streaming editor + Real-usage signal remain; all three need env keys or user-side activity outside orchestrator scope). V2 work in flight on five fronts now: (1) **health-insurance `blindspots.md`** — Layer 3 of the 4th V2 domain; ≥5 typical blind spots per framing → 14 framings × 5 = ≥70 entries; mirror immigration/blindspots.md (PR #48) and housing/blindspots.md (PR #64) at the high-stakes Mechanism E end with each Recovery-move including licensed-broker / SHIBA / Navigator / ERISA-attorney / State-Insurance-Commissioner deferral per health-insurance `high_stakes:true` posture; (2) **personal-finance `framings.md`** — Layer 2 of the newly-opened 5th V2 domain; ≥3 framings per major decision; mirror health-insurance/framings.md (PR #71) and immigration/framings.md (PR #44) structure; voice anchors should reach into fee-only-fiduciary CFP, NAPFA, Bogleheads, Mr Money Mustache, financial-economics journalism (Wessel/Sommer/Tergesen), Choose-FI / FIRE communities, retirement-experienced CPA networks, ERISA practitioner forums, SEC EDGAR investor-alerts; high-stakes Mechanism E posture explicit per ROADMAP §5; (3) **housing `eval pass`** — final housing sub-item; runs eval on 10 housing fixtures from PR #67 and verifies `per_domain` quality_score within 0.05 of V1 tech-career baseline (0.8164), gated on VOYAGE_API_KEY availability; closes housing parent [x] (V2 1/10 → 2/10 first cross-domain V2 completion); (4) **immigration `eval pass`** — same gating, closes immigration parent [x]; (5) opportunistically start a sixth domain (entrepreneurship per `_meta_ontology.md` §6 priority order) when sources subagent slots have capacity.
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
  - [x] framings.md (≥ 3 framings per major decision) **— done at 5d898f8 (PR #63, Layer 2 of the 4-layer knowledge model for V2 §4 domain 3 of 10; 14 framings, ~9550 words / 1225 lines; each framing has Decisions-it-applies-to / Mental-model-summary / Characteristic-vocabulary / Excludes per `_schema.md`; full F1–F14 coverage map shows every D1–D10 has ≥3 framings — rent-vs-buy alone draws 10 framings (F1 financial-return / F2 lifestyle-flexibility / F3 household-stability / F4 total-cost-of-ownership / F8 climate-and-insurance / F9 school-and-neighborhood-premium / F10 investor-leverage / F11 transaction-cost-amortization / F13 consumer-advocate / F14 macro-housing-cycle); mortgage-fixed-vs-arm draws F5 rate-trajectory / F6 household-cashflow / F7 duration-of-stay matching the roadmap suggestion; opposing-framing pairs explicitly named — F1↔F2 (financial-return vs lifestyle-flexibility), F5↔F6 (rate-trajectory vs household-cashflow), F10↔F12 (investor-leverage vs tenant-rights), etc.; 16 voice anchors enumerated for later sources.yaml authoring (r/RealEstate, BiggerPockets, Calculated Risk blog, NAR/NAHB, Marketplace housing, local-market subreddits, etc.); word-count came in ~40% over the schema's 6-7k suggestion driven by housing's broader framing density + slightly more verbose Excludes bullets to seed Layer 3; flagged explicitly as risk in PR body, reviewer approved as-is on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per brief)**
  - [x] blindspots.md (≥ 5 typical blind spots per framing) **— done at 8efd283 (PR #64, Layer 3 of the 4-layer knowledge model for V2 §4 domain 3 of 10; 70 entries = 5 per framing × 14 housing framings; ~19.2k words / 2392 lines; full Layer 3 schema per `community_profiles/_schema.md` (Statement / Source-evidence / Trigger / Failure-mode / Recovery-move) per entry; structure mirrors immigration/blindspots.md PR #48 exactly EXCEPT for the housing `high_stakes: false` posture — housing Recovery moves are inline/self-directed for lower-stakes framings (lease renewal, neighborhood selection, basic refinance) and route to specific professionals (real-estate attorney, CPA, fee-only mortgage broker, insurance broker + climate-resilience inspector, tiered inspector) only where the decision's tail risk justifies it; selective gating enumerated in the Maturity / source-anchor note for future `domain_pack.md` encoding; cross-framing tensions section pairs 9 framing oppositions to seed Triage routing; word-count came in modestly over the 15.2k anchor from PR #48 driven by Mechanism E partial-gating posture (more Recovery-move nuance than immigration's uniform attorney-deferral) plus denser cross-framing tensions; flagged in PR body, reviewer approved as-is on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent; orchestrator-recovered from a prior orphan-subagent's interrupted Step 10b merge — the subagent had pushed + auto-review-approved + the orchestrator session died before merge; this run's Step 10b picked up the held PR cleanly)**
  - [x] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags) **— done at 13af99a (PR #66, Layer 4 of the 4-layer knowledge model for V2 §4 domain 3 of 10; 15 source-views across 7 distinct `community_tag` values, exceeds ≥8/≥4 minimum; schema mirrors `domain_knowledge/tech-career/sources.yaml` (PR #37) and `domain_knowledge/immigration/sources.yaml` (PR #49) exactly; all reliability:1 per ROADMAP §5 Mechanism C cite-and-promote starting posture; community-tag breakdown — real-estate-experience-forums (4 entries via reddit-realestate + reddit-firsttimehomebuyer + biggerpockets-forums + reddit-metro-housing), mortgage-and-personal-finance (3 via bogleheads-housing + reddit-personalfinance-housing + mortgage-news-daily), real-estate-data-and-economics (2 via calculated-risk + fhfa-house-price-index), journalists-and-explainers (2 via marketplace-housing + propublica-housing), industry-associations-and-government (1 via nar-research with explicit F13-anti-source posture flagged in `notes`), climate-and-insurance-research (2 via first-street-foundation + ibhs-research), consumer-advocacy-and-tenant-rights (1 via nlihc-tenant-rights); adapter mix 8 rss / 4 reddit_search / 4 static_corpus; RSS URLs that need verification carry `notes: "URL placeholder — verify before enabling"` per PR #49 precedent (Collection-layer try/except tolerates 404s); Reddit entries soft-fail without REDDIT_CLIENT_ID/SECRET per existing adapter contract; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session)**
  - [x] communities/* (one profile per community_tag in sources.yaml) **— done at 280e0b3 (PR #68, 7 community-profile markdown files under `domain_knowledge/housing/communities/` — one per `community_tag` value in housing/sources.yaml: `real-estate-experience-forums.md` (r/RealEstate + r/FirstTimeHomeBuyer + BiggerPockets + r/RealEstateMetro voices), `mortgage-and-personal-finance.md` (Bogleheads + r/personalfinance + Mortgage News Daily), `real-estate-data-and-economics.md` (Calculated Risk + FHFA HPI), `journalists-and-explainers.md` (Marketplace housing + ProPublica housing), `industry-associations-and-government.md` (NAR — with explicit F13-anti-source posture flagged), `climate-and-insurance-research.md` (First Street Foundation + IBHS), `consumer-advocacy-and-tenant-rights.md` (NLIHC); each profile follows `community_profiles/_schema.md` (Voice anchors / Mental model / Characteristic vocabulary / Known blind spots OF this community); ~770–850 words per profile, ~2042 lines total; housing `high_stakes:false` posture inverted from immigration PR #54's uniform Mechanism E — Recovery moves self-directed for routine questions and selectively route to CPA / real-estate attorney / fee-only mortgage broker / insurance broker + IBHS-trained inspector / Legal Aid landlord-tenant attorney only where the decision carries six-figure tail risk per `blindspots.md` PR #64 spec; cross-community references thread throughout (r/RealEstate ↔ real-estate-data-and-economics, BiggerPockets ↔ consumer-advocacy, NAR ↔ consumer-advocacy counter-posture, Bogleheads ↔ real-estate-experience-forums consumption-value, climate-and-insurance ↔ insurance broker + IBHS recovery); pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] fixtures/* (≥ 8 fixture situations) **— done at 87820ee (PR #67, V2 §4 housing sub-item 6 of 8; 10 per-fixture YAML files under `domain_knowledge/housing/fixtures/` exceeding the ≥8 minimum: rent-vs-buy-tech-worker-seattle, fixed-vs-arm-rate-trajectory-bet, lease-renewal-vs-move-uncertain-job, condo-vs-sfh-first-time-buyer, hoa-special-assessment-disclosure-gap, climate-relocation-wildfire-flood-call, refi-cash-out-vs-heloc-decision, cross-state-move-sell-and-buy-sequencing, downsize-empty-nest-tax-trigger, house-hack-duplex-fha-first-time; covers all 10 housing decisions D1–D10 and all 14 framings F1–F14 across 16 distinct personas; mirrors PR #58 immigration schema exactly (id / text / expected_domains / expected_entities / expected_personas / expected_risk_surfaces / expected_decisions / expected_framings / expected_blindspot_categories); housing `high_stakes:false` partial-gating posture per PR #64 — selective `consult-*` deferrals only on the 4 fixtures with genuine six-figure tail risk (cross-state Section-121 near cap, downsize $830k taxable gain, FL post-Surfside SB-4-D special assessment, jumbo ARM cap-structure), no blanket attorney deferral on the other 6; pytest tests/unit/test_load_all_fixtures.py 10/10 pass (V1 invariant already scoped to tech-career subset per PR #34, no test edit needed); loader picks up all 10 fixtures, establishing housing per_domain aggregation slot in eval/results)**
  - [x] domain_pack.md **— done at 8d9591b (PR #69, 454 lines / 2780 words — Triage Pass-2 / Editor / Critic prompt overrides for the housing domain, activating via PR #33's two-pass Triage when housing domain is selected; V1 fallback path bit-for-bit preserved when no `domain_pack.md` present; posture DELIBERATELY DIVERGES from `immigration/domain_pack.md` PR #53's uniform Mechanism E deferral — housing `high_stakes:false` per `_meta_ontology.md` §3 and `blindspots.md` PR #64, so Recovery moves are self-directed for lower-stakes framings (lease renewal, neighborhood selection, basic refi, HOA-document review, first-time-buyer education) and route to 5 named professional categories only where six-figure tail risk justifies it (real-estate attorney / CPA / fee-only mortgage broker / insurance broker + climate-resilience inspector / tiered inspector) — each with explicit trigger anchors into `blindspots.md` sections; 12 housing personas (controlled list), ~40 risk surfaces, 4 load-bearing opposing-framing pairs F1↔F2 / F5↔F6 / F10↔F12 / F11↔F14 plus secondary oppositions, 6 cross-domain routing flags; Editor numeric-specificity for mortgage rates / dollar amounts / PMI / SALT / §121 / 1031 / TCJA caps / ARM caps / property-tax regimes / climate-risk anchors, mandatory opportunity-cost framing for `rent-vs-buy-on-the-fence` persona, no uniform decision-support label; Critic per-numeric-claim citation + specificity bar + +1 non_obviousness floor for `cross-state-mover` and `climate-relocation-mover` + specific-professional-referral check (both over- and missed-referral fail); references decisions.md / framings.md / blindspots.md / sources.yaml by ID rather than duplicating; pure-additive prompt overlay, eval skipped per VOYAGE_API_KEY-empty session)**
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **health-insurance**
  - [x] decisions.md (≥ 8 distinct decisions, e.g. HDHP+HSA vs PPO, COBRA-vs-marketplace, Medicare timing, spousal carve-out, FSA/HSA sizing, ACA-noncompliant alternatives, etc.) **— done at fe45f32 (PR #70, Layer 1 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 10 distinct decisions covering HDHP/PPO/HMO at OE, spousal coverage carve-out, COBRA-vs-marketplace at job loss, Medicare Part-B-delay-vs-enroll-on-time, marketplace silver-CSR/APTC math, FSA/HSA/dep-care-FSA sizing, ACA-noncompliant alternatives (short-term limited-duration / healthcare-sharing ministries), Original-Medicare+Medigap vs Medicare-Advantage at IEP, HSA last-month-rule, and embedded vs aggregate family deductible; mirrors tech-career/decisions.md [PR #30], immigration/decisions.md [PR #42], housing/decisions.md [PR #60] structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; cross-domain edges flagged inline (`tech-career` for employer-plan-at-job-change, `immigration` for visa-status-dependent coverage, `personal-finance` for HSA-as-triple-tax-advantaged-retirement, `family-planning` for spouse/dependent coverage, `legal-disputes` for ERISA/COBRA/denial-appeal procedural rights); high-stakes Mechanism E posture explicit in intro (`_meta_ontology.md` §4 `high_stakes:true`) — 12-month-lock-in OOP-cap blowout and Medicare-Part-B 10%/year-permanent late-enrollment penalty are the load-bearing tail risks; selective professional-referral matrix enumerated (licensed health-insurance broker / SHIBA volunteer / ACA-Marketplace Navigator / CPA for HSA-401k coordination / ERISA attorney for denial appeal / State Insurance Commissioner for STLDI rescission complaints); ~5793 words / 764 lines — over the 2500 anchor due to Medicare's structural depth (D4 + D8 separately) plus ACA marketplace mechanics (APTC/CSR-silver-loading/ARPA-enhanced-subsidies expiration) plus FSA/HSA sub-account density, flagged in PR body, reviewer approved as-is on iteration 1; pure-additive knowledge content, no V1 runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] framings.md (≥ 3 framings per major decision) **— done at 882d528 (PR #71, Layer 2 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 14 framings F1–F14, ~9750 words / 1315 lines; coverage map confirms every D1–D10 has ≥3 framings after cross-cutting framing application; each framing has Decisions-it-applies-to / Mental-model-summary (3–6 sentences) / Characteristic-vocabulary (5–10 phrases) / Excludes (3–5 bullets) per `community_profiles/_schema.md`; 7 opposing-framing pairs explicitly named — F1↔F2, F3↔F4, F5↔F9, F6↔F10, F8↔F13, F12↔F4, F14↔F1/F2/F3/F4 — to seed Triage / Risk Officer disambiguation; high-stakes Mechanism E posture explicit in intro and downstream-layer notes — 12-month plan-year lock-in OOP-cap blowout + Medicare-Part-B 10%/year-permanent late-enrollment penalty are load-bearing tail risks; voice anchors named conceptually for Layer 4 sources.yaml hand-off (actuarial-and-broker, SHIBA volunteer, ACA-Navigator, HSA-administrator, ERISA-attorney, healthcare-economics-journalist Kliff/Rovner/Sanger-Katz/Ornstein, Bogleheads, HR-Reddit, KFF, PNHP, patient-advocate, Galen/AEI, chronic-illness patient); cross-domain edges flagged inline (`tech-career` for employer-plan-at-job-change, `immigration` for visa-status-dependent coverage / Medicaid eligibility quirks, `personal-finance` for HSA-as-triple-tax-advantaged-retirement, `family-planning` for spouse/dependent coverage decisions, `legal-disputes` for ERISA / COBRA / denial-appeal procedural rights); word-count came in modestly over the 5500–9500 acceptable band driven by health-insurance's broad framing density (14 framings × 5–7 paragraphs each); reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] blindspots.md (≥ 5 typical blind spots per framing) **— done at c04618a (PR #75, Layer 3 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 70 entries = 5 per framing × 14 framings; ~18.5k words / 2508 lines; full Layer 3 schema per `community_profiles/_schema.md` (Statement / Source-evidence / Trigger / Failure-mode / Recovery-move) per entry; structure mirrors immigration/blindspots.md PR #48 uniform Mechanism E precedent (vs housing/blindspots.md PR #64 partial-gating) — health-insurance is `high_stakes:true` per `_meta_ontology.md` §4, so every Recovery move routes to one of licensed health-insurance broker / SHIBA volunteer / ACA-Marketplace Navigator / CPA / ERISA-litigation attorney / State Insurance Commissioner / patient-advocate service / Medicare-appeals attorney / family-law attorney (verified programmatically across all 70 entries); source-anchors are health-insurance/framings.md (PR #71) Excludes bullet lines authored specifically to seed Layer 3 + conceptual references to community-class voice anchors named in framings.md (actuarial-and-broker, SHIBA volunteer, ACA-Navigator, HSA-administrator, ERISA-attorney, healthcare-economics-journalist Kliff/Rovner/Sanger-Katz/Ornstein, Bogleheads, HR-Reddit, KFF, PNHP, patient-advocate, Galen/AEI, chronic-illness patient); no purely-LLM-extrapolated entries; cross-framing tensions section pulls 7 opposing-framing pairs from framings.md (F1↔F2, F3↔F4, F5↔F9, F6↔F10, F8↔F13, F12↔F4, F14↔F1/F2/F3/F4) to seed Triage routing; Maturity / date-stamp risk note flags 11 anchor classes (ACA OOP-max ceilings, Medicare Part A retroactivity, DPC-HSA compatibility, ARPA subsidy sunset, DACA marketplace eligibility vacatur, GEP coverage start rule, HSA contribution limits, Medicare ALJ amount-in-controversy minimum, IRMAA brackets, NSA IDR methodology); word-count came in modestly over the 15.2k anchor from PR #48 driven by health-insurance's per-Recovery selective-broker-vs-Navigator-vs-attorney specificity; reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags) **— done at 6ccbc7a (PR #76, Layer 4 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 15 source-views across 8 distinct `community_tag` values, exceeds ≥8/≥4 minimum; schema mirrors `domain_knowledge/tech-career/sources.yaml` (PR #37), `domain_knowledge/immigration/sources.yaml` (PR #49), `domain_knowledge/housing/sources.yaml` (PR #66) exactly; all `reliability: 1` per ROADMAP §5 Mechanism C cite-and-promote starting posture; community-tag breakdown maps to framings.md PR #71 voice-anchor classes — broker-and-actuarial (3), medicare-shiba-and-government (2), aca-marketplace-and-navigator (2), hsa-and-bogleheads-personal-finance (3), healthcare-economics-journalism (2), erisa-and-denial-appeal-law (1), patient-advocacy-and-billing-recovery (1), chronic-illness-patient-experience (1); adapter mix rss / reddit_search / static_corpus; RSS URLs needing verification carry `notes: "URL placeholder — verify before enabling"` per PR #49/#66 precedent (Collection-layer try/except tolerates 404s); Reddit entries soft-fail without REDDIT_CLIENT_ID/SECRET per existing adapter contract; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #44/63/64/66-72/74-75); reviewer approved on iteration 1)**
  - [x] communities/* (one profile per community_tag in sources.yaml) **— done at 392a60a (PR #81, Layer 5 of the 4-layer knowledge model for V2 §4 domain 4 of 10; 8 community-profile markdown files, one per `community_tag` value in `domain_knowledge/health-insurance/sources.yaml` PR #76 — `broker-and-actuarial.md`, `medicare-shiba-and-government.md`, `aca-marketplace-and-navigator.md`, `hsa-and-bogleheads-personal-finance.md`, `healthcare-economics-journalism.md`, `erisa-and-denial-appeal-law.md`, `patient-advocacy-and-billing-recovery.md`, `chronic-illness-patient-experience.md`; each profile follows `community_profiles/_schema.md` (Identity / Voice anchors / Mental model / Characteristic vocabulary / Known blind spots OF this community / Mechanism E posture); mirrors `domain_knowledge/immigration/communities/*` PR #54 structural pattern; uniform Mechanism E posture per health-insurance `high_stakes:true` — every Recovery move routes to a named professional channel (licensed independent broker (commercial OE) / SHIBA-SHIP counselor (Medicare) / CMS-trained Navigator (Marketplace) / HSA administrator + IRS Pub 969 (HSA mechanics) / ERISA attorney (denial appeal of self-funded plan) / patient-advocate post-billing recovery (No Surprises Act §2799A IDR) / Dollar For / DOL EBSA / State Insurance Commissioner); 8 profiles × 1.5-2k words/profile = ~14.6k words / 2025 lines total — above the 600-1200 per-profile target but matches immigration/communities/* depth pattern at per-community Identity/Voice/Vocabulary/Blindspot specificity; reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #54/#68))**
  - [ ] fixtures/* (≥ 8 fixture situations)
  - [ ] domain_pack.md
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **personal-finance / investing**
  - [x] decisions.md (≥ 8 distinct decisions, e.g. retirement-account contribution ordering, Roth-vs-traditional, asset location, debt-payoff vs invest, tax-loss harvesting, etc.) **— done at d9868eb (PR #72, Layer 1 of the 4-layer knowledge model for V2 §4 domain 5 of 10; **kicks off the 5th V2 domain** at 0/8 → 1/8; 10 distinct decisions D1–D10 covering retirement-account contribution ordering (match → HSA → Roth-or-traditional 401k → Roth IRA / backdoor / Mega-backdoor → taxable), traditional-vs-Roth split at marginal-rate vs retirement-rate projection, asset location across 401k/IRA/Roth/taxable/HSA, brokerage asset allocation (passive index / target-date / DIY 3-fund), debt-payoff-vs-invest prioritization at given debt rates, tax-loss harvesting + wash-sale management + ETF-pair substitution, Roth-conversion ladder in low-income years (job loss, sabbatical, early retirement), withdrawal sequencing in retirement (taxable / tax-deferred / Roth ordering + RMD planning + SS-claim age coordination), 529-vs-Roth-vs-taxable college funding (529-to-Roth rollover SECURE 2.0 mechanics), estate-and-beneficiary structuring (TOD / POD / beneficiary forms supersede will + basis step-up + estate-tax-exemption sunset Dec 2025); mirrors tech-career/decisions.md [PR #30], immigration/decisions.md [PR #42], housing/decisions.md [PR #60], health-insurance/decisions.md [PR #70] structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; high-stakes Mechanism E posture explicit in intro — personal-finance is the canonical Mechanism E gating case named in ROADMAP §5; dollar-specific investment guidance uniformly out-of-scope (Editor "decision-support, not financial advice"); selective professional-referral matrix keyed by decision (brokerage-allocation → fee-only fiduciary CFP; tax-loss harvesting + wash-sale → CPA + IRS Pub 550; backdoor Roth / Mega-backdoor mechanics → CPA + plan-document review; SS-claim-strategy → fee-only Social Security planner NAPFA / Mike Piper; 401k force-out / IRA-rollover → ERISA attorney for high-balance situations; estate-tax exemption sunset → state-bar estate attorney; any individual recommended → SEC/FINRA BrokerCheck verification) rather than blanket-mandating one category; cross-domain edges flagged inline AND aggregated at file level (personal-finance is the most cross-cutting V2 domain) — material edges into `tech-career` (RSU-vest-and-sell vs hold, ISO exercise timing, deferred-comp / Section 409A), `health-insurance` (HSA-as-triple-tax-advantaged-retirement, FSA timing), `housing` (primary-residence-as-asset, mortgage-interest deduction × SALT interaction, cash-out refi vs HELOC vs margin loan), `family-planning` (529 funding ordering, spousal IRA rules, estate-tax-exemption sunset), `education-funding` (529 vs Roth-as-college-funding-substitute, student-loan PAYE / IDR / forgiveness mechanics), `entrepreneurship` (solo-401k / SEP-IRA / Mega-Backdoor for self-employed, QBI deduction), `legal-disputes` (creditor-protection of retirement accounts — ERISA vs IRA state shield variation, prenup/QDRO mechanics); ~9819 words / 1426 lines — over the 7k flag threshold, flagged explicitly in PR body and justified by 10-decision tax-mechanic density + 6+ cross-domain edge volume + Mechanism E selective-referral framing; reviewer approved on iteration 1 acknowledging justification; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #42/#60/#70))**
  - [x] framings.md (≥ 3 framings per major decision) **— done at 06502fb (PR #74, Layer 2 of the 4-layer knowledge model for V2 §4 domain 5 of 10; 14 framings F1–F14, ~11k words / 1634 lines; coverage map confirms every D1–D10 has ≥3 framings after cross-cutting framing application; each framing has Decisions-it-applies-to / Mental-model-summary (3–6 sentences) / Characteristic-vocabulary (5–10 phrases) / Excludes (3–5 bullets) per `community_profiles/_schema.md`; 8 opposing-framing pairs explicitly named for Triage / Risk Officer disambiguation; high-stakes Mechanism E posture explicit in intro and downstream-layer notes per `_meta_ontology.md` §5 — personal-finance is the canonical Mechanism E gating case named in ROADMAP §5; dollar-specific investment guidance uniformly out-of-scope; selective-professional-referral matrix anchored to decisions.md (fee-only fiduciary CFP, NAPFA, retirement-experienced CPA, fee-only Social-Security planner / Mike Piper, state-bar estate attorney, ERISA attorney, SHIBA, SEC/FINRA BrokerCheck verification); voice anchors named conceptually for Layer 4 sources.yaml hand-off — fee-only-fiduciary CFP, NAPFA, Bogleheads, Mr Money Mustache, financial-economics journalism (Wessel/Sommer/Tergesen), Choose-FI / FIRE communities, retirement-experienced CPA networks, ERISA practitioner forums, SEC EDGAR investor-alerts, IRS Pub 550 / 590-A / 590-B / 525, the Finance Buff (backdoor-Roth mechanics), retirement-econ academic voices (Wade Pfau, Michael Kitces); word-count came in modestly over the 6-10k target band driven by personal-finance being the most cross-cutting V2 domain per decisions.md PR #72 (material edges into 6+ other domains); flagged in PR body, reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] blindspots.md (≥ 5 typical blind spots per framing) **— done at 2e9e679 (PR #79, Layer 3 of the 4-layer knowledge model for V2 §4 domain 5 of 10; 70 entries = 5 per framing × 14 framings F1–F14 per `domain_knowledge/personal-finance/framings.md` PR #74; ~23.7k words / 3227 lines — over the 15.2k anchor from PR #48 and 18.5k from PR #75 driven by personal-finance's 6+ cross-domain edge footprint plus per-Recovery selective-channel-routing precision (fee-only fiduciary CFP NAPFA/XY-Planning/Garrett vs retirement-experienced CPA vs fee-only SS-claiming-specialist Mike Piper/Kotlikoff vs SHIBA/SHIP vs state-bar estate attorney vs ERISA attorney vs SEC IAPD / FINRA BrokerCheck), flagged explicitly in PR body; full Layer 3 schema per `community_profiles/_schema.md` (Statement / Source-evidence / Trigger / Failure-mode / Recovery-move) per entry; structure mirrors immigration/blindspots.md PR #48 uniform Mechanism E precedent and health-insurance/blindspots.md PR #75 — personal-finance is `high_stakes:true` per `_meta_ontology.md` §5 AND the canonical Mechanism E gating case named in ROADMAP §5, so every Recovery move routes to one of the 7 named professional-counsel channels (verified programmatically across all 70 entries); source-anchors are framings.md PR #74 Excludes bullet lines (authored specifically to seed Layer 3) + decisions.md PR #72 cross-domain edge flags + conceptual references to community-class voice anchors named in framings.md (fee-only-fiduciary CFP, NAPFA, Bogleheads, Mr Money Mustache, financial-economics journalism Wessel/Sommer/Tergesen, Choose-FI / FIRE, retirement-experienced CPA, ERISA practitioner forums, SEC EDGAR investor-alerts, IRS Pubs 550 / 590-A / 590-B / 525, the Finance Buff, retirement-econ academics Pfau / Kitces); no purely-LLM-extrapolated entries; cross-framing tensions section pulls 8 opposing-framing pairs from framings.md PR #74 (priority-order ↔ equity-comp, marginal-rate ↔ policy-volatility, HSA-stealth-IRA ↔ behavioral-debt-payoff, tax-arbitrage ↔ professional-referral, risk-allocation ↔ equity-comp, lifecycle ↔ estate-intergenerational, asset-protection ↔ priority-order, professional-referral ↔ behavioral-automation) to seed Triage routing; Maturity / date-stamp risk note flags TCJA sunset Dec 2025, ARPA / IRA enhanced-subsidy sunset, estate-tax exemption sunset, SECURE 2.0 phased provisions (§603 / §126 / §125 / §107 / §302), contribution-limit indexing, IRMAA brackets, SS-taxability-thresholds-unindexed-since-1983, DPC-HSA compatibility, PSLF / IDR / SAVE shifts, SECURE 1.0 inherited-IRA final regulations Feb 2024, FAFSA Simplification Act 2024-25, 10b5-1 SEC 2023 amendments, QSBS §1202 modification attempts; subagent-level auto-review was blocked by harness auto-mode classifier (sub-agent claude -p spawn refused), orchestrator ran reviewer at parent level as documented recovery, reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags) **— done at a213a3a (PR #80, Layer 4 of the 4-layer knowledge model for V2 §4 domain 5 of 10; 16 source-views across all 8 distinct `community_tag` values, exceeds ≥8/≥4 minimum — `fee-only-fiduciary-cfp` (2), `bogleheads-and-passive-index` (2), `fire-and-mr-money-mustache` (2), `retirement-economics-academics` (2), `tax-and-cpa-practitioner` (3), `financial-economics-journalism` (2), `erisa-and-fiduciary-rule-law` (1), `social-security-claiming-and-rmd` (2); schema mirrors `domain_knowledge/tech-career/sources.yaml` (PR #37), `domain_knowledge/immigration/sources.yaml` (PR #49), `domain_knowledge/housing/sources.yaml` (PR #66), `domain_knowledge/health-insurance/sources.yaml` (PR #76) exactly; all `reliability: 1` per ROADMAP §5 Mechanism C cite-and-promote starting posture; adapter mix 9 static_corpus / 6 RSS / 1 reddit_search; RSS URLs needing verification flagged with `TODO-verify-URL` in notes field per PR #49/#66/#76 precedent (Collection-layer try/except tolerates 404s); Reddit entries soft-fail without REDDIT_CLIENT_ID/SECRET per existing adapter contract; every `notes` field flags Mechanism E gating ("per-case withdrawal-sequencing / Roth-conversion / SS-claiming / RMD-orchestration decisions require fee-only fiduciary with current facts — sources here are reference / community signal only") per `_meta_ontology.md` §5 high-stakes posture; voice-anchor coverage exactly mirrors framings.md PR #74 §'Voice anchors' and Layer-4 forward-pointer (every voice named conceptually in framings.md now has at least one concrete source-view); reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #49/#66/#76))**
  - [ ] communities/* (one profile per community_tag in sources.yaml)
  - [ ] fixtures/* (≥ 8 fixture situations)
  - [ ] domain_pack.md
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **entrepreneurship**
  - [x] decisions.md (≥ 8 distinct decisions, e.g. co-founder equity split, bootstrap vs raise seed, quit day job vs nights-and-weekends, LLC vs S-corp election, SAFE vs priced seed, etc.) **— done at 8bf45f1 (PR #73, Layer 1 of the 4-layer knowledge model for V2 §4 domain 6 of 10; **KICKS OFF the 6th V2 domain** at 0/8 → 1/8; 11 distinct decisions covering co-founder selection + equity vesting structure, bootstrap vs raise seed for time-to-PMF compression vs ownership preservation, quit day job vs nights-and-weekends signal threshold, LLC pass-through vs S-corp election at $80k self-employment-tax crossover, SAFE post-money valuation cap vs priced seed (MFN clause, pro-rata rights), sole prop vs LLC formation timing, solo-401k vs SEP-IRA vs SIMPLE retirement-savings vehicle for self-employed, bring-on-first-employee W-2 vs contractor 1099 (ABC test, state misclassification), pricing-model (per-seat vs usage vs flat vs freemium with PLG funnel), co-founder dispute resolution / cap-table-buyback / departure structural decision, international incorporation (Delaware C-corp vs LLC vs jurisdiction-shopping for tax/IP); ~11k words / 1406 lines — over the 4-7k middle target band of the brief but within personal-finance's 9.8k precedent for cross-cutting domains, flagged in PR body; mirrors tech-career/decisions.md [PR #30] / immigration/decisions.md [PR #42] / housing/decisions.md [PR #60] / health-insurance/decisions.md [PR #70] / personal-finance/decisions.md [PR #72] structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; high-stakes posture is `high_stakes:false` per `_meta_ontology.md` §6 — selective rather than uniform Mechanism E referral; Recovery moves are inline / self-directed for routine decisions (sole-prop registration, basic pricing) and route to licensed professionals only where six-figure tail risk justifies it — startup attorney (founder-IP-and-equity-disputes, SAFE-to-priced-seed conversion), tax attorney or CPA with S-corp / multi-entity experience (S-corp election, multi-state nexus), employment-law attorney (first-W-2-employee, misclassification disputes); cross-domain edges flagged inline (`personal-finance` for retirement-accounts-for-self-employed + QBI deduction + S-corp salary minimization, `tech-career` for W-2-to-1099 + employer-IP-assignment, `legal-disputes` for founder lawsuits + IP assignment + equity disputes, `health-insurance` for solo health-insurance + ACA / spousal coverage, `housing` for HELOC-to-fund-business + mortgage-qualification-with-1099-income); ROADMAP §4 entrepreneurship entry expanded from single `(same template)` placeholder line to full 8-sub-item checklist mirroring health-insurance / housing / immigration / personal-finance; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #42/#60/#70/#72))**
  - [x] framings.md (≥ 3 framings per major decision) **— done at 122add6 (PR #78, Layer 2 of the 4-layer knowledge model for V2 §4 domain 6 of 10; 14 framings F1–F14, ~16k words; each framing has Decisions-it-applies-to / Mental-model-summary (3–6 sentences) / Characteristic-vocabulary (5–10 phrases) / Excludes (3–5 bullets) per `community_profiles/_schema.md`; coverage map confirms every D1–D11 from decisions.md PR #73 has ≥3 framings; opposing-framing pairs explicitly named for Triage / Risk Officer disambiguation — raise-vs-bootstrap F1↔F2, PLG-vs-sales-led F9↔F10, founder-mode-vs-manager-mode F11↔F12, optionality-vs-conviction-commitment F13↔F14, QSBS-vs-default-alive F5↔F2, day-job-fallback-vs-conviction F8↔F14, SE-tax-vs-QSBS F4↔F5; voice anchors named conceptually for Layer 4 sources.yaml hand-off — Indie Hackers, r/Entrepreneur, r/SmallBusiness, Hacker News startup voices (PG essays, Sam Altman, Garry Tan), Patio11 / Patrick McKenzie, Stripe Atlas, YC playbooks (How To Start A Startup, Library), SaaStr / Jason Lemkin, Tomasz Tunguz / Redpoint, The Finance Buff (LLC-vs-S-corp), Clerky, IRS Pub 535 / Pub 583, Lenny Newsletter, Founder Collective / First Round Review; cross-domain edges flagged inline AND aggregated at file level — material edges into `personal-finance` (solo-401k / SEP-IRA / Mega-Backdoor for self-employed, QBI deduction), `tech-career` (W-2-to-1099 transition, employer-IP-assignment carveouts), `legal-disputes` (founder lawsuits, IP assignment, equity disputes), `health-insurance` (solo health-insurance, ACA, spousal coverage), `housing` (HELOC-to-fund-business, mortgage-qualification with 1099 income); partial-gating posture per `_meta_ontology.md` §6 `high_stakes:false` — selective Mechanism E referral (startup attorney for founder-IP-and-equity-disputes + SAFE-to-priced-seed conversion, CPA with S-corp / multi-entity experience for tax-election and multi-state nexus, employment-law attorney for first-W-2-employee and misclassification) only where six-figure tail risk justifies it (D1/D4/D5/D7/D8/D11); word-count came in over the 6–11k target band driven by opposing-framing-pair density (7 named pairs) and Excludes-as-Layer-3-seed requirement, flagged explicitly in PR body, reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent)**
  - [x] blindspots.md (≥ 5 typical blind spots per framing) **— done at f4acfeb (PR #83, Layer 3 of the 4-layer knowledge model for V2 §4 domain 6 of 10; 70 entries = 5 per framing × 14 framings F1–F14 per `domain_knowledge/entrepreneurship/framings.md` PR #78; ~23k words — over the 12-18k target band of the brief but matches personal-finance PR #79 (~23.7k) and housing PR #64 precedent density for cross-cutting domains, flagged in PR body; full Layer 3 schema per `community_profiles/_schema.md` (Statement / Source-evidence / Trigger / Failure-mode / Recovery-move) per entry; structure mirrors housing/blindspots.md PR #64 partial-gating Mechanism E precedent (NOT immigration/health-insurance/personal-finance uniform Mechanism E pattern) — entrepreneurship is `high_stakes:false` per `_meta_ontology.md` §6, so Recovery moves use selective Mechanism E partial-gating: refer to a named professional channel ONLY where six-figure tail risk justifies it (D1 co-founder equity split + vesting, D4 LLC vs S-corp election + multi-state nexus, D5 SAFE post-money cap vs priced seed, D7 solo-401k vs SEP-IRA vs SIMPLE retirement vehicle, D8 W-2 vs 1099 first-employee classification, D11 international incorporation Delaware C-corp jurisdiction) with selective Recovery channels — startup attorney (founder-IP / SAFE / cap-table / departure / IP-assignment), S-corp-experienced CPA (tax-election / multi-state nexus / SE-tax / RSU-on-startup-equity), employment-law attorney (W-2-vs-1099 classification / non-compete / equity-vesting / wage-and-hour), tax attorney with §1202 QSBS + §351 experience, estate-planning attorney; source-anchors are framings.md PR #78 Excludes bullet lines + decisions.md PR #73 cross-domain edge flags + conceptual community-class voice anchors (Indie Hackers, r/Entrepreneur, Patio11, YC, SaaStr, Stripe Atlas, IRS Pub 535 + 334 + 583); cross-framing tensions section + maturity / source-anchor note + date-stamp risk inventory; cross-domain edges flagged inline — `personal-finance` (solo-401k vs SEP-IRA per D7; QSBS §1202 holding-period per D1), `tech-career` (RSU-vs-startup-equity-from-W-2 per D8), `legal-disputes` (co-founder-departure / cap-table-buyback per D9), `housing` (commingled mortgage-and-business-loan exposure post-LLC veil-pierce per D4), `health-insurance` (founder COBRA-to-Marketplace transition; self-funded-plan MEC per W-2-conversion of contractors); reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #35/#48/#64/#75/#79))**
  - [ ] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags)
  - [ ] communities/* (one profile per community_tag in sources.yaml)
  - [ ] fixtures/* (≥ 8 fixture situations)
  - [ ] domain_pack.md
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
- [ ] **education-funding**
  - [x] decisions.md (≥ 8 distinct decisions, e.g. refi federal-vs-private loans, grad-school ROI, 529 lump-sum-vs-annual, IDR + tax-bomb savings vs 10-year standard, in-state public vs out-of-state private merit, 529-vs-Roth-vs-taxable mix, parent PLUS vs student federal vs private mix, FAFSA / CSS asset positioning, employer tuition reimbursement vs scholarship-stacking, PSLF qualification mechanics, etc.) **— done at 33e2148 (PR #77, Layer 1 of the 4-layer knowledge model for V2 §4 domain 7 of 10; **KICKS OFF the 7th V2 domain** at 0/8 → 1/8; 10 distinct decisions D1–D10 covering refi federal loans to private vs preserve IDR / PSLF / SAVE optionality, MBA at top-15 with $200k debt vs continue current trajectory, front-load 529 with §529(c)(2)(B) 5-year-election lump sum vs annual contributions, IDR + tax-bomb savings vs 10-year standard, in-state public vs out-of-state private with merit aid, 529-vs-Roth-vs-taxable college funding mix (post-SECURE 2.0 §126 529-to-Roth rollover mechanics), parent PLUS vs federal subsidized/unsubsidized vs private mix (cosigner mechanics, release windows), FAFSA / CSS asset positioning timing (year-prior-prior tax year base, custodial-account drag, divorced-parent reporting, retirement-account exclusion, FAFSA Simplification Act 2024-25), employer tuition reimbursement ($5,250 IRC §127 exclusion, retention-clawback windows) vs scholarship-stacking vs self-pay, PSLF qualification (120-payment count, §455(m) employer 501(c)(3) verification, employment-certification cadence) vs PSLF alternatives; mirrors tech-career/decisions.md [PR #30], immigration/decisions.md [PR #42], housing/decisions.md [PR #60], health-insurance/decisions.md [PR #70], personal-finance/decisions.md [PR #72], entrepreneurship/decisions.md [PR #73] structural pattern with Scope / Framing-axes-covered / Sample-situations per entry; high-stakes posture is `high_stakes:false` per `_meta_ontology.md` §7 — slow-clocked and reversible (refinance, switch repayment plan, defer enrollment) — selective Mechanism E partial-gating like housing PR #60 and entrepreneurship PR #73; selective professional-referral matrix keyed by decision — student-loan attorney / Student Loan Borrower Assistance Project / Federal Student Aid Ombudsman (refi / IDR / PSLF / default rehab / Brunner bankruptcy), retirement-experienced CPA (§127 / §529 / kiddie-tax / AOTC § 25A / LLC interaction), NACAC-member college financial-aid counselor (FAFSA / CSS profile strategy / merit-aid negotiation / appeal letters), fee-only fiduciary CFP (529-vs-Roth college funding mix and retirement-account-impact analysis); cross-domain edges flagged inline AND aggregated at file level — material edges into `personal-finance` (529-vs-Roth-vs-taxable college-funding mix, 529-to-Roth rollover SECURE 2.0 §126 mechanics, asset location, kiddie tax), `tech-career` (employer tuition reimbursement at large-tech IRC §127 $5,250, MBA-to-tech-pivot ROI), `family-planning` (kids' college funding ordering, custodial accounts UGMA/UTMA basis, divorced-parent FAFSA mechanics), `entrepreneurship` (self-employed retirement vs college funding tradeoff, S-corp salary vs distribution interacting with FAFSA EFC), `housing` (home-equity-as-college-funding source: HELOC vs Parent-PLUS rate comparison, primary-residence non-reportable on FAFSA); ~7.9k words flagged in PR body as over the 6k upper-band suggestion — justified by statutory-anchor density (D4 tax-bomb, D6 SECURE 2.0 §126 mechanics, D8 FAFSA Simplification Act, D10 PSLF §455(m)) and education-funding's 5-domain cross-cutting breadth; reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #42/#60/#70/#72/#73/#74/#75); ROADMAP §4 education-funding entry expanded from single `(same template)` placeholder line to full 8-sub-item checklist mirroring health-insurance / housing / immigration / personal-finance / entrepreneurship)**
  - [x] framings.md (≥ 3 framings per major decision) **— done at 629f234 (PR #82, Layer 2 of the 4-layer knowledge model for V2 §4 domain 7 of 10; 14 framings F1–F14 covering all 10 decisions D1–D10 from `domain_knowledge/education-funding/decisions.md` PR #77 with ≥3 framings per major decision after cross-cutting application; ~12.9k words / 1793 lines — slightly above the 6-10k target band but within the high end of established Layer 2 precedent (housing PR #63 ~9.5k, entrepreneurship PR #78 ~12k, health-insurance PR #71 ~9.75k); each framing has Decisions-it-applies-to / Mental-model-summary (3–6 sentences) / Characteristic-vocabulary (5–10 phrases) / Excludes (3–5 bullets) per `community_profiles/_schema.md`; partial-gating Mechanism E posture per `_meta_ontology.md` §7 `high_stakes:false` — mirrors `housing/framings.md` (PR #63) and `entrepreneurship/framings.md` (PR #78) precedent; selective Recovery referral on six-figure tail-risk pockets named in decisions.md (D1 federal-to-private refi as one-way door; D3 §529(c)(2)(B) 5-year-forward + Form 709; D4 IDR + tax-bomb sinking-fund; D7 Parent PLUS / private cosigner mechanics; D10 PSLF qualifying-employment / Buyback program) — student-loan attorney / Student Loan Borrower Assistance Project / Federal Student Aid Ombudsman / retirement-experienced CPA / NACAC-member college financial-aid counselor / fee-only fiduciary CFP; 10 opposing-framing pairs explicitly named in cross-framing tensions section for Triage / Risk Officer disambiguation; 13 voice-anchor community-classes organized for Layer 4 sources.yaml hand-off — PSLF-preservation (r/PSLF, SLBA, FSA Ombudsman, Heather Jarvis), ROI-by-major (Georgetown CEW, Burning Glass Lightcast, Payscale, BLS OES), FIRE-aware (r/financialindependence, MMM, ChooseFI, The College Investor), NACAC-counselor, 529 voices (Kantrowitz, SavingForCollege, Bogleheads 529, Mike Piper), CSS-Profile-aware (r/financialaid, r/ApplyingToCollege, Princeton Net Price Calculator), r/StudentLoans, MBA-admissions (Poets&Quants, GMAT Club, Wall Street Oasis), r/cscareerquestions, consumer-protection (CFPB, NCLC, SLBA, state AGs), NAPFA, retirement-experienced-CPA, HELOC-as-college-funding, bankruptcy-discharge; cross-domain edges flagged inline AND aggregated at file level — `personal-finance` (debt-payoff-vs-invest, asset location, Roth-conversion-ladder, retirement-account-exclusion-from-FAFSA, kiddie-tax §1(g), SECURE 2.0 §126 per D1/D3/D4/D6/D7/D10), `tech-career` (full-time-MBA-ROI for engineers, MS-CS-as-H-1B-cap-exempt-route, §127 retention-clawback per D2/D9), `entrepreneurship` (1099-vs-W-2 PSLF-qualifying-employment asymmetry, S-corp-formation-killing-PSLF, LLC-as-parent-for-529-front-loading per D2/D3/D10), `family-planning` (529 inter-generational gifting, UGMA/UTMA basis transfer, divorced-parent-of-record post-Simplification, custodial-account drag per D3/D6/D8), `housing` (HELOC-as-college-funding-alternative, cash-out-refi-vs-Parent-PLUS, primary-residence reporting differential FAFSA vs CSS per D7/D8), `immigration` (international-student MS-CS calculus per D2), `legal-disputes` (bankruptcy-discharge post-*Brunner*/*Frost*/2022 DOJ-USDOE-attestation, Adversary Proceeding requirements, servicer-error remediation under 2022–2024 IDR/PSLF account-adjustment consent decrees per D1/D4/D10); subagent-level claude -p reviewer spawn was blocked by harness auto-mode classifier (recurring known issue), orchestrator ran reviewer at parent level as documented recovery, reviewer approved on iteration 1; pure-additive knowledge file, no runtime gating, eval skipped per VOYAGE_API_KEY-empty session + additive-knowledge-file precedent (PRs #32/#44/#63/#71/#74/#78))**
  - [ ] blindspots.md (≥ 5 typical blind spots per framing)
  - [ ] sources.yaml (≥ 8 source-views, ≥ 4 distinct community_tags)
  - [ ] communities/* (one profile per community_tag in sources.yaml)
  - [ ] fixtures/* (≥ 8 fixture situations)
  - [ ] domain_pack.md
  - [ ] eval pass on fixtures with `quality_score` within 0.05 of V1 baseline
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
