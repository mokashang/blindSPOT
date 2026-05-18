# health-insurance — decisions.md (Layer 1)

Decision ontology for `health-insurance`. Scope inherits from
[`_meta_ontology.md` §4](../_meta_ontology.md): US-resident health-
coverage decisions — open-enrollment plan selection (HDHP / PPO / HMO
/ EPO / POS), HSA / FSA / HRA optimization, COBRA-vs-marketplace at
job change, Medicare enrollment and Part-A/B/C/D/Medigap selection,
spousal and dependent coverage strategy, ACA-marketplace subsidy and
metal-tier choice, ACA-noncompliant alternative coverage (short-term
limited-duration, healthcare-sharing ministries). Excludes diagnosis,
treatment selection, and provider-quality evaluation (deferred to
medical-diagnosis Mechanism E gating per `_meta_ontology.md`
"Out-of-scope") and excludes employer benefits design (the
plan-sponsor side; this domain covers the employee-as-consumer side).

The `health-insurance` domain is **high_stakes: true** per
`_meta_ontology.md` §4 and ROADMAP §5 Mechanism E. Two distinct
classes of irrevocability drive the posture:

- **12-month lock-in** on most decisions: outside an annual open-
  enrollment window or a narrow Qualifying-Life-Event (QLE) window,
  the user cannot change plans, switch from PPO to HDHP, add/drop
  dependents, or pivot off marketplace coverage. A wrong choice
  compounds for up to a full plan year with uncapped out-of-pocket
  exposure on the high-deductible end (the ACA OOP cap exists but
  only on in-network EHB-classified care; out-of-network specialty
  care and non-EHB services like cosmetic-adjacent procedures can
  exceed it).
- **Permanent penalties** on Medicare-side missteps: missing the
  Part-B Initial Enrollment Period (IEP) without creditable employer
  coverage triggers a 10%-of-Part-B-premium-per-12-months-late
  penalty that compounds and persists for life; missing the
  Medigap Guaranteed-Issue (GI) window similarly subjects the
  beneficiary to medical underwriting forever (denial, exclusion,
  or rate-up). A late Medicare-Advantage-to-Original-Medicare switch
  is technically allowed but practically blocked when Medigap
  underwriting denies. These are not insurance decisions in the
  ordinary sense — they have a permanent-record character closer to
  immigration status decisions than to housing or tech-career.

Posture: **"decision-support, not licensed-broker advice"** is the
consistent Editor framing. Downstream `blindspots.md` Recovery moves
should defer to **(a) a licensed health insurance broker** for plan-
comparison and EOB / appeals work in the under-65 commercial /
marketplace space (broker compensation is typically carrier-paid so
their advice is nominally free to the consumer, but the
employer-vs-broker conflict in spousal-coverage decisions is itself
a framing axis — see decision 2 below), **(b) a SHIBA / SHIP
volunteer** (State Health Insurance Assistance Program — federally
funded, free, conflict-free) for Medicare enrollment decisions
specifically, since broker compensation distorts incentives most
sharply in Medicare Advantage where carriers pay agents per-enrollee
commissions that can dwarf Original-Medicare-plus-Medigap commission,
**(c) the Marketplace Navigator or in-person assister network** for
APTC-eligibility and enrollment specifically (Navigators are CMS-
trained, plan-agnostic, and prohibited from steering), and **(d) an
ERISA-litigation attorney** when a denial-of-claim or denial-of-
appeal escalates into a six-figure dispute under a self-funded
employer plan (state-insurance-commissioner remedies are pre-empted
under ERISA, which constrains the procedural and damages posture).
Over-referral degrades signal; the Editor layer should name the
specific category (broker vs SHIBA vs Navigator vs ERISA attorney)
keyed to the decision and trigger, not blanket-mandate "consult a
professional" on every framing.

Framing-axes named below are pointers — full framings will live in
`framings.md` (later artifact). Cross-domain edges are flagged
inline. `tech-career` overlaps on employer-plan choice as a comp
component (decisions 1, 2, 3) and on layoff-driven COBRA-vs-
marketplace transitions (decision 3). `immigration` overlaps on
visa-status-dependent coverage eligibility — Marketplace APTC
requires "lawful presence" but excludes DACA recipients (as of the
current regulatory posture; the inclusive 2024 rule was vacated in
late 2025), and Medicare requires either 40 quarters of work history
OR LPR-status-with-5-year-residency-and-paid-premium (decisions 3,
5, 8). `personal-finance` overlaps heavily on HSA-as-triple-tax-
advantaged-retirement-account (decision 1) and FSA-vs-HSA-vs-
dependent-care-FSA contribution coordination (decision 6).
`family-planning` overlaps on spouse/dependent coverage and on
maternity / pediatric / fertility coverage scoping (decisions 2,
10). `legal-disputes` overlaps on ERISA pre-emption of state remedies
in denial-appeal procedures and on COBRA-election-window rights
(decisions 3, 10). Routing across edges is V2-Triage's job; the edge
annotations here help future `framings.md` authors name the adjacent
domains.

---

## 1. HDHP + HSA vs PPO vs HMO at employer open enrollment

- **Scope**: Employee with employer-sponsored coverage choosing among
  the available plan options at annual open enrollment, typically one
  HDHP (high-deductible health plan paired with HSA-eligibility), one
  or more PPO tiers, and sometimes an HMO or EPO. Decision compresses
  expected-utilization forecast, HSA-as-retirement-vehicle
  optimization, network breadth, and premium-vs-OOP-max trade-off.
  Distinct from decision 5 (marketplace metal-tier) — here employer
  subsidizes the premium, often non-uniformly across tiers, distorting
  the apparent "cost" of each plan. Distinct from decision 9 (HSA
  contribution timing) — here the question is whether HSA-eligibility
  is even on the table.
