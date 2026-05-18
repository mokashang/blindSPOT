# health-insurance — framings.md (Layer 2)

Framing library for `health-insurance`. Each entry names one lens — the
way a specific community / tradition / profession argues about a
decision — and lists the decisions from
[`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

The `health-insurance` domain is **high_stakes: true** per
[`_meta_ontology.md` §4](../_meta_ontology.md). Mechanism E gating
applies (per [ROADMAP §5](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)):
this file names *axioms and trade-offs the enrollee must reason about*,
not coverage determinations. Every framing below is a decision-support
pointer — the binding determination on any specific case comes from a
licensed broker, SHIBA / SHIP volunteer, Marketplace Navigator, CPA, or
ERISA-litigation attorney with case-specific facts (current Summary
Plan Description, the user's claim history, the current Visa Bulletin–
equivalent for ACA — Healthcare.gov regulatory posture and CMS / IRS
revenue rulings — and the user's full medical / income picture). Where
a framing names a statute, rule, or threshold (ACA §1302 EHB, IRC §223
HSA, 26 CFR §54.4980G, SSA Title XVIII, INA §245(a) — yes, immigration
status enters here too), treat the citation as a pointer to where the
analysis happens, not as the answer.

Two distinct classes of irrevocability drive the high-stakes posture
and shape every framing below: the **12-month plan-year lock-in** on
commercial / marketplace plans (outside annual open enrollment or a
narrow Qualifying-Life-Event window, the wrong choice compounds for up
to a year of uncapped out-of-network exposure), and the **permanent
Medicare-side penalty** regime (Part B 10%-per-12-months-late
permanent premium add; Medigap Guaranteed-Issue window expires 6
months after Part B effective date, after which underwriting denies
common chronic conditions). Framings that handle one of these well
often miss the other; opposing-framing pairs below frequently divide
along the commercial / Medicare boundary.

Voice anchors (conceptual, not source URLs — those live in
`sources.yaml` once authored): **actuarial-and-broker voice**
(expected-value calculation across utilization scenarios, premium-vs-
OOP-max-vs-network arithmetic, NAIC standardized Medigap plan
literacy); **SHIBA / SHIP volunteer / Medicare counselor voice**
(non-commissioned, plan-agnostic Medicare-enrollment guidance — the
gold-standard referral for D4 and D8 specifically; State Health
Insurance Assistance Program is federally funded under SSA §4360);
**ACA Navigator / in-person assister voice** (CMS-trained, prohibited
from steering, APTC and CSR mechanics, subsidy-cliff arithmetic);
**HSA-administrator voice** (HealthEquity / Fidelity / Lively style;
IRS Form 8889, last-month-rule testing-period mechanics, qualified-
medical-expense scoping, investment-threshold mechanics inside the HSA);
**ERISA-attorney voice** (self-funded vs fully-insured distinction,
state-insurance-commissioner-remedy pre-emption, 29 USC §1132 civil
enforcement, *Firestone* deference standard for plan-administrator
discretion, claim-and-appeal procedural rights under 29 CFR §2560.503);
**healthcare-economics-journalist voice** (Sarah Kliff at NYT, Julie
Rovner at KHN, Margot Sanger-Katz, Charles Ornstein at ProPublica —
denial / surprise-billing / claim-investigation reporting, structural
market-failure analysis, narrative grounding of edge cases);
**Bogleheads-meets-health-insurance voice** (HSA as the most
tax-advantaged retirement account in the IRC, dollar-cost-averaging
the HSA investment, "spend OOP, let HSA compound" as the dominant
strategy); **employer-benefits / HR-Reddit voice** (r/humanresources,
r/personalfinance benefits-megathread style — practical-OE-week
calculus, FSA timing, dependent-care-FSA-vs-credit coordination);
**ACA-reform-academic voice** (Kaiser Family Foundation / KFF, Health
Affairs blog, Brookings Center on Health Policy — subsidy-design
analysis, market-stabilization argument, mixed-status household FPL
calculation); **single-payer / Medicare-for-all advocate voice**
(Physicians for a National Health Program, Public Citizen — fundamental
critique that frames every commercial-plan decision as second-best,
introduces "you shouldn't have to think about any of this" as a
meta-framing); **patient-advocate / billing-error-recovery voice**
(NAHAC, AdvoConnection — EOB-reading, balance-billing recovery, No
Surprises Act §2799A enforcement, IDR arbitration mechanics);
**conservative health-policy voice** (Galen Institute, AEI — HSA-
maximalism, catastrophic-only-plans, healthcare-sharing-ministry
adjacent, market-mechanism faith); **disability / chronic-illness
patient voice** (r/ChronicIllness, r/Disability — claim-denial-and-
appeal-as-norm, prior-auth procedural literacy, ERISA-attorney
familiarity, formulary-tier reality).

Cross-domain edges: D1, D2, D3 boundary `tech-career` (employer plan
as comp component; layoff-driven coverage transition; benefits
differential at job change); D3, D5, D8 boundary `immigration`
(lawful-presence requirements for APTC and Medicare; mixed-status
household FPL math; DACA marketplace eligibility status under post-
2025-vacatur regulatory posture); D1, D6, D9 boundary
`personal-finance` (HSA as the most tax-advantaged retirement vehicle;
FSA-vs-Child-Care-Tax-Credit coordination; HSA last-month-rule
recapture math under amended 1040); D2, D4, D10 boundary
`family-planning` (spouse-coverage coordination, spouse-aging-into-
Medicare, dependent-coverage and newborn QLE, divorce mid-treatment);
D3, D7, D8, D10 boundary `legal-disputes` (ERISA pre-emption of state
remedies in denial appeals; mini-COBRA state extensions; healthcare-
sharing-ministry contract vs insurance regulation; divorce
mid-treatment procedural rights). Routing across edges is V2-Triage's
job; these edges help framings name adjacent domains rather than
absorb their content.

---

## 1. Expected-utilization-arithmetic framing

- **Decisions it applies to**: D1 (HDHP / PPO / HMO at OE), D5
  (Marketplace metal-tier given APTC + CSR), D6 (FSA / HSA / dep-care
  FSA sizing), D10 (Embedded vs aggregate family deductible).
- **Mental model summary**: A health plan is an actuarial bundle —
  premium, deductible, copay / coinsurance schedule, out-of-pocket
  maximum, network breadth — and the right plan minimizes
  expected-plus-tail total cost across plausible utilization
  scenarios. The framing reasons in scenario terms: low-utilization
  case (well-visits + 1 minor illness), expected-utilization case
  (chronic-disease maintenance + 1 procedure), high-utilization tail
  (major surgery, cancer dx, complicated pregnancy, premature birth).
  Each plan's total annual cost differs across scenarios — the HDHP
  often wins at low and high utilization (low premium captures the
  expected-case savings; OOP-max caps the tail), the PPO often wins
  in the messy middle. Characteristic move: build a 3-scenario table
  with premium, deductible-met, OOP-max-met, and pick the plan that
  minimizes the probability-weighted cost — or, when scenario
  probabilities are unclear, the plan whose worst-case is tolerable.
  Anchor numbers: 2026 HSA-eligible HDHP minimum deductible $1,650 /
  $3,300; HDHP OOP-max ceiling $8,300 / $16,600; ACA marketplace
  OOP-max ceiling $9,450 / $18,900; embedded individual OOP-max sub-
  limit cannot exceed self-only OOP-max.
- **Characteristic vocabulary**: "actuarial value", "metal tier",
  "deductible-then-coinsurance", "OOP-max as the real worst-case",
  "premium-vs-deductible trade-off", "scenario table", "expected
  utilization vs tail utilization", "embedded individual OOP-max
  sub-limit", "copay-vs-coinsurance asymmetry", "in-network vs
  out-of-network OOP-max separation."
- **Excludes**:
  - Treats utilization as scalar; misses that *who* utilizes within a
    family changes the embedded-individual-OOP-max calculation
    materially. A $40k surgery on the high-utilizing child caps at
    the embedded individual OOP-max (~$9,450 self-only ceiling) on
    an embedded plan, but on an aggregate-deductible plan that same
    family must spend the full family deductible across all members
    before anything covers — the arithmetic looks identical until
    you read the SPD carefully. Opposes F11.
  - Out-of-network OOP-max is structurally absent from the framing's
    scenario tables; many HMOs / EPOs / narrow-network silvers have
    *no* out-of-network OOP-max at all (you eat the entire bill if
    care is out-of-network and not an emergency under No Surprises
    Act protections), and the "tail is capped" reassurance evaporates
    when in-network specialist availability is thin.
  - Prescription-drug benefits sit in a parallel cost track on many
    plans — separate deductible, separate copay structure, separate
    specialty-tier formulary, and on a non-trivial number of plans a
    *separate* OOP-max specifically for prescription costs. The
    framing's "the plan covers everything once OOP-max is met" is
    materially wrong for the specialty-drug / biologic patient whose
    $10k/month medication continues to copay-tier after the medical
    OOP-max is hit.
  - Probability weights for scenarios are calibrated from prior
    utilization — but the framing under-prices *condition onset
    risk* (the 35-year-old with no chronic disease may be a 36-year-
    old with one, and the OE-locked-in HDHP becomes the wrong choice
    only after diagnosis closes the rescue door); the scenario table
    is a static snapshot of a dynamic process.

## 2. Risk-transfer-and-OOP-cap framing

- **Decisions it applies to**: D1 (HDHP / PPO / HMO), D3 (COBRA vs
  marketplace), D7 (ACA-compliant vs STLDI / sharing ministry), D10
  (Embedded vs aggregate family deductible).
- **Mental model summary**: Insurance is risk-transfer; the question
  is not "what is my expected annual spend" but "what is the maximum
  uncovered exposure to a single catastrophic event, and can I
  absorb it." The framing reasons in OOP-cap-presence-and-magnitude
  terms: ACA-compliant plans have a statutory OOP cap on essential
  health benefits ($9,450 self-only / $18,900 family for 2026, indexed
  annually); STLDI and healthcare-sharing-ministry "coverage" has no
  OOP cap or a very high one; international expat plans differ; HMOs
  have a separate in-network-only OOP-max (no out-of-network cap). A
  single major medical event — cancer, complex pregnancy, premature
  birth, cardiac event, organ transplant — generates $200k–$2M in
  medical charges and is the load-bearing scenario for the choice.
  Characteristic move: ignore premium headlines first, compute the
  catastrophic exposure on each option, then layer premium and
  expected utilization as secondary. Anchor: ACA OOP cap is the
  central protection; absence-of-cap is the central red flag.
- **Characteristic vocabulary**: "out-of-pocket maximum", "tail
  risk", "catastrophic event", "single-event exposure", "ACA EHB
  OOP cap", "no OOP cap", "100% coinsurance after OOP-max"
  (i.e. covered in full — what the OOP-max *means*),
  "balance-billing exposure", "stop-loss point", "uninsured
  bankruptcy adjacency."
- **Excludes**:
  - The ACA OOP cap applies only to in-network EHB-classified care;
    out-of-network specialty care, non-EHB services (LASIK, some
    fertility procedures, cosmetic-adjacent), and balance-billing
    on emergency air-ambulance / out-of-network anesthesia or
    pathology (despite No Surprises Act protections, edge cases
    persist for ground ambulance and certain free-standing
    facilities) sit outside the OOP-max for many plans. The
    framing's "ACA caps your downside at $9,450" is reassuring
    until the asker hits an excluded service-class. Opposes F1
    when one over-relies on the OOP-max as scalar.
  - Treats the OOP-max as a per-calendar-year reset that's a clean
    insurance event; misses that the *clock-reset* (Jan 1 deductible
    reset) is itself a planning event — the patient mid-treatment
    in December whose chemo-induced labs run weekly may pay
    $300/visit out-of-pocket all of January even though the
    November tax-year-prior labs were $0-cost-after-OOP-max.
  - The "absorb the catastrophic exposure" framing routes high-
    income, high-asset askers toward HDHP + self-insurance for the
    sub-OOP-max gap (e.g. "$8k deductible is rounding error on
    $500k net worth"); the framing rarely asks whether asset-
    composition matters — illiquid 401k, locked-up equity grants,
    or home equity is harder to deploy for a $50k surprise bill
    than the cash-on-balance-sheet picture suggests. Opposes F8.
  - Underweights the *psychological* tail risk — even for askers
    with capacity to absorb a $9,450 hit, the cognitive load of
    a months-long claim/appeal/billing-error grind during a
    cancer-recovery phase is itself a cost the framing's pure-
    dollar arithmetic ignores. The chronic-illness-patient voice
    catches this; the actuarial-broker voice doesn't.

## 3. HSA-as-retirement-vehicle framing

- **Decisions it applies to**: D1 (HDHP / PPO / HMO — HDHP gates
  HSA-eligibility), D6 (FSA / HSA / dep-care FSA sizing), D9 (HSA
  last-month-rule timing).
- **Mental model summary**: An HSA is the most tax-advantaged
  account in the US tax code — triple-tax-advantaged (pre-tax
  contribution, tax-free growth, tax-free withdrawal for qualified
  medical), no required minimum distributions, no income-cap on
  contributions (unlike Roth), portable across employers, and
  inheritable to a spouse without ordinary-income recognition. The
  framing reasons in long-horizon-compounding terms: HSA dollars
  invested for 30+ years inside a low-cost index fund grow to
  $250k–$500k per person on max contributions, and qualified
  medical expenses in retirement (Medicare premiums, Medigap,
  Part D, dental, vision, LTC up to IRS-published limits — all
  qualify) absorb that growth tax-free. The strategy is "fund the
  HSA to the cap; pay current medical OOP from taxable accounts;
  let the HSA compound." Characteristic move: choose HDHP at OE
  even when a PPO would have lower expected medical cost, because
  the long-run HSA tax arbitrage strictly dominates short-run
  premium savings on the PPO. Anchor: HSA cap $4,300 self / $8,550
  family for 2026, plus $1,000 55+ catch-up.
- **Characteristic vocabulary**: "triple-tax-advantaged",
  "HSA-as-retirement", "pay OOP and let HSA compound",
  "shoebox the receipts" (track historical qualified-medical
  spend, reimburse decades later tax-free), "IRC §223", "Form
  8889", "qualified medical expense", "Medicare-premium HSA
  qualified use", "HSA investment threshold" (the per-employer
  minimum cash balance required before allowing market
  investment — typically $1k–2k), "post-65 non-qualified
  withdrawal as ordinary-income-but-no-penalty."
- **Excludes**:
  - The "pay OOP, let HSA compound" strategy assumes the asker has
    sufficient taxable savings to fund current medical without
    raiding the HSA; for askers with cash-flow constraints (early-
    career, paying down debt, single-income household with kids),
    the prescription is correct in theory and infeasible in
    practice, and the framing rarely degrades-gracefully to "if you
    can't bank the receipts, just use the HSA for current spend —
    you still get the tax deduction." Opposes F4 (immediate-spend).
  - The "shoebox the receipts" decades-deferred reimbursement
    requires holding receipts, EOBs, and proof-of-non-reimbursement
    for 20+ years against potential IRS audit; the practical
    record-keeping burden is non-trivial, and most HSA
    administrators don't archive this; the framing's "just save the
    receipts" understates the operational cost.
  - HSA-eligibility is fragile: any non-HDHP coverage (general-
    purpose FSA, spouse's FSA, Medicare Part A, VA care within
    prior 3 months, Tricare, primary-care services via DPC that
    aren't structured as ancillary) disqualifies the asker from
    contributing — and Medicare Part A enrollment is *retroactive
    up to 6 months* when SS-claiming after 65, which silently
    invalidates 6 months of HSA contributions the framing's "max
    until SS-claim" timing doesn't catch. Boundary
    `personal-finance`.
  - The retirement-vehicle framing assumes the asker reaches
    retirement having accumulated medical expenses to reimburse
    against; for an asker with major medical events in their 30s
    and 40s, the optimal play may be reimburse-as-you-go rather
    than shoebox — the tax-free withdrawal is identical, the
    compounding lost is real, and the framing's bias toward
    deferral can be myopic for asker-specific health trajectories.

## 4. Immediate-cost-and-cash-flow framing

- **Decisions it applies to**: D1 (HDHP / PPO / HMO), D3 (COBRA vs
  marketplace), D6 (FSA / HSA sizing), D7 (ACA vs STLDI / sharing
  ministry).
- **Mental model summary**: For the asker living paycheck-to-
  paycheck or with no savings buffer, the binding constraint is
  monthly cash flow, not annual expected cost or tail risk. A
  $200/month premium delta is real; a $4,000 deductible is
  hypothetical until it isn't, and at that point the framing's
  default is "negotiate the bill" or "set up a payment plan" rather
  than pre-fund the exposure. The framing reasons in payroll-
  deduction and grocery-budget terms: what is the smallest reliable
  premium that gives me a network at all, what gets me into a
  primary-care visit without a copay surprise, what is the FSA
  contribution that returns to me as predictable in-year spending
  rather than locked-up retirement. Characteristic move: pick the
  HMO or low-PPO with copay-not-coinsurance structure even when the
  HDHP+HSA arithmetic strictly dominates on long-run after-tax IRR;
  decline FSA over-funding in favor of holding the cash; pick
  marketplace silver-CSR over gold when the premium difference is
  the difference between coverage and skipped coverage.
- **Characteristic vocabulary**: "monthly premium I can stomach",
  "copay-not-coinsurance for the predictability", "skipping care
  to save the copay", "deductible is hypothetical until it isn't",
  "FSA forfeiture vs cash-on-hand", "subsidized silver-CSR is the
  point", "marketplace as floor not ceiling", "drug-formulary
  cost-at-counter", "the dental bill that wasn't budgeted."
- **Excludes**:
  - The framing's premium-minimization bias routes askers into
    plans with high deductibles AND high cost-sharing-after-
    deductible (silver-bronze gap) where the structural design
    *expects* enrollee skipping-of-care to balance the actuarial
    pool — the well-documented "underinsurance" pattern where the
    formally-insured nonetheless face medical debt. Opposes F2, F3.
  - "Skipping care to save the copay" is rational at the monthly-
    budget level and catastrophic at the chronic-condition level —
    the framing has no native vocabulary for the diabetes /
    hypertension / depression patient whose foregone primary care
    converts to ER visit + admission six months later (the "moral
    hazard in reverse" pattern). The patient-advocate voice
    catches this; the cash-flow voice doesn't.
  - The marketplace-as-floor framing under-weights *coverage
    gaps* during the marketplace SEP / OE transition windows; the
    asker who picks the cheapest silver-CSR mid-year via SEP and
    then experiences premium increase at year-end OE may not
    re-evaluate, treating the prior choice as locked-in even though
    OE is the chance to reassess against the prior year's actual
    utilization.
  - Predictable monthly cost as the binding constraint is
    rational for stable-employment, stable-income asker — but for
    gig-economy / commission / 1099 askers whose income varies
    materially month-to-month, the FSA / HSA / APTC-projection
    machinery requires income-forecasting that the cash-flow
    framing's monthly-bucket vocabulary doesn't accommodate
    well. Boundary `personal-finance`.

## 5. ACA-marketplace-subsidy-mechanics framing

- **Decisions it applies to**: D3 (COBRA vs marketplace), D5
  (Marketplace silver vs bronze vs gold), D7 (ACA vs STLDI /
  sharing ministry).
- **Mental model summary**: The ACA marketplace uses two distinct
  subsidy mechanics that distort plan-comparison arithmetic
  invisibly to the unfamiliar: the **Advance Premium Tax Credit
  (APTC)** keyed to the second-cheapest-silver-plan ("benchmark
  silver") at the user's income, which subsidizes the dollar-
  amount-delta between income-percentage-of-FPL and benchmark
  silver premium (NOT a proportional fraction of any plan), and
  the **Cost-Sharing Reduction (CSR)** silver-plan-only loading
  at 100–250% FPL that bumps the actuarial value of silver-
  variant plans to 94 / 87 / 73 percent (vs the headline 70%
  silver AV) at the 100–150 / 150–200 / 200–250% FPL income
  bands. The framing reasons in benchmark-silver-and-CSR-tier
  terms: at low income silver-CSR strictly dominates gold (richer
  AV at lower premium); at higher income the APTC fixed-dollar
  subsidy makes bronze attractive (full premium savings flow to
  the enrollee, full extra premium for gold is out-of-pocket).
  Characteristic move: compute MAGI projection precisely; locate
  the FPL band; if 100–250% FPL pick silver-CSR-94/87/73 by
  default; if above pick bronze if healthy or gold if high-
  utilization. Anchor: APTC is reconciled on Form 8962 at tax
  time — under-projected income means owing back; over-projected
  means refund up to a capped amount.
- **Characteristic vocabulary**: "benchmark silver", "second-
  cheapest silver", "APTC", "CSR loading", "silver-CSR-94 / 87 /
  73 AV variant", "subsidy cliff", "ARPA / IRA enhanced
  subsidies", "400% FPL cliff (historical)", "Form 8962
  reconciliation", "projected vs prior-year MAGI", "Marketplace
  Navigator", "Healthcare.gov vs state-based exchange",
  "advance-payment vs lump-sum-at-tax-time."
- **Excludes**:
  - The silver-CSR-strict-dominance pattern at low income depends
    on the asker's actual MAGI landing in the 100–250% FPL
    window; for self-employed and equity-comp askers whose
    income is lumpy, the projected-MAGI at enrollment may diverge
    from realized-MAGI at year-end Form 8962 reconciliation —
    and the silver-CSR loading is *retroactively recalculated*
    at reconciliation in ways the framing's enrollment-time-
    optimization doesn't catch. Opposes F4 at the
    income-variability boundary.
  - ARPA / IRA enhanced subsidies (the elimination of the
    400%-FPL "subsidy cliff") have a sunset risk — they expire
    end of 2025 absent further congressional extension, and the
    framing's "no cliff to worry about above 400% FPL" requires
    annual verification of the current-year subsidy schedule.
    The cliff is back unless extended.
  - The framing presents APTC as a clean dollar-amount-subsidy
    keyed to benchmark silver; misses that *family-glitch* fixes
    (the 2022 IRS rule that recalculated affordability
    test using family-tier premium rather than employee-only-
    premium) created a new APTC-eligibility window for family
    members of employees with employer-coverage that was
    "affordable" for the employee but not for dependents —
    Triage in mixed-coverage households should surface this
    explicitly.
  - DACA-recipient eligibility was briefly granted under the
    2024 rule and vacated late 2025 (the Texas court's
    *Texas v. CMS* / *Texas v. HHS* vacatur restored
    pre-2024 exclusion); the framing's "lawful presence is
    the rule" needs a status-as-of-current-rule check, and
    mixed-status households use a complex household-FPL
    calculation excluding undocumented members from
    numerator-coverage but including them in denominator-FPL.
    Boundary `immigration`.

## 6. Medicare-enrollment-irreversibility framing

- **Decisions it applies to**: D4 (Delay Part B past 65 vs enroll
  on time), D8 (Original Medicare + Medigap vs Medicare Advantage
  at IEP), D9 (HSA last-month-rule × Medicare interaction).
- **Mental model summary**: Medicare enrollment is the single most
  irreversible decision in the entire US health-coverage system —
  the Part B Initial Enrollment Period (IEP) is a 7-month window
  around 65th-birthday-month; missing it triggers the **10%-per-
  12-months-late permanent premium add** that compounds and persists
  for life; the Medigap Guaranteed-Issue (GI) window is a 6-month
  one-time window starting at Part B effective date, after which
  underwriting denies common chronic conditions (diabetes with
  complications, recent cancer, COPD, etc.); switching from
  Medicare Advantage back to Original-Medicare-plus-Medigap
  outside GI requires medical underwriting that often denies.
  Some states — NY, CT, MA, ME — offer year-round or annual GI;
  CA / OR have "birthday rule" GI windows; most states are IEP-
  only. The framing reasons in window-and-clock terms: the IEP
  clock, the SEP clock (8 months from end of employment for
  delayed Part B), the General Enrollment Period (Jan–March with
  coverage July, a 3–9 month uncovered gap), the GI clock for
  Medigap. Characteristic move: chart the asker's birthday-month
  +/- 3 months, identify creditable-coverage status, and lock the
  enrollment timing first; downstream plan-choice (MA vs Original
  + Medigap) sits inside the irreversibility analysis, not above
  it.
- **Characteristic vocabulary**: "Initial Enrollment Period",
  "IEP 7-month window", "Special Enrollment Period", "8-month
  SEP from end-of-employment", "General Enrollment Period (GEP)",
  "10%-per-12-months-late penalty", "creditable coverage",
  "Medicare Secondary Payer rule (≥20 employees)",
  "Medigap Guaranteed-Issue 6-month window", "state-specific
  GI (NY / CT / MA / ME)", "birthday rule (CA / OR)",
  "MA-to-Original trial right", "SHIBA / SHIP volunteer",
  "Medicare & You handbook", "AEP (Annual Enrollment Period)
  for MA / Part D", "MA Open Enrollment Period (Jan–March)."
- **Excludes**:
  - The framing assumes the asker enters at 65 with the standard
    decision; misses earlier-Medicare-eligibility pathways — SSDI
    24-month-waiting-period (Medicare automatic at 25th month of
    disability), ESRD (end-stage renal disease, Medicare-eligible
    at 3rd month of dialysis), ALS (Medicare-eligible at first
    SSDI check). Each has its own GI / IEP variant that the
    "turning 65" frame doesn't catch.
  - Creditable-coverage status is presumptively yes for employer
    plans at ≥20 employees, BUT Part-D creditability is a
    separate determination requiring an annual employer-issued
    notice (29 CFR §423.56); the framing's "covered by my
    employer" doesn't separate Part-A integration from Part-D
    creditability, and the missed Part-D creditability notice
    triggers a separate Part-D late-enrollment penalty (1%-per-
    month, also lifetime). Many askers on COBRA past month 8 face
    both Part-B AND Part-D late-enrollment penalties stacking.
  - The "trial right" of MA-at-IEP-to-Original-Medicare-within-12-
    months is presented as a safety net; in practice the trial-
    right requires the asker to have enrolled in MA *at IEP* (not
    later), creates a one-time 12-month window of returning to
    Original-Medicare-with-Medigap-with-GI, and is procedurally
    fiddly. The framing's "you can always change your mind
    within a year" oversimplifies. Boundary `legal-disputes` for
    appeals of denied trial-right exercise.
  - Domestic-partner-coverage is NOT creditable for SEP purposes
    — IRS / SSA do not recognize the relationship for this rule,
    and an asker on a domestic-partner's employer plan who
    delays Part B incurs the late-enrollment penalty despite
    having continuous coverage. The framing's "creditable
    employer plan" reflex doesn't flag the marital-status
    threshold for SEP eligibility.

## 7. QLE-and-SEP-clock-arbitrage framing

- **Decisions it applies to**: D2 (Spousal / dependent coverage
  carve-out), D3 (COBRA vs marketplace at job loss), D6 (FSA / HSA
  mid-year changes), D9 (HSA last-month-rule timing), D10 (Newborn
  / divorce mid-year deductible-met transfer).
- **Mental model summary**: Outside annual open enrollment (OE),
  plan changes / dependent additions / coverage carve-outs are
  blocked unless the asker qualifies under a **Qualifying Life
  Event** (QLE) and acts within the typically 60-day SEP window
  (Marketplace), 30-day window (most employer plans), or 60-day
  window (COBRA election). The QLE list is specific: marriage,
  divorce, birth, adoption, death of covered person, loss of
  other coverage (involuntary), gain of other coverage (often
  triggers carve-out option), permanent relocation across plan-
  service-area, change in immigration status to "lawful
  presence." The framing reasons in window-clock terms: the QLE
  event date, the SEP / QLE-window start (sometimes event-date,
  sometimes notification-date, sometimes coverage-loss-date —
  varies), the proof-of-loss documentation required, the
  retroactive vs prospective coverage option. Characteristic
  move: when an asker mentions a life event (married, lost job,
  moved, baby coming), the framing's first move is "what's the
  QLE clock, when did it start, and what proof is needed."
  Anchor: marketplace SEP is 60 days from loss-of-coverage date;
  COBRA election is 60 days from QLE notification; QLE-triggered
  employer-plan changes are 30 days; SEP can fail entirely if
  documentation isn't furnished within the window.
- **Characteristic vocabulary**: "QLE", "Special Enrollment
  Period", "SEP clock", "60-day marketplace SEP", "30-day
  employer-plan QLE window", "60-day COBRA election window",
  "45-day COBRA premium-payment grace", "proof of loss of
  coverage", "retroactive vs prospective effective date",
  "marriage / divorce / birth / adoption / job loss QLE",
  "permanent-relocation QLE", "lawful-presence-gain QLE"
  (boundary `immigration`), "loss-of-Medicaid-eligibility QLE."
- **Excludes**:
  - The framing's clock-management discipline assumes the asker
    *knows* a QLE has occurred and *recognizes* the window
    starting; in practice many QLEs (loss of Medicaid eligibility
    via redetermination, employer dropping spousal coverage at
    mid-year plan-document amendment, marketplace plan
    discontinuation) are notified by mail or buried in employee
    communication, and the 60-day clock runs out before the
    asker registers that it started. The "act within 60 days"
    discipline requires inbox discipline the framing doesn't
    name. Opposes F4 in cash-flow-stressed contexts.
  - SEP-documentation requirements vary materially by exchange
    (state-based exchanges and federal Healthcare.gov differ);
    the framing's "furnish proof within the window" assumes a
    documentation pipeline that mismatches between issuer-
    notification timing and SEP-window-start timing, and many
    QLE-triggered SEPs fail at documentation despite a real
    qualifying event.
  - QLE definitions are *carrier-specific* for employer plans —
    while ACA defines QLE for marketplace, employer-plan SPDs
    define their own QLE list that often excludes events the
    asker assumes are universal (e.g. partner job loss when the
    partner is on the employer plan but the asker is on their
    own plan; a death in family where the deceased was a covered
    dependent but the asker has other coverage). The framing's
    "QLE means you can change" needs SPD-verification per plan.
  - The HSA / FSA QLE-change rules are NOT identical: HSA
    contributions can be changed any time (no QLE needed) but
    HSA-eligibility itself depends on continuous HDHP coverage;
    FSA elections lock at OE except for QLE; the framing's
    "QLE unlocks election changes" elides this asymmetry.

## 8. ERISA-procedural-posture framing

- **Decisions it applies to**: D3 (COBRA vs marketplace — ERISA
  pre-emption of state COBRA remedies), D7 (sharing-ministry
  contract vs insurance regulation), D8 (Original Medicare /
  Medigap vs MA — MA is not ERISA-governed), D10 (denial-of-claim
  / denial-of-appeal procedure on self-funded employer plan).
- **Mental model summary**: Self-funded employer plans (where the
  employer pays claims directly from corporate funds, contracting
  with a third-party administrator like Aetna / Cigna / United for
  network and claims administration) are regulated under federal
  ERISA, NOT state insurance law — state-insurance-commissioner
  remedies and state-law tort damages are pre-empted by 29 USC
  §1144(a). Fully-insured plans (where the employer buys a group
  insurance product from a carrier, and the carrier bears claims
  risk) sit under state insurance regulation. The procedural
  consequences are large: ERISA limits damages to plan benefits
  (no compensatory or punitive); ERISA imposes the *Firestone
  Bay Markets* deference standard for plan-administrator claim
  decisions; ERISA's mandatory administrative-exhaustion under
  29 CFR §2560.503-1 must precede federal-court filing; ERISA
  appeal deadlines (180 days for adverse-benefit determinations,
  60 days for some others) are strict. The framing reasons in
  *which-regulator-applies* and *what-damages-are-available*
  terms: read the SPD to determine self-funded vs fully-insured;
  identify the plan administrator; document the appeal exactly
  per the SPD's procedural calendar. Characteristic move: at any
  denial of significant claim, immediately get an ERISA-litigation
  attorney consult; the procedural mistakes are unrecoverable.
- **Characteristic vocabulary**: "ERISA pre-emption", "self-
  funded vs fully-insured", "29 USC §1144(a)", "*Firestone*
  deference standard", "plan administrator discretion",
  "Summary Plan Description (SPD)", "29 CFR §2560.503-1
  claims and appeals", "180-day adverse-benefit-determination
  appeal deadline", "administrative exhaustion requirement",
  "no compensatory or punitive damages under ERISA",
  "state-insurance-commissioner remedy (only fully-insured)",
  "TPA (Third-Party Administrator)".
- **Excludes**:
  - The framing's "ERISA limits damages" reads as a constraint
    only when damages would have been larger under state law;
    misses that ERISA also imposes a *federal-court venue
    requirement* that some askers find procedurally easier than
    state insurance commissioner routes (faster, more
    standardized, federally-trained adjudicators). The pre-emption
    cuts both ways and the framing's reflex "ERISA bad for
    consumer" isn't universally true.
  - Self-funded vs fully-insured is *invisible to the enrollee*
    — most employees never know which type they're on without
    reading the SPD carefully (look for "the plan is self-
    insured" or carrier-issued policy-number references). The
    framing's procedural distinctions are correct but the
    enrollee's ability to act on them is gated by document-
    reading literacy.
  - Healthcare-sharing-ministries are explicitly NOT insurance
    and NOT subject to ERISA; their dispute-resolution
    mechanism is contractual (the ministry's own bylaws and
    "shareable expense" determination), state-insurance-
    commissioner has no jurisdiction, and ERISA-attorney has no
    leverage. The framing's "denial-of-claim has appeal rights"
    is materially false in this configuration. Opposes F9.
  - Medicare Advantage and Medicare Part D have their own
    appeal regimes (Medicare Appeals Council, Administrative
    Law Judge tier at $1,840 amount-in-controversy minimum
    for 2026, federal-court review at $9,000+), parallel to
    but separate from ERISA. The framing's ERISA-centric
    procedural posture doesn't generalize to Medicare-side
    decisions even though the *vocabulary* of "appeal" feels
    transferable.

## 9. Pre-existing-condition-protection framing

- **Decisions it applies to**: D5 (ACA marketplace as default),
  D7 (ACA-compliant vs STLDI / sharing ministry), D8 (Medigap
  GI vs underwriting), D10 (newborn / mid-year additions).
- **Mental model summary**: The ACA's central consumer
  protection is **guaranteed-issue + community-rating** for
  ACA-compliant plans — no carrier can deny coverage, exclude
  pre-existing conditions, charge a higher premium based on
  health status, or rescind post-claim except for fraud. This
  is the *substantive* ACA achievement; the marketplace
  subsidy mechanics are derivative. The framing reasons in
  pre-existing-condition-protection terms: any plan that can
  underwrite (STLDI under current 4-month rule + 1-month
  renewal; healthcare-sharing-ministry "shareable expense"
  determinations; Medigap outside GI; some farm-bureau exempt
  plans) is structurally different from any plan that cannot
  (ACA marketplace, employer-sponsored group plans under
  HIPAA, Medigap during GI, MA at IEP). Characteristic move:
  for any asker with a pre-existing condition (asthma,
  depression, anxiety, ADHD, autoimmune, diabetes, prior cancer,
  any chronic medication), STLDI and sharing-ministry are
  category-mistakes regardless of premium; ACA-compliant is the
  default and the only safe option. Anchor: HIPAA's pre-existing
  condition exclusion limitation (1996) was the first wave;
  ACA's elimination of underwriting (2014) was the second; the
  framing's job is to keep these gains visible against the
  marketing of cheaper alternatives.
- **Characteristic vocabulary**: "guaranteed issue", "community
  rating", "pre-existing condition exclusion (banned under
  ACA)", "post-claim rescission risk", "HIPAA portability",
  "essential health benefits (10 EHB categories)",
  "essential benefits floor", "underwriting question",
  "lifestyle attestation (sharing ministry)",
  "statement of faith", "exclusion rider",
  "guaranteed renewability."
- **Excludes**:
  - The framing's "ACA-compliant is the only safe option for
    pre-existing conditions" is true at the substantive level,
    but the framing doesn't engage with the *cost* trade-off
    rigorously — for an asker at >250% FPL with a stable but
    non-severe chronic condition (well-managed hypertension on
    cheap generics), a sharing-ministry's headline 60–70%
    premium discount is real, and the framing's reflex "you
    must have ACA" can come across as paternalistic when the
    asker's specific risk profile and budget reality are
    aligned with the alternative. The risk is genuine but
    framing-dependent.
  - Sharing-ministry "shareable expense" determinations are
    *discretionary* — even for ACA-eligible-equivalent
    conditions, the ministry can decline to share for
    lifestyle-attestation violations, late-membership-and-
    pre-existing-condition rules (typically 12-month waiting
    period before sharing for any pre-existing), or
    "non-Biblical" conditions (the historical exclusion of
    HIV / AIDS coverage by some ministries, more recently
    moderated). The framing's "underwriting vs no-underwriting"
    binary misses the post-membership discretion regime.
  - The framing assumes the asker can identify their pre-
    existing conditions; in practice some askers don't *know*
    they have a condition (undiagnosed early-stage diabetes,
    early-stage cancer, mental-health condition that hasn't
    been medically named) until the claim event reveals it,
    and the STLDI / sharing-ministry retrospective-exclusion
    risk hits hardest for these askers. The "you'll know if
    you have a condition" reflex underweights diagnostic-
    timing uncertainty.
  - Medigap underwriting outside GI is structurally similar
    to pre-ACA commercial underwriting — common conditions
    (controlled diabetes, prior breast cancer, asthma)
    trigger rate-ups or denials. The framing's "ACA protects
    pre-existing conditions" doesn't extend to Medigap
    because Medigap sits outside the ACA's guaranteed-issue
    architecture (except in the named state GI regimes).
    Boundary with F6 (Medicare-enrollment-irreversibility).

## 10. Network-and-prior-authorization framing

- **Decisions it applies to**: D1 (HDHP / PPO / HMO — network
  type is plan-type-defining), D5 (Marketplace narrow vs broad
  network), D8 (MA HMO/PPO vs Original Medicare-with-any-
  provider).
- **Mental model summary**: Beyond premium and OOP-max, the
  binding constraint on care quality is **network breadth and
  prior-authorization burden**. A 70%-AV gold-tier marketplace
  plan with a narrow county-based HMO network is worse than a
  60%-AV bronze plan with a national PPO network if the
  asker's specialist, oncologist, or specialty hospital is in
  the PPO and not the HMO. Original Medicare + Medigap is the
  network-broadest US health-coverage product — *any* US
  physician who accepts Medicare (effectively all of them) is
  in-network — and prior-auth is required for almost nothing;
  Medicare Advantage by contrast operates HMO / PPO networks
  with county-based footprints, prior-auth on most specialist
  referrals, imaging, and procedures, and providers can drop
  mid-year. The framing reasons in provider-list and
  prior-auth-burden terms: who is the asker's PCP, oncologist,
  cancer-center, mental-health prescriber, and which plans
  include them — verify the provider-directory currency (often
  out-of-date by 6–18 months), confirm with the provider's
  office directly. Characteristic move: build the provider
  list first, filter plans by provider-inclusion, *then*
  apply premium / OOP-max / actuarial-value math.
- **Characteristic vocabulary**: "narrow network", "broad
  network", "PPO out-of-network coverage", "HMO referral
  requirement", "EPO no-out-of-network rule", "POS plan",
  "tiered network", "provider directory", "ghost network"
  (provider listed in-directory but not actually accepting
  patients), "prior authorization", "step therapy", "fail-
  first", "any-Medicare-accepting-provider" (Original
  Medicare's network), "MA county-based service area",
  "center-of-excellence (COE) network", "any-willing-provider
  state laws."
- **Excludes**:
  - Provider directories are systematically inaccurate — CMS
    audits of MA plans find 30–50% of listed mental-health
    providers either not accepting new patients or no longer in
    network at the time of the audit; the framing's "verify
    the directory" instruction is correct but understates the
    operational reality of finding actual in-network care.
    Calls to provider offices are the only reliable check, and
    the framing rarely acknowledges this workload.
  - Network drops mid-year are a Medicare-Advantage-specific
    phenomenon (MA contracts year-to-year with provider
    systems, and contract disputes between hospital systems
    and MA carriers in 2023–25 have produced material mid-year
    network changes for many beneficiaries). The framing's
    "I picked a plan with my doctor in network at enrollment"
    is a stable-state assumption that the actual market doesn't
    deliver. Opposes F1 (which assumes enrollment-time
    information is dispositive).
  - Prior-authorization burden is unevenly distributed across
    plans and specialties — high-cost specialty drugs and
    imaging are universally prior-auth-required, but
    psychotherapy frequency caps, durable-medical-equipment
    approvals, and ABA-therapy hour limits vary materially.
    The framing's "Original Medicare has no prior-auth" is
    broadly true (Part B has very limited PA, mostly for
    durable medical equipment under the Round 1 / 2 PA
    Demonstration); MA varies plan-by-plan and year-by-year.
  - Specialty-pharmacy and biologic-drug coverage uses a
    parallel "buy-and-bill" vs "specialty-pharmacy" path the
    framing's medical-provider-list vocabulary doesn't engage;
    a marketplace plan whose specialty-pharmacy partner doesn't
    carry the asker's biologic produces an OOP-cost surprise
    even when the medical provider is in-network.

## 11. Embedded-vs-aggregate-cost-sharing framing

- **Decisions it applies to**: D1 (HDHP / PPO at OE — family-tier
  structure), D2 (spousal / dependent coverage), D10 (embedded vs
  aggregate family deductible directly).
- **Mental model summary**: Family-tier plans split per-member
  vs whole-family deductible and OOP-max in three meaningfully
  different structures: (a) **aggregate** family deductible — no
  individual deductible-met until the entire family-tier
  deductible is reached by combined family spend (worst when
  one member has heavy utilization); (b) **embedded** individual
  deductible — each member has an individual deductible cap at
  which point that individual's care begins to pay coinsurance,
  while the family aggregate also runs; (c) **ACA-mandated
  embedded individual OOP-max sub-limit** — per the 2016 CMS
  rule, every ACA plan with family coverage must include an
  embedded individual OOP-max ≤ self-only OOP-max for that year
  (no family member can legally be exposed to more than the
  self-only OOP-max), even if the family OOP-max is higher. The
  framing reasons in concentration-of-utilization terms: when
  one member dominates the family's medical spend, embedded
  structures cap that member's exposure while aggregate
  structures force the rest of the family's care to flow
  through deductible. Characteristic move: read the SPD to
  identify deductible structure, model the high-utilization-on-
  one-member scenario, prefer embedded structures for any
  family with a member-specific risk factor.
- **Characteristic vocabulary**: "aggregate family deductible",
  "embedded individual deductible", "embedded individual OOP-
  max sub-limit (ACA 2016 rule)", "true family deductible",
  "umbrella deductible", "family OOP-max", "self-only OOP-max
  cap on individual exposure", "tiered family deductible (2x
  self-only structure)", "non-embedded HDHP (legacy)",
  "stacked deductible (annual + plan-year)."
- **Excludes**:
  - Older plan-comparison spreadsheets (and many HR open-
    enrollment portals) still display family deductible as a
    single number, hiding the embedded individual sub-limit
    that ACA mandated since 2016. The framing's "look for
    embedded sub-limit" instruction is correct but the asker
    is up against display-layer-incompleteness. Opposes F1
    when the spreadsheet under-represents structure.
  - Prescription-drug OOP tracking is *often* separate from
    medical OOP, with its own deductible and OOP-max — and on
    some plans, prescription OOP-met counts toward family but
    not toward individual embedded sub-limits, or vice versa.
    The framing's "embedded OOP caps individual exposure"
    needs the prescription-track verification that most
    enrollees don't do.
  - HRAs (Health Reimbursement Arrangements) and ICHRAs
    (Individual Coverage HRA) layer employer-funded chunks on
    top of the plan's deductible; the framing's structural
    analysis applies cleanly to plan-as-document but obscures
    when an HRA pays the first $2,000 of deductible — the
    *effective* cost-sharing structure the enrollee experiences
    is the layered product, not the plan-document standalone.
  - Mid-year additions and removals (newborn QLE, divorce
    QLE, dependent age-out at 26) interact with the embedded
    individual sub-limit in plan-specific ways — some plans
    pro-rate the embedded sub-limit by months-of-coverage,
    some don't, and the framing's "embedded caps at $9,450"
    is calendar-year-static in a way mid-year additions
    don't track. Boundary `family-planning`.

## 12. Tax-and-arbitrage framing

- **Decisions it applies to**: D1 (HDHP gates HSA), D5
  (Marketplace MAGI projection), D6 (HSA / FSA / dep-care FSA
  sizing), D9 (HSA last-month-rule timing — testing-period
  recapture).
- **Mental model summary**: Health-insurance choices interact
  with the tax code in ways that often dominate the apparent
  insurance arithmetic. Premium dollars on employer plans are
  pre-tax (Section 125 cafeteria plan, no FICA / federal /
  state income tax); HSA contributions are deductible above-
  the-line on Form 8889 (with FICA savings only on payroll
  contributions, not on after-tax 1040 deductions); FSA
  contributions are Section 125 pre-tax; APTC reconciles on
  Form 8962 at tax time; dep-care-FSA reduces income on a
  sliding scale benefit based on marginal tax rate and is
  coordinated against the Child-and-Dependent-Care Tax Credit
  (Form 2441) — both cannot be claimed on the same dollars,
  and the optimal election depends on marginal tax rate and
  total qualifying spend. The framing reasons in marginal-rate
  and form-mechanic terms: what's the asker's federal +
  state + FICA marginal rate, what's the deductible-equivalent
  tax savings on each pre-tax dollar, what's the recapture risk
  on HSA last-month-rule failure. Characteristic move: build
  the cross-form view (8889 + 2441 + 8962) before answering
  any contribution-sizing question; the headline "max the HSA"
  is correct only after verifying eligibility and recapture
  exposure.
- **Characteristic vocabulary**: "above-the-line deduction",
  "Section 125 cafeteria plan", "Form 8889", "Form 2441",
  "Form 8962", "MAGI for ACA", "MAGI for IRMAA (Medicare)",
  "last-month-rule testing period", "income recapture +
  10% penalty", "Child-and-Dependent-Care Tax Credit",
  "credit-vs-deduction coordination", "IRMAA brackets
  (Income-Related Monthly Adjustment Amount on Part B /
  Part D)", "Roth-conversion-and-IRMAA interaction."
- **Excludes**:
  - IRMAA (Income-Related Monthly Adjustment Amount on
    Medicare Part B and Part D) is calculated on a 2-year
    lookback MAGI — the asker who realizes a large capital
    gain or Roth conversion in 2026 may face IRMAA brackets
    on 2028 Medicare premiums; the framing's tax-year focus
    misses the 2-year-forward Medicare-premium implication.
    Boundary `personal-finance`.
  - HSA-on-payroll-deduction saves FICA (7.65%) in addition
    to income tax; HSA-on-after-tax-1040-deduction saves only
    income tax (FICA already paid). The framing's "HSA is
    above-the-line deductible" understates the payroll-
    contribution advantage for askers who think they can
    "catch up at tax time" — they lose the FICA save.
  - The dependent-care-FSA-vs-Child-Care-Tax-Credit
    coordination requires the asker to project marginal rate
    accurately; askers with lumpy income (equity vesting,
    self-employed) get this wrong in ways that produce
    higher effective tax than necessary. The framing's
    "coordinate the election" assumes a stable income picture
    the asker may not have.
  - APTC reconciliation on Form 8962 has *capped* repayment
    for under-projected MAGI below 400% FPL (the cap was
    intended as a hardship protection); above 400% FPL the
    repayment is uncapped and can be six-figure when ARPA-
    enhanced subsidies are in effect (the asker who
    under-projected income and received $25k/year of APTC
    on a benchmark-silver may owe the full $25k back). The
    framing's "true-up at tax time" doesn't surface the
    severity of the asymmetry above the cap.

## 13. Bureaucratic-procedural framing

- **Decisions it applies to**: D3 (COBRA election + payment
  mechanics), D6 (FSA claims submission and substantiation),
  D8 (Medicare enrollment paperwork), D10 (newborn / divorce
  QLE documentation), and as a meta-framing on all denial-of-
  claim / denial-of-appeal procedures.
- **Mental model summary**: Health-insurance is procedural in
  ways askers chronically under-estimate — EOBs (Explanation
  of Benefits) require careful reading, claims can be denied
  for coding errors that the patient must catch and dispute,
  prior-auth approvals expire and must be renewed mid-
  treatment, COBRA election requires returning a specific
  form to a specific TPA-mailing-address within 60 days
  *and* paying back-premium within 45 days, FSA claims
  require itemized receipts (not credit-card statements) plus
  Letter-of-Medical-Necessity for grey-area items (sunscreen,
  electrolytes, certain OTCs). The framing reasons in form-
  number, deadline, and substantiation terms: which form,
  which mailing address, which deadline, what proof. The
  patient-advocate / billing-error-recovery voice anchors this
  framing — every denied claim is potentially a coding error
  ($X procedure was billed with $Y CPT instead of correct $Z
  CPT, leading to in-network being processed as out-of-
  network); every EOB should be reconciled against the
  provider's bill; every prior-auth approval should be
  documented with reference number and effective dates.
  Characteristic move: build a personal-medical-finance
  binder (or digital equivalent); track every claim from
  service-date through final-EOB; dispute denials in writing
  with the explicit citation of the SPD provision or coverage
  rule. Anchor: 29 CFR §2560.503-1 mandates an internal
  appeal window before external review; No Surprises Act
  §2799A-1 IDR process for surprise out-of-network billing.
- **Characteristic vocabulary**: "EOB reading", "CPT code",
  "ICD-10 code", "denial code", "claim resubmission with
  corrected coding", "prior-auth reference number",
  "letter of medical necessity", "FSA substantiation",
  "FSA claims-submission deadline (90 days post plan
  year)", "COBRA election form + back-premium payment",
  "internal appeal", "external review (state-insurance-
  commissioner or IRO)", "No Surprises Act IDR
  arbitration", "patient advocate", "medical billing
  reconciliation."
- **Excludes**:
  - The framing's procedural diligence is *time-intensive*
    in ways that compound during a medical crisis — the
    same asker who could read EOBs in good health is now
    sleep-deprived, post-anesthesia, or coping with a
    chronic-illness cognitive fog, and the framing's
    "track every claim" workload becomes impossible exactly
    when the financial exposure peaks. Patient-advocate
    services exist for a reason; the framing rarely
    surfaces the cost-benefit of paid advocacy.
  - "Dispute the denial in writing with citations" is
    correct procedure, but the framing under-estimates the
    *response asymmetry* — TPAs and carriers respond on
    their own clock (often beyond statutory deadlines
    without consequence under ERISA), and the asker waiting
    in network limbo cannot get care without paying out-of-
    pocket and seeking reimbursement, which most cannot
    front. The procedure works for the asker who has cash
    flow and patience the system doesn't compensate.
  - The No Surprises Act §2799A IDR (Independent Dispute
    Resolution) process is heavily contested — the IDR
    determinations have been litigated under multiple
    *Texas Medical Association v. HHS* rulings, the
    methodology favoring the median-in-network-rate vs
    qualifying-payment-amount has shifted multiple times,
    and the framing's "use the IDR" assumes a process that
    is operationally lurching. Boundary `legal-disputes`.
  - The framing prices procedural literacy as a learnable
    skill; for English-second-language askers, askers with
    low-literacy backgrounds, or askers with cognitive /
    developmental disabilities, the bureaucratic complexity
    is itself a structural barrier to access — and the
    framing rarely connects to community-health-worker /
    patient-navigator / SHIP / Medicaid-redetermination-
    assistance resources that exist to bridge this gap.

## 14. Single-payer / market-failure framing

- **Decisions it applies to**: meta-framing on all decisions —
  applies most directly to D1, D5, D7 (where the system's
  product variety itself creates the choice complexity);
  applies as a critique on D8 (the public Medicare program
  vs Medicare Advantage's private overlay).
- **Mental model summary**: The fundamental framing is that
  the US health-coverage system's design — multiple
  competing carriers, plan-tier variety, network differentiation,
  prior-authorization gating, balance-billing, marketplace
  subsidies layered on top of employer-sponsored coverage,
  Medicare with private MA overlay — is itself a structural
  failure that imposes costs (cognitive, financial, time,
  health-outcome) the framing's adherents argue are
  unjustifiable relative to single-payer or unified-tier
  alternatives. The framing reasons in administrative-cost,
  market-power-asymmetry, and outcomes-comparison terms:
  US administrative costs at 8–15% of premium dollar vs 1–3%
  in single-payer systems; comparable health outcomes at 2x
  per-capita cost; chronic-illness-bankruptcy rates that
  don't exist in peer countries. Characteristic move: name
  the choice complexity as a system-design failure (not the
  asker's failure), surface that "the right plan" is
  conditional on the system staying the same, and identify
  that asker advocacy + political engagement is the
  long-horizon move that complements any short-horizon plan
  selection. This framing is more diagnostic than
  prescriptive — it explains *why* the asker is overwhelmed
  by 14 plan choices at OE, even after a tool helps them
  choose well.
- **Characteristic vocabulary**: "administrative cost",
  "single-payer", "Medicare-for-all", "everybody-in nobody-
  out", "Beveridge / Bismarck / out-of-pocket / National
  Health Insurance models", "private overlay on public
  program", "PNHP (Physicians for a National Health
  Program)", "structural underinsurance", "medical
  bankruptcy", "cost-shifting", "monopsony pricing",
  "all-payer-rate-setting (Maryland)", "public option."
- **Excludes**:
  - The framing's structural critique doesn't translate to
    actionable advice for the asker at this Tuesday's OE
    deadline — naming the system as broken doesn't help
    the 34-year-old choosing between HDHP and PPO this
    week. The framing's value is meta-explanatory but its
    direct decision-support utility is low. Opposes
    F1 / F2 / F3 / F4 as a *category* of decision-support
    framings.
  - Single-payer advocacy under-engages with the *transition
    cost* — the political-economy and institutional inertia
    of the current system are themselves the binding
    constraint that the framing's "we should have
    Medicare-for-all" rhetoric doesn't address, and the
    framing's adherents often present the alternative as
    self-evident without engaging the actual policy-design
    questions (provider-payment rates, capital-investment
    transition, employer-coverage transition path).
  - The framing's reflex toward "expand Medicare" assumes
    Original Medicare is the model — but Original Medicare
    itself has design flaws (no OOP cap, Part D donut hole
    until IRA 2025, no dental / vision / hearing) that the
    framing rarely names as needing reform. The "single-
    payer is the answer" rhetoric is structurally
    inconsistent with the actual Medicare program's
    coverage gaps.
  - Politicizes a domain where the asker often needs
    apolitical decision-support — a SHIBA volunteer doesn't
    advocate single-payer; a Marketplace Navigator doesn't
    advocate single-payer; the asker needing a plan this
    week is not well-served by a framing that grades the
    whole system. The framing's value is in *meta-context*
    for the Editor / Risk Officer layers, not in user-
    facing answers.

---

## Coverage map

Per `_schema.md`, every decision needs ≥ 3 framings.

| Decision | Framings that cover it | Count |
|---|---|---|
| D1 HDHP / PPO / HMO at OE | F1, F2, F3, F4, F10, F11, F12 | 7 |
| D2 Spousal / dependent coverage carve-out | F7, F11 | 2* |
| D3 COBRA vs marketplace at job loss | F2, F4, F5, F7, F8, F13 | 6 |
| D4 Delay Part B vs enroll on time | F6 | 1* |
| D5 Marketplace silver vs bronze vs gold | F1, F4, F5, F9, F10, F12 | 6 |
| D6 FSA / HSA / dep-care FSA sizing | F1, F3, F4, F7, F12, F13 | 6 |
| D7 ACA vs STLDI / sharing ministry | F2, F4, F5, F8, F9 | 5 |
| D8 Original Medicare + Medigap vs MA | F6, F8, F9, F10 | 4 |
| D9 HSA last-month-rule timing | F3, F6, F7, F12 | 4 |
| D10 Embedded vs aggregate family deductible | F1, F2, F8, F11, F13 | 5 |

*Note: D2 and D4 below the ≥3 minimum on direct application;
augmenting framings apply via cross-decision interaction:

- **D2 (Spousal coverage carve-out)** also pulls F1 (the actuarial
  arithmetic of dual-spousal-plan vs single-family-tier comparison),
  F3 (the HSA-family-vs-self-only contribution coordination), and
  F12 (the marginal-tax-rate implication of pre-tax spousal-
  surcharge dollars). With these cross-cutting applications,
  D2 is covered by F1, F3, F7, F11, F12 = 5 framings.
- **D4 (Delay Part B vs enroll on time)** also pulls F3 (HSA-and-
  Medicare-mutual-exclusion timing — delaying Part-A to preserve
  HSA contribution capacity), F7 (the 8-month SEP clock after
  end-of-employment is itself a SEP-clock-management problem),
  F8 (creditable-coverage determination under the SPD requires
  ERISA-document-reading procedure), F12 (the IRMAA 2-year-
  lookback Medicare-premium implication of MAGI shocks), and
  F13 (the procedural mechanics of enrolling via SSA online vs
  in-person, the GEP-fallback paperwork). With these cross-
  cutting applications, D4 is covered by F3, F6, F7, F8, F12,
  F13 = 6 framings.

Updated full coverage map after cross-cutting expansion:

| Decision | Framings (after cross-cutting) | Count |
|---|---|---|
| D1 | F1, F2, F3, F4, F10, F11, F12 | 7 |
| D2 | F1, F3, F7, F11, F12 | 5 |
| D3 | F2, F4, F5, F7, F8, F13 | 6 |
| D4 | F3, F6, F7, F8, F12, F13 | 6 |
| D5 | F1, F4, F5, F9, F10, F12 | 6 |
| D6 | F1, F3, F4, F7, F12, F13 | 6 |
| D7 | F2, F4, F5, F8, F9 | 5 |
| D8 | F6, F8, F9, F10 | 4 |
| D9 | F3, F6, F7, F12 | 4 |
| D10 | F1, F2, F8, F11, F13 | 5 |

All 10 decisions satisfy the ≥3 framings minimum after cross-
cutting application. F14 (single-payer / market-failure) is a
meta-framing that applies as a Critic / Editor layer context rather
than a primary decision lens.

## Cross-framing tensions

Direct axiom-level oppositions to surface in Layer 3 and to flag for
Triage / Risk Officer routing when the asker's prompt vocabulary
lands on one side:

- **F1 (expected-utilization arithmetic) ↔ F2 (risk-transfer / OOP-
  cap)**. F1 minimizes probability-weighted total cost across
  utilization scenarios; F2 minimizes worst-case single-event
  exposure. On D1, the healthy single 30-year-old gets HDHP from F1
  (low premium captures expected savings; healthy means low
  probability of OOP-max being binding), but gets PPO with predictable
  copay from F2 (the catastrophic accident or unexpected cancer
  diagnosis happens at low probability but with high consequence and
  a fast OOP burn that the HDHP's $8,300 OOP-max doesn't actually
  feel cheap in the moment). Same facts, opposite answers.

- **F3 (HSA-as-retirement) ↔ F4 (immediate-cost / cash-flow)**. F3
  says fund the HSA to the cap, pay current medical from after-tax
  savings, let the HSA compound for 30 years. F4 says you don't
  have after-tax savings to deploy that way; the FSA-or-HSA
  contribution is a cash-flow constraint, and the right contribution
  is the one that covers expected in-year medical without locking
  cash you need for rent. Same household, opposite contribution
  strategy. The HSA-administrator voice and the personal-finance-
  blogger voice both push F3 dogmatically; the cash-flow voice and
  the patient-advocate voice push F4 — Triage should surface F4
  when the asker's situation reads as cash-flow-binding ("I'm
  living paycheck-to-paycheck") and surface F3 when the asker
  reads as savings-rich ("I'm maxing my 401k, looking for the next
  tax-advantaged bucket").

- **F5 (ACA-subsidy-mechanics) ↔ F9 (pre-existing-condition-
  protection)**. F5 reasons within ACA-marketplace plans and
  optimizes subsidy / metal-tier; F9 reasons across ACA-vs-non-ACA
  and dismisses non-ACA options for any asker with a pre-existing
  condition. The conflict surfaces on D7: F5 has no native
  vocabulary for sharing-ministry or STLDI evaluation (they're
  out-of-scope for the marketplace subsidy framework); F9 evaluates
  them only on pre-existing-condition exclusion grounds and rules
  them out, missing the for-healthy-high-income subset where F5's
  silence is read as endorsement of alternatives. Triage should
  surface F9 when the asker mentions any chronic condition, any
  medication, or any prior medical event; surface F5 when the
  asker explicitly frames the question as "marketplace plan
  comparison."

- **F6 (Medicare-enrollment-irreversibility) ↔ F10 (network and
  prior-authorization)**. F6 makes the irreversibility of MA-vs-
  Original-Medicare-with-Medigap dispositive — once chosen at IEP,
  the path back to Medigap is medical-underwriting-gated. F10
  makes the network breadth and prior-auth burden the binding
  axis — Original Medicare's any-provider network is the dominant
  benefit, MA's network narrowness and prior-auth burden are the
  dominant cost. Both framings independently recommend Original
  Medicare + Medigap for high-utilization or specialty-care-
  expected scenarios; both should be surfaced together because
  they converge on D8 even with different reasoning paths. The
  divergence: F6 alone can be persuaded by an MA plan's "trial
  right" return path; F10 doesn't engage with the trial-right
  because the network mid-year-drop risk is the binding constraint
  regardless of return rights.

- **F8 (ERISA-procedural) ↔ F13 (bureaucratic-procedural / patient-
  advocate)**. Both engage with the procedural posture of claims
  and appeals, but F8 reasons at the regulatory-jurisdictional level
  (which body has authority, what damages are available) and F13
  reasons at the operational-form-and-deadline level (which form,
  which deadline, which substantiation). They converge in scope but
  diverge in remedy: F8 routes to an ERISA-litigation attorney
  early; F13 routes to a patient-advocate / billing-error-recovery
  service. The same denial-of-claim event has both an F8 reading
  (large dollar, self-funded plan — get an ERISA attorney) and an
  F13 reading (CPT coding error, file the corrected resubmission
  through the carrier directly). Triage should surface both when
  denial dollars exceed $5k or when the asker mentions an SPD-
  reading issue.

- **F12 (tax-and-arbitrage) ↔ F4 (immediate-cost / cash-flow)**.
  F12's "max the HSA, time the last-month-rule, coordinate dep-
  care-FSA-vs-tax-credit" optimization assumes the asker can
  navigate Form 8889 / 2441 / 8962, has stable income, and
  prioritizes after-tax dollar maximization. F4 prioritizes
  cash-on-hand and predictable cost; the FSA forfeiture risk and
  HSA-recapture risk are large in the cash-flow framing's calculus
  and small in the tax-arbitrage framing's calculus. The same
  $4,300 HSA contribution is a tax win in F12 and a cash-flow
  drag in F4. Triage should surface both when the asker's facts
  span tax-optimization questions AND cash-flow questions
  simultaneously.

- **F14 (single-payer / market-failure) ↔ F1, F2, F3, F4
  (decision-support framings)**. F14 is structurally different —
  it grades the system rather than the choice. When the asker is
  overwhelmed by 14-plan OE complexity or frustrated by
  prior-auth denial, F14 names the experience as system-failure
  rather than asker-failure, but doesn't provide decision-
  support for this Tuesday's deadline. F14 should be surfaced as
  *meta-context* — never as the sole framing on an answer, but
  acknowledged when the asker's prompt expresses frustration at
  the system itself.

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`): every
  `Excludes` bullet above is a Layer 3 candidate. Highest-density
  candidates are framings 1 (expected-utilization — embedded vs
  aggregate misread, out-of-network OOP-max absence, condition-onset
  dynamics), 2 (OOP-cap — ACA EHB-only coverage, calendar-year reset
  trap, asset-liquidity gap), 3 (HSA-as-retirement — cash-flow-
  constraint mismatch, receipt-shoebox burden, Medicare-Part-A-
  retroactivity HSA disqualification), 5 (subsidy-mechanics — MAGI
  reconciliation trap, ARPA sunset, family-glitch, DACA vacatur),
  6 (Medicare-irreversibility — SSDI / ESRD / ALS pathway gaps,
  Part-D creditability separation, trial-right oversimplification,
  domestic-partner SEP failure), 8 (ERISA — self-funded invisibility,
  sharing-ministry zero-procedural-rights, Medicare-Advantage
  distinct appeal regime), and 9 (pre-existing-condition —
  sharing-ministry discretion, undiagnosed-condition timing,
  Medigap outside GI). Sweep all 14 framings × ~4 bullets each =
  ~56 blindspot candidates; promote ≥5 per framing into
  `blindspots.md` per the [`_schema.md`](../_schema.md) minimum.

