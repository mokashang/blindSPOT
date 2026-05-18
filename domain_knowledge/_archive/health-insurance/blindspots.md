# health-insurance — blindspots.md (Layer 3)

Blindspot catalogue for `health-insurance`. Each entry names what a real
practitioner in the relevant framing would say is missed — anchored to
either an `Excludes` line in [`framings.md`](./framings.md) or to the
conceptual community-class voice anchors named in `framings.md`
(actuarial-and-broker, SHIBA / SHIP volunteer, ACA-Navigator,
HSA-administrator, ERISA-attorney, healthcare-economics-journalist
voice — Kliff / Rovner / Sanger-Katz / Ornstein, Bogleheads,
HR-Reddit, KFF, PNHP, patient-advocate / billing-error-recovery voice,
Galen / AEI, chronic-illness patient). Per [`_schema.md`](../_schema.md),
every entry is relative to a framing and ships with a trigger pattern
and a concrete recovery move.

The `health-insurance` domain is **high_stakes: true** per
[`_meta_ontology.md` §4](../_meta_ontology.md). Per
[ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating),
**every Recovery move below routes to one of the following professional-
counsel categories — a licensed health-insurance broker, a SHIBA / SHIP
volunteer (State Health Insurance Assistance Program — federally funded
non-commissioned Medicare counselor), an ACA-Marketplace Navigator
(CMS-trained, prohibited from steering), a CPA (HSA / FSA / Form 8889 /
Form 8962 coordination), an ERISA-litigation attorney (denial-of-claim
appeal on self-funded employer plans), or the State Insurance
Commissioner (STLDI rescission complaint, fully-insured-plan grievance,
external review).** This is **uniform Mechanism E gating** like
immigration (PR #48), not partial-gating like housing (PR #64) — the
two distinct classes of irrevocability driving the high-stakes posture
(per `framings.md` intro) are the **12-month plan-year lock-in** on
commercial / marketplace plans (the wrong choice compounds for up to a
year of uncapped out-of-network exposure) and the **permanent
Medicare-side penalty regime** (Part B 10%-per-12-months-late permanent
premium add; Medigap Guaranteed-Issue window expires 6 months after
Part B effective date, after which underwriting denies common chronic
conditions). The wrong call here is not recoverable on a multi-year
horizon: missed IEP triggers lifetime Medicare premium loading; missed
60-day marketplace SEP forecloses coverage until next open enrollment;
post-claim STLDI rescission converts a $200k cancer bill from
"insured" to "uninsured" retroactively. This file is decision-support
pointing at where the analysis happens — the binding determination is
the broker's / SHIBA volunteer's / Navigator's / CPA's / ERISA attorney's,
applied to the asker's full medical and income picture, the current
Summary Plan Description (SPD), the current Healthcare.gov regulatory
posture, and the current IRS / CMS revenue rulings.

Each blindspot lists:
- **Statement** — one sentence naming what is missed
- **Source evidence** — the framing-Excludes anchor or community-class
  voice-anchor reference this blindspot was extracted from (not
  invented; no purely-LLM-extrapolated entries)
- **Trigger** — the situation pattern the Triage / Risk Officer should
  match against
- **Failure mode** — the specific bad outcome if the blindspot stays
  unsurfaced (12-month-lock-in OOP-cap blowout, permanent Medicare
  Part-B 10%/year penalty, retro-rescission of STLDI plan, denial-
  appeal deadline missed, etc.)
- **Recovery move** — the concrete action that resolves it, routing to
  one of the Mechanism E professional-counsel categories above

The framing names below match [`framings.md`](./framings.md) exactly;
all 14 are covered with ≥ 5 entries each (≥ 70 total). Voice anchors
are conceptual — the source-views in
`domain_knowledge/health-insurance/sources.yaml` are not yet authored,
so attribution is to the *class* of community (actuarial-and-broker
voice, SHIBA / SHIP volunteer voice, ACA-Navigator voice, HSA-
administrator voice, ERISA-attorney voice, healthcare-economics-
journalist voice, Bogleheads voice, HR-Reddit voice, KFF / Health
Affairs voice, PNHP single-payer voice, patient-advocate / billing-
error-recovery voice, conservative-policy / Galen / AEI voice, chronic-
illness / disability patient voice). When `sources.yaml` lands,
source-evidence lines below should be tightened to the specific
source-view ids.

---

## 1. Expected-utilization-arithmetic framing

### 1.1 Embedded vs aggregate family deductible structures look identical until the SPD says otherwise

- **Statement**: The framing's 3-scenario probability-weighted table
  treats utilization as scalar, missing that *who* utilizes within a
  family materially changes the embedded-individual-OOP-max
  calculation. A $40k surgery on the high-utilizing child caps at the
  embedded individual OOP-max (~$9,450 self-only ceiling for 2026) on
  an embedded plan, but on an aggregate-deductible plan the family
  must spend the full family deductible across all members before
  anything pays — the arithmetic looks identical until you read the
  SPD carefully.
- **Source evidence**: `framings.md` §1 Excludes line on treating
  utilization as scalar and missing the embedded-vs-aggregate
  distinction; reinforced by actuarial-and-broker voice on SPD-level
  structure variation.
- **Trigger**: Asker reports a family-tier plan choice AND mentions a
  high-utilizing family member (chronic condition in child / spouse;
  upcoming surgery; pregnancy) AND has not separately verified the
  family deductible is "embedded" not "aggregate."
- **Failure mode**: Asker picks the lower-premium aggregate-deductible
  plan; the high-utilizing member's $40k surgery counts toward the
  family deductible but no member-level cap applies; the rest of the
  family pays first-dollar on all care through the calendar year while
  the family deductible burns through; total OOP exceeds the embedded-
  plan equivalent by $10–20k. The 12-month lock-in forecloses
  switching mid-year except via a narrow QLE.
- **Recovery move**: Pull the SPD (Summary Plan Description) for each
  candidate plan and identify the family-deductible structure
  (aggregate vs embedded vs ACA-mandated embedded individual OOP-max
  sub-limit per 2016 CMS rule); compute the high-utilizer scenario
  on each structure; consult a licensed health-insurance broker with
  the SPD-level structure documents before committing during the
  12-month plan-year lock-in.

### 1.2 Out-of-network OOP-max is structurally absent from many narrow-network plans

- **Statement**: Many HMOs, EPOs, and narrow-network silver plans have
  *no* out-of-network OOP-max at all — you eat the entire bill if
  care is out-of-network and not an emergency under No Surprises Act
  protections, and the framing's "the tail is capped" reassurance
  evaporates when in-network specialist availability is thin.
- **Source evidence**: `framings.md` §1 Excludes line on out-of-network
  OOP-max being structurally absent from the framing's scenario
  tables; reinforced by patient-advocate / billing-error-recovery
  voice (NAHAC, AdvoConnection, Marshall Allen's *Never Pay the First
  Bill* lineage).
- **Trigger**: Asker is choosing among marketplace narrow-network
  silvers or an HMO/EPO at OE AND reasons about catastrophic
  protection using a single "OOP-max" number AND has a specialist
  need (oncology, transplant, rare-disease care, gender-affirming
  surgery, advanced fertility) where in-network availability is
  thin.
- **Failure mode**: Asker's required specialist isn't in-network; the
  framing's "$9,450 worst case" calculus doesn't apply because the
  out-of-network track has no cap; the catastrophic event generates a
  $200k+ balance-billed bill that No Surprises Act doesn't cover (the
  Act covers emergency, anesthesia, and certain facility-based
  ancillaries, not elective specialist care chosen by the patient);
  asker faces medical bankruptcy adjacency.
