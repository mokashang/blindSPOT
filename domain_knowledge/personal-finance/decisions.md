# personal-finance — decisions.md (Layer 1)

Decision ontology for `personal-finance`. Scope inherits from
[`_meta_ontology.md` §5](../_meta_ontology.md): US-resident knowledge-
worker personal-finance decisions — retirement-account contribution
ordering across 401(k) / 403(b) / 457(b) / IRA / Roth-IRA / HSA / 529,
asset-location and asset-allocation across tax-deferred / Roth /
taxable / HSA buckets, debt-payoff-vs-invest prioritization,
tax-loss-harvesting and wash-sale management, Roth-conversion-ladder
strategy in low-income years, retirement-withdrawal sequencing
including RMD planning and Social Security claim-age coordination,
college-funding mix (529 / Coverdell / Roth-as-college-substitute /
taxable / UGMA-UTMA), and estate-and-beneficiary structuring
(TOD / POD / trust-vs-direct beneficiary, basis-step-up, lifetime
estate-tax-exemption sunset). Excludes dollar-specific investment
recommendations on individual securities (gated under Mechanism E
below), deep entity-tax optimization for operating businesses
(overlaps `entrepreneurship`), and jurisdiction-specific estate-tax
litigation (overlaps `legal-disputes`).

The `personal-finance` domain is **high_stakes: true** per
`_meta_ontology.md` §5 and is the canonical Mechanism E gating case
named in ROADMAP §5 — dollar-specific investment guidance is exactly
the harm class the gate was written to prevent. Three distinct
classes of irrevocability drive the posture:

- **Tax-year-boundary one-shot windows**: Many contribution and
  conversion mechanics are calendar-year-bound and cannot be redone
  after April 15 (extension to Oct 15 for some — verify per
  decision). Roth-IRA contributions for tax-year-N must be made by
  the unextended tax-filing deadline of year-N+1; backdoor-Roth
  conversions cleanest when no other pre-tax IRA balance exists at
  Dec 31 (the pro-rata rule treats ALL pre-tax IRA dollars as one
  pool for the Form 8606 basis calculation, not just the
  conversion-source IRA); Roth-conversion recharacterizations were
  permanently eliminated by TCJA 2017 (a Roth conversion is
  irrevocable from the day it is executed — there is no "undo"). The
  401(k)-Mega-Backdoor mechanic requires after-tax 401(k)
  contributions PLUS in-plan-Roth-conversion or in-service-rollover-
  to-Roth-IRA capability — both are plan-document features the
  employer chooses to enable or not; the window is the calendar year
  the plan offered them.
- **Permanent penalties** on certain Social Security and Medicare-
  adjacent mechanics: claiming Social Security before Full
  Retirement Age (FRA — 67 for those born 1960+) locks the
  Primary Insurance Amount (PIA) at a permanent reduction (~30% at
  age 62), which compounds for the rest of the beneficiary's life
  AND of the surviving spouse via the higher-earner-claim-survivor-
  benefit rule; missing the 60-day indirect-rollover window on a
  401(k)-to-IRA rollover causes the distribution to be treated as a
  taxable distribution with no second chance (use a direct trustee-
  to-trustee transfer to avoid the trap entirely). Wash-sale
  violations don't disallow the loss permanently but do defer it
  into the basis of the replacement security — material when the
  replacement is in a tax-advantaged account where the deferred-
  basis is functionally lost (IRS Rev Rul 2008-5).
- **Compounding-cost-of-procrastination**: Unlike most life-decision
  domains where the "wait one more year" cost is bounded, retirement
  contribution gaps compound at the equity risk premium for
  30+ years. A missed $7,000 Roth-IRA contribution at age 30
  compounds to $76k at age 65 at a 7% real return; the missed
  contribution cannot be re-made in a later year because annual caps
  are per-year-use-it-or-lose-it. The asymmetry between procrastinable
  decisions (housing-relocate, job-change) and non-procrastinable
  decisions (annual retirement contributions) is itself a framing
  axis that this domain should make explicit. Same compounding
  asymmetry applies to HSA contributions when used as a retirement
  vehicle (boundary `health-insurance` decision 1 / decision 9).

Posture: **"decision-support, not financial advice"** is the
consistent Editor framing. Downstream `blindspots.md` Recovery moves
should defer to specific professional categories keyed by decision
rather than blanket-mandating one on every framing — over-referral
degrades signal; the user has often already heard "see a financial
advisor" and ignored it because the advice was generic. Selective
referral:

- **Fee-only fiduciary CFP** (NAPFA or XY-Planning-Network — fee-only
  rather than commission-based or "fee-based" hybrid; the distinction
  is load-bearing because AUM-based and commission-based advisors
  have structural incentive to recommend rollover-to-IRA, annuity-
  purchase, or active-management even when index-fund-DIY would
  strictly dominate) for asset-allocation, glide-path, and any
  individual-security recommendation. Hourly-only or flat-fee
  planners (Garrett Planning Network) are the right referral when
  the user has a bounded one-time question rather than ongoing
  AUM management; the structural-conflict-of-interest framing is
  itself an axis that the Editor should surface.
- **CPA** (preferably one with retirement-plan and equity-comp
  experience — NOT a generic tax-prep CPA) for tax-loss-harvesting
  + wash-sale validation, backdoor-Roth Form 8606 pro-rata math,
  Mega-Backdoor Roth in-plan-conversion mechanics, Roth-conversion
  ladder sizing relative to IRMAA / ACA-subsidy / NIIT brackets,
  QSBS-Section-1202 exclusion (boundary `tech-career` /
  `entrepreneurship`), Form 5498 / Form 1099-R reconciliation when
  rollover-related 1099 codes are wrong, and any year where
  brokerage-1099 + W-2 + 1099-DIV cross multiple AGI cliffs (NIIT
  at $200k single / $250k MFJ, IRMAA tiers at $103k / $129k / $161k
  / $193k / $500k+ single MAGI). The CPA-vs-CFP referral overlaps
  heavily — many decisions need both, in sequence: CPA validates the
  tax mechanic, CFP validates the asset-allocation impact.
- **ERISA attorney** for high-balance situations (low-7-figure-plus
  401(k) balances facing a 401(k)-force-out-on-termination dispute,
  401(k)-loan-on-termination 90-day cure window, plan-document
  interpretation disputes around early-distribution exceptions like
  Rule-of-55 / SEPP-72(t) / QDRO division, and any plan-level
  fiduciary-breach claim under ERISA §404 / §405). Distinct from
  the `legal-disputes` cross-domain referral — ERISA pre-empts
  state-law remedies, which constrains procedural posture and
  damages availability sharply (see `health-insurance` decision 3
  for the parallel ERISA pre-emption framing on the insurance side).
- **Social-Security-claiming-strategy specialist** (fee-only,
  NAPFA-listed planners with Social Security software like
  Maximize-My-Social-Security / Open-Social-Security from Mike Piper,
  OR a federally-funded SHIBA / SHIP volunteer for the Medicare-
  coordination side) for the Social-Security-claim-age decision at
  62 / 63 / 64 / 65 / FRA / 70. The decision is unusually well-
  modeled — break-even analysis on continued-work earnings cap, FRA
  spousal/survivor coordination, child-in-care-survivor-benefit,
  divorced-spouse-survivor-benefit — and is exactly where generic
  "claim at 62 because the breakeven is at 80" framing fails because
  it ignores survivor benefits and the asymmetric-longevity-bet.
- **State-bar-licensed estate attorney** for trust formation (rev-
  trust vs irrev-trust vs SLAT vs ILIT vs CRT/CLT vs Dynasty trust),
  beneficiary-form audit (TOD / POD / IRA-beneficiary forms
  supersede the will — a stale ex-spouse on a 401(k) beneficiary
  form overrides a current spouse named in the will; the
  Egelhoff-vs-Egelhoff Supreme Court precedent settled this in
  ERISA-plan context), and any decision touching the 2025 sunset
  of the doubled lifetime-estate-tax-exemption ($13.99M-per-individual
  in 2025 falling to ~$7M-indexed in 2026 absent congressional
  extension — verify current statute before recommending; the
  doubled exemption was a TCJA 2017 provision with a 2026 sunset
  baked in, and pre-2026 estate-planning moves (SLAT, gift-now-pay-
  later) are time-bound).
- **SEC / FINRA BrokerCheck verification** is a procedural floor —
  ANY individual recommended (CFP, CPA, ERISA attorney, Social
  Security planner) should be cross-checked at brokercheck.finra.org
  or the SEC IAPD for disclosure events; this is a $0 zero-friction
  step that catches advisors with material disciplinary histories.
  The Editor layer should surface this anchor on every individual-
  professional recommendation, not as an over-referral but as a
  procedural safety check.

