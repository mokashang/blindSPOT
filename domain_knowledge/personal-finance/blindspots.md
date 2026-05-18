# personal-finance — blindspots.md (Layer 3)

Blindspot catalogue for `personal-finance`. Each entry names what a
real practitioner in the relevant framing would say is missed —
anchored to either an `Excludes` line in
[`framings.md`](./framings.md), a cross-domain edge flag in
[`decisions.md`](./decisions.md), or to the conceptual community-class
voice anchors named in `framings.md` (fee-only-fiduciary-CFP voice
— NAPFA / XY-Planning / Garrett; Bogleheads voice; Mr-Money-Mustache /
ChooseFI / FIRE voice; financial-economics-journalism voice — Wessel /
Sommer / Tergesen; retirement-econ academic voice — Pfau / Kitces /
Kotlikoff; The Finance Buff voice; retirement-experienced-CPA voice;
ERISA-practitioner voice; SEC-EDGAR / FINRA-BrokerCheck voice; IRS-
publication-authority voice — Pub 550 / 590-A / 590-B / 525 / 969 /
970; fee-only Social-Security-claiming-specialist voice — Mike Piper
Open-Social-Security / Kotlikoff Maximize-My-Social-Security / SHIBA /
SHIP; state-bar-estate-attorney voice; personal-finance-influencer
voice — Orman / Ramsey / Sethi; chronic-DIY-Reddit voice —
r/personalfinance / r/Bogleheads / r/financialindependence / r/tax).
Per [`_schema.md`](../_schema.md), every entry is relative to a
framing and ships with a trigger pattern and a concrete recovery move.

