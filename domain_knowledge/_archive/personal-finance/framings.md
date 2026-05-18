# personal-finance — framings.md (Layer 2)

Framing library for `personal-finance`. Each entry names one lens — the
way a specific community / tradition / profession argues about a
decision — and lists the decisions from
[`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

The `personal-finance` domain is **high_stakes: true** per
[`_meta_ontology.md` §5](../_meta_ontology.md) and is the canonical
Mechanism E gating case named in
[ROADMAP §5](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating).
Dollar-specific investment recommendations on individual securities
(buy $X of TICKER today with your $Y) are uniformly out-of-scope at
the Editor layer regardless of which framing is active — this is the
load-bearing gate the domain was written around. Framings below name
*axioms and trade-offs the household must reason about*, not
individual portfolio recommendations. The binding determination on
any specific case comes from a category-appropriate professional
(fee-only fiduciary CFP / experienced-CPA / ERISA attorney /
fee-only-Social-Security planner / state-bar-estate attorney —
keyed to the specific decision per the selective-referral matrix in
[`decisions.md` §Notes](./decisions.md)). Where a framing names a
statute, rule, or threshold (IRC §401(k), §408 IRA, §223 HSA, §529,
§1202 QSBS, §1031 like-kind, §1202 / §1244 small-business stock,
§7702 life-insurance, §72(t) early-distribution-exceptions, ERISA
§404 / §405 / §1144, SECURE Act 1.0 / 2.0, TCJA 2017 / sunset 2026,
IRMAA tables from CMS, FAFSA-Simplification-Act 2020 / 2024-rules),
treat the citation as a pointer to where the analysis happens, not
as the answer.

Three distinct classes of irrevocability drive the high-stakes
posture and shape every framing below, mirroring the structure in
[`decisions.md`](./decisions.md):

- **Tax-year-boundary one-shot windows**: contribution caps,
  backdoor-Roth pro-rata timing, mega-backdoor-Roth plan-document
  features, 5-year-Roth-conversion clocks, and HSA last-month-rule
  testing-period each compound on calendar-year boundaries that
  cannot be redone after April 15 (extended to Oct 15 for some).
  Roth-conversion-recharacterization was permanently eliminated by
  TCJA 2017 — conversions are irrevocable from the moment executed,
  full stop, no "undo."
- **Permanent penalties on Social-Security / Medicare-adjacent
  mechanics**: Social-Security claim-age before FRA permanently
  reduces PIA ~30% at age 62 and compounds for the survivor's life
  via the higher-earner-survivor rule; missing the 60-day indirect-
  rollover window turns the distribution into a taxable event with
  no second chance; wash-sale violations defer losses into the
  basis of the replacement security where they may be functionally
  lost (Rev Rul 2008-5 in tax-advantaged-account context).
- **Compounding-cost-of-procrastination**: retirement-contribution
  gaps compound at the equity risk premium for 30+ years and cannot
  be re-made later because caps are per-year-use-it-or-lose-it. A
  missed $7,000 Roth-IRA contribution at age 30 compounds to ~$76k
  at age 65 at a 7% real return — the asymmetry between
  procrastinable life-decisions and non-procrastinable annual-cap
  decisions is itself a framing axis (see F1, F11).

Framings that handle one of these classes well often miss the
others; the opposing-framing pairs below frequently divide along the
contribution-cap-window / SS-Medicare-permanence / procrastination-
asymmetry boundaries.

Voice anchors (conceptual, not source URLs — those live in
`sources.yaml` once authored): **fee-only-fiduciary-CFP voice**
(NAPFA / XY-Planning-Network / Garrett-Planning fee-only-not-fee-
based discipline, structural-conflict-of-interest as load-bearing
analytical frame, fiduciary-rule-vs-suitability-standard distinction,
AUM-fee-vs-flat-fee-vs-hourly-fee compensation transparency);
**Bogleheads voice** (bogleheads.org wiki and forum, three-fund
portfolio, low-cost-index-fund dogma, expense-ratio-and-tax-drag-
minimization, investment-priority-order canonical sequence, stay-
the-course-through-drawdown discipline); **Mr-Money-Mustache / FIRE-
community voice** (mrmoneymustache.com, ChooseFI podcast,
r/financialindependence, 4%-safe-withdrawal-rate, savings-rate-as-
years-to-retirement, geographic-arbitrage, sabbatical-as-Roth-
conversion-window); **financial-economics-journalism voice** (David
Wessel at Brookings, Jeff Sommer at NYT, Anne Tergesen at WSJ —
structural-policy-context, retirement-savings-system critique,
SECURE-Act and CRS-report-grounded reporting); **retirement-econ
academic voice** (Wade Pfau on safe-withdrawal-rate / bond-tent /
HECM-reverse-mortgage; Michael Kitces on Roth-conversion-laddering /
asset-location / Social-Security-claiming; Larry Kotlikoff on
Maximize-My-Social-Security software / lifecycle finance); **the
Finance Buff voice** (thefinancebuff.com Harry Sit — backdoor-Roth
mechanics, Mega-Backdoor-Roth plan-document analysis, HSA-payroll-
vs-after-tax-FICA-arbitrage, tax-software-Form-8606 step-by-step);
**retirement-experienced-CPA voice** (CPAs with retirement-plan
and equity-comp practice depth — NOT generic-tax-prep CPAs;
distinguish via experience with Form 8606 / Form 5498 / Form 1099-R
rollover-code reconciliation, ESPP / RSU / ISO / 83(b) experience,
Roth-conversion-modeling, IRMAA-and-NIIT-cliff-management);
**ERISA-practitioner voice** (ERISA-attorney forums, plan-document
analysis, Rule-of-55 / SEPP-72(t) early-distribution-exception
mechanics, QDRO drafting, fiduciary-breach §404 / §405 claims,
state-vs-federal creditor-protection mapping, *Egelhoff* and
*Patterson v Shumate* doctrine); **SEC-EDGAR / investor-alerts /
FINRA-BrokerCheck voice** (procedural-floor for any individual-
professional vetting, disclosure-event surfacing, Form ADV Part 2
fee-and-conflict disclosure analysis, registered-rep vs IAR
distinction); **IRS-publication-authority voice** (Pub 550
investment-income-and-expenses, Pub 590-A IRA-contributions, Pub
590-B IRA-distributions, Pub 525 taxable-and-nontaxable-income,
Pub 969 HSA-and-FSA, Pub 970 education-tax-benefits — the
authoritative ground truth for tax-mechanic disputes, against which
all advisor / blog claims should be reconciled); **fee-only Social-
Security claiming-specialist voice** (Mike Piper's Open-Social-
Security and *Social Security Made Simple* / Larry Kotlikoff's
Maximize-My-Social-Security software / federally-funded SHIBA / SHIP
volunteer for Medicare-coordination — non-commissioned, lifecycle-
math-grounded); **state-bar-estate-attorney voice** (trust-formation
SLAT / GRAT / Dynasty / CRT / CLT drafting, beneficiary-form-audit-
and-update, 2025-doubled-exemption-sunset planning, anti-clawback
Reg §20.2010-1(c) analysis); **personal-finance-influencer /
mass-media voice** (Suze Orman, Dave Ramsey, Ramit Sethi — high-
reach simplifications that capture useful patterns (snowball-vs-
avalanche, automate-savings) but often dogmatize at the cost of
edge-case nuance, especially around IRR-of-debt-payoff vs match-
capture and Roth-vs-traditional arithmetic); **chronic-DIY-Reddit
voice** (r/personalfinance, r/Bogleheads, r/financialindependence,
r/tax — flowchart-driven, peer-reviewed at scale, fast feedback on
edge cases, but variable quality and occasional dogmatism on
"the wiki says")—.

Cross-domain edges: F1 (investment-priority-order) carries the
principal cross-cutting role into `tech-career` (RSU / ISO / ESPP /
83(b) timing affects cash-available-for-contribution and the
priority-order-step-1-match-capture is dollar-binding regardless),
`health-insurance` (HSA-eligibility-and-HDHP-enrollment in step 3 of
the priority order is the load-bearing boundary into the
health-insurance domain), and `entrepreneurship` (solo-401(k) /
SEP-IRA / SIMPLE-IRA substitution for W-2 401(k) in step 4 changes
the pro-rata-IRA-trap-on-backdoor-Roth math). F4 (tax-arbitrage)
routes into `health-insurance` (HSA Section 125 cafeteria-plan FICA
arbitrage; IRMAA 2-year-lookback Medicare-premium implication),
`tech-career` (RSU-vest-and-sell vs hold, ISO-AMT-exercise-timing
parallel-tax calculation), and `housing` (mortgage-interest-
deduction-and-SALT-cap-interaction, Section-121-primary-residence-
cap-gains-exclusion on downsize). F8 (asset-protection-and-creditor-
shield) routes into `legal-disputes` (state-vs-federal-bankruptcy-
protection mapping, QDRO division on divorce, ERISA pre-emption of
state-law remedies), `entrepreneurship` (LLC-vs-S-corp asset
isolation, professional-liability-insurance interaction with
retirement-account shield), and `family-planning` (premarital-
agreement and post-marital-property characterization). F11
(behavioral-finance) is a meta-framing on all decisions but applies
most directly to F2, F3, F5 (where the technical-optimum often loses
to the behaviorally-sustainable). Routing across edges is V2-Triage's
job; these edges help framings name adjacent domains rather than
absorb their content.

---

## 1. Investment-priority-order framing

- **Decisions it applies to**: D1 (retirement-account contribution
  ordering), D2 (traditional vs Roth split at the contribution
  point), D5 (debt-payoff vs invest prioritization — where the
  match-capture step interleaves with high-interest-debt-payoff),
  D9 (529 vs Roth vs taxable — where 529 falls in the priority
  pipeline, typically late).
- **Mental model summary**: Cash flow available for retirement and
  long-term savings should flow through a *canonical priority
  ordering* across vehicles, with each step strictly dominating
  the next on after-tax-IRR-per-dollar-invested grounds. The
  Bogleheads-canonical sequence is: (1) capture the full
  employer-401(k) match (100% immediate return dominates all
  alternatives); (2) pay down debt above ~7% effective APR; (3) max
  HSA if HDHP-eligible (triple-tax-advantaged plus FICA exemption
  on payroll contributions, strictly dominates 401(k)-beyond-match
  dollar-for-dollar); (4) max traditional-or-Roth 401(k) to the
  elective deferral cap; (5) max Roth IRA (direct if income-eligible,
  backdoor otherwise); (6) Mega-Backdoor Roth via after-tax 401(k) +
  in-plan-conversion if plan supports; (7) 529 for kids; (8) taxable
  brokerage; (9) low-interest debt paydown. The framing reasons in
  ordering-and-dominance terms: each step is strictly dominated by
  every earlier step until cap is hit, then the next step opens.
  Characteristic move: when an asker asks "should I do X or Y," the
  framing first checks where X and Y sit in the priority pipeline,
  and the earlier-step option wins automatically until that step is
  capped. Anchor: 2025 caps are 401(k) elective deferral $23,500 +
  $7,500 age-50 catch-up + $11,250 age-60-63 super-catch-up (SECURE
  2.0 §603), HSA $4,300 self / $8,550 family + $1,000 age-55 catch-
  up, Roth IRA $7,000 + $1,000 age-50 catch-up, §415(c) total
  401(k) cap $70,000.
- **Characteristic vocabulary**: "investment priority order", "match
  capture is non-negotiable", "100% immediate return", "triple-tax-
  advantaged HSA", "Mega-Backdoor Roth", "after-tax 401(k) +
  in-plan-conversion", "§415(c) total cap", "elective deferral
  cap", "backdoor Roth", "pro-rata-trap-on-existing-pre-tax-IRA",
  "step-up the priority order", "Bogleheads flowchart", "above-the-
  match dollar."
- **Excludes**:
  - The "100% match dominates 25% credit-card-APR" reflex is
    correct on long-horizon IRR math, but the framing rarely
    engages with *match-vesting cliffs* — many 401(k) plans have
    1-to-6-year cliff or graded vesting on the employer match, and
    an asker who is reasonably-likely to leave before vesting (FAANG
    median tenure ~2 years; PIP / RIF probability non-trivial)
    faces an "expected-match-after-vesting" that is materially
    less than 100%. The framing's "always max the match" misses
    job-tenure-conditioned expected value. Opposes F11 (behavioral-
    finance) where tenure-uncertainty interacts with payoff-of-
    sticking-with-employer.
  - Step 3 (HSA-as-stealth-IRA) treats HDHP-enrollment as a free
    upgrade once HSA-eligibility opens, but the HDHP-vs-PPO trade-
    off on the medical-coverage side can dominate the HSA tax
    arbitrage for households with chronic conditions or expected
    high utilization (cancer survivor, pregnancy planning, child
    with autism / ABA-therapy, parent on biologics). The framing's
    "step 3 dominates step 4" elides the medical-cost-on-the-HDHP-
    side calculation entirely. Boundary `health-insurance` D1, F1.
    Opposes F3 (HSA-as-retirement-vehicle when over-applied).
  - The framing assumes the asker has *one* set of vehicles available
    — but dual-W-2 couples have *two* 401(k)s, *two* HSAs (only one
    if family-HDHP-coverage on one spouse's plan), *two* Roth-IRA
    caps; the cross-spouse-coordination layer is structurally absent
    from the single-asker flowchart, and the optimal joint sequence
    isn't simply "each spouse runs the flowchart on their own paycheck."
    The framing's individualism misses spousal-IRA rules and
    HSA-family-coverage-restriction-to-one-account. Boundary
    `family-planning`.
  - The priority order is calibrated to a W-2-employed knowledge-
    worker with stable cash flow; for self-employed / 1099 /
    equity-comp-heavy / lumpy-income askers, the steps don't map
    cleanly (solo-401(k) and SEP-IRA substitute for the W-2 401(k);
    SEP-IRA balance triggers pro-rata on backdoor Roth in step 5),
    and the framing rarely degrades-gracefully to the
    self-employment-cash-flow reality. Boundary `entrepreneurship`.

## 2. Marginal-rate-arbitrage framing

- **Decisions it applies to**: D2 (traditional vs Roth split — the
  central decision-input), D7 (Roth conversion ladder in low-income
  years — bracket-filling arithmetic), D8 (retirement withdrawal
  sequencing — drawing the right bucket against the current-year
  bracket), D1 (priority order interacts with this at the
  traditional-vs-Roth choice within step 4 / step 5).
- **Mental model summary**: Every contribution and withdrawal
  decision is an arbitrage between the *current marginal rate*
  (federal + state + FICA where applicable) and the *projected
  retirement marginal rate* (federal + state at the retirement
  state + Medicare IRMAA implications). The first-order rule is
  simple: contribute to traditional when current > projected, Roth
  when current < projected, with ties going to Roth for hedge-
  against-future-rate-rises reason. The framing reasons in
  bracket-staircase terms: 2025 federal brackets step at
  $11,925 / $48,475 / $103,350 / $197,300 / $250,525 / $626,350 (single);
  $23,850 / $96,950 / $206,700 / $394,600 / $501,050 / $751,600 (MFJ);
  state brackets stack on top (CA tops at 13.3%, NY ~10.9%, NJ
  ~10.75%, OR ~9.9%); FICA is 7.65% on wages below the SS-wage-
  base ($176,100 in 2025) plus 1.45% Medicare uncapped plus 0.9%
  Additional-Medicare above $200k single / $250k MFJ; NIIT 3.8% on
  net-investment-income above $200k / $250k. The arbitrage extends
  to Roth conversions during low-income years (sabbatical, job-loss,
  business-loss, NOL-carryforward, early-retirement-bridge to
  Medicare). Characteristic move: build a bracket-fill table for
  the current year, identify the next bracket-cliff, size the
  conversion or contribution to land exactly at the top of the
  current bracket. Anchor: the AMT exemption ($88,100 single / $137,000
  MFJ 2025) and AMT phase-out apply on top for high-ISO-exercise
  years (boundary `tech-career`).
- **Characteristic vocabulary**: "current marginal rate", "projected
  retirement marginal rate", "bracket fill", "bracket creep",
  "marginal-rate arbitrage", "tax-bracket cliff", "IRMAA tier",
  "AMT exemption", "NIIT 3.8%", "Additional Medicare 0.9%", "state-
  tax residency change in retirement", "Roth-conversion ladder",
  "fill the 12% bracket", "fill to the top of the 22%", "spillover
  into 24%", "asymmetric-cap-utility-Roth-vs-traditional."
- **Excludes**:
  - The "current marginal vs projected retirement marginal" framing
    is a *point-estimate* on a future that depends on (a) future
    federal-bracket changes (TCJA brackets sunset Dec-31-2025
    absent extension; in 2026 the 12% bracket reverts to 15%, 22%
    to 25%, 24% to 28%), (b) future state-of-residence, (c) future
    RMD-induced bracket-creep, (d) future Social-Security
    taxability thresholds (NOT inflation-indexed since 1983),
    (e) future Medicare-IRMAA tiers. The framing's deterministic
    arithmetic understates the *distributional* nature of the
    projection. Opposes F12 (single-payer / policy-volatility) at
    the federal-bracket-sunset boundary.
  - The framing's bracket-fill discipline assumes the asker can
    *project current-year income with precision* — but for equity-
    comp askers (RSU vesting on grant-date schedule plus market
    price), self-employed askers, and any asker mid-year on
    sabbatical or layoff, year-end-income is genuinely uncertain
    well into Q3, and a Roth conversion sized to "fill the 22%
    bracket" can spill into 24% if Q4 income surprises upward.
    Conversions are irrevocable (TCJA 2017 eliminated
    recharacterization) — size conservatively at year-start, fund
    mid-year as income clarifies, NEVER lump-all-in-January.
    Boundary `tech-career`.
  - The "asymmetric-cap-utility" argument (Roth $23,500 contains
    more after-tax-equivalent room than traditional $23,500) is
    correct *for cap-constrained savers* but is structurally
    invisible to the asker who isn't hitting the cap — the framing
    rarely surfaces this nuance, and the popular-press version
    ("Roth is always better for young people") propagates the
    cap-constrained logic to askers who don't face the cap.
  - The framing under-engages with *FICA on traditional-401(k)
    contributions* — traditional 401(k) contributions are pre-
    federal-and-state-income-tax but NOT pre-FICA, while HSA
    payroll contributions are pre-FICA. For high-FICA-bracket
    askers below the SS-wage-base, HSA-vs-traditional-401(k) marginal
    arbitrage includes a 7.65% FICA advantage to HSA that the
    "20% federal + 9.3% CA = 29.3% combined" calculus misses. The
    Finance Buff voice catches this; the personal-finance-blogger
    voice often doesn't.

## 3. HSA-as-stealth-IRA framing

- **Decisions it applies to**: D1 (priority order — step 3 placement
  ahead of 401(k)-beyond-match), D3 (asset location — HSA as the
  highest-return-bucket for stocks not cash), D8 (retirement
  withdrawal sequencing — HSA as Medicare-premium-payer in
  retirement), D10 (estate-and-beneficiary structuring — HSA-to-
  non-spouse-beneficiary tax-trap).
- **Mental model summary**: An HSA is *the most tax-advantaged
  account in the US tax code* — triple-tax-advantaged (pre-tax
  contribution with FICA exemption on payroll, tax-free growth,
  tax-free withdrawal for qualified medical), no required minimum
  distributions, no income-cap on contributions (unlike Roth),
  portable across employers, and inheritable to a spouse without
  ordinary-income recognition. The framing reasons in long-horizon-
  compounding terms: HSA dollars invested for 30+ years in a
  low-cost index fund grow to $250k–$500k per person on max
  contributions, and qualified medical expenses in retirement
  (Medicare Part B / D / Medigap premiums, dental, vision, qualified
  LTC up to IRS-published age-indexed limits) absorb that growth
  tax-free. The strategy is: fund HSA to the cap; pay current
  medical OOP from after-tax savings; "shoebox the receipts" and
  reimburse decades later tax-free. Post-65 non-qualified
  withdrawals become ordinary-income-but-no-penalty (HSA is
  effectively a traditional-IRA at that point). Characteristic
  move: when HDHP is on the OE menu, choose it whenever the
  long-run HSA tax arbitrage exceeds the short-run PPO premium-
  saving (almost always for healthy or low-utilization askers).
  Boundary `health-insurance` decisions 1, 6, 9.
- **Characteristic vocabulary**: "triple-tax-advantaged",
  "HSA-as-retirement", "stealth IRA", "FICA exemption on payroll
  HSA", "shoebox the receipts", "Form 8889", "IRC §223", "qualified
  medical expense", "Medicare-premium HSA qualified use", "post-65
  non-qualified withdrawal as ordinary-income-no-penalty", "HSA
  investment threshold", "spouse-as-HSA-beneficiary continues HSA
  treatment."
- **Excludes**:
  - The "pay OOP, let HSA compound" strategy assumes the asker has
    sufficient taxable savings to fund current medical without
    raiding the HSA; for askers with cash-flow constraints (early-
    career, paying down debt, single-income household with kids),
    the prescription is correct in theory and infeasible in
    practice. The framing rarely degrades-gracefully to "if you
    can't bank the receipts, just use HSA for current spend — you
    still get the contribution-side tax deduction." Opposes F4
    (tax-arbitrage when cash-flow-constrained) and F11 (behavioral-
    finance).
  - HSA-eligibility is *fragile in retirement-adjacent timing*:
    any non-HDHP coverage (general-purpose FSA, spouse's
    general-purpose FSA, Medicare Part A, VA care within prior
    3 months, Tricare, DPC without ancillary structuring)
    disqualifies HSA contributions — and Medicare Part A is
    *retroactive up to 6 months* when Social-Security-claiming
    after 65, which silently invalidates 6 months of HSA
    contributions the framing's "max until SS-claim" timing
    doesn't catch. Stop HSA contributions 6 months before SS-claim
    if claiming past 65. Boundary `health-insurance` D9.
  - HSA-inherited-by-non-spouse becomes *fully taxable in the
    year of inheritance* — the entire balance hits the non-spouse-
    heir's income for the year of death (offset only by qualified-
    medical-expenses-of-decedent paid within 1 year). For users
    with large HSA balances ($300k+) and intent-to-bequeath to
    non-spouse, this is a significant inheritance-tax-event the
    framing's "tax-free retirement vehicle" never names. Consider
    during-life-spend-down or during-life-Roth-conversion-
    equivalent moves on large HSA. Boundary `family-planning` D10.
  - The retirement-vehicle framing assumes the asker reaches
    retirement having accumulated medical expenses to reimburse
    against; for an asker with major medical events in their 30s
    and 40s, the optimal play may be reimburse-as-you-go rather
    than shoebox — the tax-free withdrawal is identical, the
    compounding lost is real, and the framing's bias toward
    deferral can be myopic for asker-specific health trajectories.

## 4. Tax-arbitrage / Form-mechanic framing

- **Decisions it applies to**: D1 (which contribution vehicle on
  the FICA / income-tax / above-the-line dimensions), D2 (Form 8606
  basis tracking, Form W-4 withholding tuning), D6 (tax-loss
  harvesting and wash-sale Form 8949), D7 (Roth conversion Form
  1099-R, Form 5498), D9 (Form 1099-Q on 529 distributions, Form
  8863 education-credit coordination).
- **Mental model summary**: Personal-finance decisions interact
  with the tax code via specific *forms, codes, and mechanics*
  that determine the after-tax outcome at a granularity the
  marginal-rate framing skips. Pre-tax contributions (401(k),
  HSA-payroll) reduce W-2 Box 1 but not Box 3 (FICA wages);
  HSA-after-tax-1040-deduction (Form 8889 Part 1) saves federal-
  and-state income tax but NOT FICA; backdoor Roth requires Form
  8606 Part I (basis tracking) AND Part II (conversion reporting);
  Mega-Backdoor Roth uses Form 1099-R with specific distribution
  codes (G for direct rollover, H for in-plan-conversion); tax-loss
  harvesting reports on Form 8949 with specific wash-sale-
  disallowance codes (W for wash-sale-disallowed amount); 529
  distributions report on Form 1099-Q with coordination required
  against Form 8863 American-Opportunity / Lifetime-Learning
  credits (cannot double-dip on same dollars per IRS Pub 970);
  Roth-conversion reports on Form 1099-R with distribution code 2
  (early-distribution-exception) or 7 (normal) plus Form 5498
  contribution-side. The framing reasons in *which-form, which-box,
  which-code* terms. Characteristic move: before answering any
  contribution-or-conversion question, build the cross-form view
  (8889, 8606, 8949, 8962, 1099-R, 5498, 1099-Q, 8863) and verify
  the asker's facts produce the expected form sequence.
- **Characteristic vocabulary**: "Form 8606 basis tracking",
  "Form 8889 HSA", "Form 8949 wash-sale code W", "Form 1099-R
  distribution code", "Form 5498 contribution-side", "Form 1099-Q
  529 distribution", "Form 8863 education credit coordination",
  "above-the-line deduction", "below-the-line deduction",
  "W-2 Box 1 vs Box 3 vs Box 5", "Section 125 cafeteria plan
  pre-FICA", "Form W-4 withholding adjustment", "Form 1040
  Schedule 1 / Schedule 2", "estimated-tax safe harbor."
- **Excludes**:
  - The Form-mechanic discipline assumes the asker can *project
    annual income* and *correctly file forms*; in practice many
    tax preparers (including paid franchise preparers — H&R Block,
    Jackson Hewitt) get backdoor-Roth Form 8606 wrong, treating
    the nondeductible IRA contribution as missing entirely (so the
    conversion is taxed at full ordinary rates with no basis
    offset). The framing's "fill the form correctly" understates
    the practitioner-error rate, and the asker often discovers
    the mistake via an IRS CP2000 notice 18 months later. Opposes
    F10 (CPA-as-validator) when the CPA is the wrong type. The
    Finance Buff voice catches this consistently.
  - The framing engages with *tax-code-as-static* but the tax-code
    is *politically dynamic* — TCJA 2017 brackets sunset 2026,
    SECURE Act 2.0 phased many provisions across 2024-2026,
    ARPA/IRA enhanced ACA subsidies sunset 2025 absent extension,
    Roth-conversion-recharacterization was eliminated 2018, and
    the Roth-401(k)-employer-match-allowed mechanic was added
    2024 but is plan-document-gated. The framing's "look up the
    current Form X" is correct only for the current cycle; asker
    questions reaching back to 2017 / 2018 cycle have *different*
    rules applying. Boundary `legal-disputes`.
  - Form-mechanic mastery is unequally distributed across the
    professional-advice market — fee-only fiduciary CFPs vary
    sharply in tax-mechanic depth (many will outsource to a CPA
    rather than calculate themselves), and CPAs vary sharply in
    retirement-and-equity-comp experience (a CPA who's done 50
    business-returns this year but 0 backdoor-Roth-Forms-8606 is
    *not* the right validator for the conversion-planning question
    despite the credential). The framing's "consult your CPA"
    reflex needs CPA-specialty-filter that the broad framing
    rarely names. See `decisions.md` §Notes selective-referral.
  - The 5-year-Roth-conversion-clock and 5-year-Roth-IRA-aging-
    clock are *two distinct clocks* that the asker must track
    separately for each conversion AND for the Roth-IRA-itself —
    the longer of the two applies for penalty-free withdrawal of
    earnings, and many askers (and some advisors) treat them as
    one clock. The framing's form-discipline captures this if
    applied consistently; the marginal-rate framing alone misses
    it.

## 5. Risk-adjusted-allocation framing

- **Decisions it applies to**: D3 (asset location across account
  types), D4 (brokerage asset allocation and glide path), D6
  (tax-loss harvesting as side-effect of allocation), D5 (debt-
  payoff-vs-invest as an implicit allocation choice between
  guaranteed return and expected-with-variance return).
- **Mental model summary**: Portfolio construction is the *joint
  optimization of expected return and variance* across asset
  classes, with the household's *risk tolerance* (psychological
  capacity to hold through drawdown) and *risk capacity* (financial
  capacity given income, time-horizon, and liability profile)
  jointly setting the equity / bond / alternative mix. The framing
  reasons in Modern-Portfolio-Theory and historical-equity-risk-
  premium terms: 7% real expected equity return vs 1-2% real
  expected bond return, historical equity volatility 15-20% annual
  std-dev with 50%+ drawdowns 1-2 times per generation, bond
  correlation with stocks shifted positive in 2022 (the 60/40
  worst year since 1937), international diversification offers
  marginal but real benefit at non-trivial correlation cost.
  Implementation frames: (a) target-date-fund single-vehicle
  glide path (Vanguard, Fidelity, Schwab, TIAA — each with
  different equity-bond-international defaults); (b) 3-fund
  Bogleheads portfolio (US-total / international / US-bond,
  manually rebalanced); (c) DIY multi-fund with factor tilts
  (small-cap-value, international-small, momentum); (d) all-
  weather / risk-parity / leveraged-bond variants for the
  sophisticated. Characteristic move: identify the household's
  risk tolerance via stress-test ("could you hold through a
  -50% S&P year without selling?"), pick an allocation, and
  rebalance annually. Anchor: any allocation the asker cannot
  hold through drawdown is the wrong allocation regardless of
  theoretical optimum (the behavior-gap is real — DALBAR studies
  show 2-3% annual underperformance from investor mistiming).
- **Characteristic vocabulary**: "expected return vs variance",
  "Modern Portfolio Theory", "Sharpe ratio", "equity risk premium",
  "behavior gap", "DALBAR investor-return-vs-fund-return",
  "stay-the-course discipline", "rebalance back to target", "glide
  path", "age-in-bonds / 120-minus-age", "three-fund portfolio",
  "target-date fund", "factor tilt (small-cap-value, momentum,
  quality)", "Fama-French 3-factor / 5-factor", "asset-location",
  "home-bias / global-cap-weight."
- **Excludes**:
  - The framing's risk-tolerance / risk-capacity distinction is
    *self-reported* — many askers genuinely don't know their
    drawdown tolerance until they've lived through one, and the
    2020 March COVID drawdown was *too brief* to genuinely test
    most askers' resolve. The "stress test" framing is the right
    discipline but the answers are unreliable; the framing rarely
    surfaces this calibration gap. Opposes F11 (behavioral-
    finance) at the meta-level.
  - The framing under-weights *concentrated-single-stock risk*
    that dominates many tech-employee households — a $400k vested
    RSU + $80k ESPP position in current employer is a $480k
    single-stock bet that overwhelms any chosen target allocation.
    The generic "diversify" advice obscures the more specific
    framing — sell-on-vest is tax-neutral for RSU because vesting
    is already a taxable event at ordinary rates; for ESPP the
    disqualifying-disposition vs qualifying-disposition math
    complicates the immediate-sell call. Boundary `tech-career` D4.
  - Bond-allocation discipline assumes the bond market is the
    *diversifier-against-equity* it was for most of 1980-2020 —
    but rate-environment shifts can break that correlation
    (2022's negative-correlation-positive-shock was the worst
    60/40 year since 1937). The framing's classical-allocation
    rule needs regime-awareness. Alternatives (gold, REITs, TIPS,
    international, alternatives) shift the conversation but each
    has its own correlation behavior and tax-treatment quirks.
  - International-allocation home-bias debate is genuinely
    unresolved — recommended ranges span 0% (Buffett, Bogle) to
    40%+ (Vanguard target-date defaults) with little empirical
    convergence; the framing rarely surfaces that the choice is
    a judgment call rather than a calculation, and dogmatism in
    either direction (the "VTI-only" or "VT-global-only" camps)
    masks the actual uncertainty.

## 6. Behavioral-debt-payoff framing

- **Decisions it applies to**: D5 (debt-payoff vs invest — the
  central decision domain), D1 (priority-order step-2 on high-
  interest debt and step-9 on low-interest debt), and as a
  meta-framing on D2 / D4 wherever the technical-optimal sacrifices
  behavioral-sustainability.
- **Mental model summary**: For households with multiple debts at
  various rates, the *math-optimal* approach (Dave Ramsey-style
  avalanche: highest-rate first to minimize interest paid) often
  loses to the *behavioral-optimal* approach (Ramsey-style
  snowball: smallest-balance first for the win-momentum effect).
  Empirical research (Gal & McShane 2012, *Journal of Marketing
  Research*; multiple follow-ups) shows snowball-completed
  payoff plans are completed at *higher rates* than avalanche
  plans for households at-risk-of-giving-up — the suboptimal
  math is dominated by completed payoff. The framing reasons in
  *delivered-result* rather than *theoretical-optimum* terms,
  and engages seriously with the psychology of sustained
  financial discipline: automate savings to remove decision
  fatigue (pay-yourself-first via direct payroll deduction);
  use the snowball when the asker has 4+ debts and history of
  giving up on multi-year plans; use the avalanche when the
  asker is mathematically-disciplined and has stable income;
  use the *cash-flow-priority* (smallest minimum-payment first
  to free monthly cash for emergency fund) when the household
  is fragile. Characteristic move: ask the asker *which debts
  they would actually pay off* before recommending a strategy;
  optimize for sustainability over mathematical purity. Anchor:
  401(k) match capture beats every debt-paydown except payday-
  loan-class debt at 200%+ APR (per F1's priority order).
- **Characteristic vocabulary**: "snowball method", "avalanche
  method", "debt-payment plan", "win-momentum effect",
  "decision fatigue", "pay yourself first", "automate the
  savings", "behavioral discipline", "emergency fund first",
  "cash-flow priority", "behavior-gap (in debt-payoff context)",
  "Dave Ramsey 7 Baby Steps", "Suze-Orman emergency-fund
  doctrine", "behavioral economics in personal finance."
- **Excludes**:
  - The framing's "snowball wins for at-risk-of-giving-up askers"
    is correct on average but can be paternalistic when applied
    to the high-financial-literacy asker who genuinely is
    avalanche-disciplined — the math-optimal asker who is
    pushed into snowball-by-default loses real money over the
    multi-year payoff window. The framing rarely surfaces the
    asker-classification step before applying the conclusion.
    Opposes F2 (marginal-rate / pure-arithmetic) on the
    technical-correctness axis.
  - Student-loan PAYE / SAVE / IDR forgiveness *fundamentally
    breaks* the debt-payoff-vs-invest framing — on PSLF-track
    the "after-tax-effective debt rate" is near-zero because
    the balance will be forgiven, and accelerating payment
    destroys the forgiveness value. The framing's "pay highest-
    rate first" reflex catastrophically mis-routes the PSLF-
    eligible asker into refinancing-to-private and losing
    forgiveness. Boundary `education-funding`.
  - Mortgage-payoff-vs-invest is a *special case* with three
    competing valid reasons to pay off (sequence-of-returns
    risk reduction, cash-flow reduction in retirement, emotional
    security) versus three competing valid reasons to invest
    (after-tax-arbitrage when mortgage rate < expected-
    investment-return, tax-deductibility for itemizers,
    liquidity preservation). The framing's binary "pay debt or
    invest" misses the configuration where *both* are right
    answers depending on the asker's specific life-stage and
    risk-profile. Boundary `housing`.
  - The "behavioral discipline" framing under-engages with the
    *cash-flow vs balance-sheet* distinction — an asker drowning
    in $15k credit-card debt but with $40k in a Roth IRA could
    technically withdraw Roth principal penalty-free to clear
    the debt (the math-optimal move in extreme cases), but
    behavioral-debt framings reflexively oppose "raiding
    retirement" without engaging with the asymmetry between
    high-interest-revolving-debt and tax-advantaged-savings.
    The right answer is context-dependent; the framing's reflex
    is overly conservative.

## 7. Time-horizon-and-lifecycle framing

- **Decisions it applies to**: D4 (asset allocation glide path —
  the lifecycle is the structural argument), D8 (retirement
  withdrawal sequencing — late-lifecycle), D9 (529 funding
  pace — child-lifecycle), D10 (estate-and-beneficiary structuring
  — terminal-lifecycle), D1 (priority order interacts with
  lifecycle via age-50 catch-up and age-60-63 super-catch-up).
- **Mental model summary**: Financial planning is *fundamentally
  lifecycle* — the optimal contribution / allocation / withdrawal
  decision depends critically on the asker's age, expected
  earnings trajectory, family-formation stage, and time-to-
  retirement. The framing draws on lifecycle-finance academic
  literature (Larry Kotlikoff's economic-spending-vs-saving
  framework; Wade Pfau's bond-tent and rising-equity-glide
  research; Michael Kitces's withdrawal-sequencing analysis;
  Modigliani-Brumberg lifecycle-savings hypothesis) to argue
  that *consumption-smoothing across the lifecycle* is the
  proper objective, not portfolio-value-maximization at any
  single point. Implementation moves: young accumulator (age
  22-35) takes maximum equity risk to capture the long horizon
  and human-capital-as-bond-substitute; mid-career (35-55)
  rebalances toward target allocation while peak earnings
  cover catch-up contributions; late-career (55-65) executes
  the Roth-conversion-ladder in low-income years and stages
  the asset-location for withdrawal-sequence efficiency;
  decumulation (65+) executes the bond-tent or rising-equity-
  glide against sequence-of-returns risk and coordinates Social
  Security claim age with spousal-survivor math. Characteristic
  move: name the asker's lifecycle stage explicitly, identify
  the lifecycle-specific decisions (529 funding for under-40-
  with-young-kids, Roth-conversion for 55-65 sabbatical-or-
  retirement-bridge, RMD-management for 73+), and route around
  framings that aren't lifecycle-anchored.
- **Characteristic vocabulary**: "lifecycle finance",
  "consumption-smoothing", "human capital as bond substitute",
  "accumulation phase", "decumulation phase", "bond tent",
  "rising-equity-glide", "sequence-of-returns risk", "safe
  withdrawal rate (4% Bengen / variable Kitces)", "Modigliani-
  Brumberg lifecycle savings", "age-50 catch-up", "age-60-63
  super-catch-up (SECURE 2.0 §603)", "retirement-bridge",
  "longevity risk", "retirement-glide-path", "actuarial-life-
  expectancy-vs-personal-longevity-assumption."
- **Excludes**:
  - The framing's "young = equity-heavy" reflex assumes the
    asker's human capital is bond-like (stable employment,
    rising wages, predictable career arc) — but for equity-
    comp-heavy tech employees, contract / gig workers, and
    self-employed askers, human capital is itself *equity-
    like* (volatile, market-correlated, downside-correlated
    with broader equity markets in a recession). The framing's
    aggressive-young-equity reflex over-concentrates equity
    risk when human capital is equity-like. Boundary
    `tech-career`.
  - Bond-tent and rising-equity-glide are *counterintuitive*
    (most retirees do the opposite — they shift more
    conservative across retirement to "preserve principal"),
    and the framing rarely engages with the practical-
    implementation barriers (employer-target-date-fund glide
    paths run conservative; advisors face liability incentive
    to shift conservative; the asker's own anxiety in down
    markets pushes conservative). The academic literature
    supports rising-equity-glide; the institutional and
    psychological environment fights it. The framing's
    technical correctness understates the implementation
    barrier.
  - The "safe withdrawal rate" framing (Bengen 4% rule,
    Kitces variable, Pfau retirement-glide-rules) is calibrated
    to *historical* US market returns over rolling 30-year
    periods, and the framing rarely surfaces that international
    historical returns include multi-decade flat markets
    (Japan 1989-present, France 1960-1995) where 4% would have
    failed. The "safe withdrawal rate" terminology implies a
    certainty the historical data doesn't deliver. Boundary
    `legal-disputes` on cross-border retirement.
  - The lifecycle framing assumes a *linear* career arc;
    sabbaticals, job-loss, layoff, caregiver-leave-from-
    workforce, and second-career-pivot break the assumed
    glide-path-of-earnings, and the framing rarely engages
    with how to *reset* the glide-path mid-life when the
    trajectory shifts. The Mr-Money-Mustache / FIRE community
    voice catches this (early-retirement-as-default-option);
    the traditional lifecycle voice doesn't.

## 8. Asset-protection-and-creditor-shield framing

- **Decisions it applies to**: D10 (estate-and-beneficiary
  structuring — creditor-protection-of-retirement-accounts is
  the central axis), D1 (priority order interacts via 401(k)-
  vs-IRA-after-rollover creditor-shield comparison), D4
  (taxable-account assets exposed to lawsuits in ways
  retirement-account assets aren't), and as a meta-framing on
  any decision touching divorce, business-formation, or high-
  liability-profession (physician, attorney, real-estate-developer).
- **Mental model summary**: Different account types and asset
  classes have *materially different creditor-protection*
  under federal bankruptcy law and state shield statutes,
  and the framing makes these distinctions load-bearing for
  high-net-worth and high-liability-exposure askers.
  ERISA-protected 401(k) is *unlimited* federal-bankruptcy-
  exempt (per 11 USC §522(b)(3)(C)) and generally judgment-
  proof against most state-law claims (per *Patterson v
  Shumate* 504 US 753 (1992)); rollover-IRA is federal-
  bankruptcy-exempt only to $1,512,350 indexed (per 11 USC
  §522(n) as of 2022, indexed every 3 years) and state-
  protection varies sharply — Texas / Florida / Arizona
  unlimited, California only "necessary for support" and
  only in bankruptcy, NY $1M, NJ $1M, IL $1M. Roth-IRA has
  the same federal-bankruptcy cap as traditional-IRA;
  contributory-IRA (not rollover) shares the cap (different
  state treatment in some states). HSA is *not* a federally-
  exempt account, has narrow state protection (Texas
  specifically protects HSA; most states don't). The framing
  reasons in *which-state, which-account-type, which-claim-
  type* terms: for HNW askers with litigation exposure or
  professional-liability risk, the rollover-from-401(k)-to-
  IRA on retirement *weakens* creditor protection; staying
  in the 401(k) plan (if plan permits indefinite-balance) is
  often the right move. For business-owners, asset-isolation
  across LLC / S-corp / professional-corporation structures
  layers with retirement-account-protection. Characteristic
  move: before recommending any rollover or asset-titling
  change, identify the asker's state-of-residence, marital
  status, professional-liability profile, and existing
  litigation risk. Anchor: *Egelhoff v Egelhoff* 532 US 141
  (2001) — ERISA-plan beneficiary form controls over state
  property law including divorce-revocation statutes; this
  is the load-bearing precedent for beneficiary-form-audit
  on every life event.
- **Characteristic vocabulary**: "ERISA pre-emption", "11
  USC §522(b)(3)(C) ERISA exempt", "11 USC §522(n) IRA cap
  $1,512,350 indexed", "*Patterson v Shumate*", "*Egelhoff
  v Egelhoff*", "state-shield variation", "Texas / Florida
  unlimited IRA protection", "California 'necessary for
  support' standard", "QDRO division on divorce",
  "fraudulent-conveyance look-back", "homestead exemption",
  "TBE (tenancy-by-the-entirety)", "professional-liability
  insurance interaction", "umbrella policy coordination",
  "asset titling".
- **Excludes**:
  - The framing's "stay in 401(k) for unlimited shield"
    reflex misses that 401(k) plans charge plan-administration
    fees that can compound to material drag over decades; the
    creditor-protection benefit is real but priced — for
    HNW-but-low-litigation-risk askers, the rollover-to-low-
    cost-IRA is genuinely the right move and the framing's
    blanket "don't roll over" overstates the protection
    benefit. Asker-specific litigation-risk-assessment is the
    missing step.
  - State-shield law is *non-uniform and shifts* — California
    AB-3088 / state-shield amendments, Florida's recent
    homestead-exemption expansions, Texas-specific HSA-
    protection statutes — the framing's "lookup-table"
    discipline needs date-of-application currency that
    generic advice doesn't deliver. The framing rarely
    surfaces "verify the current statute" as the load-bearing
    step before relying on a 5-year-old summary.
  - Inherited-IRA was held in *Clark v Rameker* 573 US 122
    (2014) to NOT be federal-bankruptcy-exempt — the
    Supreme Court ruled that an inherited IRA does not
    qualify as "retirement funds" under 11 USC §522(b)(3)(C)
    because the non-spouse-beneficiary cannot contribute to
    it and is required to take distributions. The framing's
    "IRA is bankruptcy-exempt" reflex catastrophically
    misroutes the asker who inherited an IRA and faces a
    bankruptcy event — the inherited IRA is exposed to
    creditors. Some state-laws specifically protect inherited
    IRAs (Texas, Florida, Arizona, Idaho, Missouri, North
    Carolina, Ohio); most don't. Boundary `family-planning` D10.
  - The framing's asset-protection focus can mask *over-
    isolation* risk — askers who layer LLC / trust / off-shore
    structures to maximize protection often face material
    administrative costs, complexity, and IRS-audit-attention
    that exceed the protection benefit. Boundary
    `entrepreneurship` / `legal-disputes`.

## 9. Estate-and-intergenerational framing

- **Decisions it applies to**: D10 (estate-and-beneficiary
  structuring — central), D8 (withdrawal sequencing — interacts
  with basis-step-up-at-death intent), D3 (asset location —
  step-up-eligible-taxable preference for intent-to-bequeath
  households), D9 (529 funding — grandparent-funded vs parent-
  funded FAFSA treatment under post-2024 Simplification Act).
- **Mental model summary**: For households with *intent-to-
  bequeath* (regardless of estate-tax exposure), the optimal
  withdrawal-sequence, asset-location, and account-type-
  selection differ materially from the optimal-for-pure-self-
  consumption answers the lifecycle framing produces. The
  central asymmetry is the *basis-step-up-at-death* (IRC
  §1014): taxable appreciated assets get FMV-basis-reset at
  owner's death — heirs sell at $0 capital gain immediately —
  while traditional IRA / 401(k) get NO step-up and are taxed
  as ordinary-income on distribution by the heir. This
  asymmetry argues for *running down traditional-401(k)-and-
  IRA during life* (via Roth-conversion ladder, RMD beyond
  the minimum, or strategic Roth-401(k) contributions in
  working years) and *holding appreciated taxable for heirs*
  — the inverse of the conventional "taxable first" withdrawal
  sequence in F5 / lifecycle framing. Layer on the SECURE 1.0
  10-year-rule on inherited non-spouse IRAs (eliminates the
  prior stretch-IRA strategy) and the 2025-doubled-estate-
  tax-exemption-sunset ($13.99M-per-individual in 2025
  reverting to ~$7M-indexed in 2026 absent congressional
  extension; IRS Reg §20.2010-1(c) anti-clawback rule confirms
  pre-2026 gifts are permanent), and the framing produces
  meaningfully different recommendations than the lifecycle
  framing on D8 / D10. Characteristic move: ask the asker
  about *intent-to-bequeath* explicitly; if material, invert
  the withdrawal sequence (Roth-convert traditional to give
  heirs Roth not traditional; hold appreciated taxable for
  step-up; consider 2025-sunset-pre-2026-gifting moves like
  SLAT or lifetime-gift-up-to-current-exemption); audit
  beneficiary forms quarterly for life-events. Anchor:
  Beneficiary forms supersede the will per Egelhoff doctrine;
  this is the highest-leverage zero-cost preventive move
  available in the entire domain.
- **Characteristic vocabulary**: "basis-step-up-at-death",
  "IRC §1014", "SECURE 1.0 10-year-rule on inherited IRA",
  "eligible-designated-beneficiary (EDB)", "stretch IRA
  (eliminated for non-EDB)", "2025-doubled-estate-tax-
  exemption sunset", "anti-clawback Reg §20.2010-1(c)",
  "SLAT (Spousal Lifetime Access Trust)", "GRAT (Grantor
  Retained Annuity Trust)", "ILIT (Irrevocable Life
  Insurance Trust)", "CRT (Charitable Remainder Trust)",
  "CLT (Charitable Lead Trust)", "Dynasty trust", "generation-
  skipping transfer (GST) tax", "lifetime gift exemption",
  "annual gift exclusion $19k (2025)", "TOD / POD designations",
  "Egelhoff doctrine", "see-through trust as IRA beneficiary."
- **Excludes**:
  - The intent-to-bequeath framing routes toward *holding-
    appreciated-taxable-for-step-up* — but this directly
    conflicts with the lifecycle / safe-withdrawal-rate
    framing's "taxable first" sequence, and many advisors and
    asker-self-models default to lifecycle without engaging
    with the bequest-intent override. The framing's
    asymmetry-recognition is correct but commonly missed.
    Opposes F7 directly on D8.
  - The SECURE 1.0 10-year-rule for non-spouse-non-EDB
    beneficiaries is *frequently misunderstood* — under final
    SECURE regulations (Feb 2024), if the decedent had
    already started RMDs (post-Required-Beginning-Date),
    the non-EDB heir must also take annual RMDs during years
    1-9 AND empty the account by end-of-year-10; if the
    decedent died before their RBD, the heir can lump-or-
    stagger across the 10 years with no annual RMD. The
    framing's "10-year-rule means take it whenever in 10
    years" is materially incomplete. Boundary `legal-disputes`
    on inheritance-procedural-disputes.
  - The 2025-sunset planning urgency is *time-bound and
    politically uncertain* — Congress could extend the doubled
    exemption (multiple bills have been proposed; none have
    passed as of writing); advising aggressive pre-2026
    gifting for households with $5-15M net worth carries real
    risk of "spent the exemption you didn't need to" if
    extension passes. The framing's "use-it-or-lose-it"
    urgency overstates certainty about the sunset. Boundary
    `legal-disputes`.
  - Beneficiary-form-audit reflex is *correct and necessary*
    but the framing under-engages with the *practical
    barriers*: many custodians require paper forms returned
    by mail, beneficiary-form-changes on workplace 401(k)
    plans may require employer-HR coordination, and form-
    updates after marriage / divorce / birth / death often
    fall through the cracks of life-event-management. The
    framing's "audit annually" is the right discipline; the
    operational reality is more friction than the framing
    names.

## 10. Professional-referral-and-conflict-of-interest framing

- **Decisions it applies to**: as a meta-framing on all
  decisions — applies most directly to D3, D4 (where individual-
  portfolio recommendations are needed and AUM-vs-commission
  conflict is most acute), D7, D8 (Roth-conversion sizing
  and Social-Security claim-age where specialist software
  meaningfully outperforms generalist), D10 (estate-planning
  where state-bar attorney drafting is uniquely required).
- **Mental model summary**: The professional-advice market
  for personal-finance contains *structural conflicts of
  interest* that bias recommendations away from the asker's
  optimal answer in predictable directions, and the framing
  makes the conflict-mapping load-bearing for any referral
  decision. AUM-fee advisors (charging ~1% of assets-under-
  management annually) have structural incentive to recommend
  rollover-from-401(k)-to-IRA (grows AUM), to discourage
  passive-low-cost-index strategies (no rationale for
  ongoing fee), to recommend annuity-conversion of part of
  the portfolio (commission-side), and to delay distribution-
  to-heirs (extends AUM duration). Commission-based brokers
  (registered-rep under FINRA Series 7) face the suitability-
  standard not the fiduciary-standard and can recommend higher-
  commission products even when lower-cost alternatives strictly
  dominate. "Fee-based" advisors (the deliberately-confusing
  hybrid term) are not fee-only — they take both AUM-fee AND
  commissions, with the worst of both incentive structures.
  *Fee-only* advisors (NAPFA-registered, XY-Planning-Network,
  Garrett-Planning-Network — verify membership at the
  organization's website) take no commissions and have
  materially-better-aligned incentives, though AUM-fee fee-
  only-CFPs still face rollover-recommendation bias.
  Hourly-or-flat-fee fee-only planners (Garrett) eliminate
  the rollover bias. The framing reasons in *fee-structure-
  drives-recommendation* terms. Characteristic move: before
  accepting any individual-advice recommendation, verify the
  advisor's fee structure (Form ADV Part 2A from SEC IAPD or
  state regulator), cross-check at FINRA BrokerCheck for
  disclosure events, and ask the advisor *explicitly* "what
  is your fiduciary standard and on what scope of
  recommendations." Anchor: SEC Reg-BI ("Regulation Best
  Interest") for broker-dealers, ERISA-fiduciary-standard
  for retirement-plan advisors per DOL final rule (2024),
  IAA-Section-206 fiduciary standard for SEC-registered IAs.
- **Characteristic vocabulary**: "fee-only vs fee-based vs
  commission", "AUM fee", "Form ADV Part 2A", "FINRA
  BrokerCheck", "SEC IAPD (Investment Adviser Public
  Disclosure)", "fiduciary vs suitability standard",
  "Reg-BI", "DOL fiduciary rule", "structural conflict of
  interest", "rollover-recommendation bias", "annuity-
  conversion commission", "12b-1 fee", "trail commission",
  "load fund vs no-load", "wrap account", "NAPFA / XY-
  Planning / Garrett-Planning fee-only registry."
- **Excludes**:
  - The framing's "fee-only is the gold-standard" reflex is
    *broadly correct* but masks within-fee-only variation —
    AUM-fee fee-only-CFPs still face rollover-recommendation
    bias (the same incentive that drives commission-broker
    rollover recommendations applies once the AUM is captured),
    and the framing rarely distinguishes AUM-fee-fee-only
    from hourly-or-flat-fee-fee-only. Garrett-Planning-Network
    is the sub-category for one-time-question or bounded-scope
    asker; the framing collapses these distinctions when
    over-applied.
  - Fee-only-CFP coverage is *uneven across decision categories*
    — most CFPs are generalist and lack specialized depth in
    backdoor-Roth Form 8606, Mega-Backdoor Roth plan-document
    analysis, Roth-conversion sizing relative to IRMAA / NIIT /
    ACA cliffs, QSBS Section-1202 analysis, or ERISA-plan-
    document interpretation. The framing's "consult a fee-only
    CFP" reflex needs CPA / ERISA-attorney / tax-attorney
    over-ride for technical specialty questions. See
    `decisions.md` §Notes selective-referral matrix.
  - The framing under-engages with *DIY-via-Bogleheads-Reddit-
    flowchart* as a legitimate alternative for askers with
    moderate complexity and high financial literacy — the
    "always consult a professional" reflex can be paternalistic
    and crowds out the asker who is genuinely better-served
    by self-study + occasional hourly-fee consult than by
    ongoing AUM-fee relationship. Boundary opposite to F11
    (behavioral-finance) which leans toward "automate everything
    and outsource discipline."
  - The framing's professional-referral discipline assumes
    *trustworthy-professional-availability* — but rural areas,
    immigrant communities (language barriers), and historically-
    marginalized communities face genuine access barriers to
    fiduciary-fee-only advisors. The XY-Planning-Network and
    Garrett-Planning-Network address this somewhat by virtual-
    practice models, but the framing rarely surfaces access-
    inequality as a real constraint on the "just consult a
    fee-only CFP" recommendation.

## 11. Behavioral-and-automation framing

- **Decisions it applies to**: all decisions as a meta-framing,
  with strongest direct application to D1 (priority order
  execution), D4 (asset allocation discipline through
  drawdown), D5 (debt-payoff plan completion), D6 (TLH
  discipline year-after-year), D8 (withdrawal-sequencing
  discipline against anxiety-driven cash-hoarding).
- **Mental model summary**: The *gap between knowing and
  doing* is the single largest destroyer of long-term
  personal-finance outcomes — DALBAR studies consistently
  show 2-3% annual gap between fund returns and investor
  returns from mistiming (sell-low-buy-high), and FINRA
  Foundation surveys consistently show <40% of US adults
  can answer 5 basic financial-literacy questions
  correctly. Behavioral-finance framing argues that
  *automating* the right decisions removes the decision-
  fatigue and behavioral-failure points — automated payroll
  deduction to retirement accounts, automated paycheck-
  to-Roth-IRA transfer, automated robo-advisor rebalancing,
  automated bill-pay, automated emergency-fund top-up,
  automated tax-loss-harvesting via robo. The framing
  reasons in *defaults, friction, and habit-formation*
  terms (drawing on Thaler & Sunstein's *Nudge*, Daniel
  Kahneman's *Thinking Fast and Slow*, BJ Fogg's
  *Tiny Habits*): default-enrolled 401(k) plans with
  auto-escalation produce dramatically higher
  participation rates than opt-in; emergency-fund target
  reached more reliably via auto-transfer than via
  manual-monthly-discipline; tax-loss-harvesting executed
  via robo more consistently than via human-attention-
  during-busy-life. Characteristic move: when the asker
  asks "should I do X," the framing reframes to "can I
  automate X so I don't have to remember." Anchor: the
  *behavior gap* and the *intention-action gap* in
  financial behavior.
- **Characteristic vocabulary**: "behavior gap", "intention-
  action gap", "default option", "auto-enroll, auto-escalate",
  "decision fatigue", "automate the savings",
  "pay-yourself-first via payroll deduction", "robo-advisor
  automatic TLH", "Wealthfront / Betterment / M1 / Schwab
  Intelligent Portfolios", "Thaler nudge architecture",
  "Kahneman System 1 vs System 2", "BJ Fogg tiny habits",
  "anchoring on the current paycheck", "set-and-forget",
  "remove the friction."
- **Excludes**:
  - Automation works *until it breaks* — a robo-advisor
    auto-TLH that doesn't have visibility into the asker's
    held-away accounts (spouse's IRA, employer 401(k))
    creates wash-sale violations the asker doesn't see
    until tax-time Form 1099-B-W-code surfaces them; an
    auto-escalate 401(k) that hits the elective-deferral
    cap mid-year stops contributing (and stops capturing
    match) for the rest of the year if employer doesn't
    true-up. The framing's "set-and-forget" elides the
    auto-system-failure modes. Boundary F4 (tax-mechanics).
  - The "automate everything" reflex can mask *fee leakage*
    — automatic-enrollment-default-fund is often the
    employer's target-date-fund with 0.5-1.0% expense ratio
    when a 3-fund-portfolio with 0.05% expense ratio is
    available; the auto-enrolled asker stays in the
    expensive default for years. The framing's automation
    discipline is the right starting point; periodic-
    audit-and-rebalance-toward-low-cost is the necessary
    complement.
  - Automation discipline is *anti-correlated with optionality*
    — the asker who automates everything also forfeits the
    ability to capture tactical opportunities (Roth-conversion
    in a layoff year, tax-loss-harvest in a market-drawdown,
    529-funding bump in a windfall year). The framing's
    "remove the friction" reflex can over-apply to decisions
    that benefit from human attention. Opposes F2 / F7
    where tactical timing matters.
  - The behavioral-finance framing assumes the asker has
    *agency over the relevant defaults* — but many askers
    work for employers whose 401(k) plan-document doesn't
    offer auto-escalation, doesn't allow after-tax
    contributions, doesn't permit Roth-401(k), or doesn't
    enable in-plan-Roth-conversion. The framing's "use the
    automation" recommendation depends on plan-features the
    asker may not control. Boundary `tech-career` on
    employer-plan-document analysis.

## 12. Policy-volatility / system-skepticism framing

- **Decisions it applies to**: as a meta-framing on all
  decisions, with strongest application to D2 / D7
  (Roth-vs-traditional and Roth-conversion-ladder where
  TCJA-bracket-sunset matters), D8 (Social-Security
  claim-age where SS-trust-fund-exhaustion-2034 matters),
  D9 (529 mechanics where TCJA changes and SECURE 2.0
  529-to-Roth rollover changed the calculus), D10 (estate-
  tax exemption sunset).
- **Mental model summary**: Personal-finance decisions
  are made within a *politically-determined tax-and-benefit
  framework* that changes meaningfully every 5-10 years,
  and the framing makes this volatility load-bearing for
  any long-horizon decision. Recent major shifts include:
  TCJA 2017 doubled-bracket-widening with 2026 sunset
  (12% → 15%, 22% → 25%, 24% → 28%); SECURE Act 1.0 (2019)
  raising RMD age and eliminating stretch-IRA; SECURE 2.0
  (2022) raising RMD again, adding 529-to-Roth rollover,
  mandating Roth-catch-up for high-earners, expanding HSA
  / FSA mechanics, adding emergency-savings-Roth-401(k);
  ARPA / IRA enhanced ACA subsidies 2021-2025 (sunset
  end-2025 absent extension); Inflation Reduction Act
  Medicare Part D $2,000 OOP-cap (effective 2025);
  FAFSA Simplification Act eliminating grandparent-529
  trap (effective 2024-25 academic year); 2025-sunset
  of doubled estate-tax-exemption to ~$7M-indexed.
  Social-Security trust-fund-exhaustion is projected
  2034 (per 2024 SSA Trustees Report) with 21% benefit
  cut absent legislative action. The framing reasons in
  *political-risk-as-tax-risk* terms: hedge against rate
  rises via Roth allocation, hedge against benefit cuts
  via diversified-retirement-income, hedge against
  exemption-reversion via pre-sunset gifting moves.
  Characteristic move: when an asker asks "what's optimal
  for the next 30 years," the framing surfaces "optimal
  under the *current* regime may be wrong under the
  *expected* regime, and the cost of hedging policy-risk
  is itself a real cost." Anchor: SSA Trustees Report,
  CBO Long-Term Budget Outlook, IRS revenue rulings,
  Tax Foundation policy tracking.
- **Characteristic vocabulary**: "TCJA sunset 2026",
  "SECURE Act 1.0 / 2.0", "ARPA / IRA enhanced ACA
  subsidies sunset", "Inflation Reduction Act Part D
  $2,000 cap", "FAFSA Simplification Act", "doubled-
  exemption sunset 2026", "anti-clawback Reg §20.2010-1(c)",
  "Social-Security trust-fund exhaustion 2034", "21%
  benefit cut absent legislative action", "policy risk
  as tax risk", "Roth hedge against rate rises",
  "tax-diversification as optionality", "regime-change
  in tax code", "legislative-cliff planning."
- **Excludes**:
  - The framing's policy-volatility argument can produce
    *over-hedging* that costs real money — the asker who
    refuses traditional-401(k) contributions because
    "rates might go up" loses the certain current-year
    deduction at high marginal rates, and the projected
    rate-rise may not materialize. The framing's
    asymmetry-toward-Roth reflex needs hardness about
    actual current marginal vs projected rates. Opposes
    F2 (marginal-rate arbitrage) when over-applied.
  - Predictions about *which* policy changes will pass
    are systematically poor — many predicted changes
    (estate-tax-exemption-reversion, SS-benefit cuts,
    Medicare-IRMAA-tier widening) have been delayed
    multiple times by legislative inaction, and the
    framing's "act before the cliff" urgency repeatedly
    front-runs cliffs that don't materialize on schedule.
    Boundary `legal-disputes`.
  - The framing engages with *federal-policy volatility*
    but rarely with *state-policy volatility* — state
    income-tax rates, state-shield laws for retirement
    accounts, and state-529 mechanics shift independently
    of federal cycles, and the federal-focused framing
    under-engages with state-specific changes that may
    matter more to the asker's actual situation.
  - The framing's hedge-against-policy reflexes
    (diversify-into-Roth, gift-before-sunset, claim-SS-
    early-before-cuts) can themselves *create* the
    behavior the policy was designed to prevent — early-
    SS-claiming because of trust-fund-anxiety is
    structurally identical to a bank run. The framing
    rarely engages with the meta-irony that individual
    hedging against benefit cuts can accelerate the
    fiscal trajectory toward cuts.

## 13. FIRE / extreme-saver framing

- **Decisions it applies to**: D1 (priority order — FIRE asks
  *can I max all caps AND fund taxable for early-retirement-
  bridge*), D4 (asset allocation — FIRE-specific 4% rule
  application and bond-tent for early-retirement), D5 (debt-
  payoff prioritization — FIRE emphasizes debt-free as
  precondition), D7 (Roth-conversion-ladder is the FIRE-
  community's signature early-retirement-bridge mechanic),
  D8 (withdrawal sequencing — Roth-conversion-ladder feeds
  withdrawal-sequence-discipline).
- **Mental model summary**: The Financial Independence /
  Retire Early (FIRE) community argues that *savings rate*
  (savings ÷ after-tax income) is the structural variable
  that determines years-to-financial-independence, with a
  50% savings rate producing FI in ~17 years vs ~30+ years
  at the conventional 15% savings rate. The framing reasons
  in savings-rate-and-25x-annual-expenses terms (Bengen's
  4% safe withdrawal rule inverted: target = 25x annual
  retirement expenses), with sub-flavors: *Lean FIRE*
  (minimalist retirement spend $25-40k/yr), *Regular FIRE*
  ($40-80k/yr), *Fat FIRE* ($100k+/yr), *Coast FIRE* (save
  aggressively early, then coast on compounding without
  further contributions), *Barista FIRE* (part-time work
  for health-insurance through one's 50s). Roth-conversion-
  ladder is the canonical FIRE-bridge from early-retirement
  to age-59.5: convert traditional-401(k) to Roth-IRA in
  low-income retirement years, wait 5 years per conversion,
  withdraw converted principal penalty-free. Geographic
  arbitrage (HCOL-earning + LCOL-retiring) and tax-bracket
  arbitrage (sabbatical-year-Roth-conversion) are signature
  moves. Characteristic move: compute the asker's savings
  rate, identify the FIRE-flavor that matches their
  expense-target, build the Roth-conversion-ladder timing.
  Anchor: Trinity Study (1998), Bengen 4% rule (1994),
  Mr Money Mustache "The Shockingly Simple Math Behind
  Early Retirement" (2012), ChooseFI podcast canon.
- **Characteristic vocabulary**: "savings rate as years-
  to-FI", "25x annual expenses target", "4% safe
  withdrawal rate", "Trinity Study", "Lean FIRE / Regular
  FIRE / Fat FIRE / Coast FIRE / Barista FIRE", "Roth-
  conversion ladder as FIRE bridge", "5-year clock per
  conversion", "Rule of 55", "SEPP 72(t) substantially-
  equal-periodic-payments", "geographic arbitrage",
  "HCOL-earn / LCOL-retire", "ACA-subsidy-optimization
  in early retirement", "Mustachianism", "ChooseFI",
  "r/financialindependence flowchart."
- **Excludes**:
  - The FIRE framing's 4% safe-withdrawal-rate is calibrated
    to *historical US 30-year retirement* — for FIRE
    retirees facing 50+ year retirement (retire at 35, live
    to 85), the safe-withdrawal-rate drops materially (Wade
    Pfau's research suggests 3-3.5% for 50-year horizons).
    The framing's 4%-anchored rhetoric can dramatically
    overstate sustainability for early-retirees specifically.
    Opposes F7 (lifecycle / retirement-econ academic
    voice) on the sustainable-withdrawal calculation.
  - The Roth-conversion-ladder requires *5-year-gap of
    funding before the first conversion becomes accessible*
    — early-retirees must pre-fund this 5-year gap from
    taxable-brokerage or Roth-IRA-principal-contributions
    (which are always penalty-free withdrawable as basis).
    The framing's enthusiasm for the ladder can elide the
    bridge-funding requirement, leaving askers stranded
    in years 1-5 of retirement without accessible cash.
  - FIRE's *health-insurance-pre-65* problem is a binding
    constraint the savings-rate-focus framing under-engages
    — ACA-marketplace-subsidy-management requires MAGI
    discipline that conflicts with Roth-conversion-ladder
    execution (large Roth conversions push MAGI past
    subsidy-cliff and destroy APTC eligibility); Barista
    FIRE solves this via part-time-employer-coverage but
    the framing rarely names the trade-off. Boundary
    `health-insurance` D5, D7.
  - The FIRE community's *frugality dogma* can encode
    middle-class-American assumptions (geographic mobility,
    car-optional living, partner-supportive-of-extreme-
    savings, no-eldercare-obligation, no-dependent-with-
    special-needs) that don't generalize to many askers'
    actual life constraints. The framing's
    "anyone can do this" rhetoric understates the structural
    factors that make extreme savings genuinely impossible
    for many households. Boundary `family-planning`.

## 14. Equity-comp / concentration-risk framing

- **Decisions it applies to**: D1 (priority order — equity-
  comp creates lumpy cash flow that disrupts the smooth-
  contribution model), D2 (Roth-vs-traditional — high-RSU-
  vest years are the canonical year for Roth-conversion
  acceleration), D4 (asset allocation — RSU concentration
  swamps target allocation), D5 (debt-payoff with RSU as
  funding source — capital-gains-vs-ordinary-rate math),
  D6 (TLH — equity-comp creates concentrated single-stock
  holdings that can be diversified via tax-loss-paired sales),
  D10 (estate-and-beneficiary — concentrated single-stock
  positions create estate-planning complexity).
- **Mental model summary**: For households where *equity
  compensation is a material share of total comp* (FAANG /
  startup / public-tech worker, executive at any public
  company, attorney partner with restricted units, doctor
  with practice-equity), the personal-finance decisions
  interact with the equity-comp mechanics in ways the
  generic frameworks don't capture. RSU (Restricted Stock
  Unit) vesting is taxed as ordinary-income at vest at
  the FMV-on-vest-date, with shares either sold-to-cover-
  tax-only (default at most employers) or fully-vested-and-
  sold (asker's choice via standing-instruction); the
  *sell-on-vest is tax-neutral* because vest is already
  the taxable event, and continued-hold is structurally
  identical to buying-the-employer-stock-with-after-tax-cash
  (rarely the right move from a diversification standpoint).
  ISO (Incentive Stock Option) exercise triggers AMT
  parallel-tax based on bargain-element-FMV-minus-strike,
  with the AMT-credit-recoverable-in-future-years and the
  qualifying-disposition 2-year-from-grant + 1-year-from-
  exercise hold for LTCG treatment on full appreciation.
  ESPP (Employee Stock Purchase Plan) under §423
  qualifying-disposition gives LTCG treatment on appreciation
  beyond the 15% discount-built-into-price; disqualifying-
  disposition makes the discount ordinary-income.
  Section 83(b) election on restricted stock (typically
  startup founder-stock) elects to tax the vest at *grant*
  rather than *vest* — saves enormously on AMT and ordinary-
  income at later vest if stock appreciates, but locks in
  the tax if stock declines. QSBS Section §1202 5-year-hold
  on qualified-small-business-stock allows up to $10M or
  10x-basis exclusion from capital-gains. The framing
  reasons in *equity-comp-mechanics-times-personal-finance-
  framework* terms. Characteristic move: when an asker
  mentions RSU / ISO / ESPP / 83(b) / QSBS, the framing
  *overrides* the generic priority-order to address the
  equity-specific tax-and-concentration concerns first.
  Boundary `tech-career` (the deeper analysis on equity-
  comp mechanics lives there; this framing is the
  intersection-with-personal-finance).
- **Characteristic vocabulary**: "RSU vest-and-sell vs hold",
  "ordinary-income at vest", "sell-on-vest is tax-neutral",
  "ISO AMT parallel-tax", "bargain-element calculation",
  "qualifying disposition (ISO 2+1-year hold)",
  "disqualifying disposition", "ESPP §423 qualifying
  disposition", "15% ESPP discount", "lookback feature",
  "Section 83(b) election within 30 days of grant",
  "QSBS Section §1202 5-year hold", "$10M / 10x exclusion",
  "10b5-1 trading plan", "blackout window", "concentration
  risk (single-employer stock)", "stealth-allocation",
  "deferred comp Section 409A".
- **Excludes**:
  - The "sell-on-vest is tax-neutral" reflex is correct
    on RSU mechanics but the framing rarely engages with
    *RSU lockup and 10b5-1 trading-plan requirements* —
    for many tech employees, blackout windows around
    earnings, IPO-lockup periods (typically 180 days
    post-IPO), 10b5-1 plan pre-commitment requirements,
    and securities-law restrictions on insider trading
    constrain the *timing* of sell-on-vest, and the
    diversification benefit is delayed. Boundary
    `tech-career` D4.
  - ISO-AMT-exercise-timing is *highly path-dependent* on
    company stage and stock-price trajectory — the framing's
    "exercise early for QSBS clock" reflex can be
    catastrophic if the company subsequently declines (AMT
    paid on FMV-at-exercise becomes a cash drag against
    a declined stock that may never recover). The
    framing's risk-tolerance calibration on ISO-exercise
    rarely matches the *actually-asymmetric* downside.
    Boundary `tech-career` D6.
  - Section 83(b) elections are *irrevocable, 30-day-
    window-from-grant* decisions — the framing's "elect 83(b)
    on founder stock" reflex is correct for high-conviction
    startup-founders but can lock in $50-200k of ordinary-
    income tax on stock that may be worth $0 in 3 years.
    The framing rarely engages with the asymmetric-risk-
    profile that makes 83(b) genuinely a high-conviction
    bet rather than a routine optimization.
  - QSBS Section §1202 has *eligibility conditions* the
    framing rarely surfaces — the issuing company must
    have aggregate assets ≤$50M at the time of stock
    issuance, must be a C-corp, must be in an active
    business (not investment / personal-services /
    farming / hospitality), the holder must have acquired
    stock from the corporation (not from a secondary
    purchase), and the 5-year-hold-period applies per-
    share (early-exercise-on-vest may reset the clock).
    The framing's enthusiasm for QSBS understates the
    eligibility-fragility. Boundary `entrepreneurship`
    on QSBS planning.

---

## Coverage map

Per `_schema.md`, every decision needs ≥ 3 framings.

| Decision | Framings that cover it | Count |
|---|---|---|
| D1 Retirement-account contribution ordering | F1, F2, F3, F4, F11, F13, F14 | 7 |
| D2 Traditional vs Roth split | F1, F2, F4, F12, F14 | 5 |
| D3 Asset location across account types | F3, F5, F9, F10 | 4 |
| D4 Brokerage asset allocation and glide path | F5, F7, F10, F11, F14 | 5 |
| D5 Debt-payoff vs invest | F1, F6, F11, F13, F14 | 5 |
| D6 Tax-loss harvesting and wash-sale | F4, F5, F11, F14 | 4 |
| D7 Roth conversion ladder | F2, F4, F7, F12, F13 | 5 |
| D8 Retirement withdrawal sequencing + RMD + SS | F3, F7, F9, F11, F12, F13 | 6 |
| D9 College funding mix — 529 / Roth / taxable | F1, F9, F12 | 3 |
| D10 Estate-and-beneficiary structuring | F3, F8, F9, F10, F12, F14 | 6 |

All 10 decisions satisfy the ≥3 framings minimum. F10
(professional-referral-and-conflict-of-interest) is a meta-framing
that applies as a Critic / Editor layer context on top of any
primary decision framing. F11 (behavioral-and-automation) and F12
(policy-volatility / system-skepticism) similarly apply as cross-
cutting meta-framings — they tune the recommendation surfaced by
any other framing rather than being the primary lens themselves.

## Cross-framing tensions

Direct axiom-level oppositions to surface in Layer 3 and to flag
for Triage / Risk Officer routing when the asker's prompt
vocabulary lands on one side:

- **F1 (priority-order) ↔ F14 (equity-comp / concentration-risk)**.
  F1's clean Bogleheads-canonical sequence assumes smooth W-2
  cash flow and unconstrained-by-equity-comp household budget.
  F14 overrides the priority order for equity-comp-heavy
  households: the highest-leverage move may be *sell-on-vest to
  diversify the $400k single-employer concentration* before
  funding any retirement vehicle, because the concentration-risk
  reduction dominates the marginal-tax-arbitrage of the next
  contribution step. Same household, opposite first-move. Triage
  should surface F14 whenever the asker mentions RSU / ISO /
  ESPP / 83(b) / QSBS or names a tech-employer; surface F1
  when the asker is a stable-W-2 non-equity-comp household.

- **F2 (marginal-rate arbitrage) ↔ F12 (policy-volatility)**.
  F2 computes contribution arbitrage from current marginal vs
  projected retirement marginal as deterministic point-estimates.
  F12 argues the projected retirement marginal is itself a
  policy-determined variable subject to TCJA-sunset / SECURE-
  cycle / SS-benefit-cut volatility, and recommends Roth-tilt
  as a policy-hedge. The conflict surfaces on D2: F2 says
  traditional for the high-current-marginal 32% asker; F12
  says Roth for the same asker because 2026-bracket-reversion
  may make today's 24% effective rate look unusually low
  retrospectively. Same facts, opposite Roth/traditional answer.

- **F3 (HSA-as-stealth-IRA) ↔ F6 (behavioral-debt-payoff) when
  cash-flow-constrained**. F3 says fund HSA to the cap, pay
  current medical OOP from after-tax savings, let HSA compound
  30 years. F6 says for the household with $15k credit-card
  debt and no emergency fund, the cash-flow constraint binds
  before HSA optimization; the HDHP-high-deductible exposure
  combined with no-emergency-fund creates catastrophic
  vulnerability that F3's long-horizon framing ignores. Triage
  should surface F6 when the asker's facts indicate cash-flow
  stress; surface F3 when the asker reads as savings-rich.

- **F5 (risk-adjusted allocation) ↔ F14 (equity-comp /
  concentration-risk)**. F5 reasons about portfolio-level
  target allocation with classical Modern-Portfolio-Theory
  diversification arguments. F14 surfaces that vested-RSU
  + ESPP-discount-stock create a *stealth allocation* that
  swamps any chosen target — a $480k single-employer position
  in a household with $1.2M total net worth is a 40%
  concentration that overrides the 70/30 target the asker
  asked for. Both framings independently recommend
  diversification, but F5 frames it as "pick a target and
  rebalance" while F14 frames it as "sell the concentration
  first, then think about target." On D4 they converge on
  outcome but diverge on path; Triage should surface both
  when equity-comp is present.

- **F7 (lifecycle / retirement-econ) ↔ F9 (estate-and-
  intergenerational)**. F7's withdrawal-sequencing default
  (taxable first, then tax-deferred, then Roth — preserves
  Roth tax-free compounding longest) is *inverted* by F9
  when intent-to-bequeath is material — F9 recommends
  running down traditional-401(k)-and-IRA during life (heirs
  inherit Roth or stepped-up-basis-taxable instead of
  ordinary-income-on-distribution-traditional). Same
  withdrawal decision, opposite sequence. Triage should
  surface F9 when the asker mentions inheritance / leaving
  money to kids / estate planning; surface F7 when asker
  frames it as pure self-consumption.

- **F8 (asset-protection / creditor-shield) ↔ F1 (priority-
  order)**. F1's "rollover 401(k) to IRA on job change for
  lower-cost-investment-options" is correct on expense-ratio
  arithmetic but *weakens creditor protection* per F8 —
  ERISA-protected 401(k) is unlimited federal-bankruptcy-
  exempt; rollover-IRA is capped at $1.5M-indexed and
  state-variation-dependent. For HNW or high-liability-
  profession askers, F8 argues *stay in the 401(k)* even at
  expense-ratio cost. F1 alone misses this. Same rollover
  question, opposite answer depending on litigation-risk
  profile.

- **F10 (professional-referral) ↔ F11 (behavioral-and-
  automation)**. F10's "always-consult-a-fee-only-CFP for
  individual-recommendation decisions" is the safe default
  for the asker without time-or-inclination to self-study.
  F11's "automate everything via Bogleheads-flowchart-DIY +
  robo-rebalancing" is the right call for the asker with
  financial literacy and discipline. The conflict surfaces
  when a moderate-complexity asker asks "should I hire an
  advisor or do this myself" — F10 reflexively recommends
  consultation, F11 reflexively recommends DIY-automation.
  Both are valid for different asker profiles; Triage should
  surface based on asker's stated financial-literacy and
  complexity-tolerance.

- **F13 (FIRE / extreme-saver) ↔ F7 (lifecycle / retirement-
  econ academic)**. F13's 4%-safe-withdrawal-rate is
  calibrated to 30-year retirements; F7 argues for 3-3.5%
  for 50-year-retirement (early-FIRE) horizons. Same
  savings-target ($1M), opposite sustainable-spending answer
  ($40k/yr vs $30k/yr). Triage should surface F7 when the
  asker is an early-FIRE candidate; both framings can
  appear together on the trade-off explicitly.

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  every `Excludes` bullet above is a Layer 3 candidate.
  Highest-density candidates are framings 1 (priority-order —
  match-vesting-cliff conditional-EV, HDHP-medical-cost
  trade-off, dual-spouse joint-flowchart, self-employed
  substitution), 2 (marginal-rate — TCJA-sunset volatility,
  income-projection precision, asymmetric-cap-utility hidden
  to non-cap-constrained, FICA on traditional missed), 3
  (HSA-as-stealth-IRA — cash-flow-mismatch, Medicare-Part-A
  retroactivity, non-spouse-heir taxable-in-full, reimburse-
  as-you-go for major-medical-events-young), 4 (tax-arbitrage
  Form-mechanic — practitioner-error rate on backdoor-Roth,
  tax-code political dynamism, CPA-specialty-filter, dual
  5-year-clock confusion), 7 (lifecycle — human-capital
  equity-like for equity-comp, bond-tent counterintuitive
  implementation barriers, safe-withdrawal-rate calibration-
  to-historical-US, linear-career-assumption breaks), 8
  (asset-protection — 401(k)-fee vs shield trade-off, state-
  shield-law currency, *Clark v Rameker* inherited-IRA
  exposure, over-isolation administrative cost), 9 (estate-
  intergenerational — withdrawal-sequence inversion missed,
  SECURE-1.0 RMD-during-10-years misunderstood, 2025-sunset
  political uncertainty, beneficiary-form operational
  friction), 10 (professional-referral — AUM-fee-fee-only
  rollover bias, CFP coverage uneven across decisions,
  DIY-via-Bogleheads under-engaged, access-inequality
  barriers), and 14 (equity-comp — RSU lockup / 10b5-1
  constraints, ISO-AMT path-dependence, 83(b)-irreversibility,
  QSBS eligibility fragility). Sweep all 14 framings × ~4
  bullets each = ~56 blindspot candidates; promote ≥5 per
  framing into `blindspots.md` per the
  [`_schema.md`](../_schema.md) minimum.

- **High-stakes posture (Mechanism E)**: this file is
  decision-support, not financial advice. Editor on any
  answer that lands on these framings must (per
  `domain_pack.md` once authored) explicitly label output
  as "decision-support, not financial advice" and route to
  the *specific category-appropriate professional* per the
  selective-referral matrix in
  [`decisions.md` §Notes](./decisions.md) — fee-only
  fiduciary CFP (NAPFA / XY-Planning / Garrett) for D3 / D4
  / D8; retirement-and-equity-comp CPA for D1 / D6 / D7
  (backdoor-Roth Form 8606, TLH wash-sale validation, Roth-
  conversion sizing vs IRMAA / ACA / NIIT cliffs); fee-only
  Social-Security-claiming specialist for D8's claim-age
  coordination; state-bar-licensed estate attorney for D10
  (SLAT / GRAT / Dynasty drafting, 2025-sunset-pre-2026
  gifting, beneficiary-form audit); ERISA attorney for D1 +
  D10 (high-balance 401(k) disputes, Rule-of-55 / SEPP-72(t)
  plan-document review, post-divorce QDRO drafting, creditor-
  protection consultation); SHIBA / SHIP volunteer for D8's
  Medicare-coordination side; SEC IAPD / FINRA BrokerCheck
  verification as $0-friction procedural floor on every
  individual-professional referral. Critic must apply stricter
  grounding on citation-bearing claims (IRC §401(k) / §408 /
  §223 / §529 / §1202 / §1014 / §72(t), ERISA §404 / §405 /
  §1144, 11 USC §522, SECURE Act 1.0 / 2.0, TCJA 2017, ARPA
  / IRA 2021-2022, IRS Pub 550 / 590-A / 590-B / 525 / 969 /
  970, *Patterson v Shumate*, *Egelhoff v Egelhoff*, *Clark
  v Rameker*); generic "the law says X" claims unanchored to
  a cite should fail Critic review. Dollar-specific investment
  recommendations on individual securities are uniformly
  out-of-scope at the Editor layer regardless of decision
  category — this is the load-bearing Mechanism E gate for
  the domain.

- **Triage routing notes**: framings 4, 8, 9, 14 carry the
  most distinctive vocabulary signatures (Form 8606 / 8889 /
  8949 / 1099-R / 5498; *Patterson v Shumate* / *Egelhoff* /
  11 USC §522; SECURE 1.0 / 10-year-rule / SLAT / GRAT;
  RSU / ISO / ESPP / 83(b) / QSBS / §1202) and should be
  high-confidence routing matches. Framings 1, 2, 3, 5, 7
  share vocabulary with general personal-finance content and
  will need disambiguation against adjacent domain packs once
  V2 two-pass Triage is wired — particularly against
  `tech-career` (which overlaps F14 deeply on equity-comp
  mechanics), `health-insurance` (which overlaps F3 on HSA
  mechanics and F12 on Medicare / IRMAA policy), and
  `housing` (which overlaps F6 on mortgage-vs-invest and F9
  on Section-121-primary-residence basis-step-up). F10
  (professional-referral / conflict-of-interest), F11
  (behavioral-and-automation), and F12 (policy-volatility)
  are Critic / Editor meta-context framings; they should NOT
  route as the primary decision-framing on most answers but
  should be available for Editor framing-aware completions
  on top of a primary decision lens.

- **Cross-domain edges from `decisions.md`**: F1 (priority-
  order) crosses into `tech-career` (equity-comp affects
  cash-flow availability), `health-insurance` (HDHP-and-HSA
  step-3 is the load-bearing boundary), and `entrepreneurship`
  (solo-401(k) / SEP-IRA substitution at step-4 changes pro-
  rata-IRA-trap math). F4 (tax-arbitrage Form-mechanic) routes
  into `health-insurance` (HSA FICA arbitrage, IRMAA 2-year-
  lookback), `tech-career` (RSU / ISO / ESPP / 83(b) forms),
  and `housing` (Section-121 Form 8949 reporting). F6
  (behavioral-debt-payoff) routes into `education-funding`
  (PSLF / IDR forgiveness inverting the rate calculation) and
  `housing` (mortgage-vs-invest as special case). F8 (asset-
  protection / creditor-shield) routes into `legal-disputes`
  (state-vs-federal bankruptcy mapping, QDRO, ERISA pre-emption),
  `entrepreneurship` (LLC / S-corp isolation), and `family-
  planning` (premarital agreement). F9 (estate-and-intergenerational)
  routes into `family-planning` (trusts, blended-family
  beneficiary coordination, 529 grandparent-vs-parent FAFSA)
  and `legal-disputes` (will-contests, beneficiary-form
  challenges). F12 (policy-volatility) routes into `health-
  insurance` (ACA / Medicare policy volatility) and
  `education-funding` (FAFSA Simplification, PSLF expansion,
  IDR shifts). F14 (equity-comp / concentration-risk) routes
  into `tech-career` deeply (deeper equity-comp mechanics
  live there) and `entrepreneurship` (founder-stock QSBS).
  Triage should surface these adjacencies when the user's
  situation spans both domains.

- **Voice-anchor → sources.yaml hand-off** (Layer 4 forward-
  pointer): the conceptual voices named in the intro map to
  these candidate source-view families. Fee-only-fiduciary-CFP
  → NAPFA.org / XY-Planning-Network / Garrett-Planning-Network
  member directories plus individual practitioner blogs.
  Bogleheads → bogleheads.org wiki (Investment Priority Order,
  Tax-Efficient Fund Placement, Backdoor Roth pages), the
  bogleheads.org forum, r/Bogleheads. Mr-Money-Mustache / FIRE
  → mrmoneymustache.com, ChooseFI podcast and blog,
  r/financialindependence wiki + flowchart, *Early Retirement
  Now* (Big-ERN's safe-withdrawal-rate series). Financial-
  economics-journalism → David Wessel at Brookings, Jeff
  Sommer at NYT, Anne Tergesen at WSJ, NPR *Planet Money*.
  Retirement-econ academic → Wade Pfau's RetirementResearcher,
  Michael Kitces's kitces.com Nerd's Eye View, Larry
  Kotlikoff's KotlikoffOnFinance + Maximize-My-Social-Security,
  *Journal of Financial Planning*. The Finance Buff →
  thefinancebuff.com (backdoor-Roth, Mega-Backdoor-Roth,
  HSA-FICA-arbitrage guides). Retirement-experienced-CPA →
  AICPA Personal Financial Planning Section, individual CPA-
  blog practitioners with retirement / equity-comp depth
  (verify via experience-with-specific-forms not credential).
  ERISA-practitioner → ERISA-attorney blogs (Natalie Choate,
  Mary Kay Foss), ABA Section of Real Property Trust & Estate
  Law, ERISA Industry Committee (ERIC). SEC EDGAR / FINRA
  BrokerCheck / SEC IAPD → adviserinfo.sec.gov, brokercheck.finra.org,
  SEC.gov investor-alerts. IRS-publication-authority → Pub
  550 / 590-A / 590-B / 525 / 969 / 970, Form 8606 / 8889 /
  8949 / 8962 Instructions. Fee-only Social-Security-claiming-
  specialist → Mike Piper's Open-Social-Security + *Social
  Security Made Simple*, Larry Kotlikoff's Maximize-My-Social-
  Security, federally-funded SHIBA / SHIP per-state via
  shiphelp.org. State-bar-estate-attorney → state-bar lawyer-
  referral-services (NOT for-profit finders), ACTEC, Heckerling
  Institute materials. Personal-finance-influencer / mass-media
  → Suze Orman, Dave Ramsey, Ramit Sethi (catch-and-translate
  the patterns; do not cite for technical tax / ERISA claims).
  Chronic-DIY-Reddit → r/personalfinance wiki + flowchart,
  r/Bogleheads pinned posts, r/financialindependence wiki,
  r/tax pinned guides. Sources author should weight reliability
  and keyword_filter per `_schema.md`; high-stakes domain
  requires reliability ≥3 for any source cited in Risk Officer
  answers, ≥4 for direct citation in Editor framing-claims,
  with IRS-publication-authority voice uniquely permitted to
  ground tax-mechanic claims that conflict with practitioner-
  blog interpretations.