Framing-axes named below are pointers — full framings will live in
`framings.md` (later artifact). `personal-finance` is **the most
cross-cutting V2 domain** — every other domain in `_meta_ontology.md`
has a material edge into it because tax-and-cash-flow consequences
cascade out of most life decisions. Cross-domain edges flagged
inline below: `tech-career` overlaps on RSU-vest-and-sell vs hold
(decisions 1, 4), ISO-AMT-exercise-timing (decisions 1, 4, 6),
deferred-comp Section 409A elections (decisions 1, 8), 83(b)-election
timing on restricted stock (decisions 1, 6). `health-insurance`
overlaps on HSA-as-triple-tax-advantaged-retirement (decisions 1,
3, 8), FSA-timing-vs-HSA-vs-LPFSA (decision 1), Medicare-IRMAA-
tier-management via Roth-conversion-sizing (decisions 7, 8).
`housing` overlaps on primary-residence-as-asset (decisions 4, 5,
8, 10), mortgage-interest-deduction-interaction-with-SALT-cap
(decisions 1, 5), cash-out-refi-vs-HELOC-vs-portfolio-margin
(decision 5), Section-121-primary-residence-capital-gains-exclusion
(decisions 8, 10). `family-planning` overlaps on 529-funding-
ordering and superfunding-5-year-election (decisions 1, 9),
spousal-IRA contribution rules (decision 1), beneficiary-form-
audit-on-marriage-divorce-birth-death (decision 10), kiddie-tax
on UGMA / UTMA (decision 9), 2025-estate-tax-exemption-sunset
preparation (decision 10). `education-funding` overlaps on 529-vs-
Roth-vs-taxable funding mix (decision 9), 529-to-Roth-rollover
SECURE 2.0 mechanics (decision 9), student-loan PAYE / SAVE / IDR
forgiveness with marital-tax-filing-strategy interaction (decision
5), Public-Service-Loan-Forgiveness (PSLF) AGI-management. 
`entrepreneurship` overlaps on solo-401(k) / SEP-IRA / SIMPLE-IRA
selection for self-employment income (decision 1), QBI Section-199A
deduction sizing (decisions 1, 7), QSBS Section-1202 5-year-hold
and gain-exclusion (decisions 1, 6, 7), backdoor-Roth complication
when self-employment SEP-IRA balance exists (decision 1, pro-rata).
`legal-disputes` overlaps on creditor-protection-of-retirement-
accounts (ERISA-protected 401(k) is unlimited federal-bankruptcy-
exempt; IRA is federal-bankruptcy-exempt to ~$1.5M-indexed but
state shield varies sharply — Texas / Florida unlimited, California
post-bankruptcy-only, NY partial — see decision 10), QDRO division
of retirement accounts on divorce (decision 10), and any tax-
deficiency-related back-tax-collection action. Routing across edges
is V2-Triage's job; the edge annotations here help future
`framings.md` authors name the adjacent domains.

---

## 1. Retirement-account contribution ordering (priority sequence across vehicles)

- **Scope**: Individual or married-household allocating annual
  retirement-savings cash flow across the available tax-advantaged
  vehicles in priority order. Canonical ordering recommended in the
  Bogleheads "investment priority order" is: (1) capture full
  employer-401(k) match; (2) pay down high-interest debt above
  ~7% effective; (3) max HSA if HDHP-eligible (highest-marginal-
  utility dollars because triple-tax-advantaged); (4) max
  traditional-or-Roth 401(k) to the elective deferral cap
  ($23,500 in 2025 + $7,500 age-50 catch-up + $11,250 age-60-63
  super-catch-up added by SECURE 2.0); (5) max Roth IRA via direct
  contribution if income-eligible, else via backdoor Roth ($7,000
  + $1,000 age-50 catch-up in 2025); (6) Mega-Backdoor Roth via
  after-tax 401(k) + in-plan-conversion (up to the $70,000 §415(c)
  total cap in 2025 minus elective + match); (7) 529 for kids
  (boundary `education-funding` / `family-planning`); (8) taxable
  brokerage; (9) low-interest debt paydown. Decision is the joint
  ordering AND amount split when total available cash is less than
  the sum of all caps. Distinct from decision 2 (within-401(k)
  traditional-vs-Roth split) and decision 6 (within-taxable
  tax-loss-harvesting). Cross-routes `tech-career` (when annual
  comp is RSU-heavy the cash-flow available for these contributions
  varies sharply year-to-year), `health-insurance` (HSA eligibility
  depends on HDHP enrollment from decision 1 in that domain),
  `entrepreneurship` (self-employed users substitute solo-401(k)
  or SEP-IRA for the W-2 401(k) — the solo-401(k) cap is higher
  and the employer-contribution side flexes with profit, but
  pro-rata complicates backdoor-Roth).
- **Framing-axes-covered**: marginal-tax-rate-vs-expected-retirement-
  rate-arbitrage (the central decision-input for traditional vs
  Roth at every step — see decision 2 for the deeper framing;
  generic "Roth-when-young, Traditional-when-old" heuristic fails
  for high-earners in high-tax states because the current 37%
  federal + 13.3% CA marginal is unlikely to be exceeded in
  retirement), employer-match-as-100%-immediate-return (the
  match-capture step dominates every other priority because no
  other vehicle returns 50–100% immediately; even a credit-card-
  paydown at 25% APR is dominated by a 100%-match dollar — match-
  first is non-negotiable absent extreme cash-flow distress),
  HSA-as-triple-tax-advantaged-strictly-dominates-401k-after-match
  (HSA dollars are pre-tax-in via payroll-deduction with FICA
  exemption that 401(k) lacks — a 7.65% additional savings — plus
  tax-free growth plus tax-free out for qualified medical; if the
  user can pay current medical OOP and let HSA compound, HSA
  strictly dominates 401(k)-beyond-match dollar-for-dollar for
  retirement-purpose savings; boundary `health-insurance` decision
  1 / decision 6 / decision 9), backdoor-Roth-pro-rata-trap-on-
  existing-pre-tax-IRA (the IRS pro-rata rule treats ALL pre-tax
  IRA / SEP-IRA / SIMPLE-IRA dollars as one aggregated pool at
  Dec 31; a backdoor Roth executed while ANY pre-tax IRA balance
  exists is partially taxable on Form 8606 — the work-around is
  reverse-rollover-of-pre-tax-IRA-into-401(k) BEFORE doing the
  backdoor, but plan-document must accept incoming-rollovers and
  the rollover must be completed by Dec 31; self-employed users
  with a SEP-IRA balance face the same trap), Mega-Backdoor-Roth-
  plan-document-dependency (after-tax 401(k) contributions are a
  plan-document feature, not a default; in-plan-Roth-conversion
  or in-service-distribution-to-Roth-IRA is ALSO a plan-document
  feature — both must be present; ~30% of large-employer 401(k)
  plans have the after-tax contribution but no in-plan-conversion,
  which strands the dollars as a pro-rata-taxable rollover later;
  verify SPD before counting on it), age-50-catch-up-and-age-60-
  63-super-catch-up-SECURE-2.0 (the $7,500 catch-up at 50+ and
  the new $11,250 super-catch-up at 60-63 expand the 401(k) cap;
  the super-catch-up is automatically Roth for high-earners under
  SECURE 2.0 Section 603, which phased in 2026), HSA-and-Medicare-
  mutual-exclusion-and-Part-A-retroactive (enrolling in Medicare
  voids HSA-eligibility prospectively; SS-claiming triggers
  Part-A retroactively up to 6 months, so stop HSA contributions
  6 months before SS-claim if claiming past 65 — boundary
  `health-insurance` decision 9), spousal-IRA-rules-for-non-
  working-or-low-earning-spouse (a non-working or low-earning
  spouse can contribute to their own IRA based on the working
  spouse's earned income — IRS Pub 590-A; useful when one spouse
  is on sabbatical or career-break and gets ignored because the
  default-frame is "you need earned income to contribute",
  boundary `family-planning`), Roth-IRA-direct-contribution-
  phase-out-vs-backdoor-Roth-substitute (direct Roth phase-out is
  $146-161k single / $230-240k MFJ MAGI in 2025; above phase-out
  the backdoor mechanic is the substitute, but pro-rata applies
  — see above), 401(k)-loan-as-near-equity-substitute-but-
  procyclical-risk (401(k) loan up to 50% / $50k at prime+1; on
  termination most plans require repayment in 90 days or it
  becomes a distribution; procyclical because layoff and forced
  401(k)-loan-repayment-in-distressed-market is a known double-hit
  trap).
- **Sample situations**:
  - "32yo single, $200k W-2 in CA, no debt; employer matches 6%
    of base. HDHP eligible. Have $30k/year available beyond
    living expenses for retirement savings. How to allocate
    across 401(k), HSA, Roth IRA, taxable?"
  - "Married couple, both 38, one $250k W-2 + RSU and one
    $0 (stay-at-home); $80k/year available. Backdoor Roth for
    both? What about the working spouse's existing SEP-IRA
    from a side-consulting year — does that block backdoor?"
  - "Self-employed consultant earning $180k schedule-C net,
    spouse $60k W-2 with 401(k). Solo-401(k) vs SEP-IRA vs
    SIMPLE-IRA for me? How does each interact with backdoor
    Roth and with spouse's 401(k)?"

## 2. Traditional vs Roth contribution split at a given marginal-rate-vs-projected-retirement-rate

- **Scope**: Within the 401(k) (and within the IRA when income-
  eligible for direct Roth), choosing the split between traditional
  (pre-tax-in, taxable-out) and Roth (after-tax-in, tax-free-out)
  contributions. Decision applies at every contribution-decision
  point in decision 1's ordering. The naive framing — "current
  marginal-rate vs projected-retirement-rate, whichever is lower at
  contribution-time picks the bucket" — captures the first-order
  arithmetic but misses several second-order effects that often
  flip the recommendation: state-tax-residency change in
  retirement, RMD-induced bracket-creep, Social-Security-taxability
  bracket interactions, IRMAA tier-management, and the
  asymmetric-cap-utility framing (Roth contributes more after-tax
  dollars per cap-unit because $23,500 Roth contains $23,500 of
  after-tax-equivalent room vs $23,500 traditional containing
  $23,500 × (1 - marginal-rate) of after-tax-equivalent room).
  Distinct from decision 1 (which vehicles) and decision 7 (Roth
  conversion ladder mid-retirement). Cross-routes `tech-career`
  (high-equity-comp years bunch income artificially high — Roth
  in those years vs traditional in lower-comp years), `housing`
  (state-tax change on retirement-state-relocation), and
  `health-insurance` (Medicare IRMAA tiers are based on MAGI two
  years prior, so traditional-401(k)-distributions raise IRMAA
  surcharges 2 years later — decision 7 picks up the deeper
  framing).
