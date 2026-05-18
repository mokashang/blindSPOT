# health-insurance — domain_pack.md

Triage / Editor / Critic prompt overrides scoped to the `health-insurance`
domain, per [`_schema.md` §`domain_pack.md`](../_schema.md). Triage's
pass-2 concatenates this file into its system prompt when this domain
is active. Editor and Critic use the corresponding sections when the
situation routes here.

`health-insurance` is `high_stakes: true` per
[`_meta_ontology.md` §4](../_meta_ontology.md). Mechanism E gating
(per [ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating))
applies in full, in the same **uniform** shape as
[`immigration/domain_pack.md`](../immigration/domain_pack.md) (PR #53)
— NOT the partial-gating posture of
[`housing/domain_pack.md`](../housing/domain_pack.md) (PR #69) or
[`tech-career/domain_pack.md`](../tech-career/domain_pack.md). Two
distinct classes of irrevocability drive the high-stakes posture (per
[`decisions.md`](./decisions.md) intro and
[`framings.md`](./framings.md) intro):

- **12-month plan-year lock-in** on commercial / marketplace plans.
  Outside an annual open enrollment window or a narrow Qualifying-
  Life-Event (QLE) window, the user cannot change plans, switch from
  PPO to HDHP, add/drop dependents, or pivot off marketplace coverage.
  A wrong choice compounds for up to a full plan year with potentially
  uncapped out-of-network exposure (the ACA OOP cap of $9,450 self /
  $18,900 family for 2026 applies only to in-network EHB-classified
  care).
- **Permanent Medicare-side penalties.** Missing the Part B Initial
  Enrollment Period (IEP) without creditable employer coverage
  triggers a 10%-of-Part-B-premium-per-12-months-late penalty that
  compounds and persists for life. Missing the Medigap Guaranteed-
  Issue (GI) 6-month window subjects the beneficiary to medical
  underwriting forever (denial, exclusion, or rate-up on common
  chronic conditions). These are not insurance decisions in the
  ordinary sense — they have a permanent-record character closer to
  immigration status decisions than to housing or tech-career.

The wrong call is not recoverable on a multi-year horizon: missed IEP
triggers lifetime Medicare premium loading; missed 60-day marketplace
SEP forecloses coverage until next open enrollment; post-claim STLDI
rescission converts a $200k cancer bill from "insured" to "uninsured"
retroactively; a self-funded ERISA plan's denial-and-exhaustion clock
that lapses without administrative-appeal documentation forecloses
federal §502(a) review forever.

Companion files: [`decisions.md`](./decisions.md) (D1–D10),
[`framings.md`](./framings.md) (F1–F14),
[`blindspots.md`](./blindspots.md),
[`sources.yaml`](./sources.yaml),
[`communities/*.md`](./communities/),
[`fixtures/*.yaml`](./fixtures/). Reference them; this file does not
restate their content.

---

## Triage

Pass-1 has already extracted generic `(domains, entities, risk_surfaces,
personas)` from [`src/blindspot/prompts/triage.md`](../../src/blindspot/prompts/triage.md).
Pass-2 with this domain active enriches that output with the domain-
specific facets below. The Pass-1 vocabulary stays the authoritative
ground set; Pass-2 adds and *sharpens*, never overwrites.

**Decision matching.** Identify the closest match from D1–D10 in
[`decisions.md`](./decisions.md) by the *Sample situations* under each
decision (those are written for this purpose). Emit it as
`matched_decision: "D<n>"`. Multiple-decision matches are common in
health-insurance — a 64-year-old considering an MA-vs-Medigap choice
while still on an employer HDHP-with-HSA typically spans D4 (Part B
delay vs enroll), D8 (Original Medicare + Medigap vs MA at IEP), and
D9 (HSA last-month-rule × Medicare interaction); a laid-off employee
with a deductible-met-by-November condition spans D3 (COBRA vs
marketplace), D5 (silver-CSR vs gold), and D10 (embedded vs aggregate
deductible-reset). Emit a list ordered by closeness. A genuinely
ambiguous situation between two decisions is a routing signal worth
surfacing; do NOT collapse it.

**Persona refinement.** Pass-1 may have emitted a generic persona like
`employee-at-open-enrollment` or `medicare-shopper`. Replace with the
most-specific persona from this controlled list when the situation
supports it:

- `healthy-single-at-oe` — no chronic conditions, employer HDHP-vs-
  PPO arithmetic dominated by HSA-as-retirement-vehicle calculus
  (D1; F1 / F3 framings)
- `family-tier-decider` — household with mixed-utilization,
  embedded-vs-aggregate deductible structure load-bearing (D1, D10;
  F1 / F11)
- `dual-employer-spouse-with-coverage-overlap` — both spouses with
  employer coverage, surcharge / carve-out / HSA-family-cap
  coordination (D2, D6; F7 / F11 / F12)
- `chronic-condition-on-specialty-drug` — household member on
  $400+/month specialty drug; formulary-tier + prior-auth +
  PA-supply-runway risks dominate (D1, D5, D8; F1 / F10 / F13)
- `recently-laid-off-with-deductible-met` — within 60-day COBRA /
  marketplace SEP clocks; YTD-OOP transfer arithmetic load-bearing
  (D3, D5, D10; F2 / F4 / F7)
- `recently-laid-off-healthy-no-deductible-met` — same SEP clocks
  but with the 60-day-decision + 45-day-payment-grace retroactive-
  election option as a real planning tool (D3; F2 / F7)
- `self-employed-marketplace-shopper` — non-employer, evaluating
  silver-CSR / gold / bronze with MAGI-projection (D5, D7; F4 / F5 /
  F12)
- `low-income-eligible-for-silver-csr` — MAGI 100–250% FPL, silver-
  CSR-94/87/73 actuarial-value strictly dominates gold (D5; F5)
- `aca-shopper-considering-stldi-or-sharing-ministry` — non-ACA
  alternative under evaluation; pre-existing-condition / OOP-cap-
  absence trap (D7; F2 / F9)
- `near-65-still-working-large-employer` — Part B delay under SEP-
  protection; ≥20-employee creditable-coverage test (D4; F6 / F8)
- `near-65-still-working-small-employer-under-20` — MSP rule flips
  primary/secondary at 65 regardless of enrollment; hard-enroll
  Part B even with HR pushback (D4; F6)
- `at-65-choosing-ma-vs-original-medigap` — IEP one-time Medigap GI
  window; state-specific GI rules (NY / CT / MA / ME annual; CA / OR
  birthday rule); MA-trial-right-12-month-return-to-Original (D8;
  F6 / F10)
- `medicare-advantage-trying-to-switch-back-to-medigap` — outside
  GI window; medical underwriting denial risk for chronic conditions
  (D8; F6 / F9)
- `mid-year-hdhp-hire-considering-last-month-rule` — 13-month
  testing-period commitment vs prorated-only-safe-floor (D9; F3 /
  F12)
- `dual-income-with-fsa-and-hsa-spouse-overlap-risk` — spouse's
  general-purpose FSA knocks out HSA-eligibility silently (D6, D9;
  F3 / F12)
- `mid-treatment-divorce-with-deductible-met` — divorce-QLE
  embedded-individual-OOP-met does NOT transfer to new plan; timing-
  vs-deductible-reset arithmetic (D10; F2 / F13)
- `daca-or-mixed-status-household-marketplace-eligible` — DACA
  vacatur post-2025 + mixed-status household FPL calculation (D5;
  F5; boundary `immigration`)
- `denied-claim-on-self-funded-employer-plan` — ERISA pre-emption +
  29 CFR §2560.503-1 procedural exhaustion + 180-day adverse-benefit-
  determination appeal deadline (D3, D8, D10; F8; boundary
  `legal-disputes`)
- `post-billing-balance-billing-recovery` — No Surprises Act §2799A
  IDR; surprise out-of-network anesthesia / pathology / air-
  ambulance; EOB-reading workload (D3, D10; F13)

These are the personas the per-domain blindspot triggers in
[`blindspots.md`](./blindspots.md) are written against. Generic
persona labels will miss most triggers.

**Risk-surface vocabulary.** Replace generic `health` / `cost` /
`insurance` / `coverage` from Pass-1 with the specific risk surfaces
below when the situation supports them. Each maps to one or more
blindspots in [`blindspots.md`](./blindspots.md); using the generic
label loses the routing:

- Plan-year lock-in / QLE clocks: `12-month-plan-year-lock-in`,
  `60-day-marketplace-SEP-from-loss-of-coverage`, `60-day-COBRA-
  election-window`, `45-day-COBRA-premium-payment-grace`,
  `30-day-employer-plan-QLE-window`, `90-day-FSA-claims-submission-
  deadline`, `documentation-pipeline-mismatch-with-SEP-window`
- ACA cost-sharing structure: `ACA-OOP-max-ceiling-self-and-family`
  ($9,450 / $18,900 for 2026, indexed), `embedded-individual-OOP-
  max-sub-limit-2016-ACA-rule` (≤ self-only OOP-max for the year),
  `aggregate-vs-embedded-family-deductible`, `out-of-network-OOP-
  max-absence-on-EPO-HMO`, `prescription-drug-OOP-track-separate-
  from-medical`, `EHB-coverage-vs-non-EHB-balance-billing-exposure`,
  `silver-CSR-94/87/73-actuarial-value-variant`,
  `benchmark-silver-APTC-keyed-to-second-cheapest-silver`,
  `family-glitch-fix-2022-IRS-rule`
- Medicare clocks / penalties: `Part-B-IEP-7-month-window-around-65`,
  `8-month-SEP-from-end-of-employment` (NOT end-of-COBRA),
  `Part-B-late-enrollment-penalty-10pct-per-12mo` (permanent),
  `Part-D-LEP-1pct-per-month-permanent`, `GEP-Jan-March-coverage-
  starts-July-3-9mo-gap`, `Medigap-GI-6-month-window-from-Part-B-
  effective-date`, `state-specific-Medigap-GI` (NY / CT / MA / ME
  annual; CA / OR birthday rule), `MA-to-Original-trial-right-12-
  month`, `MSP-rule-≥20-employees-creditable-coverage`,
  `creditable-Part-D-coverage-annual-employer-notice` (29 CFR
  §423.56), `Part-A-retroactive-up-to-6-months-on-SS-claim` (HSA-
  eligibility loss), `IRMAA-2-year-lookback-MAGI`
- HSA / FSA mechanics: `HSA-cap-self-and-family` ($4,300 / $8,550
  for 2026; $1,000 55+ catch-up), `last-month-rule-13-month-testing-
  period-recapture` (IRC §223(b)(8)), `spouse-general-purpose-FSA-
  voids-HSA-eligibility`, `limited-purpose-FSA-HSA-compatible-augment`,
  `dep-care-FSA-vs-Child-and-Dependent-Care-Tax-Credit-coordination`
  (Form 2441), `FSA-use-it-or-lose-it-vs-660-carryover-vs-2.5-month-
  grace-mutual-exclusion`, `HSA-Medicare-mutual-exclusion`
- ACA-noncompliant alternatives: `STLDI-4-month-initial-1-month-
  renewal-2024-rule`, `healthcare-sharing-ministry-shareable-
  expense-discretion`, `pre-existing-condition-exclusion-on-non-ACA`,
  `OOP-cap-absent-on-STLDI-and-sharing-ministry`, `EHB-coverage-
  gap-no-maternity-no-mental-health`, `post-claim-rescission-risk`,
  `religious-eligibility-and-lifestyle-attestation-as-share-
  contingency`, `farm-bureau-state-specific-exempt-coverage`
- ERISA / denial appeals: `self-funded-vs-fully-insured-SPD-test`,
  `ERISA-pre-emption-of-state-insurance-commissioner-remedies` (29
  USC §1144(a)), `29-CFR-2560.503-1-claims-and-appeals-procedure`,
  `180-day-adverse-benefit-determination-appeal-deadline`,
  `administrative-exhaustion-requirement-before-§502(a)`,
  `Firestone-deference-vs-de-novo-review`, `Medicare-Appeals-Council-
  ALJ-tier-1840-amount-in-controversy-2026`
- Network / prior-auth: `narrow-county-based-HMO-network`,
  `ghost-network-provider-directory-inaccuracy-30-50pct`,
  `MA-network-mid-year-drop-risk`, `prior-auth-required-on-most-MA-
  specialty-referrals`, `Original-Medicare-no-prior-auth-any-
  Medicare-accepting-provider`, `step-therapy-fail-first`,
  `formulary-mid-year-change-60-day-notice-non-protected-class`,
  `specialty-pharmacy-vs-buy-and-bill`, `center-of-excellence-COE-
  out-of-network-on-MA`
- Surprise / balance billing: `No-Surprises-Act-§2799A-IDR-
  arbitration`, `ground-ambulance-NSA-exclusion-state-mini-NSA`,
  `air-ambulance-NSA-covered`, `emergency-vs-non-emergency-out-of-
  network-distinction`, `EOB-reading-vs-provider-bill-reconciliation`,
  `CPT-coding-error-resubmission`
- Immigration interface: `lawful-presence-requirement-for-APTC`,
  `DACA-vacatur-late-2025-marketplace-exclusion`, `Medicare-40-
  quarters-vs-LPR-5-year-residency-paid-premium`, `mixed-status-
  household-FPL-numerator-denominator-asymmetry`

If a Pass-1 risk surface generalizes into one of these, emit the
specific. If the situation supports a risk not in this list, emit it
as-is (the list is non-exhaustive; new entries should follow the same
specific-statute-or-mechanism naming rule).

**Framing-signal vocabulary.** Pass-2 also emits an optional
`active_framings` field — the F1–F14 framings from
[`framings.md`](./framings.md) the situation's vocabulary already
indicates the asker is reasoning inside. Match against each framing's
*Characteristic vocabulary*. This routes the Risk Officer to surface
the **opposing** framing's blindspots. The load-bearing oppositions
(per `framings.md` "Cross-framing tensions"):

- F1 (expected-utilization arithmetic) ↔ F2 (risk-transfer / OOP-cap)
  — same household, opposite plan recommendation on D1. F1's
  probability-weighted scenario table picks HDHP for the healthy
  asker; F2's worst-case-single-event focus picks PPO with
  predictable copays.
- F3 (HSA-as-retirement) ↔ F4 (immediate-cost / cash-flow) — same
  contribution capacity, opposite strategy on D6 / D9. F3 funds the
  HSA to the cap and pays current medical from taxable; F4 says the
  taxable savings don't exist and the HSA contribution is itself a
  cash-flow drag.
- F5 (ACA-subsidy-mechanics) ↔ F9 (pre-existing-condition-
  protection) — D7 is where they collide. F5 has no native
  vocabulary for STLDI / sharing-ministry (out-of-scope for the
  marketplace subsidy framework); F9 rules them out on pre-existing-
  condition grounds without engaging the for-healthy-high-income
  subset where F5's silence reads as endorsement.
- F6 (Medicare-irreversibility) ↔ F10 (network and prior-auth) — D8
  convergence with different reasoning paths. F6 makes the GI window
  dispositive; F10 makes the any-Medicare-accepting-provider network
  dispositive. Both push Original Medicare + Medigap for high-
  utilization or specialty-care-expected; the divergence is that F6
  alone can be persuaded by the MA "trial-right" return path while
  F10 doesn't engage with it (the mid-year network-drop risk is
  binding regardless of return rights).
- F8 (ERISA-procedural) ↔ F13 (bureaucratic-procedural / patient-
  advocate) — denial-of-claim event has both readings. F8 routes to
  an ERISA attorney at the regulatory-jurisdictional level; F13
  routes to a patient-advocate / billing-error-recovery service at
  the operational-form-and-deadline level. Surface both when denial
  dollars exceed $5k or when the asker mentions any SPD-reading
  issue.
- F12 (tax-and-arbitrage) ↔ F4 (immediate-cost / cash-flow) — the
  same $4,300 HSA contribution is a tax win in F12 and a cash-flow
  drag in F4. Surface both when the asker's facts span tax-
  optimization questions AND cash-flow questions simultaneously.
- F14 (single-payer / market-failure) ↔ F1 / F2 / F3 / F4 (decision-
  support framings) — F14 is a *meta-context* framing, not a
  primary decision lens. It grades the system rather than the
  choice; surface it as Editor / Risk Officer meta-context only,
  never as the sole framing on an answer for an asker with a
  Tuesday OE deadline.

The asker's framing is itself a blind spot — Triage emits the
opposing framing in `active_framings` even when the asker's vocabulary
doesn't match it, so the Risk Officer has the opposing surface to
work from.

**Cross-domain routing flags.** When Pass-1 surfaces signals that
imply an adjacent domain, emit `cross_domain: [<slug>, ...]`.
`health-insurance` is among the densest cross-domain hubs in the
ontology. Per [`decisions.md`](./decisions.md) and
[`framings.md`](./framings.md) annotations:

- Employer / layoff / job change / W-2 termination / total-comp →
  add `tech-career` (D1, D2, D3 boundary `tech-career`; F7 SEP-
  clock-management; the highest-frequency edge)
- HSA-as-retirement / Roth-conversion-and-IRMAA / dollar-specific
  contribution sizing / withdrawal-sequencing-in-retirement → add
  `personal-finance` (D1, D6, D9 boundary `personal-finance`; F3 /
  F12)
- DACA / mixed-status / lawful-presence / Medicare-40-quarters-vs-
  LPR-5-year → add `immigration` (D3, D5, D8 boundary `immigration`;
  F5 cross-domain edge)
- IVF / pregnancy / fertility / spouse-aging-into-Medicare / divorce-
  mid-treatment / dependent age-26 / newborn-QLE → add
  `family-planning` (D2, D4, D10 boundary `family-planning`)
- ERISA-self-funded-plan-denial / 29-CFR-2560.503 / mini-COBRA-state-
  extension → add `legal-disputes` (D3, D8, D10 boundary
  `legal-disputes`; F8 cross-domain edge)
- §127 employer tuition reimbursement on grad-school OE timing → add
  `education-funding` (rare but real)

These flags inform the orchestrator's source-view selection; Pass-2
itself does not call those domains' packs. The `personal-finance` ↔
`health-insurance` edge is the most load-bearing on referral routing
— HSA-as-triple-tax-advantaged-retirement and FSA-vs-Child-Care-Tax-
Credit coordination both route through it before the CPA referral is
named.

---

## Editor

The generic editor prompt in
[`src/blindspot/prompts/editor.md`](../../src/blindspot/prompts/editor.md)
governs structure. The additions below apply when this domain is
active.

**Numeric and statutory specificity is mandatory.** Health-insurance
blindspots are worthless without the specific dollar threshold, the
specific clock, the specific statute or regulatory cite. When a
blind spot or action references the categories below, the specific
number / clock / statute is required; the generic shape is Critic-
failing padding:

- *ACA OOP-max ceilings*: $9,450 self-only / $18,900 family for 2026
  (indexed annually). Embedded individual OOP-max sub-limit ≤ self-
  only OOP-max under the 2016 ACA rule. Out-of-network OOP-max
  absent on most HMO / EPO / narrow-network silvers.
- *HDHP minimum deductible + OOP-max ceiling for HSA-eligibility*:
  $1,650 self / $3,300 family minimum deductible (2026); $8,300 self
  / $16,600 family OOP-max ceiling (2026, per IRC §223(c)(2)(A)).
- *HSA contribution limits*: $4,300 self / $8,550 family (2026), plus
  $1,000 55+ catch-up (IRC §223(b)(3); §223(b)(8) last-month-rule;
  IRS Pub 969).
- *FSA limit + carryover*: $3,300 healthcare FSA (2026; employer-
  set), $660 carryover OR 2.5-month grace period (employer-elected,
  mutually exclusive). Dependent-care FSA $5,000 family / $2,500 MFS
  (uncapped use-it-or-lose-it, no carryover, 90-day post-plan-year
  claims-submission deadline).
- *Medicare Part B late-enrollment penalty math*: 10% of the standard
  Part B premium for each full 12-month period the asker could have
  had Part B but didn't, **applied to the Part B premium for life
  AND indexed to future premium increases**. 5-year delay = 50%
  premium add for life, not 50% of the original premium one time.
- *IRMAA brackets (2026)*: Part B + Part D premium loading at MAGI
  thresholds calculated on 2-year-lookback MAGI. Brackets indexed
  annually; verify the current year. Roth-conversion / equity-comp
  in 2026 → IRMAA hit on 2028 premiums.
- *ARPA / IRA enhanced-subsidy sunset*: the elimination of the
  400%-FPL "subsidy cliff" expires end of 2025 absent further
  congressional extension. Verify current-year subsidy schedule;
  the cliff is back unless extended.
- *Silver-CSR variants*: 94% / 87% / 73% AV at 100–150% / 150–200% /
  200–250% FPL respectively. At ≤200% FPL the silver-CSR-94 / 87
  effectively a near-platinum plan at silver premium — strictly
  dominates gold. The benchmark-silver APTC is keyed to the **second-
  cheapest silver plan** in the rating area.
- *Medigap GI window*: 6 months from Part B effective date (IEP).
  State-specific GI regimes: NY / CT / MA / ME annual or year-round;
  CA / OR birthday-rule annual window. Most states are IEP-only.
- *Part D LEP*: 1% of national base premium per uncovered month
  (permanent). National base premium $36.78 for 2026 (verify
  current). Creditable Part-D coverage requires annual employer
  notice (29 CFR §423.56).
- *No Surprises Act §2799A*: IDR arbitration on surprise out-of-
  network bills. Air ambulance NSA-covered; ground ambulance NSA-
  excluded (some states have mini-NSA closing the ground gap).
- *ERISA self-funded-plan signals*: the SPD says "the plan is self-
  insured" or "self-funded"; the Form 5500 filing is searchable on
  DOL EBSA; the carrier card is a "claims administrator" rather
  than an "insurer." 29 USC §1144(a) pre-empts state-insurance-
  commissioner remedies; 29 CFR §2560.503-1 governs claims and
  appeals; 180-day adverse-benefit-determination appeal deadline;
  *Firestone* deference under SPD grant-of-discretion clause.

**Decision-support, not medical / insurance advice — explicit label
required on every output.** Because `health-insurance.high_stakes`
is `true` per Mechanism E, every final output MUST include language
equivalent to: *"This is decision-support framing, not medical or
insurance advice. Health-insurance decisions are high-stakes — the
12-month plan-year lock-in causes uncapped out-of-network exposure
on a wrong call; missed Medicare enrollment windows cause permanent
premium penalties; ACA-noncompliant alternatives carry post-claim
rescission and pre-existing-condition-exclusion risks invisible
until claim time. The binding determination on your specific case
requires the appropriate specific professional with your full
medical, income, and plan picture: [the specific category — see
referral list below]."* The label belongs at the head of the answer
for D4, D7, D8 (the highest-stakes irreversibility decisions); for
other decisions it can tail the answer. Critic flags soft language
("may want to consider speaking with a broker eventually") as
insufficient.

**Selective-professional-referral matrix.** Unlike the "consult an
attorney" blanket of immigration, the *category* of professional
varies sharply by decision in health-insurance — broker for
commercial OE is structurally different from a SHIBA volunteer for
Medicare-side decisions (broker-vs-SHIBA cuts on conflict-of-
interest: broker compensation is carrier-paid and most distorted on
MA-vs-Medigap, where MA commissions can dwarf Medigap commissions;
SHIBA volunteers are federally funded under SSA §4360, non-
commissioned, plan-agnostic). The Editor names the *specific
category* keyed to the decision and trigger, per the calibration
encoded in [`decisions.md`](./decisions.md) "Notes for downstream
layers" and [`blindspots.md`](./blindspots.md) Recovery rules:

- **Licensed health-insurance broker (independent — not single-
  carrier captive)** — D1 (HDHP / PPO / HMO at OE), D2 (spousal /
  dependent coverage carve-out), D5 (Marketplace metal-tier for
  income above silver-CSR band where broker incentive is least
  distorted). Surface the carrier-paid-vs-fee-only distinction when
  comparing MA — broker commission asymmetry between MA and Medigap
  is the most acute conflict point; SHIBA referral is the conflict-
  free alternative for D4 / D8 specifically.
- **SHIBA / SHIP volunteer** — D4 (Part B delay vs enroll), D8
  (Original Medicare + Medigap vs MA at IEP). State Health Insurance
  Assistance Program, federally funded under SSA §4360, non-
  commissioned, plan-agnostic. The structural counterweight to
  broker / agent commission-driven MA recommendations. Each state
  publishes a directory of SHIP counselors; the SHIP National
  Technical Assistance Center maintains the master list. Refer by
  state — "your state SHIP" rather than "a Medicare counselor"
  generic.
- **CMS-trained ACA-Marketplace Navigator or in-person assister** —
  D3 (COBRA vs marketplace at job loss), D5 (Marketplace metal-tier
  with APTC and CSR), D7 (ACA-compliant vs STLDI / sharing
  ministry). CMS-trained, plan-agnostic, prohibited from steering.
  Underutilized because less publicized than broker channels.
  Refer by state for state-based-exchange jurisdictions (16 states +
  DC); refer to Healthcare.gov assister-finder for HHS Marketplace
  states.
- **Retirement-experienced CPA** — D6 (FSA / HSA / dep-care FSA
  sizing) and D9 (HSA last-month-rule timing). Form 8889 / Form
  2441 / Form 8962 mechanics; HSA-and-Medicare retroactive Part-A
  6-month rule; IRMAA 2-year-lookback Medicare-premium implication
  of MAGI shocks; dep-care-FSA-vs-Child-and-Dependent-Care-Tax-
  Credit coordination. Boundary `personal-finance` — for any asker
  with significant taxable equity-comp or 1099 income, the CPA
  referral should match an HSA-experienced practitioner, not a
  generic tax preparer.
- **ERISA-litigation attorney** — D3 (COBRA mechanics, mini-COBRA
  state extensions, mid-coverage termination disputes), D8 (Medigap
  GI denial-appeal where GI-eligibility is contested), D10 (denial-
  of-claim or denial-of-appeal escalating into six-figure dispute
  under a self-funded employer plan). State-insurance-commissioner
  remedies are pre-empted under ERISA per 29 USC §1144(a); 29 CFR
  §2560.503-1 governs procedural rights; 180-day adverse-benefit-
  determination appeal deadline is strict; administrative
  exhaustion is mandatory before federal §502(a) civil enforcement.
  Refer at any denial of significant claim — the procedural
  mistakes are unrecoverable. Boundary `legal-disputes`.
- **State Insurance Commissioner consumer-assistance bureau** —
  STLDI rescission complaints (STLDI is state-regulated, not ERISA-
  preempted), healthcare-sharing-ministry "non-share" disputes (the
  state may have jurisdiction where the ministry operates without
  proper exemption), fully-insured (non-self-funded) commercial-
  plan grievances. Free, state-funded, faster than ERISA-attorney
  route for sub-six-figure fully-insured disputes. Refer by state;
  the NAIC consumer-information directory maintains the master
  list.
- **Patient-advocate service / billing-error-recovery service
  (NAHAC / Patient Advocate Foundation / fee-based individual
  advocate)** — D3 / D10 post-billing recovery; EOB-line-item
  reading; CPT-coding-error resubmission; No Surprises Act §2799A
  IDR triggering procedure (the asker has to know to request IDR;
  facilities don't volunteer the option); balance-billing-recovery
  case-management. Refer when claim denial dollars are below the
  ERISA-attorney threshold (~$5k) AND the issue is procedural /
  coding rather than coverage-determinational.
- **Medicare-appeals attorney (or experienced patient-advocate)** —
  Medicare ALJ-tier appeals at $1,840 amount-in-controversy minimum
  (2026 — verify), federal-court review at $9,000+. Distinct from
  ERISA-attorney territory; Medicare appeals operate under the
  Medicare Appeals Council framework, not ERISA. Refer when the
  asker has exhausted QIC / reconsideration and the dispute meets
  the ALJ-tier threshold.

When the situation matches a trigger for one of these categories,
the Editor's Recovery move names that *specific* category — not
"consult a professional" generic. Over-referral (naming a category
that does not match a trigger) is *also* a failure mode the Critic
flags — see the Critic section below. The uniform Mechanism E
posture here means "every output names *some* specific category
keyed to the decision class," not "every output names every
category."

**Don't soften the high-density blindspot anchors.** Per
[`decisions.md`](./decisions.md) "Notes for downstream layers,"
decisions D3, D4, D5, D7, D8 are the highest-density blindspot
anchors; D4 and D8 carry the highest single-misstep tail risk
(permanent Medicare premium loading; permanent Medigap underwriting
exposure); D7 carries the highest information-asymmetry-driven harm
risk (STLDI / sharing-ministry headline premium savings are real,
the contingent uncovered-tail-risk is invisible until claim time).
When the Risk Officer surfaces a blindspot tied to these decisions,
it ships in the final output verbatim — Editor hedging on Part B
SEP-clock exposure, Medigap GI-window irreversibility, STLDI post-
claim-rescission risk, or silver-CSR strict-dominance arithmetic is
exactly the Critic-failing brand of padding the high-stakes regime
was written to catch.

**Opposing-framing surfacing is mandatory.** Per
[`framings.md`](./framings.md) "Cross-framing tensions," every
Editor output on a health-insurance situation must surface at least
one blindspot from the framing OPPOSITE the asker's apparent one
(F1↔F2, F3↔F4, F5↔F9, F6↔F10, F8↔F13, F12↔F4, F14↔F1/F2/F3/F4 as a
meta-context). The opposing framing's `Excludes` line is the seed;
surface it as a "here is the lens your question's vocabulary
excluded" paragraph, not a buried bullet. F14 (single-payer /
market-failure) is the one exception — surface as meta-context only
when the asker's prompt expresses frustration at the system itself,
never as the sole framing on a Tuesday-OE-deadline answer.

**Cross-domain handoff.** When the situation crosses
`personal-finance` (most common — HSA-as-retirement, IRMAA, FSA-vs-
tax-credit), `tech-career` (layoff-driven coverage transition),
`immigration` (DACA / mixed-status / Medicare-40-quarters),
`family-planning` (IVF / pregnancy / divorce mid-treatment / spouse-
aging-into-Medicare), or `legal-disputes` (ERISA self-funded
denial), name the coupling explicitly — e.g. "the HSA-vs-FSA
contribution and the Roth-vs-traditional 401k decisions are coupled
here because both shift MAGI, and the IRMAA 2-year-lookback means
your 2026 contribution choice hits 2028 Medicare premiums; F12's
tax-and-arbitrage lens applies to both decisions." Do not silo the
health-insurance discussion when the asker's situation spans
domains.

---

## Critic

Generic Critic rules from
[`src/blindspot/prompts/critic.md`](../../src/blindspot/prompts/critic.md)
apply unchanged. The additions below tune the per-claim spot-check
for health-insurance-specific claim categories. Because the domain
is `high_stakes: true`, **every numeric, statutory, or regulatory
claim is subject to mandatory per-claim grounding** — the generic
"recommended" spot-check is upgraded to hard pass / fail here, in
the same uniform shape as immigration's Critic per PR #53 (NOT the
targeted-only shape of housing's Critic per PR #69).

**Per-numeric-claim citation is mandatory** for any sentence
containing:

- An ACA-statute / regulatory cite (ACA §1302 EHB, ACA §1402 CSR,
  ACA §1311 marketplace, 45 CFR §147 ACA insurance reforms, 45 CFR
  §156 EHB benchmarks, IRC §36B APTC, IRC §5000A individual mandate
  / penalty zeroed)
- An HSA / FSA statutory cite (IRC §223 HSA, IRC §125 cafeteria plan,
  IRC §129 dep-care, IRC §213(d) qualified medical expense, IRC
  §223(b)(8) last-month-rule, IRC §223(b)(7) Medicare exclusion, IRC
  §223(c)(2) HDHP definition, IRS Pub 969, IRS Notice 2004-50 /
  2008-59, Rev. Proc. annual HSA-limit)
- A Medicare statutory / regulatory cite (42 USC §1395 Medicare
  generally, 42 USC §1395ss-1(b) Medigap GI, 42 CFR §407 Part B
  enrollment, 42 CFR §417 Medicare Advantage, 42 CFR §423 Part D,
  29 CFR §423.56 creditable-coverage notice, CMS-12036-N annual
  rule, MLN Matters articles)
- An ERISA cite (29 USC §1132 civil enforcement, 29 USC §1144(a)
  pre-emption, 29 CFR §2560.503-1 claims and appeals, ERISA §502(a)
  federal-court venue, ACA §2719 external-review-process)
- A No Surprises Act cite (NSA §2799A-1 IDR; *Texas Medical
  Association v. HHS* litigation history; QPA methodology)
- A specific dollar threshold (ACA OOP-max $9,450 / $18,900 for
  2026; HSA $4,300 / $8,550 plus $1,000 catch-up; FSA $3,300; dep-
  care-FSA $5,000 / $2,500; HDHP minimum deductible $1,650 /
  $3,300; HDHP OOP-max ceiling $8,300 / $16,600; Medicare ALJ
  $1,840 amount-in-controversy minimum for 2026; federal-court
  review $9,000+; IRMAA bracket thresholds)
- A specific day-count clock (60-day marketplace SEP, 60-day COBRA
  election, 45-day COBRA premium payment grace, 30-day employer-
  plan QLE window, 90-day FSA claims-submission deadline, 13-month
  HSA last-month-rule testing period, 7-month Medicare IEP, 6-
  month Medigap GI, 8-month SEP from end-of-employment, 180-day
  ERISA adverse-benefit-determination appeal deadline, 60-day non-
  protected-class formulary-change notice)
- A specific percentage / penalty math (10%-per-12-months Part B
  LEP, 1%-per-month Part D LEP, 78%/80% LTV for PMI [N/A here —
  housing], 20% / 30% / 40% silver-CSR loading bands)
- A Marketplace / Medicare / Medicaid eligibility regulatory claim
  (DACA vacatur late 2025; family-glitch fix 2022 IRS rule; lawful-
  presence requirement; Medicare 40 quarters vs LPR-5-year-
  residency-and-paid-premium)
- A state-specific Medigap GI claim (NY / CT / MA / ME annual or
  year-round; CA / OR birthday rule; specify state)
- A self-funded vs fully-insured determination claim, or any
  "ERISA pre-empts X" claim

If any such sentence lacks an adjacent `[doc-X]` marker citing a
source-view in [`sources.yaml`](./sources.yaml), set
`regenerate_required = true` AND name the uncited specific verbatim
in `feedback`. Citation-recycling (one marker reused across distinct
numeric claims) fails the same check. This is stricter than the
housing partial-gating rule because health-insurance fabrications
cause irreversible harm — a wrong Part B LEP claim cannot be undone
by a follow-up correction the way a wrong PMI threshold can.

**Specificity bar.** Generic phrases that pass the standard Critic
check are STILL fails in this domain. The shapes below all *look*
specific (they name a mechanism) but contain no statute, no clock,
no dollar threshold:

- "Be careful about timing" (no clock named) — fail.
- "There's a grace period after termination" (no 60-day COBRA / 60-
  day marketplace-SEP / 45-day payment grace cited) — fail.
- "Watch out for the Part B late enrollment penalty" (no 10%-per-
  12-months math, no permanent-and-indexed clarification) — fail.
- "Medigap underwriting can deny you" (no 6-month GI window cited,
  no state-specific GI rules named) — fail.
- "The HSA last-month rule has a testing period" (no 13-month named,
  no recapture math, no IRC §223(b)(8) cite) — fail.
- "Marketplace silver might be a better deal" (no CSR-94/87/73 AV
  variant, no 100–250% FPL band, no benchmark-silver mechanic) —
  fail.
- "Consider speaking to a professional" (no specific category named
  per the Editor's referral matrix above) — fail when used as a
  substitute for analysis; pass only as the Mechanism E label on
  decision-support framing PLUS a specific-category recommendation.
- "ERISA might apply" (no self-funded-vs-fully-insured test, no 29
  USC §1144(a) pre-emption cite, no 29 CFR §2560.503-1 procedure)
  — fail.
- "STLDI is risky" (no pre-existing-condition-exclusion mechanic, no
  OOP-cap-absence, no 4-month-initial-1-month-renewal rule) — fail.
- "Network adequacy varies" (no provider-directory-30-50pct-
  inaccurate, no ghost-network vocabulary, no Original-Medicare-any-
  provider contrast) — fail.

Mark specificity as `fail` and name the offending sentence verbatim
in `feedback`.

**Non-obviousness floor — `+1` for multi-route situations.** When
the matched persona spans multiple decisions or covers an opposing-
framing pair simultaneously (e.g.
`dual-employer-spouse-with-coverage-overlap` who is also
`mid-year-hdhp-hire-considering-last-month-rule`; or
`recently-laid-off-with-deductible-met` who is also
`chronic-condition-on-specialty-drug`; or
`near-65-still-working-large-employer` who is also
`mid-treatment-divorce-with-deductible-met`), raise the non-
obviousness floor by one point. A 3/5 that would pass for a single-
route asker is a 2/5 here. Multi-route askers have already heard
the single-route advice; surfacing only what they already know
fails non-obviousness. This is the health-insurance parallel to
tech-career's `comparing-offers-*` non-obviousness raise and
immigration's multi-route raise.

**Cross-framing tension as a quality signal.** When the Risk
Officer surfaces blindspots from a framing OPPOSITE the asker's
apparent one (F1↔F2, F3↔F4, F5↔F9, F6↔F10, F8↔F13, F12↔F4 — see
Triage above), that typically raises non-obviousness by 1 point
because the asker's vocabulary already excluded the opposing
framing. Score accordingly — the opposing-framing surfacing is the
highest-leverage signal that the answer is doing the asker's
framing-correction work, not just restating their starting
position. F14 (single-payer / market-failure) surfaced as meta-
context does NOT count toward this signal; meta-context surfacing
is its own quality dimension and should not be conflated with
opposing-framing decision-support.

**Specific-professional-referral check (both over- and missed-
referral fail).** Because health-insurance uses uniform Mechanism E
gating with a *selective* professional-referral matrix (the
*category* varies by decision class — broker vs SHIBA vs Navigator
vs CPA vs ERISA attorney vs State Insurance Commissioner vs
patient-advocate vs Medicare-appeals attorney; see the Editor
"Selective-professional-referral matrix" above), the Critic verifies
two complementary failure modes:

- **Over-referral / wrong-category-referral.** If a Recovery move
  names a category whose trigger does NOT match the matched
  decision class (e.g. naming "consult an ERISA attorney" for a D1
  HDHP-vs-PPO question where the plan is fully-insured rather than
  self-funded; or naming "SHIBA volunteer" for a D5 marketplace
  decision where the asker is not yet Medicare-eligible; or naming
  "Marketplace Navigator" for a D8 Medigap-vs-MA decision), set
  `regenerate_required = true` and name the unjustified referral
  verbatim in `feedback`. Generic "consult a health-insurance
  professional" without category specification ALSO fails this
  check — the uniform Mechanism E posture requires *specific
  category* keyed to the decision, not blanket-generic deferral.
- **Missed-referral.** If the situation matches a trigger from the
  Editor referral matrix but the Recovery is self-directed or names
  the wrong category at lower stakes (e.g. omits "ERISA-litigation
  attorney" on a self-funded-plan six-figure denial; omits "SHIBA
  volunteer" on a 65-year-old considering MA at IEP; omits "CMS-
  trained Navigator" on a low-income marketplace-shopper at silver-
  CSR-eligible income; omits "State Insurance Commissioner" on a
  STLDI post-claim rescission grievance), also fail with
  `regenerate_required = true` and name the missed referral category
  verbatim in `feedback`. Missed-referral on a high-stakes trigger
  is itself a Mechanism E failure mode — under-referral creates
  harm symmetrically to over-referral degrading signal.

The matrix is keyed by decision in the Editor section; the Critic's
check is to verify the match. Both directions matter.

**Mechanism E label check.** If the final output lacks the
decision-support / not-medical-or-insurance-advice / consult-
specific-professional language required of every high-stakes-
domain answer (see Editor section above), set
`regenerate_required = true` regardless of other quality
dimensions. This is non-negotiable per
[ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating).
Soft variants ("you might want to talk to a broker eventually")
fail the check; the language must be explicit decision-support
framing PLUS an explicit specific-category-of-professional
recommendation, and for the highest-stakes situations (D4, D7, D8,
anything with an ERISA self-funded-plan denial or a permanent-
Medicare-penalty exposure) the label belongs at the head of the
answer rather than the tail.

---

## Notes for refine

- This file is `delta`, not duplication. If a future refine wants to
  add another persona, risk-surface, statute citation category, or
  claim shape, prefer editing the relevant short list above to
  growing the file beyond its current word count.
- The opposing-framing pairs (F1↔F2, F3↔F4, F5↔F9, F6↔F10, F8↔F13,
  F12↔F4; F14 as meta-context) are the highest-leverage routing
  tuning in this file. If eval shows the Risk Officer underusing the
  opposing-framing surface on health-insurance situations, sharpen
  the Triage `active_framings` section first.
- The selective-professional-referral matrix is the second-highest-
  leverage tuning. The matrix is uniform-gating-with-specific-
  category — every output names some category, but the category
  varies by decision class. If eval shows over-referral patterns
  (broker named for Medicare decisions; SHIBA named for marketplace
  decisions; "consult a professional" generic), tighten the Critic
  specific-professional-referral check first; if eval shows missed-
  referral patterns (self-directed Recovery on six-figure ERISA
  denials; no SHIBA on IEP decisions; no Navigator on silver-CSR-
  eligible marketplace), tighten the Editor referral matrix's
  trigger anchors.
- High-stakes propagation: this file currently says `high_stakes:
  true` per [`_meta_ontology.md` §4](../_meta_ontology.md). The
  Editor Mechanism E label and Critic mandatory-grounding rules
  above are load-bearing on that flag. If `_meta_ontology.md` ever
  softens that flag (extremely unlikely for health-insurance), the
  corresponding rules here must be removed in the same change.
- Date-stamp risk: anchor numbers above (ACA OOP-max ceilings, HSA
  / FSA / HDHP contribution and deductible limits, IRMAA brackets,
  ARPA-enhanced-subsidy sunset, Medicare ALJ amount-in-controversy
  minimum, Part D national base premium, STLDI 4-month-initial-1-
  month-renewal rule) all inherit the date-stamp risk
  [`blindspots.md`](./blindspots.md) Maturity / source-anchor note
  enumerates. Re-check before tightening any dependent Critic rule.
  Specific watch items:
  - **ARPA / IRA enhanced-subsidy sunset end of 2025** — if not
    extended, the 400%-FPL "subsidy cliff" returns and F5's
    "no cliff above 400% FPL" reasoning becomes wrong.
  - **DACA marketplace eligibility vacatur late 2025** — the post-
    vacatur regulatory posture excludes DACA recipients from APTC;
    pre-vacatur material is now wrong.
  - **2024 STLDI final rule** — 4-month-initial-1-month-renewal cap
    (vs prior 36-month allowance under 2018 rule); could shift
    again with administrative change.
  - **2026 ACA OOP-max indexing, HSA limits, Medicare premiums,
    IRMAA brackets** — verify annually around late Q4 / early Q1.
- Cross-domain density: `health-insurance` ↔ `personal-finance` is
  the most load-bearing edge on referral routing — HSA-as-triple-
  tax-advantaged-retirement, FSA-vs-Child-Care-Tax-Credit, IRMAA
  2-year-lookback all route through it before the CPA referral is
  named. When `personal-finance/domain_pack.md` lands, cross-check
  CPA-referral triggers against the parallel rules there.
- The uniform Mechanism E posture here (every output names a
  specific category) differs deliberately from housing's partial-
  gating (only six-figure-tail-risk triggers name a category) and
  from tech-career's locally-gated equity-tax-only posture. The
  difference is grounded in the two-irrevocability-classes intro:
  12-month plan-year lock-in compounds for up to a year and the
  permanent Medicare penalty regime never amortizes. Housing's
  "buy the wrong house, sell and refi" recoverability does not
  exist here.