- **High-stakes posture (Mechanism E)**: this file is decision-
  support, not licensed-broker / SHIBA-counselor / CPA / ERISA-
  attorney advice. Editor on any answer that lands on these
  framings must (per `domain_pack.md` once authored) explicitly
  label output as "decision-support; consult [the specific
  category — broker for D1/D2/D5, SHIBA for D4/D8, Navigator
  for D3/D5/D7, CPA for D6/D9, ERISA attorney for D3/D8/D10]
  for case-specific facts." Selective referral is itself a
  framing axis — the actuarial-broker voice has different
  conflicts of interest than the SHIBA voice; the Editor should
  name the *right* referral category for each decision, not
  blanket-mandate "consult a professional." Critic must apply
  stricter grounding on citation-bearing claims (IRC §223 for
  HSA, ACA §1302 for EHB, 42 USC §1395 for Medicare, 29 USC
  §1144 for ERISA, 26 CFR §54.4980G for HSA, 45 CFR §147 for
  ACA insurance reforms) — generic "the law says X" claims
  unanchored to a cite should fail Critic review.

- **Triage routing notes**: framings 6, 8, 12 carry the most
  distinctive vocabulary signatures (IEP / SEP / GEP / Medigap-GI,
  ERISA-pre-emption / *Firestone* / SPD, IRMAA-lookback / Form
  8889 / Form 8962) and should be high-confidence routing
  matches. Framings 1, 2, 4 share vocabulary with general
  insurance and personal-finance topics and will need
  disambiguation against adjacent domain packs once V2 two-pass
  Triage is wired. F14 (single-payer / market-failure) is a
  Critic / Editor meta-context framing; it should NOT route to
  primary decision-support answers but should be available for
  Editor framing-aware completions.