The `personal-finance` domain is **high_stakes: true** per
[`_meta_ontology.md` §5](../_meta_ontology.md) AND is the canonical
Mechanism E gating case named in
[ROADMAP §5](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating).
**Every Recovery move below routes to one of the following
professional-counsel categories — a fee-only fiduciary CFP (NAPFA /
XY-Planning-Network / Garrett-Planning-Network — fee-only NOT
fee-based), a retirement-and-equity-comp-experienced CPA (Form 8606 /
Form 8889 / Form 8949 / Form 1099-R reconciliation depth; NOT generic
tax-prep CPA), a fee-only Social-Security-claiming specialist (Mike
Piper's Open-Social-Security, Kotlikoff's Maximize-My-Social-Security)
or SHIBA / SHIP volunteer for Medicare-coordination side, a state-bar-
licensed estate attorney (trust formation, SLAT / GRAT / Dynasty /
ILIT / CRT / CLT drafting, 2025-doubled-exemption-sunset planning), an
ERISA attorney (high-balance 401(k) disputes, Rule-of-55 / SEPP-72(t)
plan-document review, post-divorce QDRO drafting, creditor-protection
consultation), or SEC IAPD / FINRA BrokerCheck procedural verification
on any individual advisor before engagement.** This is **uniform
Mechanism E gating** like immigration (PR #48) and health-insurance
(PR #75), not partial-gating like housing (PR #64). The three classes
of irrevocability driving the high-stakes posture (per `framings.md`
intro) are: **tax-year-boundary one-shot windows** (Roth-conversion-
recharacterization permanently eliminated by TCJA 2017; contribution
caps cannot be re-made after April 15 / Oct 15; backdoor-Roth pro-rata
turns on Dec-31 IRA balances; 5-year-Roth-conversion clocks start
per-conversion-per-year); **permanent Social-Security / Medicare-
adjacent penalties** (claim-age-before-FRA permanently reduces PIA
~30% at 62 and compounds for the survivor's life via higher-earner-
survivor rule; 60-day-indirect-rollover-window missed turns the
distribution into a taxable event with no second chance; missed
Medicare IEP triggers permanent Part-B 10%-per-12-months-late premium
add); and **compounding-cost-of-procrastination** (a missed $7,000
Roth-IRA contribution at age 30 compounds to ~$76k at age 65 at a 7%
real return; cap-room is per-year-use-it-or-lose-it). The wrong call
here is not recoverable on a multi-year horizon. This file IS
decision-support, NOT licensed-fiduciary / CPA / ERISA-attorney /
state-bar-estate-attorney / Social-Security-specialist / SHIBA advice.
The framings name where the analysis happens; the binding
determination on any specific decision comes from the professional
with case-specific facts — current Summary Plan Description, current
state-of-residence shield law, current IRS revenue rulings, current
SSA Trustees Report and benefit projections, the asker's full income
and family picture, and the asker's full beneficiary-form history.
**Dollar-specific investment recommendations on individual securities
(buy $X of TICKER today with your $Y) are uniformly out-of-scope at
the Editor layer regardless of which framing is active** — this is
the load-bearing gate the domain was written around.

Each blindspot lists:
- **Statement** — one sentence naming what is missed
- **Source evidence** — the framing-Excludes anchor, `decisions.md`
  cross-domain edge flag, or community-class voice-anchor reference
  this blindspot was extracted from (not invented; no purely-LLM-
  extrapolated entries)
- **Trigger** — the situation pattern the Triage / Risk Officer should
  match against
- **Failure mode** — the specific bad outcome if the blindspot stays
  unsurfaced (irrevocable Roth-conversion sized into next bracket,
  permanent SS-claim-age penalty, missed contribution-cap window,
  Form 8606 basis-tracking failure leading to CP2000, inherited-IRA
  exposure to bankruptcy, etc.)
- **Recovery move** — the concrete action that resolves it, routing
  to one of the Mechanism E professional-counsel categories above

The framing names below match [`framings.md`](./framings.md) exactly;
all 14 are covered with ≥ 5 entries each (≥ 70 total). Voice anchors
are conceptual — the source-views in
`domain_knowledge/personal-finance/sources.yaml` are not yet authored,
so attribution is to the *class* of community (fee-only-fiduciary-CFP
voice, Bogleheads voice, FIRE voice, financial-economics-journalism
voice, retirement-econ academic voice, The Finance Buff voice,
retirement-experienced-CPA voice, ERISA-practitioner voice, SEC-EDGAR
/ FINRA-BrokerCheck voice, IRS-publication-authority voice, fee-only
Social-Security-claiming-specialist voice, state-bar-estate-attorney
voice, personal-finance-influencer voice, chronic-DIY-Reddit voice).
When `sources.yaml` lands, source-evidence lines below should be
tightened to specific source-view ids.

---

## 1. Investment-priority-order framing

### 1.1 Match-vesting-cliff makes "always max the match" job-tenure-conditional

- **Statement**: The "100% match dominates 25% credit-card-APR" reflex
  is correct on long-horizon IRR math but rarely engages with
  *match-vesting cliffs* — many 401(k) plans have 1-to-6-year cliff
  or graded vesting on the employer match, and an asker who is
  reasonably-likely to leave before vesting (FAANG median tenure
  ~2 years; PIP / RIF probability non-trivial) faces an
  "expected-match-after-vesting" that is materially less than 100%,
  often closer to 30-60% on a probability-weighted basis.
- **Source evidence**: `framings.md` §1 Excludes line on
  match-vesting cliffs and job-tenure-conditioned expected value;
  reinforced by retirement-experienced-CPA voice and Bogleheads
  forum threads on vesting-schedule arithmetic. `decisions.md` §D1
  cross-domain edge into `tech-career`.
- **Trigger**: Asker is in tech / early-career / contract-to-hire /
  startup AND mentions a cliff-vested or graded-vested 401(k) match
  AND is below their tenure-to-cliff AND is reasoning about
  "max the match" as if dollar-for-dollar.
- **Failure mode**: Asker reduces taxable savings to "capture the
  match" worth $11.7k/yr; departs the employer 14 months later (no
  vesting cliff hit yet on a 3-year cliff plan); employer claws back
  the entire match; asker has foregone after-tax brokerage savings
  for two years to capture a $0 actual match. The opportunity-cost
  of cash that could have funded emergency-fund / Roth-IRA / taxable
  is the real loss.
- **Recovery move**: Read the 401(k) plan-document (Summary Plan
  Description) for the exact vesting schedule; build a probability-
  weighted expected-match table conditioned on the asker's realistic
  tenure horizon; if expected-match-after-vesting falls below 60%,
  consult a retirement-and-equity-comp-experienced CPA on whether
  the priority-order should down-weight step 1 in favor of taxable-
  brokerage liquidity until vesting is closer. Verify CPA via SEC
  IAPD / FINRA BrokerCheck before engagement.

### 1.2 HSA step-3 priority assumes HDHP-side medical math is neutral

- **Statement**: Step 3 (HSA-as-stealth-IRA) treats HDHP-enrollment
  as a free upgrade once HSA-eligibility opens, but the HDHP-vs-PPO
  trade-off on the medical-coverage side can dominate the HSA tax
  arbitrage for households with chronic conditions or expected high
  utilization (cancer survivor, pregnancy planning, child with
  autism / ABA-therapy, parent on biologics). The framing's "step 3
  dominates step 4" elides the medical-cost-on-the-HDHP-side
  calculation entirely, and a $4,300 HSA tax arbitrage at 32%
  marginal ($1,376) is dominated by $8,300 of additional family-
  HDHP-deductible exposure in a high-utilization year.
- **Source evidence**: `framings.md` §1 Excludes line on HDHP-vs-PPO
  trade-off dominating the HSA arbitrage for high-utilization
  households; cross-domain edge into `health-insurance` D1, F1 per
  `decisions.md` §D1. Reinforced by The Finance Buff voice and
  Bogleheads HSA-vs-PPO forum threads.
- **Trigger**: Asker is at OE choosing between HDHP and PPO AND has
  any of: chronic-condition household-member, planned pregnancy in
  next 12 months, child with developmental / behavioral therapy
  needs, household member on $1k+/month specialty drug or biologic,
  asker over 50 with rising utilization.
- **Failure mode**: Asker chooses HDHP for the "stealth IRA" tax
  arbitrage; high-utilization member triggers $40k of in-network
  care; asker hits family OOP-max but pays the full $8,300 family
  HDHP deductible before coverage kicks in; net-of-tax-arbitrage
  cost is $5k-$10k higher than PPO would have been. 12-month plan-
  year lock-in forecloses correction.
- **Recovery move**: For OE plan-choice questions, route into the
  `health-insurance` domain's F1 (expected-utilization arithmetic)
  framing before committing to HDHP on tax-arbitrage grounds; pull
  the SPD for HDHP and PPO and build the probability-weighted total-
  cost table including HSA-tax-arbitrage as a line item not a
  decision-driver. For high-utilization candidates, consult a
  licensed health-insurance broker on the medical-coverage side AND
  a retirement-experienced CPA on the HSA-tax-arbitrage side
  separately — the trade-off is two distinct expert domains.

### 1.3 Dual-W-2-couple priority order is structurally absent from single-asker flowchart

- **Statement**: The framing assumes the asker has *one* set of
  vehicles available — but dual-W-2 couples have *two* 401(k)s,
  *two* HSAs (only one if family-HDHP-coverage on one spouse's plan
  — per IRC §223(b)(5) the family-HDHP-coverage limits one HSA per
  spouse to the family cap), *two* Roth-IRA caps; the cross-spouse-
  coordination layer is structurally absent from the single-asker
  flowchart, and the optimal joint sequence isn't simply "each
  spouse runs the flowchart on their own paycheck."
- **Source evidence**: `framings.md` §1 Excludes line on dual-W-2-
  couple absent from single-asker flowchart; reinforced by
  Bogleheads forum threads on spousal-IRA rules and HSA-family-
  coverage-restriction-to-one-account, and by The Finance Buff voice
  on cross-spouse coordination.
- **Trigger**: Asker is in a dual-W-2 household AND is running the
  priority-order flowchart on their own paycheck without engaging
  the cross-spouse layer AND has not separately identified which
  spouse claims the HSA family-cap, whether spousal-IRA rules apply,
  or how to coordinate Roth-IRA-eligibility-via-MFJ-MAGI vs spousal-
  income-based contributions.
- **Failure mode**: Both spouses contribute to separate HSAs at the
  family cap thinking they each get $8,550; IRS treats the excess
  as a $4,300+ overcontribution subject to 6% excise tax annually
  until withdrawn (Form 5329); OR couple misses spousal-IRA
  eligibility for non-working spouse and forgoes $7,000/year cap
  room; OR couple over-contributes Roth-IRA based on individual-
  income test instead of MFJ-MAGI test and faces 6% excise on
  excess. Each error compounds annually with the missed-correction.
- **Recovery move**: For dual-W-2 households, build the *joint*
  priority-order spreadsheet covering both spouses' caps,
  identifying which spouse claims the HSA family-cap (only one
  per IRC §223(b)(5)), verifying spousal-IRA eligibility per
  IRS Pub 590-A, and checking joint MAGI against the Roth-IRA
  phase-out ($236k-$246k MFJ for 2025). Consult a retirement-
  experienced CPA before the first contribution year if any cross-
  spouse coordination feature is in play.

### 1.4 Self-employed cash-flow breaks the W-2 priority-order mapping

- **Statement**: The priority order is calibrated to a W-2-employed
  knowledge-worker with stable cash flow; for self-employed / 1099
  / equity-comp-heavy / lumpy-income askers, the steps don't map
  cleanly (solo-401(k) and SEP-IRA substitute for the W-2 401(k);
  SEP-IRA balance triggers pro-rata on backdoor Roth in step 5
  because Form 8606 Line 6 aggregates all traditional / SEP / SIMPLE
  IRA balances on Dec 31), and the framing rarely degrades-
  gracefully to the self-employment-cash-flow reality.
- **Source evidence**: `framings.md` §1 Excludes line on W-2
  flowchart not mapping to self-employed cash-flow reality;
  `decisions.md` §D1 cross-domain edge into `entrepreneurship`.
  Reinforced by The Finance Buff voice on solo-401(k) vs SEP-IRA
  pro-rata-trap analysis.
- **Trigger**: Asker is self-employed / 1099 / S-corp owner / has
  SEP-IRA balance AND is reasoning about backdoor Roth or step-by-
  step priority-order from a W-2 flowchart AND has not separately
  verified the SEP-IRA balance triggers pro-rata aggregation.
- **Failure mode**: Asker executes backdoor Roth converting $7,000;
  Form 8606 Line 6 aggregates the $200k SEP-IRA balance into the
  pro-rata calculation; ~96% of the conversion is taxable at ordinary
  rates ($6,720 of the $7,000 conversion produces a $1,500-$2,200 tax
  bill on top of the no-deduction nondeductible contribution); the
  asker discovers via tax-prep or CP2000 18 months later that the
  intended "backdoor" was a normal taxable conversion with a basis
  offset of only ~$280. Recovery requires either rolling SEP-IRA
  into solo-401(k) (loses pro-rata exposure) BEFORE next backdoor
  attempt or accepting the pro-rata math going forward.
- **Recovery move**: Before any backdoor Roth attempt for self-
  employed askers with existing pre-tax IRA balances (traditional
  IRA, SEP-IRA, SIMPLE-IRA), build the Form 8606 Line 6 / Line 8 /
  Line 10 cross-form view and verify pro-rata exposure; consider
  solo-401(k) rollover-of-SEP before year-end to eliminate pro-rata
  exposure; consult a retirement-and-equity-comp-experienced CPA
  with explicit backdoor-Roth and solo-401(k) plan-document
  experience before executing. Verify CPA via SEC IAPD before
  engagement.

### 1.5 Match-capture reflex misses high-fee-401(k) sub-optimization for low-match employers

- **Statement**: For employers with low match (3% or below) AND
  high 401(k) plan-administration fees (~1% expense ratio on
  available funds with no low-cost-index alternative, common at
  small-employer-plan-administrators like ADP / Paychex /
  ShareBuilder 401k), the post-fee-after-tax return on dollars
  beyond the match can be *lower* than taxable-brokerage in a
  $0-fee index fund. The framing's "step 4 dominates everything
  past the match" doesn't engage with fee-leakage variance across
  plans — a 1% expense ratio compounded over 30 years halves the
  terminal balance.
- **Source evidence**: `framings.md` §1 Excludes line on the framing's
  individualism missing fee-variance across plan-document quality;
  Bogleheads voice on expense-ratio-and-tax-drag-minimization;
  financial-economics-journalism voice (David Wessel at Brookings,
  Anne Tergesen at WSJ) on small-employer-plan-fee-leakage as a
  retirement-savings-system structural issue.
- **Trigger**: Asker works for small employer / law-firm / medical-
  practice / startup AND mentions limited fund menu / high expense
  ratios / no index-fund option in their 401(k) AND is reasoning
  about step-4-beyond-match from generic priority-order advice.
- **Failure mode**: Asker maxes 401(k) at $23,500/year in a 0.95%-
  expense-ratio target-date fund (the plan's only equity option);
  over 30 years the fee-drag costs ~25-30% of terminal balance vs
  a 0.05%-expense-ratio comparable in a taxable brokerage account
  (~$200k-$400k on a $23,500/year contribution); the asker discovers
  the magnitude only when consolidating accounts at retirement.
- **Recovery move**: For any asker with limited-menu high-fee 401(k),
  request the plan's Form 5500 fee disclosure (DOL public filing) and
  the participant fee-disclosure (annual ERISA §404(a)(5) required
  disclosure); compute expense-ratio-weighted cost across the menu;
  consult a fee-only fiduciary CFP (NAPFA / XY-Planning) on whether
  the after-fee-after-tax return on beyond-match contributions
  dominates taxable-brokerage in the asker's situation. Verify CFP
  fee-only status via NAPFA member directory and SEC IAPD Form ADV
  Part 2A before engagement.

## 2. Marginal-rate-arbitrage framing

### 2.1 TCJA-bracket-sunset 2026 makes "projected retirement marginal" a moving target

- **Statement**: The "current marginal vs projected retirement
  marginal" framing is a *point-estimate* on a future that depends
  on (a) future federal-bracket changes (TCJA brackets sunset
  Dec-31-2025 absent extension; in 2026 the 12% bracket reverts to
  15%, 22% to 25%, 24% to 28%), (b) future state-of-residence,
  (c) future RMD-induced bracket-creep, (d) future Social-Security
  taxability thresholds (NOT inflation-indexed since 1983),
  (e) future Medicare-IRMAA tiers. The framing's deterministic
  arithmetic understates the *distributional* nature of the
  projection and an asker who picks traditional on a "22% now vs
  expected 12% in retirement" point-estimate may discover the 12%
  is actually 15% retroactively.
- **Source evidence**: `framings.md` §2 Excludes line on point-
  estimate on a politically-volatile future; financial-economics-
  journalism voice (David Wessel at Brookings on TCJA-sunset
  legislative posture; Anne Tergesen at WSJ on retirement-bracket-
  creep reporting); IRS-publication-authority voice (Pub 590-A
  bracket-table updates per cycle).
- **Trigger**: Asker is in the 22% or 24% federal marginal bracket
  in 2025 AND is making a Roth-vs-traditional decision on the basis
  of "current 22-24% vs expected 12% in retirement" point-estimate
  AND has not separately accounted for TCJA-bracket-sunset risk.
- **Failure mode**: Asker chooses traditional 401(k) over Roth based
  on 22%-now-vs-projected-12%-retirement comparison; TCJA brackets
  sunset Dec-31-2025; in 2026 the asker's working-year marginal
  reverts from 22% to 25% (slightly higher) while the projected
  retirement marginal also reverts from 12% to 15% (the arbitrage
  spread narrows). For the asker already in retirement, the bracket-
  reversion compounds with the RMD-induced bracket-creep at age 73
  (now 75 under SECURE 2.0 §107). The "asymmetric-cap-utility"
  argument for Roth strengthens retrospectively when the future
  retirement marginal is higher than the point-estimate assumed.
- **Recovery move**: For Roth-vs-traditional decisions with 5+ year
  horizon, treat the projected retirement marginal as a
  *distribution* not a point-estimate, with explicit scenario weights
  on TCJA-sunset / SECURE 3.0 future changes / state-of-residence
  shift. Consult a retirement-and-equity-comp-experienced CPA who
  tracks tax-policy-shifts (verify via SEC IAPD Form ADV Part 2A
  before engagement) on bracket-fill sizing under explicit policy-
  uncertainty.

### 2.2 Mid-year-income-uncertainty forecloses precise bracket-fill sizing

- **Statement**: The framing's bracket-fill discipline assumes the
  asker can *project current-year income with precision* — but for
  equity-comp askers (RSU vesting on grant-date schedule plus market
  price), self-employed askers, and any asker mid-year on sabbatical
  or layoff, year-end-income is genuinely uncertain well into Q3,
  and a Roth conversion sized to "fill the 22% bracket" can spill
  into 24% if Q4 income surprises upward. Conversions are
  irrevocable (TCJA 2017 eliminated recharacterization) — size
  conservatively at year-start, fund mid-year as income clarifies,
  NEVER lump-all-in-January.
- **Source evidence**: `framings.md` §2 Excludes line on bracket-fill
  precision being structurally unavailable for variable-income
  askers; The Finance Buff voice on Roth-conversion-sizing-against-
  income-uncertainty; cross-domain edge into `tech-career` per
  `decisions.md` §D7.
- **Trigger**: Asker is equity-comp-heavy / self-employed / on
  sabbatical / between jobs / has variable bonus structure AND is
  contemplating a Roth conversion sized to fill a specific bracket
  AND is doing the sizing in Q1 / Q2 before year-end-income is
  resolved.
- **Failure mode**: Asker executes $40k Roth conversion in January
  sized to "fill the 22% bracket assuming $130k base + $30k bonus";
  Q4 RSU vest at higher-than-expected stock price adds $25k of
  additional ordinary income; the $40k conversion now spills $15k
  into the 24% bracket plus possibly into NIIT 3.8% (above $200k
  single / $250k MFJ); the $15k spill costs $300-$900 in additional
  tax that was avoidable. Conversion is irrevocable post-TCJA-2017
  — recharacterization is permanently eliminated; the asker eats
  the spill.
- **Recovery move**: For variable-income askers, execute Roth
  conversions only in *Q4* with realized YTD income known plus
  conservative Q4 estimate; size to the *bottom* of the target
  bracket with margin for surprise; or execute in multiple smaller
  tranches across the year with each tranche sized against the
  current YTD-actual income. Consult a retirement-and-equity-comp-
  experienced CPA on conversion-timing-and-sizing methodology
  before any conversion is executed. Verify CPA experience with
  Form 8606 + Form 1099-R distribution-code-2-vs-7 reconciliation
  via SEC IAPD before engagement.

### 2.3 Asymmetric-cap-utility argument is invisible to non-cap-constrained savers

- **Statement**: The "asymmetric-cap-utility" argument (Roth $23,500
  contains more after-tax-equivalent room than traditional $23,500
  for a cap-constrained saver) is correct *for cap-constrained
  savers* but is structurally invisible to the asker who isn't
  hitting the cap — the framing rarely surfaces this nuance, and
  the popular-press version ("Roth is always better for young
  people") propagates the cap-constrained logic to askers who don't
  face the cap. For these askers traditional-vs-Roth reduces back
  to a pure-marginal-rate comparison without the cap-utility
  premium.
- **Source evidence**: `framings.md` §2 Excludes line on asymmetric-
  cap-utility being structurally invisible to non-cap-constrained
  savers; The Finance Buff voice on the cap-room arithmetic;
  personal-finance-influencer voice (Suze Orman / Dave Ramsey /
  Ramit Sethi) propagating "Roth is always better for young people"
  without the cap-constraint conditional.
- **Trigger**: Asker is young / early-career AND is reasoning about
  Roth-vs-traditional from popular-press "Roth is always better"
  advice AND is NOT cap-constrained (saves less than the elective-
  deferral cap of $23,500/year) AND is in a higher current marginal
  rate than their projected retirement rate.
- **Failure mode**: Asker chooses Roth-401(k) on "Roth is always
  better for young people" advice; gives up $5,170 of current-year
  federal+state tax deduction at 22%-fed + 9.3%-CA combined ($23,500
  × 22% ≈ $5,170; ignore state for simplicity); contributes the same
  $23,500 nominal (gross) but ends up with $23,500 nominal Roth
  rather than $30,150 nominal traditional ($23,500 + the $5,170
  saved-tax that could have been contributed to taxable). For non-
  cap-constrained savers, the Roth-vs-traditional choice should
  reduce to pure marginal-rate-arbitrage; the popular-press version
  systematically misroutes them.
- **Recovery move**: For non-cap-constrained askers (saving less
  than $23,500/year on a single-401(k), or less than $7,000/year on
  Roth-IRA), the Roth-vs-traditional decision should be made on
  pure marginal-rate-arbitrage grounds (current marginal vs
  projected retirement marginal, hedged for policy-volatility per
  §2.1) rather than on the cap-utility premium. Consult a retirement-
  experienced CPA for personalized marginal-rate analysis; verify
  CPA via SEC IAPD before engagement.

### 2.4 FICA on traditional-401(k) vs HSA-payroll arbitrage missed by blogger voice

- **Statement**: The framing under-engages with *FICA on traditional-
  401(k) contributions* — traditional 401(k) contributions are pre-
  federal-and-state-income-tax but NOT pre-FICA, while HSA payroll
  contributions are pre-FICA per IRC §125 cafeteria-plan treatment.
  For high-FICA-bracket askers below the SS-wage-base ($176,100 in
  2025), HSA-vs-traditional-401(k) marginal arbitrage includes a
  7.65% FICA advantage to HSA that the "20% federal + 9.3% CA =
  29.3% combined" calculus misses entirely. On $4,300 HSA contribution
  the FICA arbitrage alone is $329/year — a non-trivial fraction of
  the HSA tax-arbitrage that compounds annually.
- **Source evidence**: `framings.md` §2 Excludes line on FICA-on-
  traditional missed by personal-finance-blogger voice but caught by
  The Finance Buff; The Finance Buff voice canonical on HSA-payroll-
  vs-after-tax-FICA-arbitrage analysis.
- **Trigger**: Asker is below SS-wage-base ($176,100 in 2025) AND is
  HSA-eligible (HDHP-enrolled with no disqualifying coverage) AND is
  funding HSA via after-tax 1040-deduction (Form 8889 Part 1) rather
  than via payroll-deduction Section 125 cafeteria plan AND has not
  separately verified the FICA implication.
- **Failure mode**: Asker funds HSA $4,300/year via after-tax 1040-
  deduction (Form 8889 Part 1) saving income tax but NOT FICA;
  forgoes $329/year FICA arbitrage that payroll-deduction HSA would
  have captured; over 30 working years the foregone FICA arbitrage
  compounds to ~$30k-$50k of foregone tax-equivalent savings (FICA
  also reduces SS-PIA via Box-3-wages reduction; the trade-off is
  complex but the net effect for most middle-income savers is
  positive for payroll-HSA).
- **Recovery move**: For HSA-eligible askers, prefer payroll-
  deduction HSA via Section 125 cafeteria plan over after-tax 1040-
  deduction whenever the employer offers it; if employer doesn't
  offer payroll-HSA, raise it with HR as a structural plan-feature
  request. Consult The Finance Buff guides (thefinancebuff.com on
  HSA-payroll-vs-after-tax-FICA-arbitrage) for the arithmetic, AND
  consult a retirement-experienced CPA for confirmation in the
  asker's specific income-and-state-tax situation before changing
  contribution method mid-year (some payroll-HSA elections are
  annual-irrevocable).

### 2.5 Bracket-fill ignores Social-Security taxability thresholds (un-indexed since 1983)

- **Statement**: The framing's bracket-fill discipline focuses on
  federal income tax brackets but rarely engages with the *Social-
  Security taxability thresholds* — once provisional income exceeds
  $25k single / $32k MFJ, 50% of SS becomes taxable, and at $34k
  single / $44k MFJ 85% becomes taxable. These thresholds have NOT
  been indexed for inflation since 1983 (per Social Security
  Amendments of 1983, 42 USC §86), so bracket-fill conversions in
  retirement that push provisional income across these stale
  thresholds can create an effective marginal rate (federal-bracket
  + SS-taxability) of 40-50% even at nominally low federal brackets.
  The 22.2% / 27.75% "Social-Security tax torpedo" zone is
  catastrophically missed by simple-bracket-fill arithmetic.
- **Source evidence**: `framings.md` §2 Excludes line on Social-
  Security taxability thresholds NOT inflation-indexed since 1983;
  retirement-econ academic voice (William Reichenstein and William
  Meyer, *Income Strategy for Retirement* on SS-tax-torpedo
  modeling); fee-only Social-Security-claiming-specialist voice
  (Mike Piper's Open Social Security software, *Social Security
  Made Simple*).
- **Trigger**: Asker is 60+ AND has begun OR is about to begin
  collecting Social-Security AND is contemplating a Roth conversion
  sized to fill a federal bracket AND has not separately modeled the
  conversion's effect on provisional-income and SS-taxability.
- **Failure mode**: Asker (single, age 67) executing Roth conversion
  sized to "fill the 12% federal bracket"; conversion pushes
  provisional income from $30k to $50k; SS-taxability transitions
  from 50%-taxable to 85%-taxable across the conversion amount;
  effective marginal rate on the conversion is 12% federal + 8.5%-
  10% SS-tax-torpedo = 20-22% effective, not the 12% the asker
  modeled. For MFJ couples the torpedo zone is wider and persists
  through more of the bracket-fill range.
- **Recovery move**: For any retiree contemplating Roth conversion
  while collecting SS, model the *provisional-income effect* on SS-
  taxability before sizing the conversion; consult a fee-only
  Social-Security-claiming-specialist (Mike Piper's Open Social
  Security software is free and conflict-free; SHIBA / SHIP for
  Medicare-coordination side) for the SS-taxability arithmetic AND
  a retirement-experienced CPA for the conversion sizing AND
  cross-check via Form SSA-1099 provisional-income reconciliation.
  Verify both professionals via SEC IAPD / FINRA BrokerCheck before
  engagement.

## 3. HSA-as-stealth-IRA framing

### 3.1 Cash-flow constraint makes "pay OOP let HSA compound" infeasible

- **Statement**: The "pay OOP, let HSA compound" strategy assumes
  the asker has sufficient taxable savings to fund current medical
  without raiding the HSA; for askers with cash-flow constraints
  (early-career, paying down debt, single-income household with
  kids), the prescription is correct in theory and infeasible in
  practice. The framing rarely degrades-gracefully to "if you can't
  bank the receipts, just use HSA for current spend — you still get
  the contribution-side tax deduction." Asker abandonment of HSA
  entirely on perceived complexity loses both the contribution-side
  AND withdrawal-side tax arbitrage.
- **Source evidence**: `framings.md` §3 Excludes line on cash-flow-
  constrained askers; opposes F4 (tax-arbitrage when cash-flow-
  constrained) and F11 (behavioral-finance). Reinforced by chronic-
  DIY-Reddit voice (r/personalfinance HSA threads) on the
  pragmatic-use-vs-theoretical-optimum split.
- **Trigger**: Asker is HSA-eligible AND has cash-flow stress
  (paying down high-APR debt, no emergency fund, single-income
  household, student-loan-heavy, recent medical event AND no
  taxable savings buffer) AND is reasoning about "shoebox the
  receipts" as the only-right-way-to-use-HSA.
- **Failure mode**: Asker reads Bogleheads / The Finance Buff "max
  HSA, pay OOP, shoebox receipts" advice; cannot fund current
  medical from taxable savings; abandons HSA contribution entirely
  on perceived complexity; loses BOTH the contribution-side income-
  tax deduction (~$1,376/year at 32% marginal on $4,300 family-cap)
  AND the FICA arbitrage (~$329/year) AND the withdrawal-side tax-
  free arbitrage on current medical. Theoretical-optimum
  prescription drives complete-abandonment in cash-flow-constrained
  practice.
- **Recovery move**: For cash-flow-constrained HSA-eligible askers,
  the *first*-order recommendation is "contribute to HSA at any
  amount and use it for current medical — you still get the
  contribution-side income-tax + FICA arbitrage even if you can't
  shoebox the receipts." Defer the "let HSA compound" optimization
  to later years when cash-flow allows. Consult a retirement-
  experienced CPA via SEC IAPD verification if Form 8889 Part 1 vs
  Part 2 reconciliation is unclear.

### 3.2 Medicare-Part-A retroactivity silently invalidates HSA contributions

- **Statement**: HSA-eligibility is *fragile in retirement-adjacent
  timing*: any non-HDHP coverage (general-purpose FSA, spouse's
  general-purpose FSA, Medicare Part A, VA care within prior 3
  months, Tricare, DPC without ancillary structuring) disqualifies
  HSA contributions — and Medicare Part A is *retroactive up to 6
  months* when Social-Security-claiming after 65 (per 42 CFR
  §406.5), which silently invalidates 6 months of HSA contributions
  the framing's "max until SS-claim" timing doesn't catch. Stop HSA
  contributions 6 months before SS-claim if claiming past 65.
- **Source evidence**: `framings.md` §3 Excludes line on Medicare-
  Part-A retroactivity invalidating HSA contributions; cross-domain
  edge into `health-insurance` D9 per `decisions.md` §D8. SHIBA /
  SHIP volunteer voice on the retroactivity rule; The Finance Buff
  voice on the 6-month-pre-claim stop-rule.
- **Trigger**: Asker is 65+ AND is HSA-eligible AND is contemplating
  Social-Security claim AND has not stopped HSA contributions 6
  months before the claim AND has not separately modeled the
  retroactivity rule.
- **Failure mode**: Asker (age 67) continues HSA contributions
  through June, then claims Social-Security in July; Medicare Part A
  enrolls retroactive to January (6-month look-back from claim
  date); IRS treats Jan-June HSA contributions ($2,150 of $4,300
  annual cap pro-rated) as excess contributions subject to 6%
  excise tax annually until withdrawn (Form 5329); plus the
  $2,150-of-contribution-side-tax-deduction must be reversed on an
  amended Form 8889 / 1040-X. Asker discovers the issue 18 months
  later via CP2000 notice.
- **Recovery move**: For HSA-eligible askers approaching SS-claim
  after 65, *stop HSA contributions 6 months before the planned
  claim date*; if SS-claim has already occurred with retroactive
  Part A enrollment, file Form 8889 with the corrected pro-rated
  contribution amount and withdraw excess contributions plus
  earnings via timely-withdrawal-of-excess process per IRS
  procedure (avoid 6% excise if withdrawn by extended-tax-deadline).
  Consult SHIBA / SHIP volunteer (federally-funded, free) for
  Medicare-side AND a retirement-experienced CPA via SEC IAPD for
  the HSA-side reconciliation.

### 3.3 HSA-inherited-by-non-spouse becomes fully taxable in year of inheritance

- **Statement**: HSA-inherited-by-non-spouse becomes *fully taxable
  in the year of inheritance* — the entire balance hits the non-
  spouse-heir's income for the year of death (offset only by
  qualified-medical-expenses-of-decedent paid within 1 year of
  death per IRC §223(f)(8)(B)). For users with large HSA balances
  ($300k+) and intent-to-bequeath to non-spouse, this is a
  significant inheritance-tax-event the framing's "tax-free
  retirement vehicle" never names. Consider during-life-spend-down
  or during-life-Roth-conversion-equivalent moves on large HSA.
- **Source evidence**: `framings.md` §3 Excludes line on HSA-non-
  spouse-heir taxable-in-full; cross-domain edge into `family-
  planning` D10 per `decisions.md` §D10. State-bar-estate-attorney
  voice on beneficiary-form structuring; IRS-publication-authority
  voice (Pub 969 HSA-and-FSA, IRC §223(f)(8)(B)).
- **Trigger**: Asker has accumulated HSA balance >$100k AND has
  named non-spouse beneficiary (child / sibling / parent / charity
  except as below) AND has not separately modeled the inheritance-
  tax event.
- **Failure mode**: Asker dies with $400k HSA balance and non-spouse
  child as beneficiary; child reports entire $400k as ordinary income
  on Form 1040 in year-of-death (less any qualified-medical-expenses-
  of-decedent paid within 1 year, typically <$10k); $400k at 32%
  marginal = $128k federal tax bill plus state tax (up to $53k in
  CA), reducing the heir's net inheritance from $400k to ~$220k.
  Compared to a spouse-beneficiary continuation (rolls into spouse's
  own HSA continuing tax-free treatment per §223(f)(8)(A)), the
  non-spouse hit is catastrophic.
- **Recovery move**: For large HSA balances ($100k+) with intent-to-
  bequeath to non-spouse, consider: (a) during-life-spend-down
  reimbursing accumulated medical receipts (shoebox-strategy
  reverse-direction) to reduce the HSA balance pre-death; (b)
  charity-as-beneficiary (qualified charitable beneficiary gets the
  full balance tax-free); (c) consult a state-bar-licensed estate
  attorney via state-bar lawyer-referral-service (NOT a for-profit
  finder) on HSA-beneficiary structuring relative to overall estate
  plan AND a retirement-experienced CPA on the during-life-spend-
  down arithmetic. Verify CPA via SEC IAPD before engagement.

### 3.4 Reimburse-as-you-go may dominate for major-medical-events-young

- **Statement**: The retirement-vehicle framing assumes the asker
  reaches retirement having accumulated medical expenses to
  reimburse against; for an asker with major medical events in
  their 30s and 40s, the optimal play may be reimburse-as-you-go
  rather than shoebox — the tax-free withdrawal is identical, the
  compounding lost is real (a $20k withdrawal at age 35 forgoes
  ~$215k of terminal-balance compounding at 7% real over 30 years),
  but the after-tax-dollar of withdrawal at age 35 is also worth
  more in liquidity terms than at 65. The framing's bias toward
  deferral can be myopic for asker-specific health trajectories.
- **Source evidence**: `framings.md` §3 Excludes line on reimburse-
  as-you-go vs shoebox for major-medical-events-young; The Finance
  Buff voice on the trade-off arithmetic; chronic-DIY-Reddit voice
  (r/personalfinance HSA threads) on the personal-trajectory
  override of generic-rules.
- **Trigger**: Asker is under 50 AND has experienced or is planning
  for a major medical event ($20k+ OOP expected) AND is reasoning
  about shoebox-the-receipts purely on long-horizon-compounding
  grounds AND has not separately modeled liquidity-needs-now vs
  liquidity-needs-65.
- **Failure mode**: Asker (age 36) has $40k of medical expenses
  during a cancer-treatment-year; reads "shoebox the receipts" Boglehead
  / Finance Buff guides; uses taxable-brokerage / 401(k)-loan / credit-
  card to pay current OOP rather than tapping HSA; ends up paying
  3-7% in cumulative interest / opportunity-cost-of-stocks-sold-at-
  cap-gains over the recovery year; loses the liquidity option AND
  the long-horizon compounding (the compounding is only marginally
  better than alternative-bucket compounding once interest /
  cap-gains drag is factored).
- **Recovery move**: For major-medical-events under age 50, treat
  reimburse-as-you-go vs shoebox as a separate decision keyed to
  the asker's full balance-sheet liquidity, alternative-bucket
  return assumptions, and personal-trajectory health expectations;
  consult a fee-only fiduciary CFP (NAPFA / XY-Planning) for the
  liquidity arithmetic AND a retirement-experienced CPA for the
  tax-arbitrage arithmetic. Verify both via SEC IAPD before
  engagement.

### 3.5 DPC-and-HSA compatibility gray zone IRS-pending

- **Statement**: Direct Primary Care (DPC) monthly memberships
  ($50-$150/month for unlimited primary care) are a growing
  alternative care model, but their HSA-eligibility-compatibility
  is *gray zone* per IRS Notice 2013-54 and subsequent guidance —
  DPC arrangements that include "ancillary" services (labs,
  imaging, prescription dispensing) may disqualify HSA contributions
  by being treated as a non-HDHP health plan. Pending legislation
  (Primary Care Enhancement Act) would formalize HSA-DPC
  compatibility but has not passed. The framing's "HSA is portable
  and stable" reflex misses the DPC-compatibility regulatory
  uncertainty.
- **Source evidence**: `framings.md` §3 Excludes line on DPC-and-HSA
  compatibility being IRS-pending; cross-domain edge into `health-
  insurance` D6 per `decisions.md` §D1. IRS-publication-authority
  voice (Pub 969 HSA-and-FSA, IRS Notice 2013-54); ACA-Navigator /
  HSA-administrator voice on the DPC-eligibility uncertainty.
- **Trigger**: Asker is HSA-eligible AND is enrolled in or
  considering a DPC arrangement AND has not separately verified the
  DPC structure's HSA-compatibility AND is reasoning about HSA
  contribution as if DPC enrollment has no HSA-eligibility
  implication.
- **Failure mode**: Asker (age 42) enrolls in DPC with prescription-
  dispensing ancillary; continues HSA contributions assuming
  eligibility; IRS audit (or self-discovery during tax-prep) treats
  DPC as a non-HDHP health plan; HSA contributions for the year
  become excess, subject to 6% annual excise via Form 5329 until
  withdrawn; the contribution-side tax deduction must be reversed
  via 1040-X. Recovery requires either DPC-restructuring (drop
  ancillary services) or HSA-contribution-suspension.
- **Recovery move**: Before combining DPC with HSA contributions,
  verify the specific DPC arrangement's structure against IRS
  Notice 2013-54 (the IRS has not issued bright-line guidance; the
  conservative read is that any ancillary services beyond direct
  primary care risk HSA-disqualification); consult a retirement-
  experienced CPA via SEC IAPD with explicit DPC-and-HSA experience
  before continuing HSA contributions while enrolled in DPC; track
  pending legislation (Primary Care Enhancement Act) for
  formalization.

## 4. Tax-arbitrage / Form-mechanic framing

### 4.1 Paid-preparer backdoor-Roth Form-8606 error rate is non-trivial

- **Statement**: The Form-mechanic discipline assumes the asker can
  *project annual income* and *correctly file forms*; in practice
  many tax preparers (including paid franchise preparers — H&R
  Block, Jackson Hewitt) get backdoor-Roth Form 8606 wrong, treating
  the nondeductible IRA contribution as missing entirely (so the
  conversion is taxed at full ordinary rates with no basis offset).
  The framing's "fill the form correctly" understates the
  practitioner-error rate, and the asker often discovers the mistake
  via an IRS CP2000 notice 18 months later.
- **Source evidence**: `framings.md` §4 Excludes line on backdoor-
  Roth Form 8606 practitioner-error rate; The Finance Buff voice
  consistently catches this — thefinancebuff.com canonical guides
  on Form 8606 Part I + Part II reporting reconciliation;
  retirement-experienced-CPA voice distinguishing CPA-specialty-
  filter from generic-tax-prep.
- **Trigger**: Asker executed a backdoor Roth (nondeductible
  traditional IRA contribution + same-year Roth conversion) AND
  uses a franchise tax preparer / DIY software (TurboTax / H&R
  Block) AND has not separately verified Form 8606 Part I
  (nondeductible contribution basis) and Part II (conversion with
  basis offset) on the filed return.
- **Failure mode**: Asker contributes $7,000 nondeductible to
  traditional IRA in March 2025, converts to Roth in April 2025;
  tax preparer in early 2026 reports the conversion on Form 1099-R
  as taxable but fails to file Form 8606 with basis offset; IRS
  treats entire $7,000 as ordinary-income taxable in 2025; CP2000
  arrives in Sep 2026 with $1,540-$2,240 federal tax bill on
  income the asker thought was already-after-tax. Recovery
  requires amended 1040-X plus Form 8606 plus possibly Form 5329
  reconciliation, and unwinding the misreport in subsequent years
  carries forward.
- **Recovery move**: For any asker who has executed or is planning
  backdoor Roth, *manually verify* Form 8606 Part I and Part II on
  the filed return; cross-check via The Finance Buff's annual
  "Backdoor Roth in TurboTax" step-by-step (free, conflict-free);
  if Form 8606 is missing or wrong, consult a retirement-and-
  equity-comp-experienced CPA with explicit backdoor-Roth experience
  to file 1040-X plus Form 8606 to establish basis going forward.
  Verify CPA via SEC IAPD before engagement; ask explicitly about
  Form 8606 + Form 5498 + Form 1099-R reconciliation experience.

### 4.2 Tax-code political dynamism breaks "look up the current Form X"

- **Statement**: The framing engages with *tax-code-as-static* but
  the tax-code is *politically dynamic* — TCJA 2017 brackets sunset
  2026, SECURE Act 2.0 phased many provisions across 2024-2026,
  ARPA/IRA enhanced ACA subsidies sunset 2025 absent extension,
  Roth-conversion-recharacterization was eliminated 2018, and the
  Roth-401(k)-employer-match-allowed mechanic was added 2024 but
  is plan-document-gated. The framing's "look up the current Form
  X" is correct only for the current cycle; asker questions
  reaching back to 2017 / 2018 cycle have *different* rules
  applying.
- **Source evidence**: `framings.md` §4 Excludes line on tax-code
  political dynamism; IRS-publication-authority voice on
  cycle-specific Form-X versioning; financial-economics-journalism
  voice (Anne Tergesen at WSJ on SECURE 2.0 phased-provision
  reporting; David Wessel at Brookings on TCJA-sunset legislative
  posture).
- **Trigger**: Asker is reviewing or considering reopening a tax
  decision from a prior cycle (Roth-recharacterization pre-2018,
  Mega-Backdoor-Roth pre-2024-Roth-match, RMD age 70.5 vs 72 vs 73
  vs 75 depending on birth year) AND is reasoning about it from
  current-year rules.
- **Failure mode**: Asker wants to "undo" a 2024 Roth conversion
  the way they did in 2016 — discovers recharacterization was
  permanently eliminated by TCJA 2017 effective Jan 1 2018;
  conversion is irrevocable, the spill into 32% bracket is
  permanent. OR: asker born in 1951 thinks RMDs start at 72 per
  SECURE 1.0 but doesn't realize SECURE 2.0 §107 raised the age
  to 73 for those born 1951-1959 and 75 for those born 1960+;
  misses or over-takes a year of RMDs depending on direction of
  error.
- **Recovery move**: For any cross-cycle tax decision, verify the
  rules-as-of-the-decision-year against the current IRS
  publications (Pub 590-A, 590-B for IRA; Pub 525 for compensation;
  Pub 969 for HSA; Pub 970 for education); cross-check via The
  Finance Buff annual-update posts; consult a retirement-experienced
  CPA with explicit current-cycle experience before relying on
  pre-cycle rules. Verify CPA via SEC IAPD before engagement.

### 4.3 CFP-vs-CPA selective-referral mismatch on technical-tax questions

- **Statement**: Form-mechanic mastery is unequally distributed
  across the professional-advice market — fee-only fiduciary CFPs
  vary sharply in tax-mechanic depth (many will outsource to a CPA
  rather than calculate themselves), and CPAs vary sharply in
  retirement-and-equity-comp experience (a CPA who's done 50
  business-returns this year but 0 backdoor-Roth-Forms-8606 is
  *not* the right validator for the conversion-planning question
  despite the credential). The framing's "consult your CPA" reflex
  needs CPA-specialty-filter that the broad framing rarely names.
- **Source evidence**: `framings.md` §4 Excludes line on CPA-
  specialty-filter; cross-reference to `decisions.md` §Notes
  selective-referral matrix (CPA experienced with retirement-plan
  and equity-comp mechanics for decisions 1, 6, 7 — backdoor-Roth
  Form 8606, tax-loss-harvesting + wash-sale validation, Roth-
  conversion sizing). The Finance Buff voice on this distinction.
- **Trigger**: Asker has a technical-tax question (backdoor Roth,
  Mega-Backdoor Roth plan-document, ISO-AMT-exercise-timing, QSBS
  §1202 5-year-hold, ESPP §423 qualifying-disposition) AND is
  reaching for "my CPA" without verifying retirement-and-equity-
  comp specialty depth.
- **Failure mode**: Asker asks their generic small-business CPA
  about Mega-Backdoor-Roth-via-after-tax-401(k)-in-plan-conversion;
  CPA hasn't seen the structure (their practice is mostly Schedule
  C / S-corp K-1 / Sales-Tax-Permit work); CPA either declines or
  produces wrong advice (e.g. mis-reports the in-plan conversion
  on Form 1099-R distribution-code-G as taxable rather than 1099-R
  distribution-code-H as in-plan-Roth-rollover-with-basis); asker
  files an incorrect return; CP2000 follows.
- **Recovery move**: Before consulting a CPA on technical-retirement
  questions, *filter by specialty*: ask explicitly "how many
  backdoor Roth Form 8606 filings have you prepared this year?
  How many Mega-Backdoor Roth in-plan conversions have you
  reconciled? Do you have ISO-AMT clients? QSBS §1202 5-year-hold
  clients?"; verify Form ADV Part 2A (for IRS / CPA-PFS) at SEC
  IAPD or state-board for any disclosure history; consult fee-only
  fiduciary CFP (NAPFA / XY-Planning) for advice-and-strategy AND
  retirement-experienced CPA for tax-mechanic-execution separately
  — the specialty mismatch is structural.

### 4.4 5-year-conversion-clock and 5-year-Roth-aging clock are two separate clocks

- **Statement**: The 5-year-Roth-conversion-clock and 5-year-Roth-
  IRA-aging-clock are *two distinct clocks* that the asker must
  track separately for each conversion AND for the Roth-IRA-itself
  — the longer of the two applies for penalty-free withdrawal of
  earnings, and many askers (and some advisors) treat them as one
  clock. The framing's form-discipline captures this if applied
  consistently; the marginal-rate framing alone misses it.
- **Source evidence**: `framings.md` §4 Excludes line on dual 5-
  year-clock confusion; The Finance Buff voice canonical on
  Roth-conversion-5-year-clock-per-conversion + Roth-IRA-5-year-
  aging-clock-from-first-contribution distinction; IRS-publication-
  authority voice (Pub 590-B IRA-distributions).
- **Trigger**: Asker is under 59.5 AND is planning to withdraw from
  Roth IRA in less than 10 years AND has executed Roth conversions
  in multiple years AND is conflating the clocks.
- **Failure mode**: Asker (age 50) opens Roth IRA in 2020 with
  contributions, does Roth conversion in 2023; plans to withdraw
  $30k of converted-principal in 2026 (3 years after conversion,
  6 years after Roth-IRA-opened); thinks "5-year aging clock met
  via 2020 Roth-IRA-opening so withdrawal is qualified." Wrong:
  the *converted* principal has its own 5-year-conversion-clock
  per Pub 590-B; withdrawal before 5-year-conversion-clock = 10%
  penalty on the converted amount (the federal income tax was
  paid at conversion, so no income tax — but the early-withdrawal
  penalty applies). $3,000 penalty on the $30k converted-principal
  withdrawal.
- **Recovery move**: For Roth IRAs with multiple conversions, track
  the 5-year-conversion-clock per-conversion separately from the
  5-year-Roth-IRA-aging-clock; consult The Finance Buff's "Roth
  IRA 5-Year Rules" guide AND a retirement-and-equity-comp-
  experienced CPA on withdrawal-sequence ordering rules (Roth IRA
  ordering: contributions first, then conversions oldest-first,
  then earnings last); cross-check via Form 5498 contribution-and-
  conversion-history annual statements. Verify CPA via SEC IAPD.

### 4.5 Section 125 cafeteria-plan irrevocability blocks mid-year correction

- **Statement**: Section 125 cafeteria-plan elections (FSA / HSA /
  Dep-Care-FSA / commuter / health-premium pre-tax) are
  *irrevocable for the plan year* once made at OE absent a
  qualifying-life-event (QLE — birth, marriage, divorce, employment
  change, spouse-coverage change). The framing's "adjust as the
  year unfolds" reflex applies to non-cafeteria-plan tax decisions
  (Form W-4, estimated-tax payments) but NOT to cafeteria-plan
  elections. Asker who realizes mid-year that they over-elected FSA
  ($3,300 cap) or under-elected HSA cannot correct without a QLE.
- **Source evidence**: `framings.md` §4 Excludes line on Form-
  mechanic discipline assuming projectability that doesn't hold for
  cafeteria-plan-irrevocability; IRS-publication-authority voice
  (Pub 969 HSA-and-FSA; Treasury Reg §1.125-4 mid-year-election-
  change-rules); HR-Reddit voice on cafeteria-plan-frustration
  threads.
- **Trigger**: Asker is contemplating a mid-year change to FSA /
  HSA / Dep-Care-FSA election based on income or expense changes
  AND has not separately verified whether a qualifying-life-event
  triggers the §125 mid-year-change-rule AND is reasoning about it
  as if Form-W-4-style adjustment applies.
- **Failure mode**: Asker elects $3,300 Healthcare-FSA in November
  2024 at OE for 2025; mid-year 2025 changes jobs (covered by new
  employer's FSA at $0); cannot recover unused $3,300 from prior-
  employer FSA absent run-out-period rules in the SPD; loses
  remaining-balance to the "use-it-or-lose-it" rule (Healthcare-
  FSA grace period up to 2.5 months OR carryover up to $660 in
  2025; both depend on employer plan-document). For HSA the
  consequence is different (HSA is portable), but the contribution
  cap pro-rates per coverage month under §223(b)(8) if HDHP-
  coverage gaps occur.
- **Recovery move**: At OE, size FSA elections conservatively based
  on *known* (not projected) medical expenses; for HSA, prefer
  contribution flexibility via payroll-deduction-with-mid-year-
  adjustment-permitted-in-most-plans over front-loaded annual
  elections; if a mid-year change is needed, consult HR for §125
  mid-year-election-change-event documentation requirements;
  consult a retirement-experienced CPA via SEC IAPD on §223(b)(8)
  pro-rata HSA contribution rules if HDHP-coverage gaps occurred.

## 5. Risk-adjusted-allocation framing

### 5.1 Risk-tolerance self-report is unreliable until drawdown-tested

- **Statement**: The framing's risk-tolerance / risk-capacity
  distinction is *self-reported* — many askers genuinely don't
  know their drawdown tolerance until they've lived through one,
  and the 2020 March COVID drawdown was *too brief* to genuinely
  test most askers' resolve (the V-shaped recovery hit before the
  full anxiety cycle resolved). The "stress test" framing is the
  right discipline but the answers are unreliable; the framing
  rarely surfaces this calibration gap.
- **Source evidence**: `framings.md` §5 Excludes line on risk-
  tolerance self-report unreliability; behavioral-finance research
  voice (Daniel Kahneman *Thinking Fast and Slow*; DALBAR studies
  on investor-vs-fund-return gap); opposes F11 (behavioral-finance)
  at the meta-level.
- **Trigger**: Asker is new investor / under 35 / has not lived
  through a sustained bear market (Dec 2007-Mar 2009 -55%; Mar 2000-
  Oct 2002 -49%; Oct 1973-Oct 1974 -48%) AND is selecting an
  allocation based on self-reported "I can handle 50% drawdowns"
  stress-test answer.
- **Failure mode**: Asker reports "100% equities, I can hold through
  -50%"; allocates accordingly; in actual 18-month drawdown event
  (vs the 1-month-V-shape COVID experience) sells at -35% to
  preserve "what's left"; locks in 35% real loss; misses the
  recovery; ends up materially worse than a 60/40 allocation that
  the asker would have held. DALBAR studies show 2-3% annual
  underperformance from this mistiming pattern.
- **Recovery move**: For askers without lived-through-prior-bear-
  market experience, select allocation *one step more conservative*
  than self-reported tolerance suggests (the calibration gap goes
  one direction — overestimation, not underestimation); set up
  automated-rebalance discipline (robo-advisor or manual-quarterly)
  to remove decision-fatigue at drawdown peaks; consult a fee-only
  fiduciary CFP (NAPFA / XY-Planning) on glide-path appropriateness
  before committing. Verify CFP via SEC IAPD Form ADV Part 2A
  before engagement.

### 5.2 Concentrated-single-stock dominates target allocation for tech employees

- **Statement**: The framing under-weights *concentrated-single-stock
  risk* that dominates many tech-employee households — a $400k
  vested RSU + $80k ESPP position in current employer is a $480k
  single-stock bet that overwhelms any chosen target allocation.
  The generic "diversify" advice obscures the more specific framing
  — sell-on-vest is tax-neutral for RSU because vesting is already
  a taxable event at ordinary rates; for ESPP the disqualifying-
  disposition vs qualifying-disposition math complicates the
  immediate-sell call.
- **Source evidence**: `framings.md` §5 Excludes line on
  concentrated-single-stock dominating target allocation; cross-
  domain edge into `tech-career` D4 per `decisions.md` §D4 + §D6.
  The Finance Buff voice on RSU-sell-on-vest tax-neutrality;
  retirement-and-equity-comp-experienced CPA voice on ESPP
  qualifying-vs-disqualifying-disposition math.
- **Trigger**: Asker is a tech employee / public-company executive
  / startup-employee-post-IPO AND has $100k+ in employer-stock
  through RSU / ISO / ESPP AND is reasoning about portfolio
  allocation from a generic "diversify" framing without naming the
  concentration.
- **Failure mode**: Asker holds $480k single-employer-stock at age
  35 in a $1.2M net-worth household (40% concentration); employer
  stock declines 50% in industry downturn (correlated with their
  job security — equity-comp-correlation-with-human-capital);
  household net worth drops to $960k AND asker is at elevated
  layoff risk; the "diversified 70/30 target" the asker thought
  they had was structurally not what their actual balance sheet
  said.
- **Recovery move**: For equity-comp-heavy households, compute the
  *single-stock concentration* as a percentage of investable assets
  AND of total balance sheet (including human-capital correlation
  if employer-correlated); if concentration > 10%, prioritize
  diversification over other priority-order steps; for RSU, sell-
  on-vest by default unless tax-deferred-comp Section 409A or
  qualifying-§1202 considerations apply; for ESPP, model
  qualifying-vs-disqualifying-disposition math explicitly. Consult
  a retirement-and-equity-comp-experienced CPA via SEC IAPD on
  ESPP §423 qualifying-disposition AND a fee-only fiduciary CFP
  (NAPFA / XY-Planning) on diversification-staging.

### 5.3 Bond-equity correlation regime-shift breaks classical 60/40 assumption

- **Statement**: Bond-allocation discipline assumes the bond market
  is the *diversifier-against-equity* it was for most of 1980-2020
  — but rate-environment shifts can break that correlation (2022's
  negative-correlation-positive-shock was the worst 60/40 year
  since 1937, with -16% equity and -13% bonds simultaneously). The
  framing's classical-allocation rule needs regime-awareness.
  Alternatives (gold, REITs, TIPS, international, alternatives)
  shift the conversation but each has its own correlation behavior
  and tax-treatment quirks.
- **Source evidence**: `framings.md` §5 Excludes line on bond-
  equity-correlation-regime-shift; retirement-econ academic voice
  (Wade Pfau on bond-tent research, Michael Kitces on rising-rate-
  environment-allocation analysis); financial-economics-journalism
  voice (Jeff Sommer at NYT on 2022 60/40 worst-year reporting).
- **Trigger**: Asker is in or near retirement (age 55+) AND is
  using classical 60/40 or target-date glide-path AND has not
  separately modeled bond-equity correlation regime risk AND is
  reasoning about portfolio diversification from textbook 1980-2020
  data.
- **Failure mode**: Asker (age 62, retiring in 3 years) maintains
  60/40 allocation; encounters 2022-style year (stocks -16%, bonds
  -13%); portfolio drops 15% rather than the 9-10% the classical
  diversification math predicted; sequence-of-returns risk hits
  early-retirement years; safe-withdrawal-rate sustainable spend
  drops materially. The "preserved tail" the framing promised
  evaporated when correlation flipped.
- **Recovery move**: For retirement-adjacent askers (55+),
  explicitly model bond-equity-correlation regime as a *parameter*
  in the allocation decision; consider TIPS / I-Bonds (rate-
  sensitive but inflation-hedged), short-duration-Treasury (lower
  rate-sensitivity), or bond-tent rising-equity-glide approaches
  per Pfau's research; consult a fee-only fiduciary CFP (NAPFA /
  XY-Planning) with retirement-income-specialty AND a retirement-
  experienced CPA via SEC IAPD on bond-fund-vs-Treasury-direct tax-
  treatment differences (Treasury interest is state-tax-exempt
  per 31 USC §3124).