- **Framing-axes-covered**: expected-utilization-and-premium-vs-OOP-
  max-arithmetic (the worst-case-vs-expected-case framing — many
  plans cross over only at the 90th-percentile-utilization scenario),
  employer-premium-subsidy-asymmetry-across-tiers (the apparent
  $300/mo HDHP-vs-PPO delta may be $700/mo gross with employer
  picking up $400 differently — check the total-comp impact, not the
  payroll-deduction delta), HSA-as-triple-tax-advantaged-retirement-
  vehicle (pre-tax in, tax-free growth, tax-free out for qualified
  medical — strictly dominates 401k-after-match dollar-for-dollar
  if the user can pay current medical OOP and let HSA compound;
  boundary `personal-finance`), employer-HSA-contribution-and-vest
  (some employers match HSA contributions; some put a flat amount in
  regardless), network-breadth-and-narrow-network-EPO-trap (an EPO
  with no out-of-network coverage at all carries balance-billing risk
  even for emergency-room out-of-network anesthesia; surprise-billing
  protections via No Surprises Act help but do not fully eliminate),
  embedded-vs-aggregate-family-deductible (see decision 10),
  prescription-formulary-tier-and-specialty-drug-coverage
  (specialty-drug copays can be $500–5000/month even on
  "good" PPOs — verify the specific drug if any household member is
  on one), telehealth-and-mental-health-parity-coverage.
- **Sample situations**:
  - "32yo software engineer, no chronic conditions, employer offers
    HDHP at $80/biweekly with $1,500 employer HSA contribution vs
    PPO at $220/biweekly with $250 deductible. HDHP saves $3,640/year
    in premium plus the HSA contribution — should I switch from PPO?"
  - "Family of 4, two parents on different employers' plans, both
    offer HDHP. One parent has an ongoing $400/month specialty drug.
    HDHP still the right call given the OOP-max math, or stay on PPO
    for the predictable copay?"

## 2. Cover spouse on your plan vs each on respective employer plans

- **Scope**: Dual-income married couple where both employers offer
  coverage. Decision is whether each spouse takes their own
  employer plan, one spouse covers both via family tier, or some
  hybrid (e.g. spouse-A on plan-A self-only, spouse-B + kids on
  plan-B family). The choice interacts with employer "spousal
  surcharge" or "spousal carve-out" policies (employer adds $50–
  200/month surcharge when covered spouse has their own employer
  coverage available; or refuses to cover the spouse at all),
  with the dual-HSA-contribution-coordination rule (family-tier HDHP
  enables $8,550/year family HSA contribution split between spouses,
  vs $4,300 each if both on self-only HDHP), and with maternity /
  fertility coverage variance between the two plans. Distinct from
  decision 10 (dependent-coverage timing). Cross-routes
  `family-planning` (maternity-coverage timing as decision input)
  and `tech-career` (employer benefits as comp differential between
  job-change candidates).
