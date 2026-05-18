# Blindspot Meta-Ontology — Life-Decision Domains

> **Scope-narrow note — 2026-05-18.** On 2026-05-18 the Blindspot
> project narrowed from a universal 10-domain blind-spot tool to a
> single in-scope vertical: **Chinese international students in the
> US, making SDE job-hunt and visa-coupled career decisions**
> (slug: `cn-sde-jobhunt`). The roadmap is in
> [`docs/specs/ROADMAP.md`](../docs/specs/ROADMAP.md). The previous
> 10-domain ontology is preserved in this file's git history; the
> deprecated content was either *archived* (no longer in scope) or
> *moved to legacy* (still referenced as upstream-source material for
> the in-scope vertical). The runtime now loads only
> `cn-sde-jobhunt`; the rest is documentation.

## Purpose

This file names the top-level taxonomy of life-decision domains the
Blindspot project covers. After 2026-05-18 it names **one** in-scope
vertical plus pointers to deferred / archived material. Each
in-scope entry below maps to a folder under `domain_knowledge/<slug>/`
holding the four knowledge layers (decisions, framings, blindspots,
sources) the runtime consumes. The authoring guide for those layers
is at [`_schema.md`](./_schema.md).

## The in-scope vertical: cn-sde-jobhunt

- **slug**: `cn-sde-jobhunt`
- **scope**: US-based SDE career decisions made by Chinese
  international students whose status — F-1, OPT, STEM-OPT, cap-gap,
  H-1B, H-4, O-1, or AOS-pending — is a binding constraint on the
  career move under consideration. The vertical lives at the
  **intersection** of two domains the V1 build invested in
  (`tech-career` and `immigration`); per-decision content is
  *only* in scope when both axes are live. Pure-tech-career
  decisions without visa-status pressure and pure-visa decisions
  without an SDE / employer choice are out of scope and Triage
  refuses them (see `cn-sde-jobhunt/domain_pack.md` §Triage).

  In-scope decision types include:
  - Offer comparison under H-1B-sponsorship-willingness filter
    (FAANG vs unicorn vs Series-B startup, GC-timeline implication
    of employer choice).
  - OPT / STEM-OPT / cap-gap timing decisions across job offers,
    school re-enrollment, and gap-year intent.
  - H-1B lottery strategy: multiple-registration mechanics, alternate
    paths if not selected (O-1, L-1 transfer, day-1-CPT risk, study
    back to F-1, day-1-OPT MS-pipeline).
  - Employer switch mid-PERM / mid-I-140 with AC21 §106(c)
    same-or-similar portability and §104(c) 3-year extension
    eligibility implications.
  - Layoff response under visa-status pressure: 60-day grace,
    severance-and-grace clock interaction, H-1B transfer timing,
    H-4/H-4-EAD effect on the spouse-and-children unit, downgrade-
    to-F-1 fallback, departure timing.
  - Return-to-China (海归) timing: when ROI of staying flips
    negative under GC backlog, family pressure, geopolitical
    posture, China-tech market and 35-and-over职场风险.
  - Family-located optimization: H-4 / H-4-EAD spouse strategy,
    kids' schooling and state-residency coupling, parent visiting
    visas (B-2) and 海外父母医疗 access.
  - PhD-to-industry / postdoc-to-industry conversion under both
    EB-1A / NIW self-petition routes and H-1B-with-employer
    sponsorship — coverage of when each route fits.
  - Long-term career capital vs short-term visa security tradeoff:
    a job that maximizes 10-year skill-trajectory may not maximize
    next-3-year status security, and vice versa.
  - O-1 vs H-1B lottery: when O-1's higher evidentiary bar trades
    off against H-1B's lower bar but cap-and-lottery exposure.
  - Post-cliff (post-RSU-vest) career strategy when GC timeline,
    employer-switch optimality, and family timing all couple.

- **maturity**: `in-construction` — folder is scaffolded but Layers
  1–3 are placeholder entries pending insider voice work. Runtime
  enables `cn-sde-jobhunt` for routing once Layer 1 is hand-authored.

- **high_stakes**: `true` — visa status lapses are irreversible
  (60-day grace, 6-year H-1B cap, multi-year reentry bars after
  unlawful presence). Mechanism E gating applies: Editor labels
  visa-decision output "decision-support, not legal advice" and
  routes to a named immigration-attorney channel for any actionable
  visa step. Critic's grounding threshold is raised to ≥ 90% on any
  claim about a visa timeline, statute, regulation, or named program.

- **sample decisions** (6, drawn from Layer 1 `decisions.md`):
  - Offer comparison: FAANG-A sponsors H-1B and starts PERM Year 2
    vs Series-B-B pays $30k more but won't commit to PERM until
    Year 4 — net 4-year-comp value under the visa-security adjustment.
  - First-time OPT employer choice under cap-gap risk: take a sure
    e-verified F-1-friendly employer that lottery-petitions next
    March, or hold out for FAANG that lottery-petitions but starts
    20 weeks later.
  - Laid off on H-1B Year 3, 4 weeks of severance, PERM filed but
    pre-audit, H-4 spouse without EAD: how to sequence 60-day grace
    clock, H-1B transfer search, and family-located decisions.
  - Return-to-China timing for a senior SDE on approved I-140 with
    EB-2 China backlog 8 years out: stay through the backlog vs
    return now while China-tech hiring is open vs hedge with a
    multi-year reduced-presence arrangement.
  - PhD-graduating SDE-pivot candidate: EB-1A / NIW self-petition
    while still on F-1 OPT vs H-1B-lottery with employer sponsorship
    vs O-1 bridge into industry vs return.
  - H-4-EAD spouse career strategy when principal's I-140 is approved
    and EAD is rule-vulnerable: how to time spouse's job change,
    employer commitment, and citizenship-of-children decisions.

