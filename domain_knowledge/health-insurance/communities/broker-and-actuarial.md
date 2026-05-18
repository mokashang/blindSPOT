# Broker and Actuarial

Licensed-broker bulletin and actuarial-research voice — the
practitioners and analysts who quote premium-vs-OOP-max-vs-network
trade-offs out of expected-utilization tables, read NAIC standardized
Medigap plan letters as bright-line statutory categories, and reason
about plan design out of trend-rate research. This community is a
SOURCE of decision-support framings on commercial / individual-market
plan selection and the actuarial mechanics that drive it; it is **not
a substitute** for case-specific licensed-broker advice during open
enrollment, nor for the SHIBA-side counterweight on Medicare
decisions where broker commission incentives systematically tilt
recommendations toward Medicare Advantage. The blog post tells you
where the analysis lives; the licensed independent broker (commercial
OE) is where the binding plan-selection conversation happens with the
asker's actual carrier appointments, dependents, and prescriptions in
hand.

## Identity

Practitioners who sell or analyze health insurance for a living —
NAHU / NABIP-credentialed brokers and benefits consultants on the
commercial side, FSA / ASA / MAAA actuaries on the research side.
They reason about coverage as a stochastic-cost-distribution problem
with statutory constraints: ACA §1302 essential health benefits,
metal-tier actuarial-value bands (Bronze 60% / Silver 70% / Gold 80%
/ Platinum 90% ±2 de minimis), Medigap standardized plan letters
(Plans A–N post-2010/2020 reforms), MLR floor (85% large-group / 80%
small-group / individual). They are *not* the consumer-finance
generalist who treats premium as the sole price signal, nor the
chronic-illness patient community that lives inside formulary churn —
they are the people who priced the formulary churn into the premium.

## Voice anchors

- Source-views from `health-insurance/sources.yaml` under this
  community_tag:
  - `naic-consumer-guides` — NAIC (National Association of Insurance
    Commissioners) Medigap standardized-plan reference, state-
    insurance-commissioner directory, No Surprises Act IDR data.
  - `ehealth-broker-blog` — eHealth Resource Center, a large national
    licensed-broker outlet publishing comparison content across
    commercial, Marketplace, and Medicare-Advantage / Medigap product
    lines.
  - `milliman-research` — Milliman + Oliver Wyman + Wakely actuarial
    research publications (Milliman Medical Index annual; Aon /
    Mercer employer-plan trend reports).
- Adjacent named voices / outlets: Society of Actuaries (SOA) Health
  Section newsletter; Conference of Consulting Actuaries (CCA);
  American Academy of Actuaries (AAA) Health Practice Council;
  AcademyHealth research conference; *Health Affairs* applied-
  actuarial papers; NAHU / NABIP regional chapter publications;
  GoHealth, eHealth, HealthMarkets brokerage research desks;
  Healthinsurance.org (Louise Norris's consumer-facing licensed-
  broker explainer).

## Mental model

Health insurance is a contract priced from an expected-utilization
distribution under statutory constraints — premium, deductible, OOP-
max, and network adequacy each carry a measurable cost, and the
prudent enrollee chooses the combination that minimizes worst-case
exposure conditional on a plausible utilization scenario. The metal-
tier actuarial-value bands and Medigap plan letters are *bright-line
statutory categories*: any Plan G sold by any insurer in any state
covers the same benefits, so premium is the only legitimate
differentiator (carrier service quality is secondary signal, not
benefit-design difference). Trend-rate is the load-bearing variable
on the employer side — the Milliman Medical Index publishes the
benchmark every May, and the year-over-year cost trajectory ripples
into employer plan-design decisions that the broker layer reads
downstream. The fully-insured-vs-self-funded jurisdictional line
controls remedy: state insurance commissioner has authority over
fully-insured plans; ERISA pre-empts state remedies on self-funded
plans, which is why the SPD's "insurance information" disclosure
matters. Risk pooling and adverse selection are real and structural,
not rhetorical — the individual-market death spiral of 2014–2018 and
the post-2018 stabilization track this exactly.

## Characteristic vocabulary

- "Actuarial value (AV)", "metal tier", "de minimis variation
  (±2%)", "essential health benefits (EHB)", "categorical exclusion"
- "Medical Loss Ratio (MLR)", "MLR rebate", "ASO" (administrative
  services only, self-funded contract type), "stop-loss", "carve-out"
- "Trend rate", "Milliman Medical Index (MMI)", "PEPM" (per employee
  per month), "PMPM" (per member per month), "leveraging"
- "OEP" (Open Enrollment Period), "SEP" (Special Enrollment Period),
  "QLE" (Qualifying Life Event), "1095-A reconciliation"
- "OOP max", "embedded vs aggregate deductible", "coinsurance",
  "copay tier", "network tier (T1 / T2 / OON)", "balance billing"
- "Medigap GI window", "guaranteed-issue", "underwriting", "open
  enrollment for Medigap (6-month §1395ss-1(b) window)"
- "Risk adjustment", "HCC coding", "Medicare Advantage RAF score",
  "supplemental benefits"
- "NAHU", "NABIP", "FSA / ASA / MAAA" (actuarial credentials)

## Known blind spots OF this community