### 5.4 International-allocation home-bias debate is genuinely unresolved

- **Statement**: International-allocation home-bias debate is
  genuinely unresolved — recommended ranges span 0% (Buffett, Bogle)
  to 40%+ (Vanguard target-date defaults) with little empirical
  convergence; the framing rarely surfaces that the choice is a
  judgment call rather than a calculation, and dogmatism in either
  direction (the "VTI-only" or "VT-global-only" camps) masks the
  actual uncertainty.
- **Source evidence**: `framings.md` §5 Excludes line on
  international-home-bias-debate-unresolved; Bogleheads voice on
  the persistent debate; retirement-econ academic voice on
  dispersion in recommended ranges; Bogle's *Common Sense on Mutual
  Funds* (2017 edition) on US-domestic-only stance vs Vanguard
  target-date-fund 40%-international default.
- **Trigger**: Asker is selecting equity allocation AND is
  encountering conflicting "all-US" vs "global-market-cap-weighted"
  advice AND is treating one camp as definitive AND has not
  separately recognized the debate is unresolved.
- **Failure mode**: Asker locks into "VTI only" (US-domestic-100%-
  equity) on Bogle/Buffett advice; misses the 2002-2007 cycle when
  international outperformed US substantially; OR locks into
  "VT-global-only" (40%+ international) on Vanguard default; misses
  the 2010-2020 cycle when US dramatically outperformed international.
  Either commitment creates a 1-2%/year tracking-error vs the
  alternative; over 30 years the difference compounds materially —
  but the *direction* of advantage is unknown ex-ante.
- **Recovery move**: For international-allocation choice, recognize
  the unresolved-debate explicitly; choose a range (10-30% common
  middle-ground) and *commit* with rebalance discipline rather than
  chasing recent-outperformance; consult a fee-only fiduciary CFP
  (NAPFA / XY-Planning) for personalized-context (currency-of-
  spending in retirement, geographic-arbitrage plans) before
  committing. Verify CFP via SEC IAPD Form ADV Part 2A before
  engagement.

### 5.5 Target-date-fund glide-path defaults vary materially across providers

- **Statement**: Target-date-fund single-vehicle implementation
  hides substantial *provider-specific glide-path variation* —
  Vanguard 2050 fund has 90/10 equity at age-25 ramping to 50/50 at
  age-65 then 30/70 at age-72; Fidelity 2050 fund has 90/10 to
  60/40 to 27/73; Schwab 2050 has 95/5 to 55/45 to 25/75; TIAA-CREF
  2050 has more conservative entry (85/15). The "set-and-forget
  target-date fund" reflex obscures that the choice of *provider*
  encodes a glide-path policy decision the asker isn't making
  consciously.
- **Source evidence**: `framings.md` §5 Mental model line on
  target-date-fund single-vehicle glide path with different
  defaults named; Bogleheads voice on target-date-fund-comparison
  forum threads; The Finance Buff voice on provider-specific
  glide-path differences.
- **Trigger**: Asker is using target-date fund as primary
  retirement vehicle AND has selected the fund without comparing
  provider-specific glide-paths AND is reasoning about it as if
  target-date funds are interchangeable.
- **Failure mode**: Asker selects "Schwab Target 2050" in their
  workplace 401(k) without realizing the glide-path is materially
  more aggressive than Vanguard's at retirement (25/75 vs 30/70);
  over 30+ years the cumulative-allocation-difference produces
  $50k-$200k of terminal-balance variance depending on equity
  realized returns; the asker had a *de facto* allocation policy
  they didn't choose.
- **Recovery move**: For target-date-fund users, *explicitly verify*
  the provider's glide-path against the asker's risk preference;
  compare across Vanguard / Fidelity / Schwab / TIAA / T. Rowe Price
  defaults; consider 3-fund-Bogleheads-portfolio if the workplace
  plan offers low-cost-index alternatives; consult a fee-only
  fiduciary CFP (NAPFA / XY-Planning) for personalized glide-path
  alignment. Verify CFP via SEC IAPD before engagement.

## 6. Behavioral-debt-payoff framing

### 6.1 Snowball-default paternalism mis-routes the avalanche-disciplined asker

- **Statement**: The framing's "snowball wins for at-risk-of-giving-
  up askers" is correct on average but can be paternalistic when
  applied to the high-financial-literacy asker who genuinely is
  avalanche-disciplined — the math-optimal asker who is pushed into
  snowball-by-default loses real money over the multi-year payoff
  window. The framing rarely surfaces the asker-classification
  step before applying the conclusion.
- **Source evidence**: `framings.md` §6 Excludes line on
  paternalistic snowball-default for avalanche-disciplined asker;
  opposes F2 (marginal-rate / pure-arithmetic) on the technical-
  correctness axis; personal-finance-influencer voice (Dave Ramsey
  Baby Steps canonically snowball; Suze Orman canonically snowball
  with emergency-fund-first variant) propagating snowball as
  universal.
- **Trigger**: Asker is high-financial-literacy AND has stable
  income AND has historical discipline on multi-year financial
  plans AND is being pushed toward snowball method by influencer-
  voice advice without engaging with the avalanche math.
- **Failure mode**: Asker (high-literacy, software engineer with
  stable income) has $20k credit-card at 22% APR, $15k auto-loan
  at 7% APR, $5k personal-loan at 12% APR; influencer advice
  pushes snowball (start with smallest = $5k personal-loan);
  asker follows; total interest paid over 36-month payoff is
  $4,200 vs $3,300 if avalanche (start with highest-APR credit-
  card); $900 of behavior-tax that wasn't necessary for this
  asker.
- **Recovery move**: Before applying snowball-vs-avalanche default,
  *classify the asker* explicitly on (a) financial-literacy
  (independent indicator beyond income), (b) historical multi-year
  financial-plan-completion track record, (c) cash-flow stability;
  for avalanche-disciplined askers, recommend avalanche method;
  for the high-risk-of-giving-up asker, recommend snowball method.
  Consult a fee-only fiduciary CFP (NAPFA / XY-Planning) for
  borderline cases; verify CFP via SEC IAPD Form ADV Part 2A
  before engagement.

### 6.2 PSLF / IDR forgiveness inverts the "pay highest-rate first" reflex

- **Statement**: Student-loan PAYE / SAVE / IDR forgiveness
  *fundamentally breaks* the debt-payoff-vs-invest framing — on
  PSLF-track (Public Service Loan Forgiveness for 10-year-
  qualified-employment-with-120-qualifying-payments-on-IDR) the
  "after-tax-effective debt rate" is near-zero because the balance
  will be forgiven, and accelerating payment destroys the
  forgiveness value. The framing's "pay highest-rate first" reflex
  catastrophically mis-routes the PSLF-eligible asker into
  refinancing-to-private and losing forgiveness.
- **Source evidence**: `framings.md` §6 Excludes line on PSLF / IDR
  forgiveness inverting the debt-payoff calculus; cross-domain
  edge into `education-funding` per `decisions.md` §D5;
  retirement-experienced-CPA voice on the IDR-vs-private-refi
  decision; chronic-DIY-Reddit voice (r/StudentLoans, r/PSLF) on
  the refi-trap.
- **Trigger**: Asker has federal student loans AND is in or
  eligible-for PSLF-qualifying employment (501(c)(3) nonprofit /
  government / qualifying-public-service) AND is contemplating
  refinancing to private OR accelerating payment beyond IDR-
  required AND has not separately verified PSLF qualification.
- **Failure mode**: Asker refinances $180k federal student loans
  to private at 5.5% APR to "lock in a low rate and pay off
  faster"; loses PSLF-eligibility permanently (private loans don't
  qualify); had been on track for $80k-$120k of forgiveness after
  10 years of qualifying payments on IDR. Net loss: the entire
  forgiveness amount, $80k-$120k.
- **Recovery move**: For any asker with federal student loans AND
  potential PSLF qualifying employment, *never* recommend refi-to-
  private without explicit PSLF analysis first; verify PSLF
  qualification via PSLF Help Tool (studentaid.gov/pslf) and
  employer-certification (Form PSLF-ECF); consult a retirement-
  experienced CPA with explicit student-loan-IDR-tax-bomb
  experience (IDR forgiven balance is taxable as ordinary income
  for non-PSLF tracks; PSLF forgiveness is tax-free per IRC
  §108(f)) before any refi decision. Verify CPA via SEC IAPD before
  engagement.

### 6.3 Mortgage-vs-invest is a special case framings binary misses

- **Statement**: Mortgage-payoff-vs-invest is a *special case* with
  three competing valid reasons to pay off (sequence-of-returns
  risk reduction, cash-flow reduction in retirement, emotional
  security) versus three competing valid reasons to invest (after-
  tax-arbitrage when mortgage rate < expected-investment-return,
  tax-deductibility for itemizers, liquidity preservation). The
  framing's binary "pay debt or invest" misses the configuration
  where *both* are right answers depending on the asker's specific
  life-stage and risk-profile.