- **Framing-axes-covered**: current-marginal-vs-projected-
  retirement-marginal-arithmetic (the first-order math; if
  current marginal is HIGHER than expected retirement marginal,
  traditional dominates dollar-for-dollar; reverse for Roth; ties
  go to Roth for hedge-against-future-rate-rises reason), state-
  tax-residency-change-in-retirement (moving from CA / NY / NJ /
  OR to TX / FL / WA / NV / NH on retirement saves ~6-13% state-
  tax on traditional-401(k) distributions; if planned, traditional
  is preferred at contribution; if uncertain, Roth hedges; the
  state-tax-arbitrage framing is the single biggest under-named
  factor for HCOL-to-LCOL retirees — boundary `housing` decision
  on retirement-relocation), RMD-induced-bracket-creep (RMDs
  start at age 73 under SECURE 2.0 (age 75 from 2033); a large
  pre-tax-401(k) balance generates forced distributions that can
  push retirees into 22%, 24%, or higher brackets even when
  Social Security and pension are modest; Roth-401(k) and Roth-
  IRA have NO RMD for the original owner under SECURE 2.0;
  inherited Roth IRAs have a 10-year-rule but no annual RMD
  during the 10 years), Social-Security-taxability-bracket-
  staircase (SS benefits become 50% / 85% taxable as provisional-
  income crosses $25k / $34k single / $32k / $44k MFJ thresholds
  — these thresholds are NOT inflation-indexed and have eroded
  in real-value since 1983; Roth distributions don't count toward
  provisional income but traditional-401(k) distributions do —
  for middle-income retirees, Roth can preserve the 0%-tax-on-SS
  band), IRMAA-Medicare-Part-B-and-D-tier-management (IRMAA
  surcharges start at $103k single / $206k MFJ MAGI in 2025 and
  step up sharply at each tier — a Roth-conversion or traditional-
  401(k)-distribution that pushes MAGI into the next tier
  triggers a $1k–4k Part B + Part D premium increase 2 years
  later; the Roth-conversion-ladder in decision 7 is structured
  around this; boundary `health-insurance`), asymmetric-cap-
  utility-Roth-vs-traditional (a $23,500 Roth contribution
  occupies more "tax-free-future-room" than a $23,500 traditional
  contribution; for cap-constrained savers — anyone maxing the
  cap — Roth puts more after-tax dollars into the tax-advantaged
  shell, which materially changes the calculus vs the naive
  marginal-rate framing; this is the "Roth is bigger" argument
  that justifies Roth even when current-marginal exceeds
  projected-retirement-marginal), automatic-Roth-catch-up-SECURE-
  2.0-Section-603 (for participants earning over $145k indexed in
  prior year, the age-50 catch-up MUST be Roth under SECURE 2.0;
  phased in 2026; for affected high-earners this constrains the
  decision below the catch-up amount), tax-diversification-as-
  optionality (holding both traditional and Roth provides
  flexibility to manage retirement-year MAGI for IRMAA / ACA-
  subsidy / NIIT / capital-gains-bracket purposes — pure-
  optimization for one bucket sacrifices this option-value).
- **Sample situations**:
  - "28yo SWE in CA, $180k base + variable RSU, currently 24%
    federal + 9.3% state marginal. Plan to retire at 60 in
    Texas or Florida. Traditional or Roth 401(k)?"
  - "55yo dual-income couple, both $200k W-2 in NY. $2.3M
    combined in traditional 401(k)s, $0 Roth. RMD math says
    we'll be in 24-32% bracket in retirement. Switch new
    contributions to Roth, or convert some traditional to Roth
    now (decision 7)?"
  - "42yo earning $190k just above the SECURE 2.0 Roth-catch-up
    threshold. Have to make age-50 catch-up Roth — does that
    change the rest of my contribution split, or treat as fixed
    constraint?"

## 3. Asset location across tax-deferred / Roth / taxable / HSA

- **Scope**: For a given household-level target asset allocation
  (decision 4), placing specific asset classes into specific
  account types to optimize after-tax growth. Decision is
  orthogonal to allocation (decision 4) and orthogonal to
  contribution ordering (decision 1) but compounds with both.
  Core framing: each account type taxes growth and distributions
  differently — traditional 401(k) is tax-deferred-then-ordinary
  on distribution; Roth is tax-free-out; taxable is tax-free-in
  with annual drag (dividends + interest taxed annually, capital
  gains at sale); HSA is tax-free in/out for qualified medical
  (in retirement, qualified medical includes Medicare premiums
  and LTC up to a cap — boundary `health-insurance` decision 8).
  Asset classes have different tax-drag profiles — bonds throw
  off ordinary-income coupon interest (highest drag in taxable),
  REITs throw off non-qualified dividends, US-stock index funds
  throw off mostly qualified dividends and very little realized
  gain, international funds may have foreign-tax-credit-
  recoverable withholding (only recoverable in taxable, lost in
  IRA). The optimization places highest-tax-drag assets in the
  highest-tax-shielding accounts. Distinct from decision 4
  (overall allocation %) and decision 6 (within-taxable harvesting).
- **Framing-axes-covered**: bonds-in-tax-deferred-stocks-in-
  taxable-rule-and-its-exceptions (classic Bogleheads guidance;
  bonds throw off ordinary-income coupon — keep in traditional
  401(k) where the ordinary-tax treatment matches the eventual-
  distribution treatment anyway; stocks in taxable for the LTCG-
  rate + step-up-at-death asymmetry; BUT — exceptions: at very
  low projected-retirement-tax-rates the calculus inverts;
  munis are tax-free already so go in taxable; tax-managed
  funds blur the distinction; this rule is the right default
  but not load-bearing in all configurations), Roth-as-highest-
  expected-return-asset-bucket (Roth has no future tax — placing
  the highest-expected-return assets there maximizes the tax-
  free-out value; small-cap-value / emerging-markets / equity-
  premium-heavy / venture-style assets belong in Roth IF the
  user holds them at all, vs traditional where the future-tax
  drag is bigger on bigger growth), HSA-as-stocks-not-cash
  (the HSA-as-medical-emergency-fund framing keeps HSA in cash
  / MMF and forfeits the triple-tax-advantage growth — for users
  who can pay current medical OOP, HSA should be invested in
  index funds and let to compound, with receipts saved to
  reimburse any time in the future at zero tax; this is the
  HSA-as-stealth-IRA strategy and is the single highest-leverage
  asset-location move available, boundary `health-insurance`),
  taxable-account-asset-selection-for-tax-efficiency (broad-
  market index funds and ETFs have lower realized-distribution
  drag than active funds and target-date funds — target-date
  funds in particular are tax-inefficient in taxable because
  they auto-rebalance via realized capital gains; never hold
  target-date in taxable), international-stocks-and-foreign-
  tax-credit (15-30% of qualified dividend yield on international
  funds has foreign-tax withholding — recoverable on Form 1116
  if held in taxable, NON-recoverable if held in IRA; this is a
  weak argument to keep some international in taxable, often
  overstated relative to the bonds-in-tax-deferred rule), REITs-
  and-MLPs-in-tax-advantaged-only (REITs throw off non-qualified
  dividends taxed at ordinary rates; MLPs generate K-1s and UBIT
  if held in IRA — neither belongs in taxable in most cases;
  REIT in IRA is the cleanest), step-up-in-basis-at-death-
  shapes-taxable-priority (taxable assets get cost-basis-step-
  up at owner's death — heirs inherit at fair-market-value
  basis with $0 capital gains realized; the doubled estate-tax
  exemption sunset in 2026 changes the calculus for HNW estates;
  the step-up alone is a strong reason to hold appreciated
  long-term assets in taxable and run down tax-deferred and
  Roth first — see decision 8 for sequencing; boundary
  `family-planning` decision 10), QBI-Section-199A-pass-through-
  income-allocation (for self-employed users with pass-through
  income, the asset-location question extends to where K-1
  income lands — boundary `entrepreneurship`).
- **Sample situations**:
  - "Target 70/30 stocks/bonds across $400k 401(k), $80k Roth
    IRA, $20k HSA, $150k taxable. Where do the bonds go? What
    about the $50k I want in REITs?"
  - "Held $50k of VXUS (Vanguard total international) in my
    IRA for 5 years. Should it have been in taxable for
    foreign-tax-credit recovery — and if so, is there a
    repositioning move now or is the FTC water under the
    bridge?"
  - "HSA at Fidelity, $40k balance, 100% in cash because spouse
    treats it as medical emergency fund. We've never withdrawn
    from it in 8 years. Worth moving to FZROX equivalent and
    paying current medical OOP, or keep cash as buffer?"

## 4. Brokerage asset allocation and glide path

- **Scope**: Setting the household target asset allocation — the
  percentage split across asset classes (US stocks, international
  stocks, bonds, alternatives, cash) — and the glide path
  (how the allocation shifts with age toward more bonds /
  conservative). Decision is the strategic-level allocation choice
  for the entire household portfolio across all accounts;
  decision 3 then implements the allocation across specific
  accounts. Distinct from decision 3 (asset location) and
  decision 6 (tax-loss harvesting within an allocation). Three
  implementation frames compete: (a) target-date fund — fully
  automated single-fund glide path (Vanguard / Fidelity /
  Schwab / TIAA all have free or near-free options); (b) 3-fund
  portfolio — US-total, international, US-bond, manually
  rebalanced (the classic Bogleheads option); (c) DIY
  multi-fund — small-cap-value tilt, international-small,
  REIT slice, TIPS slice. Cross-routes `tech-career` (RSU
  concentration risk — a tech employee with 30% of net worth
  in single-company stock has a "stealth-allocation" that
  swamps any chosen target-allocation; sell-and-diversify-
  on-vest framing is the load-bearing move here).
