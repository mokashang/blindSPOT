# ACA Marketplace and Navigator

CMS-trained Navigator / in-person assister + Healthcare.gov +
KFF policy-research voice — the federally-funded, structurally-
prohibited-from-steering consumer-assistance network operating
under 45 CFR §155.215, paired with the policy-research apparatus
that does the FPL → APTC → CSR subsidy arithmetic. This community
specializes in the pre-65 individual-market Marketplace plan
selection problem and the subsidy mechanics that drive it; it is
**not a substitute** for case-specific Navigator assistance during
OEP or SEP. The KFF subsidy calculator and the Healthcare.gov plan-
finder tell you the candidate plans and the headline APTC; the
Navigator with the asker's actual MAGI projection, household
composition, mixed-immigration-status facts, and state-based-
exchange jurisdiction is where the enrollment happens.

## Identity

CMS-trained Marketplace Navigators (45 CFR §155.215, certified
through annual CMS training, structurally prohibited from steering
to specific carriers or plans), in-person assisters, Certified
Application Counselors (CACs) at FQHCs / community health centers,
and the policy-research community that publishes the FPL → APTC →
CSR worksheets that drive D5 decisions (KFF, Commonwealth Fund,
Health Affairs, Brookings Center on Health Policy). They reason
about coverage as a *subsidy-eligibility-and-metal-tier*
optimization problem under federal-and-state jurisdictional
overlap: FFE (Federally-Facilitated Marketplace) on Healthcare.gov
in 32 states; State-Based Exchanges (SBEs) running their own
platforms in 18 states + DC (Covered California, NY State of
Health, HealthSource RI, Connect for Health Colorado, etc.); the
post-ARPA / IRA-extended enhanced subsidies through 2025 with the
post-2025 cliff in regulatory limbo; the family-glitch fix making
employer-affordability test family-wide; the mixed-immigration-
status household FPL math where some members are eligible for APTC
and others not. They are *not* brokers (Navigators cannot earn
commission and are prohibited from steering); they are *not* the
chronic-illness patient community (Navigators reason about plan
*selection* upfront, not formulary-mid-year-change recovery).

## Voice anchors

- Source-views from `health-insurance/sources.yaml` under this
  community_tag:
  - `healthcare-gov-policy-updates` — Healthcare.gov blog + CMS
    Marketplace policy bulletins (OEP / SEP eligibility rules,
    APTC reconciliation, CSR mechanics, state-based-exchange
    jurisdiction map).
  - `kff-marketplace-and-medicaid` — KFF Health Reform topic feed,
    subsidy-design analysis, mixed-status FPL math, Medicaid
    expansion / unwinding tracker, state-by-state Medicaid
    eligibility detail.
- Adjacent named voices / outlets: Louise Norris at
  Healthinsurance.org (the canonical pre-65 Marketplace consumer
  explainer); Charles Gaba at ACASignups.net (enrollment data
  tracker, state-by-state); Cynthia Cox at KFF (program-on-program
  analysis); the Center on Budget and Policy Priorities (CBPP)
  Health Reform team; the *Commonwealth Fund Blog*; *Health
  Affairs Forefront* (formerly Health Affairs Blog); Get America
  Covered enrollment campaign; CoveringCalifornia.org and the
  state-based-exchange consumer-help platforms (NY State of
  Health, Covered California, HealthSource RI, etc.).

## Mental model