- **Source evidence**: `framings.md` §6 Excludes line on mortgage-
  vs-invest special case; cross-domain edge into `housing` per
  `decisions.md` §D5. Retirement-econ academic voice (Wade Pfau on
  reverse-mortgage / paid-off-home-as-bond-substitute research;
  Michael Kitces on mortgage-vs-invest sequence-of-returns analysis).
- **Trigger**: Asker has a mortgage AND has investable surplus AND
  is reasoning about extra-payment vs additional-investment as a
  binary AND has not separately modeled life-stage / risk-profile /
  rate-arbitrage variables.
- **Failure mode**: Asker (age 55, 3.5% mortgage from 2021 refi,
  $400k balance) accelerates mortgage payoff at $30k/year extra;
  forgoes equity-investment expected-return of ~6%-real on the
  $30k; opportunity cost over 10 years is $50k-$100k. OR: asker
  (age 65, retired, 6.5% mortgage from 2024) maintains 30-year
  amortization in retirement; sequence-of-returns risk on the
  portfolio funding the mortgage payments is binding; would have
  been safer to use part of portfolio to pay off mortgage at
  retirement. Same framing, opposite right-answer depending on
  rate / life-stage.
- **Recovery move**: For mortgage-vs-invest decisions, build a
  multi-variable model: (a) mortgage rate (after-tax-deductibility
  if itemizing), (b) expected investment return with realistic
  uncertainty band, (c) life-stage (years to retirement / years
  in retirement), (d) sequence-of-returns risk profile,
  (e) emotional-security weight; consult a fee-only fiduciary CFP
  (NAPFA / XY-Planning) with retirement-income-specialty;
  cross-check via The Finance Buff or Kitces analyses for the
  arithmetic. Verify CFP via SEC IAPD before engagement.

### 6.4 Cash-flow vs balance-sheet distinction in extreme cases

- **Statement**: The "behavioral discipline" framing under-engages
  with the *cash-flow vs balance-sheet* distinction — an asker
  drowning in $15k credit-card debt but with $40k in a Roth IRA
  could technically withdraw Roth principal penalty-free (per
  Pub 590-B ordering rules: contributions are first-out and
  always penalty-and-tax-free) to clear the debt (the math-optimal
  move in extreme cases), but behavioral-debt framings reflexively
  oppose "raiding retirement" without engaging with the asymmetry
  between high-interest-revolving-debt and tax-advantaged-savings.
- **Source evidence**: `framings.md` §6 Excludes line on cash-flow-
  vs-balance-sheet distinction in extreme cases; The Finance Buff
  voice on Roth-IRA-ordering-rules per Pub 590-B; IRS-publication-
  authority voice (Pub 590-B ordering rules).
- **Trigger**: Asker has high-interest revolving debt ($10k+ at
  18%+ APR) AND has Roth IRA principal-contributions available AND
  is reasoning about debt-vs-retirement from "don't raid the
  retirement" reflex without engaging with the ordering-rule math.
- **Failure mode**: Asker (age 30, $20k credit-card debt at 22%
  APR, $40k Roth IRA with $35k of contribution-basis) follows
  "never raid retirement" advice; pays minimum on credit-card while
  trying to invest more; over 5 years pays $11k in credit-card
  interest; the Roth IRA grows by maybe $5k less than the
  alternative path of withdraw-$20k-principal-to-clear-debt-then-
  rebuild. Net: the rigid "never touch retirement" reflex cost the
  asker ~$15k.
- **Recovery move**: For extreme high-interest-debt + Roth-IRA-
  basis cases, recognize the option exists per Pub 590-B ordering
  rules; verify the asker's specific Roth-IRA basis via Form 5498
  history; model the trade-off explicitly (interest-saved vs lost-
  Roth-compounding); consult a retirement-experienced CPA via SEC
  IAPD on the basis-tracking arithmetic before withdrawing. Plan
  for *immediate-rebuild* of Roth contributions in subsequent
  years (cap-room is per-year, so rebuilding takes 5+ years on
  $7,000/year cap).

### 6.5 Emergency-fund-first reflex blocks match-capture for the low-emergency-fund household

- **Statement**: The "emergency fund first" reflex (per Dave Ramsey
  Baby Step 1 / 3, Suze Orman canonical advice) is the right
  discipline for the high-risk-of-cash-flow-crisis household but
  *catastrophically* blocks match-capture for the low-emergency-
  fund household — an asker waiting to fully fund $30k emergency
  fund before capturing $11.7k/year employer match forgoes the
  100% immediate return for 2-3 years. The framing rarely engages
  with the *match-and-emergency-fund-can-coexist* configuration.
- **Source evidence**: `framings.md` §6 Mental model line on
  emergency-fund-first when fragile; personal-finance-influencer
  voice (Dave Ramsey Baby Steps; Suze Orman) propagating
  emergency-fund-first as universal; Bogleheads voice on the match-
  capture-AND-emergency-fund compatibility.
- **Trigger**: Asker is W-2-employed with 401(k) match available
  AND has incomplete emergency fund (<3 months expenses) AND is
  following emergency-fund-first influencer advice that delays
  match-capture.
- **Failure mode**: Asker (age 28, $50k salary, 6% match on first
  6% of contribution = $3,000/year match) follows "build 6-month
  $30k emergency fund first" advice; takes 3 years to build at
  $10k/year of saving discipline; over those 3 years foregoes
  $9,000 of employer match. The match-room is per-year-use-it-or-
  lose-it; that $9,000 cannot be recovered even after the emergency
  fund is built.
- **Recovery move**: For W-2 employees with available match,
  *always* capture the match concurrently with emergency-fund
  building (even at minimum: contribute the match-percentage,
  direct remaining surplus to emergency-fund); recognize that
  401(k) contributions can be partially-accessed via 401(k) loan
  in true-emergency (50% of vested-balance up to $50k per IRC
  §72(p)) — so the 401(k) doubles as a partial emergency-buffer
  in extreme cases. Consult a retirement-experienced CPA via SEC
  IAPD for the specific match-and-emergency-fund-coordination
  arithmetic; do NOT take the universal "emergency-fund first" at
  face value when match-capture is on the table.

## 7. Time-horizon-and-lifecycle framing

### 7.1 Human capital is equity-like for equity-comp tech employees

- **Statement**: The framing's "young = equity-heavy" reflex
  assumes the asker's human capital is bond-like (stable
  employment, rising wages, predictable career arc) — but for
  equity-comp-heavy tech employees, contract / gig workers, and
  self-employed askers, human capital is itself *equity-like*
  (volatile, market-correlated, downside-correlated with broader
  equity markets in a recession). The framing's aggressive-young-
  equity reflex over-concentrates equity risk when human capital
  is equity-like.
- **Source evidence**: `framings.md` §7 Excludes line on human-
  capital-equity-like for equity-comp; cross-domain edge into
  `tech-career` per `decisions.md` §D4. Retirement-econ academic
  voice (Larry Kotlikoff's economic-spending-vs-saving framework;
  Moshe Milevsky on human-capital-as-bond research); financial-
  economics-journalism voice (Jeff Sommer at NYT on tech-recession
  human-capital-drawdown reporting).
- **Trigger**: Asker is tech employee / contractor / gig worker /
  self-employed AND has significant employer-stock concentration
  OR has industry-correlated job-security AND is reasoning about
  100%-equity allocation purely from "young = aggressive" framing
  without engaging with human-capital correlation.
- **Failure mode**: Asker (age 28, tech employee) holds 100%
  equity allocation across all accounts; 2022-2023 tech downturn
  hits; employer-stock concentration declines 60%; asker is laid
  off mid-downturn at depressed-equity-prices; portfolio also
  drops 30% on broad-equity correlation; emergency-fund (held in
  equity for "long horizon") is liquidated at -30% to cover
  living expenses. The 100%-equity allocation was structurally
  wrong because human-capital was correlated, not orthogonal.
- **Recovery move**: For equity-comp / industry-correlated
  human-capital askers, model human capital as *equity-like* not
  *bond-like* in the allocation decision; tilt the portfolio
  *more conservative* than the generic age-based glide-path (e.g.
  60/40 at age-28 rather than 100/0); maintain an emergency-fund
  in cash / short-Treasury rather than equity; consult a fee-only
  fiduciary CFP (NAPFA / XY-Planning) with tech-employee-specialty
  on the human-capital-correlation analysis. Verify CFP via SEC
  IAPD Form ADV Part 2A before engagement.

### 7.2 Rising-equity-glide is academically supported but institutionally fought