- **Framing-axes-covered**: age-in-bonds-vs-100-minus-age-vs-
  longer-life-glide-paths (rule-of-thumb glide paths; "age in
  bonds" is too conservative for most modern 30+-year retirement
  horizons; "120-minus-age" is more reflective of equity-
  required-for-longevity-risk; target-date-fund glide paths
  vary sharply across providers — Vanguard 2055 holds ~90%
  equity, T.Rowe-Price 2055 holds ~98% equity, BlackRock
  LifePath 2055 holds ~96% — these are not interchangeable;
  verify the specific glide-path before committing), passive-
  index-vs-target-date-vs-DIY-3-fund (target-date-fund is the
  zero-friction default for a single retirement account but
  is tax-inefficient in taxable due to auto-rebalancing
  realizations — see decision 3; 3-fund-portfolio is the
  cost-of-rebalancing-yourself for a small expense-ratio and
  tax-efficiency gain in taxable; DIY-multi-fund is the next
  step up in complexity, justifiable for HNW or specific
  tilts), small-cap-value-tilt-and-Fama-French-factor-
  premium-evidence (the academic literature is split on
  whether SCV / international-small / momentum / quality
  factor tilts add expected return net of cost over a 30-year
  horizon; the Fama-French 3-factor and 5-factor research
  supports small + value premia historically; subsequent
  papers question robustness; the user should hold the tilt
  ONLY if they can stick with it through multi-year drag
  periods relative to S&P 500 — behavioral discipline
  dominates the factor premium, see decision below on
  behavior), international-allocation-home-bias-and-the-
  global-cap-weight (US-only investors hold a "home-bias"
  position equivalent to a 100% US-cap-weight bet; global-
  market-cap is ~60% US / 40% international; recommended
  ranges from 0% international (Buffett, Bogle) to 40%+
  (Vanguard target-date); the diversification argument is
  stronger for international-small + emerging than for
  international-developed-large, which correlates 0.8+ with
  US over multi-year periods), bond-allocation-duration-and-
  yield-curve-position (within-bonds: short / intermediate /
  long duration, Treasury / corporate / TIPS / muni; rising
  rate environments crush long-duration bond values — held
  intermediate-Treasury matches typical retirement-spending
  horizon and avoids credit risk; TIPS hedge inflation
  explicitly; munis are tax-shielded in taxable for high-
  bracket users), behavioral-discipline-and-stay-the-course-
  premium (the gap between fund-return and investor-return
  ("behavior gap") averaged ~2-3% annually in DALBAR studies
  — selling at lows and buying at highs is the single
  biggest destroyer of long-term return; any allocation the
  user CANNOT hold through a -50% drawdown is the wrong
  allocation regardless of theoretical optimum), RSU-and-
  ESPP-concentration-risk-as-stealth-allocation (a tech
  employee with $400k in vested RSU + $80k in ESPP-discounted
  stock has effectively a $480k single-stock concentrated
  position that overwhelms most household allocations; the
  generic "diversify" advice obscures the more specific
  framing — sell-on-vest is tax-neutral for RSU because
  vesting is already a taxable event at ordinary rates; for
  ESPP the disqualifying-disposition vs qualifying-disposition
  math complicates the immediate-sell call; boundary
  `tech-career`).
- **Sample situations**:
  - "30yo target 90/10 stocks/bonds. Considering Vanguard
    Target Retirement 2060 (90/10 default) vs DIY 3-fund
    (VTI / VXUS / BND). What's the actual difference over
    30 years, accounting for tax-drag and rebalancing?"
  - "45yo holding $700k vested RSU in current employer, $1.2M
    in 401(k) + Roth at 80/20. Target-allocation says 70/30,
    but the RSU concentration says I'm at 95/5 effective
    equity. Sell RSU now to rebalance, hold for capital-gains-
    rate (already past 1-yr LTCG), or hedge with put options?"
  - "60yo, $2M portfolio, retiring in 5 years. Glide path
    says I should be 60/40 now and 50/50 by retirement. But
    longevity is 30+ years post-retirement — am I overly
    conservative? Bond-tent / equity-glide / static-allocation?"

## 5. Debt-payoff vs invest prioritization

