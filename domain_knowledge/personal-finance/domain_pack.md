# personal-finance — domain_pack.md

Triage / Editor / Critic prompt overrides scoped to the `personal-finance`
domain, per [`_schema.md` §`domain_pack.md`](../_schema.md). Triage's
pass-2 concatenates this file into its system prompt when this domain
is active. Editor and Critic use the corresponding sections when the
situation routes here.

`personal-finance` is `high_stakes: true` per
[`_meta_ontology.md` §5](../_meta_ontology.md), AND it is **the canonical
Mechanism E gating case** named in
[ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)
— dollar-specific investment guidance is exactly the harm class the gate
was written to prevent. Mechanism E gating applies in full, in the same
**uniform** shape as
[`immigration/domain_pack.md`](../immigration/domain_pack.md) (PR #53)
and [`health-insurance/domain_pack.md`](../health-insurance/domain_pack.md)
(PR #88) — NOT the partial-gating posture of
[`housing/domain_pack.md`](../housing/domain_pack.md) (PR #69) or
[`tech-career/domain_pack.md`](../tech-career/domain_pack.md). Three
distinct classes of irrevocability drive the uniform high-stakes posture
(per [`decisions.md`](./decisions.md) intro and
[`framings.md`](./framings.md) intro):

- **Tax-year-boundary one-shot windows.** Many contribution and
  conversion mechanics are calendar-year-bound and cannot be redone
  after the unextended tax-filing deadline of year-N+1 (extension to
  Oct 15 for some — verify per decision). Roth-IRA contributions for
  tax-year-N must be made by April 15 of year-N+1; backdoor-Roth
  cleanest when no other pre-tax IRA balance exists at Dec 31 (the
  pro-rata rule under IRC §408(d)(2) and Form 8606 treats **ALL**
  pre-tax IRA dollars as one pool); Roth-conversion recharacterizations
  were permanently eliminated by TCJA 2017 (IRC §408A(d)(6)(B)(iii)) —
  a Roth conversion is irrevocable from the day it is executed. The
  Mega-Backdoor 401(k) mechanic requires after-tax 401(k)
  contributions PLUS in-plan-Roth-conversion or in-service-rollover-
  to-Roth-IRA capability; both are plan-document features the employer
  chooses to enable, and the window closes if the plan changes. The
  60-day indirect-rollover window on a 401(k)-to-IRA rollover (IRC
  §402(c)(3)) is a one-shot clock — missed without a hardship
  PLR-exception causes the distribution to be treated as a taxable
  distribution with no second chance.
- **Permanent penalties on Social-Security and Medicare-adjacent
  mechanics.** Claiming Social Security before Full Retirement Age (FRA
  — age 67 for those born 1960+) locks the Primary Insurance Amount
  (PIA) at a permanent ~30% reduction at age 62, which compounds for
  the rest of the beneficiary's life AND of the surviving spouse via
  the higher-earner-claim-survivor-benefit rule (42 USC §402(e)(2)).
  Missed RMD (now age 73 for those born 1951–1959, age 75 for those
  born 1960+ per SECURE 2.0 §107) triggers a 25%-of-shortfall excise
  tax (IRC §4974(a), reduced from 50% by SECURE 2.0 — SECURE 2.0
  §302), reducible to 10% if corrected within the SECURE 2.0
  correction window. Missed Medicare Part B IEP without creditable
  employer coverage triggers a 10%-per-12-months-late premium loading
  that persists for life (boundary `health-insurance` D4); IRMAA
  brackets crossed via Roth conversion in year-N hit Medicare premiums
  in year-N+2 via the 2-year-lookback (42 CFR §418.1115). These are
  not investment-return decisions — they have a permanent-record
  character closer to immigration status than to tech-career or housing.
- **Compounding-cost-of-procrastination.** Unlike most life-decision
  domains where the "wait one more year" cost is bounded, retirement-
  contribution gaps compound at the equity risk premium for 30+ years.
  A missed $7,000 Roth-IRA contribution at age 30 compounds to ~$76k at
  age 65 at a 7% real return; the missed contribution cannot be re-made
  because annual caps (IRC §219(b) traditional-IRA, §408A(c)(2) Roth-
  IRA) are per-year-use-it-or-lose-it. The asymmetry between
  procrastinable decisions (housing-relocate, job-change) and non-
  procrastinable decisions (annual retirement contributions) is itself
  a framing axis this domain makes explicit; same compounding applies
  to HSA-as-retirement-vehicle (boundary `health-insurance` D1 / D9).

The wrong call is not recoverable on a multi-year horizon: a Roth
conversion executed at the wrong IRMAA tier in year-N elevates Medicare
premiums for year-N+2 with no undo; an early Social Security claim at
62 locks a 30% reduction in PIA for life AND for the survivor; a stale
ex-spouse on a 401(k) beneficiary form overrides the current will under
*Egelhoff v Egelhoff Ex rel Breiner*, 532 U.S. 141 (2001) and the funds
are paid to the ex-spouse regardless of will or divorce decree; a
$7,000 missed annual IRA contribution at 30 compounds to a 35-year tax-
sheltered-growth gap that cannot be re-made; a wash-sale violation that
the household didn't detect because the replacement security was bought
in the spouse's IRA (IRS Rev. Rul. 2008-5) permanently transfers the
disallowed loss into the basis of the replacement security inside a
tax-advantaged account — where the basis-adjusted-loss is functionally
lost forever.

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
personal-finance because tax-cash-flow couples decisions tightly — a
35-year-old equity-heavy FAANG employee with 60% RSU concentration and
no Roth-IRA contributions spans D1 (contribution ordering), D4 (asset
allocation — RSU as stealth equity allocation per F14), and D6
(harvesting against the concentration via direct-indexing); a 58-year-
old considering retiring early at 62 with $400k traditional 401(k)
spans D2 (Roth-vs-traditional decision deferred too late), D7 (Roth-
conversion-ladder bridge years before age 65 ACA-MAGI / age-73 RMD),
and D8 (withdrawal sequencing + SS claim age 62 vs 67 vs 70). Emit a
list ordered by closeness. A genuinely ambiguous situation between two
decisions is a routing signal worth surfacing; do NOT collapse it.

**Persona refinement.** Pass-1 may have emitted a generic persona like
`retirement-saver` or `investor`. Replace with the most-specific
persona from this controlled list when the situation supports it:

- `early-career-no-debt-w2-stable` — 22–32, no high-interest debt,
  building emergency fund, ordering 401(k)-match-then-Roth-IRA vs
  Roth-401(k); Bogleheads-flowchart canonical setup (D1; F1 / F11)
- `early-career-with-high-interest-debt` — 22–32, credit-card or
  private-student-loan debt > 7% after-tax-effective rate, deciding
  payoff order vs employer-match-capture (D1, D5; F1 / F4 / F6)
- `pslf-aspirant-public-sector` — physician / lawyer / teacher / non-
  profit employee on PSLF track; IDR / SAVE / PAYE forgiveness math
  + tax-bomb-at-forgiveness savings (D5; F4 / F6; boundary
  `education-funding`)
- `dual-w2-household-rsu-heavy` — household with ≥40% net worth in
  single-employer RSU + ESPP discount stock; concentration-risk
  override of F1/F5 priority order (D1, D4, D6; F1↔F14, F5↔F14;
  boundary `tech-career`)
- `equity-comp-iso-amt-exposure` — pre-IPO ISO grants under AMT
  exposure (IRC §56(b)(3) AMT preference item); 83(b)-election
  timing on restricted stock (IRC §83(b)) (D1, D4, D6; F14;
  boundary `tech-career`)
- `backdoor-roth-with-existing-trad-IRA-balance` — household pursuing
  backdoor-Roth where one or both spouses have pre-tax IRA balances
  from prior 401(k) rollovers; pro-rata trap on Form 8606 (D1, D7;
  F4)
- `mega-backdoor-via-after-tax-401k` — plan supports after-tax 401(k)
  contributions + in-plan-Roth-conversion or in-service-rollover-to-
  Roth-IRA; sizing relative to the total 415(c) limit ($70k 2025
  per IRC §415(c)(1)(A), $77.5k with age-50 catch-up, $81.25k with
  age-60–63 super-catch-up per SECURE 2.0 §109) (D1; F1 / F4)
- `hsa-eligible-hdhp-electing-stealth-ira` — HSA-eligible household
  treating the HSA as a 3rd retirement bucket per F3; coordinating
  with spouse FSA-overlap-knockout under IRC §223(c)(1)(A)(ii) and
  the 13-month last-month-rule testing period under IRC §223(b)(8)
  (D1, D3, D8; F3; boundary `health-insurance` D1 / D9)
- `roth-conversion-bridge-year-50s-or-60s` — sabbatical / early-
  retirement / pre-Medicare bridge years between earnings-end and
  age-73-RMD where marginal rate is unusually low; Roth conversion
  ladder sizing against IRMAA / ACA-MAGI / NIIT cliffs (D7; F2 / F12 /
  F4; boundary `health-insurance` D4 / `entrepreneurship`)
- `early-retiree-aca-magi-managing` — under age 65, ACA-marketplace
  enrolled, managing MAGI under 400%-FPL cliff (or post-IRA-sunset:
  under 400%-FPL hard cliff if ARPA enhanced subsidies expire) to
  preserve APTC; Roth-conversion AND capital-gains-realization both
  shift MAGI (D7, D8; F2 / F4 / F12; boundary `health-insurance` D5)
- `near-rmd-age-72-to-75` — within 5 years of RMD start age (73 born
  1951–1959, 75 born 1960+ per SECURE 2.0 §107); should have run
  Roth conversions during sabbatical / pre-SS-claim window if
  bracket allowed (D7, D8; F7 / F12)
- `ss-claim-age-decider-62-67-70` — at age 60–70, deciding when to
  start Social Security against breakeven, survivor coordination
  (42 USC §402(e)(2)), continued-earnings cap (RET), divorced-
  spouse benefit, FRA-spousal-vs-survivor (D8; F7 / F9)
- `retiree-withdrawal-sequencer-traditional-roth-taxable` — retired,
  drawing from 60/40 across taxable / traditional / Roth; sequencing
  against IRMAA tier management, basis-step-up planning for heirs,
  QCD-from-IRA above age 70.5 (IRC §408(d)(8)) (D8; F3 / F7 / F9 /
  F12 / F13)
- `inherited-ira-non-eligible-designated-beneficiary` — inherited
  IRA / 401(k) from non-spouse, subject to SECURE 1.0 10-year
  drawdown (IRC §401(a)(9)(H)) with annual-RMD-during-10-year
  question after 2024 final regs; non-spouse-heir traditional-IRA
  is fully taxable-on-distribution (D8, D10; F7 / F9)
- `tlh-with-cross-account-wash-sale-risk` — household tax-loss-
  harvesting across taxable brokerage while a spouse IRA or robo-
  advisor in another household account holds substantially-identical
  shares (IRS Rev. Rul. 2008-5); household-aggregation-of-wash-sale-
  rule under IRC §1091 is not always intuited (D6; F4)
- `direct-indexing-with-concentration-offsetting` — household using
  a direct-indexed S&P 500 / total-market account to harvest losses
  systematically against gains from concentrated single-stock
  liquidation (D4, D6; F4 / F14)
- `529-vs-roth-vs-taxable-college-funder` — household with kids 0–18,
  evaluating 529 in-state / 529 superfund 5-year-election (IRC
  §529(c)(2)(B)) / Roth-IRA-as-college-substitute (post-2024 SECURE
  2.0 529-to-Roth $35k lifetime rollover under §529(c)(3)(E)) /
  UGMA-UTMA (D9; F1 / F9 / F12; boundary `education-funding`)
- `grandparent-529-owner-fafsa-friendly-post-2024` — grandparent-
  owned 529 distributions no longer count as student income on
  FAFSA after the 2024–25 FAFSA Simplification Act roll-out (D9;
  F9; boundary `education-funding` / `family-planning`)
- `pre-2026-sunset-slat-or-gift` — high-net-worth household pre-2026
  doubled-estate-exemption sunset window (TCJA 2017 §11061(a) →
  sunset Dec 31 2025 per §11061(b)); SLAT / GRAT / direct-gift
  lifetime-exemption-use timing relative to anti-clawback regs
  (Treas. Reg. §20.2010-1) (D10; F9 / F12)
- `stale-beneficiary-form-on-life-event` — divorce / remarriage /
  birth / death event in household; beneficiary-form audit on
  401(k) / IRA / TOD / POD / life-insurance not yet done; *Egelhoff*
  risk that ex-spouse-on-401(k)-form overrides current will (D10;
  F9)
- `creditor-shielded-or-litigation-exposed-professional` — physician /
  surgeon / dentist / RIA / fund-manager / contractor in high-
  liability profession; 401(k) ERISA-protected-unlimited vs IRA-
  rollover-creditor-shield-limited (~$1.5M federal-bankruptcy-
  exempt under 11 USC §522(n) indexed, plus state-shield variation
  — TX / FL unlimited, CA post-bankruptcy-only, NY partial) (D1,
  D10; F8)
- `fire-saver-bridge-pre-59.5-roth-ladder` — household pursuing
  early-retirement (FIRE), bridging the age-gap-pre-59.5 via Roth-
  conversion-ladder (IRC §72(t)(2)(F) 5-year-aging-clock per
  conversion) and/or Substantially Equal Periodic Payments under
  IRC §72(t)(2)(A)(iv) (D7, D8; F13; boundary
  `health-insurance` D5 ACA bridge)
- `self-employed-solo-401k-vs-sep-ira` — 1099 / self-employed; solo-
  401(k) vs SEP-IRA selection given pro-rata complication on later
  backdoor-Roth (SEP-IRA balance triggers Form 8606 pro-rata; solo-
  401(k) does not) (D1; F1 / F4; boundary `entrepreneurship`)
- `qsbs-section-1202-5-year-holder` — pre-IPO equity holder
  approaching 5-year QSBS clock under IRC §1202; up-to-$10M-or-10x-
  basis gain-exclusion eligibility, gifting-to-trust strategies
  (D1, D6, D7; F14; boundary `tech-career` / `entrepreneurship`)
- `divorce-mid-trade-qdro-asset-division` — divorcing household with
  retirement-account division; QDRO drafting (29 USC §1056(d)(3));
  beneficiary-form-update under *Egelhoff*; wash-sale risk if both
  parties hold same security mid-divorce (D6, D10; F8 / F9;
  boundary `legal-disputes`)

These are the personas the per-domain blindspot triggers in
[`blindspots.md`](./blindspots.md) are written against. Generic
persona labels will miss most triggers.

**Risk-surface vocabulary.** Replace generic `taxes` / `retirement` /
`investing` / `debt` / `inheritance` from Pass-1 with the specific
risk surfaces below when the situation supports them. Each maps to one
or more blindspots in [`blindspots.md`](./blindspots.md); using the
generic label loses the routing:

- Contribution / cap one-shot clocks: `Roth-IRA-cap-7000-or-8000-
  catch-up-2025` (IRC §408A(c)(2)), `401k-elective-deferral-cap-23500-
  plus-7500-age-50-plus-11250-age-60-63-super-catch-up-2025`,
  `415c-overall-defined-contribution-limit-70000-2025` (IRC
  §415(c)(1)(A)), `HSA-cap-4300-or-8550-plus-1000-55-catch-up-2026`
  (IRC §223(b)), `dep-care-FSA-5000-MFJ-or-2500-MFS`,
  `tax-year-N-Roth-IRA-contribution-deadline-April-15-N+1`,
  `Roth-conversion-irrevocable-since-TCJA-2017` (IRC §408A(d)(6)(B)(iii)),
  `60-day-indirect-rollover-window` (IRC §402(c)(3)),
  `12-month-one-rollover-per-IRA-rule` (IRC §408(d)(3)(B); *Bobrow v
  Commissioner*, TC Memo 2014-21)
- Pro-rata / aggregation traps: `pro-rata-rule-form-8606`
  (IRC §408(d)(2)), `traditional-IRA-balance-aggregation-across-
  SEP-and-SIMPLE-and-rollover-IRA`, `Mega-Backdoor-plan-document-
  feature-check`, `step-doctrine-IRS-Notice-2014-54`,
  `solo-401k-vs-SEP-IRA-impact-on-backdoor-pro-rata`
- Tax-arbitrage / harvesting mechanics: `wash-sale-30-day-window`
  (IRC §1091), `substantially-identical-security-determination`,
  `household-aggregation-of-wash-sale-spouse-IRA` (Rev. Rul. 2008-5),
  `wash-sale-into-tax-advantaged-account-basis-loss-permanently`,
  `0-percent-LTCG-bracket-for-MFJ-under-94k-2025`,
  `NIIT-3.8-percent-200k-single-250k-MFJ-MAGI` (IRC §1411),
  `AMT-iso-bargain-element-preference-item` (IRC §56(b)(3)),
  `QSBS-section-1202-5-year-hold-10M-or-10x-basis-exclusion`,
  `83b-election-30-day-deadline-from-grant` (IRC §83(b)),
  `direct-indexing-as-systematic-harvesting-vehicle`
- Roth / conversion windows + cliffs: `Roth-conversion-5-year-aging-
  clock-per-conversion-pre-59.5` (IRC §72(t)(2)(F)),
  `Roth-IRA-contribution-vs-conversion-distinct-5-year-clocks`,
  `IRMAA-2-year-lookback-MAGI` (42 CFR §418.1115),
  `IRMAA-2026-brackets-103k-129k-161k-193k-500k-single` (verify
  current year), `ACA-MAGI-400-percent-FPL-cliff-or-IRA-sliding-
  scale-pre-sunset` (IRC §36B; ARPA / IRA extension expiring end
  of 2025 absent extension), `NIIT-bracket-3.8-percent`,
  `tax-bracket-fill-vs-cliff-bunching`, `Medicare-Part-A-
  retroactive-up-to-6-months-on-SS-claim-loses-HSA-eligibility`
  (boundary `health-insurance` D9)
- Social-Security mechanics: `SS-claim-age-62-FRA-70`,
  `PIA-permanent-30-percent-reduction-at-62`,
  `delayed-retirement-credits-8-percent-per-year-to-70`,
  `survivor-benefit-higher-earner-claim-locks-survivor-floor`
  (42 USC §402(e)(2)),
  `divorced-spouse-benefit-10-year-marriage-test`,
  `child-in-care-survivor-benefit`,
  `earnings-cap-RET-before-FRA-2025-thresholds`,
  `WEP-and-GPO-2024-Social-Security-Fairness-Act-repeal`,
  `bend-points-PIA-formula-90-32-15-percent`
- RMD / withdrawal mechanics: `RMD-start-age-73-born-1951-1959-or-
  75-born-1960-plus` (SECURE 2.0 §107 → IRC §401(a)(9)(C)),
  `RMD-25-percent-shortfall-excise-tax-reduced-to-10-if-corrected`
  (SECURE 2.0 §302 → IRC §4974), `QCD-from-IRA-age-70.5-up-to-
  105000-2024-indexed` (IRC §408(d)(8)), `Rule-of-55-employer-
  plan-only-not-IRA` (IRC §72(t)(2)(A)(v)), `SEPP-72t-substantially-
  equal-periodic-payments-modify-trap` (IRC §72(t)(2)(A)(iv)),
  `4-percent-safe-withdrawal-rate-Bengen-1994-30-year`,
  `3-3.5-percent-safe-withdrawal-rate-50-year-FIRE`,
  `sequence-of-returns-risk-early-retirement`,
  `bond-tent-glide-path-prior-to-and-into-retirement`
- Inherited / estate mechanics: `SECURE-1.0-10-year-rule-non-EDB`
  (IRC §401(a)(9)(H)), `EDB-exception-spouse-disabled-chronically-
  ill-not-more-than-10-years-younger`, `annual-RMD-during-10-years-
  if-decedent-was-past-RMD-age-2024-final-regs`,
  `inherited-traditional-IRA-fully-taxable-non-spouse`,
  `inherited-Roth-IRA-tax-free-but-still-10-year-rule`,
  `stretch-IRA-pre-2020-only-eliminated-SECURE-1.0`,
  `basis-step-up-on-taxable-inheritance` (IRC §1014),
  `lifetime-estate-tax-exemption-13.99M-2025-sunsetting-to-
  ~7M-indexed-2026` (TCJA §11061(b)),
  `anti-clawback-Treas-Reg-20.2010-1`,
  `Egelhoff-beneficiary-form-supersedes-will-and-divorce-decree`
  (*Egelhoff v Egelhoff Ex rel Breiner*, 532 U.S. 141 (2001)),
  `TOD-POD-transfer-on-death-supersedes-will`,
  `Clark-v-Rameker-inherited-IRA-not-creditor-protected`
  (*Clark v Rameker*, 573 U.S. 122 (2014))
- Asset-protection / creditor mechanics: `ERISA-401k-unlimited-
  federal-bankruptcy-exempt` (29 USC §1132; 11 USC §522(d)(12)),
  `rollover-IRA-1.5M-indexed-federal-bankruptcy-exempt` (11 USC
  §522(n)), `state-IRA-shield-variation-TX-FL-unlimited-CA-post-
  bankruptcy-NY-partial`, `solo-401k-not-ERISA-protected-state-
  shield-only`, `inherited-IRA-not-creditor-protected-Clark`,
  `QDRO-division-of-retirement-on-divorce` (29 USC §1056(d)(3))
- Debt-vs-invest mechanics: `after-tax-effective-debt-rate-vs-after-
  tax-expected-return`, `PSLF-aggressive-payoff-destroys-forgiveness`
  (boundary `education-funding`), `SAVE-PAYE-IDR-AGI-management`
  (boundary `education-funding`), `mortgage-vs-invest-rate-arbitrage`
  (boundary `housing`), `student-loan-tax-bomb-saved-separately-not-
  in-pre-tax-401k`, `0-percent-promotional-balance-transfer-clock-
  trap`
- Equity-comp interactions: `RSU-vest-sell-vs-hold-concentration`
  (boundary `tech-career`), `ISO-AMT-disqualifying-disposition-1-
  year-or-2-year-hold` (IRC §422), `ESPP-15-percent-discount-
  qualified-disposition-2-year-or-1-year`, `83b-election-30-day-
  deadline-restricted-stock`, `409A-deferred-comp-election-prior-
  year`, `QSBS-1202-5-year-hold`, `wash-sale-RSU-vest-and-sell-
  same-week-as-replacement-buy`
- Professional-conflict-of-interest mechanics: `AUM-fee-1-percent-
  per-year-vs-fee-only-flat`, `commission-vs-fee-only-vs-fee-based-
  hybrid`, `IRA-rollover-from-401k-incentive-bias`, `annuity-
  purchase-commission-bias`, `series-7-broker-vs-series-65-RIA-
  fiduciary`, `Reg-BI-suitability-vs-fiduciary-standard`,
  `SEC-IAPD-disclosure-check`, `FINRA-BrokerCheck-disclosure-event`,
  `XY-Planning-Network-NAPFA-Garrett-Planning-Network-fee-only-
  directory`

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

- F1 (investment-priority-order Bogleheads-canonical) ↔ F14 (equity-
  comp / concentration-risk) — same household, opposite first-move on
  D1 / D4. F1's clean sequence assumes smooth W-2 cash flow and
  unconstrained-by-equity-comp budget; F14 overrides for the equity-
  comp-heavy household where sell-on-vest-to-diversify $400k single-
  employer concentration dominates the marginal-tax-arbitrage of the
  next-step contribution. Triage emits F14 whenever the asker
  mentions RSU / ISO / ESPP / 83(b) / QSBS or names a single
  employer holding > 20% of net worth.
- F2 (marginal-rate-arbitrage) ↔ F12 (policy-volatility / system-
  skepticism) — same facts, opposite Roth-vs-traditional on D2 / D7.
  F2 computes contribution-arbitrage from current-marginal vs
  projected-retirement-marginal as deterministic point estimates;
  F12 argues the projected-retirement-marginal is itself a policy-
  determined variable subject to TCJA-sunset / SECURE-cycle / SS-
  benefit-cut volatility, and tilts Roth as a policy-hedge.
  Particularly load-bearing in 2025 because of the Dec 31 2025 TCJA-
  income-tax-bracket sunset — the same 24% effective rate the asker
  pays today may look unusually low in retrospect from a 2026 post-
  sunset perspective.
- F3 (HSA-as-stealth-IRA) ↔ F6 (behavioral-debt-payoff) when cash-
  flow-constrained — same household, opposite priority on D1 / D5 /
  D9. F3 says fund the HSA to the $4,300 / $8,550 cap and pay current
  medical OOP from after-tax savings, letting the HSA compound 30
  years; F6 says for the household with $15k credit-card debt and no
  emergency fund, the HDHP-high-deductible exposure combined with no
  emergency-fund creates catastrophic vulnerability F3's long-horizon
  ignores.
- F4 (tax-arbitrage / Form-mechanic) ↔ F6 (behavioral-debt-payoff) on
  D5 — F4 reasons about after-tax-effective-debt-rate vs after-tax-
  expected-return as a clean arbitrage; F6 surfaces that the
  behavioral-stickiness of carrying revolving debt creates compliance-
  failure risk on the supposedly higher-EV "carry-debt-and-invest"
  strategy. Both produce technically-correct answers under their own
  assumptions, but F4 alone misses Dave-Ramsey-class askers who need
  the behavioral-anchor of debt-free milestone.
- F5 (risk-adjusted-allocation MPT) ↔ F14 (equity-comp /
  concentration-risk) — D4 convergence with different reasoning paths.
  F5 frames as "pick target, rebalance to target"; F14 frames as
  "sell concentration first, then think about target." Both
  recommend diversification, but on different paths — for the asker
  whose 70/30 target is undermined by a $480k single-employer stealth
  position swamping the chosen allocation, F5 alone underestimates
  the urgency.
- F7 (time-horizon / lifecycle retirement-econ) ↔ F9 (estate-and-
  intergenerational) — D8 / D10 collision. F7's withdrawal-sequencing
  default (taxable first, then tax-deferred, then Roth — preserves
  Roth tax-free compounding longest) is *inverted* by F9 when intent-
  to-bequeath is material: F9 recommends running down traditional-
  401(k) / IRA during life because heirs inherit Roth or stepped-up-
  basis-taxable rather than ordinary-income-on-distribution-
  traditional under SECURE 1.0 10-year drawdown.
- F8 (asset-protection / creditor-shield) ↔ F1 (priority-order) on D1
  for the high-liability-profession household. F1's "rollover 401(k)
  to IRA on job change for lower-cost investment options" is correct
  on expense-ratio arithmetic but **weakens** creditor protection per
  F8 — ERISA-protected 401(k) is unlimited federal-bankruptcy-exempt
  while rollover-IRA is capped at ~$1.5M-indexed and state-shield
  varies sharply. Surface F8 whenever the asker mentions a high-
  liability profession (physician / surgeon / dentist / RIA / fund-
  manager / contractor) or any ongoing litigation exposure.
- F10 (professional-referral / conflict-of-interest) ↔ F11
  (behavioral-and-automation / DIY) — both safe defaults, different
  asker profiles. F10's "always-consult-a-fee-only-CFP for individual-
  recommendation decisions" is the safe default for the asker without
  time-or-inclination to self-study; F11's "automate everything via
  Bogleheads-flowchart-DIY + robo-rebalancing" is right for the asker
  with literacy and discipline. The conflict surfaces on moderate-
  complexity "should I hire an advisor or do this myself" questions.
- F12 (policy-volatility / system-skepticism) ↔ F2 (marginal-rate-
  arbitrage) — surfaced above on D2 / D7. ALSO crosses F4 on D7 —
  same Roth-conversion-ladder decision, F4 says "convert exactly to
  the top of the 12% bracket, no more"; F12 says "convert past the
  12% bracket because future brackets may compress and 12% may not
  exist."
- F13 (FIRE / extreme-saver) ↔ F7 (lifecycle / retirement-econ
  academic) — same savings target ($1M), opposite sustainable-
  spending answer ($40k/yr at 4% per Bengen 1994 vs $30k/yr at 3% for
  50-year early-FIRE retirement). Surface both when the asker is an
  early-FIRE candidate; the trade-off should appear explicitly.
- F14 (equity-comp / concentration-risk) is the most cross-cutting
  framing in this domain because it overrides F1, F5, and F11 for any
  household with > 20% net-worth concentration in a single employer.
  Triage emits F14 whenever the asker's facts indicate equity-comp.

F11 (behavioral-and-automation), F12 (policy-volatility), and F10
(professional-referral) are **meta-framings** that apply on top of any
primary decision framing rather than as the primary lens themselves —
they tune the recommendation surfaced by F1–F9 / F13 / F14. The asker's
framing is itself a blind spot — Triage emits the opposing framing in
`active_framings` even when the asker's vocabulary doesn't match it,
so the Risk Officer has the opposing surface to work from.

**Cross-domain routing flags.** When Pass-1 surfaces signals that
imply an adjacent domain, emit `cross_domain: [<slug>, ...]`.
`personal-finance` is **the most cross-cutting V2 domain** because
tax-and-cash-flow consequences cascade out of most life decisions.
Per [`decisions.md`](./decisions.md) and [`framings.md`](./framings.md)
annotations:

- RSU / ISO / ESPP / 83(b) / QSBS / Mega-Backdoor-401(k) plan-document
  / sabbatical-year-Roth-conversion / deferred-comp Section 409A →
  add `tech-career` (D1, D2, D4, D5, D6, D7 boundary; F14 cross-
  domain edge — the highest-frequency edge after `health-insurance`)
- HSA-as-triple-tax-advantaged-retirement / FSA-vs-LPFSA / IRMAA-2-
  year-lookback-on-Roth-conversion / Medicare-Part-A-retroactive-on-
  SS-claim-loses-HSA-eligibility / ACA-MAGI-cliff-on-early-retiree →
  add `health-insurance` (D1, D3, D7, D8 boundary; F3 / F12 cross-
  domain edge)
- Solo-401(k) / SEP-IRA / SIMPLE-IRA / QBI Section-199A / QSBS
  Section-1202 5-year-hold / NOL-carryforward-as-Roth-conversion-
  headroom → add `entrepreneurship` (D1, D6, D7 boundary)
- Mortgage-vs-invest-rate-arbitrage / cash-out-refi / HELOC / Section-
  121-primary-residence-cap-gains-exclusion / real-estate-TOD-deed
  → add `housing` (D4, D5, D8, D10 boundary)
- 529-superfunding / 529-to-Roth-rollover-SECURE-2.0 / spousal-IRA /
  beneficiary-form-audit-on-marriage-divorce-birth-death / SLAT /
  GRAT / lifetime-gifting-pre-2026-sunset → add `family-planning`
  (D1, D2, D7, D8, D9, D10 boundary)
- 529-vs-Roth-as-college-substitute / student-loan-PAYE-SAVE-IDR-
  PSLF / private-refi-vs-federal-IDR / kiddie-tax-on-UGMA-UTMA → add
  `education-funding` (D1, D5, D9 boundary)
- Wash-sale-coordination-across-spouse-or-divorce / QDRO-division-of-
  retirement-on-divorce / creditor-protection-state-shield → add
  `legal-disputes` (D6, D10 boundary; F8 cross-domain edge)
- Mid-career-pivot-with-sabbatical-Roth-conversion-window / coast-
  FIRE-bridge-job / early-retirement-glide-path → add
  `career-pivots` (D7, D8 boundary; F7 / F13 cross-domain edge)

These flags inform the orchestrator's source-view selection; Pass-2
itself does not call those domains' packs. The `personal-finance` ↔
`health-insurance` edge is among the most load-bearing on referral
routing — HSA-as-triple-tax-advantaged-retirement, IRMAA-2-year-
lookback, ACA-MAGI-cliff-management all route through it before the
CPA referral is named. The `personal-finance` ↔ `tech-career` edge is
the densest on equity-comp surfaces.

---

## Editor

The generic editor prompt in
[`src/blindspot/prompts/editor.md`](../../src/blindspot/prompts/editor.md)
governs structure. The additions below apply when this domain is
active.

**Numeric and statutory specificity is mandatory.** Personal-finance
blindspots are worthless without the specific contribution cap, the
specific IRC section, the specific clock or AGI-cliff threshold. When
a blind spot or action references the categories below, the specific
number / clock / statute is required; the generic shape is Critic-
failing padding:

- *Annual contribution caps (2025, indexed annually — re-verify)*:
  Roth-IRA $7,000 (+ $1,000 catch-up at 50+) per IRC §408A(c)(2);
  401(k)/403(b)/457(b) elective deferral $23,500 (+ $7,500 age 50+
  catch-up, + $11,250 age-60–63 super-catch-up per SECURE 2.0 §109);
  IRC §415(c)(1)(A) overall defined-contribution limit $70,000 (+
  catch-ups); HSA $4,300 self / $8,550 family for 2026 + $1,000 age-
  55-catch-up (IRC §223(b)); SEP-IRA the lesser of 25% of net self-
  employment or §415(c) limit; SIMPLE-IRA $16,500 + $3,500 catch-up
  (+ $5,250 age-60–63 super-catch-up); 529 superfund 5-year-election
  $95,000 single / $190,000 MFJ per beneficiary (IRC §529(c)(2)(B);
  re-verify against 2025 annual-gift-exclusion of $19,000 × 5 = $95k).
- *AGI / MAGI cliffs and brackets (2025, indexed annually)*: NIIT 3.8%
  at $200k single / $250k MFJ MAGI (IRC §1411); Roth-IRA contribution
  phase-out $146k–$161k single / $230k–$240k MFJ (IRC §408A(c)(3));
  traditional-IRA deduction phase-out when covered by workplace plan
  $79k–$89k single / $126k–$146k MFJ (IRC §219(g)); IRMAA 2026
  brackets $103k / $129k / $161k / $193k / $500k+ single MAGI on 2-
  year-lookback (verify current year per 42 CFR §418.1115);
  0%-LTCG-bracket $48,350 single / $94,050 MFJ for 2025; ACA-MAGI
  400%-FPL cliff (or 8.5%-of-MAGI-cap if ARPA enhanced subsidies
  extended past 2025 — verify current statute); Saver's Credit
  income limits $38,250 single / $76,500 MFJ for 2025 (IRC §25B).
- *Roth-conversion mechanics*: irrevocable since TCJA 2017 §13611(a)
  amended IRC §408A(d)(6)(B)(iii); each conversion starts its own
  5-year aging clock under IRC §72(t)(2)(F) for pre-59.5 withdrawal
  of conversion principal; the 5-year clock for tax-free earnings on
  Roth-IRA contribution-or-conversion runs from Jan 1 of the year of
  first Roth-IRA opening (NOT per-conversion). Roth-IRA contribution
  for tax-year-N must be made by the unextended April 15 deadline of
  year-N+1; no Oct 15 extension applies despite the filing extension.
- *Pro-rata math on backdoor-Roth (IRC §408(d)(2); Form 8606)*:
  applies across **all** pre-tax IRA balances aggregated at Dec 31 of
  the conversion year, including SEP-IRA and SIMPLE-IRA but NOT
  401(k) / 403(b) / 457(b) / solo-401(k). The pro-rata fraction is
  pre-tax-IRA-aggregate / (pre-tax-IRA-aggregate + after-tax-
  contribution-basis), applied to the conversion amount as the
  taxable percentage. Step-doctrine guidance: IRS Notice 2014-54
  blessed the same-day-non-deductible-contribute-and-convert sequence.
- *Wash-sale rule (IRC §1091; Rev. Rul. 2008-5)*: 30-day window
  before AND after the loss-sale; substantially-identical securities
  triggered (ETF vs near-identical-ETF is the canonical edge);
  household-aggregation includes spouse's IRA — wash sale into
  spouse's IRA permanently shifts the disallowed loss into the IRA
  basis where the basis adjustment is functionally lost; direct-
  indexing as a systematic harvesting vehicle requires algorithmic
  tracking of substantially-identical exposure across all household
  accounts.
- *Social-Security mechanics (42 USC §402)*: PIA at FRA (67 for those
  born 1960+); claim at 62 = ~30% permanent reduction in PIA;
  delayed-retirement credit of 8%/year past FRA to age 70; survivor
  benefit equals the higher of (a) the survivor's own PIA or (b) the
  decedent's effective claim — claiming early permanently locks the
  survivor floor; earnings-cap RET applies before FRA only — $23,400
  for 2025 sub-FRA (verify current year); GPO and WEP repealed by
  Social Security Fairness Act 2024 (Public Law 118-273); divorced-
  spouse benefit available after 10-year-marriage even if remarried-
  after-60.
- *RMD / SECURE-2.0 mechanics (IRC §401(a)(9))*: RMD start age 73 for
  those born 1951–1959, 75 for those born 1960+ (SECURE 2.0 §107);
  25% shortfall excise tax (IRC §4974, reduced from 50% by SECURE
  2.0 §302), reduced to 10% if corrected within the SECURE 2.0
  correction window with Form 5329; QCD from IRA at age 70.5 up to
  $105,000 for 2024 (indexed; verify current year per IRC §408(d)(8));
  Rule-of-55 employer-plan-only (IRC §72(t)(2)(A)(v)); SEPP-72(t)
  modifications-trap (modifying any factor before later of 5 years or
  age 59.5 retroactively imposes 10% penalty + interest on all prior
  distributions); SECURE 1.0 10-year drawdown for non-EDB inheritors
  (IRC §401(a)(9)(H)); EDB exceptions: surviving spouse, disabled,
  chronically ill, not-more-than-10-years-younger, minor child of
  decedent until age 21.
- *Estate exemption sunset*: lifetime exemption $13.99M per individual
  / $27.98M MFJ for 2025; sunsets to ~$7M-indexed per individual on
  Jan 1 2026 per TCJA §11061(b) absent congressional extension; anti-
  clawback regs (Treas. Reg. §20.2010-1) confirm pre-sunset gifts do
  not pull back into the lower-exemption post-2026 estate; pre-2026
  SLAT / GRAT / lifetime-gifting strategies are time-bound; basis-
  step-up at death per IRC §1014 makes the taxable / brokerage account
  the asymmetric-best vehicle for HNW inheritance vs traditional-IRA
  (which loses basis-step-up because it has zero basis to step up).
- *Beneficiary-form supremacy (Egelhoff and *Kennedy v Plan
  Administrator for DuPont Savings*)*: under ERISA preemption,
  401(k) / 403(b) beneficiary forms supersede a contrary will or
  divorce decree (*Egelhoff v Egelhoff Ex rel Breiner*, 532 U.S. 141
  (2001); *Kennedy v Plan Administrator for DuPont Savings & Investment
  Plan*, 555 U.S. 285 (2009)). IRA / Roth-IRA beneficiary forms have
  the same supremacy under state contract law / state intestate-
  succession. TOD / POD on taxable brokerage supersede the will.
  Stale-form-on-ex-spouse is the canonical horror-story scenario in
  this domain. Beneficiary-form-audit-on-life-event (marriage /
  divorce / birth / death) is a zero-cost preventive move and the
  Editor should surface it on ANY estate-and-beneficiary framing.
- *Asset-protection statute citations*: ERISA-protected 401(k)
  unlimited federal-bankruptcy-exempt under 11 USC §522(d)(12) and
  ERISA §206(d) (29 USC §1056(d)); rollover-IRA capped at $1,512,350
  federal-bankruptcy-exempt indexed (11 USC §522(n)); inherited-IRA
  has NO federal-bankruptcy exemption per *Clark v Rameker*, 573 U.S.
  122 (2014); state-shield laws vary sharply — TX / FL unlimited,
  CA post-bankruptcy-only, NY partial; solo-401(k) is NOT ERISA-
  protected unless covering W-2 employees (gets state-shield only).
- *PSLF / IDR mechanics (boundary `education-funding`)*: SAVE /
  PAYE / IBR forgiveness after 120 qualifying payments (10 years)
  for PSLF, or 20–25 years for IDR forgiveness; aggressive private-
  refi-or-payoff destroys forgiveness eligibility; tax-bomb at IDR-
  forgiveness applies (PSLF forgiveness is tax-free under IRC
  §108(f)(1); IDR-forgiveness is taxable as ordinary income under
  ARPA-2021 sunset through 2025, post-sunset taxable as ordinary
  income).
- *QSBS Section-1202 mechanics (boundary `tech-career` /
  `entrepreneurship`)*: 5-year-hold from acquisition; up to $10M-or-
  10x-basis gain exclusion under IRC §1202(b)(1); C-corp-only;
  qualified-trade-or-business test (most professional-services
  excluded — law, accounting, health, consulting; tech generally
  qualifies); 100% exclusion for QSBS acquired after Sep 27 2010;
  gifting-to-trust-or-children can multiply the $10M cap.

**Decision-support, not financial advice — explicit label required on
every output.** Because `personal-finance.high_stakes` is `true` per
Mechanism E AND personal-finance is the canonical Mechanism E gating
case named in ROADMAP §5, every final output MUST include language
equivalent to: *"This is decision-support framing, not financial
advice. Personal-finance decisions are high-stakes — Roth conversions
are irrevocable since TCJA 2017; Social Security claim-age decisions
permanently affect both the claimant's and the surviving spouse's
benefit; the 2025 doubled-estate-exemption sunsets Dec 31 2025 absent
congressional extension; beneficiary-form errors on retirement
accounts override even a current will under Egelhoff. The binding
determination on your specific case requires the appropriate specific
professional with your full income, asset, and household picture: [the
specific category — see referral list below]. I cannot and do not
recommend specific securities, dollar amounts, fund tickers, or
allocations for your portfolio."* The label belongs at the head of the
answer for D7 (Roth-conversion ladder), D8 (Social Security and RMD
sequencing), and D10 (estate / beneficiary structuring) — the highest-
stakes irreversibility decisions; for other decisions it can tail the
answer. Critic flags soft language ("you might want to consider
speaking to a financial planner eventually") as insufficient.

**No dollar-specific investment guidance is the load-bearing gate.**
This is the canonical Mechanism E gating posture for the entire V2
ontology — the Editor MUST NOT recommend a specific security
(individual stock, individual bond, specific ETF ticker), specific
dollar-amount for an individual user's portfolio, or specific
allocation-percentage tailored to the user's named net worth.
Categorical recommendations (US-total-stock-index, intermediate-
Treasury-bond-fund, target-date-fund-with-glide-path-X, three-fund-
portfolio-in-Bogleheads-style, broadly diversified low-cost index
fund) are decision-support framings and ARE in scope. "Buy 60% VTI
and 40% BND today with your $500k inheritance" is financial advice
and is out-of-scope regardless of how good the underlying analytical
case is — the structural problem is that the Editor lacks the
asker's full picture (tax situation, equity-comp constraints, IRMAA
exposure, behavioral discipline, beneficiary considerations), and
the appropriate fiduciary professional supplies that picture.

**Opportunity-cost framing on multi-route situations.** Per
[`framings.md`](./framings.md) "Cross-framing tensions," any answer
that lands on multiple decisions (D1+D5; D1+D4+D6; D7+D8; D8+D10)
must surface the opportunity-cost lens between routes — the same
$23,500 of annual savings allocated to traditional-401(k) vs Roth-
401(k) vs HSA vs Mega-Backdoor-Roth-401(k) vs taxable-brokerage-tax-
loss-harvested produces structurally different terminal-wealth
distributions and different optionality, not just different point
estimates. The Editor MUST name the trade-off on the route NOT taken
("if you fund Roth-401(k) instead of Mega-Backdoor Roth, the after-
tax compounding of $23,500 at 7% real over 30 years is X; the trade-
off you give up is access to potentially additional $46,500 of after-
tax 401(k) space that would have rolled to Roth-IRA tax-free under
Notice 2014-54"), even when the question only asked about one route.

**Selective-professional-referral matrix.** Unlike a blanket "consult
a financial advisor," the *category* of professional varies sharply
by decision in personal-finance — fee-only CFP for portfolio
construction is structurally different from a retirement-experienced
CPA for tax-loss-harvesting validation, which is different again from
an ERISA attorney for QDRO drafting. The Editor names the *specific
category* keyed to the decision and trigger, per the calibration
encoded in [`decisions.md`](./decisions.md) intro "Selective referral"
and [`blindspots.md`](./blindspots.md) Recovery rules. Each named
referral SHOULD be paired with the SEC IAPD / FINRA BrokerCheck
verification anchor (see below):

- **Fee-only fiduciary CFP** (NAPFA / XY-Planning-Network / Garrett
  Planning Network — fee-only NOT fee-based hybrid; the distinction
  is load-bearing because AUM-based and commission-based advisors
  have structural incentive to recommend rollover-from-401(k)-to-IRA,
  annuity-purchase, or actively-managed funds even when low-cost
  index-fund-DIY strictly dominates on expected-return-net-of-fees) —
  D3 (asset location across account types), D4 (asset allocation and
  glide path), D7 (Roth conversion ladder when CFP and CPA work in
  tandem on tax-and-allocation sides), D8 (retirement-withdrawal
  sequencing and SS-claim-age coordination). Hourly-or-flat-fee (the
  Garrett Planning Network niche) is the right category when the
  asker has a bounded one-time question; AUM-only is wrong for the
  asker whose decision is fundamentally one-time-irreversible (D7,
  D10). Surface the structural-conflict-of-interest framing inline:
  "AUM advisors charge ~1% of assets annually, which compounds to
  ~24% of terminal wealth over 30 years; fee-only-flat-fee advisors
  charge $2,000–$5,000 for a comprehensive plan."
- **Retirement-experienced CPA** (NOT a generic tax-prep CPA; verify
  the practitioner has explicit experience with Form 8889 / Form
  8606 / Form 5498 / Form 1099-R reconciliation / Mega-Backdoor /
  equity-comp / RSU-and-ESPP-W-2-vs-Form-1099-B basis adjustments) —
  D1 (contribution-ordering when Mega-Backdoor + after-tax 401(k) is
  in play and Form 8606 pro-rata math is non-trivial), D2 (Roth-vs-
  traditional split when current-marginal-vs-projected-retirement-
  marginal arithmetic has bracket-fill nuance), D6 (tax-loss
  harvesting + wash-sale validation, especially household-aggregation
  across spouse IRA), D7 (Roth-conversion ladder sizing against
  IRMAA / ACA-MAGI / NIIT / 0%-LTCG-bracket cliffs), D9 (529-vs-Roth-
  vs-taxable in combination with state-income-tax-deduction-for-529
  in 30+ states), D10 (RMD-and-QCD coordination, basis-step-up at
  death calculations). Boundary `entrepreneurship` — for any asker
  with significant 1099 income, solo-401(k) / SEP-IRA / SIMPLE-IRA
  selection requires a CPA with self-employed-retirement-plan
  experience; the wrong selection (e.g. SEP-IRA when backdoor-Roth is
  important) creates a pro-rata trap that lasts as long as the SEP-
  IRA balance remains. The CPA-vs-CFP referral overlaps; many
  decisions need both, in sequence: CPA validates the tax mechanic,
  CFP validates the asset-allocation impact.
- **Fee-only Social-Security-claiming-strategy specialist** — D8 (SS-
  claim-age 62 vs FRA vs 70 vs spousal vs survivor coordination).
  The asker needs Mike-Piper-Open-Social-Security / Maximize-My-
  Social-Security / Bedrock-Capital-class software-run scenarios
  against the asker's actual earnings record (pulled from
  ssa.gov-my-account). Fee-only NOT commission-based — commission-
  based "Social Security consultants" are often annuity salespeople
  whose recommendations route to commissionable products. Some fee-
  only CFPs subspecialize here; the SHIP / SHIBA volunteer is the
  parallel for the Medicare-coordination side (boundary `health-
  insurance` D4 / D8).
- **State-bar-licensed estate attorney** — D10 (trust formation —
  revocable vs irrevocable vs SLAT vs ILIT vs Dynasty trust vs
  charitable-remainder-trust; beneficiary-form audit; the 2025
  doubled-exemption sunset window). Each state has its own probate /
  trust law variation; multi-state property holdings require
  coordinated multi-state estate plans. The 2025 sunset window
  closes Dec 31 2025; pre-2026 SLAT / GRAT / lifetime-gifting moves
  are time-bound with anti-clawback Treas. Reg. §20.2010-1
  protection. Refer at any decision touching trust formation OR
  high-net-worth households facing the 2026 exemption reduction.
- **ERISA attorney** — D1 (high-balance 401(k) force-out disputes,
  Rule-of-55 / SEPP-72(t) plan-document review, in-service-rollover
  capability disputes), D10 (post-divorce QDRO drafting and division
  under 29 USC §1056(d)(3), creditor-protection consultation for
  high-liability professions, beneficiary-form-dispute escalation),
  Plan-fiduciary-breach claims under ERISA §404 / §405. Boundary
  `legal-disputes` and `health-insurance` D3 / D8 / D10 (parallel
  ERISA-pre-emption framing on the insurance side). Refer at any
  six-figure-plus retirement-account dispute or post-divorce QDRO
  drafting — procedural errors are unrecoverable; ERISA pre-empts
  state-court remedies under 29 USC §1144(a).
- **State insurance / securities regulator and SEC IAPD / FINRA
  BrokerCheck** — verification floor on any advisor recommendation.
  brokercheck.finra.org for FINRA-registered broker-dealers
  (Series 7 / 65 / 66); SEC IAPD at adviserinfo.sec.gov for SEC-
  registered investment advisers (Form ADV part 2A; disclosure
  events; compensation structure). This is a $0 zero-friction step
  that catches advisors with material disciplinary histories
  (suspensions, customer disputes, criminal records). The Editor
  surfaces this anchor on EVERY individual-professional
  recommendation, not as over-referral but as a procedural safety
  check. State-insurance / state-securities regulators handle
  fraud-on-elderly / annuity-mis-selling complaints below the SEC
  IAPD threshold.
- **SHIBA / SHIP volunteer for Medicare-coordination side of D8** —
  federally-funded under SSA §4360, non-commissioned, plan-agnostic;
  the structural counterweight to broker / agent commission-driven
  recommendations on Medicare Advantage vs Original-Medicare-with-
  Medigap at IEP. Refer by state when D8 spans personal-finance ↔
  health-insurance (SS-claim-age coordinated with Medicare Part B
  IEP and IRMAA-tier management). Boundary `health-insurance` D4 /
  D8.

When the situation matches a trigger for one of these categories,
the Editor's Recovery move names that *specific* category — not
"consult a professional" generic. Over-referral (naming a category
that does not match a trigger) is *also* a failure mode the Critic
flags — see the Critic section below. The uniform Mechanism E
posture here means "every output names *some* specific category
keyed to the decision class," not "every output names every
category." For multi-decision spans (D7+D8 + IRMAA / ACA-MAGI in a
bridge year), naming CPA AND fee-only CFP IS appropriate because the
spans genuinely require both; this is not over-referral.

**Don't soften the high-density blindspot anchors.** Per
[`decisions.md`](./decisions.md) "Notes for downstream layers,"
decisions D1, D5, D6, D7, D10 are highest-density blindspot anchors,
and D7 / D8 / D10 carry the highest single-misstep tail risk:

- D1: pro-rata-IRA-trap on backdoor-Roth (the canonical "I thought I
  was doing the right thing" mistake — surface the SEP-IRA / SIMPLE-
  IRA / rollover-IRA aggregation prominently)
- D5: PSLF-aggressive-payoff-destroys-forgiveness (the canonical
  "math-correct, policy-wrong" mistake — refi-to-private-or-pay-off-
  early disqualifies)
- D6: wash-sale-into-spouse's-IRA (the canonical "household-
  aggregation-rule-ignored" mistake — the disallowed loss is
  permanently lost into the spouse's IRA basis)
- D7: Roth-conversion-recharacterization-no-longer-available
  irreversibility (TCJA 2017 IRC §408A(d)(6)(B)(iii) — the
  canonical "I'll undo it if I change my mind" mistake)
- D10: stale-beneficiary-form-supersedes-current-will (the canonical
  Egelhoff-class horror story — the single highest-leverage zero-
  cost preventive move available across the entire domain; surface
  on ANY estate-and-beneficiary framing regardless of context)

When the Risk Officer surfaces a blindspot tied to these decisions,
it ships in the final output verbatim — Editor hedging on Roth-
conversion irrevocability, Egelhoff-class beneficiary-form errors,
PSLF-destroyed-by-payoff, or wash-sale-into-spouse's-IRA is exactly
the Critic-failing brand of padding the high-stakes regime was
written to catch.

**Opposing-framing surfacing is mandatory.** Per
[`framings.md`](./framings.md) "Cross-framing tensions," every Editor
output on a personal-finance situation must surface at least one
blindspot from the framing OPPOSITE the asker's apparent one (F1↔F14,
F2↔F12, F3↔F6, F4↔F6, F5↔F14, F7↔F9, F8↔F1, F10↔F11, F13↔F7). The
opposing framing's `Excludes` line is the seed; surface it as a "here
is the lens your question's vocabulary excluded" paragraph, not a
buried bullet. F11 / F12 / F10 are meta-framings that apply on top of
any primary decision framing — surface them when the asker's prompt
expresses time-or-literacy constraint (F10 vs F11) or system-skepticism
(F12 as policy-hedge against F2 / F4), but never as the sole framing.

**Cross-domain handoff.** When the situation crosses `tech-career`
(equity comp dominant — most common edge), `health-insurance` (HSA-as-
retirement / IRMAA / ACA-MAGI / Medicare-Part-A retroactivity),
`entrepreneurship` (solo-401(k) / SEP / QBI / QSBS),
`housing` (mortgage-vs-invest / cash-out-refi / Section-121
exclusion), `family-planning` (529-superfund / SLAT / pre-2026-
sunset), `education-funding` (PSLF / IDR / 529-vs-Roth), or
`legal-disputes` (QDRO / creditor-shield), name the coupling
explicitly — e.g. "the Roth-conversion-ladder and the ACA-marketplace-
APTC decisions are coupled here because both depend on MAGI in the
same tax year, AND the 2-year-lookback IRMAA implication of an
aggressive conversion in 2026 will hit Medicare Part B + D premiums
in 2028; F2's tax-arbitrage lens applies to one side, F12's policy-
volatility lens applies to both, and the CPA referral should
coordinate with the SHIP / SHIBA volunteer on the Medicare side."
Do not silo the personal-finance discussion when the asker's
situation spans domains.

---

## Critic

Generic Critic rules from
[`src/blindspot/prompts/critic.md`](../../src/blindspot/prompts/critic.md)
apply unchanged. The additions below tune the per-claim spot-check
for personal-finance-specific claim categories. Because the domain
is `high_stakes: true` AND is the canonical Mechanism E gating case,
**every numeric, statutory, or regulatory claim is subject to
mandatory per-claim grounding** — the generic "recommended" spot-
check is upgraded to hard pass / fail here, in the same uniform shape
as immigration's Critic per PR #53 and health-insurance's Critic per
PR #88 (NOT the targeted-only shape of housing's Critic per PR #69).

**Per-numeric-claim citation is mandatory** for any sentence
containing:

- An IRC statutory cite (IRC §72(t) early-withdrawal-and-exceptions;
  §83(b) restricted-stock-election; §125 cafeteria plan; §219(b)
  traditional-IRA cap; §219(g) deduction phase-out; §223 HSA;
  §401(a)(9) RMD; §401(k); §402(c)(3) 60-day-rollover; §408 IRA;
  §408(d)(2) pro-rata; §408(d)(3) 12-month-one-rollover;
  §408(d)(8) QCD; §408A Roth-IRA; §408A(c)(2) Roth-IRA cap;
  §408A(c)(3) Roth-IRA phase-out; §408A(d)(6) recharacterization-
  eliminated; §415(c) overall-DC-limit; §422 ISO; §423 ESPP;
  §457(b) governmental-deferred-comp; §529 529-plan;
  §530 Coverdell; §1014 basis-step-up; §1091 wash-sale; §1202
  QSBS; §1411 NIIT; §3101 FICA; §4974 RMD-excise; §4975 prohibited-
  transaction; §6651 failure-to-file)
- A SECURE / TCJA / ARPA / Tax Reform statutory cite (SECURE 1.0
  §401 → §401(a)(9)(H) 10-year-rule; SECURE 2.0 §107 RMD-age-73-75;
  SECURE 2.0 §109 age-60-63-super-catch-up; SECURE 2.0 §302 RMD-
  excise-reduced; SECURE 2.0 §126 529-to-Roth-rollover-$35k;
  TCJA 2017 §11061 doubled-estate-exemption-with-2025-sunset;
  TCJA §13611 Roth-recharacterization-elimination; ARPA 2021
  §9661 ACA enhanced-subsidy through 2025; SS Fairness Act 2024
  WEP-and-GPO repeal)
- A Treasury Regulation cite (Treas. Reg. §1.401(a)(9) RMD regs;
  §1.408A-4 Roth-IRA regs; §20.2010-1 anti-clawback; §1.529-1
  529-plan regs; §1.401(k)-1 401(k) regs)
- An IRS-issued cite (Rev. Rul. 2008-5 wash-sale-into-IRA;
  Rev. Rul. 78-406 once-per-12-month-rollover; IRS Notice 2014-54
  after-tax-401(k)-step-doctrine; IRS Notice 2014-7 Medicaid-waiver-
  payments; IRS Pub 590-A IRA contributions; IRS Pub 590-B IRA
  distributions; IRS Pub 969 HSA / HRA / FSA; IRS Pub 575 Pension
  and Annuity Income; Form 8606 / 8889 / 5498 / 1099-R / 5329
  references)
- An ERISA cite (29 USC §1056(d)(3) QDRO; 29 USC §1132 civil
  enforcement; 29 USC §1144(a) state-law pre-emption; ERISA §404
  fiduciary-duty; ERISA §405 co-fiduciary liability; ERISA §206(d)
  anti-alienation; 11 USC §522(d)(12) ERISA-401(k)-unlimited-
  bankruptcy-exempt; 11 USC §522(n) IRA-bankruptcy-exempt-cap-
  indexed)
- A Supreme Court / Tax Court precedent (*Egelhoff v Egelhoff Ex rel
  Breiner*, 532 U.S. 141 (2001); *Kennedy v Plan Administrator for
  DuPont Savings*, 555 U.S. 285 (2009); *Clark v Rameker*, 573 U.S.
  122 (2014); *Bobrow v Commissioner*, TC Memo 2014-21 once-per-12-
  month-rollover)
- A specific dollar threshold or annual contribution cap (Roth-IRA
  $7,000 / $8,000 catch-up 2025; 401(k) $23,500 + $7,500 + $11,250
  for 2025; §415(c) $70,000 2025; HSA $4,300 / $8,550 plus $1,000
  catch-up 2026; SEP-IRA 25%-of-net-SE; 529 superfund $95k / $190k;
  NIIT $200k / $250k MAGI; IRMAA 2026 $103k / $129k / $161k /
  $193k / $500k; 0%-LTCG $48,350 / $94,050 2025; estate exemption
  $13.99M / $27.98M 2025 sunsetting to ~$7M 2026)
- A specific day / month / year clock (60-day-indirect-rollover; 30-
  day-wash-sale-before-and-after; 30-day-83(b)-election-deadline;
  5-year-Roth-conversion-aging-clock; 5-year-Roth-IRA-establishment-
  clock; 5-year-QSBS-hold; 12-month-one-rollover-per-IRA; 10-year-
  inherited-IRA-drawdown; 18-month-or-22.5%-COBRA boundary; 10-year-
  marriage-test-for-divorced-spouse-SS; April-15-Roth-IRA-tax-year-
  deadline-no-extension)
- A specific age (59.5 early-withdrawal; 50 catch-up; 55 HSA-catch-
  up; 60-63 super-catch-up; 70.5 QCD; 67 FRA; 73 / 75 RMD; 62
  earliest-SS; 21 EDB-minor-child)
- A specific percentage / penalty math (10% early-withdrawal IRC
  §72(t); 25% RMD-excise reduced from 50%, further reduced to 10%
  if corrected; 3.8% NIIT; 0% / 15% / 20% LTCG; 30% claim-at-62-PIA-
  reduction; 8%-per-year delayed-retirement-credit; 7% / 8% rule-
  of-thumb-equity-risk-premium; 4% Bengen-safe-withdrawal; 3.5%
  FIRE-50-year-safe-withdrawal)
- An AGI / MAGI cliff or bracket claim (NIIT 3.8% at $200k / $250k
  MAGI; IRMAA brackets and 2-year-lookback; Roth-IRA phase-out;
  ACA-MAGI 400%-FPL cliff or sliding scale; 0%-LTCG-bracket; QSBS
  $10M-or-10x-basis cap; estate exemption sunset)
- A QSBS / Section-1202 specific claim, an §83(b) election claim,
  or an §72(t) SEPP-modification claim
- A state-shield-law claim (TX / FL unlimited IRA-protection vs CA
  post-bankruptcy-only vs NY partial — specify state)
- An ERISA-pre-emption claim or a QDRO drafting claim

If any such sentence lacks an adjacent `[doc-X]` marker citing a
source-view in [`sources.yaml`](./sources.yaml), set
`regenerate_required = true` AND name the uncited specific verbatim
in `feedback`. Citation-recycling (one marker reused across distinct
numeric claims) fails the same check. This is stricter than the
housing partial-gating rule because personal-finance fabrications
cause irrevocable harm — a wrong Roth-conversion-irreversibility
claim or a wrong IRMAA-bracket cite cannot be undone by a follow-up
correction the way a wrong PMI threshold can.

**Specificity bar.** Generic phrases that pass the standard Critic
check are STILL fails in this domain. The shapes below all *look*
specific (they name a mechanism) but contain no statute, no clock,
no dollar threshold:

- "Be careful about the pro-rata rule" (no IRC §408(d)(2) cite, no
  Form 8606 reference, no all-pre-tax-IRA-aggregation-mention) —
  fail.
- "Roth conversions can't be undone" (no TCJA 2017 cite, no IRC
  §408A(d)(6)(B)(iii) cite, no "since 2018" timing) — fail.
- "Watch out for wash sales" (no 30-day-window, no IRC §1091, no
  household-aggregation-Rev-Rul-2008-5, no substantially-identical
  determination guidance) — fail.
- "The 4% rule says you can withdraw 4% safely" (no Bengen-1994-
  origin, no 30-year-retirement-calibration, no FIRE-3.5%-for-50-
  year-modifier, no sequence-of-returns-risk-mention) — fail.
- "PSLF can forgive your loans" (no 120-qualifying-payments, no
  qualifying-employer-test, no tax-free-IRC-§108(f)(1)-vs-IDR-tax-
  bomb distinction, no "refi-or-payoff-destroys-eligibility") —
  fail.
- "Social Security has spousal benefits" (no FRA-vs-claim-age math,
  no survivor-benefit-locks-higher-earner cite, no divorced-spouse-
  10-year-marriage-test, no Social Security Fairness Act 2024
  WEP/GPO-repeal note) — fail.
- "RMDs start at 73" (no SECURE 2.0 §107 cite, no born-1960+-age-75
  distinction, no 25%-excise-reduced-from-50%, no QCD-at-70.5-
  alternative-IRC-§408(d)(8)) — fail.
- "Beneficiary forms are important" (no Egelhoff cite, no will-
  supersession mechanic, no TOD-POD-on-taxable, no zero-cost-
  preventive-move framing) — fail.
- "Consider talking to a CPA or financial planner" (no specific
  category named per the Editor's referral matrix, no fee-only-vs-
  AUM distinction, no BrokerCheck-verification anchor) — fail when
  used as a substitute for analysis; pass only as the Mechanism E
  label on decision-support framing PLUS a specific-category
  recommendation.
- "401(k) is creditor-protected" (no ERISA-vs-IRA distinction, no
  11 USC §522 cites, no Clark-v-Rameker inherited-IRA exception,
  no state-shield-variation note) — fail.

Mark specificity as `fail` and name the offending sentence verbatim
in `feedback`.

**Non-obviousness floor — `+1` for multi-route situations.** When
the matched persona spans multiple decisions or covers an opposing-
framing pair simultaneously (e.g. `dual-w2-household-rsu-heavy` who
is also `backdoor-roth-with-existing-trad-IRA-balance`; or
`roth-conversion-bridge-year-50s-or-60s` who is also `early-retiree-
aca-magi-managing`; or `near-rmd-age-72-to-75` who is also
`pre-2026-sunset-slat-or-gift`), raise the non-obviousness floor by
one point. A 3/5 that would pass for a single-route asker is a 2/5
here. Multi-route askers have already heard the single-route advice;
surfacing only what they already know fails non-obviousness. This is
the personal-finance parallel to tech-career's `comparing-offers-*`
non-obviousness raise, immigration's multi-route raise, and health-
insurance's multi-decision raise.

**Cross-framing tension as a quality signal.** When the Risk Officer
surfaces blindspots from a framing OPPOSITE the asker's apparent one
(F1↔F14, F2↔F12, F3↔F6, F4↔F6, F5↔F14, F7↔F9, F8↔F1, F10↔F11, F13↔F7
— see Triage above), that typically raises non-obviousness by 1
point because the asker's vocabulary already excluded the opposing
framing. Score accordingly — the opposing-framing surfacing is the
highest-leverage signal that the answer is doing the asker's framing-
correction work, not just restating their starting position. F11 / F12
/ F10 meta-framings surfaced as meta-context do NOT count toward this
signal in isolation; meta-context surfacing is its own quality
dimension and should not be conflated with opposing-framing decision-
support.

**Specific-professional-referral check (both over- and missed-
referral fail).** Because personal-finance uses uniform Mechanism E
gating with a *selective* professional-referral matrix (the
*category* varies by decision class — fee-only CFP vs retirement-
experienced CPA vs fee-only SS-claiming specialist vs state-bar
estate attorney vs ERISA attorney vs SHIBA / SHIP volunteer vs
SEC IAPD / FINRA BrokerCheck verification; see the Editor
"Selective-professional-referral matrix" above), the Critic verifies
two complementary failure modes:

- **Over-referral / wrong-category-referral.** If a Recovery move
  names a category whose trigger does NOT match the matched
  decision class (e.g. naming "consult an ERISA attorney" for a D1
  Roth-vs-traditional contribution-ordering question where no
  fiduciary-breach is alleged; or naming "fee-only SS-claiming
  specialist" for a D5 debt-payoff-vs-invest question; or naming
  "state-bar estate attorney" for a D6 tax-loss-harvesting
  question; or naming "AUM advisor" rather than "fee-only fiduciary
  CFP" anywhere — the AUM-vs-fee-only distinction is load-bearing
  per F10), set `regenerate_required = true` and name the
  unjustified referral verbatim in `feedback`. Generic "consult a
  financial advisor" without category specification ALSO fails this
  check — the uniform Mechanism E posture requires *specific
  category* keyed to the decision, not blanket-generic deferral.
- **Missed-referral.** If the situation matches a trigger from the
  Editor referral matrix but the Recovery is self-directed or names
  the wrong category at lower stakes (e.g. omits "retirement-
  experienced CPA" on a D1 Mega-Backdoor or D7 Roth-conversion-
  ladder situation; omits "state-bar estate attorney" on a D10
  estate-and-beneficiary or pre-2026-sunset SLAT situation; omits
  "fee-only SS-claiming specialist" on a D8 SS-claim-age decision;
  omits "ERISA attorney" on a divorce + QDRO division; omits
  "BrokerCheck / IAPD verification" when any individual professional
  is named), also fail with `regenerate_required = true` and name
  the missed referral category verbatim in `feedback`. Missed-
  referral on a high-stakes trigger is itself a Mechanism E failure
  mode under the canonical-gating-case framing — under-referral
  creates harm symmetrically to over-referral degrading signal,
  AND personal-finance is where the gate is most load-bearing
  precisely because the harm class (dollar-specific guidance with
  irrevocable tax consequences) was the gate's authoring case.

The matrix is keyed by decision in the Editor section; the Critic's
check is to verify the match. Both directions matter.

**Dollar-specific-investment-guidance check (load-bearing canonical
gate).** Because personal-finance is the canonical Mechanism E
gating case named in ROADMAP §5, the Critic enforces a hard pass /
fail on dollar-specific investment guidance:

- If the final output names a specific security (individual stock
  ticker, individual bond CUSIP, specific ETF ticker beyond
  illustrative category like "a broad US total-market index ETF"),
  set `regenerate_required = true` and name the violating sentence
  verbatim in `feedback`. Categorical recommendations (US total
  stock market index, intermediate-term Treasury bond fund, target-
  date fund matching the asker's retirement year, three-fund-
  Bogleheads-style portfolio, low-cost broadly-diversified index
  ETF) PASS — these are decision-support framings, not financial
  advice. The line is at the specific ticker / specific CUSIP / vs
  the category.
- If the final output names a specific dollar amount tailored to
  the asker's stated portfolio (e.g. "buy $300,000 of VTI"; "put
  60% of your $500k inheritance in stocks and 40% in bonds";
  "convert exactly $75,000 to Roth this year"), set
  `regenerate_required = true` and name the violating sentence
  verbatim. Illustrative dollar amounts that explicitly disclaim
  applicability to the asker ("the IRS contribution cap is $23,500
  for 2025"; "the standard deduction is $14,600 single / $29,200
  MFJ"; "the IRMAA tier-1 threshold is $103,000 single") PASS —
  these are statutory / regulatory limits that ARE the
  decision-support content.
- If the final output names a specific allocation-percentage
  tailored to the asker's named situation (e.g. "given your $1.2M
  net worth and age 45, allocate 65% stocks / 25% bonds / 10%
  cash"), set `regenerate_required = true`. Generic allocation-
  glide-path framings ("a common rule-of-thumb is age-in-bonds,
  though it's been criticized as too conservative for households
  with long horizons") PASS — they're framing, not personalized
  advice.

This check is independent of the over-referral / missed-referral
check above; both can fire simultaneously.

**Mechanism E label check.** If the final output lacks the
decision-support / not-financial-advice / consult-specific-
professional language required of every high-stakes-domain answer
(see Editor section above), set `regenerate_required = true`
regardless of other quality dimensions. This is non-negotiable per
[ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)
and is MORE strict here because personal-finance is the canonical
gating case. Soft variants ("you might want to talk to a financial
advisor eventually") fail the check; the language must be explicit
decision-support framing PLUS an explicit specific-category-of-
professional recommendation PLUS an explicit no-dollar-specific-
guidance disclaimer, and for the highest-stakes situations (D7 Roth-
conversion-ladder irrevocability, D8 SS-claim-age and RMD, D10
estate-and-beneficiary structuring with sunset window, anything with
a six-figure ERISA-plan dispute or QDRO drafting) the label belongs
at the head of the answer rather than the tail.

---

## Notes for refine

- This file is `delta`, not duplication. If a future refine wants to
  add another persona, risk-surface, statute citation category, or
  claim shape, prefer editing the relevant short list above to
  growing the file beyond its current word count.
- The opposing-framing pairs (F1↔F14, F2↔F12, F3↔F6, F4↔F6, F5↔F14,
  F7↔F9, F8↔F1, F10↔F11, F13↔F7; F11 / F12 / F10 as meta-context) are
  the highest-leverage routing tuning in this file. If eval shows the
  Risk Officer underusing the opposing-framing surface on personal-
  finance situations, sharpen the Triage `active_framings` section
  first.
- The selective-professional-referral matrix is the second-highest-
  leverage tuning. The matrix is uniform-gating-with-specific-
  category — every output names some category, but the category
  varies by decision class. If eval shows over-referral patterns
  (ERISA attorney named for non-fiduciary-dispute decisions; estate
  attorney named for non-D10 decisions; "consult a financial advisor"
  generic), tighten the Critic specific-professional-referral check
  first; if eval shows missed-referral patterns (self-directed
  Recovery on Mega-Backdoor or Roth-conversion-ladder; no CPA on
  pro-rata-trap situations; no SS-specialist on D8; no estate
  attorney on pre-2026-sunset SLAT), tighten the Editor referral
  matrix's trigger anchors.
- The dollar-specific-investment-guidance gate is the third-highest-
  leverage tuning AND the most domain-canonical. If eval shows the
  Editor crossing the line into specific-ticker / specific-dollar /
  specific-allocation-percentage personalized advice, tighten the
  Critic dollar-specific-investment-guidance check first; the Editor
  rule is uniform-categorical-only-no-personalized. Personal-finance
  is the canonical Mechanism E gating case in ROADMAP §5 — the gate
  is most-stringently enforced here.
- High-stakes propagation: this file currently says `high_stakes:
  true` per [`_meta_ontology.md` §5](../_meta_ontology.md). The
  Editor Mechanism E label and Critic mandatory-grounding rules
  above are load-bearing on that flag. If `_meta_ontology.md` ever
  softens that flag (extremely unlikely for personal-finance — it is
  the named canonical case), the corresponding rules here must be
  removed in the same change.
- Date-stamp risk: anchor numbers above (annual contribution caps,
  AGI / MAGI cliffs, IRMAA brackets, 0%-LTCG-bracket, estate
  exemption, IRC §408(d)(8) QCD cap, NIIT thresholds, ACA-MAGI cliff
  if ARPA enhanced subsidies expire post-2025) all inherit the date-
  stamp risk [`blindspots.md`](./blindspots.md) Maturity / source-
  anchor note enumerates. Re-check before tightening any dependent
  Critic rule. Specific watch items:
  - **2025 doubled-estate-exemption sunset Dec 31 2025** — exemption
    falls from $13.99M/$27.98M to ~$7M/$14M-indexed Jan 1 2026
    absent congressional extension; anti-clawback Treas. Reg.
    §20.2010-1 protects pre-2026 gifts. Re-verify before any 2026-
    forward edit.
  - **TCJA 2017 income-tax-bracket sunset Dec 31 2025** — pre-2018
    brackets return (10/15/25/28/33/35/39.6%) absent extension;
    F2 marginal-rate arbitrage calculations need re-grounding.
  - **ARPA / IRA enhanced-subsidy sunset end of 2025** (boundary
    `health-insurance`) — the 400%-FPL "subsidy cliff" returns
    absent extension; ACA-MAGI cliff management for early-retirees
    changes shape.
  - **2026 IRS contribution caps** — verify annually around late Q4
    / early Q1 (IR-news-release).
  - **2026 IRMAA brackets** (boundary `health-insurance`) — verify
    annually; the 2-year-lookback means 2026 conversions hit 2028
    Medicare premiums and the brackets in effect at 2028 may
    differ.
  - **SECURE 2.0 §126 529-to-Roth $35k rollover** (effective 2024)
    — 15-year-account-age requirement and annual-Roth-contribution-
    cap-coordination; final regs may further constrain.
  - **Social Security Fairness Act 2024** (Public Law 118-273,
    enacted Jan 2025) — WEP and GPO repealed; D8 framings written
    against pre-repeal mechanics need re-grounding.
- Cross-domain density: `personal-finance` ↔ `tech-career` is the
  densest edge on equity-comp surfaces; `personal-finance` ↔
  `health-insurance` is the densest edge on referral routing (HSA-
  as-triple-tax-advantaged-retirement, IRMAA 2-year-lookback, ACA-
  MAGI cliff). When `tech-career/domain_pack.md` or `health-
  insurance/domain_pack.md` (PR #88) updates, cross-check
  CPA-referral and SHIBA-referral triggers against the parallel
  rules there.
- The uniform Mechanism E posture here (every output names a
  specific category PLUS a dollar-specific-investment-guidance
  gate) is the strictest in the entire V2 ontology because
  personal-finance is the canonical case named in ROADMAP §5. The
  difference from housing's partial-gating, tech-career's locally-
  gated equity-tax-only posture, and even health-insurance /
  immigration's uniform-but-not-dollar-gated posture is grounded
  in the three-irrevocability-classes intro: tax-year-boundary one-
  shot windows compound for years; Social Security and RMD permanent
  penalties never amortize; missed annual contributions compound at
  the equity risk premium for 30+ years. Housing's "buy the wrong
  house, sell and refi" recoverability does not exist here.