- **Statement**: Bond-tent and rising-equity-glide are
  *counterintuitive* (most retirees do the opposite — they shift
  more conservative across retirement to "preserve principal"),
  and the framing rarely engages with the practical-implementation
  barriers (employer-target-date-fund glide paths run conservative;
  advisors face liability incentive to shift conservative; the
  asker's own anxiety in down markets pushes conservative). The
  academic literature supports rising-equity-glide; the
  institutional and psychological environment fights it.
- **Source evidence**: `framings.md` §7 Excludes line on bond-tent
  / rising-equity-glide implementation barriers; retirement-econ
  academic voice (Wade Pfau's *Reverse Glide Path* research, Pfau
  & Kitces 2014 *Journal of Financial Planning* paper on rising-
  equity-glide); fee-only fiduciary CFP voice on the liability-
  incentive-vs-academic-evidence tension.
- **Trigger**: Asker is approaching or in early retirement (age
  55-70) AND is using a default-conservative target-date-fund
  glide-path AND has not separately considered rising-equity-glide
  AND has discretion to deviate from the workplace-default.
- **Failure mode**: Asker (age 67, retired) uses Vanguard 2025
  Target Date which is at 50/50 declining to 30/70 over 7 years
  past retirement; sequence-of-returns risk in early retirement
  years is the binding risk; bond-heavy allocation increases
  sequence-risk exposure (counterintuitively); 30-year-retirement
  sustainable spend is lower than rising-equity-glide alternative.
  Pfau / Kitces models suggest 5-10% higher safe-withdrawal-rate
  with rising-equity-glide.
- **Recovery move**: For early-retirement askers, consider rising-
  equity-glide (start retirement at 30-40% equity, ramp to 60-70%
  equity by age 80-85) per Pfau / Kitces research; recognize the
  institutional default (target-date-fund) is conservative-glide
  not rising-equity-glide; consult a fee-only fiduciary CFP (NAPFA
  / XY-Planning) with retirement-income-specialty AND a retirement-
  econ academic resource (Pfau's RetirementResearcher;
  Kitces.com Nerd's Eye View) for the rising-equity-glide
  arithmetic. Verify CFP via SEC IAPD before engagement.

### 7.3 4% safe-withdrawal-rate is calibrated to US 30-year history

- **Statement**: The "safe withdrawal rate" framing (Bengen 4%
  rule, Kitces variable, Pfau retirement-glide-rules) is calibrated
  to *historical* US market returns over rolling 30-year periods,
  and the framing rarely surfaces that international historical
  returns include multi-decade flat markets (Japan 1989-present,
  France 1960-1995) where 4% would have failed. The "safe
  withdrawal rate" terminology implies a certainty the historical
  data doesn't deliver.
- **Source evidence**: `framings.md` §7 Excludes line on safe-
  withdrawal-rate calibration-to-historical-US data; retirement-
  econ academic voice (Wade Pfau on international-historical-data
  failure-rate research; Big-ERN's *Early Retirement Now* SWR
  series on Japan-and-France data extension); FIRE voice
  recognition of the 3-3.5% sustainable rate for early-FIRE
  horizons.
- **Trigger**: Asker is using 4% safe-withdrawal-rate as a planning
  anchor AND has 30+ year retirement horizon (early-FIRE, long
  life-expectancy) AND is treating 4% as a stable-floor rather
  than a US-30-year-historical estimate.
- **Failure mode**: Asker (age 45, early-FIRE, $1M target) uses
  4% SWR = $40k/year sustainable; faces 50-year retirement;
  international-historical-data suggests 3-3.25% is the actual
  sustainable rate for 50-year horizons; the $40k/year spend is
  ~25% above sustainable; portfolio depletion by year 40 in
  realistic scenarios. The "4% safe" terminology was overconfident.
- **Recovery move**: For long-horizon retirement (40+ years), use
  3-3.5% SWR not 4% per Pfau / Big-ERN extended-data research;
  build a variable-spending plan (Guyton-Klinger guardrails,
  Kitces variable-SWR) that adjusts spend down in bad-sequence
  years; consult a retirement-econ academic resource (Pfau's
  RetirementResearcher; Big-ERN's SWR series at
  earlyretirementnow.com) AND a fee-only fiduciary CFP (NAPFA /
  XY-Planning) with retirement-income-specialty. Verify CFP via
  SEC IAPD Form ADV Part 2A before engagement.

### 7.4 Linear-career-assumption breaks for sabbatical / layoff / second-career

- **Statement**: The lifecycle framing assumes a *linear* career
  arc; sabbaticals, job-loss, layoff, caregiver-leave-from-
  workforce, and second-career-pivot break the assumed glide-
  path-of-earnings, and the framing rarely engages with how to
  *reset* the glide-path mid-life when the trajectory shifts. The
  Mr-Money-Mustache / FIRE community voice catches this (early-
  retirement-as-default-option); the traditional lifecycle voice
  doesn't.
- **Source evidence**: `framings.md` §7 Excludes line on linear-
  career-assumption breaking for non-linear trajectories;
  Mr-Money-Mustache / FIRE community voice canonical on early-
  retirement-as-default-option; chronic-DIY-Reddit voice
  (r/financialindependence, r/leanFIRE) on the sabbatical-Roth-
  conversion-window mechanic.
- **Trigger**: Asker is contemplating sabbatical / planned
  unemployment / caregiver-leave / second-career-pivot AND is
  using lifecycle planning anchored to linear-career assumptions
  AND has not separately modeled the trajectory-shift implication
  on contribution-pace / Roth-conversion-window / glide-path-
  reset.
- **Failure mode**: Asker (age 38) takes 2-year sabbatical without
  re-running lifecycle plan; continues conservative allocation
  inherited from "age-based" rule; misses the sabbatical-year as
  a low-income Roth-conversion window (could convert $40-60k of
  traditional-401(k) to Roth at 12-22% effective rate vs the
  pre-sabbatical 32% rate); misses 2 years of contribution-room
  that could have been replaced by self-employed solo-401(k) if
  consulting; returns to traditional W-2 employment without
  ever-having captured the sabbatical financial-windows.
- **Recovery move**: For any career-trajectory-shift event,
  *re-run* the lifecycle plan: identify Roth-conversion-window
  opportunities in low-income years; reset the glide-path to the
  new trajectory; consider solo-401(k) / SEP-IRA if consulting
  income materializes; consult a fee-only fiduciary CFP (NAPFA /
  XY-Planning) with FIRE / non-linear-career specialty AND a
  retirement-experienced CPA for the Roth-conversion sizing.
  Verify both via SEC IAPD before engagement.

### 7.5 Decumulation-phase advisors face liability-incentive toward conservative

- **Statement**: The lifecycle framing under-engages with the
  *advisor liability-incentive structure* in decumulation phase —
  advisors face asymmetric-liability exposure for client losses
  (clients sue for losses, rarely for opportunity-cost-of-
  conservatism), which pushes advisor recommendations toward
  *more conservative than academically-supported* allocations and
  withdrawal rates. The framing's "consult an advisor" reflex
  doesn't engage with the structural-bias-toward-conservative.
- **Source evidence**: `framings.md` §7 Excludes line on
  implementation barriers including advisor liability incentive
  shifting conservative; fee-only fiduciary CFP voice on the
  structural-conflict (some practitioners write about this; many
  practice from within the bias); retirement-econ academic voice
  (Kitces on the advisor-vs-academic decumulation gap).
- **Trigger**: Asker is in decumulation phase (post-retirement) AND
  is working with an AUM-fee advisor AND has received recommendation
  to "shift more conservative for safety" AND has not separately
  cross-checked the recommendation against retirement-econ academic
  guidance.
- **Failure mode**: Asker (age 70, $1.5M portfolio, advisor-managed
  AUM at 1%) receives recommendation to shift from 60/40 to 30/70;
  asker complies; over 15-year remaining-lifespan the more-
  conservative allocation underperforms by ~1.5-2%/year vs
  academic-research rising-equity-glide; terminal-balance is $400k-
  $700k lower than alternative; advisor faces no liability for
  the opportunity-cost; asker has no recourse.
- **Recovery move**: For decumulation-phase allocation advice, cross-
  check advisor recommendations against retirement-econ academic
  research (Pfau's RetirementResearcher; Kitces.com Nerd's Eye View);
  recognize the AUM-fee structural-bias toward conservative; consult
  an *hourly-fee or flat-fee* fee-only fiduciary CFP (Garrett-Planning-
  Network specializes in hourly-fee for second-opinion work) as a
  conflict-mitigated alternative second-opinion source. Verify all
  advisors via SEC IAPD Form ADV Part 2A AND FINRA BrokerCheck for
  disclosure events before engagement.

## 8. Asset-protection-and-creditor-shield framing

### 8.1 401(k)-fee vs shield-benefit trade-off is structurally invisible

- **Statement**: The framing's "stay in 401(k) for unlimited shield"
  reflex misses that 401(k) plans charge plan-administration fees
  that can compound to material drag over decades; the creditor-
  protection benefit is real but priced — for HNW-but-low-
  litigation-risk askers, the rollover-to-low-cost-IRA is genuinely
  the right move and the framing's blanket "don't roll over"
  overstates the protection benefit. Asker-specific litigation-
  risk-assessment is the missing step.
- **Source evidence**: `framings.md` §8 Excludes line on 401(k)-
  fee vs shield trade-off; ERISA-practitioner voice on the actual
  risk-profile-conditional rollover decision; Bogleheads voice on
  401(k)-plan-fee analysis.
- **Trigger**: Asker is HNW (>$1M retirement balance) AND is in
  low-litigation-risk profession (W-2 engineer, salaried admin,
  retired) AND is being advised "stay in 401(k) for shield" AND
  the 401(k) has materially higher expense ratios than rollover-
  IRA alternatives.
- **Failure mode**: Asker (age 60, $2M 401(k) in employer plan with
  0.75% expense ratio, retiring in 2 years, software engineer with
  no professional-liability exposure, no business-ownership)
  follows "don't roll over for shield" advice; pays 0.75% × $2M =
  $15k/year in plan-fee drag for 20+ years of retirement; total
  fee leakage $300k+ vs $20k-$40k on equivalent IRA at 0.05%-
  0.15% expense; creditor-protection benefit was structurally
  irrelevant given low-litigation profile.
- **Recovery move**: For rollover-vs-stay-in-401(k) decisions, build
  the *risk-conditional* trade-off: (a) actual litigation-risk
  profile (profession, business-ownership, state-of-residence,
  net-worth-attracting-suits, history of disputes), (b) 401(k)
  plan-fee disclosure (Form 5500 + participant disclosure),
  (c) state-specific IRA shield law for asker's state-of-residence,
  (d) inherited-IRA-implication for heirs (per §8.3 *Clark v
  Rameker*); consult an ERISA attorney for high-balance / disputed
  cases AND a fee-only fiduciary CFP (NAPFA / XY-Planning) for the
  cost-arithmetic. Verify both via SEC IAPD before engagement.

### 8.2 State-shield-law currency requires date-stamp verification

- **Statement**: State-shield law is *non-uniform and shifts* —
  California AB-3088 / state-shield amendments, Florida's recent
  homestead-exemption expansions, Texas-specific HSA-protection
  statutes — the framing's "lookup-table" discipline needs date-
  of-application currency that generic advice doesn't deliver. The
  framing rarely surfaces "verify the current statute" as the
  load-bearing step before relying on a 5-year-old summary.
- **Source evidence**: `framings.md` §8 Excludes line on state-
  shield-law non-uniformity and currency requirement; ERISA-
  practitioner voice on the per-state-shield-mapping exercise;
  state-bar-estate-attorney voice on the state-statute date-stamp
  verification practice.
- **Trigger**: Asker is making a creditor-protection-driven decision
  (rollover, account-titling, gift-vs-retain, trust-formation) AND
  is relying on a state-shield summary that is 2+ years old AND has
  not separately verified the current state statute.
- **Failure mode**: Asker (Texas resident) relies on 2021 summary
  showing "Texas unlimited IRA protection plus HSA protection";
  makes a large IRA rollover and HSA accumulation; the Texas
  statute is subsequently amended (or interpreted by state-court
  decision); the protection footprint is materially narrower than
  the asker assumed; in subsequent litigation event the assumed
  shield doesn't hold.
- **Recovery move**: For any creditor-protection-driven decision,
  verify the *current* state statute via state bar / state legal-
  research-service / Westlaw / Lexis as of the decision date;
  consult a state-bar-licensed estate attorney OR ERISA attorney
  (depending on the account type) via state-bar lawyer-referral-
  service (NOT a for-profit finder) to confirm the current shield-
  footprint; document the verification date in case of subsequent
  challenge. Verify attorney via SEC IAPD if dual-licensed, OR via
  state-bar member-search for state-bar status.

### 8.3 Clark v Rameker — inherited-IRA loses bankruptcy protection

- **Statement**: Inherited-IRA was held in *Clark v Rameker* 573 US
  122 (2014) to NOT be federal-bankruptcy-exempt — the Supreme
  Court ruled that an inherited IRA does not qualify as
  "retirement funds" under 11 USC §522(b)(3)(C) because the non-
  spouse-beneficiary cannot contribute to it and is required to
  take distributions. The framing's "IRA is bankruptcy-exempt"
  reflex catastrophically misroutes the asker who inherited an
  IRA and faces a bankruptcy event — the inherited IRA is exposed
  to creditors. Some state-laws specifically protect inherited
  IRAs (Texas, Florida, Arizona, Idaho, Missouri, North Carolina,
  Ohio); most don't.
- **Source evidence**: `framings.md` §8 Excludes line on *Clark v
  Rameker* inherited-IRA exposure; cross-domain edge into `family-
  planning` D10 per `decisions.md` §D10. ERISA-practitioner voice
  on the *Clark* doctrine; state-bar-estate-attorney voice on the
  state-shield-of-inherited-IRA variation.
- **Trigger**: Asker has inherited an IRA from non-spouse decedent
  AND is in or facing potential bankruptcy / lawsuit / creditor-
  pressure AND is reasoning about "IRA is protected" from the
  general framing without engaging with *Clark* doctrine.
- **Failure mode**: Asker (age 45, just inherited $300k IRA from
  deceased parent in 2024) faces creditor-pressure / Chapter 7
  bankruptcy in 2025; relies on "IRA is bankruptcy-exempt" general
  understanding; bankruptcy trustee challenges and seizes the
  inherited IRA per *Clark v Rameker*; asker loses the entire
  $300k. If asker had been in a state-shield state (TX/FL/AZ/ID/
  MO/NC/OH) AND used state-shield rather than federal-bankruptcy-
  exemption, the result would have been different; the
  jurisdictional choice was load-bearing.
- **Recovery move**: For any asker with inherited IRA AND any
  creditor-protection concern (current litigation, professional-
  liability profession, business-ownership), consult an ERISA
  attorney immediately on *Clark v Rameker* implications AND a
  state-bar-licensed estate attorney on whether the asker's state
  protects inherited IRAs (TX/FL/AZ/ID/MO/NC/OH affirmative
  protection; others varying); consider *during-life-conversion*
  of decedent's IRA to Roth as a planning move to convert exposed-
  inherited-traditional to less-exposed-inherited-Roth (still
  subject to 10-year-rule per SECURE 1.0 but Roth-character
  preserved). Verify attorney via SEC IAPD AND state-bar member-
  search before engagement.

### 8.4 Over-isolation cost can exceed protection benefit

- **Statement**: The framing's asset-protection focus can mask
  *over-isolation* risk — askers who layer LLC / trust / off-shore
  structures to maximize protection often face material
  administrative costs, complexity, and IRS-audit-attention that
  exceed the protection benefit. Asset-isolation is a real-cost
  decision, not a free upgrade.
- **Source evidence**: `framings.md` §8 Excludes line on over-
  isolation administrative cost; cross-domain edge into
  `entrepreneurship` / `legal-disputes` per `decisions.md` §D10.
  State-bar-estate-attorney voice on the over-engineered-structure-
  vs-actual-need tension; SEC-EDGAR / FINRA-BrokerCheck voice on
  the off-shore-structure-promoter conflict-of-interest pattern.
- **Trigger**: Asker is being marketed off-shore-trust / asset-
  protection-LLC / sophisticated-shield-structure packages AND has
  not separately evaluated whether the protection benefit justifies
  the administrative cost AND has not verified the promoter's
  credentials.
- **Failure mode**: Asker (HNW physician, $5M net worth, real
  litigation risk from professional-liability) signs up for $20k
  / year asset-protection-LLC + off-shore-trust package; spends
  20-40 hours/year on entity-maintenance, multi-state filings,
  FinCEN BOI / FBAR / Form 8938 / Form 5471 / Form 8865 reporting;
  faces IRS audit for the multi-entity structure; legal-fees
  defending the structure exceed the protection-benefit in
  realistic-litigation scenarios. The structure-promoter's
  commission was the actual beneficiary.
- **Recovery move**: For asset-protection structuring, consult a
  state-bar-licensed estate attorney OR an asset-protection
  attorney (verify state-bar AND specialty via state-bar member-
  search) BEFORE engaging any promoter; ask explicitly "what is the
  protection benefit relative to my actual risk profile, and what
  is the all-in annual administrative cost"; cross-check the
  promoter via SEC IAPD + FINRA BrokerCheck for disclosure events;
  prefer the *simplest* structure that meets the actual protection
  need (often just umbrella-insurance + entity-formation for
  business-ownership) over multi-layer structures.

### 8.5 Egelhoff doctrine — beneficiary form supersedes will and state law

- **Statement**: ERISA-plan beneficiary forms control over both the
  will AND state property law including divorce-revocation statutes
  (per *Egelhoff v Egelhoff* 532 US 141 (2001) — the Supreme Court
  ruled state-law revocation-on-divorce is pre-empted by ERISA, so
  an outdated beneficiary form trumps the divorce decree). The
  framing names this as load-bearing precedent but askers and even
  attorneys regularly fail to *update* beneficiary forms after
  marriage / divorce / birth / death, creating beneficiary-form-
  vs-will mismatch that defeats estate plans.
- **Source evidence**: `framings.md` §8 Excludes line on Egelhoff
  doctrine + operational friction on beneficiary-form audit;
  cross-domain edge into `family-planning` D10 per `decisions.md`
  §D10. ERISA-practitioner voice on the per-Egelhoff doctrine;
  state-bar-estate-attorney voice on the beneficiary-form-audit
  discipline.
- **Trigger**: Asker has had any life-event in the last 5 years
  (marriage, divorce, birth, death of spouse / parent / child) AND
  has not separately audited 401(k) / IRA / Roth / HSA / life-
  insurance / pension / TOD-POD beneficiary forms post-event.
- **Failure mode**: Asker (age 50) divorces in 2018; updates will;
  fails to update 401(k) beneficiary (still names ex-spouse as
  100% primary); dies suddenly in 2024; 401(k) of $800k goes to
  ex-spouse per Egelhoff doctrine despite the divorce-revocation
  statute in asker's state; current spouse and children receive
  nothing from the 401(k); the will's bequest to current spouse /
  children is moot because the 401(k) is non-probate. Recovery
  via litigation against ex-spouse (constructive-trust theories,
  fraud-on-spouse-during-marriage claims) is expensive and
  uncertain.
- **Recovery move**: Audit ALL beneficiary forms (401(k), IRA, Roth-
  IRA, HSA, life-insurance, pension, TOD / POD on taxable accounts,
  TOD-deed on real estate in permitted states) on every life-event
  AND annually; document the audit date in a beneficiary-form-
  inventory spreadsheet; for high-balance accounts ($100k+), use
  certified-mail or custodian-confirmation-email to verify the
  custodian received and processed the update; consult a state-bar-
  licensed estate attorney for trust-as-beneficiary structuring
  questions (see-through-trust requirements per IRC §401(a)(9));
  consult an ERISA attorney via state-bar member-search for high-
  balance 401(k) beneficiary-form complications.

## 9. Estate-and-intergenerational framing

### 9.1 Withdrawal-sequence inversion for intent-to-bequeath missed by lifecycle default

- **Statement**: The intent-to-bequeath framing routes toward
  *holding-appreciated-taxable-for-step-up* — but this directly
  conflicts with the lifecycle / safe-withdrawal-rate framing's
  "taxable first" sequence, and many advisors and asker-self-models
  default to lifecycle without engaging with the bequest-intent
  override. The framing's asymmetry-recognition is correct but
  commonly missed.
- **Source evidence**: `framings.md` §9 Excludes line on withdrawal-
  sequence inversion for intent-to-bequeath; opposes F7 directly on
  D8 per `framings.md` Cross-framing tensions. Retirement-econ
  academic voice (Michael Kitces on withdrawal-sequencing inversion
  for bequest-intent households); state-bar-estate-attorney voice
  on the basis-step-up-at-death (IRC §1014) load-bearing math.
- **Trigger**: Asker is in decumulation phase AND has stated intent-
  to-bequeath material assets to heirs AND is using lifecycle-
  default "taxable first" withdrawal sequence AND has not
  separately modeled basis-step-up vs traditional-IRA-ordinary-
  income-to-heirs.
- **Failure mode**: Asker (age 75, $3M portfolio split $1M
  traditional-IRA / $500k Roth / $1.5M taxable with $800k of
  appreciation) follows lifecycle "taxable first" sequence; spends
  taxable across age 65-75 realizing $800k of cap-gains over the
  decade; dies in 2030 with $1M traditional-IRA / $500k Roth / $0
  taxable remaining; non-spouse heirs inherit $1M traditional-IRA
  subject to SECURE 10-year-rule + ordinary-income-on-distribution
  ($300k-$400k of heir-side federal tax); had basis-step-up been
  preserved on $1.5M taxable, heirs would have received it with
  $0 capital-gain. Net asymmetry: $300k-$400k of avoidable heir-
  side tax.
- **Recovery move**: For intent-to-bequeath households, invert the
  withdrawal sequence: spend traditional-IRA-first (or aggressively
  Roth-convert during life) to leave heirs Roth or stepped-up-basis-
  taxable rather than ordinary-income-distribution-traditional;
  consult a fee-only fiduciary CFP (NAPFA / XY-Planning) with
  retirement-income-and-estate-planning specialty AND a state-bar-
  licensed estate attorney on the integrated withdrawal-and-
  bequest plan; consult a retirement-experienced CPA for the
  Roth-conversion-sizing-and-IRMAA / NIIT cliff arithmetic. Verify
  all via SEC IAPD before engagement.

### 9.2 SECURE 1.0 10-year rule has RMD-during-years-1-9 subtlety

- **Statement**: The SECURE 1.0 10-year-rule for non-spouse-non-EDB
  beneficiaries is *frequently misunderstood* — under final SECURE
  regulations (Feb 2024), if the decedent had already started RMDs
  (post-Required-Beginning-Date), the non-EDB heir must also take
  annual RMDs during years 1-9 AND empty the account by end-of-
  year-10; if the decedent died before their RBD, the heir can
  lump-or-stagger across the 10 years with no annual RMD. The
  framing's "10-year-rule means take it whenever in 10 years" is
  materially incomplete.
- **Source evidence**: `framings.md` §9 Excludes line on SECURE-1.0
  RMD-during-10-years misunderstood; cross-domain edge into
  `legal-disputes` on inheritance-procedural-disputes per
  `decisions.md` §D10. State-bar-estate-attorney voice on the
  final-SECURE-regulation reading; IRS-publication-authority voice
  (Pub 590-B inherited-IRA section; final IRS regulations Feb
  2024).
- **Trigger**: Asker has inherited an IRA / 401(k) from non-spouse
  decedent who died after their RBD AND is reasoning about
  withdrawal as "take it sometime in 10 years" AND has not
  separately verified whether the decedent had started RMDs at
  death.
- **Failure mode**: Asker inherits $400k traditional IRA from
  parent who had been taking RMDs at age 76; asker (age 50)
  assumes "I can take it any time in 10 years" and plans to lump-
  withdraw in year-10 to delay taxation; IRS regulations require
  annual RMDs in years 1-9 because decedent was post-RBD; asker
  fails to take year-1 RMD; IRS assesses 25% excise tax (reduced
  from 50% under SECURE 2.0 §302) on the missed RMD; asker also
  faces lump in year-10 of remaining balance at potentially-
  spiked-bracket. Compounded mis-planning.
- **Recovery move**: For inherited IRA / 401(k), immediately
  identify (a) whether decedent had started RMDs (post-RBD = yes
  for any death after age 73-75 depending on birth year),
  (b) whether asker qualifies as EDB (eligible-designated-
  beneficiary — spouse / minor-child / disabled / chronically-ill /
  not-more-than-10-years-younger), (c) the required-distribution
  schedule for years 1-9; consult a retirement-and-equity-comp-
  experienced CPA via SEC IAPD on the SECURE-1.0 final-regulation
  application AND a state-bar-licensed estate attorney for trust-
  as-beneficiary cases (see-through-trust requirements).

### 9.3 2025-sunset planning urgency politically uncertain

- **Statement**: The 2025-sunset planning urgency is *time-bound
  and politically uncertain* — Congress could extend the doubled
  exemption (multiple bills have been proposed; none have passed
  as of writing); advising aggressive pre-2026 gifting for
  households with $5-15M net worth carries real risk of "spent the
  exemption you didn't need to" if extension passes. The framing's
  "use-it-or-lose-it" urgency overstates certainty about the
  sunset.
- **Source evidence**: `framings.md` §9 Excludes line on 2025-
  sunset political uncertainty; cross-domain edge into `legal-
  disputes` per `decisions.md` §D10. State-bar-estate-attorney
  voice on the legislative-uncertainty calibration; financial-
  economics-journalism voice (Anne Tergesen at WSJ on estate-tax-
  sunset legislative posture).
- **Trigger**: Asker has $5-15M net worth AND is being advised to
  execute aggressive pre-2026 gifting (SLAT / GRAT / annual-
  exemption-front-loading) AND is treating the sunset as certain
  AND has not separately modeled the extension-scenario opportunity-
  cost.
- **Failure mode**: Asker (HNW $10M couple) executes $8M-each SLAT
  in 2025 to "use the doubled exemption before sunset"; Congress
  extends the doubled exemption in 2026; asker has now permanently
  given away $16M of estate that they didn't need to gift; lost
  control / lost income-stream / lost flexibility; the asymmetric-
  risk-tolerance call may have been wrong. Alternative: gift only
  the *minimum* hedge amount and retain optionality.
- **Recovery move**: For 2025-sunset planning, distinguish between
  "household genuinely needs to use the doubled exemption" (i.e.
  >$14M+ projected estate by reasonable longevity-and-growth
  scenarios) from "household is being optimized into using
  exemption because the planner gets a fee." For the marginal-
  exemption-need household, prefer *partial* gifting (use 50% of
  exemption) over full; preserve optionality for extension; consult
  a state-bar-licensed estate attorney (NOT a sales-driven trust-
  company promoter) via state-bar lawyer-referral-service AND a
  retirement-experienced CPA on the estate-tax-vs-during-life-
  income-needs analysis. Verify both via state-bar member-search
  AND SEC IAPD before engagement.

### 9.4 Beneficiary-form-audit operational friction defeats discipline

- **Statement**: Beneficiary-form-audit reflex is *correct and
  necessary* but the framing under-engages with the *practical
  barriers*: many custodians require paper forms returned by mail,
  beneficiary-form-changes on workplace 401(k) plans may require
  employer-HR coordination, and form-updates after marriage /
  divorce / birth / death often fall through the cracks of life-
  event-management. The framing's "audit annually" is the right
  discipline; the operational reality is more friction than the
  framing names.
- **Source evidence**: `framings.md` §9 Excludes line on
  beneficiary-form operational friction; ERISA-practitioner voice
  on the workplace-401(k)-HR-coordination friction; chronic-DIY-
  Reddit voice (r/personalfinance threads on custodian-paper-form
  delays).
- **Trigger**: Asker is contemplating beneficiary-form updates
  after a life-event AND has not separately scheduled the actual
  paper-form completion AND has not separately verified custodian
  receipt-and-processing of prior updates.
- **Failure mode**: Asker (age 55, recently married second time)
  intends to update 401(k) beneficiary; custodian requires paper
  form mailed with notarized signature; asker fills out form,
  mails it; form is lost in custodian intake; asker doesn't
  follow up; 5 years later asker dies; original ex-spouse remains
  on the 401(k) per Egelhoff doctrine (see §8.5). The intent to
  update was correct; the operational friction defeated it.
- **Recovery move**: For any beneficiary-form update, treat the
  paper-form completion as a *time-bounded task* with a follow-up
  date (4 weeks post-mailing) to verify custodian receipt-and-
  processing; request a written confirmation OR online-portal-
  verification that the update is recorded; document the update
  date in a beneficiary-form-inventory spreadsheet for next-year-
  audit; for high-balance accounts ($100k+), consider involving
  a state-bar-licensed estate attorney via state-bar lawyer-
  referral-service in the audit to verify the form-update is
  consistent with the overall estate plan.

### 9.5 529-grandparent-vs-parent FAFSA treatment changed under Simplification Act

- **Statement**: FAFSA treatment of 529 ownership changed under
  the FAFSA Simplification Act (effective 2024-25 academic year):
  *previously* grandparent-owned 529 distributions counted as
  student-income on FAFSA (worst possible treatment, reducing aid
  ~50% of distribution amount); *now* grandparent-owned 529 has
  no FAFSA impact at all (best possible treatment). The framing's
  "use parent-owned to minimize FAFSA hit" reflex from pre-2024
  guidance is now structurally wrong — grandparent-owned 529 is
  often the *optimal* configuration post-Simplification.
- **Source evidence**: `framings.md` §9 Excludes line on cross-
  domain edge into `family-planning`-grandparent-529 FAFSA
  treatment; `framings.md` §12 Excludes line on FAFSA
  Simplification Act; financial-economics-journalism voice (Jeff
  Sommer at NYT on FAFSA Simplification reporting); chronic-DIY-
  Reddit voice (r/personalfinance, r/college on 529-strategy
  threads).
- **Trigger**: Asker is contemplating 529 ownership structure (parent
  vs grandparent vs UTMA) for a child / grandchild approaching
  college AND is using pre-2024 guidance treating grandparent-529
  as FAFSA-penalty.
- **Failure mode**: Asker (grandparent, intends to fund $50k of
  grandchild's college) is advised to "transfer the 529 to
  parent-ownership" per pre-2024 FAFSA reflex; the grandparent
  loses control / loses ability to retract funds for grand-
  parent's own retirement needs; AND the grandparent-owned
  configuration would have actually been better post-2024
  Simplification (zero FAFSA hit vs the parent-owned configuration
  treating 529 balance as parent-asset at 5.64%).
- **Recovery move**: For 529-ownership decisions in 2024 and beyond,
  use FAFSA Simplification Act rules: grandparent-owned 529 has
  zero FAFSA impact (no income, no asset hit); parent-owned 529
  is treated as parent-asset at 5.64% assessment; for grandparent-
  funded education, prefer grandparent-ownership for control-and-
  flexibility AND optimal FAFSA treatment. Verify current FAFSA
  treatment via Federal Student Aid (studentaid.gov) AND consult
  a retirement-experienced CPA via SEC IAPD on the 529-vs-Roth
  funding-pace decision.

## 10. Professional-referral-and-conflict-of-interest framing

### 10.1 AUM-fee-fee-only-CFP still faces rollover-recommendation bias

- **Statement**: The framing's "fee-only is the gold-standard"
  reflex is *broadly correct* but masks within-fee-only variation
  — AUM-fee fee-only-CFPs still face rollover-recommendation bias
  (the same incentive that drives commission-broker rollover
  recommendations applies once the AUM is captured), and the
  framing rarely distinguishes AUM-fee-fee-only from hourly-or-
  flat-fee-fee-only. Garrett-Planning-Network is the sub-category
  for one-time-question or bounded-scope asker; the framing
  collapses these distinctions when over-applied.
- **Source evidence**: `framings.md` §10 Excludes line on AUM-fee-
  fee-only rollover-recommendation bias; fee-only-fiduciary-CFP
  voice (NAPFA's own analysis of within-fee-only variation;
  Garrett-Planning-Network distinguishing hourly-fee from AUM-fee);
  financial-economics-journalism voice on the structural-conflict
  reporting.
- **Trigger**: Asker is contemplating rollover-of-401(k)-to-IRA AND
  is using a fee-only CFP advisor on an AUM-fee basis AND has not
  separately verified whether the rollover recommendation is
  asker-optimal or AUM-growth-optimal.
- **Failure mode**: Asker (age 65, $1.5M 401(k) at job-end)
  consults a fee-only-AUM-fee CFP at 0.75% AUM; CFP recommends
  rollover-to-IRA (which CFP will manage); asker rolls over;
  consequence is (a) creditor-protection downgrade per §8.1,
  (b) ongoing 0.75% × $1.5M = $11.25k/year of AUM fee on
  $1.5M, (c) absence of in-service-Rule-of-55 access that the
  401(k) had if asker was 55+ at separation. The "fee-only =
  conflict-free" framing missed the structural-rollover-bias.
- **Recovery move**: For rollover decisions, get a *second opinion*
  from an hourly-or-flat-fee fee-only CFP (Garrett-Planning-Network
  is the canonical category) before committing; verify the
  recommending CFP's compensation structure via Form ADV Part 2A
  at SEC IAPD; explicitly ask "does your recommendation change if
  I keep this in the 401(k) instead?"; the answer-conditional-on-
  same-recommendation is the conflict-free signal. Verify CFPs via
  SEC IAPD AND FINRA BrokerCheck before engagement.

### 10.2 Fee-only-CFP coverage uneven across decision categories

- **Statement**: Fee-only-CFP coverage is *uneven across decision
  categories* — most CFPs are generalist and lack specialized
  depth in backdoor-Roth Form 8606, Mega-Backdoor Roth plan-
  document analysis, Roth-conversion sizing relative to IRMAA /
  NIIT / ACA cliffs, QSBS Section-1202 analysis, or ERISA-plan-
  document interpretation. The framing's "consult a fee-only CFP"
  reflex needs CPA / ERISA-attorney / tax-attorney over-ride for
  technical specialty questions.
- **Source evidence**: `framings.md` §10 Excludes line on CFP
  coverage uneven across decisions; cross-reference to `decisions.
  md` §Notes selective-referral matrix specifying CPA for D1, D6,
  D7 and ERISA-attorney for D1 + D10 technical-mechanic depth.
- **Trigger**: Asker has a technical-mechanic question (backdoor
  Roth, Mega-Backdoor Roth, ISO-AMT, QSBS, ERISA plan-document
  features) AND is using a generalist fee-only CFP without CPA /
  ERISA-attorney over-ride AND is treating the CFP's advice as
  sufficient.
- **Failure mode**: Asker (tech employee with $1M of vested-RSU and
  $200k of ISO-exercised-but-unsold) consults generalist fee-only
  CFP on tax-and-investment strategy; CFP recommends generic
  diversification + Roth-conversion-ladder without modeling AMT-
  parallel-tax-credit-recovery on the ISO exercise; asker executes
  Roth conversion in the same year as ISO exercise; combined-AMT
  parallel tax is $40k higher than coordinated planning would have
  produced; AMT-credit-recovery delays the offset by 5-15 years.
- **Recovery move**: For technical-mechanic questions, use the
  selective-referral matrix in `decisions.md` §Notes: CPA for
  Form 8606 / Form 8889 / Form 8949 / Form 1099-R mechanics; ERISA-
  attorney for plan-document features (Mega-Backdoor Roth, Rule-of-
  55, SEPP-72(t), QDRO); fee-only Social-Security-claiming
  specialist for SS-claim-age; state-bar-estate-attorney for trust
  formation. Verify each professional's specialty depth via SEC
  IAPD + FINRA BrokerCheck + state-bar member-search; ask
  explicitly "how many [specific-form / specific-mechanism] cases
  do you handle annually?"

### 10.3 DIY-via-Bogleheads-flowchart under-engaged as legitimate alternative

- **Statement**: The framing under-engages with *DIY-via-Bogleheads-
  Reddit-flowchart* as a legitimate alternative for askers with
  moderate complexity and high financial literacy — the "always
  consult a professional" reflex can be paternalistic and crowds
  out the asker who is genuinely better-served by self-study +
  occasional hourly-fee consult than by ongoing AUM-fee
  relationship.
- **Source evidence**: `framings.md` §10 Excludes line on DIY-
  Bogleheads-flowchart under-engaged; Bogleheads voice canonical
  on self-directed retirement planning; chronic-DIY-Reddit voice
  (r/personalfinance, r/Bogleheads, r/financialindependence) on
  the DIY-with-occasional-consult model; opposes F11 (behavioral-
  finance) which leans toward "outsource discipline."
- **Trigger**: Asker is high-financial-literacy AND has stable
  income AND has moderate complexity (W-2 + standard retirement
  accounts + maybe taxable + maybe mortgage; no equity-comp / no
  estate-tax exposure / no business-ownership) AND is being
  pushed toward ongoing AUM-fee CFP relationship despite the
  asker's stated DIY preference.
- **Failure mode**: Asker (high-literacy software engineer, $800k
  net worth, no equity-comp, no business-ownership, no inherited-
  estate-complications) signs up for ongoing 1% AUM CFP at $8k/year;
  pays the AUM fee for 20 years at growing balance; total cost
  $200k-$400k; the same asker could have used Bogleheads-flowchart
  + Garrett-Planning hourly-fee for $500-$2k once every 2-3 years
  at $5k-$15k total cost over the same period. The "always
  consult" reflex over-charged this asker by 90%+.
- **Recovery move**: For high-literacy / moderate-complexity askers,
  *self-classify*: are you genuinely DIY-capable on (a) Form 8606
  / Roth-IRA-ordering / asset-location, (b) rebalance-discipline,
  (c) tax-bracket-fill arithmetic, (d) emergency-fund discipline?
  If yes-to-all, use Bogleheads-flowchart-DIY + Garrett-Planning-
  Network hourly-fee for once-per-2-3-year second-opinion;
  reserve full-AUM-relationship for genuinely-complex situations.
  Verify hourly-fee CFP via SEC IAPD before engagement.

### 10.4 Access-inequality is real for rural / immigrant / marginalized

- **Statement**: The framing's professional-referral discipline
  assumes *trustworthy-professional-availability* — but rural areas,
  immigrant communities (language barriers), and historically-
  marginalized communities face genuine access barriers to
  fiduciary-fee-only advisors. The XY-Planning-Network and Garrett-
  Planning-Network address this somewhat by virtual-practice
  models, but the framing rarely surfaces access-inequality as a
  real constraint on the "just consult a fee-only CFP"
  recommendation.
- **Source evidence**: `framings.md` §10 Excludes line on access-
  inequality barriers; financial-economics-journalism voice
  (David Wessel at Brookings on retirement-savings-system inequality
  reporting); XY-Planning-Network mission-statement on the access-
  gap for under-served communities.
- **Trigger**: Asker is in rural area / immigrant community /
  historically-marginalized community AND is being advised to
  "consult a fee-only CFP" without engaging with the local
  availability AND has not separately considered virtual-practice
  alternatives.
- **Failure mode**: Asker (rural Wyoming resident with $400k IRA)
  receives "consult a fee-only fiduciary CFP" advice; local
  options are commission-based brokers only (no NAPFA / XY /
  Garrett members within 200 miles); asker defaults to the local
  commission-broker; receives commission-driven advice; ends up
  in higher-cost variable-annuity product. The "just consult a
  fee-only CFP" recommendation was infeasible-in-place.
- **Recovery move**: For access-constrained askers, route to
  *virtual-practice* fee-only fiduciary CFPs via XY-Planning-
  Network (xyplanningnetwork.com), Garrett-Planning-Network
  (garrettplanningnetwork.com), and NAPFA virtual-practice
  members; verify each via SEC IAPD Form ADV Part 2A AND FINRA
  BrokerCheck; for language-barrier asker, verify the practice
  offers the asker's language at the depth-of-financial-detail
  required (not just basic-translation). The remote-practice
  model meaningfully expands access; the framing should surface
  this as the default for access-constrained askers.

### 10.5 SEC IAPD vs FINRA BrokerCheck different scope — verify both

- **Statement**: SEC IAPD (adviserinfo.sec.gov) and FINRA
  BrokerCheck (brokercheck.finra.org) cover *different scopes* of
  the professional-advice market: SEC IAPD covers Investment
  Advisers (IA / IAR — fiduciary standard, Form ADV-based) and
  state-registered advisers; FINRA BrokerCheck covers Registered
  Representatives (RR / Series 7 / Series 63 — suitability
  standard, broker-dealer-based). The framing's reflex to "verify
  the advisor" rarely names that *both* should be checked for any
  dual-registered or hybrid advisor; many advisors hold both
  registrations.
- **Source evidence**: `framings.md` §10 Mental model line on SEC
  IAPD / FINRA BrokerCheck verification; SEC-EDGAR / FINRA-
  BrokerCheck voice on the per-registration-scope distinction;
  fee-only-fiduciary-CFP voice on the dual-registration
  disclosure-event surfacing pattern.
- **Trigger**: Asker is verifying a professional advisor AND has
  checked one of SEC IAPD or FINRA BrokerCheck but not both AND
  has not separately verified whether the advisor is dual-
  registered.
- **Failure mode**: Asker checks FINRA BrokerCheck for a "financial
  advisor" recommendation; no disclosure events flagged; engages
  the advisor; the advisor was actually dual-registered with
  significant Form ADV Part 2A conflicts (12b-1 fee revenue,
  cross-product-sales arrangements, prior IA-disciplinary-event)
  that show on SEC IAPD but not FINRA BrokerCheck. The verification
  was incomplete; the conflicts were missed.
- **Recovery move**: For *every* professional advisor under
  consideration, verify BOTH SEC IAPD (adviserinfo.sec.gov) AND
  FINRA BrokerCheck (brokercheck.finra.org); for state-registered
  advisers (below $100M AUM), also check the state-regulator's
  IAPD-equivalent (most states use the SEC IAPD interface);
  request and read Form ADV Part 2A (the advisor's brochure)
  before engagement, paying particular attention to disclosure
  events, fee structure, and conflicts-of-interest sections.
  Document the verification date and findings; re-verify every
  2-3 years during ongoing engagement.

## 11. Behavioral-and-automation framing

### 11.1 Robo-TLH-wash-sale visibility gap creates Form 1099-B-W surprises

- **Statement**: Automation works *until it breaks* — a robo-advisor
  auto-TLH that doesn't have visibility into the asker's held-away
  accounts (spouse's IRA, employer 401(k)) creates wash-sale
  violations the asker doesn't see until tax-time Form 1099-B-W-
  code surfaces them. Per IRS Rev Rul 2008-5, a wash-sale across a
  taxable-and-IRA boundary defers the loss permanently into the
  IRA basis (functionally lost). The framing's "set-and-forget"
  elides the auto-system-failure modes.
- **Source evidence**: `framings.md` §11 Excludes line on robo-TLH
  wash-sale visibility gap; IRS-publication-authority voice
  (Pub 550 wash-sale rules; Rev Rul 2008-5 on IRA wash-sale
  permanence); The Finance Buff voice on robo-TLH-vs-DIY-TLH
  wash-sale-control trade-off.
- **Trigger**: Asker uses robo-advisor with auto-TLH (Wealthfront,
  Betterment, Schwab Intelligent Portfolios, M1 Smart Transfers)
  AND has held-away accounts (spouse IRA / spouse 401(k) /
  separate-employer-401(k)) holding overlapping funds AND has not
  separately verified no wash-sale exposure across accounts.
- **Failure mode**: Asker uses Wealthfront auto-TLH at taxable
  account; spouse holds same total-stock-index in their IRA at a
  different custodian; Wealthfront sells VTI at loss, buys
  ITOT-equivalent (avoiding direct wash-sale in the taxable
  account); spouse's IRA buys VTI within 30-day-window in
  unrelated rebalance; per Rev Rul 2008-5 the wash-sale crosses
  the spouse-IRA boundary; loss is permanently disallowed and
  basis-shifted to the IRA (where it can't ever offset gains since
  IRA gains are ordinary-income-on-distribution); $5-10k of "tax-
  loss-harvest" was structurally illusory.
- **Recovery move**: For robo-TLH users, *manually inventory* all
  household accounts (spouse, joint, IRA, Roth-IRA, 401(k), HSA,
  taxable-brokerage) and verify no overlapping-fund-purchases
  within 30 days of robo-TLH sales; either (a) eliminate
  overlapping holdings across accounts, (b) disable auto-TLH on
  the robo and execute TLH manually with cross-account visibility,
  or (c) accept the wash-sale leakage as cost of automation;
  consult a retirement-and-equity-comp-experienced CPA via SEC
  IAPD on Form 8949 wash-sale-code-W reconciliation across
  accounts.

### 11.2 Auto-escalate 401(k) cap-hit mid-year cuts off match

- **Statement**: An auto-escalate 401(k) that hits the elective-
  deferral cap mid-year stops contributing (and stops capturing
  match) for the rest of the year if employer doesn't true-up.
  The framing's "automate the escalation" reflex misses the cap-
  hit-match-cut-off failure mode that affects high-earners who
  back-load contributions early in the year.
- **Source evidence**: `framings.md` §11 Excludes line on auto-
  escalate cap-hit cutting off match; Bogleheads voice on the
  employer-true-up-vs-no-true-up plan-document variation; The
  Finance Buff voice on the front-load vs even-spread contribution
  pacing analysis.
- **Trigger**: Asker is high-earner (likely to hit $23,500 cap)
  AND uses auto-escalate 401(k) AND front-loads contributions
  early in the year AND employer does NOT have true-up provision
  for missed match on capped-employee.
- **Failure mode**: Asker (high-earner $250k) sets 401(k) at 25%
  of pay; hits $23,500 cap in August; for Sep-Dec the asker
  contributes $0; if employer match is per-pay-period (typical),
  no match is generated for Sep-Dec; asker forgoes 4 months of
  match (~$4k-$8k depending on match formula); employer plan
  document does not have a "true-up" provision restoring the
  missed match.
- **Recovery move**: Read the 401(k) plan-document (Summary Plan
  Description) for *true-up* provision; if no true-up, pace
  contributions to spread evenly across the year (NOT front-
  loaded); for asker hitting the cap mid-year, request employer
  HR adjust the contribution percentage mid-year to even-spread
  the remaining contributions; consult a retirement-experienced
  CPA via SEC IAPD on the contribution-pacing-vs-match-capture
  arithmetic if the plan-document is complex.

### 11.3 Auto-enrollment-default-fund expensive-fund trap

- **Statement**: The "automate everything" reflex can mask *fee
  leakage* — automatic-enrollment-default-fund is often the
  employer's target-date-fund with 0.5-1.0% expense ratio when a
  3-fund-portfolio with 0.05% expense ratio is available; the
  auto-enrolled asker stays in the expensive default for years.
  The framing's automation discipline is the right starting point;
  periodic-audit-and-rebalance-toward-low-cost is the necessary
  complement.
- **Source evidence**: `framings.md` §11 Excludes line on
  automation masking fee leakage; Bogleheads voice on the auto-
  enroll-default-fund-vs-3-fund-portfolio trade-off; financial-
  economics-journalism voice (Anne Tergesen at WSJ on default-fund
  fee-leakage reporting).
- **Trigger**: Asker was auto-enrolled in employer 401(k) AND has
  not separately reviewed the default-fund selection AND the plan
  offers lower-cost index alternatives AND the asker is in the
  expensive default.
- **Failure mode**: Asker (auto-enrolled at employer start in
  2020) remains in the default Target-Date-Fund with 0.65%
  expense ratio for 5 years; plan offers Vanguard Institutional
  Index at 0.03% expense; the 0.62% expense delta on a $50k-and-
  growing balance compounds to $5k-$15k of fee leakage over 5
  years; over 30-year career, the leakage projects to $200k-
  $500k of foregone terminal balance.
- **Recovery move**: For auto-enrolled 401(k) participants,
  *audit the default fund* within first 3 months of enrollment;
  pull the plan's full-fund-menu with expense-ratio comparison;
  switch to the lowest-cost index alternative (3-fund-portfolio
  if available); set a calendar reminder for annual fund-menu-
  review (employers occasionally add lower-cost share-classes);
  consult a fee-only fiduciary CFP (Garrett-Planning hourly-fee
  for once-only) for the rebalance-allocation. Verify CFP via SEC
  IAPD before engagement.

### 11.4 Automation discipline anti-correlated with tactical optionality

- **Statement**: Automation discipline is *anti-correlated with
  optionality* — the asker who automates everything also forfeits
  the ability to capture tactical opportunities (Roth-conversion
  in a layoff year, tax-loss-harvest in a market-drawdown,
  529-funding bump in a windfall year). The framing's "remove the
  friction" reflex can over-apply to decisions that benefit from
  human attention.
- **Source evidence**: `framings.md` §11 Excludes line on
  automation anti-correlated with optionality; opposes F2 / F7
  where tactical timing matters; The Finance Buff voice on the
  manual-tactical-Roth-conversion-window-capture practice.
- **Trigger**: Asker has fully-automated savings / rebalancing /
  TLH AND experiences a tactical event (layoff, sabbatical,
  windfall, market-drawdown) AND has not separately considered
  manual-tactical-execution opportunities AND is reasoning about
  the event from automation-default mindset.
- **Failure mode**: Asker (age 38) is laid off in 2024 with
  6-month severance; asker's income for 2024 is $50k (vs typical
  $200k); asker continues auto-pilot 401(k)-and-Roth-IRA
  contributions on the new much-lower income; misses the
  opportunity to execute a $60-80k Roth-conversion at the low-
  income year's 12-22% bracket vs the typical 32% bracket. The
  $60k Roth conversion at 22% saves $6k in lifetime tax vs the
  same conversion executed in a typical year — a one-time
  $6k optimization that automation didn't surface.
- **Recovery move**: For tactical-event years (layoff, sabbatical,
  windfall, market-drawdown), *temporarily disable automation*
  and execute tactical moves manually with retirement-experienced
  CPA review; for layoff years specifically, consider Roth-
  conversion-ladder timing AND COBRA-vs-marketplace decision AND
  unemployment-tax-treatment AND Form W-4 adjustment for new
  income level. Consult a fee-only fiduciary CFP (NAPFA / XY-
  Planning) AND a retirement-experienced CPA on the tactical-
  window opportunities. Verify both via SEC IAPD before
  engagement.

### 11.5 Plan-document features limit available automation

- **Statement**: The behavioral-finance framing assumes the asker
  has *agency over the relevant defaults* — but many askers work
  for employers whose 401(k) plan-document doesn't offer auto-
  escalation, doesn't allow after-tax contributions (Mega-Backdoor-
  Roth requires after-tax + in-plan-conversion), doesn't permit
  Roth-401(k), or doesn't enable in-plan-Roth-conversion. The
  framing's "use the automation" recommendation depends on plan-
  features the asker may not control.
- **Source evidence**: `framings.md` §11 Excludes line on plan-
  features the asker may not control; cross-domain edge into
  `tech-career` on employer-plan-document analysis per
  `decisions.md` §D1. ERISA-practitioner voice on plan-document
  feature-variation; The Finance Buff voice on Mega-Backdoor-
  Roth-plan-document-feature-required analysis.
- **Trigger**: Asker is in a small / mid-size employer (or some
  large employers with conservative plan-documents) AND is being
  advised to execute Mega-Backdoor Roth / Roth-401(k)-conversion
  / in-plan-Roth-conversion AND has not separately verified the
  employer's plan-document supports the maneuver.
- **Failure mode**: Asker (mid-size-employer, software engineer)
  reads Bogleheads / The Finance Buff Mega-Backdoor-Roth-canonical
  guide; assumes employer 401(k) supports after-tax + in-plan-
  conversion; attempts to make after-tax contributions; plan-
  document doesn't allow after-tax contributions (only pre-tax
  + Roth-401(k) up to elective-deferral cap); asker has wasted
  weeks on a maneuver the plan-document forecloses; misses the
  alternative (taxable-brokerage savings to fund Roth-IRA
  separately) for the year.
- **Recovery move**: Before attempting any plan-feature-dependent
  retirement maneuver, *pull the plan-document* (Summary Plan
  Description, available from HR or plan-administrator) and
  verify the specific feature (after-tax contributions allowed?
  in-plan-Roth-conversion allowed? Roth-401(k) option? Rule-of-
  55 separation-from-service provisions? loan provisions?);
  consult an ERISA attorney via state-bar member-search for
  high-balance / complex plan-document questions; if the desired
  feature isn't available, request plan-document amendment via HR
  AND identify alternative-maneuver paths in the interim.

## 12. Policy-volatility / system-skepticism framing

### 12.1 Over-hedging toward Roth costs real current-year deduction

- **Statement**: The framing's policy-volatility argument can
  produce *over-hedging* that costs real money — the asker who
  refuses traditional-401(k) contributions because "rates might go
  up" loses the certain current-year deduction at high marginal
  rates, and the projected rate-rise may not materialize. The
  framing's asymmetry-toward-Roth reflex needs hardness about
  actual current marginal vs projected rates.
- **Source evidence**: `framings.md` §12 Excludes line on over-
  hedging toward Roth; opposes F2 (marginal-rate arbitrage) when
  over-applied. Retirement-econ academic voice (Michael Kitces on
  tax-diversification-vs-rate-hedging analysis); financial-
  economics-journalism voice on the Roth-vs-traditional debate.
- **Trigger**: Asker is in a high current marginal bracket (32%+)
  AND is being advised to prefer Roth over traditional purely on
  policy-volatility grounds AND has not separately verified the
  projected retirement marginal would justify the deduction-
  foregone.
- **Failure mode**: Asker (high-earner $300k, 32% federal marginal)
  follows "always Roth for rate-rise hedge" advice; contributes
  $23,500 to Roth-401(k) instead of traditional; gives up $7,520
  of current-year federal tax deduction (plus $2,184 of state-tax
  at 9.3% CA = $9,704 combined deduction-foregone); even if
  retirement marginal turns out to be 28% (post-TCJA-sunset, MFJ
  retirement income), the foregone $9,704 deduction at 32% > the
  projected $6,580 tax savings at 28% on the same $23,500. The
  pure rate-arithmetic favored traditional.
- **Recovery move**: For Roth-vs-traditional decisions, compute
  the *expected* break-even rate (current marginal vs projected
  retirement marginal as a distribution) before applying policy-
  hedging premium; the policy-hedge premium should be small
  (5-10 percentage points of conviction), not dominate the
  arithmetic; consult a retirement-and-equity-comp-experienced
  CPA via SEC IAPD on bracket-fill arithmetic AND a fee-only
  fiduciary CFP (NAPFA / XY-Planning) on the tax-diversification
  question. Verify both via SEC IAPD before engagement.

### 12.2 Front-running cliffs that don't materialize on schedule

- **Statement**: Predictions about *which* policy changes will pass
  are systematically poor — many predicted changes (estate-tax-
  exemption-reversion, SS-benefit cuts, Medicare-IRMAA-tier
  widening) have been delayed multiple times by legislative
  inaction, and the framing's "act before the cliff" urgency
  repeatedly front-runs cliffs that don't materialize on schedule.
- **Source evidence**: `framings.md` §12 Excludes line on cliffs
  not materializing on schedule; cross-domain edge into `legal-
  disputes` per `decisions.md` §D10. Financial-economics-
  journalism voice (David Wessel at Brookings on legislative-
  delay-and-extension pattern reporting); fee-only-fiduciary-CFP
  voice on the front-running-cliff risk.
- **Trigger**: Asker is being advised to execute aggressive
  pre-cliff moves (SLAT before 2026, claim-SS-early before
  benefit cuts, accelerate Roth-conversions before bracket-sunset)
  AND has not separately modeled the legislative-extension
  scenario AND is treating the cliff as date-certain.
- **Failure mode**: Asker (age 62, healthy, married, $1.5M
  portfolio) claims Social Security at 62 to "lock in benefits
  before SS-trust-fund-exhaustion-2034 cuts"; permanently reduces
  PIA by ~30%; loses ~$300k of lifetime benefits if asker lives to
  85; SS-trust-fund-exhaustion in 2034 either gets legislatively
  patched (most likely outcome historically) OR results in 21%
  across-the-board cut that affects the asker just as much in
  either case. The "act before cliff" reflex created permanent
  damage to hedge against an uncertain cliff.
- **Recovery move**: For policy-cliff-driven planning, distinguish
  *certain costs of front-running* (claim-age-permanent-reduction,
  irrevocable Roth conversion, gifted exemption-room-spent) from
  *uncertain benefits of front-running* (cliff materializes on
  schedule with full impact); the asymmetry usually favors patient
  waiting; consult a fee-only Social-Security-claiming specialist
  (Mike Piper's Open Social Security software for free, conflict-
  free analysis) on claim-age AND a state-bar-licensed estate
  attorney on exemption-sunset planning AND a retirement-and-
  equity-comp-experienced CPA on Roth-conversion-sizing. Verify
  all via SEC IAPD before engagement.

### 12.3 Federal-focused framing under-engages with state-policy volatility

- **Statement**: The framing engages with *federal-policy
  volatility* but rarely with *state-policy volatility* — state
  income-tax rates, state-shield laws for retirement accounts, and
  state-529 mechanics shift independently of federal cycles, and
  the federal-focused framing under-engages with state-specific
  changes that may matter more to the asker's actual situation.
- **Source evidence**: `framings.md` §12 Excludes line on state-
  policy volatility under-engaged; state-bar-estate-attorney voice
  on the state-specific-statute date-stamp practice; financial-
  economics-journalism voice on state-tax-policy reporting.
- **Trigger**: Asker is planning a state-of-residence change (move
  to FL / TX / WA / NV from CA / NY / NJ for retirement income-tax
  savings) AND has anchored the analysis on federal tax policy
  only AND has not separately verified state-specific changes
  (state-shield-law, state-529-tax-treatment, state-estate-tax,
  state-retirement-income-exemption).
- **Failure mode**: Asker (age 65, NJ resident, $2M portfolio)
  plans to move to FL for retirement to escape NJ 10.75% state
  income tax; executes the move; subsequently discovers (a) NJ
  has a state-estate-tax with a $0 exemption that may apply to
  pre-move gifts via reach-back rules, (b) FL homestead-exemption
  has acquisition-time-requirements asker hasn't met, (c) the
  state-shield-law for the asker's IRA differs between NJ ($1M
  cap) and FL (unlimited), creating a window where the rollover-
  timing matters. Planning gaps the federal-focused analysis
  missed.
- **Recovery move**: For any state-of-residence change planning,
  add a state-specific layer to the analysis: state income tax
  rate AND exemptions (retirement-income / SS / pension), state
  estate / inheritance tax (rare but exists in 17 states),
  state-shield law for retirement accounts (per §8.2), state
  529 deduction treatment AND deduction-recapture-on-out-of-state-
  use, state homestead exemption acquisition rules; consult a
  state-bar-licensed estate attorney in both states (origin and
  destination) AND a retirement-experienced CPA for the multi-
  state tax analysis. Verify both via state-bar member-search AND
  SEC IAPD before engagement.

### 12.4 Individual policy-hedging can accelerate the trajectory toward cuts

- **Statement**: The framing's hedge-against-policy reflexes
  (diversify-into-Roth, gift-before-sunset, claim-SS-early-before-
  cuts) can themselves *create* the behavior the policy was
  designed to prevent — early-SS-claiming because of trust-fund-
  anxiety is structurally identical to a bank run. The framing
  rarely engages with the meta-irony that individual hedging
  against benefit cuts can accelerate the fiscal trajectory toward
  cuts.
- **Source evidence**: `framings.md` §12 Excludes line on
  individual hedging accelerating cuts; fee-only Social-Security-
  claiming-specialist voice (Mike Piper on the SS-claim-anxiety-
  pattern); retirement-econ academic voice (Larry Kotlikoff on
  the SS-trust-fund-actuarial-reality vs claim-anxiety-perception).
- **Trigger**: Asker is contemplating an early-action move
  motivated primarily by policy-cliff anxiety (early SS-claim,
  early-RMD, accelerated gifting) AND is treating the personal-
  decision as separable from the system-level dynamic AND has
  not separately considered whether the anxiety-trigger is
  load-bearing for the personal decision.
- **Failure mode**: Asker (age 63, well-resourced, married, no
  immediate cash need) claims Social Security at 63 motivated by
  trust-fund-exhaustion-anxiety; permanently reduces PIA ~25%;
  the trust-fund is patched legislatively (or asker would receive
  the 79% reduced benefit anyway in the no-patch scenario);
  asker now permanently receives 75% × 79% = 59% of the FRA
  benefit in the no-patch scenario, vs 100% × 79% = 79% if asker
  had claimed at FRA. The policy-anxiety claim was self-harming
  in both legislative outcomes.
- **Recovery move**: For policy-anxiety-driven moves, distinguish
  between *individual-rational-given-information* and *anxiety-
  driven-collectively-irrational*; cross-check the personal
  decision against the dispassionate analysis (Mike Piper's Open
  Social Security software is free, conflict-free, and computes
  expected-lifetime-benefit under both patch and no-patch
  scenarios); for SS-claim-age specifically, the math usually
  favors waiting to FRA or age 70 even under partial-benefit-cut
  scenarios; consult a fee-only Social-Security-claiming
  specialist for asker-specific analysis. Verify specialist via
  SEC IAPD before engagement.

### 12.5 SECURE 2.0 phased provisions create rolling-cycle complexity

- **Statement**: SECURE Act 2.0 (Dec 2022) phased many provisions
  across 2024-2026 (Roth-catch-up mandatory for high-earners in
  2026 per §603; emergency-savings-Roth-401(k) optional starting
  2024; 529-to-Roth-IRA rollover starting 2024 per §126;
  in-plan-Roth-conversion expanded). The framing's "look up
  current rules" is correct only if the asker tracks the rolling
  effective-date schedule; an asker reading 2022-vintage advice
  in 2026 will mis-apply rules that have phased in.
- **Source evidence**: `framings.md` §12 Excludes line on tax-code
  political dynamism + SECURE 2.0 phased provisions reference;
  retirement-experienced-CPA voice on the rolling-effective-date
  practice; IRS-publication-authority voice (Pub 590-A, 590-B,
  969 cycle-specific updates); The Finance Buff voice on SECURE
  2.0 phased-provision tracking.
- **Trigger**: Asker is contemplating a maneuver that touches a
  SECURE 2.0 phased provision (529-to-Roth rollover, Roth-catch-
  up, emergency-savings-Roth-401(k), in-plan-Roth-conversion-
  expanded) AND is using guidance that predates the specific
  phased effective date AND has not separately verified the
  current effective-date status.
- **Failure mode**: Asker (age 55, $50k 529 with overfunded balance
  for now-college-graduated-child) reads 2023 article promising
  "529-to-Roth rollover starting 2024"; in 2024 attempts $35k
  rollover; discovers (a) the 529 must have been open for 15
  years for SECURE 2.0 §126 eligibility, (b) the rollover is
  capped at $7,000/year (Roth-IRA cap), (c) the receiving Roth-IRA
  must belong to the 529 beneficiary not the parent, (d) the
  beneficiary must have earned-income covering the rollover
  amount. The 2023 article's enthusiastic framing of the
  maneuver missed the eligibility constraints; asker's $35k-in-
  one-year plan was structurally infeasible.
- **Recovery move**: For any SECURE 2.0 phased-provision maneuver,
  verify the *current-year-specific* eligibility constraints
  against the IRS publications AND the final IRS regulations
  (where issued); cross-check via The Finance Buff annual-update
  posts (thefinancebuff.com); consult a retirement-experienced
  CPA via SEC IAPD on the specific maneuver before execution. The
  529-to-Roth-rollover specifically has 4-5 binding constraints
  that the headlines obscure.

## 13. FIRE / extreme-saver framing

### 13.1 4% SWR fails at 50-year FIRE horizons per Pfau / Big-ERN

- **Statement**: The FIRE framing's 4% safe-withdrawal-rate is
  calibrated to *historical US 30-year retirement* — for FIRE
  retirees facing 50+ year retirement (retire at 35, live to 85),
  the safe-withdrawal-rate drops materially (Wade Pfau's research
  suggests 3-3.5% for 50-year horizons; Big-ERN's *Early Retirement
  Now* SWR series suggests 3.25% as the prudent rate). The
  framing's 4%-anchored rhetoric can dramatically overstate
  sustainability for early-retirees specifically.
- **Source evidence**: `framings.md` §13 Excludes line on 4% SWR
  calibration-to-30-year-US history; opposes F7 (lifecycle /
  retirement-econ academic voice) on the sustainable-withdrawal
  calculation. Retirement-econ academic voice (Pfau on 50-year-
  horizon SWR research; Big-ERN's earlyretirementnow.com SWR
  series); FIRE community voice recognition of the issue
  (ChooseFI episodes covering Big-ERN's analysis).
- **Trigger**: Asker is FIRE-candidate (savings rate 30%+, target
  retirement age before 50) AND is using 4% SWR as the planning
  anchor AND has not separately modeled the 50-year-horizon
  failure-rate implications.
- **Failure mode**: Asker (age 35, $1M FIRE target = $40k/year
  spend at 4%) retires; faces 50-year horizon; 4% SWR has 25-30%
  failure rate at 50-year horizon per Pfau / Big-ERN historical
  back-test; portfolio depletion by year 35-40 in adverse
  sequences; asker re-enters labor market at age 70 after
  decades-out-of-workforce. The 4%-anchored confidence was
  catastrophically over-stated.
- **Recovery move**: For FIRE planning with 40+ year horizon, use
  3-3.5% SWR not 4% per Pfau / Big-ERN extended-data research;
  build a variable-spending plan (Guyton-Klinger guardrails,
  Kitces variable-SWR, Big-ERN's CAPE-based rule) that adjusts
  spend down in bad-sequence years; build a barbell of
  conservative-bridge (5-7 years cash + Treasury + I-Bonds) +
  equity-rest to mitigate sequence-of-returns risk; consult a
  fee-only fiduciary CFP (NAPFA / XY-Planning) with FIRE specialty
  via Garrett-Planning-Network for the second-opinion; cross-
  check via Big-ERN's SWR series (free, conflict-free). Verify
  CFP via SEC IAPD before engagement.

### 13.2 Roth-conversion-ladder requires 5-year bridge funding

- **Statement**: The Roth-conversion-ladder requires *5-year-gap of
  funding before the first conversion becomes accessible* — early-
  retirees must pre-fund this 5-year gap from taxable-brokerage
  or Roth-IRA-principal-contributions (which are always penalty-
  free withdrawable as basis per Pub 590-B ordering rules). The
  framing's enthusiasm for the ladder can elide the bridge-funding
  requirement, leaving askers stranded in years 1-5 of retirement
  without accessible cash.
- **Source evidence**: `framings.md` §13 Excludes line on Roth-
  conversion-ladder 5-year-bridge requirement; The Finance Buff
  voice on the ladder mechanics; Mr-Money-Mustache canonical post
  on Roth-conversion-ladder (mrmoneymustache.com "Roth IRA
  Conversion Ladder"); IRS-publication-authority voice (Pub 590-B
  conversion-clock per-conversion).
- **Trigger**: Asker is FIRE-candidate AND is planning to retire
  before 59.5 AND is relying on Roth-conversion-ladder as the
  primary early-retirement-access mechanism AND has not separately
  pre-funded a 5-year-bridge of accessible-cash.
- **Failure mode**: Asker (age 45, retires with $1.2M traditional-
  401(k), $0 taxable, $0 Roth-IRA-contribution-basis) plans to
  execute Roth-conversion-ladder; rolls 401(k) to IRA; converts
  $40k in year 1; the converted $40k is not accessible penalty-
  free until year 6 per the 5-year-conversion-clock; asker has
  $0 of accessible cash for living expenses in years 1-5; only
  options are (a) early-withdrawal-with-10%-penalty on the
  traditional-IRA, (b) SEPP 72(t) substantially-equal-periodic-
  payments lock-in, (c) return-to-work. The retirement was
  premature without the bridge.
- **Recovery move**: For Roth-conversion-ladder-planned early
  retirement, build a *5-year-bridge fund* before retiring:
  taxable-brokerage savings + accumulated Roth-IRA-contribution-
  basis (always penalty-free per Pub 590-B ordering) + I-Bonds /
  Treasury ladders; size the bridge to 5+ years of living
  expenses; consult a retirement-and-equity-comp-experienced CPA
  via SEC IAPD on the Roth-IRA-ordering-rule mechanics AND a fee-
  only fiduciary CFP (Garrett-Planning-Network hourly-fee) on the
  bridge-sizing AND the SEPP 72(t) alternative if bridge is
  insufficient. Verify both via SEC IAPD before engagement.

### 13.3 ACA-subsidy-management conflicts with Roth-conversion-ladder

- **Statement**: FIRE's *health-insurance-pre-65* problem is a
  binding constraint the savings-rate-focus framing under-engages
  — ACA-marketplace-subsidy-management requires MAGI discipline
  that conflicts with Roth-conversion-ladder execution (large
  Roth conversions push MAGI past subsidy-cliff and destroy APTC
  eligibility); Barista FIRE solves this via part-time-employer-
  coverage but the framing rarely names the trade-off.
- **Source evidence**: `framings.md` §13 Excludes line on ACA-
  subsidy-management conflicting with Roth-conversion-ladder;
  cross-domain edge into `health-insurance` D5, D7 per `decisions.
  md` §D7. ACA-Navigator voice on subsidy-cliff arithmetic; FIRE
  community voice on Barista FIRE as the part-time-coverage
  solution; retirement-experienced-CPA voice on MAGI-management.
- **Trigger**: Asker is FIRE-candidate in early retirement AND is
  using ACA-marketplace for health-insurance AND is contemplating
  Roth conversions AND has not separately modeled the conversion's
  effect on MAGI and APTC subsidy eligibility.
- **Failure mode**: Asker (age 48, FIRE-retired in 2024) qualifies
  for $18k/year of APTC subsidies on ACA marketplace; executes
  $60k Roth conversion in 2024; the conversion pushes MAGI from
  $40k to $100k, past the prior 400%-FPL subsidy-cliff (ARPA / IRA
  enhanced subsidies sunset end of 2025 absent extension); asker
  loses $18k of APTC subsidies and owes the full premium of
  ~$24k/year; net cost of the conversion is $60k × ~22% = $13.2k
  ordinary-income tax PLUS $18k of foregone subsidies = $31k of
  effective conversion cost on a $60k principal — over 50%
  effective marginal rate.
- **Recovery move**: For FIRE retirees on ACA marketplace, build a
  multi-year MAGI plan that *coordinates* Roth conversions with
  subsidy thresholds; size conversions to stay below the relevant
  cliff (400%-FPL pre-2026 if enhanced subsidies sunset; current
  cliffs phase-out gradually under ARPA / IRA enhanced subsidies);
  consider Barista FIRE (part-time-employer-coverage at $15-20k
  / year of work for ACA-coverage exit) as the alternative; consult
  an ACA-Marketplace Navigator (CMS-trained, prohibited from
  steering — free) AND a retirement-and-equity-comp-experienced
  CPA on the integrated MAGI-and-conversion-sizing arithmetic.
  Verify CPA via SEC IAPD before engagement.

### 13.4 FIRE frugality dogma encodes middle-class-American assumptions

- **Statement**: The FIRE community's *frugality dogma* can encode
  middle-class-American assumptions (geographic mobility, car-
  optional living, partner-supportive-of-extreme-savings, no-
  eldercare-obligation, no-dependent-with-special-needs) that
  don't generalize to many askers' actual life constraints. The
  framing's "anyone can do this" rhetoric understates the
  structural factors that make extreme savings genuinely
  impossible for many households.
- **Source evidence**: `framings.md` §13 Excludes line on FIRE
  frugality dogma encoding middle-class-American assumptions;
  cross-domain edge into `family-planning` per `decisions.md`
  §D1. Financial-economics-journalism voice (Anne Tergesen at
  WSJ on FIRE-feasibility-by-demographic reporting); chronic-DIY-
  Reddit voice (r/financialindependence, r/leanFIRE) on the
  structural-feasibility tensions.
- **Trigger**: Asker is being pushed toward FIRE by online community
  / podcast / mass-media AND has any of: eldercare obligation,
  special-needs dependent, partner with conflicting financial
  values, geographic constraint (job-locked to expensive area),
  limited-income-trajectory AND is treating FIRE as universally
  feasible.
- **Failure mode**: Asker (single-parent of special-needs child,
  job-locked to expensive area for medical access) attempts FIRE
  savings rate 40%; cuts essential expenses (therapy, respite-
  care, geographic-stability) to hit the savings target; quality-
  of-care for dependent declines; asker burns out and abandons
  the plan after 3 years; net result is no FIRE progress AND
  damaged dependent-care situation AND 3 years of compounded
  stress. The framing's "anyone can do this" rhetoric was
  structurally inapplicable.
- **Recovery move**: For FIRE-considering askers, *self-assess* the
  structural assumptions explicitly: geographic mobility (or job-
  locked?), partner alignment, eldercare horizon (next 10 years),
  dependent-care obligations (current and projected), income-
  trajectory; for askers where structural constraints bind, prefer
  *moderate-FI* targets (15-25 years to traditional retirement age
  with normal expenses) over extreme-FIRE; consult a fee-only
  fiduciary CFP (NAPFA / XY-Planning) with family-and-caregiving
  specialty for the goal-realism analysis. Verify CFP via SEC
  IAPD before engagement.

### 13.5 LCOL geographic-arbitrage interacts with state-shield / state-tax

- **Statement**: FIRE's geographic-arbitrage signature move (HCOL-
  earn / LCOL-retire) interacts with state-tax and state-shield
  in ways the savings-rate-focus framing under-engages — the
  move from CA (state-IRA-shield is "necessary for support" only
  in bankruptcy) to TX (unlimited IRA shield AND no state income
  tax) materially shifts the asker's creditor-protection and
  tax-burden footprint. The framing names the savings-rate
  optimization but rarely engages with the state-specific
  state-shield / state-tax-on-retirement-income arithmetic.
- **Source evidence**: `framings.md` §13 Mental model line on
  geographic-arbitrage; §8.2 cross-reference on state-shield-law
  variation; cross-domain edge into `legal-disputes` /
  `family-planning` per `decisions.md` §D10. State-bar-estate-
  attorney voice on state-shield mapping; FIRE community voice
  on geographic-arbitrage tax arithmetic.
- **Trigger**: Asker is FIRE-candidate AND is planning geographic-
  arbitrage (move to LCOL state for retirement) AND has not
  separately verified state-specific (a) IRA shield law, (b)
  retirement-income exemption, (c) state-estate-tax, (d) state-
  health-insurance options pre-65.
- **Failure mode**: Asker (CA resident, $1.2M FIRE-portfolio,
  age 45) moves to TX for retirement; assumes uniform federal-
  tax-and-shield treatment; subsequently discovers (a) TX has
  weaker ACA-marketplace network depth in some regions for asker's
  pre-65 health-insurance needs, (b) CA's "necessary for support"
  shield meant the asker's IRA was at risk during the move
  transition for any pending judgment, (c) TX homestead-exemption
  has acquisition-time-requirements asker hasn't met. Planning
  gaps the federal-focused FIRE framing missed.
- **Recovery move**: For FIRE geographic-arbitrage, add a state-
  specific layer to the analysis: state income tax on retirement
  income (CA taxes all retirement income; PA exempts most;
  TX/FL/NV/WA/NH no state income tax; etc.), state-IRA-shield
  law per §8.2, state estate / inheritance tax (rare but exists
  in 17 states), ACA-marketplace network adequacy, state-CCRC /
  eldercare market quality for long-term planning; consult a
  state-bar-licensed estate attorney in both states AND a fee-only
  fiduciary CFP (NAPFA / XY-Planning) with multi-state experience.
  Verify both via state-bar member-search AND SEC IAPD before
  engagement.

## 14. Equity-comp / concentration-risk framing

### 14.1 RSU lockup and 10b5-1 constraints delay diversification

- **Statement**: The "sell-on-vest is tax-neutral" reflex is
  correct on RSU mechanics but the framing rarely engages with
  *RSU lockup and 10b5-1 trading-plan requirements* — for many
  tech employees, blackout windows around earnings, IPO-lockup
  periods (typically 180 days post-IPO), 10b5-1 plan pre-
  commitment requirements, and securities-law restrictions on
  insider trading constrain the *timing* of sell-on-vest, and
  the diversification benefit is delayed.
- **Source evidence**: `framings.md` §14 Excludes line on RSU
  lockup / 10b5-1 constraints; cross-domain edge into `tech-
  career` D4 per `decisions.md` §D4 + §D6. SEC-EDGAR / FINRA-
  BrokerCheck voice on 10b5-1 plan-document mechanics;
  retirement-and-equity-comp-experienced CPA voice on the
  blackout-window-vs-sell-on-vest timing.
- **Trigger**: Asker has vesting RSU at a publicly-traded employer
  AND is contemplating sell-on-vest as a diversification move AND
  is potentially subject to insider-trading restrictions (Section
  16 officer, executive, certain employee categories) OR is in
  an IPO lockup period OR is in an earnings blackout window AND
  has not separately considered 10b5-1 plan execution.
- **Failure mode**: Asker (Section 16 officer at public tech
  company) has $500k of vesting RSU during an earnings-blackout
  window; cannot sell during blackout; stock declines 30% over
  the blackout period before the trading-window opens; asker
  realized $500k of ordinary income on vesting (taxable in 2024)
  but the post-tax stock value is now $350k; net concentration-
  risk loss is $150k that 10b5-1 pre-commitment could have
  hedged.
- **Recovery move**: For Section 16 officers / executives /
  insiders, execute *10b5-1 trading plans* with quarterly-or-
  monthly sell-on-vest pre-commitment (per Rule 10b5-1 the plan
  must be entered when the executive is not in possession of
  material non-public information; SEC 2023 amendments tightened
  cooling-off and disclosure requirements); for IPO-lockup-bound
  employees, prepare a tranched-diversification plan for post-
  lockup execution; consult a retirement-and-equity-comp-
  experienced CPA AND a securities-law attorney (state-bar
  member-search for securities-law specialty) AND a fee-only
  fiduciary CFP (NAPFA / XY-Planning) with equity-comp specialty.
  Verify all via SEC IAPD / state-bar / FINRA BrokerCheck.

### 14.2 ISO-AMT-exercise-timing is highly path-dependent

- **Statement**: ISO-AMT-exercise-timing is *highly path-dependent*
  on company stage and stock-price trajectory — the framing's
  "exercise early for QSBS clock" reflex can be catastrophic if
  the company subsequently declines (AMT paid on FMV-at-exercise
  becomes a cash drag against a declined stock that may never
  recover). The framing's risk-tolerance calibration on ISO-
  exercise rarely matches the *actually-asymmetric* downside.
- **Source evidence**: `framings.md` §14 Excludes line on ISO-AMT-
  exercise-timing path-dependence; cross-domain edge into `tech-
  career` D6 per `decisions.md` §D6. Retirement-and-equity-comp-
  experienced CPA voice on ISO-AMT-exercise-timing methodology;
  The Finance Buff voice on AMT-credit-recovery mechanics; IRS-
  publication-authority voice (Pub 525, Form 6251 AMT).
- **Trigger**: Asker has ISOs in a private or recently-public
  company AND is contemplating early-exercise-for-QSBS-clock AND
  has not separately modeled the AMT-cash-drag scenario for
  company decline AND has not separately considered downside-
  asymmetry of cash spent on AMT against declining stock.
- **Failure mode**: Asker (startup employee, age 35, $50k cash
  savings) early-exercises ISOs at $0.50 strike when FMV is
  $5/share for 50,000 shares = bargain-element $225k; AMT due
  is ~$56k (28% AMT rate on the $225k bargain-element); asker
  pays $25k from savings + $30k from new credit-line; company
  subsequently fails (50% of startups don't reach liquidity);
  asker has paid $56k cash for stock now worth $0; AMT-credit-
  recovery of $56k spreads over decades if asker has high
  ordinary income, but the cash-drag during the recovery period
  is real.
- **Recovery move**: For ISO-exercise decisions, model the AMT-
  cash-drag-vs-stock-decline scenario explicitly; never use
  borrowed funds for ISO exercise unless the cash drag is
  recoverable from non-stock sources; for early-stage private-
  company ISOs, consider exercising only the amount where AMT-
  cash-drag fits within 6-12 months of ordinary income (limiting
  downside-exposure if company fails); coordinate with QSBS
  Section §1202 5-year-hold clock per §14.4; consult a retirement-
  and-equity-comp-experienced CPA via SEC IAPD with explicit
  ISO-AMT-exercise-timing experience. Verify CPA's specific Form
  6251 + Form 3921 (ISO-exercise reporting) experience before
  engagement.

### 14.3 Section 83(b) is irrevocable in 30 days

- **Statement**: Section 83(b) elections are *irrevocable, 30-day-
  window-from-grant* decisions — the framing's "elect 83(b) on
  founder stock" reflex is correct for high-conviction startup-
  founders but can lock in $50-200k of ordinary-income tax on
  stock that may be worth $0 in 3 years. The framing rarely
  engages with the asymmetric-risk-profile that makes 83(b)
  genuinely a high-conviction bet rather than a routine
  optimization.
- **Source evidence**: `framings.md` §14 Excludes line on §83(b)
  irrevocability and asymmetric-risk-profile; IRS-publication-
  authority voice (Pub 525 §83(b) mechanics; Treas Reg §1.83-2);
  retirement-and-equity-comp-experienced CPA voice on §83(b)
  decision methodology; cross-domain edge into `entrepreneurship`
  per `decisions.md` §D6.
- **Trigger**: Asker is a startup founder / early employee with
  restricted-stock-grant AND is within the 30-day window from
  grant AND is being advised to elect §83(b) without engaging
  with downside scenarios AND has not separately modeled the
  asymmetric-risk.
- **Failure mode**: Asker (early employee, restricted-stock grant
  of 200,000 shares at $1/share = $200k FMV at grant, 4-year
  vest) elects §83(b); pays ordinary-income tax on $200k at 32%
  = $64k federal plus state; company fails 30 months later;
  asker has paid $64k+ for stock now worth $0; the §83(b) was
  irrevocable; no claim-of-loss recovery beyond the basis-
  worthlessness (limited to $3k/year against ordinary income per
  IRC §165(g) for personal-loss capital-losses).
- **Recovery move**: For §83(b) decisions, *do not elect by
  default*; explicitly model the downside scenario (company
  fails, stock worth $0, $X of ordinary-income tax paid);
  reserve §83(b) election for high-conviction founder situations
  where the asker can absorb the downside without financial
  catastrophe; consult a retirement-and-equity-comp-experienced
  CPA via SEC IAPD with explicit §83(b) experience AND a
  securities-law attorney for cap-table mechanics within the
  30-day window. Verify both via SEC IAPD / state-bar member-
  search before engagement.

### 14.4 QSBS Section §1202 eligibility-fragility under-surfaced

- **Statement**: QSBS Section §1202 has *eligibility conditions* the
  framing rarely surfaces — the issuing company must have
  aggregate assets ≤$50M at the time of stock issuance, must be a
  C-corp, must be in an active business (not investment /
  personal-services / farming / hospitality), the holder must
  have acquired stock from the corporation (not from a secondary
  purchase), and the 5-year-hold-period applies per-share (early-
  exercise-on-vest may reset the clock). The framing's enthusiasm
  for QSBS understates the eligibility-fragility.
- **Source evidence**: `framings.md` §14 Excludes line on QSBS
  Section §1202 eligibility-fragility; cross-domain edge into
  `entrepreneurship` on QSBS planning per `decisions.md` §D6 /
  §D10. Retirement-and-equity-comp-experienced CPA voice on
  §1202 eligibility methodology; IRS-publication-authority voice
  (IRC §1202; Treas Reg §1.1202).
- **Trigger**: Asker has stock or options in a private company AND
  is anticipating significant appreciation AND is reasoning about
  QSBS §1202 exclusion AND has not separately verified the
  company's QSBS-eligibility on all 5 conditions.
- **Failure mode**: Asker (early employee at a $200M-valuation
  fintech startup) is told "your stock qualifies for QSBS
  exclusion" by a generalist accountant; holds for 5 years; at
  exit the IRS challenges QSBS exclusion because (a) company's
  aggregate assets exceeded $50M at stock-issuance date,
  (b) company's primary activity was "investment" not "active
  business" per §1202(e)(3) excluded categories; asker owes
  $10M+ in capital-gains tax that he believed was excluded;
  recovery via litigation is unlikely.
- **Recovery move**: For QSBS-anticipating askers, *verify all 5
  eligibility conditions* explicitly with documentation: (a)
  company's aggregate assets at stock-issuance date (request
  from company CFO; verify against capitalization-table records),
  (b) company is C-corp at issuance AND continuously through
  5-year hold, (c) company is engaged in active business per
  §1202(e)(3) excluded-category-list (NOT investment / banking /
  insurance / leasing / professional-services / hospitality),
  (d) stock was acquired directly from corporation in primary-
  issuance, (e) per-share-5-year-hold-clock from acquisition
  date; consult a retirement-and-equity-comp-experienced CPA
  via SEC IAPD with explicit §1202 experience AND a tax-attorney
  (state-bar member-search) for high-value cases; obtain written
  representations from the company on QSBS eligibility before
  relying on the exclusion. Verify all via SEC IAPD / state-bar
  before engagement.

### 14.5 ESPP qualifying-disposition vs disqualifying-disposition math

- **Statement**: ESPP (Employee Stock Purchase Plan) under §423
  has a binary qualifying-vs-disqualifying-disposition treatment
  that materially shifts the tax-cost basis of the discount and
  appreciation: *qualifying disposition* (hold ≥ 2 years from
  grant date AND ≥ 1 year from purchase date) gives LTCG
  treatment on the appreciation beyond the 15% discount-built-
  into-price; *disqualifying disposition* (sold earlier than
  either window) makes the entire discount ordinary-income at
  disposition. The framing's "ESPP is free 15% discount" rhetoric
  obscures the hold-period math that determines whether the
  discount is ordinary-income or LTCG-eligible.
- **Source evidence**: `framings.md` §14 Mental model line on
  ESPP §423 qualifying-disposition mechanics; The Finance Buff
  voice on ESPP-disposition decision methodology; IRS-publication-
  authority voice (Pub 525 ESPP; IRC §423(c)).
- **Trigger**: Asker participates in employer ESPP AND is
  contemplating sale of ESPP shares AND has not separately
  verified hold-period status (qualifying vs disqualifying) AND
  is reasoning about ESPP as if 15% discount is automatically
  preserved tax-advantageously.
- **Failure mode**: Asker (mid-career employee, $20k of ESPP-
  purchased stock at 15% discount over 2 years) sells shares 6
  months after purchase to diversify (disqualifying disposition
  — sold before 1-year-from-purchase); the entire 15% discount
  ($3k) becomes ordinary-income at 32% marginal = $960 federal
  plus state; the post-purchase appreciation is short-term
  capital-gain (also ordinary-rate); total tax-cost is materially
  higher than the qualifying-disposition path would have produced.
  For asker with longer-hold-tolerance the disqualifying-
  disposition sacrificed $1k-$2k in avoidable tax.
- **Recovery move**: For ESPP holdings, *verify hold-period status*
  (grant date + 2 years AND purchase date + 1 year for qualifying)
  before selling; for shares short of qualifying-disposition,
  weigh the tax-cost of disqualifying-disposition against the
  concentration-risk-cost of continuing to hold; consider holding
  to qualifying-disposition if (a) the asker has cash for
  diversification from other sources, (b) the company is not in
  significant decline scenario, (c) the asker is in a stable-
  income bracket where tax-deferral helps; consult a retirement-
  and-equity-comp-experienced CPA via SEC IAPD with explicit
  ESPP §423 experience on the qualifying-vs-disqualifying-
  disposition tax-arithmetic. Verify CPA via SEC IAPD before
  engagement.

---

## Cross-framing tensions

These call out where blindspots in one framing are the *recovery move*
of another, mirroring the structure in
[`framings.md` "Cross-framing tensions"](./framings.md). The pairings
are useful for the Triage / Risk Officer when the asker is clearly
inside one framing — the contrarian framing's blindspot list is often
the right intervention.

- **§1 Priority-order ↔ §14 Equity-comp / concentration-risk**. F1's
  clean Bogleheads-canonical sequence assumes smooth W-2 cash flow
  and unconstrained-by-equity-comp household budget; F14 overrides
  the priority order for equity-comp-heavy households. §1.1 (match-
  vesting-cliff makes "always max" job-tenure-conditional) and §14.1
  (RSU lockup delays diversification) are the cross-framing tensions:
  the asker over-anchored on F1's clean priority order needs F14.1's
  reminder that the diversification benefit they're expecting from
  sell-on-vest is delayed by lockup / 10b5-1 / blackout window; the
  asker over-anchored on F14 may benefit from F1.1's reminder that
  the match-capture they're skipping for equity-comp focus is itself
  tenure-conditional and may be a smaller actual benefit than the
  headline rate. Same equity-comp-heavy household, opposite first-
  move depending on dimensions emphasized.

- **§2 Marginal-rate arbitrage ↔ §12 Policy-volatility**. F2 computes
  contribution arbitrage from current marginal vs projected retirement
  marginal as deterministic point-estimates; F12 argues the projected
  retirement marginal is itself a policy-determined variable subject
  to TCJA-sunset / SECURE-cycle / SS-benefit-cut volatility. §2.1
  (TCJA-bracket-sunset makes "projected retirement marginal" a moving
  target) and §12.1 (over-hedging toward Roth costs real current-year
  deduction) are the cross-framing tensions: the asker engaging with
  F2 needs §2.1 surfaced (point-estimate-is-actually-a-distribution);
  the asker over-anchored on F12 needs §12.1 surfaced (the actual
  current-year deduction is certain while the projected-rate-rise is
  uncertain). Same facts, opposite Roth/traditional answer; the
  synthesis is "size the policy-hedge at conviction-weighted small
  amounts rather than dogmatize either direction."

- **§3 HSA-as-stealth-IRA ↔ §6 Behavioral-debt-payoff when cash-flow
  constrained**. F3 says fund HSA to the cap and pay current medical
  from after-tax savings, letting HSA compound 30 years; F6 says for
  the household with $15k credit-card debt and no emergency fund, the
  cash-flow constraint binds before HSA optimization. §3.1 (cash-flow-
  constraint makes "pay OOP let HSA compound" infeasible) and §6.4
  (cash-flow vs balance-sheet distinction in extreme cases) are the
  cross-framing tensions: the asker over-anchored on F3 needs §3.1's
  reminder that the contribution-side tax arbitrage alone is worth
  capturing; the asker over-anchored on F6 may need §6.4's reminder
  that even high-interest debt has a Roth-IRA-basis-withdrawal
  alternative the rigid "never raid retirement" reflex blocks. Triage
  should surface F6 / §3.1 when the asker's facts indicate cash-flow
  stress; surface F3 / §6.4 when the asker reads as savings-rich and
  the framings are pushing in inverse directions.

- **§4 Tax-arbitrage / Form-mechanic ↔ §10 Professional-referral**.
  F4's "fill the form correctly" assumes correct-form-execution; F10
  surfaces that practitioner-error rate is non-trivial and CPA-
  specialty-filter matters. §4.1 (paid-preparer backdoor-Roth Form-
  8606 error rate is non-trivial) and §10.2 (Fee-only-CFP coverage
  uneven across decision categories) are the cross-framing tensions:
  asker thinking "my CPA handled it" needs §4.1's reminder that
  franchise / generalist preparers reliably get backdoor-Roth Form
  8606 wrong; asker reaching for "consult a fee-only CFP" on a
  technical-mechanic question needs §10.2's reminder that the CFP
  category is generalist-broad and CPA / ERISA-attorney override is
  required for specific mechanic depth. The synthesis: use the
  selective-referral matrix in `decisions.md` §Notes to keyed-
  professional-to-decision-category.

- **§5 Risk-adjusted allocation ↔ §14 Equity-comp / concentration**.
  F5 reasons about portfolio-level target allocation with classical
  Modern-Portfolio-Theory diversification; F14 surfaces that vested-
  RSU + ESPP-discount-stock create a *stealth allocation* that swamps
  any chosen target. §5.2 (concentrated-single-stock dominates target
  allocation) and §14.5 (ESPP qualifying-vs-disqualifying disposition
  math) are the cross-framing tensions: same household, asker over-
  anchored on F5 misses the stealth-allocation problem entirely;
  asker over-anchored on F14 may focus too narrowly on the equity-
  comp-mechanics and miss the broader allocation discipline question.
  Both framings independently recommend diversification, but F5
  frames it as "pick a target and rebalance" while F14 frames it as
  "sell the concentration first, then think about target." On D4 they
  converge on outcome but diverge on path.

- **§7 Lifecycle / retirement-econ ↔ §9 Estate-and-intergenerational**.
  F7's withdrawal-sequencing default (taxable first, then tax-deferred,
  then Roth — preserves Roth tax-free compounding longest) is
  *inverted* by F9 when intent-to-bequeath is material. §7.5
  (decumulation-phase advisors face liability-incentive toward
  conservative) and §9.1 (withdrawal-sequence inversion for intent-
  to-bequeath missed by lifecycle default) are the cross-framing
  tensions: same withdrawal decision, opposite sequence; the asker
  over-anchored on F7 misses bequest-intent override entirely; the
  asker over-anchored on F9 may push aggressive Roth-conversion at
  the cost of cash-flow sustainability per F7. The synthesis: the
  asker's intent-to-bequeath weight (0%-100% of estate to heirs)
  scales the F9-vs-F7 mix; for 80%+ intent-to-bequeath F9 dominates,
  for pure-self-consumption F7 dominates.

- **§8 Asset-protection / creditor-shield ↔ §1 Priority-order**. F1's
  "rollover 401(k) to IRA on job change for lower-cost-investment-
  options" is correct on expense-ratio arithmetic but *weakens
  creditor protection* per F8. §1.5 (match-capture reflex misses
  high-fee-401(k) sub-optimization) and §8.1 (401(k)-fee vs shield-
  benefit trade-off is structurally invisible) are the cross-framing
  tensions: the asker over-anchored on F1 needs §8.1's reminder that
  the shield benefit is genuine for litigation-exposed households;
  the asker over-anchored on F8 needs §1.5's reminder that the fee
  drag of staying in a high-fee 401(k) is also real and may exceed
  the protection benefit for low-litigation-risk askers. The
  synthesis: asker-specific litigation-risk-assessment is the
  missing variable that determines which framing dominates.

- **§10 Professional-referral ↔ §11 Behavioral-and-automation**. F10's
  "always-consult-a-fee-only-CFP" is the safe default for the asker
  without time-or-inclination to self-study; F11's "automate
  everything via Bogleheads-flowchart-DIY + robo-rebalancing" is the
  right call for the asker with financial literacy and discipline.
  §10.3 (DIY-via-Bogleheads-flowchart under-engaged as legitimate
  alternative) and §11.4 (automation discipline anti-correlated with
  tactical optionality) are the cross-framing tensions: asker
  considering DIY needs §10.3 surfaced (it IS a legitimate path for
  moderate-complexity high-literacy); asker fully-automated needs
  §11.4 surfaced (tactical events require manual override). The
  synthesis: asker-self-classification on literacy + complexity +
  tactical-availability drives the F10 vs F11 mix; DIY-with-
  occasional-hourly-fee-consult is the modal optimal middle for
  many askers.

## Maturity note

This file is `planned` maturity per
[`_meta_ontology.md` §5](../_meta_ontology.md) (the personal-finance
domain is `planned`, like all V2 domains except tech-career which is
`in-migration`). Source-evidence lines above currently anchor to:

- `framings.md` Excludes lines (load-bearing — the framing-level
  Excludes were authored specifically to seed Layer 3, per the
  Notes-for-downstream-layers section of `framings.md`).
- `decisions.md` cross-domain edge flags (Triage Pass-1 multi-label
  hints into `tech-career` / `health-insurance` / `housing` /
  `family-planning` / `education-funding` / `entrepreneurship` /
  `legal-disputes`).
- Conceptual references to the personal-finance-specific community
  classes named in `framings.md` voice anchors (fee-only-fiduciary-
  CFP voice — NAPFA / XY-Planning-Network / Garrett-Planning-Network;
  Bogleheads voice — bogleheads.org wiki and forum, r/Bogleheads;
  Mr-Money-Mustache / ChooseFI / FIRE voice — mrmoneymustache.com,
  ChooseFI podcast, r/financialindependence, Big-ERN's
  earlyretirementnow.com; financial-economics-journalism voice —
  David Wessel at Brookings, Jeff Sommer at NYT, Anne Tergesen at
  WSJ; retirement-econ academic voice — Wade Pfau's
  RetirementResearcher, Michael Kitces's kitces.com Nerd's Eye View,
  Larry Kotlikoff's KotlikoffOnFinance + Maximize-My-Social-Security;
  The Finance Buff voice — thefinancebuff.com Harry Sit; retirement-
  experienced-CPA voice — AICPA Personal Financial Planning Section;
  ERISA-practitioner voice — Natalie Choate, Mary Kay Foss, ABA
  Section of Real Property Trust & Estate Law, ERISA Industry
  Committee (ERIC); SEC-EDGAR / FINRA-BrokerCheck voice —
  adviserinfo.sec.gov, brokercheck.finra.org, SEC.gov investor-alerts;
  IRS-publication-authority voice — Pub 550 / 590-A / 590-B / 525 /
  969 / 970, Form 8606 / 8889 / 8949 / 8962 Instructions; fee-only
  Social-Security-claiming-specialist voice — Mike Piper's Open Social
  Security + *Social Security Made Simple*, Larry Kotlikoff's
  Maximize-My-Social-Security, federally-funded SHIBA / SHIP per-state
  via shiphelp.org; state-bar-estate-attorney voice — state-bar
  lawyer-referral-services (NOT for-profit finders), ACTEC, Heckerling
  Institute materials; personal-finance-influencer / mass-media voice
  — Suze Orman, Dave Ramsey, Ramit Sethi; chronic-DIY-Reddit voice —
  r/personalfinance wiki + flowchart, r/Bogleheads pinned posts,
  r/financialindependence wiki, r/tax pinned guides).

When `domain_knowledge/personal-finance/sources.yaml` is authored and
`domain_knowledge/personal-finance/communities/*.md` community
profiles land (Layer 4 is the next sub-item per ROADMAP §4 personal-
finance checklist), source-evidence lines above should be tightened
to specific source-view ids. Until then, this file's grounding is
the framings-Excludes seed plus `decisions.md` cross-domain edge
flags plus the conceptual community-class voice anchors named above.

**Date-stamp risk**: anchor numbers below carry the date-stamp risk
inherited from the underlying IRS / Treasury / SSA / CMS / state-bar
policy corpus. Entries to re-check before relying on for an active
decision:

- §1.5, §11.3 — 2025-cycle 401(k) elective-deferral cap $23,500 +
  $7,500 age-50 catch-up + $11,250 age-60-63 super-catch-up (SECURE
  2.0 §603 phased in 2025); indexed annually; verify current year.
- §1.4 — §415(c) total 401(k) cap $70,000 (2025); indexed annually.
- §2.1, §4.2, §12.1 — TCJA 2017 brackets sunset Dec-31-2025 absent
  extension; 2026 reverts 12% → 15%, 22% → 25%, 24% → 28%. Verify
  current legislative posture before relying on either pre- or post-
  sunset rates.
- §2.4 — 2025 SS-wage-base $176,100; FICA 7.65% below base + 1.45%
  Medicare uncapped + 0.9% Additional-Medicare above $200k single /
  $250k MFJ; NIIT 3.8% above same thresholds. All indexed annually
  (wage-base) or fixed-with-legislation (Additional-Medicare / NIIT
  unchanged since 2013).
- §2.5 — Social-Security taxability thresholds ($25k / $34k single;
  $32k / $44k MFJ) NOT inflation-indexed since 1983; the thresholds
  themselves will not change but the inflation-erosion is the
  date-stamp-drift.
- §3.5 — DPC-and-HSA compatibility (IRS Notice 2013-54 + subsequent
  guidance; pending Primary Care Enhancement Act could formalize);
  significant date-stamp risk pending legislation.
- §3.2, §3.3, §6.4 — IRS Pub 590-A / 590-B / 969 specific provisions
  re-checked annually (HSA contribution limits, IRA contribution
  limits, RMD-age, ordering rules).
- §4.5 — §125 cafeteria-plan mid-year-election-change rules; Treas
  Reg §1.125-4 stable but interpretations may shift.
- §6.2 — PSLF / IDR / SAVE / PAYE rules have shifted multiple times
  2022-2025 (post-COVID emergency; SAVE plan litigation halt
  mid-2024); verify current schedule before relying on any
  forgiveness-pace assumption.
- §6.5 — Match-formula and true-up provisions are plan-document-
  specific; SECURE 2.0 §126 (529-to-Roth rollover) effective 2024
  but with 15-year-account-aging requirement; date-stamp risk on
  the rollover-eligibility calculation.
- §8.3 — *Clark v Rameker* 573 US 122 (2014) is statutory-law
  precedent on federal-bankruptcy; state-shield variation indexed
  per `decisions.md` §D10. State-specific protection of inherited
  IRAs continues to evolve (TX/FL/AZ/ID/MO/NC/OH affirmative; others
  varying).
- §9.2 — SECURE 1.0 (2019) 10-year-rule + final IRS regulations (Feb
  2024) on years-1-9-RMD-during-10-year window. The regulations were
  finalized in early 2024 after multiple proposed-vs-final iterations;
  re-check current IRS guidance before relying.
- §9.3 — 2025-doubled-estate-tax-exemption sunset ($13.99M-per-
  individual in 2025 reverting to ~$7M-indexed in 2026 absent
  congressional extension; Reg §20.2010-1(c) anti-clawback rule
  confirms pre-2026 gifts are permanent). Significant legislative
  uncertainty.
- §9.5 — FAFSA Simplification Act (effective 2024-25 academic year);
  re-check current FAFSA-treatment-of-grandparent-529 rules each
  cycle.
- §11.2 — 401(k) auto-escalate-and-true-up provisions are plan-
  document-specific; SECURE 2.0 §125 (auto-enrollment mandates for
  new plans starting 2025) shifts the default but not all plans.
- §12.5 — SECURE 2.0 phased provisions: §603 Roth-catch-up for high-
  earners effective 2026 (delayed from original 2024 effective date
  per IRS Notice 2023-62); §126 529-to-Roth rollover effective 2024;
  §125 auto-enrollment mandate effective 2025 for new plans; §107
  RMD-age phase (73 for 1951-1959 birth; 75 for 1960+ birth); §302
  RMD-miss-penalty reduced 50% → 25% (10% if cured within 2 years).
  All require current-year verification.
- §13.3 — ARPA / IRA enhanced ACA subsidies sunset end-2025 absent
  extension; current cliffs phase-out gradually vs pre-2021 400%-FPL
  hard-cliff. Verify current schedule each OE.
- §13.5 — State-shield law and state-income-tax-on-retirement-income
  state-specific; re-verify current state statutes when relying.
- §14.1 — 10b5-1 plan rules (SEC 2023 amendments tightened cooling-
  off period to 90 days for officers / directors; tightened disclosure
  requirements); re-verify before plan-execution.
- §14.2, §14.3 — ISO / §83(b) mechanics statutorily stable but
  practitioner-error rate non-trivial; verify CPA experience before
  executing time-bounded elections.
- §14.4 — QSBS §1202 has had several legislative-modification
  attempts (raising the $50M asset cap to $75-100M; reducing the
  5-year-hold to 3-years; capping the exclusion); current statute as
  of writing has the $50M / 5-year / $10M-or-10x-basis structure but
  re-verify before relying for exit planning.

**Mechanism E posture**: every Recovery move above routes to one of:
fee-only fiduciary CFP (NAPFA / XY-Planning / Garrett — fee-only NOT
fee-based) for D3 / D4 / D8 (asset-location, asset-allocation,
withdrawal sequencing); retirement-and-equity-comp-experienced CPA
for D1 / D6 / D7 (backdoor-Roth Form 8606; TLH wash-sale validation;
Roth-conversion sizing relative to IRMAA / NIIT / ACA cliffs); fee-only
Social-Security-claiming-strategy specialist for D8 (claim-age
coordination); state-bar-licensed estate attorney for D10 (trust
formation, SLAT / GRAT / Dynasty drafting, 2025-sunset-pre-2026-
gifting moves, beneficiary-form-audit-and-update); ERISA attorney for
D1 + D10 (high-balance 401(k) force-out disputes, Rule-of-55 /
SEPP-72(t) plan-document review, post-divorce-QDRO drafting, creditor-
protection consultation); SHIBA / SHIP volunteer for D8's Medicare-
coordination side (federally funded, free, conflict-free); SEC IAPD
Form ADV Part 2A / FINRA BrokerCheck procedural verification as
$0-friction procedural floor on any individual professional
recommended. This is **uniform Mechanism E gating** like immigration
(PR #48) and health-insurance (PR #75), not partial-gating like
housing (PR #64). The wrong call here is not recoverable on a
multi-year horizon: TCJA-2017 permanently eliminated Roth-conversion-
recharacterization (conversions are irrevocable from execution); SS-
claim-age-before-FRA permanently reduces PIA ~30% at 62 and compounds
for the survivor's life via higher-earner-survivor rule; missed
60-day-indirect-rollover-window turns the distribution into a taxable
event with no second chance; missed Medicare IEP triggers permanent
Part-B 10%-per-12-months-late premium add; missed contribution caps
are per-year-use-it-or-lose-it; cumulative-cost-of-procrastination
compounds at the equity risk premium for 30+ years and cannot be
re-made later. This file IS decision-support, NOT licensed-fiduciary
/ CPA / ERISA-attorney / state-bar-estate-attorney / Social-Security-
specialist / SHIBA advice. The framings name where the analysis
happens; the binding determination on any specific decision comes
from the professional with case-specific facts — current Summary Plan
Description, current state-of-residence shield law, current IRS
revenue rulings, current SSA Trustees Report and benefit projections,
the asker's full income and family picture, and the asker's full
beneficiary-form history. **Dollar-specific investment recommendations
on individual securities (buy $X of TICKER today with your $Y) are
uniformly out-of-scope at the Editor layer regardless of which framing
is active** — this is the load-bearing Mechanism E gate for the
domain, and the calibration that holds across all 70 entries above.