- **Cross-domain edges from `decisions.md`**: F3 (HSA-as-
  retirement-vehicle) is the principal cross-domain framing into
  `personal-finance` (HSA contribution-ordering within the
  general tax-advantaged-account stack); F5 (ACA-subsidy-
  mechanics) routes into `immigration` on lawful-presence /
  DACA / mixed-status household FPL calculation; F7 (QLE-and-
  SEP-clock) routes into `tech-career` on layoff-driven
  coverage transition and `family-planning` on marriage /
  birth / divorce QLE; F8 (ERISA-procedural) routes into
  `legal-disputes` on self-funded-plan denial-of-claim disputes
  and `tech-career` on employer-plan governance questions; F11
  (embedded-vs-aggregate) routes into `family-planning` on
  family-tier structure for households with one high-utilizer.
  Triage should surface these adjacencies when the user's
  situation spans both domains.

- **Voice-anchor → sources.yaml hand-off** (Layer 4 forward-
  pointer): the conceptual voices named in the intro have
  candidate source-view mappings as follows. The actuarial-and-
  broker voice → eHealth, GoHealth, individual licensed brokers'
  blogs, NAIC consumer guides. SHIBA / SHIP voice → state-
  specific SHIP program web resources, Medicare.gov, KFF
  Medicare resources. ACA Navigator voice → Healthcare.gov,
  state-based-exchange consumer pages, KFF marketplace
  resources. HSA-administrator voice → HealthEquity / Fidelity
  / Lively / Optum-Bank consumer education content, IRS
  Publication 969. ERISA-attorney voice → Society for Human
  Resource Management (SHRM), American Bar Association ERISA
  Committee resources, *Employee Benefits News*. Healthcare-
  economics-journalist voice → Sarah Kliff at NYT,
  KFF Health News (formerly Kaiser Health News), ProPublica
  Health Care series, *Health Affairs* blog. Bogleheads voice
  → bogleheads.org HSA wiki, r/Bogleheads HSA-specific threads.
  Employer-benefits / HR voice → r/personalfinance benefits
  megathread, r/HumanResources, SHRM employer-facing
  resources. ACA-reform-academic voice → KFF, Health Affairs
  blog, Brookings Center on Health Policy, Commonwealth Fund.
  Single-payer / Medicare-for-all voice → PNHP, *Healthcare-
  NOW!*, Public Citizen Health Research Group. Patient-
  advocate / billing-recovery voice → NAHAC (National Association
  of Healthcare Advocacy), AdvoConnection, Marshall Allen's
  *Never Pay the First Bill* and follow-on ProPublica work.
  Conservative health-policy voice → Galen Institute, AEI
  Health Policy Center, Heritage Foundation Health Policy.
  Disability / chronic-illness patient voice → r/ChronicIllness,
  r/Disability, Patient Advocate Foundation. Sources author
  should weight reliability and keyword_filter per
  `_schema.md`; high-stakes domain requires reliability ≥3
  for any source cited in Risk Officer answers, ≥4 for direct
  decision-support quotes.