## Deferred / legacy domains

The 2026-05-18 scope narrow split the V2 ontology into two
non-runtime piles:

### `domain_knowledge/_legacy/`

Domains the runtime **no longer routes to** but whose hand-authored
content is **still referenced as upstream source material** by the
in-scope vertical. The runtime reads these only via
`cn-sde-jobhunt/sources.yaml` `static_corpus` entries:

- `_legacy/tech-career/` — US knowledge-worker comp, equity, offer
  negotiation, perf, layoff response. `cn-sde-jobhunt` borrows its
  Layer 2 framings (offer-negotiation framings, comp-arithmetic
  framings) and Layer 3 blindspots (e.g. RSU-mark-to-market vesting
  math, IPO-cliff exit timing, perf-review post-layoff signaling)
  wherever those translate to a CN-student-with-visa-constraint
  asker. The CN-student-specific overlay is in
  `cn-sde-jobhunt/framings.md` and `cn-sde-jobhunt/blindspots.md`.
- `_legacy/immigration/` — US visa categories, status transitions,
  employer-sponsored vs self-petitioned paths, dependent visas.
  `cn-sde-jobhunt` borrows its Layer 1–3 visa-mechanic ground truth
  (AC21 §106(c) portability, CSPA aged-out formula, EB-1A Dhanasar
  three-prong) without re-authoring the statutory plumbing. The
  CN-student-specific overlay narrows scope to F-1 → OPT → H-1B →
  GC and the dependent (H-4 / H-4-EAD) couplings most-cited in
  one-acre-three-mu threads.

Both `_legacy/` folders are referenced from `cn-sde-jobhunt/sources.yaml`
as `static_corpus` adapter entries at reliability 4 — they meet the
V2 quality bar but are not CN-specific, so they get a one-notch
discount from a CN-community-cited source at the same source-tier.

### `domain_knowledge/_archive/`

Domains the runtime no longer routes to and which are **not** used
as upstream sources by `cn-sde-jobhunt`. They are preserved as
project history per ROADMAP §0:

- `_archive/housing/` — rent vs buy, mortgage selection, location
  choice.
- `_archive/health-insurance/` — open-enrollment plan choice, HSA /
  FSA, COBRA vs marketplace, Medicare timing.
- `_archive/personal-finance/` — retirement-account ordering,
  tax-advantaged account strategy, debt-payoff vs invest.
- `_archive/entrepreneurship/` — co-founder selection, fundraising
  vs bootstrapping, side-business / freelance structure.
- `_archive/education-funding/` — student-loan type and refi
  timing, grad-school ROI, 529 / Coverdell.

These remain readable for reviewers of the project's history but
the runtime does NOT load them and the refine routine does NOT
edit them.

## Cross-domain notes

`cn-sde-jobhunt` is the **intersection** of `tech-career` and
`immigration`, with **CN-student-specific community knowledge as
the moat**. The vertical is *not* the union — a question that is
purely tech-career (no visa pressure) or purely visa (no SDE
employer choice) is **out of scope** and the Triage Officer refuses
it. The defensible thesis is that the intersection has
under-represented community knowledge: 一亩三分地 (1point3acres)
threads, Zhihu 海归 career-decision narratives, WeChat blogs from
practicing immigration attorneys reading USCIS Policy Manual updates
in Chinese for a CN-applicant audience, and 海归 podcasts (硅谷101,
软实力) where returnees narrate the timing decision in retrospect.
General-purpose LLMs underrepresent these voices because they are
behind Chinese-language paywalls, hostile-to-scrape registration
walls, or WeChat-public-account silos.

The legacy folders are referenced (via `cn-sde-jobhunt/sources.yaml`)
as static-corpus inputs — they ground the visa-mechanic and
comp-mechanic claims while the CN-student-specific layers
(community profiles, blindspots oriented around 一亩三分地 framing,
return-to-China optionality) carry the moat.

## Out-of-scope / deferred

The scope narrow folded these categories of work out of the live
project:

- **All non-CN international-student verticals** (Indian-student
  SDE, European-student SDE, etc.). Same architecture would apply
  but the author lacks community knowledge.
- **Non-SDE CN-international-student verticals** (CN-student
  finance careers, CN-student academic / postdoc-stays-academic
  decisions). Different community knowledge; defer.
- **Mainland-China-to-China returnee decisions** that don't pass
  through a US-SDE-stay-or-leave moment. Out of scope.
- **Asylum, family-sponsored, EB-5, citizenship-by-investment,
  and removal-defense routes.** Out of scope; refer to counsel.
- The seven `_archive/` domains and any cross-domain
  frame-breaking work (V4 of the deprecated plan). Killed.

## Update policy

This file is editable by future refine runs:

- **Editing scope is allowed** — sharpen the `cn-sde-jobhunt`
  scope statement, add sample decisions, refine the high-stakes
  rationale.
- **Do NOT add a new in-scope vertical without explicit human
  review.** The scope narrow is deliberate; adding a vertical
  re-opens the deprecated work.
- **Do NOT remove the `_legacy/` or `_archive/` pointers.** They
  are referenced from `cn-sde-jobhunt/sources.yaml` and the
  ROADMAP §0 history.
- **Renames are also human-review.** A slug rename to
  `cn-sde-jobhunt` ripples through `cn-sde-jobhunt/sources.yaml`,
  `cn-sde-jobhunt/fixtures/*.yaml`, Triage pass-1 labels, and the
  refine-routine targeting. Slugs are load-bearing.