ACA Marketplace plan selection is a subsidy-arithmetic problem
framed by metal-tier actuarial value, expected-utilization, and
the strict federal rules on who counts as a household member and
how MAGI gets projected forward. APTC (Advance Premium Tax
Credit, IRC §36B) is computed as the difference between the
benchmark second-lowest-cost silver plan premium and the
"applicable percentage of income" (a sliding scale from ~0% at
150% FPL to ~8.5% at 400% FPL under the ARPA / IRA extension,
restored to the pre-ARPA cliff if Congress doesn't act post-2025).
CSR (Cost-Sharing Reduction) applies *only* to silver-plan
enrollment at <250% FPL, raising actuarial value from 70% to
73% / 87% / 94% depending on FPL band — meaning "buy silver" is
load-bearing advice for low-income enrollees and *anti-advice* for
higher-income enrollees who would prefer gold's lower OOP-max
without paying for the AV bonus they don't qualify for. The
family-glitch fix (effective 2023) makes employer-coverage
affordability assessed at family premium, not employee-only,
unlocking Marketplace APTC for spouses and children of workers
with affordable-on-paper employer coverage. Mixed-immigration-
status households compute APTC on the *tax household* but
eligibility restricts to "lawfully present" members — DACA
recipients' Marketplace eligibility was vacated and reinstated
and is in active litigation. State-Based Exchange jurisdiction
matters: California, New York, Washington, Massachusetts, and
others have their own platforms, their own SEP-trigger
interpretations, and their own subsidy-supplement programs
(California Premium Subsidy through Covered California; New York's
Essential Plan at 138–250% FPL replacing Marketplace eligibility).

## Characteristic vocabulary

- "APTC" (Advance Premium Tax Credit, IRC §36B), "PTC" (Premium
  Tax Credit, reconciled on Form 8962), "applicable percentage of
  income"
- "CSR" (Cost-Sharing Reduction, silver-plan-only), "AV bands"
  (Silver CSR: 73% / 87% / 94%), "benchmark plan" (second-lowest-
  cost silver)
- "FPL" (Federal Poverty Level), "100% FPL Medicaid-eligibility
  floor in expansion states", "138% FPL (Medicaid expansion cap)",
  "250% FPL (CSR cap)", "400% FPL (pre-ARPA APTC cliff)"
- "Form 8962" (APTC reconciliation), "repayment limit" (FPL-banded
  cap on excess-APTC payback), "redetermination", "AV calculator"
- "OEP" (Open Enrollment Period, Nov 1 – Jan 15 federally), "SEP"
  (Special Enrollment Period — loss-of-coverage, marriage, birth/
  adoption, income change, residency, etc.), "QLE" triggers
- "Family glitch fix" (effective 2023), "lawfully present", "five-
  year bar" (Medicaid LPR eligibility), "mixed-status household"
- "FFE" (Federally-Facilitated Marketplace, Healthcare.gov), "SBE"
  (State-Based Exchange), "SBE-FP" (State-Based Exchange on the
  Federal Platform)
- "Navigator" (45 CFR §155.215), "CAC" (Certified Application
  Counselor), "Marketplace Assister", "in-person assister"
- "Continuous coverage unwinding" (post-PHE Medicaid eligibility
  re-screening that ran 2023–2024), "coverage gap" (in non-
  expansion states between Medicaid eligibility and 100% FPL APTC
  threshold)

## Known blind spots OF this community

- **APTC over-estimation repayment-cap protection is fragile.**
  Navigators emphasize the FPL-banded repayment limit on excess
  APTC ($375 / $950 / $1,575 / unlimited at higher FPL bands as
  of authoring), but the limit only applies if MAGI ends the year
  below 400% FPL. An asker who projects 320% FPL in November,
  receives full APTC all year, and earns a year-end bonus that
  pushes annual MAGI to 410% FPL owes back the *entire* APTC —
  often $8,000–$15,000 — with no cap. Trigger: a Navigator
  workflow that ends at the MAGI projection without surfacing
  "what if your income comes in higher." Failure mode: the asker
  treats the projected APTC as a settled subsidy; the year-end
  reconciliation surprises them with a $12,000 IRS bill they
  didn't budget for and have no income-smoothing remedy on. Per
  `blindspots.md` F3-class trap. Recovery: explicit
  "what's your variance scenario" probe during MAGI projection;
  for high-variance askers (commission income, RSU vest schedule,
  side-business income, capital gains), recommend opting for
  reduced APTC mid-year with the option to claim the residual
  PTC at filing.

- **CSR-eligibility is a hard step-function and bad advice ports
  across FPL bands.** CSR raises silver-plan AV from 70% to 94%
  at <150% FPL, 87% at 150–200% FPL, 73% at 200–250% FPL, and 0%
  (no CSR) above 250% FPL. The advice "buy silver to get CSR" is
  correct below 250% FPL and structurally wrong at 251% FPL. A
  Navigator who internalized the "silver good" pattern from
  low-income casework can mis-route a 280% FPL asker into silver
  when gold's lower OOP-max would dominate; the silver plan at
  no-CSR levels has the worst price-performance in the metal-tier
  ladder due to silver-loading (CSR cost shifted to silver
  premium after CSR-payment cessation in 2017). Trigger:
  Navigator workflow that doesn't recompute the OOP-max-vs-
  premium trade-off across metal tiers for >250% FPL askers.
  Failure mode: 280% FPL asker enrolls in silver, doesn't get
  CSR, and pays both the silver-loaded premium AND silver-tier
  OOP-max — a strict Pareto loss vs gold. Recovery: at MAGI
  projection >250% FPL, run the metal-tier-comparison arithmetic
  on premium + expected OOP rather than defaulting to silver.

- **Non-expansion-state coverage gap routinely under-surfaced.**
  Ten states (as of authoring: Alabama, Florida, Georgia,
  Kansas, Mississippi, South Carolina, Tennessee, Texas, Wisconsin
  partial, Wyoming) have not expanded Medicaid under ACA §2001.
  Adults below 100% FPL in non-expansion states are *categorically
  ineligible for APTC* (the ACA assumed they'd be on expanded
  Medicaid) — they fall into the coverage gap. Trigger: a
  Navigator in a non-expansion state working with an asker at 80%
  FPL who is not categorically Medicaid-eligible (childless adult
  without disability). Failure mode: the asker is told "you don't
  qualify for help" without the Navigator surfacing the gap, the
  political context, or remedies (CHC sliding-fee-scale care,
  hospital financial assistance under §501(r), state-specific
  county-level programs). Recovery: explicit coverage-gap
  conversation in non-expansion states; route to FQHC sliding-
  fee-scale enrollment + §501(r) financial-assistance application
  + state county-level safety-net programs.

- **Family-glitch-fix awareness lag.** The IRS finalized the
  family-glitch fix (Rev. Proc. 2022-34, effective 2023 plan year)
  separating employer affordability for the employee from
  affordability for family members. The fix opened Marketplace
  APTC eligibility to spouses and children of workers whose
  family-coverage cost exceeds the affordability threshold (8.39%
  of household income at authoring) even where employee-only
  coverage is "affordable" on paper. Trigger: an HR / employee-
  benefits page or a 2022-era Navigator workflow that pre-dates
  the fix; asker is told "you have affordable employer coverage,
  no Marketplace APTC." Failure mode: a family-of-four with
  affordable employee-only coverage but unaffordable family
  coverage stays on employer family plan at $20,000+/year when
  spouse + kids could enroll Marketplace with substantial APTC.
  Recovery: at any D1 / D5 / D7 conversation involving family
  coverage and employer plans, run the family-glitch-fix
  affordability test explicitly on the family premium, not just
  employee-only.

- **Mixed-immigration-status household math interacts non-
  obviously with `immigration` domain rules.** APTC requires
  "lawfully present" status; some household members can be
  eligible and others not. The mixed-status calculation: APTC is
  computed on the tax-household FPL but applied only to lawfully-
  present applicants' premium share, with the "household
  contribution" allocated proportionally. DACA recipients'
  Marketplace eligibility status is in active litigation (post-
  2024 final rule, partial vacatur, partial reinstatement —
  current posture should be checked against `framings.md` F3 and
  the immigration domain's `decisions.md` D3). Trigger: a
  Navigator workflow that doesn't explicitly screen each
  household member's immigration status separately. Failure
  mode: the asker enrolls under a misclassification, faces a
  reconciliation surprise at filing, or fails to enroll a
  family member who was actually eligible. Recovery: route
  mixed-status household cases to a Navigator with cross-domain
  immigration literacy and verify each member's status against
  USCIS evidence; cross-domain edge with `immigration` domain
  D3 / D5 — see `framings.md` cross-domain edges block.

- **State-based-exchange jurisdiction routinely confused on
  national Healthcare.gov-centric resources.** Healthcare.gov
  serves only the 32 FFE states; 18 states + DC run their own
  SBE platforms with different SEP-trigger interpretations,
  different consumer-help workflows, and different subsidy-
  supplement programs (California Premium Subsidy, NY Essential
  Plan, MA Health Connector ConnectorCare). Trigger: a national-
  audience consumer-help article that says "go to Healthcare.gov"
  to a California / New York / Washington asker. Failure mode:
  the asker hits a state-redirect they don't understand, abandons
  the workflow, or misses an SBE-only SEP trigger. Recovery: at
  the start of any Marketplace conversation, identify the
  asker's state of residence and route to the correct platform
  (FFE = Healthcare.gov; SBE = the specific SBE URL).

## Mechanism E posture

Health-insurance is `high_stakes: true` per `_meta_ontology.md` §4.
Every blindspot above ends with a Recovery move routed to a named
professional channel. For aca-marketplace-and-navigator-sourced
framings the default channel is a **CMS-trained Marketplace
Navigator (or state-based-exchange equivalent — Certified Enrollment
Counselor / CEC in CA, etc.) for D5 plan-selection and SEP-trigger
decisions** — structurally prohibited from steering, federally-
funded, with explicit cross-checking against employer-side
affordability and Medicaid-eligibility-first logic. Where the
decision crosses into employer-plan affordability (D7), Mechanism
E pairs the Navigator with the asker's HR or benefits administrator
for current-plan-year documentation; where the decision crosses
into mixed-immigration-status (D3 / D5 boundary with `immigration`
domain), to a Navigator with immigration-status literacy plus
an immigration attorney for status-determination questions; where
the decision crosses into post-enrollment denial or surprise-
billing recovery (D7 / D9), to **patient-advocate channels**
(`sources.yaml` community `patient-advocacy-and-billing-recovery`)
or the **state insurance commissioner** (where the plan is fully-
insured, not ERISA self-funded). This community is the subsidy-
arithmetic-and-enrollment-workflow layer; the named professional
with the asker's MAGI projection, household composition, and
state-platform-jurisdiction is the binding-determination layer.