- **Recovery move**: Before committing during OE, for every narrow-
  network plan candidate explicitly check the SPD for out-of-network
  OOP-max language ("no maximum" / "100% of charges after
  out-of-network deductible" is the red flag); confirm the asker's
  required specialists are in-network with the specialist's office
  directly (provider directories are systematically wrong); if
  in-network specialist availability is thin, consult a licensed
  health-insurance broker on whether a broader-network PPO with
  out-of-network OOP-max is worth the premium delta.

### 1.3 Prescription-drug benefits often sit on a parallel cost track with a separate OOP-max

- **Statement**: On many plans the prescription-drug benefit has a
  separate deductible, separate copay structure, separate specialty-
  tier formulary, and on a non-trivial subset of plans a *separate*
  prescription OOP-max. The framing's "the plan covers everything
  once OOP-max is met" is materially wrong for the specialty-drug /
  biologic patient whose $10k/month medication continues to copay-
  tier after the medical OOP-max is hit.
- **Source evidence**: `framings.md` §1 Excludes line on prescription
  drugs sitting on a parallel cost track with separate OOP-max on
  some plans; chronic-illness / disability patient voice
  (r/ChronicIllness, r/Disability) on formulary-tier reality.
- **Trigger**: Asker takes a specialty drug or biologic ($1k+/month
  list price) AND is choosing between plans on the basis of medical
  OOP-max alone AND has not separately verified the formulary tier
  and pharmacy OOP-max integration.
- **Failure mode**: Asker hits medical OOP-max in March; specialty
  drug continues at 30% coinsurance on tier-4 specialty for the rest
  of the calendar year; annual OOP exceeds the "capped" amount by
  $20k+; the 12-month lock-in forecloses switching to a plan with
  integrated OOP-max.
- **Recovery move**: For every plan candidate, pull the formulary
  document and locate the asker's specific drug; verify the tier,
  the cost-share, and whether the plan's prescription OOP-max is
  integrated with medical OOP-max or separate; consult a licensed
  health-insurance broker with the formulary documents and the
  asker's medication list before OE deadline.

### 1.4 Condition-onset risk is under-priced because the scenario table is static

- **Statement**: Probability weights for scenarios are calibrated from
  prior utilization — but the framing under-prices *condition-onset
  risk* (the 35-year-old with no chronic disease may be a 36-year-old
  with one, and the OE-locked-in HDHP becomes the wrong choice only
  after diagnosis closes the rescue door); the scenario table is a
  static snapshot of a dynamic process.
- **Source evidence**: `framings.md` §1 Excludes line on under-pricing
  condition-onset risk and the scenario table being a static snapshot
  of a dynamic process; reinforced by healthcare-economics-journalist
  voice (Sarah Kliff on diagnosis-as-financial-event reporting).
- **Trigger**: Asker is currently healthy with no chronic conditions,
  is choosing an HDHP largely on the basis of "low expected utilization,"
  AND has known family history of high-utilization conditions
  (diabetes, cancer, autoimmune, mental-health) OR is in an
  age-cohort where condition-onset probability is non-trivial (35+).
- **Failure mode**: Diagnosis mid-year converts the HDHP from "optimal
  expected-utilization plan" to "binding $1,650–$8,300 OOP exposure
  before coverage starts"; 12-month lock-in forecloses switching;
  asker pays full HDHP deductible during the diagnostic workup and
  initial treatment phase while the OE for switching to a low-
  deductible plan is months away.
- **Recovery move**: Include a "diagnosis-mid-year" scenario in the
  scenario table at non-zero probability (consult age- and family-
  history-adjusted incidence data); if the post-diagnosis HDHP cost
  is intolerable, prefer the lower-deductible plan even if the
  expected-utilization arithmetic favors HDHP; consult a licensed
  health-insurance broker on the trade-off and on whether a Marketplace-
  SEP exists for any forecastable mid-year diagnosis (none does for
  diagnosis alone — SEP requires a QLE, not a diagnosis).

### 1.5 Mental-health and substance-use treatment have parallel cost-sharing structures the framing rarely surfaces

- **Statement**: Mental-health and substance-use treatment have
  network adequacy, prior-authorization, and frequency-limit issues
  the framing's medical-utilization arithmetic doesn't surface.
  Federal MHPAEA (Mental Health Parity and Addiction Equity Act)
  requires parity between mental-health and medical/surgical benefits,
  but operational implementation varies widely — CMS audits find
  systematic prior-auth and frequency-limit disparities the asker's
  scenario table doesn't predict.
- **Source evidence**: `framings.md` §10 Excludes line on prior-auth
  burden being unevenly distributed across plans and specialties,
  with psychotherapy frequency caps and ABA-therapy hour limits as
  examples; chronic-illness patient voice on parity gaps in actual
  operational implementation.
- **Trigger**: Asker has known mental-health or substance-use care
  needs (current therapy, medication, recent diagnosis, family
  member needing ABA / SUD care) AND is comparing plans on medical
  OOP-max without separately verifying behavioral-health network
  adequacy and prior-auth burden.
- **Failure mode**: In-network therapist availability is thin (CMS
  audits show 30–50% of listed mental-health providers either not
  accepting new patients or no longer in network); asker pays
  out-of-network or self-pay; behavioral-health spend doesn't count
  toward medical OOP-max in the same way; total annual OOP exceeds
  the calculated worst-case by thousands.
- **Recovery move**: For asker with behavioral-health care needs,
  separately verify in-network behavioral-health provider acceptance
  (phone the providers, do not trust the directory), confirm visit-
  frequency limits and prior-auth requirements on the SPD, and
  evaluate whether broader-network plans or marketplace plans with
  better behavioral-health network adequacy are worth the premium
  delta; consult a licensed health-insurance broker on the trade-off
  AND consider filing a State Insurance Commissioner complaint if
  the asker discovers a current-plan parity violation.

---

## 2. Risk-transfer-and-OOP-cap framing

### 2.1 The ACA OOP cap applies only to in-network EHB; non-EHB and out-of-network sit outside

- **Statement**: The ACA OOP cap applies only to in-network EHB-
  classified care; out-of-network specialty care, non-EHB services
  (LASIK, some fertility procedures, cosmetic-adjacent),
  balance-billing on emergency air-ambulance / out-of-network
  anesthesia or pathology (despite No Surprises Act protections,
  edge cases persist for ground ambulance and certain free-standing
  facilities) sit outside the OOP-max for many plans. The framing's
  "ACA caps your downside at $9,450" reassurance fails on excluded
  service classes.
- **Source evidence**: `framings.md` §2 Excludes line on ACA OOP cap
  applying only to in-network EHB; patient-advocate / billing-error-
  recovery voice on edge cases of No Surprises Act §2799A enforcement.
- **Trigger**: Asker reasons about catastrophic exposure citing the
  ACA OOP cap ($9,450 self-only / $18,900 family for 2026) AND has
  a near-term need for any of (a) elective fertility treatment, (b)
  bariatric surgery, (c) ground-ambulance transport, (d) services at
  free-standing facilities, (e) any care at an out-of-network
  facility chosen non-emergently.
- **Failure mode**: Asker incurs $40k+ in non-EHB or balance-billed
  charges that don't accumulate against OOP-max; asker's "I'm capped
  at $9,450" mental model produces a catastrophic OOP surprise that
  consumes savings or routes to medical-debt; 12-month lock-in
  forecloses switching to a plan that covers the specific service
  category.
- **Recovery move**: For every near-term elective or specialized
  service, verify EHB classification AND in-network coverage AND
  No-Surprises-Act applicability AND OOP-accumulation rules in the
  SPD; for non-EHB services, get a written cost-share estimate from
  the plan and the provider in advance; consult a patient-advocate
  / billing-error-recovery service (NAHAC, AdvoConnection) for any
  estimated exposure above $5k, AND consult a licensed health-
  insurance broker on whether a different plan structure (e.g.
  PPO with broader EHB coverage, or specialty rider) is available.

### 2.2 The calendar-year reset is itself a planning event the framing rarely names

- **Statement**: The framing treats the OOP-max as a per-calendar-year
  reset that's a clean insurance event; misses that the *clock-reset*
  (January 1 deductible reset) is itself a planning event — the
  patient mid-treatment in December whose chemo-induced labs run
  weekly may pay $300/visit out-of-pocket all of January even though
  the November tax-year-prior labs were $0-cost-after-OOP-max.
- **Source evidence**: `framings.md` §2 Excludes line on calendar-
  year reset trap; chronic-illness patient voice (r/ChronicIllness,
  r/Disability) on the December-to-January transition as a known
  patient-finance crisis pattern.
- **Trigger**: Asker is mid-treatment for an ongoing condition (cancer,
  autoimmune flare, post-surgical recovery, high-risk pregnancy in
  Q4) AND has hit OOP-max in the current calendar year AND is
  approaching January 1 without explicit Q1-cashflow planning.
- **Failure mode**: January 1 reset; asker faces full deductible
  ($1,650–$8,300) plus coinsurance through deductible-met in Q1;
  cashflow shock during active treatment; care delays from copay
  surprise; the framing's "OOP-max caps your downside" was true for
  CY1 and false for CY2 within the same illness episode.
- **Recovery move**: For asker mid-treatment in Q4, model the January
  reset explicitly — project Q1 OOP exposure under the renewing plan
  and compare to alternative plan structures (HMO with lower
  deductible, gold-tier marketplace if OE allows switch); pull
  forward elective-but-deferrable care into the current calendar
  year if possible to amortize against the already-met OOP-max;
  consult a licensed health-insurance broker on Q4-into-Q1 timing
  strategies AND consult a patient-advocate / billing-error-recovery
  service on payment-plan options for Q1 exposure.

### 2.3 Asset liquidity is a separate question from asset magnitude

- **Statement**: The "absorb the catastrophic exposure" framing
  routes high-income, high-asset askers toward HDHP + self-insurance
  for the sub-OOP-max gap (e.g. "$8k deductible is rounding error on
  $500k net worth"); the framing rarely asks whether asset-
  composition matters — illiquid 401k, locked-up equity grants, or
  home equity is harder to deploy for a $50k surprise bill than the
  cash-on-balance-sheet picture suggests.
- **Source evidence**: `framings.md` §2 Excludes line on asset-
  composition mattering; Bogleheads-meets-health-insurance voice on
  emergency-fund liquidity discipline separate from net-worth
  aggregate.
- **Trigger**: Asker is high-net-worth on paper ($500k+) but with
  most assets in 401k / equity grants / home equity / illiquid
  startup equity AND is being advised to absorb HDHP catastrophic
  exposure on the basis of headline net worth.
- **Failure mode**: Catastrophic event ($40k OOP exposure); cash
  emergency fund insufficient; 401k early-withdrawal triggers 10%
  penalty + ordinary income tax; equity grants illiquid until vest;
  home-equity-line setup takes 30–60 days the medical-bill cycle
  doesn't tolerate; asker ends up on a 24-month medical-bill payment
  plan despite "having the money."
- **Recovery move**: Compute the *liquid* emergency fund (cash +
  brokerage available within 7 days), not the headline net worth;
  if liquid funds don't cover 2× OOP-max comfortably, treat HDHP
  catastrophic exposure as not yet absorbable; consult a licensed
  health-insurance broker AND a CPA on the cash-flow-versus-tax-
  arbitrage trade-off before defaulting to HDHP on net-worth grounds
  alone.

### 2.4 Psychological-tail risk is real cost the dollar framing misses

- **Statement**: Even for askers with capacity to absorb a $9,450 hit,
  the cognitive load of a months-long claim / appeal / billing-error
  grind during a cancer-recovery phase is itself a cost the framing's
  pure-dollar arithmetic ignores. The chronic-illness-patient voice
  catches this; the actuarial-broker voice doesn't.
- **Source evidence**: `framings.md` §2 Excludes line on
  psychological tail risk being underweighted; chronic-illness
  patient voice on the cognitive cost of claim/appeal grind during
  active treatment.
- **Trigger**: Asker has a known stressor on cognitive bandwidth
  (caregiving for an aging parent, demanding job, child with
  special needs, single-parent household) AND is being routed to an
  HDHP largely on the basis that "you can absorb the OOP-max."
- **Failure mode**: Catastrophic event arrives; asker has dollar
  capacity but no time/bandwidth capacity; claims pile up unread;
  prior-auth deadlines missed; appeal windows lapsed; care delayed
  or skipped; total cost (financial + health-outcome) exceeds the
  PPO premium delta by orders of magnitude.
- **Recovery move**: Price the cognitive-load tail explicitly when
  choosing between HDHP-and-self-insure vs PPO-with-copay-
  predictability; for asker with high cognitive-load competing
  demands, prefer the higher-premium / lower-procedural-burden
  plan; consult a licensed health-insurance broker on plan-level
  procedural-burden differences (copay vs coinsurance, prior-auth
  density, in-network breadth) AND budget for a patient-advocate
  service ($50–200/month or hourly) as part of the cost of HDHP if
  chosen.

### 2.5 STLDI and healthcare-sharing-ministry "coverage" carry retroactive-rescission risk the OOP-cap framing doesn't engage

- **Statement**: STLDI (Short-Term Limited-Duration Insurance) and
  healthcare-sharing-ministry "coverage" are not insurance —
  STLDI can be retroactively rescinded post-claim for any pre-
  existing-condition the asker didn't disclose (including conditions
  the asker didn't know they had); sharing ministries discretionarily
  decline to share for lifestyle-attestation violations or "non-
  Biblical" conditions. The OOP-cap framing's "absence of cap is the
  red flag" understates the retroactive-rescission risk that converts
  $200k in "covered" claims back to "uninsured" months after the
  fact.
- **Source evidence**: `framings.md` §2 Excludes line implicitly via
  the "no OOP cap" red flag for STLDI / sharing ministries;
  `framings.md` §9 Excludes line on sharing-ministry discretion;
  healthcare-economics-journalist voice (ProPublica, Charles
  Ornstein) on post-claim rescission cases.
- **Trigger**: Asker is considering STLDI or healthcare-sharing-
  ministry coverage on price grounds AND has any condition they
  could plausibly have (diabetes, depression, anxiety, ADHD,
  autoimmune, prior cancer, chronic medication) — including
  undiagnosed.
- **Failure mode**: Major medical event ($200k cancer dx);
  STLDI carrier rescinds back to enrollment date for "material
  misrepresentation" on a condition the asker either didn't know
  about or didn't realize was disclosable; asker is retroactively
  uninsured for the entire claim period; medical bankruptcy
  adjacency.
- **Recovery move**: For any asker considering STLDI or sharing
  ministry, surface the rescission risk explicitly AND consult a
  licensed health-insurance broker on ACA-compliant alternatives
  (including catastrophic plans for under-30 / hardship-exemption
  askers); if STLDI / sharing-ministry is the only affordable
  option, document every potentially-disclosable condition on the
  application with overwhelming completeness; file a State Insurance
  Commissioner complaint immediately upon any post-claim rescission
  attempt (state SIDs have limited but real authority on STLDI
  marketed in-state).

---

## 3. HSA-as-retirement-vehicle framing

### 3.1 The "pay OOP, let HSA compound" strategy requires liquidity the framing rarely verifies

- **Statement**: The "pay OOP, let HSA compound" strategy assumes the
  asker has sufficient taxable savings to fund current medical
  without raiding the HSA; for askers with cash-flow constraints
  (early-career, paying down debt, single-income household with
  kids), the prescription is correct in theory and infeasible in
  practice, and the framing rarely degrades-gracefully to "if you
  can't bank the receipts, just use the HSA for current spend — you
  still get the tax deduction."
- **Source evidence**: `framings.md` §3 Excludes line on the
  cash-flow-constraint mismatch; HR-Reddit voice (r/personalfinance
  benefits megathread, r/HumanResources) on the practical-cash-flow
  pushback against Bogleheads-style HSA maximalism.
- **Trigger**: Asker is being advised to "max the HSA and pay
  current medical OOP" AND has any of (a) student loan debt,
  (b) credit-card balance, (c) sub-$10k emergency fund,
  (d) single-income household with dependents, (e) gig/1099
  income that varies month-to-month.
- **Failure mode**: Asker maxes HSA per advice; lacks cash to pay
  current $3k OOP medical bill; raids HSA early (still tax-free for
  qualified) which negates compounding; OR uses credit card at 22%
  APR which destroys the after-tax IRR the framing was optimizing;
  OR skips care entirely which compounds into worse health outcome
  later.
- **Recovery move**: Verify liquid-savings capacity before applying
  the "pay OOP, let HSA compound" strategy; if cash-flow-constrained,
  use the HSA for current medical spend (still gets the above-the-
  line deduction) and treat any leftover contribution as the
  compounding bucket; consult a licensed health-insurance broker
  on HSA contribution sizing AND a CPA on Form 8889 documentation
  for the specific reimbursement pattern.

### 3.2 The receipt-shoebox strategy has a 20-year operational cost

- **Statement**: The "shoebox the receipts" decades-deferred
  reimbursement requires holding receipts, EOBs, and proof-of-non-
  reimbursement for 20+ years against potential IRS audit; the
  practical record-keeping burden is non-trivial, and most HSA
  administrators don't archive this; the framing's "just save the
  receipts" understates the operational cost.
- **Source evidence**: `framings.md` §3 Excludes line on receipt-
  shoebox-burden being understated; HSA-administrator voice
  (HealthEquity / Fidelity / Lively) on the documentation gap.
- **Trigger**: Asker is being advised to bank receipts for decades-
  later HSA reimbursement AND has no current digital archive
  practice AND has not surfaced the document-retention burden.
- **Failure mode**: 15 years later, asker wants to reimburse $80k
  in accumulated qualified medical expenses; HSA administrator no
  longer has the records; asker has lost or never digitized the
  paper receipts; IRS audit (rare but possible) requires substantiation
  the asker can't produce; the "tax-free reimbursement" becomes
  taxable distribution + 20% penalty (before 65) or just taxable
  ordinary income (after 65).
- **Recovery move**: Set up a durable digital archive workflow
  (cloud-based folder with year-tagged subfolders, automated EOB
  download from carrier portal, scanned receipts) from year-1 of
  HSA contributions; verify the asker's discipline against this
  workflow before relying on the receipt-shoebox strategy; consult
  a CPA on Form 8889 documentation requirements AND IRS
  substantiation standards for qualified-medical-expense
  reimbursement.

### 3.3 Medicare Part A enrollment retroactively invalidates HSA contributions

- **Statement**: HSA-eligibility is fragile: any non-HDHP coverage
  (general-purpose FSA, spouse's FSA, Medicare Part A, VA care
  within prior 3 months, Tricare, primary-care services via DPC
  that aren't structured as ancillary) disqualifies the asker from
  contributing — AND Medicare Part A enrollment is *retroactive up
  to 6 months* when SS-claiming after 65, which silently invalidates
  6 months of HSA contributions the framing's "max until SS-claim"
  timing doesn't catch.
- **Source evidence**: `framings.md` §3 Excludes line on Medicare-
  Part-A-retroactivity invalidating HSA contributions; SHIBA / SHIP
  volunteer voice on the under-65-SS-claim trigger as a known
  HSA-disqualification trap.
- **Trigger**: Asker is approaching 65 AND is claiming Social
  Security at or after 65 (which auto-enrolls Part A retroactively)
  AND is continuing HSA contributions on the assumption that
  "I'm not on Medicare yet."
- **Failure mode**: SS-claim at 66.5 retroactively enrolls Part A
  back to 6 months prior; 6 months of HSA contributions are now
  excess contributions subject to 6% annual excise tax until
  withdrawn; if not withdrawn by Oct 15 of the year, the asker owes
  the 6% on the excess every year until removed; the framing's
  "you have until Medicare enrollment" was off by 6 months.
- **Recovery move**: For any asker 64+ contemplating SS-claim,
  surface the Part-A-retroactivity rule explicitly AND stop HSA
  contributions at least 6 months before planned SS-claim date;
  if SS-claim is already filed and retroactive Part A enrollment
  is in effect, consult a CPA on excess-contribution withdrawal
  by Oct 15 of the affected tax year AND a SHIBA / SHIP volunteer
  on the Medicare-side timing.

### 3.4 The retirement-vehicle framing biases toward deferral even when reimburse-as-you-go is better

- **Statement**: The retirement-vehicle framing assumes the asker
  reaches retirement having accumulated medical expenses to
  reimburse against; for an asker with major medical events in
  their 30s and 40s, the optimal play may be reimburse-as-you-go
  rather than shoebox — the tax-free withdrawal is identical, the
  compounding lost is real, and the framing's bias toward deferral
  can be myopic for asker-specific health trajectories.
- **Source evidence**: `framings.md` §3 Excludes line on retirement-
  vehicle framing's deferral bias being myopic for asker-specific
  health trajectories; Bogleheads voice (with the chronic-illness
  patient voice as the corrective).
- **Trigger**: Asker has a known chronic condition with ongoing
  medical spend ($10k+/year) AND is being advised to bank receipts
  for decades-later reimbursement on Bogleheads-style framing.
- **Failure mode**: Asker pays current medical from after-tax
  cash flow (worsening the cash-flow constraint) while HSA balance
  grows tax-deferred; asker dies or experiences major HSA-
  administrator failure before reimbursing; OR the decades-later
  reimbursement compounds at 7% real but the after-tax marginal
  utility of those dollars is lower than current spend on care
  quality.
- **Recovery move**: Model the chronic-condition asker's lifetime
  medical spend trajectory explicitly; if current medical spend
  is consistently $10k+/year, treat the HSA as a current-spend
  bucket (still gets the deduction) rather than a 30-year
  compounding bucket; consult a CPA on the marginal-utility
  trade-off and Form 8889 documentation for the reimbursement
  pattern AND a licensed health-insurance broker on whether the
  HDHP-required HSA-eligibility is even the right plan choice
  for the asker's actual utilization.

### 3.5 DPC and direct-pay arrangements may disqualify HSA contributions

- **Statement**: Direct-Primary-Care (DPC) memberships and direct-pay
  primary-care arrangements that aren't structured as ancillary to
  an HDHP may disqualify the asker from HSA contributions under
  current IRS guidance — DPC is treated as a second health plan in
  some interpretations, making the HDHP no longer the asker's sole
  coverage. The framing's "HSA-eligible" reflex doesn't engage the
  DPC-disqualification ambiguity.
- **Source evidence**: `framings.md` §3 Excludes line implicitly via
  the "any non-HDHP coverage disqualifies" enumeration; HSA-
  administrator voice on DPC disqualification ambiguity (IRS
  Notice 2013-54 and subsequent guidance lag).
- **Trigger**: Asker has or is considering a DPC membership or
  direct-pay primary-care arrangement AND is on an HDHP with HSA
  contributions AND has not verified DPC-vs-HSA compatibility under
  current IRS guidance.
- **Failure mode**: IRS audit determines DPC membership disqualified
  HSA contributions for prior tax years; excess-contribution 6%
  excise tax applies annually until removed; the framing's "HSA-
  eligible" reflex created a years-long latent tax liability.
- **Recovery move**: For any asker with a DPC or direct-pay
  primary-care arrangement, verify HSA compatibility with a CPA
  who tracks current IRS guidance on DPC-and-HSA (this is an
  evolving area — pending congressional legislation could
  formalize compatibility); if guidance is unclear, suspend HSA
  contributions until the question is resolved AND consult a
  licensed health-insurance broker on the plan-design trade-off.

---

## 4. Immediate-cost-and-cash-flow framing

### 4.1 Underinsurance is the structural design, not an accident

- **Statement**: The framing's premium-minimization bias routes
  askers into plans with high deductibles AND high cost-sharing-
  after-deductible (silver-bronze gap) where the structural design
  *expects* enrollee skipping-of-care to balance the actuarial pool
  — the well-documented "underinsurance" pattern where the
  formally-insured nonetheless face medical debt. The framing's
  "cheapest premium that gets me a network" reflex doesn't surface
  the underinsurance trap.
- **Source evidence**: `framings.md` §4 Excludes line on
  underinsurance being structural; KFF / Commonwealth Fund voice
  on the underinsurance research literature (Sara Collins et al.,
  Commonwealth Fund Biennial Health Insurance Survey).
- **Trigger**: Asker is at 250–400% FPL income AND is comparing
  marketplace plans largely on premium AND has not surfaced the
  silver-bronze cost-sharing gap (where bronze AV is 60% and silver
  AV is 70% — a 10-point AV gap that compounds into thousands of
  OOP differential).
- **Failure mode**: Asker picks the bronze plan to save $80/month
  in premium; major medical event yields $7k OOP on bronze vs
  $4k on silver (after cost-sharing-after-deductible asymmetry);
  asker carries medical debt for years; the headline premium savings
  ($960/year) is consumed many times over.
- **Recovery move**: Compute the full annual cost (premium +
  expected OOP) under at least 3 utilization scenarios (zero, modal,
  high) for each plan; if the asker's income lands in 100–250% FPL,
  silver-CSR-94/87/73 strictly dominates bronze on after-cost-share
  basis; consult an ACA-Marketplace Navigator on the silver-CSR
  loading mechanics AND a licensed health-insurance broker if
  cross-plan-type comparison is needed.

### 4.2 Skipping care to save copay is a chronic-condition cliff

- **Statement**: "Skipping care to save the copay" is rational at
  the monthly-budget level and catastrophic at the chronic-condition
  level — the framing has no native vocabulary for the diabetes /
  hypertension / depression patient whose foregone primary care
  converts to ER visit + admission six months later (the "moral
  hazard in reverse" pattern). The patient-advocate voice catches
  this; the cash-flow voice doesn't.
- **Source evidence**: `framings.md` §4 Excludes line on skipping-
  care-to-save-copay being catastrophic for chronic conditions;
  patient-advocate / billing-error-recovery voice on
  primary-care-to-ER cost cascade.
- **Trigger**: Asker has known chronic condition (diabetes,
  hypertension, mental-health) AND is choosing a plan on premium-
  minimization AND has surfaced "I'll just skip the copay visits"
  as a coping strategy.
- **Failure mode**: Asker skips primary-care follow-up to save the
  $40 copay; medication adherence drops; A1c climbs; ER visit at
  18 months for hypoglycemic event or hypertensive crisis; $20k
  inpatient admission counts against deductible but is the wrong
  side of the cost-benefit math the framing was optimizing.
- **Recovery move**: For asker with chronic condition, prioritize
  plan structures that minimize chronic-care cost-sharing (look
  for $0-copay primary care, $5-copay generics, $0-copay chronic-
  disease-management visits — many marketplace silver-CSR plans
  have these); avoid HDHP-with-deductible-applies-to-everything
  structures; consult a licensed health-insurance broker on plan-
  level chronic-care benefit design AND a patient-advocate service
  on patient-assistance programs (manufacturer copay cards, RX
  patient assistance) that can offset the cost-sharing gap.

### 4.3 Mid-year SEP changes don't auto-evaluate at next OE

- **Statement**: The marketplace-as-floor framing under-weights
  *coverage gaps* during the marketplace SEP / OE transition
  windows; the asker who picks the cheapest silver-CSR mid-year via
  SEP and then experiences premium increase at year-end OE may not
  re-evaluate, treating the prior choice as locked-in even though
  OE is the chance to reassess against the prior year's actual
  utilization.
- **Source evidence**: `framings.md` §4 Excludes line on marketplace
  mid-year SEP plans not getting re-evaluated at OE; ACA-Marketplace
  Navigator voice on OE re-shopping discipline.
- **Trigger**: Asker enrolled mid-year via SEP (job loss, marriage,
  move) AND OE is approaching AND asker has not explicitly planned
  to re-shop AND the carrier has notified a premium increase or
  benefit change for the renewal year.
- **Failure mode**: Asker auto-renews via marketplace passive
  enrollment; new-year premium is 15% higher; benefit network
  has narrowed; the asker is locked into 12-month plan-year that
  is worse than alternatives available at OE; the prior-year
  utilization data that would have informed a better choice is
  unused.
- **Recovery move**: For every asker who enrolled mid-year via SEP,
  set a calendar reminder for the next OE (Nov 1–Jan 15 for
  federal marketplace) AND re-shop against the prior-year utilization
  data; consult an ACA-Marketplace Navigator before OE deadline on
  the silver-CSR-band landing if income has changed AND a licensed
  health-insurance broker if cross-marketplace plan comparison is
  warranted.

### 4.4 Variable-income askers need a different cash-flow framework

- **Statement**: Predictable monthly cost as the binding constraint
  is rational for stable-employment, stable-income asker — but for
  gig-economy / commission / 1099 askers whose income varies
  materially month-to-month, the FSA / HSA / APTC-projection
  machinery requires income-forecasting that the cash-flow framing's
  monthly-bucket vocabulary doesn't accommodate well.
- **Source evidence**: `framings.md` §4 Excludes line on variable-
  income askers needing different cash-flow framework; ACA-
  Marketplace Navigator voice on income-forecasting complexity for
  1099 askers.
- **Trigger**: Asker is gig / commission / 1099 / equity-comp-
  heavy AND is being advised on FSA election or APTC enrollment
  using stable-income assumptions.
- **Failure mode**: Asker projects $50k income; actual is $80k;
  APTC over-payment of $4k owed back at Form 8962 reconciliation
  (capped at $1,575 below 400% FPL; uncapped above); OR projects
  $80k and actual is $40k; eligible for Medicaid retroactively;
  marketplace coverage may have been duplicative; tax-time surprise
  in both directions.
- **Recovery move**: For variable-income askers, use the prior 2-3
  years' actual MAGI to bracket the income projection; revisit the
  APTC election quarterly via marketplace account update (income
  changes can be reported any time, not only at OE); consult an
  ACA-Marketplace Navigator on income-projection discipline AND a
  CPA on Form 8962 reconciliation projection before December 31 to
  surface any avoidable surprise.

### 4.5 Premium-tax-credit reconciliation can be a four-figure shock above 400% FPL

- **Statement**: APTC reconciliation on Form 8962 has *capped*
  repayment for under-projected MAGI below 400% FPL (the cap was
  intended as a hardship protection); above 400% FPL the repayment
  is uncapped and can be six-figure when ARPA-enhanced subsidies
  are in effect (the asker who under-projected income and received
  $25k/year of APTC on a benchmark-silver may owe the full $25k
  back). The framing's "true-up at tax time" doesn't surface the
  severity of the asymmetry above the cap.
- **Source evidence**: `framings.md` §12 Excludes line on APTC
  reconciliation cap asymmetry above 400% FPL; ACA-Marketplace
  Navigator voice on the under-projection trap.
- **Trigger**: Asker projects MAGI under 400% FPL AND has any
  income-event risk that could push MAGI over (equity vesting,
  Roth conversion, year-end bonus, RSU vest, capital-gain
  realization) AND has not modeled the unconditioned-cap exposure.
- **Failure mode**: MAGI lands at 405% FPL at year-end; ARPA-
  enhanced APTC reconciliation requires asker to repay the full
  year's advance subsidy ($15–25k for a family on benchmark-silver);
  tax-time refund becomes a four-figure-to-six-figure liability;
  cash-flow shock at filing.
- **Recovery move**: For asker near the 400% FPL threshold, monitor
  MAGI through Q3 and update marketplace income estimate before
  Q4; if MAGI is likely to cross the threshold, consider reducing
  the advance subsidy claim mid-year to reduce reconciliation
  exposure; consult a CPA on the Form 8962 reconciliation projection
  AND an ACA-Marketplace Navigator on the income-update mechanics
  via the marketplace account.

---

## 5. ACA-marketplace-subsidy-mechanics framing

### 5.1 Projected vs realized MAGI divergence invalidates the silver-CSR loading retroactively

- **Statement**: The silver-CSR-strict-dominance pattern at low
  income depends on the asker's actual MAGI landing in the 100–
  250% FPL window; for self-employed and equity-comp askers whose
  income is lumpy, the projected-MAGI at enrollment may diverge
  from realized-MAGI at year-end Form 8962 reconciliation — and
  the silver-CSR loading is *retroactively recalculated* at
  reconciliation in ways the framing's enrollment-time-
  optimization doesn't catch.
- **Source evidence**: `framings.md` §5 Excludes line on projected-
  vs-realized MAGI divergence invalidating silver-CSR loading
  retroactively; ACA-Marketplace Navigator voice on the silver-CSR
  reconciliation mechanics.
- **Trigger**: Asker is enrolled in silver-CSR-94/87/73 AV-loaded
  plan AND has variable income AND realized MAGI at year-end
  exceeds the CSR-band ceiling (250% FPL).
- **Failure mode**: Realized MAGI lands at 270% FPL; CSR-loading
  ineligible retroactively; asker's actual silver plan was sold
  at AV-87 but cost-sharing for the full year is reclaimed back
  to AV-70; Form 8962 reconciliation includes a clawback of the
  CSR benefit; tax-time surprise plus latent OOP exposure on
  already-paid care.
- **Recovery move**: For asker enrolled in silver-CSR plan with
  variable income, monitor MAGI through year-end; if income
  trajectory will exceed 250% FPL, consult an ACA-Marketplace
  Navigator on mid-year SEP options (income-change can trigger
  SEP for plan switch in some circumstances) AND a CPA on the
  Form 8962 reconciliation impact and tax-planning options.

### 5.2 ARPA / IRA enhanced subsidies have a sunset risk

- **Statement**: ARPA / IRA enhanced subsidies (the elimination of
  the 400%-FPL "subsidy cliff") have a sunset risk — they expire
  end of 2025 absent further congressional extension, and the
  framing's "no cliff to worry about above 400% FPL" requires
  annual verification of the current-year subsidy schedule. The
  cliff is back unless extended.
- **Source evidence**: `framings.md` §5 Excludes line on ARPA /
  IRA enhanced subsidy sunset risk; KFF / Health Affairs voice
  on the legislative-extension uncertainty.
- **Trigger**: Asker is above 400% FPL AND is being advised on
  marketplace plan choice using the post-ARPA-enhanced-subsidy
  framework AND OE is in a year where the enhanced subsidies are
  not yet legislatively extended.
- **Failure mode**: Enhanced subsidies expire; asker's income at
  450% FPL was paying $400/month under enhanced ARPA framework
  but reverts to $1,200/month under pre-ARPA cliff (full premium,
  no subsidy); asker doesn't re-evaluate at OE; the unexpected
  premium hike comes mid-year as the carrier bills the unsubsidized
  rate; 12-month lock-in compounds the surprise.
- **Recovery move**: At every OE, verify the current-year subsidy
  schedule per Healthcare.gov posted rules (do not assume prior-
  year enhanced subsidies still apply); for asker above 400% FPL,
  model both subsidized and unsubsidized scenarios before
  committing; consult an ACA-Marketplace Navigator on the
  current-year subsidy regime AND a licensed health-insurance
  broker on cross-marketplace plan comparison if subsidies expire.

### 5.3 Family-glitch fix opened a new APTC eligibility window

- **Statement**: The framing presents APTC as a clean dollar-
  amount-subsidy keyed to benchmark silver; misses that *family-
  glitch* fixes (the 2022 IRS rule that recalculated affordability
  test using family-tier premium rather than employee-only-
  premium) created a new APTC-eligibility window for family
  members of employees with employer-coverage that was
  "affordable" for the employee but not for dependents — Triage
  in mixed-coverage households should surface this explicitly.
- **Source evidence**: `framings.md` §5 Excludes line on family-
  glitch fix creating new APTC eligibility window; ACA-Marketplace
  Navigator voice on the post-2022 IRS rule and the mixed-coverage
  household enrollment pattern.
- **Trigger**: Asker is in a household where one member has
  employer coverage AND dependents are not on the employer plan
  due to high family-tier premium AND household has not evaluated
  APTC eligibility for the dependents on marketplace.
- **Failure mode**: Family pays full out-of-pocket marketplace
  premium for dependents OR leaves dependents uninsured;
  affordability test based on family-tier premium would have
  qualified the dependents for APTC since the 2022 rule change;
  the framing's "employer coverage means no APTC" reflex misses
  the family-glitch fix.
- **Recovery move**: For mixed-coverage household, run the
  affordability test using the family-tier premium (not employee-
  only) and verify APTC eligibility for dependents on marketplace;
  consult an ACA-Marketplace Navigator on the family-glitch-fix
  rule application AND a CPA on the Form 8962 reconciliation if
  the household claims APTC for dependents while the employee
  remains on the employer plan.

### 5.4 DACA vacatur restored pre-2024 exclusion mid-cycle

- **Statement**: DACA-recipient eligibility was briefly granted
  under the 2024 rule and vacated late 2025 (the Texas court's
  *Texas v. CMS* / *Texas v. HHS* vacatur restored pre-2024
  exclusion); the framing's "lawful presence is the rule" needs
  a status-as-of-current-rule check, and mixed-status households
  use a complex household-FPL calculation excluding undocumented
  members from numerator-coverage but including them in
  denominator-FPL.
- **Source evidence**: `framings.md` §5 Excludes line on DACA
  vacatur restoring pre-2024 exclusion; ACA-Marketplace Navigator
  voice on the post-vacatur mixed-status household enrollment
  pattern. Boundary `immigration`.
- **Trigger**: Asker is DACA recipient OR in mixed-status household
  with undocumented family member AND is being advised on ACA
  marketplace eligibility on the assumption of post-2024 rule.
- **Failure mode**: DACA-recipient asker enrolls on marketplace
  under 2024-rule assumption; vacatur applies; coverage retroactively
  terminated; APTC clawback at Form 8962; mid-year coverage gap
  with no SEP path.
- **Recovery move**: Verify current ACA-marketplace eligibility for
  DACA / mixed-status under current Healthcare.gov regulatory
  posture (which is the vacated-back-to-pre-2024 status as of late
  2025); for any DACA / mixed-status asker, consult an ACA-
  Marketplace Navigator with documented mixed-status experience AND
  a licensed immigration attorney on the status-cascade implications.

### 5.5 State-based exchanges and Healthcare.gov diverge on SEP and CSR mechanics

- **Statement**: The framing's "marketplace" vocabulary treats
  Healthcare.gov (federal) and state-based exchanges (CA / NY /
  WA / MD / others) as interchangeable; in practice SEP
  documentation requirements, CSR-loading rules, plan-cost-
  sharing standardization (some states standardize across all
  silver plans; federal does not), and enrollment-portal
  reliability differ materially.
- **Source evidence**: `framings.md` §5 Excludes line on SEP
  documentation varying between state-based and federal exchanges;
  ACA-Marketplace Navigator voice on the state-vs-federal exchange
  divergence.
- **Trigger**: Asker is on a state-based exchange AND is being
  advised using federal-Healthcare.gov framing OR vice versa; OR
  asker is moving between states with different exchange types.
- **Failure mode**: Asker assumes federal-rule SEP documentation
  pattern; state-based exchange requires different documentation
  or different deadlines; SEP closes without enrollment; asker
  uninsured for months until next OE; the framing's "60-day SEP
  with proof-of-loss" was approximate but jurisdiction-specific.
- **Recovery move**: Identify the asker's specific state exchange
  (or federal Healthcare.gov) AND verify SEP documentation,
  CSR-loading, and enrollment rules for that specific exchange;
  consult an ACA-Marketplace Navigator licensed in the asker's
  state AND a licensed health-insurance broker if state-specific
  plan-comparison is needed.

---

## 6. Medicare-enrollment-irreversibility framing

### 6.1 SSDI, ESRD, and ALS pathways have their own IEP / GI variants

- **Statement**: The framing assumes the asker enters at 65 with the
  standard decision; misses earlier-Medicare-eligibility pathways —
  SSDI 24-month-waiting-period (Medicare automatic at 25th month of
  disability), ESRD (end-stage renal disease, Medicare-eligible at
  3rd month of dialysis), ALS (Medicare-eligible at first SSDI
  check). Each has its own GI / IEP variant that the "turning 65"
  frame doesn't catch.
- **Source evidence**: `framings.md` §6 Excludes line on earlier-
  Medicare-eligibility pathways; SHIBA / SHIP volunteer voice on
  the under-65 Medicare-eligibility decision-support.
- **Trigger**: Asker is under 65 AND has any of (a) SSDI approval
  approaching 24-month waiting period, (b) ESRD diagnosis with
  dialysis, (c) ALS diagnosis, OR is the caregiver / family-decider
  for such an asker.
- **Failure mode**: Asker on SSDI doesn't realize Medicare auto-
  enrollment is happening at month 25; existing employer / COBRA /
  marketplace plan continues unnecessarily; HSA contributions
  retroactively invalidated by Part A; Medigap-GI window opens but
  asker doesn't know to use it; chronic-condition asker locked out
  of Medigap underwriting 6 months later.
- **Recovery move**: For any under-65 asker with SSDI / ESRD / ALS
  pathway, surface the early-Medicare-eligibility timing explicitly
  AND consult a SHIBA / SHIP volunteer (federally funded, non-
  commissioned Medicare counselor) on the IEP / GI variant for the
  specific pathway BEFORE the 25th month of SSDI or the 3rd month
  of dialysis or the first SSDI check on ALS.

### 6.2 Part-D creditability is a separate determination from Part-A

- **Statement**: Creditable-coverage status is presumptively yes for
  employer plans at ≥20 employees, BUT Part-D creditability is a
  separate determination requiring an annual employer-issued notice
  (29 CFR §423.56); the framing's "covered by my employer" doesn't
  separate Part-A integration from Part-D creditability, and the
  missed Part-D creditability notice triggers a separate Part-D
  late-enrollment penalty (1%-per-month, also lifetime). Many
  askers on COBRA past month 8 face both Part-B AND Part-D late-
  enrollment penalties stacking.
- **Source evidence**: `framings.md` §6 Excludes line on Part-D
  creditability being a separate determination; SHIBA / SHIP
  volunteer voice on the Part-D-creditability notice as a known
  trap.
- **Trigger**: Asker is approaching 65 AND on employer plan or COBRA
  AND has not separately verified Part-D creditability via the
  annual employer-issued notice.
- **Failure mode**: Asker delays Part D beyond 65 assuming employer
  drug coverage is creditable; drug coverage is in fact non-
  creditable (some employer plans have prescription benefits below
  Part-D actuarial equivalent); Part-D late-enrollment penalty
  accrues 1% per month; permanent premium loading; the framing's
  "I'm covered" was true for Part A but not Part D.
- **Recovery move**: For any asker approaching 65 on employer plan
  or COBRA, request the annual creditability notice from the plan
  administrator (employers are required to provide this); verify
  Part-D creditability explicitly; if non-creditable, enroll in
  Part D at IEP to avoid penalty; consult a SHIBA / SHIP volunteer
  on the creditability determination AND a licensed health-insurance
  broker on the Part-D plan choice (PDP standalone vs MA-PD bundled).

### 6.3 The MA trial right is procedurally fiddly and time-limited

- **Statement**: The "trial right" of MA-at-IEP-to-Original-Medicare-
  within-12-months is presented as a safety net; in practice the
  trial-right requires the asker to have enrolled in MA *at IEP*
  (not later), creates a one-time 12-month window of returning to
  Original-Medicare-with-Medigap-with-GI, and is procedurally
  fiddly. The framing's "you can always change your mind within a
  year" oversimplifies. Boundary `legal-disputes` for appeals of
  denied trial-right exercise.
- **Source evidence**: `framings.md` §6 Excludes line on MA-to-
  Original trial-right being procedurally fiddly; SHIBA / SHIP
  volunteer voice on trial-right paperwork.
- **Trigger**: Asker is in MA at IEP AND considering a return to
  Original Medicare + Medigap AND is within the 12-month trial-
  right window but past the AEP (Oct 15 – Dec 7) AND has not
  verified MA-Original-Medicare paperwork timing.
- **Failure mode**: Asker tries to exercise trial right outside
  the AEP window; carrier or CMS rejects the paperwork; trial
  right is interpreted as not exercised; asker is locked into
  MA for the rest of the calendar year; Medigap underwriting now
  required and may deny on chronic conditions.
- **Recovery move**: For any asker considering MA-to-Original
  trial-right exercise, surface the procedural requirements
  (12-month window from MA effective date, specific paperwork to
  CMS and to the future Medigap carrier) AND consult a SHIBA /
  SHIP volunteer on the timing AND a licensed Medicare broker
  who handles Medigap with-GI applications on the carrier-side
  process.

### 6.4 Domestic-partner coverage is not creditable for SEP

- **Statement**: Domestic-partner-coverage is NOT creditable for
  SEP purposes — IRS / SSA do not recognize the relationship for
  this rule, and an asker on a domestic-partner's employer plan
  who delays Part B incurs the late-enrollment penalty despite
  having continuous coverage. The framing's "creditable employer
  plan" reflex doesn't flag the marital-status threshold for SEP
  eligibility.
- **Source evidence**: `framings.md` §6 Excludes line on domestic-
  partner-coverage not being creditable for SEP; SHIBA / SHIP
  volunteer voice on the domestic-partner Part-B trap.
- **Trigger**: Asker is approaching 65 AND on a domestic partner's
  employer plan (not legally married) AND is considering delaying
  Part B on the assumption that employer-plan coverage triggers
  SEP eligibility post-employment.
- **Failure mode**: Asker delays Part B past 65 on assumption of
  SEP-after-loss-of-coverage; domestic-partner relationship doesn't
  qualify for SEP per SSA rule; 10%-per-12-months-late premium
  loading applies; asker also faces GEP-only enrollment window
  (Jan–Mar with coverage July, 3–9 month uncovered gap); permanent
  premium loading on Part B for life.
- **Recovery move**: For any unmarried asker approaching 65 on a
  partner's employer plan, surface the domestic-partner SEP-
  ineligibility rule explicitly AND enroll in Part B at IEP to
  avoid the penalty; if marriage is on the table, consult a SHIBA
  / SHIP volunteer on whether marriage prior to 65 would qualify
  for SEP after employment-coverage loss; consider the marital-
  status decision in conjunction with a licensed health-insurance
  broker on the family-coverage trade-off.

### 6.5 GEP coverage starts July, leaving a 3–9 month uncovered gap

- **Statement**: When the asker misses both IEP and SEP, the General
  Enrollment Period (GEP — January 1 to March 31) becomes the only
  enrollment pathway, but GEP-enrolled coverage doesn't start until
  July 1 — creating a 3–9 month uncovered gap that the framing's
  "you can enroll in GEP if you missed IEP" reflex doesn't surface.
  (Note: SSA rules effective 2023 changed GEP-enrolled coverage
  to start the month after enrollment, but historical materials
  and many community resources still reflect the old July-start
  rule — verify current rule.)
- **Source evidence**: `framings.md` §6 vocabulary on GEP and the
  uncovered-gap implication; SHIBA / SHIP volunteer voice on the
  GEP-to-coverage timing as a known surprise; date-stamp risk on
  the 2023 GEP-coverage-start rule change.
- **Trigger**: Asker has missed IEP AND has missed SEP (or no SEP
  pathway exists) AND is being told "you can enroll in GEP."
- **Failure mode**: Asker enrolls in GEP in January 2026; coverage
  starts based on whichever rule applies (historical July or
  current month-after-enrollment); asker has uncovered gap during
  which any medical event is uninsured; 12-month plan-year lock-
  in elsewhere can't bridge the gap.
- **Recovery move**: For any asker missing IEP, immediately consult
  a SHIBA / SHIP volunteer on the current GEP-coverage-start rule
  (this rule changed in 2023; date-stamp risk) AND evaluate any
  SEP pathway that may apply (Special Enrollment Period after loss
  of creditable coverage extends 8 months; check qualifying basis);
  bridge any uncovered gap with marketplace SEP if a coincident
  QLE exists, consulting an ACA-Marketplace Navigator on the
  marketplace-SEP-during-Medicare-enrollment-gap pattern.

---

## 7. QLE-and-SEP-clock-arbitrage framing

### 7.1 QLE notification delay can close the 60-day window before the asker registers it started

- **Statement**: The framing's clock-management discipline assumes
  the asker *knows* a QLE has occurred and *recognizes* the window
  starting; in practice many QLEs (loss of Medicaid eligibility via
  redetermination, employer dropping spousal coverage at mid-year
  plan-document amendment, marketplace plan discontinuation) are
  notified by mail or buried in employee communication, and the
  60-day clock runs out before the asker registers that it started.
- **Source evidence**: `framings.md` §7 Excludes line on QLE
  notification delay closing the window; ACA-Marketplace Navigator
  voice on the Medicaid-redetermination cliff (2023–24 Medicaid
  unwinding pattern).
- **Trigger**: Asker is in any of (a) Medicaid coverage facing
  redetermination, (b) employer plan with rumored mid-year plan-
  document amendment, (c) marketplace plan facing discontinuation,
  (d) any situation where coverage could end without explicit
  asker-action.
- **Failure mode**: Asker discovers coverage ended on a date 70+
  days prior; SEP window has closed; asker is uninsured until next
  OE (could be 6–9 months); any medical event in the gap is
  uninsured; the framing's "60-day SEP" was true but the clock
  had been running unnoticed.
- **Recovery move**: For asker facing any potential involuntary-
  loss-of-coverage scenario, set a calendar reminder to check
  marketplace / employer-plan / Medicaid status monthly; preserve
  all coverage-related mail unopened only briefly before
  immediate review; consult an ACA-Marketplace Navigator on the
  SEP-still-available threshold (some marketplace SEPs accept
  late documentation with cause) AND a licensed health-insurance
  broker on bridge-coverage options if the SEP has closed.

### 7.2 SEP documentation varies by exchange and rejects many qualifying events

- **Statement**: SEP-documentation requirements vary materially by
  exchange (state-based exchanges and federal Healthcare.gov
  differ); the framing's "furnish proof within the window" assumes
  a documentation pipeline that mismatches between issuer-
  notification timing and SEP-window-start timing, and many
  QLE-triggered SEPs fail at documentation despite a real qualifying
  event.
- **Source evidence**: `framings.md` §7 Excludes line on SEP-
  documentation variation; ACA-Marketplace Navigator voice on
  exchange-specific documentation failures.
- **Trigger**: Asker is enrolling via SEP AND the qualifying event
  is one of the harder-to-document categories (loss of "minimum
  essential coverage" without explicit termination notice;
  marriage with non-traditional ceremony; relocation across plan-
  service-area).
- **Failure mode**: Marketplace rejects SEP enrollment for
  insufficient documentation; asker re-submits but window closes;
  enrollment denied; asker is uninsured until next OE.
- **Recovery move**: For asker enrolling via SEP, request the
  exchange-specific SEP documentation checklist BEFORE the
  qualifying event if foreseeable (planned move, planned wedding,
  expected coverage loss); assemble documentation in advance;
  consult an ACA-Marketplace Navigator licensed in the asker's
  state on the documentation pattern AND a licensed health-
  insurance broker on alternative coverage pathways if SEP is
  denied.

### 7.3 Employer-plan QLE definitions are SPD-specific, not ACA-uniform

- **Statement**: QLE definitions are *carrier-specific* for employer
  plans — while ACA defines QLE for marketplace, employer-plan SPDs
  define their own QLE list that often excludes events the asker
  assumes are universal (e.g. partner job loss when the partner is
  on the employer plan but the asker is on their own plan; a death
  in family where the deceased was a covered dependent but the
  asker has other coverage). The framing's "QLE means you can
  change" needs SPD-verification per plan.
- **Source evidence**: `framings.md` §7 Excludes line on QLE
  definitions being carrier-specific for employer plans; HR-Reddit
  voice on the SPD-QLE-list verification pattern.
- **Trigger**: Asker is requesting a mid-year employer-plan change
  on the basis of a life event AND has not verified the event is
  on the employer plan's SPD QLE list.
- **Failure mode**: Asker submits employer-plan change request
  within the 30-day window; HR rejects on the basis that the
  event isn't on the SPD QLE list; asker is locked into the
  current plan until next OE; the framing's "QLE within 30 days"
  was true for ACA but not for the asker's specific employer SPD.
- **Recovery move**: For any employer-plan mid-year change request,
  pull the SPD's QLE list before submitting; verify the specific
  life event qualifies under the SPD; if the SPD QLE list is
  narrower than the marketplace QLE list, consider whether the
  asker can shift to marketplace coverage via the marketplace SEP;
  consult HR / benefits administrator on the SPD QLE list AND a
  licensed health-insurance broker on the marketplace alternative
  if employer plan doesn't accommodate.

### 7.4 HSA and FSA election change rules diverge sharply

- **Statement**: The HSA / FSA QLE-change rules are NOT identical:
  HSA contributions can be changed any time (no QLE needed) but
  HSA-eligibility itself depends on continuous HDHP coverage; FSA
  elections lock at OE except for QLE; the framing's "QLE unlocks
  election changes" elides this asymmetry.
- **Source evidence**: `framings.md` §7 Excludes line on HSA / FSA
  QLE-change rules diverging; HSA-administrator voice and HR-Reddit
  voice on the contribution-change-anytime vs FSA-locked-at-OE
  distinction.
- **Trigger**: Asker is making mid-year HSA or FSA changes on the
  assumption that both follow the same rules.
- **Failure mode**: Asker stops FSA contribution mid-year on the
  assumption that QLE-or-anytime applies as it does for HSA;
  payroll continues FSA deduction; asker's expectation diverges
  from actual deduction; year-end FSA forfeiture for
  un-claimed-but-deducted funds; OR asker increases FSA without
  QLE basis; HR rejects the change; asker's spending plan was
  built on an election that didn't apply.
- **Recovery move**: For mid-year HSA / FSA changes, verify the
  specific rule per account type (HSA can be changed any time;
  FSA requires QLE except for limited-purpose health-FSA-and-
  dep-care-FSA exceptions); consult HR / benefits administrator
  on the employer-specific FSA QLE list AND a CPA on the HSA
  contribution-change-mid-year impact on Form 8889 reporting.

### 7.5 COBRA 60-day election + 45-day payment grace creates a procedural arbitrage that often fails

- **Statement**: COBRA election has a 60-day window from QLE
  notification AND a 45-day premium-payment grace from election
  date — meaning an asker can defer COBRA payment 105 days from
  the QLE, retroactively electing if a medical event occurs in
  the interim. The framing rarely engages the COBRA-as-bridge-
  insurance arbitrage, AND the practical execution often fails
  (missed deadlines, payment-method confusion with the TPA,
  retro-election rejected by the carrier on procedural grounds).
- **Source evidence**: `framings.md` §7 vocabulary on the COBRA
  60-day election + 45-day premium-payment grace; patient-
  advocate / billing-error-recovery voice on the failed-COBRA-
  bridge pattern.
- **Trigger**: Asker is at job-loss QLE AND is considering
  delaying COBRA election in favor of the 105-day bridge AND has
  not verified COBRA TPA payment-method and procedural deadlines.
- **Failure mode**: Asker delays COBRA election; mid-bridge
  medical event occurs (ER visit, accident); asker tries to
  retroactively elect; COBRA TPA rejects on procedural grounds
  (election form not received in time, payment method incorrect,
  back-premium calculation disputed); asker is uninsured for the
  event; the framing's "you can always elect within 60 days" was
  procedurally true but operationally fragile.
- **Recovery move**: For any asker considering COBRA-as-bridge,
  obtain the COBRA election form and TPA payment instructions
  in writing on day 1 of the QLE; verify the back-premium
  calculation in advance; treat the 105-day deferral as risky
  rather than as a guarantee; consult a licensed health-insurance
  broker on the COBRA-vs-marketplace-bridge trade-off AND a
  patient-advocate / billing-error-recovery service if retroactive
  COBRA election is contested by the TPA after a claim event.

---

## 8. ERISA-procedural-posture framing

### 8.1 ERISA pre-emption cuts both ways — federal venue can be procedurally easier

- **Statement**: The framing's "ERISA limits damages" reads as a
  constraint only when damages would have been larger under state
  law; misses that ERISA also imposes a *federal-court venue
  requirement* that some askers find procedurally easier than
  state insurance commissioner routes (faster, more standardized,
  federally-trained adjudicators). The pre-emption cuts both ways
  and the framing's reflex "ERISA bad for consumer" isn't
  universally true.
- **Source evidence**: `framings.md` §8 Excludes line on ERISA pre-
  emption cutting both ways; ERISA-attorney voice on federal-
  court-as-procedurally-easier in some contexts.
- **Trigger**: Asker is in a self-funded ERISA plan claim dispute
  AND is being advised to pursue state-insurance-commissioner
  remedies (which are pre-empted) AND has not surfaced the
  federal-court ERISA-litigation alternative.
- **Failure mode**: Asker files state SID complaint; SID dismisses
  for ERISA pre-emption; asker has lost 60+ days of appeal
  deadline before the state route was determined inapplicable;
  ERISA 180-day appeal deadline may now be close or missed;
  procedural exhaustion path is now compressed.
- **Recovery move**: For any self-funded employer plan claim
  dispute, verify the plan's self-funded vs fully-insured status
  on day 1 of the dispute AND consult an ERISA-litigation attorney
  immediately rather than the state SID; if the plan is fully-
  insured, the state SID is the right route; the threshold
  determination is the SPD-reading question that drives
  professional-counsel selection.

### 8.2 Self-funded vs fully-insured is invisible to the enrollee without SPD reading

- **Statement**: Self-funded vs fully-insured is *invisible to the
  enrollee* — most employees never know which type they're on
  without reading the SPD carefully (look for "the plan is self-
  insured" or carrier-issued policy-number references). The
  framing's procedural distinctions are correct but the enrollee's
  ability to act on them is gated by document-reading literacy.
- **Source evidence**: `framings.md` §8 Excludes line on self-funded
  vs fully-insured being invisible without SPD reading; ERISA-
  attorney voice on the SPD-reading-as-threshold-determination.
- **Trigger**: Asker is on employer plan AND has a claim dispute or
  potential dispute AND has not pulled the SPD or determined
  self-funded vs fully-insured status.
- **Failure mode**: Asker pursues wrong procedural route (state SID
  for self-funded, or ERISA federal-court for fully-insured); time
  consumed on the wrong path; correct deadline approaches or
  passes; the procedural error compounds the substantive denial.
- **Recovery move**: For any employer-plan asker with a claim
  concern, immediately request the SPD from HR / benefits
  administrator (employers are required to provide on request
  per ERISA §104(b)(4)); identify the funding type before pursuing
  any appeal; consult an ERISA-litigation attorney on self-funded
  plans and the State Insurance Commissioner / external review on
  fully-insured plans; the SPD-reading determination is the
  threshold that drives professional-counsel selection.

### 8.3 Healthcare-sharing-ministry contracts have zero procedural appeal rights

- **Statement**: Healthcare-sharing-ministries are explicitly NOT
  insurance and NOT subject to ERISA; their dispute-resolution
  mechanism is contractual (the ministry's own bylaws and
  "shareable expense" determination), state-insurance-
  commissioner has no jurisdiction, and ERISA-attorney has no
  leverage. The framing's "denial-of-claim has appeal rights" is
  materially false in this configuration.
- **Source evidence**: `framings.md` §8 Excludes line on sharing-
  ministry zero-procedural-rights; patient-advocate voice on the
  sharing-ministry-dispute pattern; ProPublica / healthcare-
  economics-journalist voice on sharing-ministry shareable-
  expense denials.
- **Trigger**: Asker is on a healthcare-sharing-ministry "coverage"
  AND has a "non-shared" determination on a significant medical
  bill AND is being told "you can appeal."
- **Failure mode**: Asker pursues "appeal" within the ministry's
  bylaws; ministry's internal review reaffirms denial; state SID
  has no jurisdiction; ERISA attorney has no leverage; asker has
  no procedural recourse; the medical bill is owed in full
  without insurance-style adversarial-fairness protections.
- **Recovery move**: For any asker on healthcare-sharing-ministry,
  surface the zero-procedural-rights reality explicitly BEFORE
  enrollment; if already enrolled and facing a non-shared
  determination, document the determination in writing; pursue
  the ministry's internal "appeal" as the only available route
  while simultaneously consulting a patient-advocate / billing-
  error-recovery service (NAHAC, AdvoConnection) on direct-with-
  provider bill-reduction negotiation; for next OE, consult a
  licensed health-insurance broker on ACA-compliant alternatives
  with real procedural-appeal rights AND consider filing a State
  Insurance Commissioner complaint if the ministry was marketed
  in-state in violation of state insurance-disclosure rules.

### 8.4 Medicare Advantage and Part D have a distinct appeal regime, not ERISA

- **Statement**: Medicare Advantage and Medicare Part D have their
  own appeal regimes (Medicare Appeals Council, Administrative Law
  Judge tier at $1,840 amount-in-controversy minimum for 2026,
  federal-court review at $9,000+), parallel to but separate from
  ERISA. The framing's ERISA-centric procedural posture doesn't
  generalize to Medicare-side decisions even though the *vocabulary*
  of "appeal" feels transferable.
- **Source evidence**: `framings.md` §8 Excludes line on MA / Part
  D having distinct appeal regime; SHIBA / SHIP volunteer voice
  on Medicare-side appeals.
- **Trigger**: Asker is on Medicare Advantage or Part D AND has a
  denial-of-claim or coverage-determination AND is being routed
  to ERISA-style procedural framework OR is being told "no appeal
  is available" (which is wrong — Medicare has 5-tier appeal regime).
- **Failure mode**: Asker pursues wrong procedural route (ERISA
  internal appeal, state SID); Medicare appeal deadlines pass
  (5-day expedited; 60-day standard reconsideration; 180-day for
  most subsequent levels); the substantive coverage question is
  procedurally barred; the framing's vocabulary mismatch
  forecloses the real remedy.
- **Recovery move**: For any Medicare Advantage or Part D denial,
  consult a SHIBA / SHIP volunteer on the 5-tier Medicare appeals
  regime (Initial Determination → Reconsideration → ALJ →
  Medicare Appeals Council → Federal Court) AND verify the
  appeal deadlines for the specific decision type; if ALJ tier
  is reached (amount-in-controversy ≥ $1,840 for 2026), consult
  an attorney with Medicare-appeals experience (specifically — this
  is a sub-specialty distinct from ERISA-litigation practice).

### 8.5 The 180-day ERISA appeal deadline is strict and procedurally inflexible

- **Statement**: ERISA's 180-day adverse-benefit-determination
  appeal deadline (29 CFR §2560.503-1) is strict; missed deadlines
  forfeit administrative exhaustion required for federal-court
  filing; the framing's "appeal within 180 days" assumes the
  asker recognizes the adverse determination on day-1 and tracks
  the clock, but in practice the 180-day clock starts on the
  carrier's *first* adverse determination, not on the asker's
  recognition of it.
- **Source evidence**: `framings.md` §8 Excludes line implicitly
  via the strict-deadline reference; ERISA-attorney voice on the
  180-day-clock-from-first-adverse-determination as a known
  procedural trap.
- **Trigger**: Asker has received a written claim denial or
  adverse-benefit-determination letter AND has not started the
  appeal clock OR is treating the denial as informal /
  negotiable.
- **Failure mode**: 180-day clock runs from the denial letter
  date; asker negotiates informally for 150 days; appeal letter
  drafted at day 175 doesn't meet ERISA-administrative-exhaustion
  procedural requirements; clock expires; federal-court ERISA
  litigation barred for failure to exhaust; the substantive merit
  of the claim is procedurally foreclosed.
- **Recovery move**: For any written claim denial from a self-
  funded employer plan, treat the date as Day 1 of the 180-day
  clock AND immediately consult an ERISA-litigation attorney on
  the appeal-letter requirements (specific claim citations, SPD
  provision references, evidence to include); do not negotiate
  informally without preserving the administrative-exhaustion
  record; the procedural-exhaustion-requirement is the gatekeeper
  for the substantive challenge.

---

## 9. Pre-existing-condition-protection framing

### 9.1 Sharing-ministry discretionary "non-share" determinations are not pre-existing-condition exclusions

- **Statement**: Sharing-ministry "shareable expense" determinations
  are *discretionary* — even for ACA-eligible-equivalent conditions,
  the ministry can decline to share for lifestyle-attestation
  violations, late-membership-and-pre-existing-condition rules
  (typically 12-month waiting period before sharing for any pre-
  existing), or "non-Biblical" conditions (the historical
  exclusion of HIV / AIDS coverage by some ministries, more
  recently moderated). The framing's "underwriting vs no-
  underwriting" binary misses the post-membership discretion regime.
- **Source evidence**: `framings.md` §9 Excludes line on sharing-
  ministry discretion; patient-advocate / billing-error-recovery
  voice on shareable-expense-denial patterns; healthcare-economics-
  journalist voice (ProPublica investigations into sharing
  ministries).
- **Trigger**: Asker is considering or is on a healthcare-sharing-
  ministry AND has any of (a) chronic condition under management,
  (b) substance-use history, (c) lifestyle-attestation-relevant
  facts (cohabitation without marriage, tobacco, alcohol over
  ministry-specific thresholds), (d) HIV / AIDS or other condition
  with historical ministry-exclusion.
- **Failure mode**: Major medical event; ministry invokes
  discretionary non-share for an attestation violation or pre-
  existing condition rule; asker is responsible for $100k+ in
  full; the framing's "ACA underwriting protection" was correct
  for ACA but didn't apply to the sharing-ministry alternative
  the asker chose on price.
- **Recovery move**: For any asker considering or on sharing-
  ministry, surface the discretionary non-share regime explicitly
  AND consult a licensed health-insurance broker on ACA-compliant
  alternatives (including catastrophic plans for under-30 or
  hardship-exemption askers); if on sharing-ministry and facing
  non-share determination, consult a patient-advocate / billing-
  error-recovery service on direct-with-provider bill-reduction
  negotiation AND file a State Insurance Commissioner complaint
  if the ministry was marketed in-state in violation of state
  insurance-disclosure rules.

### 9.2 Undiagnosed-condition risk hits hardest on STLDI / sharing-ministry

- **Statement**: The framing assumes the asker can identify their
  pre-existing conditions; in practice some askers don't *know*
  they have a condition (undiagnosed early-stage diabetes,
  early-stage cancer, mental-health condition that hasn't been
  medically named) until the claim event reveals it, and the
  STLDI / sharing-ministry retrospective-exclusion risk hits
  hardest for these askers. The "you'll know if you have a
  condition" reflex underweights diagnostic-timing uncertainty.
- **Source evidence**: `framings.md` §9 Excludes line on
  undiagnosed-condition risk hitting hardest on STLDI / sharing-
  ministry; healthcare-economics-journalist voice on
  retrospective-exclusion cases.
- **Trigger**: Asker is considering STLDI or sharing-ministry on
  price grounds AND is reasoning from "I have no diagnoses" AND
  has not surfaced the undiagnosed-condition risk.
- **Failure mode**: ER visit reveals previously undiagnosed
  early-stage cancer or autoimmune; STLDI carrier rescinds
  retroactively for "material misrepresentation" of pre-existing
  condition the asker didn't know about; full claim period
  uninsured; medical bankruptcy adjacency.
- **Recovery move**: For any asker considering STLDI / sharing-
  ministry on the basis of "I have no diagnoses," surface the
  undiagnosed-condition rescission risk explicitly; if STLDI /
  sharing-ministry remains the only affordable option, document
  every symptom-history detail on the application with
  overwhelming completeness; consult a licensed health-insurance
  broker on ACA-compliant alternatives AND file a State Insurance
  Commissioner complaint immediately upon any post-claim
  rescission attempt.

### 9.3 Medigap underwriting outside GI denies common chronic conditions

- **Statement**: Medigap underwriting outside GI is structurally
  similar to pre-ACA commercial underwriting — common conditions
  (controlled diabetes, prior breast cancer, asthma) trigger
  rate-ups or denials. The framing's "ACA protects pre-existing
  conditions" doesn't extend to Medigap because Medigap sits
  outside the ACA's guaranteed-issue architecture (except in the
  named state GI regimes — NY / CT / MA / ME year-round; CA / OR
  birthday rule).
- **Source evidence**: `framings.md` §9 Excludes line on Medigap
  underwriting outside GI; SHIBA / SHIP volunteer voice on the
  state-specific Medigap-GI variation.
- **Trigger**: Asker is past the 6-month Medigap-GI window AND
  has any chronic condition (controlled diabetes, prior cancer,
  asthma, COPD, autoimmune) AND is considering switching from MA
  back to Original Medicare + Medigap.
- **Failure mode**: Medigap carriers underwrite and deny on the
  chronic condition; asker is locked into MA without the trial-
  right window AND without medical underwriting; the framing's
  "ACA pre-existing-condition protection" reflex was true for
  commercial but false for Medigap.
- **Recovery move**: For any asker past 6-month Medigap-GI window
  considering MA-to-Original-Medicare switch, verify state-
  specific Medigap-GI rules (NY / CT / MA / ME / CA / OR have
  varying year-round or birthday-rule GI windows; most states are
  IEP-only); if GI is unavailable, evaluate whether MA-trial-right
  (12 months from MA effective date at IEP) applies; consult a
  SHIBA / SHIP volunteer on the state-specific GI determination
  AND a licensed Medicare broker on Medigap underwriting carrier-
  by-carrier (some carriers are more lenient than others).

### 9.4 Cost trade-off for healthy high-income askers is not negligible

- **Statement**: The framing's "ACA-compliant is the only safe
  option for pre-existing conditions" is true at the substantive
  level, but the framing doesn't engage with the *cost* trade-off
  rigorously — for an asker at >250% FPL with a stable but non-
  severe chronic condition (well-managed hypertension on cheap
  generics), a sharing-ministry's headline 60–70% premium
  discount is real, and the framing's reflex "you must have ACA"
  can come across as paternalistic when the asker's specific risk
  profile and budget reality are aligned with the alternative. The
  risk is genuine but framing-dependent.
- **Source evidence**: `framings.md` §9 Excludes line on the cost
  trade-off for healthy high-income askers; conservative-policy /
  Galen / AEI voice on the price-protected-by-substantive-rights
  trade-off.
- **Trigger**: Asker is at >250% FPL with stable well-managed
  chronic condition (hypertension on generics, controlled diabetes
  with simple metformin, mild asthma) AND is being told "you must
  have ACA" without the cost-side trade-off surfaced.
- **Failure mode**: Asker accepts ACA recommendation without
  cost-side analysis; pays $800–1,200/month premium that the
  household can't sustain; lapses coverage entirely; uninsured
  with worse outcome than the sharing-ministry alternative would
  have provided.
- **Recovery move**: For asker at >250% FPL with stable chronic
  condition, surface BOTH the ACA-substantive-protection AND the
  sharing-ministry-discretion risk; model the catastrophic-event
  scenario on each option; allow the asker to make the trade-off
  with eyes open; consult a licensed health-insurance broker on
  the cost-vs-protection trade-off AND a patient-advocate service
  on what happens if the chronic condition flares while on the
  alternative coverage.

### 9.5 Conditional approvals and exclusion riders persist in non-ACA markets

- **Statement**: STLDI carriers and some non-ACA group plans
  (farm-bureau exempt plans, association health plans in some
  states) underwrite with exclusion riders ("this plan will not
  cover claims related to [condition X]") rather than outright
  denial; the framing's "underwriting either denies or accepts"
  binary misses the conditional-approval-with-exclusion regime
  the asker may misread as full coverage.
- **Source evidence**: `framings.md` §9 vocabulary on exclusion
  riders; patient-advocate voice on exclusion-rider-misread
  pattern.
- **Trigger**: Asker is offered an STLDI or association-health-
  plan policy AND the offer letter includes any "rider,"
  "exclusion," or "limitation" language AND the asker is reading
  the offer as standard coverage.
- **Failure mode**: Asker accepts the rider'd plan thinking it's
  comprehensive; the excluded condition (back pain, mental health,
  reproductive care, prior cancer recurrence) is the claim event;
  full claim cost uninsured; the framing's "got approved" was
  true but conditional.
- **Recovery move**: For any non-ACA plan offer, read every page
  of the policy for "rider," "exclusion," "limitation,"
  "specifically excluded," or condition-name language; for any
  excluded condition, treat the plan as uninsured for that
  condition class; consult a licensed health-insurance broker on
  ACA-compliant alternatives AND a patient-advocate / billing-
  error-recovery service if a rider is invoked on a claim the
  asker believed was covered; file a State Insurance Commissioner
  complaint if the rider was inadequately disclosed under state
  insurance-disclosure rules.

---

## 10. Network-and-prior-authorization framing

### 10.1 Ghost networks and outdated provider directories distort the comparison

- **Statement**: Provider directories are systematically inaccurate
  — CMS audits of MA plans find 30–50% of listed mental-health
  providers either not accepting new patients or no longer in
  network at the time of the audit; the framing's "verify the
  directory" instruction is correct but understates the operational
  reality of finding actual in-network care. Calls to provider
  offices are the only reliable check, and the framing rarely
  acknowledges this workload.
- **Source evidence**: `framings.md` §10 Excludes line on
  systematically inaccurate provider directories; chronic-illness
  patient voice on the directory-vs-actual-acceptance gap;
  healthcare-economics-journalist voice (KFF / Health Affairs on
  the ghost-network research literature).
- **Trigger**: Asker is choosing a plan partly on provider-
  directory listings AND has not verified directly with provider
  offices that the listed providers are accepting new patients
  AND are in the plan's specific network tier.
- **Failure mode**: Asker enrolls based on directory listings;
  attempts to schedule with listed in-network providers; 30–50%
  of listings either not accepting new patients or out of network
  at the new plan year; asker faces out-of-network costs or care
  delays; 12-month plan-year lock-in forecloses switch to a plan
  with actual access.
- **Recovery move**: For asker depending on specific providers
  (mental-health prescriber, specialist, oncologist, PCP),
  CALL each provider office before OE deadline to verify
  in-network status AND new-patient acceptance for the candidate
  plan year; do not trust the directory; if access is thin,
  consult a licensed health-insurance broker on cross-plan
  network comparison AND consider filing a State Insurance
  Commissioner complaint on the discovered directory inaccuracy
  (state SIDs have begun enforcing directory-accuracy rules
  under No Surprises Act §116).

### 10.2 MA network drops mid-year are a structural risk

- **Statement**: Network drops mid-year are a Medicare-Advantage-
  specific phenomenon (MA contracts year-to-year with provider
  systems, and contract disputes between hospital systems and MA
  carriers in 2023–25 have produced material mid-year network
  changes for many beneficiaries). The framing's "I picked a
  plan with my doctor in network at enrollment" is a stable-
  state assumption that the actual market doesn't deliver.
- **Source evidence**: `framings.md` §10 Excludes line on MA
  network drops mid-year being structural; healthcare-economics-
  journalist voice on 2023–25 MA-vs-hospital-system contract
  disputes; SHIBA / SHIP volunteer voice on the mid-year-
  disenrollment pattern.
- **Trigger**: Asker is on Medicare Advantage AND has specific
  in-network provider dependencies (PCP, oncologist, cancer-
  center) AND is reasoning from current enrollment-time network
  status.
- **Failure mode**: Mid-year network change drops asker's
  oncologist or cancer-center; asker either pays out-of-network
  (no out-of-network cap on most MA HMOs) or disrupts care
  continuity; mid-year MA-disenrollment requires specific
  conditions (SEP for network-loss in some cases; AEP otherwise);
  the framing's enrollment-time information was outdated within
  6 months.
- **Recovery move**: For asker on MA dependent on specific
  providers, verify renewal-year network status during each AEP
  (Oct 15 – Dec 7) AND set quarterly reminders to recheck
  during the plan year; if mid-year network drop occurs, consult
  a SHIBA / SHIP volunteer on the SEP-for-network-loss criteria
  AND a licensed Medicare broker on alternative MA plans with
  the lost provider in-network; consider switching to Original
  Medicare + Medigap if Medigap-underwriting passes (otherwise
  GI / trial-right path applies).

### 10.3 Prior-authorization density varies enormously by plan and specialty

- **Statement**: Prior-authorization burden is unevenly distributed
  across plans and specialties — high-cost specialty drugs and
  imaging are universally prior-auth-required, but psychotherapy
  frequency caps, durable-medical-equipment approvals, and ABA-
  therapy hour limits vary materially. The framing's "Original
  Medicare has no prior-auth" is broadly true (Part B has very
  limited PA, mostly for durable medical equipment under the Round
  1 / 2 PA Demonstration); MA varies plan-by-plan and year-by-year.
- **Source evidence**: `framings.md` §10 Excludes line on prior-
  auth-burden variation by plan and specialty; chronic-illness
  patient voice on prior-auth attrition.
- **Trigger**: Asker has known need for specialty drugs, imaging,
  psychotherapy, DME, or ABA therapy AND is choosing between
  plans without comparing prior-auth lists and frequency limits.
- **Failure mode**: Asker enrolls in plan with heavy prior-auth on
  the asker's specific care needs; each visit / refill / scan
  requires PA submission; PA denials common; care delays
  systematic; the framing's "the plan covers it" was true
  formally but operationally compromised by PA burden.
- **Recovery move**: For asker with specific specialty-care needs,
  request the plan's prior-auth list and frequency-limit table
  (carriers are required to publish these under recent CMS
  transparency rules); compare against the asker's specific
  care pattern; consult a licensed health-insurance broker on
  prior-auth-burden differentials between plans AND consider
  Original Medicare + Medigap for asker with heavy specialty-
  care needs (substantially lower PA burden) if Medigap-eligibility
  applies.

### 10.4 Specialty-pharmacy partner is a separate access question

- **Statement**: Specialty-pharmacy and biologic-drug coverage uses
  a parallel "buy-and-bill" vs "specialty-pharmacy" path the
  framing's medical-provider-list vocabulary doesn't engage; a
  marketplace plan whose specialty-pharmacy partner doesn't carry
  the asker's biologic produces an OOP-cost surprise even when
  the medical provider is in-network.
- **Source evidence**: `framings.md` §10 Excludes line on
  specialty-pharmacy parallel track; chronic-illness patient voice
  on biologic-coverage gaps.
- **Trigger**: Asker takes a specialty drug or biologic ($1k+/month
  list price) AND is choosing a plan on the basis of medical
  provider-network only AND has not separately verified the
  specialty-pharmacy partner.
- **Failure mode**: Plan's specialty-pharmacy partner doesn't carry
  the asker's specific biologic; asker forced to switch drug
  (if therapeutically possible) OR pay out-of-network specialty-
  pharmacy at non-discount rate; OOP exposure thousands per
  month beyond the framing's medical-cost projection.
- **Recovery move**: For asker on specialty drug or biologic,
  separately verify the plan's specialty-pharmacy partner
  carries the specific drug at the specific dose; do this
  before OE deadline; consult a licensed health-insurance broker
  on plan-level specialty-pharmacy network differences AND a
  patient-advocate / billing-error-recovery service on
  manufacturer copay-card and patient-assistance options if
  the specialty-pharmacy fit is poor.

### 10.5 Tiered networks and "preferred" providers create cost-share asymmetries the framing rarely names

- **Statement**: Tiered network structures (Tier 1 "preferred,"
  Tier 2 "in-network," Tier 3 "out-of-network") create cost-
  share asymmetries the framing's binary in-vs-out vocabulary
  doesn't capture; many plans incentivize Tier 1 with lower
  copay / coinsurance, but Tier 2 coverage looks "in-network" on
  the directory while costing 1.5–2× more in OOP.
- **Source evidence**: `framings.md` §10 vocabulary on "tiered
  network"; HR-Reddit voice on the tiered-network surprise
  pattern.
- **Trigger**: Asker is enrolled in or considering a tiered-
  network plan AND is reasoning from "my provider is in-network"
  without checking the specific tier.
- **Failure mode**: Asker's provider is Tier 2 ("in-network" but
  not "preferred"); cost-share is 30% coinsurance instead of
  Tier 1's $40 copay; annual OOP exceeds projection by 1.5–2×
  on the same utilization pattern; the framing's binary in-vs-
  out reflex missed the tier distinction.
- **Recovery move**: For any tiered-network plan, verify provider
  tier-classification explicitly (call provider office AND
  check the plan's tier-specific directory); model OOP under
  the actual tier; if Tier 1 access is thin for asker's specific
  providers, treat the plan as effectively narrower than the
  headline network breadth suggests; consult a licensed health-
  insurance broker on tiered-network plan-vs-flat-network plan
  trade-offs.

---

## 11. Embedded-vs-aggregate-cost-sharing framing

### 11.1 OE portals display family deductible as a single number, hiding the embedded sub-limit

- **Statement**: Older plan-comparison spreadsheets (and many HR
  open-enrollment portals) still display family deductible as a
  single number, hiding the embedded individual sub-limit that
  ACA mandated since 2016. The framing's "look for embedded sub-
  limit" instruction is correct but the asker is up against
  display-layer-incompleteness.
- **Source evidence**: `framings.md` §11 Excludes line on display-
  layer-incompleteness in OE portals; HR-Reddit voice on the
  family-deductible-display problem.
- **Trigger**: Asker is comparing family-tier plans via HR portal
  display OR is reading plan summaries that show only "family
  deductible: $X" without separate individual sub-limit.
- **Failure mode**: Asker picks plan thinking family deductible
  is the binding constraint; doesn't realize embedded individual
  OOP-max sub-limit caps any single member's exposure at
  self-only OOP-max ($9,450 for 2026); on plans where the family
  OOP-max is much higher than the individual sub-limit, the
  individual-exposure protection is invisible to the asker.
- **Recovery move**: For family-tier plan choice, pull the SPD
  (not just the HR portal summary) and verify both the family
  deductible AND the embedded individual OOP-max sub-limit;
  for plans without explicit embedded sub-limit language,
  request the carrier's policy document; consult a licensed
  health-insurance broker if the SPD is ambiguous on embedded
  sub-limit structure AND HR / benefits administrator on the
  plan-document language for embedded vs aggregate clarification.

### 11.2 Prescription OOP and medical OOP tracking can diverge on individual sub-limits

- **Statement**: Prescription-drug OOP tracking is *often* separate
  from medical OOP, with its own deductible and OOP-max — and on
  some plans, prescription OOP-met counts toward family but not
  toward individual embedded sub-limits, or vice versa. The
  framing's "embedded OOP caps individual exposure" needs the
  prescription-track verification that most enrollees don't do.
- **Source evidence**: `framings.md` §11 Excludes line on
  prescription / medical OOP-tracking divergence; HSA-administrator
  voice on dual-track OOP accumulation.
- **Trigger**: Asker is on family-tier plan AND has a member with
  high specialty-drug spend AND is reasoning from "embedded OOP
  caps the individual" without verifying prescription-track
  accumulation rules.
- **Failure mode**: Specialty-drug spend on one member hits the
  prescription-track OOP-max but not the medical-track individual
  embedded sub-limit; member's continued medical care doesn't
  enjoy individual-sub-limit cap; family OOP exceeds projection
  by the prescription-vs-medical OOP-tracking gap.
- **Recovery move**: For family-tier plan with specialty-drug
  member, verify the SPD's OOP-accumulation rules for prescription
  vs medical AND for individual-embedded-sub-limit vs family-
  aggregate; if the SPD is ambiguous, request the carrier's
  policy document; consult a licensed health-insurance broker on
  the specific accumulation-rule pattern AND a CPA on the HSA-
  contribution-sizing implication if the plan is HDHP-with-HSA.

### 11.3 HRAs and ICHRAs layer over the plan's deductible in non-obvious ways

- **Statement**: HRAs (Health Reimbursement Arrangements) and
  ICHRAs (Individual Coverage HRA) layer employer-funded chunks
  on top of the plan's deductible; the framing's structural
  analysis applies cleanly to plan-as-document but obscures
  when an HRA pays the first $2,000 of deductible — the
  *effective* cost-sharing structure the enrollee experiences
  is the layered product, not the plan-document standalone.
- **Source evidence**: `framings.md` §11 Excludes line on HRA /
  ICHRA layering; HR-Reddit voice on the HRA-as-deductible-
  buyer pattern.
- **Trigger**: Asker is on a plan with HRA / ICHRA layer AND is
  reasoning from the headline plan-document deductible without
  the HRA offset.
- **Failure mode**: Asker over-projects OOP exposure under the
  plan-document deductible (HRA buys down first $2k);
  alternatively under-projects when the HRA is itself capped
  and runs out mid-year; the framing's plan-document analysis
  was correct but incomplete on the layered product.
- **Recovery move**: For asker with HRA / ICHRA, model the
  layered cost-sharing explicitly (HRA covers first $X of
  deductible, then plan-document cost-sharing applies); verify
  HRA-rollover rules (carries over to next year?), HRA-on-
  termination rules (forfeit?), and ICHRA-vs-marketplace-APTC
  coordination (ICHRA disqualifies APTC); consult HR / benefits
  administrator on the HRA structure AND a licensed health-
  insurance broker on the layered cost-sharing AND a CPA if
  ICHRA-vs-APTC trade-offs apply.

### 11.4 Mid-year additions and removals interact with embedded sub-limits plan-specifically

- **Statement**: Mid-year additions and removals (newborn QLE,
  divorce QLE, dependent age-out at 26) interact with the
  embedded individual sub-limit in plan-specific ways — some
  plans pro-rate the embedded sub-limit by months-of-coverage,
  some don't, and the framing's "embedded caps at $9,450" is
  calendar-year-static in a way mid-year additions don't track.
  Boundary `family-planning`.
- **Source evidence**: `framings.md` §11 Excludes line on mid-
  year additions / removals interacting with embedded sub-limits
  plan-specifically; HR-Reddit voice on the QLE-and-embedded-
  cap trap.
- **Trigger**: Asker has a mid-year QLE addition (newborn,
  marriage, adoption) OR removal (divorce, death, age-out) AND
  has not verified the SPD's pro-rate-or-not rule for embedded
  individual OOP-max sub-limit.
- **Failure mode**: New family member's care in Q4 hits a
  pro-rated embedded sub-limit (e.g. $2,400 instead of $9,450)
  on a plan that pro-rates by months-of-coverage; the framing's
  "embedded caps at $9,450" was true for full-year members but
  false for mid-year additions; OOP exposure exceeds projection.
- **Recovery move**: For any mid-year family change, verify
  the SPD's pro-rate rule for embedded individual sub-limit
  AND for family aggregate OOP-max; if pro-rated, model the
  reduced cap; consult HR / benefits administrator on the SPD
  language AND a licensed health-insurance broker if the
  mid-year change makes a different plan structure preferable
  for the partial-year membership.

### 11.5 Tiered family deductible structures (2× self-only) are not the same as embedded

- **Statement**: Some plans use a "tiered family deductible"
  where the family deductible is exactly 2× self-only (not the
  aggregate-deductible 3× pattern); the framing's "embedded vs
  aggregate" binary doesn't engage the 2× tiered structure,
  which can have its own cost-sharing-after-deductible quirks
  the framing's binary vocabulary misses.
- **Source evidence**: `framings.md` §11 vocabulary on "tiered
  family deductible (2x self-only structure)"; HR-Reddit voice
  on the tiered-family-deductible distinction.
- **Trigger**: Asker is comparing family-tier plans AND one or
  more plans displays family deductible as exactly 2× self-only
  (rather than 2.5–3× which is the aggregate-deductible norm).
- **Failure mode**: Asker reads the 2× tiered structure as
  embedded (favorable) or aggregate (unfavorable) when neither
  binary applies; SPD-specific cost-sharing-after-deductible
  rules don't match the asker's mental model; total OOP
  diverges from projection.
- **Recovery move**: For any plan with 2× tiered family-
  deductible structure, pull the SPD and read the full cost-
  sharing-after-deductible language including individual-vs-
  family interactions; do not assume embedded-or-aggregate
  binary applies; consult a licensed health-insurance broker on
  the SPD-specific structure AND HR / benefits administrator on
  carrier-provided plan-comparison summaries that explicitly
  call out the 2× tiered behavior.

---

## 12. Tax-and-arbitrage framing

### 12.1 IRMAA is calculated on 2-year-lookback MAGI

- **Statement**: IRMAA (Income-Related Monthly Adjustment Amount
  on Medicare Part B and Part D) is calculated on a 2-year
  lookback MAGI — the asker who realizes a large capital gain
  or Roth conversion in 2026 may face IRMAA brackets on 2028
  Medicare premiums; the framing's tax-year focus misses the
  2-year-forward Medicare-premium implication. Boundary
  `personal-finance`.
- **Source evidence**: `framings.md` §12 Excludes line on IRMAA
  2-year-lookback; SHIBA / SHIP volunteer voice on the IRMAA-
  surprise pattern; Bogleheads voice on Roth-conversion-and-
  IRMAA coordination.
- **Trigger**: Asker is 63+ years old AND is planning a large
  income event (Roth conversion, RSU vest, capital-gain
  realization, business sale) AND has not modeled the 2028
  IRMAA implication.
- **Failure mode**: 2026 income spike pushes MAGI to $200k+;
  2028 IRMAA Part B premium is $400/month additional on top of
  base; 2028 Part D premium adds $80/month additional; total
  $5,760 additional annual Medicare premium for one year of
  income shock that wasn't projected.
- **Recovery move**: For asker 63+ planning income events,
  model the 2-year-forward IRMAA implication; if income shock
  is avoidable (defer Roth conversion, spread RSU sale across
  tax years), consider deferral; consult a CPA on the IRMAA
  bracket structure for the planned MAGI AND a SHIBA / SHIP
  volunteer on the IRMAA-appeal pathway (life-changing-event
  appeal can sometimes reduce IRMAA if the income event was
  one-time).

### 12.2 Payroll-deduction HSA saves FICA; after-tax-1040 deduction does not

- **Statement**: HSA-on-payroll-deduction saves FICA (7.65%) in
  addition to income tax; HSA-on-after-tax-1040-deduction
  saves only income tax (FICA already paid). The framing's "HSA
  is above-the-line deductible" understates the payroll-
  contribution advantage for askers who think they can "catch
  up at tax time" — they lose the FICA save.
- **Source evidence**: `framings.md` §12 Excludes line on
  payroll-vs-after-tax HSA FICA differential; HSA-administrator
  voice on the FICA-save mechanic.
- **Trigger**: Asker is contributing to HSA after-tax (via 1040
  deduction) instead of through payroll deduction AND has
  available payroll-deduction capacity at the employer.
- **Failure mode**: Asker contributes $4,300 to HSA after-tax;
  saves income tax ($1,032 at 24% bracket) but pays FICA
  ($329 at 7.65%) that payroll-deduction would have avoided;
  loses $329 per year on the contribution-routing decision.
- **Recovery move**: For asker with payroll-deduction option,
  always prefer payroll-deduction over after-tax 1040-deduction
  for HSA contributions; consult HR / benefits administrator on
  payroll-deduction enrollment AND a CPA on Form 8889 timing if
  the asker has already made after-tax contributions for the
  year (allowed but suboptimal).

### 12.3 Dep-care-FSA vs Child-Care-Tax-Credit coordination requires accurate marginal-rate projection

- **Statement**: The dependent-care-FSA-vs-Child-Care-Tax-Credit
  coordination requires the asker to project marginal rate
  accurately; askers with lumpy income (equity vesting, self-
  employed) get this wrong in ways that produce higher effective
  tax than necessary. The framing's "coordinate the election"
  assumes a stable income picture the asker may not have.
- **Source evidence**: `framings.md` §12 Excludes line on dep-
  care-FSA-vs-Child-Care-Tax-Credit coordination requiring
  accurate marginal-rate projection; CPA voice on Form 2441
  coordination patterns.
- **Trigger**: Asker has dependent-care expenses (child under
  13, disabled spouse, disabled dependent) AND has lumpy income
  (equity vesting, self-employed, commission) AND is choosing
  between dep-care-FSA and Child-Care-Tax-Credit on Form 2441.
- **Failure mode**: Asker locks in dep-care-FSA at OE on
  projected marginal rate of 32%; actual marginal rate at tax
  time is 22% (income lower than projected); Child-Care-Tax-
  Credit would have been the better choice; FSA forfeiture risk
  on unspent funds; the framing's "coordinate the election"
  assumed stable income.
- **Recovery move**: For variable-income askers with dependent-
  care expenses, model the dep-care-FSA-vs-tax-credit decision
  under at least 3 marginal-rate scenarios; consider conservative
  FSA election to limit forfeiture risk; consult a CPA on the
  Form 2441 coordination AND HR / benefits administrator on
  mid-year FSA election changes (limited but possible for QLE).

### 12.4 Last-month-rule testing-period recapture catches asker who drops HDHP mid-following-year

- **Statement**: HSA last-month-rule (LMR) allows an asker who is
  HSA-eligible on December 1 to contribute the full annual
  amount even if they were only eligible part of the year, but
  requires the asker to remain HSA-eligible through the entire
  following calendar year (the "testing period"). Loss of
  HSA-eligibility during the testing period triggers income
  recapture on the LMR contribution PLUS 10% penalty; the
  framing's "max under LMR" reflex doesn't surface the testing-
  period recapture exposure.
- **Source evidence**: `framings.md` §12 Excludes line implicit via
  the "income recapture + 10% penalty" vocabulary; HSA-
  administrator voice on the LMR testing-period as a known trap.
- **Trigger**: Asker became HSA-eligible mid-year (started new
  HDHP-with-HSA mid-year) AND contributed full annual amount
  under LMR AND is now considering a plan change for next year
  that would drop HDHP coverage OR is approaching 65 with
  Medicare enrollment risk.
- **Failure mode**: Asker drops HDHP in March of testing-period
  year (job change to non-HDHP plan, marriage to spouse with
  PPO, Medicare enrollment); LMR recapture applies: the prior-
  year LMR-attributed contribution amount becomes ordinary
  income PLUS 10% penalty; tax-time surprise.
- **Recovery move**: For asker considering LMR contribution,
  surface the testing-period recapture rule explicitly before
  contributing the LMR-elevated amount; if HDHP-continuity
  through the full following year is uncertain, prefer the
  pro-rated contribution instead of LMR; consult a CPA on the
  Form 8889 LMR-vs-pro-rata calculation AND a licensed health-
  insurance broker on the HDHP-continuity assumption.

### 12.5 APTC reconciliation cap is irrelevant above 400% FPL

- **Statement**: APTC reconciliation on Form 8962 has *capped*
  repayment for under-projected MAGI below 400% FPL (the cap was
  intended as a hardship protection); above 400% FPL the
  repayment is uncapped and can be six-figure when ARPA-
  enhanced subsidies are in effect (the asker who under-projected
  income and received $25k/year of APTC on a benchmark-silver
  may owe the full $25k back). The framing's "true-up at tax
  time" doesn't surface the severity of the asymmetry above the
  cap.
- **Source evidence**: `framings.md` §12 Excludes line on APTC
  reconciliation cap asymmetry above 400% FPL; ACA-Marketplace
  Navigator voice on the under-projection trap; CPA voice on
  Form 8962 reconciliation projection.
- **Trigger**: Asker projects MAGI under 400% FPL AND has any
  income-event risk that could push MAGI over (equity vesting,
  Roth conversion, year-end bonus, RSU vest, capital-gain
  realization) AND is receiving APTC at the under-400% subsidy
  level.
- **Failure mode**: MAGI lands at 405% FPL; full ARPA-enhanced
  APTC ($25k for family on benchmark-silver) owed back at tax
  time; cash-flow shock at filing; the framing's "cap protects
  me" was true below 400% FPL but false above.
- **Recovery move**: For asker near the 400% FPL threshold,
  monitor MAGI through Q3 and update marketplace income estimate
  before Q4; if MAGI is likely to cross the threshold, consider
  reducing the advance subsidy claim mid-year via marketplace
  account income-update; consult a CPA on the Form 8962
  reconciliation projection AND an ACA-Marketplace Navigator on
  the income-update mechanics.

---

## 13. Bureaucratic-procedural framing

### 13.1 Procedural diligence is unsustainable during a medical crisis

- **Statement**: The framing's procedural diligence is *time-
  intensive* in ways that compound during a medical crisis — the
  same asker who could read EOBs in good health is now sleep-
  deprived, post-anesthesia, or coping with chronic-illness
  cognitive fog, and the framing's "track every claim" workload
  becomes impossible exactly when the financial exposure peaks.
  Patient-advocate services exist for a reason; the framing
  rarely surfaces the cost-benefit of paid advocacy.
- **Source evidence**: `framings.md` §13 Excludes line on procedural
  diligence being unsustainable during medical crisis; patient-
  advocate voice (NAHAC, AdvoConnection) on the paid-advocate
  cost-benefit.
- **Trigger**: Asker is currently in a medical crisis (active
  cancer treatment, post-surgical recovery, chronic-illness
  flare) AND is being told to "track every claim and EOB" AND
  has not surfaced the paid-advocate cost-benefit.
- **Failure mode**: Asker mid-crisis fails to track claims;
  carrier-paid amounts include coding errors; provider bills
  include duplicated charges; asker pays inflated amounts; the
  framing's procedural-discipline assumption was reasonable in
  baseline health and impossible during crisis.
- **Recovery move**: For asker in active medical crisis, surface
  the paid patient-advocate option explicitly (typical cost
  $50–200/month or hourly contingency-style on recovered
  amounts); consult a patient-advocate / billing-error-recovery
  service (NAHAC, AdvoConnection) on engagement structure AND
  family-member surrogate for claims tracking if professional
  advocacy is not affordable; for self-funded ERISA plan claim
  disputes, also consult an ERISA-litigation attorney on
  appeal-clock-preservation while the medical crisis is active.

### 13.2 Response asymmetry: TPAs respond on their clock, asker waits in network limbo

- **Statement**: "Dispute the denial in writing with citations"
  is correct procedure, but the framing under-estimates the
  *response asymmetry* — TPAs and carriers respond on their own
  clock (often beyond statutory deadlines without consequence
  under ERISA), and the asker waiting in network limbo cannot
  get care without paying out-of-pocket and seeking reimbursement,
  which most cannot front. The procedure works for the asker who
  has cash flow and patience the system doesn't compensate.
- **Source evidence**: `framings.md` §13 Excludes line on response
  asymmetry; patient-advocate voice on the cash-flow-front-for-
  reimbursement pattern.
- **Trigger**: Asker is in a claim dispute AND needs ongoing care
  AND lacks cash to front out-of-pocket pending reimbursement.
- **Failure mode**: Asker delays care while dispute pending;
  condition worsens; emergency-room visit (not deferrable);
  total cost exceeds the original dispute by orders of magnitude;
  the framing's "procedure works" was true in steady-state but
  false under cash-constraint.
- **Recovery move**: For asker in claim dispute needing ongoing
  care, document the dispute in writing AND continue care at
  in-network providers paying minimum required amounts;
  consult a patient-advocate / billing-error-recovery service
  on hardship-applications and payment-plan options with the
  provider AND an ERISA-litigation attorney on the appeal-clock-
  preservation if the dispute is on a self-funded employer plan;
  consider escalating to the State Insurance Commissioner if
  the plan is fully-insured AND the carrier exceeds statutory
  response deadlines.

### 13.3 No Surprises Act IDR is operationally lurching

- **Statement**: The No Surprises Act §2799A IDR (Independent
  Dispute Resolution) process is heavily contested — the IDR
  determinations have been litigated under multiple *Texas
  Medical Association v. HHS* rulings, the methodology favoring
  the median-in-network-rate vs qualifying-payment-amount has
  shifted multiple times, and the framing's "use the IDR"
  assumes a process that is operationally lurching. Boundary
  `legal-disputes`.
- **Source evidence**: `framings.md` §13 Excludes line on No
  Surprises Act IDR being operationally lurching; patient-
  advocate voice on IDR-arbitration patterns.
- **Trigger**: Asker has a balance-billing dispute under No
  Surprises Act AND is considering IDR arbitration AND has not
  surfaced the operational-lurch in IDR methodology.
- **Failure mode**: Asker pursues IDR; methodology shifts mid-
  arbitration; IDR award doesn't match the asker's expectation
  based on the prior methodology; appeal of IDR award is limited;
  the framing's "use the IDR" produced a worse outcome than
  direct-negotiation might have.
- **Recovery move**: For balance-billing dispute under NSA,
  consult a patient-advocate / billing-error-recovery service
  on direct-with-provider negotiation FIRST before IDR (often
  faster and predictable than IDR); if IDR is necessary, consult
  a legal-disputes-experienced attorney on the current IDR
  methodology AND the State Insurance Commissioner if fully-
  insured plan and direct negotiation has stalled.

### 13.4 Bureaucratic complexity is a structural access barrier for many askers

- **Statement**: The framing prices procedural literacy as a
  learnable skill; for English-second-language askers, askers
  with low-literacy backgrounds, or askers with cognitive /
  developmental disabilities, the bureaucratic complexity is
  itself a structural barrier to access — and the framing rarely
  connects to community-health-worker / patient-navigator /
  SHIP / Medicaid-redetermination-assistance resources that
  exist to bridge this gap.
- **Source evidence**: `framings.md` §13 Excludes line on
  bureaucratic complexity being a structural access barrier;
  patient-advocate voice and community-health-worker voice on
  the navigation-assistance gap.
- **Trigger**: Asker has limited English proficiency, low-
  literacy background, cognitive / developmental disability, OR
  is the family-member-surrogate for such an asker AND is being
  routed through standard EOB-reading / appeal-drafting / FSA-
  substantiation procedural advice.
- **Failure mode**: Asker can't complete the procedural steps;
  claims unprocessed; appeals unfilled; care access blocked;
  the framing's "track and dispute" assumed literacy and
  language access the asker doesn't have.
- **Recovery move**: For askers with access barriers, route to
  community-health-worker programs (federally qualified health
  centers often have CHWs), patient-navigator programs
  (cancer-care navigators, chronic-disease navigators in many
  hospital systems), in-person ACA-Marketplace Navigators
  (CMS-trained, often multilingual), and SHIBA / SHIP
  volunteers (state-program with multilingual capacity in many
  regions) for hands-on procedural support; consult a patient-
  advocate / billing-error-recovery service if a specific
  claim is in dispute.

### 13.5 FSA substantiation requires itemized receipts, not credit-card statements

- **Statement**: FSA claims require itemized receipts (not
  credit-card statements) plus Letter-of-Medical-Necessity for
  grey-area items (sunscreen, electrolytes, certain OTCs); the
  framing's "submit the claim" reflex doesn't surface the
  substantiation requirement that converts a real medical
  expense into a denied claim if documentation is wrong.
- **Source evidence**: `framings.md` §13 Excludes line implicit
  via "FSA substantiation" vocabulary; HR-Reddit voice on
  FSA-substantiation-failures.
- **Trigger**: Asker is submitting FSA claims AND is using
  credit-card statements OR is including grey-area items
  (sunscreen, electrolytes, OTCs) without Letter-of-Medical-
  Necessity AND has not verified the FSA administrator's
  substantiation rules.
- **Failure mode**: FSA claim denied for inadequate
  substantiation; FSA forfeiture risk approaches as plan-year
  ends; asker has spent the money but can't be reimbursed;
  the framing's "submit the claim" was procedurally insufficient.
- **Recovery move**: For every FSA claim, attach itemized
  receipt (not credit-card statement) AND, for grey-area
  items, attach Letter-of-Medical-Necessity from the
  prescribing provider; verify the FSA administrator's specific
  substantiation rules in advance; consult HR / benefits
  administrator on the FSA-substantiation requirements AND a
  CPA on the Form-2441-or-similar reporting if substantial
  FSA spending is in dispute.

---

## 14. Single-payer / market-failure framing

### 14.1 Naming the system as broken doesn't help the asker at Tuesday's OE deadline

- **Statement**: The framing's structural critique doesn't
  translate to actionable advice for the asker at this Tuesday's
  OE deadline — naming the system as broken doesn't help the
  34-year-old choosing between HDHP and PPO this week. The
  framing's value is meta-explanatory but its direct decision-
  support utility is low.
- **Source evidence**: `framings.md` §14 Excludes line on the
  framing's direct decision-support utility being low; PNHP
  voice and the chronic-illness patient voice on the system-
  critique-as-meta-context vs decision-support distinction.
- **Trigger**: Asker is at a specific decision deadline (OE
  closing, COBRA election clock, Medicare IEP closing) AND is
  being routed to single-payer-framing content as decision-
  support rather than meta-context.
- **Failure mode**: Asker reads system-critique content; gets
  no help with the specific decision; misses the OE / SEP /
  IEP deadline; the framing's "system is broken" was diagnostically
  true but operationally useless for the binding decision.
- **Recovery move**: For asker at a specific decision deadline,
  surface the single-payer / market-failure framing as
  *meta-context* (system-explanation, validation of complexity)
  but route the operational decision through the directly
  applicable decision-support framing (F1–F13); consult a
  licensed health-insurance broker, SHIBA / SHIP volunteer, OR
  ACA-Marketplace Navigator on the deadline-binding decision
  AND treat F14 as Editor-layer context rather than primary
  decision lens.

### 14.2 Transition cost is the binding political-economy constraint the framing rarely engages

- **Statement**: Single-payer advocacy under-engages with the
  *transition cost* — the political-economy and institutional
  inertia of the current system are themselves the binding
  constraint that the framing's "we should have Medicare-for-
  all" rhetoric doesn't address, and the framing's adherents
  often present the alternative as self-evident without
  engaging the actual policy-design questions (provider-payment
  rates, capital-investment transition, employer-coverage
  transition path).
- **Source evidence**: `framings.md` §14 Excludes line on
  transition cost being the binding constraint; KFF / Health
  Affairs voice on the policy-design-detail gap in single-
  payer advocacy.
- **Trigger**: Asker is engaging with single-payer advocacy
  content AND is treating it as decision-support for personal
  coverage choice AND has not engaged the transition-cost
  policy-design questions.
- **Failure mode**: Asker reads advocacy content; assumes
  single-payer is imminent or even feasible on short horizon;
  declines to engage current-system optimization in favor of
  waiting; misses OE deadline; current-system worst-case
  applies in the meantime.
- **Recovery move**: For asker engaging with single-payer
  framing, surface the transition-cost reality (single-payer
  legislation is not on near-term US horizon; current-system
  decisions matter for the foreseeable future); route the
  operational decision through F1–F13 framings; consult a
  licensed health-insurance broker, SHIBA / SHIP volunteer, OR
  ACA-Marketplace Navigator on the current-system choice AND
  treat single-payer engagement as longer-horizon political
  participation rather than near-term coverage strategy.

### 14.3 "Expand Medicare" assumes Original Medicare is the model

- **Statement**: The framing's reflex toward "expand Medicare"
  assumes Original Medicare is the model — but Original Medicare
  itself has design flaws (no OOP cap, Part D donut hole until
  IRA 2025, no dental / vision / hearing) that the framing
  rarely names as needing reform. The "single-payer is the
  answer" rhetoric is structurally inconsistent with the actual
  Medicare program's coverage gaps.
- **Source evidence**: `framings.md` §14 Excludes line on the
  Medicare-model assumption; KFF voice on Medicare-design-gaps;
  SHIBA / SHIP volunteer voice on the no-OOP-cap-on-Original-
  Medicare as a routine planning constraint.
- **Trigger**: Asker is engaging with "expand Medicare" or
  "Medicare-for-all" content AND is reasoning from Original
  Medicare as the model AND has not surfaced Original Medicare's
  no-OOP-cap and other design gaps.
- **Failure mode**: Asker over-relies on "Medicare is good"
  reflex; assumes Original Medicare alone is comprehensive;
  reaches 65 without Medigap or MA evaluation; faces
  no-OOP-cap exposure on Original Medicare alone; the framing's
  model-clarity gap caused under-preparation.
- **Recovery move**: For any asker approaching 65 OR engaging
  with Medicare-as-model content, surface Original Medicare's
  specific design gaps (no OOP cap, Part D coverage gap, no
  dental / vision / hearing) AND the Medigap-or-MA decision
  that must accompany Original Medicare enrollment; consult a
  SHIBA / SHIP volunteer on the specific Original-Medicare-
  plus-Medigap-or-MA decision AND a licensed Medicare broker
  on the Medigap underwriting / GI question.

### 14.4 SHIBA and Navigator voices are apolitical by design

- **Statement**: F14 politicizes a domain where the asker often
  needs apolitical decision-support — a SHIBA volunteer doesn't
  advocate single-payer; a Marketplace Navigator doesn't
  advocate single-payer; the asker needing a plan this week is
  not well-served by a framing that grades the whole system.
  The framing's value is in *meta-context* for the Editor /
  Risk Officer layers, not in user-facing answers.
- **Source evidence**: `framings.md` §14 Excludes line on
  politicizing a domain where apolitical decision-support is
  needed; SHIBA / SHIP volunteer voice and ACA-Marketplace
  Navigator voice on the steering-prohibition and apolitical
  posture by design.
- **Trigger**: Asker is being routed to F14 content as primary
  decision-support OR is asking for "objective" help and being
  given political-advocacy framing.
- **Failure mode**: Asker receives political-advocacy framing
  when they need apolitical decision-support; disengages from
  the help offered; the framing's substantive value as
  meta-context is undermined by its operational mis-deployment.
- **Recovery move**: For asker requesting apolitical decision-
  support, route to SHIBA / SHIP volunteer, ACA-Marketplace
  Navigator, or licensed health-insurance broker (all of which
  are professionally constrained from advocacy); reserve F14
  content for Editor-layer system-validation context when the
  asker explicitly expresses frustration with the system as a
  whole; never default to F14 as primary decision lens.

### 14.5 Administrative-cost critique is correct but not actionable for the asker

- **Statement**: The framing's "US administrative costs at
  8–15% of premium dollar vs 1–3% in single-payer systems"
  analysis is substantively correct but not actionable for the
  asker's coverage choice; the asker can't reduce administrative
  cost by choosing differently among existing plans (all of which
  carry the structural administrative load). The critique is
  diagnostic but not prescriptive at the asker level.
- **Source evidence**: `framings.md` §14 Mental model on
  administrative cost; PNHP voice and healthcare-economics-
  journalist voice on the administrative-cost analysis.
- **Trigger**: Asker is reading administrative-cost critique
  AND is being told this critique should drive plan choice OR
  AND is treating administrative-cost as a personal-choice
  variable.
- **Failure mode**: Asker treats administrative-cost critique as
  decision-support; chooses plan on the basis that "all plans
  are equally bad on administrative cost" (true) without
  engaging the framing-relevant decision axes; the framing's
  diagnostic accuracy obscures the operational decision the
  asker still must make.
- **Recovery move**: For asker engaging administrative-cost
  framing, validate the diagnostic accuracy AND route the
  operational decision through the appropriate F1–F13 framings;
  consult a licensed health-insurance broker, SHIBA / SHIP
  volunteer, OR ACA-Marketplace Navigator on the binding
  decision AND treat F14 as Editor-layer context; for asker
  motivated by structural critique, route political engagement
  separately (advocacy organizations, voter contact, policy-
  comment processes) — these are real participation channels
  that don't conflict with the immediate coverage decision.

---

## Cross-framing tensions

Direct framing-pair conflicts surface where the same fact pattern is
read differently by adjacent framings; the asker over-anchored on one
needs the other's blindspots surfaced. These tensions are pulled from
`framings.md` "Cross-framing tensions" section and translated into
blindspot-tension form:

- **§1 (expected-utilization arithmetic) ↔ §2 (risk-transfer / OOP-
  cap)**. F1 minimizes probability-weighted total cost across
  utilization scenarios; F2 minimizes worst-case single-event
  exposure. §1.1 (embedded vs aggregate misread) and §2.1 (ACA OOP
  cap excludes non-EHB) are the cross-framing intersection: the
  asker over-anchored on F1's scenario-table calculation needs
  F2.1's reminder that the ACA OOP-cap they're treating as binding
  has gaps; the asker over-anchored on F2's "tail is capped" framing
  needs F1.1's reminder that the embedded-vs-aggregate distinction
  changes the cap's actual scope. Same facts (family-tier plan
  choice with chronic condition), opposite blindspot routing.

- **§3 (HSA-as-retirement) ↔ §4 (immediate-cost / cash-flow)**. F3
  says fund the HSA to the cap and let it compound; F4 says
  cash-flow constraint is binding and HSA-maximalism is infeasible.
  §3.1 (pay-OOP-let-HSA-compound requires liquidity) and §4.2
  (skipping care to save copay is a chronic-condition cliff) are
  the cross-framing tensions: the asker over-anchored on F3 needs
  F4.2's reminder that the cash-flow framing they're dismissing is
  what actually causes care-skipping; the asker over-anchored on F4
  needs F3.1's reminder that liquid-savings-first is the prerequisite
  for the F3 strategy they're rejecting wholesale. The Bogleheads-
  and-HSA-administrator voice pushes F3 dogmatically; the cash-
  flow and patient-advocate voices push F4. Triage should surface
  F4 when the asker reads as cash-flow-binding ("I'm living
  paycheck-to-paycheck") and surface F3 when the asker reads as
  savings-rich ("I'm maxing my 401k, looking for the next tax-
  advantaged bucket").

- **§5 (ACA-subsidy-mechanics) ↔ §9 (pre-existing-condition-
  protection)**. F5 reasons within ACA-marketplace plans; F9
  reasons across ACA-vs-non-ACA. §5.2 (ARPA / IRA enhanced subsidy
  sunset risk) and §9.4 (cost trade-off for healthy high-income
  askers) are the cross-framing tensions: the asker over-anchored
  on F5's marketplace-only framework needs F9.4's reminder that
  the sharing-ministry alternative may be cost-rational for
  healthy high-income askers; the asker over-anchored on F9's
  "ACA is the only safe option" reflex needs F5.2's reminder that
  the marketplace's subsidy generosity is itself a moving target.
  Triage should surface F9 when the asker mentions any chronic
  condition, any medication, or any prior medical event; surface
  F5 when the asker frames the question as "marketplace plan
  comparison."

- **§6 (Medicare-enrollment-irreversibility) ↔ §10 (network and
  prior-authorization)**. F6 makes the irreversibility of MA-vs-
  Original-Medicare dispositive; F10 makes the network breadth
  and prior-auth burden the binding axis. §6.3 (MA trial right is
  procedurally fiddly) and §10.2 (MA network drops mid-year are
  structural) are the cross-framing tensions: the asker over-
  anchored on F6 can be persuaded by an MA plan's "trial right"
  return path; F10.2 reminds them that mid-year network drops
  invalidate the enrollment-time assumption regardless of return
  rights. Both framings independently recommend Original Medicare +
  Medigap for high-utilization scenarios; both should be surfaced
  together because they converge on D8 even with different
  reasoning paths.

- **§8 (ERISA-procedural) ↔ §13 (bureaucratic-procedural / patient-
  advocate)**. F8 reasons at the regulatory-jurisdictional level;
  F13 reasons at the operational-form-and-deadline level. §8.5
  (180-day ERISA appeal deadline is strict) and §13.1 (procedural
  diligence is unsustainable during medical crisis) are the
  cross-framing tensions: the asker over-anchored on F8 needs
  F13.1's reminder that the procedural-exhaustion-requirement they're
  navigating requires cognitive bandwidth that may be unavailable
  during the actual medical crisis; the asker over-anchored on F13
  needs F8.5's reminder that the 180-day clock is starting
  regardless of whether they're tracking it. They converge in scope
  but diverge in remedy: F8 routes to an ERISA-litigation attorney
  early; F13 routes to a patient-advocate / billing-error-recovery
  service. Triage should surface both when denial dollars exceed
  $5k or when the asker mentions an SPD-reading issue.

- **§12 (tax-and-arbitrage) ↔ §4 (immediate-cost / cash-flow)**.
  F12's "max the HSA, time the last-month-rule, coordinate dep-
  care-FSA-vs-tax-credit" optimization assumes the asker can
  navigate Form 8889 / 2441 / 8962, has stable income, and
  prioritizes after-tax dollar maximization. F4 prioritizes
  cash-on-hand and predictable cost. §12.4 (LMR testing-period
  recapture) and §4.4 (variable-income askers need different
  cash-flow framework) are the cross-framing tensions: the asker
  over-anchored on F12 needs F4.4's reminder that the income-
  forecasting machinery they're relying on may not fit their
  income pattern; the asker over-anchored on F4 needs F12.4's
  reminder that the FSA / HSA elections they're making with cash-
  flow framing have tax-recapture exposure on the back end. The
  same $4,300 HSA contribution is a tax win in F12 and a cash-flow
  drag in F4.

- **§14 (single-payer / market-failure) ↔ §1, §2, §3, §4 (decision-
  support framings)**. F14 grades the system rather than the choice.
  §14.1 (naming the system as broken doesn't help at OE deadline)
  inverts F1's expected-utilization arithmetic, F2's risk-transfer
  reasoning, F3's HSA-retirement-vehicle calculus, and F4's
  immediate-cost framework. The asker engaging with F14 needs the
  reminder that the decision-support framings still apply at the
  binding deadline; the asker over-anchored on F1–F4 may benefit
  from F14 as Editor-layer meta-context when expressing system-
  level frustration, but not as primary decision lens. F14 should
  be surfaced as meta-context — never as the sole framing on an
  answer.

---

## Maturity note

This file is `planned` maturity per
[`_meta_ontology.md` §4](../_meta_ontology.md) (the health-insurance
domain is `planned`, like all V2 domains except tech-career which is
`in-migration`). Source-evidence lines above currently anchor to:

- `framings.md` Excludes lines (load-bearing — the framing-level
  Excludes were authored specifically to seed Layer 3, per the
  Notes-for-downstream-layers section of `framings.md`).
- Conceptual references to the health-insurance-specific community
  classes named in `framings.md` voice anchors (actuarial-and-broker
  voice, SHIBA / SHIP volunteer voice, ACA-Marketplace Navigator
  voice, HSA-administrator voice, ERISA-attorney voice, healthcare-
  economics-journalist voice — Sarah Kliff / Julie Rovner / Margot
  Sanger-Katz / Charles Ornstein, Bogleheads-meets-health-insurance
  voice, employer-benefits / HR-Reddit voice, ACA-reform-academic /
  KFF voice, single-payer / PNHP voice, patient-advocate / billing-
  error-recovery voice — NAHAC / AdvoConnection / Marshall Allen
  *Never Pay the First Bill* lineage, conservative-policy / Galen /
  AEI voice, chronic-illness / disability patient voice).

When `domain_knowledge/health-insurance/sources.yaml` is authored and
`domain_knowledge/health-insurance/communities/*.md` community profiles
land (Layer 4 is the next sub-item per ROADMAP §4 health-insurance
checklist), source-evidence lines below should be tightened to specific
source-view ids.

**Date-stamp risk**: anchor numbers below carry the date-stamp risk
inherited from the underlying ACA / Medicare / HSA contribution-limit
policy corpus. Entries to re-check before relying on for an active
decision:

- §1.1, §2.1, §11.1, §11.4 — 2026 OOP-max ceilings ($9,450 self-only /
  $18,900 family for ACA; $8,300 / $16,600 for HDHP). These index
  annually; verify current year before applying.
- §3.3, §6.1 — Medicare Part A retroactivity (6-month look-back on
  SS-claim after 65) is statutory but interpretive details shift;
  re-check current SSA policy.
- §3.5 — DPC-and-HSA compatibility (IRS Notice 2013-54 + subsequent
  guidance; pending legislation could formalize); date-stamp risk.
- §5.2 — ARPA / IRA enhanced subsidies expire end of 2025 absent
  congressional extension; verify current subsidy schedule each OE.
- §5.4 — DACA marketplace eligibility (vacated late 2025; date-stamp
  risk on the regulatory posture).
- §6.5 — GEP-enrolled coverage start date (changed in 2023 from
  July-start to month-after-enrollment); verify current SSA rule.
- §3.1, §12.2 — 2026 HSA contribution limits ($4,300 self / $8,550
  family + $1,000 55+ catch-up). These index annually; verify current
  year.
- §8.4 — 2026 Medicare ALJ amount-in-controversy minimum ($1,840 for
  ALJ; $9,000+ for federal-court review). Indexed annually.
- §12.1 — IRMAA brackets (2-year-lookback; brackets index annually);
  verify current year.
- §13.3 — No Surprises Act IDR methodology (litigated in multiple
  *Texas Medical Association v. HHS* rulings; methodology has shifted
  multiple times); verify current arbitration rules.

**Mechanism E posture**: every Recovery move above routes to one of:
licensed health-insurance broker, SHIBA / SHIP volunteer, ACA-
Marketplace Navigator, CPA (HSA / FSA / Form 8889 / Form 8962
coordination), ERISA-litigation attorney (self-funded employer plan
denial appeals), State Insurance Commissioner (STLDI rescission
complaint, fully-insured-plan grievance, external review), or
patient-advocate / billing-error-recovery service. This is **uniform
Mechanism E gating** like immigration (PR #48), not partial-gating
like housing (PR #64). The wrong call here is not recoverable on a
multi-year horizon: missed IEP triggers lifetime Medicare premium
loading; missed 60-day marketplace SEP forecloses coverage until next
OE; post-claim STLDI rescission converts $200k in "covered" claims
back to "uninsured" retroactively; 12-month plan-year lock-in
forecloses mid-year correction outside narrow QLE windows. This file
IS decision-support, NOT licensed-broker / SHIBA-counselor / CPA /
ERISA-attorney / State-Insurance-Commissioner advice. The framings
name where the analysis happens; the binding determination on any
specific decision comes from the professional with case-specific
facts — current SPD, current Healthcare.gov regulatory posture,
current IRS / CMS revenue rulings, the asker's full medical and
income picture, and the asker's full claim history.