- **Scope**: Household with both (a) outstanding debt at various
  rates (credit card 18-29%, student loan 4-8%, auto 6-10%,
  mortgage 3-7%, HELOC / portfolio-margin 5-10%) and (b) the
  capacity to either accelerate debt payoff or contribute to
  investment / retirement accounts (decision 1's pipeline).
  Decision is the dollar-by-dollar allocation between these
  two destinations; classic framing compares debt-rate
  (after-tax-effective) vs expected-investment-return (after-
  tax-effective) and routes to whichever is higher. The
  framing is right on average but misses several second-
  order factors that flip the recommendation in specific
  cases. Distinct from decision 1 (which captures the high-
  interest-debt step in the priority ordering) but the deeper
  framing of when "high interest" applies lives here. Cross-
  routes `education-funding` (student-loan-PAYE / SAVE / IDR
  forgiveness changes the after-tax-effective rate sharply —
  on PSLF-track, the "after-tax-effective rate" is near-zero
  because the balance will be forgiven; never accelerate a
  PSLF-eligible loan), `housing` (mortgage-payoff vs invest
  is a special case with tax-deduction-loss + liquidity-cost
  + emotional-security-of-paid-off-house framing; cash-out
  refi / HELOC as alternate financing source), `tech-career`
  (vested-RSU-as-debt-paydown-source is mechanically simple
  but tax-inefficient — selling appreciated RSU triggers
  realized cap gain).
- **Framing-axes-covered**: after-tax-effective-debt-rate-vs-
  after-tax-expected-investment-return (the core arithmetic;
  18% credit card debt is 18% after-tax-effective because
  the interest is non-deductible; 6.5% student loan is
  ~5.4% after-tax-effective if user can deduct (income-
  capped); 6% mortgage is ~4.6% after-tax-effective if user
  itemizes AND under SALT-cap limits; compare against
  ~7% expected real S&P 500 return after-tax-of-LTCG-and-
  dividends or ~5% after-tax-bond-equivalent — credit card
  always wins on payoff side, mortgage often wins on invest
  side, student-loan-and-auto is the contested middle),
  student-loan-PAYE-SAVE-IDR-PSLF-changes-the-rate-to-near-
  zero (IDR plans cap monthly payment at 5-20% of discretionary
  income with forgiveness at 20-25 years; PSLF forgives at
  10 years for qualifying public-service employment; on
  these plans the effective-payment-rate-relative-to-balance
  is decoupled from the loan APR, and the optimization is
  AGI-minimization, not balance-paydown; aggressive
  refinance-to-private-loan during the wrong policy moment
  destroys forgiveness eligibility — boundary
  `education-funding`), psychological-debt-burden-and-Dave-
  Ramsey-snowball-vs-avalanche (the "math-optimal" avalanche
  pays highest-rate first; the "behavioral-optimal" snowball
  pays smallest-balance first for the win-momentum effect;
  for users at risk of giving up on a multi-year payoff
  plan, snowball can dominate avalanche in actual-delivered
  result; rule-out psychology is wrong here), employer-match-
  beats-everything-except-payday-loan (the 100% immediate
  return on a 401(k) match dollar dominates even 25% APR
  credit card debt over any sensible horizon; the only debt
  rate that beats match is payday-loan / overdraft 200%+
  effective — never skip match to pay debt unless it's
  the rare payday-loan-class debt), mortgage-payoff-vs-
  invest-emotional-and-tail-risk-framing (mortgage payoff
  is a guaranteed after-tax return at mortgage-rate; invest
  is expected-return with variance; for retirees or near-
  retirees facing sequence-of-returns risk, paying off
  mortgage reduces fixed cash-flow obligation and is a
  tail-risk hedge worth the suboptimal-mean — math says
  invest, behavior+sequence-risk says payoff, the right
  answer depends on the household's other liquidity),
  HELOC-and-cash-out-refi-and-margin-loan-as-alternate-
  financing (rather than paying off debt with cash, refinance
  expensive debt into cheap debt — credit-card-debt-into-
  HELOC at 8% vs 22% is a $14% spread on the balance,
  same household-savings-rate but vastly faster paydown;
  cash-out-refi at 6% to invest at 7% is rate-arbitrage
  that requires the user to stick with the strategy through
  2009-style drawdowns; margin-loan-against-portfolio at
  prime+1 is similar arbitrage with margin-call-risk on
  drawdown — boundary `housing`), tax-deductibility-vs-non-
  deductibility (student loan interest deductible up to
  $2,500 with income phase-out, mortgage interest itemizable
  with TCJA caps and SALT $10k limitation, credit card and
  auto are never deductible — the after-tax-effective rate
  calculation must account for this), QSBS-and-RSU-as-debt-
  paydown-source (selling appreciated RSU to pay off debt
  triggers ordinary-rate income on the vest-portion already
  taxed but capital-gains on subsequent appreciation; for
  QSBS-eligible founder-stock the §1202 5-year-hold for
  100%-exclusion makes "wait to sell" structurally important
  — boundary `tech-career` / `entrepreneurship`).
- **Sample situations**:
  - "$15k credit card debt at 24%, $30k student loan at
    6.5%, $400k mortgage at 4.2%. Have $30k/year extra
    above living expenses. Pay debt first or invest? Which
    debts in which order?"
  - "PSLF-track public-defender, $180k student loans at
    7%. On SAVE plan at $200/mo. Pay extra or save / invest
    the extra? What about a private-refi opportunity
    advertised at 4.5%?"
  - "$300k mortgage at 3.5% locked in pre-2022, $400k
    available in taxable brokerage. Pay off mortgage early
    for the certainty / cash-flow reduction, or keep
    invested in 60/40?"

## 6. Tax-loss harvesting and wash-sale management

- **Scope**: Within a taxable brokerage account, harvesting
  losses on positions trading below cost basis to offset
  realized gains and (up to $3k/year) ordinary income, while
  navigating the wash-sale rule's 30-day-before-and-after
  prohibition on buying a "substantially identical" security
  in any account (including the user's IRA and spouse's
  accounts under the household-aggregation rule). Decision is
  twofold: (a) WHEN to harvest (mechanical — late-year
  cleanup, intra-year on drawdowns, or continuous via robo-
  advisor), (b) HOW to harvest cleanly (ETF-pair-substitution
  to maintain market exposure without wash-sale, account
  segregation to avoid spousal-IRA cross-pollination). Cross-
  routes `entrepreneurship` (QSBS sale gains can absorb
  unlimited losses for the non-QSBS portion of the same
  year), and to `legal-disputes` when joint-account-on-
  divorce creates wash-sale traps mid-divorce.
- **Framing-axes-covered**: $3,000-ordinary-income-offset-
  and-unlimited-carryforward (TLH losses offset realized
  gains dollar-for-dollar; net losses up to $3,000 offset
  ordinary income annually; the rest carries forward
  indefinitely until used — accumulated TLH banking is real
  value, treat it as a permanent asset on the personal-
  balance-sheet), wash-sale-30-day-before-and-after-and-
  substantially-identical-test (you cannot buy a
  "substantially identical" security 30 days before or after
  realizing the loss in ANY account — including spouse's IRA
  per IRS Pub 550 and Rev Rul 2008-5; the substantially-
  identical test is judgment-call territory — VOO and IVV
  tracking the same S&P 500 index are NOT considered
  substantially identical per long-standing practice, but
  VOO and VFIAX share underlying portfolio and ARE
  substantially identical; double-check ETF-pair
  substitutions before relying on them), ETF-pair-
  substitution-table (the standard TLH pairs: VTI ↔ ITOT;
  VOO ↔ IVV; VXUS ↔ IXUS; BND ↔ AGG; VTV ↔ IUSV — each pair
  tracks similar but not identical indices, both
  high-volume, low-expense; rotation among 3+ pairs across
  multiple harvest cycles avoids "always selling the same
  fund into the same fund" which the IRS has not challenged
  but cleaner to vary), spousal-IRA-wash-sale-trap (a
  loss-harvested fund repurchased in spouse's IRA within
  30 days IS a wash-sale per Rev Rul 2008-5 — the loss is
  permanently lost into the IRA's basis where it cannot be
  recovered; this is the single most expensive TLH mistake
  and is missed when robo-advisors don't have visibility
  into spouse's accounts; coordinate household-wide before
  enabling automatic-TLH-robo on one spouse's taxable),
  robo-advisor-automatic-TLH-vs-manual (Wealthfront,
  Betterment, Schwab Intelligent Portfolios all offer
  automatic daily-or-weekly-TLH; the value-add over manual-
  annual-harvesting is real but modest — academic estimates
  range 0.2-0.6% / year of after-tax-alpha; verify the robo's
  pair-substitution list is reasonable; verify the robo's
  visibility into your held-away accounts to avoid spousal-
  IRA traps), tax-gain-harvesting-as-the-reverse (in 0%-LTCG
  years — typically retirees or sabbatical years with low
  income — REALIZING gains at 0% federal rate and
  immediately rebuying resets basis upward without tax;
  no wash-sale rule on the gain side; underutilized; boundary
  decision 7 on Roth-conversion-ladder timing),
  short-term-vs-long-term-loss-character-and-ordering
  (short-term losses offset short-term gains first;
  long-term losses offset long-term gains first; net any
  excess goes against the other character — keep losses
  matched to gains by character when possible; for users
  with concentrated single-stock positions, holding-period-
  management before sale matters), wash-sale-extends-to-
  options-and-substantially-similar-derivatives (buying
  calls on a security within 30 days of harvesting the
  underlying triggers wash-sale; "buying-back" via deep-
  ITM calls is a known IRS-litigated trap; not all
  derivatives substantially-identical but caution-warranted),
  end-of-year-mutual-fund-capital-gains-distribution-trap
  (mutual funds distribute realized cap gains in November-
  December based on year-long internal turnover; buying a
  fund in late October and receiving a 10% capital-gain-
  distribution in November is a "buy a tax bill" — verify
  the fund's estimated distribution before purchase in
  late-year, or wait until after ex-div date).
- **Sample situations**:
  - "Held VTI in taxable for 3 years, currently down 12%
    on $40k cost basis. Have $5k of realized short-term
    gain from a sale earlier in the year. Harvest the VTI
    loss into VOO? Wait for end-of-year? What about my
    spouse's Vanguard IRA which holds VTSAX?"
  - "Have $80k of accumulated TLH carryforward built up
    over 5 years. Now have $300k QSBS-Section-1202 gain
    coming on an acquisition. Does the TLH offset apply
    before or after the §1202 exclusion?"
  - "Robo-advisor (Wealthfront) running automatic TLH on
    my taxable. Spouse just rolled over old 401(k) into a
    new IRA holding VTI. Set up wash-sale risk — how to
    coordinate without giving up either the robo-TLH or
    the spouse's preferred fund?"

## 7. Roth conversion ladder in low-income years

- **Scope**: Person facing a transient low-income year — job
  loss, sabbatical, early-retirement bridge before age-65
  Medicare, business-loss year, NOL carryforward year —
  executing a Roth conversion that moves dollars from
  traditional 401(k) / IRA into Roth IRA at the low marginal
  rate of the current year, rather than paying the higher
  expected-future rate at RMD-time. Decision spans the
  CONVERSION-AMOUNT sizing (filling up specific brackets
  without crossing tier boundaries), the ACA-subsidy-and-
  IRMAA interactions, the 5-year-clock on each converted
  amount (each Roth-conversion has its own 5-year-aging clock
  for penalty-free withdrawal of the converted amount), and
  the recharacterization-elimination caveat (TCJA 2017
  eliminated the prior ability to undo a Roth conversion —
  it's now irrevocable from the moment executed). Distinct
  from decision 2 (within-year traditional-vs-Roth split at
  contribution time) and decision 8 (withdrawal sequencing
  in retirement). Cross-routes `tech-career` (sabbatical
  windows are the highest-leverage Roth-conversion year for
  current-employees), `health-insurance` (ACA-subsidy MAGI
  management and IRMAA-2-year-lookback on Medicare premiums
  — converting too much pushes 2026-conversion-MAGI into
  2028-IRMAA tier), and `entrepreneurship` (business-loss
  years and NOL-carryforward years).
- **Framing-axes-covered**: bracket-filling-arithmetic-12pct-
  to-22pct-jump-and-22pct-to-24pct-jump (federal bracket
  rates step at $11,925 / $48,475 / $103,350 / $197,300 /
  $250,525 / $626,350 for 2025 single; sizing a Roth
  conversion to fill exactly to the top of a bracket
  without spilling into the next is the central optimization
  — converting $40k into the 12% bracket and stopping is
  often dominant over converting $100k that spills into
  22% at the margin; for HCOL-state retirees the state
  bracket also matters), pro-rata-rule-on-conversion-when-
  pre-tax-IRA-balance-exists (every Roth conversion from a
  traditional-IRA is partially taxable based on the pro-rata
  share of basis-to-total-balance; the form 8606 calculation
  treats all traditional / SEP / SIMPLE IRAs as one pool;
  401(k)-to-Roth-401(k) conversions (in-plan-Roth-rollover)
  do NOT trigger pro-rata across IRAs, which is a clean way
  to convert without IRA aggregation), 5-year-clock-per-
  conversion-and-age-59.5-rule (each Roth-conversion-amount
  has its own 5-year-aging-from-Jan-1-of-conversion-year
  clock for penalty-free withdrawal of the converted
  principal; the 5-year clock is separate from the 5-year-
  clock-on-Roth-IRA-itself which runs from first-contribution-
  year; both apply, take the longer; over age 59.5, the
  10%-penalty no longer applies but the 5-year-clock for
  earnings-withdrawal-tax-free still does), IRMAA-Medicare-
  surcharge-2-year-lookback (IRMAA tiers based on MAGI 2
  years prior — a Roth conversion in 2025 affects 2027
  Medicare Part B + Part D premiums; the IRMAA cliffs at
  $103k / $129k / $161k / $193k / $500k+ single MAGI in
  2025 step up sharply, $1k–4k per tier; for retired
  conversions, conversion-sizing should specifically target
  the top of the current IRMAA tier — boundary
  `health-insurance`), ACA-subsidy-cliff-pre-Medicare (early-
  retirees on ACA marketplace face the APTC subsidy phase-
  out; a Roth conversion that pushes MAGI past the 400%-FPL
  cliff (if reinstated after ARPA expiration) destroys the
  subsidy — net cost of the conversion is the implicit-tax
  + lost-subsidy; verify current subsidy schedule —
  boundary `health-insurance` decision 5), NOL-carryforward-
  and-business-loss-years-as-free-Roth-conversion-headroom
  (a Schedule-C loss carrying forward an NOL absorbs Roth-
  conversion income up to the NOL amount at $0 federal —
  the conversion is genuinely free of income tax; commonly
  missed by self-employed; boundary `entrepreneurship`),
  recharacterization-no-longer-available-since-TCJA-2017
  (pre-2018, a Roth conversion could be undone via
  recharacterization until Oct-15-of-following-year; TCJA
  permanently eliminated recharacterization for conversions;
  conversions are now irrevocable — size carefully and
  conservatively at year-start, fund mid-year as income
  becomes clearer, NOT all at January-1), surviving-spouse-
  filing-status-trap (a married couple in low-bracket
  conversion-window loses MFJ status the year after a
  spouse's death and reverts to single-filer brackets — the
  brackets shrink dramatically, especially the high-end
  cliffs; this is an underappreciated reason to accelerate
  conversions during MFJ years when one spouse's health is
  declining; boundary `family-planning`).
- **Sample situations**:
  - "62yo retired in 2025, bridging to Medicare at 65 on
    ACA marketplace. $1.4M traditional IRA, $200k Roth.
    Plan to convert $50k / year for 3 years. Sizing right
    given ACA subsidy phase-out and 2027 IRMAA lookback?"
  - "55yo on sabbatical year — earned income $30k from
    consulting, no W-2. Have $800k traditional 401(k)
    from former employer. Roll into IRA and convert
    aggressively this year, or stay in 401(k) and convert
    via in-plan-Roth-rollover (if plan allows)?"
  - "Self-employed earning $40k Schedule-C net with $80k
    NOL carryforward from a prior business loss. $300k
    in pre-tax SEP-IRA from earlier career. Convert
    $80k to Roth-IRA this year to use up the NOL? What
    about backdoor Roth simultaneously?"

## 8. Retirement withdrawal sequencing and RMD planning

- **Scope**: Retired or near-retired person sequencing
  withdrawals across taxable / tax-deferred / Roth / HSA
  buckets to fund retirement spending while minimizing
  lifetime tax. Decision spans the WITHDRAWAL-ORDERING
  rule of thumb (taxable first, then tax-deferred, then
  Roth — preserves the tax-free-compounding longest), the
  RMD-mandated minimum from tax-deferred starting at age
  73 / 75, Social-Security claim-age coordination at 62 /
  FRA / 70, and the qualified-charitable-distribution
  (QCD) opportunity to satisfy RMD up to $108k/year (2025
  indexed) by direct charity-transfer with no income
  inclusion. Distinct from decision 7 (pre-retirement
  Roth conversions setting up the withdrawal landscape)
  and decision 10 (estate-and-beneficiary side). Cross-
  routes `health-insurance` (HSA-as-Medicare-premium-
  payment in retirement is qualified medical use with
  zero tax; IRMAA management via withdrawal sequencing),
  `housing` (Section-121 primary-residence cap-gains-
  exclusion frees up to $250k / $500k single / MFJ tax-
  free upon sale; reverse-mortgage as supplement vs not),
  and `family-planning` (QCD-vs-itemized-deduction-on-
  large-charitable-gift; surviving-spouse-filing-status
  trap one year after spouse's death).
- **Framing-axes-covered**: taxable-first-tax-deferred-
  second-Roth-last-default (the conventional ordering
  preserves Roth tax-free-compounding the longest while
  using up taxable assets first; works well for users
  with moderate tax-deferred balances; for HNW with
  $5M+ in traditional 401(k), the default ordering is
  suboptimal because RMDs balloon the tax-deferred
  bucket — see Roth-conversion-ladder decision 7 to
  preempt), Social-Security-claim-age-62-vs-FRA-vs-70-
  arithmetic (claiming at 62 reduces PIA permanently
  ~30%; FRA at 67 (born 1960+) is unreduced; delaying
  to 70 increases PIA 8% / year via Delayed Retirement
  Credits — break-even is around age 80 for self-only;
  for higher-earning spouse in a couple, delaying to 70
  also locks in the higher survivor-benefit which the
  lower-earning survivor receives for life — this
  spousal-survivor-coordination math often dominates
  the self-only break-even and is widely under-modeled;
  underutilized — boundary `family-planning`), RMD-
  age-73-or-75-mechanics-and-25%-penalty-on-missed
  (RMD age is 73 under SECURE 2.0 (rises to 75 for
  those who turn 74 in 2033+); the IRS-uniform-lifetime-
  table divisor sets the minimum; missing an RMD
  triggers a 25%-of-shortfall-penalty (reduced from 50%
  by SECURE 2.0), reducible to 10% if corrected within
  2 years via Form 5329 — never ignore, fix promptly),
  qualified-charitable-distribution-QCD-from-IRA (age
  70.5+ can transfer directly from IRA to qualified
  charity up to $108k/year 2025 indexed; the QCD
  satisfies RMD with NO income inclusion, vs taking
  RMD and itemizing the charity gift which doesn't
  benefit those taking standard deduction; for users
  who would otherwise take standard deduction, QCD is
  pure-additive tax savings; the donor-advised-fund
  bunch-and-fund framing is the alternative for users
  who itemize anyway — boundary `family-planning`),
  HSA-as-tax-free-medical-and-Medicare-premium-payer
  (in retirement, HSA dollars pay Medicare Part B + D
  + Medigap premiums (NOT Medicare Advantage premiums)
  and qualified long-term-care insurance premiums up
  to age-indexed caps as tax-free distributions —
  this is one of the highest-leverage uses of an HSA
  built up via decision 1 / decision 3; boundary
  `health-insurance` decision 8), provisional-income-
  and-SS-taxability-staircase-management (SS becomes
  50% or 85% taxable as provisional income crosses
  $25k / $34k single / $32k / $44k MFJ — NOT inflation-
  indexed since 1983; managing withdrawals to keep
  provisional income below these thresholds preserves
  the 0%-tax-on-SS band; Roth withdrawals don't count
  toward provisional income, traditional and capital-
  gains do), sequence-of-returns-risk-and-bond-tent-
  vs-equity-glide (early-retirement-year market
  drawdowns combined with portfolio-withdrawals are
  the canonical SoR-risk failure mode that destroys
  30-year retirement plans; bond-tent (temporarily
  increase bond allocation in years 0-5 of retirement)
  and rising-equity-glide (start at 60/40, rise to
  80/20 by year 10) both mitigate but are
  counterintuitive — most retirees do the opposite;
  the academic literature (Pfau-Kitces 2014) supports
  both), Section-121-primary-residence-capital-gains-
  exclusion-on-downsize (selling primary residence
  after 2-of-5-year-ownership excludes $250k single /
  $500k MFJ of gain — funds first 1-5 years of
  retirement spending tax-free; for HCOL retirees with
  $1M+ home appreciation the exclusion is only partial
  and gains above the limit are taxable at LTCG rates;
  boundary `housing`), reverse-mortgage-and-HECM-line-
  of-credit-as-buffer-asset (HECM line-of-credit grows
  at the loan-rate annually, providing a non-depleting
  bucket to draw from in market-drawdown years instead
  of selling depressed equities; the Federal-Trade-
  Commission HECM disclosures and counseling
  requirements add procedural friction but the
  strategy is well-modeled academically; underutilized
  per Pfau research — boundary `housing`), surviving-
  spouse-filing-status-and-bracket-compression-year-2
  (in the year of one spouse's death, MFJ filing
  status applies; thereafter the survivor reverts to
  single-filer brackets — same income lands in
  meaningfully higher brackets; accelerate any planned
  Roth-conversion or large taxable-realization into
  the final MFJ year if one spouse's death is
  foreseeable; sensitive framing — boundary
  `family-planning`).
- **Sample situations**:
  - "65yo retiring, $400k taxable, $1.6M traditional
    401(k), $300k Roth, $80k HSA. Plan to draw $90k/year
    pre-SS-claim. Sequence — taxable first, or carve
    out HSA for Medicare premiums? Claim SS at 65 or
    delay to 70?"
  - "75yo, RMD this year is $65k from traditional IRA.
    Income otherwise $50k from SS + small pension. Tithe
    $30k/year to church. Use QCD to satisfy $30k of
    RMD vs take RMD and itemize church-gift?"
  - "Surviving spouse, husband died Feb 2025. MFJ in 2025
    last time. Have $80k accumulated taxable-bracket-
    fill-up Roth-conversion plan started in 2024.
    Accelerate remaining $50k into Dec 2025 or stick
    with original plan?"

## 9. College funding mix — 529 vs Roth vs taxable

- **Scope**: Parent / grandparent saving for child's higher-
  education funding, choosing among 529 plans (state-sponsored,
  in-state-tax-deduction-or-credit vs out-of-state-no-tax-
  benefit), Coverdell Education Savings Accounts (ESA),
  Roth-IRA-as-college-substitute, UGMA / UTMA custodial
  accounts (taxed at kiddie-tax rates), and plain taxable
  brokerage in parent's name. Decision spans the SAVINGS-
  VEHICLE choice, the OWNERSHIP-structure (parent vs
  grandparent vs custodial — affects FAFSA Expected Family
  Contribution calculation differently), the funding pace
  (front-loading 5-year-election lump sum vs annual
  contributions), and the SECURE 2.0 §529-to-Roth-IRA
  rollover mechanic (up to $35k lifetime per beneficiary
  rolled to Roth IRA after 15-year-old-529 — verifies the
  "trapped 529" anxiety that previously deterred over-
  funding). Distinct from decision 1 (where 529 falls in
  the contribution ordering priority — typically after
  retirement caps because retirement-first-college-second
  is the airline-oxygen-mask framing). Cross-routes
  `education-funding` (the deeper decision-set on
  student-loan vs in-state-vs-OOS / merit-aid / IDR /
  PSLF / refinance) and `family-planning` (grandparent-
  owned 529 FAFSA-treatment, kiddie-tax on UTMA, 5-year-
  election as estate-planning gift).
- **Framing-axes-covered**: 529-state-tax-deduction-or-
  credit-vs-out-of-state-flexibility (30+ states offer
  tax deduction or credit for 529 contributions, but
  some only for the in-state plan; the state-tax
  benefit is typically 5-10% of contribution, real but
  modest; non-tax-state residents (TX, FL, WA, etc.)
  face no in-state advantage and can pick the best
  plan nationally — Utah, NY, Nevada are commonly
  cited; verify the user's state's specific plan and
  carry-forward rules), 529-investment-options-and-
  age-based-glide-path (529 plans offer age-based
  glide-path-portfolios that auto-shift from equity to
  bond as the beneficiary approaches college age;
  glide paths vary by plan — Utah's Vanguard plan has
  a moderate glide, others are more conservative;
  pick based on glide-path-aggressiveness and expense-
  ratio), Roth-IRA-as-college-substitute-Pre-SECURE-
  2.0-rationale (pre-SECURE-2.0 the argument was:
  Roth-IRA principal is withdrawable penalty-free
  anytime and tax-free; if not used for college,
  remains as retirement savings — strictly more
  flexible than 529; SECURE 2.0's 529-to-Roth
  rollover ($35k lifetime, 15-year-old-529, $7k/year
  cap) partially closes this gap but the flexibility
  argument for using Roth-as-college-savings is
  weakening), kiddie-tax-on-UGMA-UTMA-after-age-19-or-
  24-still-a-student (TCJA-revised kiddie-tax taxes
  unearned income on under-19 (or under-24 student)
  at the trust-and-estate rate which compresses to
  37% above ~$15k; UTMA assets count against FAFSA
  as the student's own asset (20% EFC-rate) vs
  parent's 5.6%; high-cost-of-flexibility for UTMA
  vs 529 in most cases; UTMA was the right vehicle
  in the 1990s, the wrong vehicle now), 5-year-
  election-superfunding-as-estate-tax-move ($19k/year
  gift exclusion in 2025 × 5 = $95k single, $190k
  MFJ as a one-time front-load to a 529 with no gift-
  tax filing, no estate inclusion if donor survives
  5 years; useful for grandparent-funded 529 plans
  in 2025 just before the 2026 estate-tax-exemption
  sunset; boundary `family-planning` decision 10),
  529-to-Roth-rollover-SECURE-2.0-mechanics (up to
  $35k lifetime per beneficiary, account must be 15+
  years old, contributions in last 5 years not
  eligible, $7k/year Roth-IRA cap applies, beneficiary
  must have earned income equal to the rolled amount;
  closes the "what if my kid doesn't go to college"
  trap that previously deterred overfunding; still
  cleaner to right-size the 529 from the start),
  grandparent-owned-529-FAFSA-treatment-post-2024
  (FAFSA Simplification Act eliminated the previous
  grandparent-529-distribution-as-student-income
  trap; grandparent-owned 529s no longer count against
  FAFSA in any year — this is a sharp recent change
  many advisors haven't internalized; grandparent-
  funded is now optimal for high-aid-likelihood
  students), tuition-and-fees-vs-room-and-board-vs-K-
  12-qualified-expenses (qualified-529 expenses
  include tuition, fees, room+board (capped at
  cost-of-attendance), books, computer, but NOT
  transportation, health insurance, or extracurriculars;
  529-for-K-12 up to $10k/year tuition was added by
  TCJA but state-tax-benefit treatment varies by
  state, NY clawback applies on K-12 distributions
  of state-tax-deduction-claimed contributions —
  verify state rules), in-state-vs-OOS-and-merit-
  aid-tradeoffs (deeper framing in
  `education-funding`; flagged here because the
  decision on 529-balance to accumulate depends
  on the expected-cost path — full-pay private $400k
  vs in-state-public-merit $80k — same 529 saved
  amount has very different "right-sized" target).
- **Sample situations**:
  - "Kid born 2025, parents both 32 earning $250k
    combined. Open 529 now and superfund $190k via
    5-year-election? Or contribute Roth IRA up first?
    Or both? What's the right 529 balance target for
    college in 2043?"
  - "Kid is 17, accepted to in-state-public, total
    COA $80k. 529 has $40k. Other parent's UTMA has
    $25k. Spend 529 first or UTMA first? Which
    spending order minimizes total tax and maximizes
    aid eligibility?"
  - "Grandparents want to fund $50k toward
    grandchild's college. Open grandparent-owned 529
    (post-FAFSA-Simplification) vs gift directly to
    parent's 529 vs pay tuition directly to
    institution (gift-tax-exclusion)? Which optimizes
    aid + estate-tax considerations given the 2026
    exemption sunset?"

## 10. Estate-and-beneficiary structuring

- **Scope**: Aligning beneficiary forms across all account
  types (401(k), IRA, Roth IRA, HSA, life insurance,
  brokerage TOD / POD, bank POD, real-estate-transfer-on-
  death deeds where state-permitted) to ensure smooth
  intergenerational transfer at death, while sizing
  estate-tax-exposure given the doubled-exemption-sunset.
  Decision spans the BENEFICIARY-FORM AUDIT (forms
  supersede the will — a stale ex-spouse on a 401(k)
  beneficiary form overrides a current spouse named in
  the will; Egelhoff v. Egelhoff Supreme Court settled
  this for ERISA-plans, similar treatment for IRAs and
  insurance), the BASIS-STEP-UP-AT-DEATH planning (assets
  in taxable get FMV-basis reset at death — heirs realize
  $0 of gain on inherited appreciated assets — favoring
  hold-don't-sell-during-life for highly-appreciated
  taxable; conversely, traditional-IRA-and-401(k) get
  NO basis-step-up; Roth gets no basis-step-up but
  remains tax-free), and the SECURE 1.0 10-YEAR-RULE on
  inherited IRAs (non-spouse-beneficiaries inheriting a
  retirement account in 2020+ must distribute the full
  balance within 10 years — eliminates the prior
  "stretch IRA" lifetime distribution; modest annual
  RMDs may also apply under final SECURE regs for
  non-eligible-designated-beneficiaries inheriting from
  someone past their own RBD). Cross-routes
  `family-planning` (the entire estate-planning side —
  trusts, prenups, blended-family beneficiary
  coordination), and `legal-disputes` (will-contests,
  intestacy disputes, ERISA-plan-beneficiary-form-
  challenge claims).
- **Framing-axes-covered**: beneficiary-forms-supersede-
  the-will-and-Egelhoff (Egelhoff v. Egelhoff 532 US
  141 (2001) — ERISA-plan beneficiary form controls
  even when state law (community property,
  divorce-revocation-statute) would say otherwise; most
  IRA custodians and insurance companies follow the
  same rule; checking and updating beneficiary forms
  after marriage / divorce / birth / death is the
  single highest-leverage estate-planning act and is
  routinely neglected — a stale ex-spouse on a 401(k)
  form is the canonical horror story; audit annually
  at minimum, and at every life event), per-stirpes-
  vs-per-capita-beneficiary-designation-and-
  contingent-beneficiaries (default beneficiary forms
  ask for primary + contingent — name BOTH; per-stirpes
  designates that a predeceased beneficiary's share
  flows to their descendants (the typical preferred
  outcome for a parent-naming-children-and-
  grandchildren); per-capita reallocates among
  surviving beneficiaries — most providers default to
  one but allow election; verify the form's exact
  language), spousal-rollover-vs-inherited-IRA-vs-
  10-year-rule-for-non-spouse (a surviving spouse can
  ROLL OVER an inherited IRA into their own IRA — gets
  the spouse's own age for RMD purposes, can convert
  to Roth, has full flexibility; a non-spouse
  beneficiary cannot roll over — must take as
  Inherited-IRA, subject to SECURE 1.0 10-year-rule;
  eligible-designated-beneficiaries (EDBs — minor child
  of decedent up to age of majority, disabled,
  chronically ill, less-than-10-yr-younger
  beneficiary) can stretch over their lifetime;
  non-EDBs are the 10-year-rule), basis-step-up-at-
  death-and-traditional-IRA-asymmetry (taxable
  appreciated assets get FMV basis-step-up at owner's
  death — heirs sell at $0 cap-gain immediately, OR
  hold and start the cap-gain clock fresh; traditional
  IRA / 401(k) get NO step-up — heirs inherit the
  full income-tax-deferred balance which is taxed as
  ordinary income on distribution; this asymmetry
  favors RUNNING DOWN traditional 401(k) in life and
  HOLDING appreciated taxable for heirs — the
  inverse of the conventional "taxable first"
  withdrawal sequence for users with significant
  intent-to-bequeath; under the doubled-estate-tax-
  exemption the basis-step-up is genuinely free for
  most estates), 2025-vs-2026-estate-tax-exemption-
  sunset ($13.99M-per-individual / $27.98M-MFJ
  lifetime exemption in 2025 falls to ~$7M-indexed-
  per-individual / ~$14M-MFJ in 2026 absent
  congressional extension — TCJA 2017 baked the
  sunset in; HNW pre-2026 moves: lifetime gifts up
  to the current exemption (use-it-or-lose-it),
  Spousal-Lifetime-Access-Trust (SLAT) to lock in
  current exemption, GRAT for appreciation-shifting,
  Dynasty-trust for generation-skipping; the IRS
  has confirmed via Reg §20.2010-1(c) that lifetime
  gifts using the doubled exemption will NOT be
  clawed back if the user dies post-sunset — this
  "anti-clawback" rule makes pre-sunset gifting
  permanent, which is the load-bearing reason to
  move pre-2026; verify status of any congressional
  extension before recommending — boundary
  `family-planning`), trust-as-IRA-beneficiary-only-
  with-careful-drafting (naming a trust as IRA
  beneficiary can be done but requires the trust to
  qualify as a "see-through trust" — irrevocable on
  donor's death, identifiable beneficiaries, copy
  furnished to custodian by Oct-31-following-year;
  trust-as-beneficiary is appropriate when the heir
  is a minor / disabled / financially-imprudent /
  blended-family-protection; otherwise it
  unnecessarily forces 10-year-rule even for EDB-
  eligible beneficiaries; do NOT name a trust as
  IRA beneficiary casually — boundary
  `family-planning`), TOD-POD-bank-account-and-real-
  estate-transfer-on-death-deeds (transfer-on-death
  designations on brokerage and bank accounts pass
  outside probate at death — same legal mechanism
  as retirement-account beneficiary forms; some
  states (~30) allow real-estate-transfer-on-death-
  deeds for primary residence — also outside probate;
  for users in TOD-deed states this is a powerful
  zero-cost probate-avoidance move; verify state
  permits, boundary `housing`), QDRO-on-divorce-as-
  beneficiary-form-revocation (a Qualified Domestic
  Relations Order from divorce can DIVIDE retirement
  account balances and SUPERSEDE beneficiary-form
  designations for the divided portion, but the
  REMAINING balance still flows per beneficiary form
  — so an ex-spouse named on a beneficiary form
  before divorce can still inherit the non-QDRO
  portion absent a post-divorce update; the
  "automatic-revocation-on-divorce" state laws
  exist in some states but Egelhoff held they don't
  apply to ERISA plans; ALWAYS update beneficiary
  forms post-divorce regardless of QDRO and
  regardless of state-revocation-statute; boundary
  `family-planning` / `legal-disputes`),
  creditor-protection-of-retirement-accounts-ERISA-
  vs-IRA-state-variation (ERISA-protected 401(k) is
  unlimited federal-bankruptcy-protected and
  generally judgment-proof; IRA is federal-
  bankruptcy-protected to $1.5M-indexed (per 11 USC
  522(n)) and STATE-protected to varying levels:
  Texas / Florida / Arizona unlimited, California
  only in bankruptcy and only "necessary for support",
  NY $1M, NJ $1M, etc. — for HNW users with
  litigation exposure, ROLLING from 401(k) into IRA
  on retirement WEAKENS creditor protection,
  argument for staying in the 401(k) plan if
  litigation risk is real; boundary `legal-disputes`),
  HSA-and-non-spouse-beneficiary-tax-trap (HSA
  inherited by spouse continues as HSA tax-free;
  HSA inherited by non-spouse becomes TAXABLE-IN-
  FULL in the year of inheritance — entire balance
  hits non-spouse-heir's income in the year of
  death; for users with large HSA balances this is a
  significant inheritance-tax-event; offset by
  qualified-medical-expenses-of-decedent paid within
  1 year of death; consider during-life Roth-
  conversion-equivalent moves on large HSA when
  intent-to-bequeath to non-spouse; boundary
  `health-insurance`).
- **Sample situations**:
  - "45yo, just divorced, new spouse. Have 401(k),
    Roth IRA, HSA, $400k taxable brokerage, $80k life
    insurance. Audit beneficiary forms — what's the
    checklist? Stale ex-spouse anywhere?"
  - "Parents both 70, $8M net worth, $5M in
    traditional IRA / 401(k), $2M taxable, $1M Roth.
    2025 doubled-exemption-sunset to ~$7M in 2026.
    Lifetime gifting strategy? SLAT? Roth conversions
    now to reduce inherited-traditional-IRA tax-drag
    on kids?"
  - "Just inherited $600k traditional IRA from parent
    who died in 2024 (post-SECURE 1.0). I'm 40, non-
    spouse, non-EDB. 10-year-rule applies. Take $60k
    / year evenly to smooth bracket impact, or
    front-load in low-income years, or wait till
    year 10 and lump-sum?"

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the
  axes above cluster into ~12–14 reusable framings — current-
  marginal-vs-projected-retirement-marginal-arithmetic (decisions
  1, 2, 7), after-tax-effective-debt-rate-vs-after-tax-expected-
  return (decision 5), tax-bracket-filling-and-cliff-avoidance
  (decisions 2, 7, 8), HSA-as-triple-tax-advantaged-stealth-IRA
  (decisions 1, 3, 8), employer-match-as-100%-immediate-return
  (decisions 1, 5), wash-sale-and-substantially-identical-
  household-aggregation (decision 6), pro-rata-rule-on-backdoor-
  Roth-and-conversion (decisions 1, 7), 5-year-clock-and-Roth-
  aging (decisions 1, 7), IRMAA-2-year-lookback-and-tier-
  management (decisions 2, 7, 8), social-security-spousal-survivor-
  coordination (decision 8), basis-step-up-at-death-and-asset-
  asymmetry (decisions 3, 8, 10), 10-year-inherited-IRA-rule-and-
  EDB-exceptions (decision 10), 2025-doubled-estate-exemption-
  sunset-and-anti-clawback (decision 10), behavioral-discipline-
  and-stay-the-course-premium (decision 4), RSU-and-ESPP-
  concentration-as-stealth-allocation (decision 4), opportunity-
  cost-of-down-payment-and-mortgage-vs-invest (decision 5,
  cross-boundary with `housing`).
- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  decisions 1, 5, 6, 7, 10 are highest-density. Decision 1's
  pro-rata-IRA-trap on backdoor Roth is the canonical "I
  thought I was doing the right thing" mistake — surface
  prominently. Decision 5's PSLF-aggressive-payoff-destroys-
  forgiveness is the canonical "math-correct-policy-wrong"
  mistake. Decision 6's wash-sale-into-spouse's-IRA is the
  canonical "household-aggregation-rule-ignored" mistake.
  Decision 7's recharacterization-no-longer-available
  irreversibility is the canonical "I'll undo it if I
  change my mind" mistake. Decision 10's stale-beneficiary-
  form-supersedes-current-will is the canonical
  Egelhoff-class horror story and is the single highest-
  leverage zero-cost preventive move available — the Editor
  layer should surface it on ANY estate-and-beneficiary
  framing regardless of decision-context. Decisions 7, 8, 10
  carry the highest single-misstep tail risk per ROADMAP §5
  Mechanism E (irrevocable conversions; lifetime-Social-
  Security-claim-age; 2025-vs-2026-estate-tax-exemption-
  sunset window-closing) and warrant the most explicit
  professional-referral specifically — CPA-for-conversion-
  sizing, fee-only-Social-Security-planner-for-claim-age,
  state-bar-estate-attorney-for-sunset-window. Decision 4
  carries the highest behavioral-failure tail risk — the
  best technical allocation the user cannot stick with is
  dominated by a mediocre allocation the user CAN stick with.
- **Cross-domain edges** at the file level: `personal-finance` is
  the most cross-cutting V2 domain, with material edges into 6+
  other domains. Per-decision edges enumerated above; aggregated
  here for the Triage Pass-1 multi-label hint:
  - **`tech-career`** (decisions 1, 2, 4, 5, 6, 7): RSU /
    ISO / ESPP / 83(b) / Mega-Backdoor 401(k) plan-document /
    deferred-comp Section 409A — equity comp lives on this
    boundary; sabbatical / job-loss year as Roth-conversion
    window.
  - **`health-insurance`** (decisions 1, 3, 7, 8): HSA-as-
    triple-tax-advantaged-retirement; FSA-LPFSA-coordination;
    IRMAA-2-year-lookback on Medicare Part B+D for Roth
    conversions; HSA-Medicare-Part-B-premium-payer in
    retirement.
  - **`housing`** (decisions 4, 5, 8, 10): mortgage-vs-invest
    rate-arbitrage; cash-out-refi / HELOC / portfolio-margin
    as alternate financing; Section-121-primary-residence-
    cap-gains-exclusion on downsize; real-estate-TOD-deed
    in permitted states.
  - **`family-planning`** (decisions 1, 2, 7, 8, 9, 10):
    spousal-IRA rules; surviving-spouse-filing-status; QCD
    coordinated with itemize-vs-standard; 529-superfunding
    via 5-year-election; grandparent-529 FAFSA treatment;
    SLAT / GRAT / lifetime-gifting pre-2026-sunset.
  - **`education-funding`** (decisions 1, 5, 9): student-
    loan-PAYE / SAVE / IDR / PSLF; 529-vs-Roth-as-college-
    substitute; in-state-vs-OOS / merit-aid; private-refi
    vs federal-IDR.
  - **`entrepreneurship`** (decisions 1, 6, 7): solo-401(k)
    / SEP-IRA / SIMPLE-IRA for self-employment; QBI Section-
    199A; QSBS Section-1202 5-year-hold; NOL-carryforward
    as Roth-conversion headroom; pro-rata complication when
    SEP-IRA balance exists.
  - **`legal-disputes`** (decisions 6, 10): wash-sale
    coordination across spouse / divorce-mid-trade; QDRO-
    division of retirement on divorce; creditor-protection-
    of-retirement-accounts ERISA-vs-IRA state shield
    variation; will-contests / beneficiary-form-disputes.

  Edges are documentation; routing across edges is V2-Triage's
  job, taking the multi-label hint from this list.
- **High-stakes posture** (uniform with selective referral
  category): `personal-finance` is `high_stakes: true` per
  `_meta_ontology.md` §5 and is the canonical Mechanism E
  gating case named in ROADMAP §5 — the Editor layer must
  consistently label output "decision-support, not financial
  advice", and must NEVER recommend a specific security, fund,
  ticker, or dollar-amount for an individual user's portfolio.
  Generic categories (US-total-stock-index, intermediate-
  Treasury-bond-fund, target-date-fund-with-glide-path-X) are
  decision-support framings; "buy 60% VTI and 40% BND today
  with your $500k inheritance" is financial advice and is
  out-of-scope. The selective referral enumeration in the
  intro keys to specific decisions:
  - **Fee-only fiduciary CFP** (NAPFA / XY-Planning /
    Garrett — fee-only NOT fee-based) for decisions 3, 4, 8
    (asset-location, asset-allocation, withdrawal sequencing —
    where individual-portfolio recommendations are needed and
    the structural-conflict-of-interest of AUM-or-commission
    advisors matters most).
  - **CPA experienced with retirement-plan and equity-comp
    mechanics** for decisions 1, 6, 7 (backdoor-Roth pro-rata
    Form 8606; tax-loss-harvesting + wash-sale validation;
    Roth-conversion sizing relative to IRMAA / ACA / NIIT
    cliffs).
  - **Fee-only Social-Security-claiming-strategy specialist**
    for decision 8 (claim-age coordination — the spousal-
    survivor math is widely under-modeled; fee-only because
    AUM-based and insurance-product-based Social-Security
    consultants have structural incentives to recommend
    annuity-conversion strategies).
  - **State-bar-licensed estate attorney** for decision 10
    (trust formation, SLAT / GRAT / Dynasty trust drafting,
    2025-sunset-pre-2026-gifting moves, beneficiary-form-
    audit-and-update).
  - **ERISA attorney** for decision 1 + decision 10 (high-
    balance 401(k) force-out disputes, Rule-of-55 / SEPP-72(t)
    early-distribution plan-document review, post-divorce-
    QDRO drafting and division, creditor-protection-
    consultation when litigation risk is real).
  - **SHIBA / SHIP volunteer** for decision 8's Medicare-
    coordination side specifically (federally funded, free,
    conflict-free — boundary `health-insurance` decision 4
    / decision 8).
  - **SEC / FINRA BrokerCheck verification** as a $0-friction
    procedural floor on any individual professional
    recommended — surfaced on every individual-professional
    referral, not as over-referral but as safety check;
    catches disciplinary histories on advisors before
    engagement.

  The posture remains "decision-support, not financial
  advice"; the Editor surfaces the appropriate specific
  category inline rather than blanket-mandating one on
  every decision. Over-referral degrades signal; under-
  referral creates harm. Dollar-specific investment
  recommendations and individual-security picks are
  uniformly out-of-scope at the Editor layer regardless of
  decision category — this is the load-bearing Mechanism E
  gate for the domain. The selective referral enumeration
  above is the calibration.