- **Framing-axes-covered**: spousal-surcharge-vs-carve-out-employer-
  policy (carve-out forces a choice when spouse-A's employer offers
  coverage — spouse cannot enroll on spouse-B's plan; surcharge
  allows enrollment but at $600–2400/year penalty), total-household-
  premium-vs-OOP-max-with-each-config (run the arithmetic across
  3+ configurations — both-self-only-each, both-on-A-family, both-
  on-B-family, one-plus-kids-split — many people only compare
  defaults), maternity-and-fertility-coverage-variance (one
  employer's plan may cover IVF and the other may not; mid-year
  switch to access fertility coverage is generally blocked outside
  QLE; coordinate with planning timeline early), HSA-family-vs-self-
  only-contribution-coordination (the $8,550 family cap is shared
  across both spouses' HSAs if both are HSA-eligible; one HSA can
  hold the full family contribution if the other spouse prefers FSA
  or non-HSA plan; the 55+-catch-up $1,000 is per-individual and
  must go in that individual's HSA), divorce-and-job-loss-coverage-
  continuity-risk (each-on-own-plan is more resilient — if either
  spouse loses their job, the other's coverage is unaffected; bundled
  configurations require COBRA or QLE migration), pediatric-cost-
  sharing-and-EHB-coverage-variance, eldercare-and-spouse's-Medicare-
  age-asymmetry (when one spouse hits 65 and considers Medicare,
  the other spouse may need to migrate off the employer family plan
  if employer plan is non-creditable for Medicare integration).
- **Sample situations**:
  - "Both spouses at large employers; my plan has $50 spousal
    surcharge per pay period, spouse's plan covers ours fully without
    surcharge but with $500 higher deductible. Switch both to her
    plan, or each stay on our own?"
  - "Planning IVF next year; my employer covers IVF at $20k lifetime
    max, spouse's employer doesn't cover IVF at all. Migrate spouse
    to my plan at open enrollment so we both have the benefit, or
    keep her on her employer plan for the lower premium?"

## 3. COBRA for 18 months vs marketplace coverage at job loss

- **Scope**: Employee who has just lost their job (involuntary
  termination, layoff, voluntary separation) or whose hours dropped
  below benefits-eligibility threshold, facing the QLE-triggered
  60-day window to elect COBRA continuation, the 60-day Special
  Enrollment Period (SEP) for ACA Marketplace coverage, OR the option
  to migrate onto a spouse's employer plan (if eligible) within their
  30-day QLE window. Decision compresses premium delta (COBRA at
  full-cost-plus-2%-admin-fee can be $1500–2500/mo for family
  coverage vs marketplace silver with subsidy potentially $0–300/mo
  at the same income), network-and-deductible-continuity
  (mid-year-COBRA preserves YTD deductible-met status; marketplace
  resets to $0), subsidy-cliff arithmetic (ARPA-enhanced subsidies'
  income-based phase-out, separate from the original ACA 400%-FPL
  cliff that ARPA had eliminated through 2025), and the 60-day
  retroactive-election trap (electing COBRA retroactively requires
  paying back-premium for the gap months too). Distinct from
  decision 5 (marketplace metal-tier choice given you've already
  chosen marketplace). Cross-routes `tech-career` (layoff timing
  vs benefit-vest cliff) and `legal-disputes` (ERISA pre-emption of
  state COBRA remedies; mini-COBRA state extensions beyond 18
  months).
- **Framing-axes-covered**: COBRA-as-bridge-vs-marketplace-as-
  destination (COBRA's 18-month cap is hard — if marketplace eligible
  later anyway, paying premium for a bridge now plus marketplace
  later is often worse than going to marketplace immediately),
  subsidy-cliff-and-APTC-arithmetic (income-based subsidy
  calculation; the "silver-CSR" cost-sharing-reduction loading is
  available only on silver plans at 100–250% FPL — see decision 5),
  deductible-and-YTD-OOP-continuity-vs-reset (a $4,000-deductible-
  met-by-November job loss makes 60 days of COBRA much more valuable
  than the same situation in February with $0 met), retroactive-
  COBRA-election-as-real-option (the 60-day decision window plus
  45-day premium-payment grace creates a unique 105-day "free
  insurance" option for healthy people — bet on no claim, save the
  premium; on a major claim, retroactively elect and pay back-
  premium), network-and-specialist-continuity-mid-treatment
  (mid-treatment migration breaks specialist relationships and
  often resets prior-auth approvals; weigh against premium savings),
  TAA-or-trade-affected-worker-HCTC-eligibility (Trade Adjustment
  Assistance Health Coverage Tax Credit; pays 72.5% of premium for
  eligible workers; underutilized), Marketplace-SEP-clock-and-
  documentation-requirements (the 60-day SEP starts on the loss-of-
  coverage date, NOT the QLE event-notification; you must furnish
  proof-of-loss-of-coverage within the window), mini-COBRA-state-
  extension-for-small-employers (some states extend COBRA-like
  rights to employers under 20 employees and beyond 18 months;
  boundary `legal-disputes`).
- **Sample situations**:
  - "Laid off November 1; COBRA quote is $2,100/mo family, marketplace
    silver at our likely $40k 2027 income would be $200/mo with APTC.
    Met $6,800 of $8,000 family OOP on the year. COBRA the 2 months
    for $4,200 to close out, or jump to marketplace?"
  - "Just laid off in February; severance equals 4 months pay; I'm
    healthy, no chronic conditions, no upcoming procedures. Skip
    coverage entirely for 60 days and retroactively elect COBRA if
    something happens, or marketplace now?"

## 4. Delay Medicare Part B past 65 while on employer plan vs enroll on time

- **Scope**: Person turning 65 (or already 65) who is still working,
  whose spouse is still working, or who has retiree health coverage
  through a former employer. Decision is whether to enroll in
  Medicare Part B during the Initial Enrollment Period (IEP — the
  7-month window around 65th-birthday-month) or to delay enrollment
  under Special Enrollment Period (SEP) protection, which requires
  the employer plan to be **creditable coverage** AND the employer
  to have ≥20 employees (for the Medicare Secondary Payer rule to
  apply; smaller employers' plans become secondary at 65 regardless
  of enrollment, leaving employees with massive uncovered exposure
  if they delay Part B). Distinct from decision 8 (Original Medicare
  + Medigap vs Medicare Advantage at the moment of enrollment).
  Cross-routes `tech-career` (when to retire decision feeds back
  into this — delaying retirement past 65 to preserve creditable
  coverage status).
- **Framing-axes-covered**: creditable-coverage-test-and-employer-
  size-threshold (employer plan with ≥20 employees is presumptively
  creditable for Part-A integration; for Part-D creditability the
  test is different and requires annual notice — verify each year;
  on a self-insured ERISA plan, the determination is in the SPD),
  Part-B-late-enrollment-penalty-10pct-per-12mo (permanent, lifetime,
  not waivable on hardship — 5-year delay = 50% premium add for life),
  Part-A-vs-Part-B-asymmetry-when-still-contributing-to-HSA (Part A
  is automatic at 65 for SS-claiming beneficiaries; enrolling in
  Part A retroactively disqualifies HSA contributions for the prior
  6-month look-back period — Medicare and HSA-eligibility are
  mutually exclusive even for partial enrollment; delaying SS-claim
  alongside delaying Part-A preserves HSA contribution capacity but
  is its own decision; boundary `personal-finance`), 8-month-SEP-
  clock-after-employment-ends (the SEP runs 8 months from the end-
  of-employment date, NOT end-of-COBRA-coverage; people on COBRA
  past month 8 face the Part-B late-enrollment penalty plus a wait
  until the next General Enrollment Period in January–March with
  coverage starting July, a 3-9-month uncovered gap), Medigap-
  Guaranteed-Issue-window-coordination (Medigap GI is a one-time
  6-month window starting at Part-B effective date; delaying Part-B
  delays this clock — strategic for some, a trap for those who don't
  enroll in Medigap during GI and face underwriting later; see
  decision 8), spousal-coverage-and-domestic-partner-edge-cases (a
  spouse aging into Medicare while the other still works is the
  modal case; domestic-partner-coverage is NOT creditable for SEP
  purposes — IRS / SSA do not recognize the relationship for this
  rule; verify whenever non-marital partnership is the coverage
  source).
- **Sample situations**:
  - "Turning 65 in March, still working at a 500-person tech employer
    on their PPO. Plan to retire at 67. Skip Part B for 2 years —
    safe under SEP, or am I missing something on Part-D or Medigap
    timing?"
  - "Turning 65 in August on a 12-person small-business plan with
    excellent coverage; HR says I should keep their plan. But MSP
    rules — under-20 employees flips primary/secondary at 65. Hard
    enroll Part B regardless of what HR says?"

## 5. Marketplace silver vs bronze vs gold given subsidy-cliff math

- **Scope**: Person enrolling on the ACA Marketplace (HealthCare.gov
  or state-based exchange) — either at annual open enrollment, after
  a QLE, or as a self-employed / non-employer-covered consumer —
  choosing among metal tiers (bronze, silver, gold, platinum, and
  catastrophic for under-30 or hardship-exempt). Decision is
  distorted by two subsidy mechanics absent from employer plans:
  (a) the Advance Premium Tax Credit (APTC) calibrated to the
  second-cheapest-silver-plan ("benchmark silver") at the user's
  income, which subsidizes the dollar-cost-delta but not the
  category-quality-delta, and (b) the Cost-Sharing Reduction (CSR)
  silver-plan-only loading at 100–250% FPL, which dramatically
  lowers OOP-max only on silver-CSR-variant plans, often making
  silver-with-CSR strictly dominate gold for low-income enrollees
  (a structural anomaly that catches the financially literate who
  default to "richer is better"). Distinct from decision 3 (the
  decision to be on marketplace at all). Cross-routes `personal-
  finance` (MAGI calculation, projected-income vs prior-year-income
  arbitrage, year-end true-up reconciliation on Form 8962).
- **Framing-axes-covered**: APTC-benchmark-silver-math (you receive
  the dollar-amount-subsidy-keyed-to-benchmark-silver regardless of
  which plan you actually buy; therefore the marginal cost of going
  bronze vs silver is the full plan-quality-delta, NOT a
  proportional fraction; for high-income / no-subsidy enrollees the
  trade-off is undistorted), silver-CSR-loading-at-low-income-as-
  structural-anomaly (94/87/73 actuarial-value silver-CSR variants
  at 100-150 / 150-200 / 200-250% FPL respectively; below 200% FPL
  the silver-CSR-94/87 is effectively a near-platinum plan at a
  silver premium — silver strictly dominates gold; over-200% FPL
  the calculus shifts and gold may dominate if the user expects
  high utilization), ARPA-enhanced-subsidy-expiration-timeline (the
  ARPA / IRA enhanced subsidies that eliminated the 400%-FPL
  "subsidy cliff" expire end of 2025 absent further congressional
  extension; verify the current-year subsidy schedule before
  recommending — the cliff is back unless extended), projected-vs-
  prior-year-income-arbitrage-and-year-end-true-up (you predict
  next-year income at enrollment; APTC is reconciled on Form 8962
  at tax time — under-prediction means owing back; over-prediction
  means refund up to a cap; self-employed and equity-comp
  households are highest risk for true-up shocks; boundary
  `personal-finance`), network-narrowness-on-marketplace-vs-
  employer-plans (marketplace plans often have HMO-style narrow
  networks even at gold tier; verify in-network specialist and
  hospital availability — surprise narrow-network on a gold plan
  is a common regret), DACA-and-mixed-status-household-eligibility
  (DACA recipients were briefly APTC-eligible under 2024 rule;
  rule vacated late 2025; mixed-status households use a complex
  household-FPL calculation excluding undocumented members from
  numerator-coverage but including them in denominator-FPL —
  boundary `immigration`), catastrophic-plan-eligibility-under-30-
  or-hardship-exemption (catastrophic plans cover ACA EHBs but at
  bronze-minus actuarial value; minimum-coverage option for healthy
  young adults but NOT eligible for APTC).
- **Sample situations**:
  - "Self-employed, projected 2027 income $48k for household of 2.
    Marketplace shows silver at $180/mo and gold at $310/mo after
    APTC. Spouse has a chronic condition with $300/mo specialty
    drug. Silver-CSR vs gold — which dominates given our income is
    just under 250% FPL?"
  - "Recently retired at 62, living off taxable brokerage drawdowns.
    Want to MAGI-manage to qualify for max APTC. Bronze HDHP-style
    plan with HSA-eligibility for $80/mo after APTC vs silver-CSR
    at $20/mo. Which optimizes total tax-and-coverage outcome?"

## 6. Pre-tax FSA vs HSA vs dependent-care-FSA contribution sizing

- **Scope**: Employee with access to one or more pre-tax spending
  accounts at open enrollment, deciding contribution amounts. Common
  configurations: (a) HDHP enrollees with HSA-eligibility deciding
  HSA contribution (annual cap $4,300 self / $8,550 family for 2026,
  plus $1,000 55+ catch-up); (b) non-HDHP enrollees with healthcare
  FSA (annual cap $3,300 for 2026, employer-set; "use-it-or-lose-it"
  with $660 carryover OR 2.5-month grace period — not both); (c)
  parents of under-13 children with dependent-care FSA (annual cap
  $5,000 family / $2,500 if MFS, fully use-it-or-lose-it, no
  carryover); (d) limited-purpose FSA paired with HSA (HSA-compatible
  FSA for dental + vision only — extends pre-tax coverage without
  voiding HSA-eligibility). Distinct from decision 1 (HDHP-vs-PPO is
  the gate to HSA-eligibility) and decision 9 (HSA contribution
  timing — last-month rule). Cross-routes `personal-finance` (HSA-as-
  retirement-vehicle; dependent-care-FSA vs Child-and-Dependent-Care
  Tax Credit on Form 2441) and `family-planning` (dependent-care-
  FSA only applies for under-13-care-while-parent-works; eldercare
  is eligible if the parent is a tax-dependent).
- **Framing-axes-covered**: HSA-strict-dominance-over-FSA-when-
  HDHP-eligible (HSA dollars persist year-to-year, are portable
  across employers, can be invested in market funds inside the HSA,
  and remain available for medical at any age — strictly dominates
  FSA unless the user is FSA-only-eligible), dependent-care-FSA-vs-
  Child-and-Dependent-Care-Tax-Credit-coordination (the FSA reduces
  income on a sliding scale benefit based on marginal tax rate; the
  tax credit phases down with income — at higher incomes FSA wins,
  at lower incomes tax credit wins; coordinated election is
  required, both cannot be claimed on the same dollars), use-it-or-
  lose-it-and-2.5-month-grace-vs-660-carryover-mutual-exclusion
  (employer chooses one or the other but not both — verify SPD;
  many employees over-fund FSA and forfeit; pattern is well-known
  yet unfixed because the "free money" framing dominates the
  "forfeit risk" framing), limited-purpose-FSA-as-HSA-compatible-
  augment (LPFSA for dental + vision is HSA-compatible; can run
  alongside HSA without disqualification; useful for households
  with predictable dental/vision spend), domestic-partner-and-
  non-tax-dependent-eligibility-edge-cases (FSA covers IRS-qualified
  medical dependents only — domestic partners typically don't
  qualify even if on the health plan; verify before counting
  partner spend in FSA budget), QLE-and-mid-year-FSA-election-
  changes (FSA elections lock at open enrollment except for QLEs;
  HSA contributions can be changed any time during the year),
  prior-year-FSA-claims-submission-deadline (the 90-day-post-plan-
  year claims-submission deadline is independent of the 2.5-month
  grace; missed claims = forfeit even with otherwise-qualified
  receipts).
- **Sample situations**:
  - "Family of 4, both parents work, two kids in daycare at $1,800/
    month. Employer offers dependent-care FSA. Max out at $5,000 or
    reduce to keep some flexibility? And does that interact with
    the Child-and-Dependent-Care Tax Credit at our $180k income?"
  - "On HDHP with full HSA contribution maxed at $4,300. Employer
    also offers limited-purpose FSA. We spend ~$1,500/year on
    dental and vision combined. Worth electing LPFSA, or just pay
    OOP and use the HSA later?"

## 7. ACA marketplace vs short-term limited-duration vs healthcare-sharing ministry

- **Scope**: Person without employer coverage and not yet Medicare-
  eligible, evaluating ACA-compliant marketplace coverage against
  ACA-noncompliant alternatives: (a) short-term limited-duration
  insurance (STLDI — under the 2024 final rule, capped at 4 months
  initial + 1-month renewal; prior rule allowed 36 months — verify
  current rule), (b) Christian healthcare-sharing ministries
  (Samaritan, Christian Healthcare Ministries, Medi-Share, OneShare
  Health — explicitly not insurance, regulated under separate state
  rules, member fees rather than premiums, "shareable" rather than
  "covered" medical expenses), (c) farm bureau membership-based
  coverage (TN, IA, KS, NE — exempt from ACA in their states,
  underwritten and capped), (d) direct primary care (DPC)
  membership + catastrophic stop-loss (a recent retail trend
  combining a $50–150/month DPC subscription with a high-deductible
  catastrophic plan). Distinct from decision 5 (metal-tier within
  ACA marketplace). The decision is fundamentally a risk-transfer-
  vs-self-insurance question with strong moral-hazard and adverse-
  selection dynamics — many ACA-noncompliant alternatives look
  attractive premium-wise but exclude or cap pre-existing
  conditions, lack EHB coverage (no maternity, no mental health,
  often no prescription drug), and lack the ACA OOP cap (a single
  catastrophic event can wipe out a year of premium savings several
  times over).
- **Framing-axes-covered**: pre-existing-condition-exclusion-and-
  post-claim-rescission-risk (ACA-noncompliant plans can underwrite,
  exclude, rescind on technical application errors, or "share" /
  cover only the conditions that arose strictly after enrollment;
  ACA-compliant plans cannot do any of this — this is the central
  protection of the ACA), EHB-coverage-gap-on-non-ACA-plans (no
  maternity coverage on STLDI is the most common surprise — the
  unplanned pregnancy + STLDI combination is a known six-figure-OOP
  trap), OOP-cap-presence-vs-absence (ACA-compliant: $9,200 self /
  $18,400 family for 2025; STLDI and sharing ministries: no OOP
  cap or a very high one — a single cancer diagnosis on STLDI can
  exhaust the policy limit and dump the patient into uncompensated-
  care or back to marketplace at the next SEP), premium-and-
  member-fee-arithmetic-with-and-without-subsidy (the headline
  $300/month sharing ministry vs $200/month subsidized silver
  comparison flips entirely when APTC enters; the comparison only
  favors alternatives when subsidies don't apply, i.e. higher-
  income or self-employed with non-MAGI-counting income),
  healthcare-sharing-ministry-religious-eligibility-and-lifestyle-
  requirements (statements of faith, sobriety / sexuality / lifestyle
  attestations are part of the contract; non-compliance is grounds
  for non-share; not just a paperwork formality), STLDI-renewability-
  cap-as-bridge-only (current 4-month rule means STLDI is genuinely
  only useful as a sub-6-month bridge to marketplace SEP or new
  employer plan; not a year-round option under current rule —
  rule can change; verify), direct-primary-care-as-augment-not-
  substitute (DPC is fine for primary care and many urgent issues
  but does not cover hospitalization, specialty drugs, or
  emergency surgery — the catastrophic-stop-loss combo can work
  but the catastrophic plan must itself be ACA-compliant or you've
  taken on the OOP-uncapped tail risk).
- **Sample situations**:
  - "Self-employed consultant, projected income $180k household,
    no APTC eligible. Marketplace gold = $2,200/mo family;
    Christian sharing ministry = $700/mo family. Healthy family
    of 4. Save $18k/year on sharing ministry — what's the catch?"
  - "Sabbatical year planned March–December. Need coverage 9 months
    before new job starts. STLDI for 4 months bridges March–June;
    what about July–December? Stack STLDI plans or marketplace?"

## 8. Original Medicare + Medigap + Part D vs Medicare Advantage at initial enrollment

- **Scope**: Person at age 65 (or earlier with disability or ESRD)
  during their Initial Enrollment Period choosing between (a)
  Original Medicare (Parts A + B) plus a Medigap supplement (Plan
  G or N, occasionally F for those eligible before 2020) plus a
  standalone Part D prescription drug plan, vs (b) Medicare
  Advantage (Part C), an all-in-one private plan replacing
  Original Medicare. Decision is one-time-with-permanent-consequence
  in a way most insurance decisions are not: the Medigap
  Guaranteed-Issue (GI) window is 6 months from Part B effective
  date during IEP; outside it, switching from MA back to Original-
  Medicare-plus-Medigap requires medical underwriting and can be
  denied or rated-up (some states — NY, CT, ME, MA — offer
  year-round or annual GI; verify the user's state). Cross-routes
  `personal-finance` (HSA spending in retirement for Medicare
  premiums is qualified medical use — HSA Part-B / Part-D / Medigap
  premiums in retirement is one of the highest-ROI uses of HSA
  dollars).
- **Framing-axes-covered**: Medigap-GI-as-one-time-irreversible-
  window (the 6-month GI clock starts at Part B effective date;
  outside it, underwriting denies common conditions — diabetes
  with complications, recent cancer, etc; choosing Medicare
  Advantage at IEP without securing Medigap first is the
  no-going-back trap; secondarily, some MA plans offer "trial
  rights" of 12-month return-to-Original-with-GI but only if you
  enrolled in MA at IEP and try it within first year — verify),
  network-narrowness-MA-vs-any-doctor-Medicare (Original Medicare
  + Medigap accepts any provider that accepts Medicare —
  effectively any US physician; MA HMO / PPO networks are county-
  based and can drop providers mid-year; cancer-center-of-
  excellence access is the marquee differentiator at diagnosis
  time), prior-authorization-burden-MA-vs-Original (MA plans
  require prior-auth for many services; Original Medicare requires
  it for almost none — this is the procedural-friction axis MA
  plans minimize in their marketing), MA-extra-benefits-vs-
  hidden-trade-offs (dental, vision, hearing, gym, transportation,
  OTC allowance — common MA "extras" that don't exist in
  Original; but cost-sharing on actual major medical events is
  often worse than Medigap-G; the framing inversion where
  consumers anchor on extras-loss instead of major-event-coverage
  is well-documented), Part-D-coverage-and-formulary-tier-
  selection (Part-D plans are separate from Medigap; choose
  annually during AEP; verify the user's specific drugs are on
  formulary at each plan; the $2,000-OOP-cap from IRA 2025 is
  important context), travel-and-snowbird-coverage-MA-vs-Medigap
  (MA HMOs typically only cover non-emergency care in-network in
  their county; Medigap follows the user anywhere Medicare
  accepted — material for retirees who travel or relocate),
  state-by-state-Medigap-GI-rules (NY, CT, MA, ME offer annual or
  continuous GI — switching MA-to-Medigap is open year-round; CA
  and OR have "birthday rule" annual GI windows; most states have
  IEP-only — verify before recommending any reversal strategy),
  end-of-life-and-hospice-coverage-mechanics (Medicare hospice
  benefit applies even in MA; but the network-and-prior-auth
  burden of MA continues to apply outside hospice, which can
  fragment late-life care).
- **Sample situations**:
  - "65, retiring in 6 months, no significant conditions. Local
    MA plan has $0 premium, dental, gym — sounds too good. Or
    Original Medicare + Plan G at $180/month + Part D. Father
    had cancer treated at MD Anderson out-of-state. Which?"
  - "67, currently on MA plan after IEP enrollment. Need
    surgery at a center-of-excellence the plan doesn't network
    with. Can I switch to Original Medicare + Medigap for next
    year, or is underwriting going to deny given my chronic
    conditions?"

## 9. HDHP enrollment timing and HSA last-month rule contribution sizing

- **Scope**: Person enrolling in an HDHP mid-year (job change, QLE
  marriage / divorce / birth, open-enrollment for non-calendar
  fiscal-year plans), deciding HSA contribution amount given
  the proration rules: by default HSA contribution is prorated to
  months of HDHP coverage (e.g. 6 months of HDHP = half the cap),
  BUT the "last-month rule" lets a person who is HSA-eligible on
  December 1 contribute the full annual amount — at the cost of a
  13-month testing-period requirement (must remain HSA-eligible
  the entire following year, or face income recapture plus 10%
  penalty on the over-contribution). Distinct from decision 1
  (HDHP-vs-PPO choice itself) and decision 6 (HSA-vs-FSA
  contribution sizing within a stable plan year). Cross-routes
  `personal-finance` (the testing-period failure scenario hits
  taxpayers who change jobs the following year and lose HSA-
  eligibility — the income recapture is on the prior-year tax
  return, requiring amended 1040 plus penalty).
- **Framing-axes-covered**: last-month-rule-as-real-option-with-
  contingent-tax-liability (December-1-eligibility unlocks the
  full annual contribution; the contingent-liability framing is
  more accurate than the "tax bonus" framing many employers use
  in onboarding — the option has positive value if you expect to
  remain HSA-eligible, negative if not), 13-month-testing-period-
  failure-modes-and-recapture-math (failure = ordinary income
  on the over-contributed portion plus 10% penalty on the failed
  amount; payable on the prior-year return via amended 1040;
  failure triggers: job change to non-HDHP plan, marriage onto
  spouse's non-HDHP family plan, Medicare enrollment, FSA-overlap
  via spouse's general-purpose FSA, etc), proration-default-as-
  safe-floor (contributing prorated-only is always safe regardless
  of next-year plan status; this is the default if uncertain),
  spouse-family-tier-coordination (when both spouses are HSA-
  eligible the family limit is shared; the last-month rule applies
  per-person and is asserted on the family limit, not duplicated),
  mid-year-disqualification-event-handling-without-last-month-rule
  (when last-month rule is NOT used, mid-year disqualification
  simply caps that year's contribution at prorated amount; no
  testing period or penalty), COBRA-and-HSA-eligibility-
  continuation (electing HDHP-COBRA after layoff preserves
  HSA-eligibility provided COBRA-HDHP-coverage continues; many
  miss this), HSA-and-Medicare-mutual-exclusion-and-6-month-
  retroactive-Part-A (enrolling in Medicare voids HSA eligibility
  prospectively; SS-claiming triggers Part-A retroactively up to
  6 months — stop HSA contributions 6 months before SS-claim if
  delayed past 65; boundary `personal-finance`).
- **Sample situations**:
  - "Starting new job July 1 with HDHP. Was on non-HDHP first
    half of year (no HSA). Last-month rule lets me contribute
    the full $4,300 vs prorated $2,150. Plan to stay through
    next year. Worth the testing-period commitment, or stick to
    prorated?"
  - "Used last-month rule last December for full HSA. Now
    considering accepting a job offer that has only PPO option
    (no HDHP). Mid-March job-change — what does the testing-
    period failure cost me, and can I structure around it?"

## 10. Embedded vs aggregate family deductible and OOP-max sub-limits

- **Scope**: Family-tier enrollee in any health plan with family
  coverage, understanding how deductible and out-of-pocket maximum
  apply across multiple covered members. Decision-relevance is
  highest at plan-selection time (decision 1) — the deductible
  and OOP-max structure matters more than the headline numbers —
  but the framing is also load-bearing when responding to claims
  questions mid-year or evaluating whether to add a dependent
  (decision 2). Three structures to distinguish: (a) aggregate
  family deductible — no one member's care counts toward
  individual deductible-met until the entire family deductible is
  met by combined spend (worst when one member has heavy
  utilization and others are healthy), (b) embedded individual
  deductible within family — each member has an individual
  deductible cap (typically family / 2) at which point that
  individual's care is covered; family aggregate also applies, (c)
  ACA-mandated embedded individual OOP-max sub-limit — under ACA,
  every plan with family coverage must include an embedded
  individual OOP-max equal to the self-only OOP-max for that
  year, even if the family OOP-max is higher (a 2016 ACA rule
  many older plan-comparison tools still miss). Distinct from
  decision 1 (which plan) and decision 6 (FSA / HSA sizing).
  Cross-routes `family-planning` (the embedded individual OOP-max
  is the binding constraint when one family member has a serious
  diagnosis and others are healthy).
- **Framing-axes-covered**: aggregate-vs-embedded-family-deductible-
  asymmetric-utilization-risk (aggregate is worst when utilization
  is concentrated in one member — the high-utilizer must spend the
  full family deductible before anything covers; embedded caps the
  per-person exposure), ACA-embedded-individual-OOP-max-as-floor
  (the 2016 ACA rule requires every family plan to have an embedded
  individual OOP-max ≤ self-only OOP-max — no family plan can
  legally expose one individual to more than the self-only OOP-max,
  even if the family OOP-max is higher; many older spreadsheet
  comparisons miss this), prescription-drug-OOP-tracking-separate-
  vs-combined (some plans track prescription OOP separately from
  medical, with separate caps — verify on each plan), HRA-and-
  employer-deductible-coverage (some employers add Health
  Reimbursement Arrangements that cover the first chunk of the
  deductible — the "true" deductible to the employee is lower
  than the plan document states; ALWAYS surface this when
  comparing plans), dependent-coverage-age-26-and-tax-dependency-
  decoupling (ACA allows children to age 26 regardless of tax-
  dependent status; useful for young-adult-children who file
  their own taxes — they remain on parents' plan but the
  individual OOP-max applies to them as embedded individual),
  newborn-coverage-30-day-QLE-window-and-retroactive-effective
  (birth is a QLE — newborn must be enrolled within 30 days but
  coverage backdates to date of birth on most plans; failure
  triggers a coverage gap and out-of-pocket exposure for the L&D
  bills, which are billed in the newborn's name not the parent's
  — distinct from the maternity bills which are in the parent's
  name), divorce-and-mid-year-family-tier-disenrollment (divorce
  is a QLE; the embedded individual deductible-met / OOP-met for
  the disenrolled spouse generally does NOT transfer to their new
  individual plan — they start over at $0; consider mid-treatment
  divorce-timing-relative-to-deductible-met-status, an
  underappreciated framing axis at high-OOP-met points; boundary
  `family-planning` and `legal-disputes`).
- **Sample situations**:
  - "Family plan with $6,000 family deductible. One kid needs
    surgery costing $40,000 in February. Aggregate plan vs
    embedded plan — what's the actual OOP exposure difference?
    Plan documents are ambiguous; how to verify which structure
    applies?"
  - "Divorcing mid-year, was on spouse's family plan and met
    $4,500 of $5,000 individual embedded OOP via cancer treatment.
    Moving to my employer's plan via QLE. Does my OOP-met
    transfer, or am I back to $0 with my new plan's deductible
    on the next chemo cycle?"

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the
  axes above cluster into ~10–12 reusable framings — expected-
  utilization-vs-OOP-max arithmetic, HSA-as-triple-tax-advantaged-
  retirement, employer-premium-subsidy-asymmetry, QLE-and-SEP-
  clock-management, ACA-marketplace-subsidy-mechanics (APTC + CSR
  silver-loading), Medicare-enrollment-irreversibility (IEP / SEP /
  GE / Medigap GI), ERISA-and-self-funded-plan-procedural-posture,
  pre-existing-condition-protection-vs-ACA-noncompliant-alternative,
  network-narrowness-and-prior-authorization-burden, embedded-vs-
  aggregate-cost-sharing-structures, spousal-and-dependent-coverage-
  coordination, end-of-coverage-continuity-vs-deductible-reset.
- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  decisions 3, 4, 5, 7, 8 are highest-density — COBRA-vs-marketplace
  retroactive-election timing arithmetic (3), Medicare Part-B SEP
  clock and HSA-eligibility-loss-on-Part-A-retroactive (4), silver-
  CSR loading anomaly at low-income (5), ACA-noncompliant
  alternative pre-existing-condition / OOP-cap absence as
  catastrophic-event trap (7), and the one-time Medigap GI window
  with permanent underwriting consequences (8). Decisions 4 and 8
  carry the highest single-misstep tail risk per ROADMAP §5
  Mechanism E and warrant the most explicit SHIBA / Medicare-
  counselor referral. Decision 7 carries the highest information-
  asymmetry-driven harm risk — the headline premium savings are
  real, the contingent uncovered-tail-risk is invisible until
  claim time.
- **Cross-domain edges**: 1, 2, 3 boundary `tech-career` (employer
  coverage as comp component; layoff-driven coverage transition;
  job-change deductible-reset trap); 3, 5, 8 boundary `immigration`
  (lawful-presence requirements for APTC and Medicare; mixed-status
  household FPL calculation; DACA marketplace eligibility status);
  1, 6, 9 boundary `personal-finance` (HSA as retirement vehicle;
  FSA-vs-tax-credit coordination; HSA last-month-rule recapture
  math); 2, 4, 10 boundary `family-planning` (spouse coverage
  coordination; spouse-aging-into-Medicare; dependent-coverage and
  newborn QLE; divorce mid-treatment); 3, 8, 10 boundary
  `legal-disputes` (ERISA pre-emption of state remedies in denial
  appeals; mini-COBRA state extensions; divorce mid-treatment
  procedural rights). Edges are documentation; routing is V2-Triage's
  job.
- **High-stakes posture** (uniform with selective referral
  category): `health-insurance` is `high_stakes: true` per
  `_meta_ontology.md` §4, but the appropriate professional category
  varies sharply by decision. The Editor layer should NOT
  default-defer every decision to a single "consult a professional"
  category. Selective referral:
  - **Licensed health insurance broker** for decisions 1, 2, 5
    (commercial / marketplace plan selection where broker compensation
    is carrier-paid; surface the carrier-paid-vs-fee-only distinction
    when broker bias matters — e.g. comparing Medicare Advantage
    plans is where broker-incentive-distortion is most acute).
  - **SHIBA / SHIP volunteer** for decisions 4 and 8 (Medicare-side
    decisions specifically; federally funded, free, conflict-free).
  - **Marketplace Navigator or in-person assister** for decisions 3,
    5, 7 (APTC eligibility and enrollment specifically; plan-agnostic,
    CMS-trained, prohibited from steering — the gold-standard
    referral for marketplace navigation, underutilized because the
    program is less publicized than broker channels).
  - **CPA** for decisions 6, 9 (HSA last-month-rule testing-period
    recapture and FSA-vs-Child-Care-Tax-Credit coordination both
    require Form 8889 / Form 2441 mechanics; boundary
    `personal-finance`).
  - **ERISA-litigation attorney** for decisions 3, 8, 10 when
    denial-of-claim or denial-of-appeal escalates into six-figure
    dispute under a self-funded employer plan (boundary
    `legal-disputes` — state-insurance-commissioner remedies are
    ERISA-preempted, which constrains both procedural posture and
    damages availability).
  - **State Insurance Commissioner consumer-assistance** for any
    fully-insured (non-self-funded) commercial-plan dispute — free,
    state-funded, faster than ERISA-attorney route for
    sub-six-figure disputes.

  The posture remains "decision-support, not licensed-broker
  advice"; the Editor surfaces the appropriate specific category
  inline rather than blanket-mandating one on every decision. Over-
  referral degrades signal; under-referral creates harm. The
  selective enumeration above is the calibration.