- **Commission-structure bias toward Medicare Advantage.** Broker
  commission on MA enrollment routinely exceeds commission on
  Medigap, and the broker's recommendation conversation reflects
  that economic gradient even when the asker's chronic-condition
  profile and Medigap GI-window timing argue for traditional
  Medicare + Medigap. Trigger: a broker post on "Medicare options"
  that leads with MA's $0-premium and supplemental-benefit framing
  without naming the Medigap underwriting cliff after the 6-month
  GI window expires. Failure mode: an asker enrolls in MA at 65,
  develops a chronic condition at 67, attempts to switch to
  Medigap, and is underwritten-out — Medigap GI is now closed and
  the asker is locked into MA's prior-auth and network constraints
  for life. Recovery: route Medicare-timing decisions to a SHIBA /
  SHIP non-commissioned counselor (per `framings.md` §"Voice
  anchors"; per `sources.yaml` community `medicare-shiba-and-
  government`) before signing the MA election; explicit named-
  professional referral satisfies the Mechanism E posture for D4 / D8.

- **Expected-utilization framing under-weights chronic-utilizer
  reality.** Broker scenario-tables price "high-utilizer" as a tail
  scenario; for an asker with diabetes, MS, ankylosing spondylitis,
  Crohn's, lupus, or any specialty-tier-drug regimen, high-utilizer
  is the *recurring baseline*, not the tail. Trigger: an eHealth
  comparison page recommending the HDHP-with-HSA option as "best
  for healthy individuals" without surfacing that the same asker's
  specialty-tier drug at Tier 4 routinely costs $2,000–8,000/month
  pre-OOP-max and exhausts the HSA balance in the first quarter.
  Failure mode: the asker picks a $200/month-cheaper HDHP, hits the
  full $7,500 individual deductible by April, and discovers the
  formulary excluded their drug from the tier-4 list mid-year with
  60-day notice on a non-protected class. Recovery: cross-reference
  against `chronic-illness-patient-experience` community
  (`sources.yaml` community `chronic-illness-patient-experience`)
  for the inverse framing; consult an independent licensed broker
  with the asker's actual medication list and current pharmacy
  before committing to plan selection.

- **State-insurance-commissioner-remedy assumption.** Broker-side
  resources routinely route denial / appeal questions to "your
  state insurance commissioner" without checking whether the plan
  is fully-insured (commissioner has jurisdiction) or self-funded
  (ERISA pre-empts; remedy is administrative appeal then federal
  §502(a) civil action). Trigger: an eHealth or NAHU post on
  "denied claim recourse" that lists state-insurance-commissioner
  contact as Step 1 without naming the SPD-disclosure check.
  Failure mode: the asker spends 6–9 months pursuing a state
  commissioner complaint that the commissioner declines for lack
  of jurisdiction; ERISA's 180-day appeal clock has tolled; the
  asker has no remedy. Recovery: read the SPD's "insurance
  information" disclosure or check Form 5500 filing; if self-
  funded, route to an ERISA-side plaintiff attorney
  (`sources.yaml` community `erisa-and-denial-appeal-law`) before
  the §502(a) administrative-exhaustion clock runs.

- **Practitioner-economic structural bias: "commission product
  recommendation is the firm's product."** Licensed brokers are
  paid by carrier commission, not by the consumer, even when the
  consumer-facing branding is "free help." The signal is real
  (broker has carrier appointments, plan-design literacy, and
  enrollment-workflow access) and the economic alignment is real
  (commission is paid by the insurer the broker enrolls the asker
  into). Trigger: a broker steering an asker who'd qualify for ACA
  Marketplace APTC subsidies into a non-subsidy-eligible direct-
  carrier policy because Marketplace commission is lower or zero.
  Failure mode: the asker pays full premium for a year on a plan
  that, on Marketplace, would have cost $0–$200/month after APTC.
  Recovery: cross-check the broker's recommendation against
  Healthcare.gov's anonymous plan-finder + KFF subsidy calculator
  (`sources.yaml` community `aca-marketplace-and-navigator`); a
  CMS-trained Navigator is structurally prohibited from steering
  and is a non-commissioned counterweight.

- **Trend-rate research lags lived-experience signal by 12–24
  months.** Milliman Medical Index publishes the prior plan year's
  data; Mercer / Aon employer surveys are annual. By the time the
  trend number reaches the broker's slide deck, the underlying
  utilization shift (GLP-1 explosion 2023–2025, specialty-tier
  growth, post-COVID care-deferral catch-up) has already moved.
  Trigger: a 2024 broker-blog post citing a 2023 trend rate (which
  itself reports 2022 data) to argue an employer plan-design
  scenario; asker treats the cited number as current. Failure mode:
  premium projections used for D7 (job-change benefits-differential)
  understate the actual carrier-renewal increase by 200–400 bps;
  the asker locks in a side that proves uncompetitive on next-year
  renewal. Recovery: cross-check trend claims against
  `healthcare-economics-journalism` reporting (`sources.yaml`
  community `healthcare-economics-journalism`) for the same plan
  year — journalism catches lived-experience shifts before the
  actuarial publication cycle does.

## Mechanism E posture

Health-insurance is `high_stakes: true` per `_meta_ontology.md` §4.
Every blindspot above ends with a Recovery move routed to a named
professional channel. For broker-and-actuarial-sourced framings the
default channel is a **licensed independent broker on commercial /
individual-market plan selection (commercial OE)** — independent
because captive-agent appointments at a single carrier reproduce the
commission-structure bias above; licensed because state-by-state
producer licensing is the consumer-protection floor (NAIC model law,
state insurance department enforcement). Where the decision crosses
into Medicare timing (D4 / D8), Mechanism E re-routes the channel to
**SHIBA / SHIP counselor** (non-commissioned, federally-funded under
SSA §4360); where the decision crosses into Marketplace subsidy
arithmetic (D5), to a **CMS-trained Navigator** (prohibited from
steering, 45 CFR §155.215); where the asker has a self-funded plan
and a denied claim, to an **ERISA-side attorney** (29 USC §1132
civil enforcement). This community is the framing layer; the named
professional with case-specific facts is the binding-determination
layer.
