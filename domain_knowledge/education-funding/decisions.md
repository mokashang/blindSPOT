# education-funding — decisions.md (Layer 1)

Decision ontology for `education-funding`. Scope inherits from
[`_meta_ontology.md` §7](../_meta_ontology.md): US higher-education
funding — student-loan type selection and refinance timing, graduate-
school ROI given career stage, 529 / Coverdell / taxable / Roth-IRA
mixes for children's college, repayment-plan selection and forgiveness
strategy, FAFSA / CSS-Profile positioning, and federal-vs-private loan
mix. Excludes K–12 private-school and tuition funding (overlaps
`family-planning`), employer-sponsored on-the-job training that is not
degree-conferring (overlaps `tech-career`), professional-licensing
exam fees and continuing-education that are not 1098-T-eligible, and
international-student / non-resident funding paths (deferred to V3+
under an outbound-education domain — F-1 / J-1 status interactions
belong in `immigration`, not here).

The `education-funding` domain is **high_stakes: false** per
`_meta_ontology.md` §7 — most decisions are slow-clocked and reversible
on multi-year horizons (refinance, switch repayment plan, defer
enrollment, transfer 529 beneficiary, take a leave of absence, drop
back to part-time, claim AOTC in a different year, pursue
employer-tuition next cycle). The dollar magnitudes are large but the
irreversibility profile is fundamentally different from
`health-insurance` (12-month plan-year lock-in + permanent Medicare
late-enrollment penalty) or `immigration` (out-of-status multi-year
bans, missed filing windows with no recovery). The two genuine
irreversibility traps inside education-funding are (a) refinancing
federal loans to private — which permanently erases IDR / PSLF / SAVE /
death-and-disability discharge / IDR-forgiveness optionality and is
not undoable, and (b) the 30-day-window-style **5-year-election** on
front-loaded 529 contributions under §529(c)(2)(B), where filing
errors propagate forward — but even these are bounded by their dollar
caps, not by life trajectory. The Editor posture is therefore
**decision-support framing rather than uniform Mechanism E deferral**:
the user is treated as a decision-capable adult navigating
slow-clocked financial choices, and the system surfaces the framings
the borrower / 529-funder / financial-aid community would name.
Selective referral is applied to specific decisions with concentrated
tail risk; over-referral degrades signal.

Selective referral categories (keyed by decision, not blanket-applied):

- **Student-loan attorney / Student Loan Borrower Assistance Project
  (SLBA) / National Consumer Law Center** — for default rehabilitation,
  servicer-error disputes (especially IDR-recertification miscounts
  and PSLF qualifying-employment / qualifying-payment disputes), and
  any bankruptcy-discharge posture post-*Brunner* / post-*Frost* / 2022
  DOJ-USDOE attestation-guidance shift (the discharge bar has softened
  but remains highly fact-specific). Warranted for decisions 1, 4, 10.
- **Retirement-experienced CPA or Enrolled Agent with §25A / §127 /
  §529 history** (NOT a generic 1040-prep CPA — the relevant
  qualifications are AOTC/LLC interaction with 529 distributions, 529
  state-tax recapture rules on out-of-state plans, employer §127
  exclusion mechanics, kiddie-tax §1(g) interaction with UGMA/UTMA
  growth, and the SECURE 2.0 §126 529-to-Roth rollover 15-year-clock
  and beneficiary-aging mechanics). Warranted for decisions 3, 6, 8, 9.
- **College financial-aid counselor / NACAC-member counselor / a
  high-school college-counseling office in the case of dependent
  students** — for FAFSA / CSS-Profile strategy, year-prior-prior base
  year positioning, merit-aid negotiation (yes, it is negotiable —
  most enrollment offices have a discretionary "professional judgment"
  budget), and appeal letters. Warranted for decisions 5, 8.
- **Fee-only fiduciary CFP (NAPFA-affiliated, AUM-free fee structure)**
  — for the 529-vs-Roth-vs-taxable college-funding mix and retirement-
  account-impact analysis. Particularly load-bearing for households
  where parental retirement readiness is itself underfunded —
  prioritizing the kids' 529 over the parents' Roth/401k is one of the
  highest-regret patterns in the personal-finance community
  (boundary `personal-finance`). Warranted for decisions 3, 6, 9.
- **Federal Student Aid Ombudsman Group** (within FSA, an
  escalation channel for unresolved servicer disputes) — for IDR
  recertification errors, PSLF qualifying-payment-count disputes
  after the servicer has rejected an appeal, and forbearance-steering
  remediation under the 2022–2024 IDR / PSLF account-adjustment
  consent decrees. $0-cost escalation; should be tried before
  retaining counsel.
- **State Bar / SEC-FINRA BrokerCheck / NACAC-directory verification**
  as a $0-friction procedural floor on any individual attorney / CPA /
  counselor / advisor recommended — verify license and disciplinary
  history before engagement. Cross-references `personal-finance` and
  `entrepreneurship` decisions.md on this same procedural floor.

Framing-axes named below are pointers — full framings will live in
`framings.md` (later artifact). `education-funding` is cross-cutting
in a specific way: rather than the domain cascading widely into
others (as `personal-finance` does), education-funding sits *between*
several adjacent domains and inherits framings from each: 529 vs Roth
mix sits between college-funding and retirement-funding
(`personal-finance`); employer tuition-reimbursement sits between
education and comp (`tech-career`); FAFSA divorced-parent mechanics
and custodial-account drag sit between college-funding and
family-structure (`family-planning`); HELOC-as-college-funding sits
between college-funding and home-equity (`housing`); self-employed-
parent EFC reporting sits between college-funding and business
structure (`entrepreneurship`). Cross-domain edges flagged inline
below: `personal-finance` overlaps on 529-vs-Roth-as-college-funding-
substitute (decisions 3, 6), SECURE 2.0 §126 529-to-Roth rollover
mechanics (decision 6), tax-bomb sinking-fund as Roth-conversion-
ladder candidate (decision 4), asset location across 529 / Roth /
taxable / UGMA-UTMA / Coverdell (decision 6), and the kiddie-tax
threshold trade-off (decisions 3, 6). `tech-career` overlaps on
employer §127 tuition reimbursement ($5,250 annual exclusion + the
retention-clawback windows large-tech employers impose) and the
MBA-to-tech-pivot ROI question (decisions 2, 9). `family-planning`
overlaps on kids' college funding ordering relative to retirement
(decisions 3, 6), custodial-account UGMA/UTMA basis transfer and
EFC drag (decisions 3, 8), and divorced-parent FAFSA reporting —
the FAFSA Simplification Act of 2020 changed the parent-of-record
rule from custodial-by-time to higher-income-of-the-two beginning
with the 2024–25 award year, which catches many divorced households
unaware (decision 8). `entrepreneurship` overlaps on self-employed-
parent FAFSA / CSS reporting (S-corp distributions vs salary affect
EFC differently than W-2 wages; CSS counts business assets that
FAFSA does not since the 2024 simplification removed small-business
reporting from FAFSA, but CSS still asks; decision 8) and on the
self-employed retirement vs college funding tradeoff (decision 3).
`housing` overlaps on home-equity-as-college-funding (HELOC vs
Parent PLUS rate and risk comparison, decisions 6, 7; primary-
residence is non-reportable on FAFSA but is reportable on CSS
Profile, decision 8). Routing across edges is V2-Triage's job; the
edge annotations here help future `framings.md` authors name the
adjacent domains.

---

## 1. Refinance federal loans to private vs preserve IDR / PSLF / SAVE / death-and-disability optionality

- **Scope**: Borrower with existing federal student loans (Direct
  Subsidized / Unsubsidized / Grad PLUS / Parent PLUS, or older
  FFEL / Perkins consolidated) is evaluating refinancing some or all
  of the federal balance to a private lender (SoFi, Earnest, ELFI,
  Splash, Laurel Road, etc.) — typically driven by a private-lender
  rate quote materially below the federal weighted-average. The
  decision is fundamentally about **whether the federal optionality
  is worth the rate premium** the borrower is currently paying.
  Distinct from decision 4 (which repayment plan to choose within the
  federal system) and decision 10 (PSLF qualifying mechanics, which
  presupposes staying federal). Cross-routes `personal-finance` on
  the rate-vs-optionality framing (boundary decision 3 in
  personal-finance — debt-payoff-vs-invest prioritization), and
  `tech-career` if a layoff probability is part of the model.
- **Framing-axes-covered**: federal-optionality-as-embedded-put-option
  (IDR-driven payment cap on adverse-income shocks, PSLF qualifying-
  employment forgiveness, IDR-25-year-forgiveness, death-and-
  disability discharge under §437(a), military / Peace Corps deferment,
  in-school deferment if returning for grad school — refinancing to
  private erases ALL of these and the erasure is permanent because
  re-federalization is not available), rate-spread-and-break-even
  (a 200bp rate spread on a $150k balance is ~$3k/year of interest
  savings; the optionality is worth multiples of that for any borrower
  with non-trivial layoff / disability / income-shock probability —
  the rough community heuristic is "do not refi federal if there is
  any plausible PSLF path or any household member with elevated
  disability risk"), SAVE-Plan-current-status-and-political-risk (SAVE
  was the most generous IDR plan with a 5% discretionary-income cap on
  undergrad and an interest-non-accrual subsidy; it is currently in
  litigation-induced forbearance as of the 8th Circuit injunction and
  the rulemaking-rollback process — borrowers in SAVE have been
  switched to administrative forbearance with months counting for
  PSLF but not for IDR-forgiveness, which materially changes the
  refi math), rate-fixed-vs-variable-and-lender-credit-tier-pricing
  (private lenders price aggressively for 800+ FICO + high-income
  professionals — radiologists / dentists / lawyers — but the
  same lenders re-rate hard on income change at refi-cycle so the
  "I'll just refi again if rates fall" assumption is fragile),
  cosigner-and-cosigner-release-mechanics-on-private-refi (most
  private refis allow cosigner-release after 12–48 months of
  on-time payments but require a re-underwrite that can fail if
  income has dropped — material for borrowers whose parent
  cosigned and wants release), federal-consolidation-as-non-refi
  alternative (Direct Consolidation preserves federal status and
  resets-then-recombines the qualifying-payment count on a
  weighted-average basis — useful for borrowers with mixed FFEL /
  Direct who want PSLF eligibility on the FFEL portion without
  losing optionality).
- **Sample situations**:
  - "$210k of federal grad-PLUS at 7.5% weighted-avg; SoFi offers
    refi to 5.25% fixed. I'm a software engineer at a big-tech
    company, AGI $280k, no plausible PSLF path. Refi save the
    $4.7k/year or keep federal optionality given the current
    layoff environment?"
  - "$95k federal undergrad + grad mix; I work at a 501(c)(3)
    research nonprofit, 6 years into PSLF on an IDR plan (now in
    SAVE-induced administrative forbearance). Earnest offered 4.95%
    fixed which would save $5k/year. Refi or stay the course
    through PSLF forgiveness at year 10?"
  - "Parent PLUS $120k at 8.05% (origination-fee inflated APR
    closer to 8.4%). Kid is now W-2 income-earning. We're
    considering having the kid take over via private refi in
    their name to drop the rate — what do we lose?"

## 2. Graduate school ROI given career stage — MBA / law / med / CS-Masters vs continue current trajectory

- **Scope**: Working professional (typically 3–8 years post-undergrad)
  evaluating whether to leave their current career trajectory for a
  full-time graduate program (typically MBA at top-15, JD at top-14,
  MD, MS-CS, or PhD), part-time / executive variant, or stay on
  current trajectory. Decision is fundamentally about the *return
  on tuition + opportunity cost of forgone income + the pivot the
  degree enables* relative to alternative paths (lateral move, internal
  promotion, side-startup, certificate program, employer-funded
  part-time). Distinct from decision 9 (the employer tuition-
  reimbursement mechanic, which presupposes already-employed
  part-time enrollment) and decision 6 (the funding-source mix once
  the decision to enroll is made). Cross-routes `tech-career`
  heavily — for software engineers, the MBA-to-PM / MBA-to-VC pivot
  has very different ROI than the same MBA into traditional
  consulting / finance tracks (typical 2026 outcome: MBA delivers
  positive NPV for finance / consulting / general-management
  pivots; modestly-negative-to-neutral NPV for engineering →
  product-management pivots that can also happen internally;
  highly-negative for engineers who would have stayed engineers
  anyway). MS-CS has its own framing — for self-taught or
  bootcamp-trained engineers, the MS-CS at a top-10 program
  unlocks FAANG-tier interviews + research-track-eligibility +
  H-1B-quota-exempt master's-cap routes (boundary `immigration`).
  PhD calculus is fundamentally different — opportunity cost is
  6–7 years not 2, but tuition is typically funded.
- **Framing-axes-covered**: lost-income-as-the-largest-cost
  (a $250k MBA is sticker-price; the $400k–$700k in forgone
  earnings over 2 years for a $200k–$350k-comp tech worker
  dominates the math and is rarely surfaced in the sticker-shock
  framing — total program cost is sticker + lost income + lost
  401k-match + lost-RSU-vest-on-cliff, easily $1M+ all-in for a
  senior software engineer), degree-as-credential-vs-degree-as-
  learning (MBA is overwhelmingly a credential + network + recruiting
  funnel and only marginally a curriculum upgrade — the learning is
  largely from peers and case-method; this means M7 / T15 ranking
  matters disproportionately because credential value is positional;
  MS-CS at non-top-program is a credential negative for most
  ML / systems / research tracks because the program signals
  weakness if the candidate could have done a top program),
  internal-promotion-vs-external-pivot-option-value (if the pivot
  the degree enables can also happen via internal mobility — eng-to-
  PM is the canonical case — the degree is paying for option-value
  that may already be free, and the lost-income cost makes the
  net NPV strongly negative for staying-internal pivots),
  loan-payoff-trajectory-on-post-MBA-comp (post-MBA finance / MBB
  consulting comp at $200–$280k base + bonus can amortize $200k of
  debt in 3–5 years; post-MBA non-target outcomes can take 8–12
  years; the dispersion is enormous and the median-MBA framing
  hides a bimodal outcome distribution), executive-and-part-time-
  variants-as-discounted-credential (Sloan Fellows, Berkeley-Haas
  EWMBA, NYU Stern part-time deliver some of the credential value
  at fraction of opportunity cost; the trade-off is recruiting-
  pipeline access — full-time programs control the campus-
  recruiting flow), employer-sponsorship-vs-loan-vs-self-fund
  (decision 9 — employer tuition-reimbursement with retention
  clawback windows can fund 30–80% of cost in exchange for 2–4 year
  retention; PhD-funded programs and JD-with-school-of-origin-
  scholarships are different funding regimes), age-and-career-
  curve-considerations (MBA ROI declines with age because the
  remaining-career-horizon shrinks the integral of post-degree
  comp uplift; the sweet spot is widely held to be 4–8 years
  post-undergrad, with negative ROI above ~12 years out unless
  the pivot is genuinely structural).
- **Sample situations**:
  - "L5 software engineer at FAANG, 6 years out, $380k total comp,
    wants to move into product management. Accepted at Wharton
    (full-pay $250k). Stay and pursue internal eng-to-PM rotation
    or take the MBA hit?"
  - "Year-3 consultant at MBB, $185k all-in, considering Stanford
    GSB. The 2-year opportunity cost is ~$450k; the post-MBA
    pivot is into VC / growth-equity. Worth the math?"
  - "Self-taught backend engineer, 4 years out, $160k at a
    series-C startup. Accepted at CMU MS-CS (full-pay $80k).
    Goes for FAANG ML-eng track or pivot into research? Lifetime
    NPV vs accelerating in current role?"

## 3. Front-load 529 with 5-year-election lump sum vs annual contributions vs Roth-as-substitute

- **Scope**: Parent / grandparent with a discrete pool of capital
  earmarked for a child's college funding, deciding the contribution
  cadence and vehicle mix. The §529(c)(2)(B) **5-year-forward
  election** allows a 5x annual-gift-tax-exclusion contribution
  ($95k single / $190k MFJ for 2026, per the indexed exclusion) in
  a single year by treating it as 5 ratable annual gifts — useful
  for grandparents using the lifetime estate-tax exemption before
  the 2026 sunset and for parents wanting to maximize tax-deferred
  growth. Distinct from decision 6 (the funding-source mix question
  when the 529 is one option among Roth / taxable / UGMA-UTMA /
  Coverdell) — here we presume the 529 is already chosen and the
  question is the *timing* of contribution. Cross-routes
  `personal-finance` (529 sits in the asset-location framing,
  boundary decision 3 / decision 9 of personal-finance/decisions.md),
  and `family-planning` on the inter-generational gifting framing.
- **Framing-axes-covered**: 5-year-election-mechanics-and-form-709-
  filing (Form 709 gift-tax return is required in the election year
  even though no tax is owed; election is per-donor-per-beneficiary
  not per-donor; failure to file Form 709 means the contribution
  isn't formally elected and any death within the 5-year window
  causes a clawback into the donor's estate — this is the most-
  missed mechanic), state-income-tax-deduction-and-recapture-on-
  out-of-state-rollover (most states with a 529 deduction recapture
  the deduction if you roll out to another state's plan; some
  states — NY, IL — allow tax-free in-state-to-in-state transfers
  but recapture out-of-state; this is the load-bearing reason to
  pick a state plan over a "best" plan like Utah / Nevada when the
  state-deduction value exceeds the expense-ratio drag), expected-
  growth-tax-deferral-vs-college-inflation (the longer the runway
  to enrollment, the larger the front-loaded-lump-sum advantage —
  18-year horizon with 7% real growth ~3.4x; 10-year horizon ~2.0x —
  the deferral advantage compounds against college-inflation 4–5%
  vs general-CPI 2–3%), Roth-as-substitute-and-the-no-state-
  deduction-tradeoff (using a Roth IRA for college costs is a
  community-common workaround for parents who fear "what if kid
  doesn't go to college" — but Roth IRAs have $7k/year contribution
  limits, no state deduction, and the parent must qualify under
  the AGI phase-out; the SECURE 2.0 §126 529-to-Roth rollover after
  15 years offers a partial hedge — see decision 6), beneficiary-
  change-and-rollover-flexibility (529 beneficiary can be changed
  to any family member of the original beneficiary without tax
  consequence — sibling, cousin, niece/nephew, the parent
  themselves; this materially de-risks the "kid doesn't go" case;
  one rollover per 12-month period allowed per beneficiary),
  grandparent-vs-parent-owned-529-and-FAFSA-treatment-post-
  simplification (the FAFSA Simplification Act removed grandparent-
  529 distributions from student-income reporting starting with
  the 2024–25 award year — previously these distributions counted
  as untaxed student income with a 50% EFC drag; this changes the
  grandparent-funding calculus significantly).
- **Sample situations**:
  - "Grandparent with $190k earmarked for newborn grandchild's
    college; can either 5-year-elect lump-sum into a 529 now or
    spread $19k/year over 10 years. What does the math look like
    given the 2026 estate-tax-exemption sunset?"
  - "Parent of 3-year-old; bonus year netted $350k pre-tax;
    considering $95k single-donor 5-year-election into a 529
    plus $19k/year going forward for the next 5 years — total
    funding ~$190k. NY plan with state deduction or
    out-of-state better-expense-ratio plan?"
  - "Two kids, 12 and 9; saved $80k in a taxable brokerage
    earmarked for college because we weren't sure 529 was right
    early on. Roll the $80k into 529 now (locking in the
    in-state deduction over 5 years to maximize the
    deduction-per-year cap of $10k/MFJ in our state) or keep
    taxable for flexibility?"

## 4. IDR + tax-bomb savings (sinking fund + Roth-conversion-in-low-income year) vs 10-year standard repayment

- **Scope**: Federal-loan borrower with a balance large enough that
  the 10-year standard payment would consume a structurally
  uncomfortable share of disposable income (typical inflection:
  loan balance > annual income), evaluating Income-Driven
  Repayment (IBR / PAYE / SAVE in current status / ICR — choice
  depends on loan vintage and family size) with the implicit
  bet that the 20–25 year forgiveness will fire AND that the
  taxable "tax bomb" on forgiven balance will be manageable.
  Distinct from decision 1 (whether to stay federal at all)
  and decision 10 (PSLF qualifying mechanics, which has no
  tax bomb because §108(f)(1) excludes PSLF-forgiven balances).
  IDR-forgiveness IS taxable as ordinary income on the
  forgiveness-year 1099-C UNLESS the borrower is also
  receiving insolvency exclusion under §108(a)(1)(B) or the
  current administrative-tax-exclusion-window through 2025 is
  extended (it was extended by ARPA through end-of-2025 — a
  potential cliff). Cross-routes `personal-finance` (the
  tax-bomb sinking fund is itself a portfolio-allocation
  decision and a Roth-conversion-in-the-low-income-year
  candidate, boundary decision 4 in personal-finance).
- **Framing-axes-covered**: IDR-payment-mechanics-and-
  discretionary-income-formula (each IDR plan defines
  discretionary-income differently — IBR/PAYE use 150% of
  poverty-line floor with 10% cap on the rest; SAVE used 225%
  / 5% on undergrad but is in administrative forbearance;
  ICR uses 100% / 20% and is the worst of the four for most
  borrowers; choice is mechanical given balance, AGI, and
  family size — the decision IS not which IDR plan but
  *whether* to be on IDR), the-tax-bomb-arithmetic (a $200k
  balance forgiven after 20 years on IDR with a borrower at
  35% marginal bracket = $70k tax liability due in cash that
  year; the sinking-fund needed is the future-value calculation
  back to today, typically $30–40k contributed now in a
  taxable account growing at market rate; this calculation is
  the load-bearing fact that the "I'll just be on IDR forever"
  framing systematically misses), tax-bomb-exclusion-cliff-2025
  (ARPA §9675 excluded student-loan forgiveness from federal
  taxable income for 2021–2025; the cliff at end-2025 means
  borrowers reaching forgiveness post-2025 face the full
  ordinary-income inclusion absent further extension; SAVE-
  borrowers reaching forgiveness in 2026+ are most exposed),
  Roth-conversion-in-low-income-year-as-tax-bomb-bracket-
  management (in years where the borrower has a structurally
  low income — sabbatical, leave, between jobs — the tax-bomb
  cash hit is partly offsettable by accelerating Roth
  conversions in those same years to use up bracket headroom;
  this is a personal-finance cross-edge that few borrowers
  surface), insolvency-exclusion-§108(a)(1)(B) (if forgiven
  amount + other income leaves the borrower with negative
  net worth at the moment of forgiveness, the forgiveness is
  excluded from income under the insolvency rule — this is a
  fact-specific computation, must be filed with Form 982,
  and is a CPA-supervised analysis), state-level-tax-bomb
  (state taxation of forgiven loans varies — some states
  conform to federal ARPA exclusion, others don't; California,
  Mississippi, Indiana, North Carolina, Wisconsin treated
  the 2022 one-time forgiveness wave as state-taxable even
  when federally excluded; for IDR borrowers, the state-
  exposure matters as much as federal).
- **Sample situations**:
  - "$280k of federal grad-PLUS + Direct Unsubsidized, AGI
    $115k, single, no PSLF path (private-sector tech). IBR
    10-year payment would be ~$3,200/mo (impossible);
    discretionary IBR payment is ~$700/mo. Stay on IDR for
    20 years to forgiveness or pay aggressively to avoid the
    tax bomb?"
  - "PSLF-eligible borrower at year 6 of 10; spouse just took
    a tech job and household AGI jumped from $90k to $230k.
    The PAYE recertification is going to spike from $400/mo
    to $1,800/mo on the new household income — should we file
    taxes MFS to keep my IDR payment low or MFJ for the
    long-term tax-planning win?"
  - "I'm 4 years into IBR, $190k balance not amortizing
    because the IDR payment doesn't cover interest. I'll
    forgive in 2046 — way past the ARPA exclusion cliff —
    so I need to build a tax-bomb sinking fund. How big and
    where should it live?"

## 5. In-state public vs out-of-state private with merit aid vs ranked-private with need-based aid

- **Scope**: Prospective undergraduate (or their family) deciding
  among admit offers that differ along the public-vs-private,
  in-state-vs-out-of-state, and merit-vs-need-aid axes. The
  decision is fundamentally about **net cost per outcome** —
  sticker prices are largely irrelevant; the relevant comparison
  is the post-aid net price of attendance over 4 years against
  the wage premium and prestige value of each program. Distinct
  from decision 2 (graduate-school decision, which has different
  cost structure and ROI curve) and decision 7 (the federal-vs-
  private mix question once the school is chosen). Cross-routes
  `family-planning` on the household-financial-readiness framing
  and on the role of the student's preferences vs the funder's
  preferences in the joint decision.
- **Framing-axes-covered**: sticker-vs-net-price (the College
  Scorecard and each school's Net Price Calculator publish
  average net price by income decile; the sticker price is
  the worst possible anchor — flagship publics often have
  net prices for high-income families near sticker, while
  ranked-private schools with strong need-aid policies
  publish net prices below in-state-public for middle-income
  families; the decision turns on the difference, not the
  number on the front page), merit-vs-need-aid-and-financial-
  aid-leverage (merit aid is school-discretion and *highly*
  negotiable for cross-admits between peer schools; need-
  based aid is computed by the FAFSA / CSS-Profile formula
  and is less negotiable absent a "professional judgment"
  appeal — see decision 8; merit-aid letters explicitly
  list a contact for "additional consideration if
  comparable offer from a peer institution"), outcomes-by-
  program-not-by-school (engineering at a flagship public
  often out-earns liberal-arts at a ranked-private; the
  College Scorecard now publishes program-level
  earnings outcomes for federally-funded programs — these
  are more decision-relevant than US News rankings; pre-
  professional programs — pre-med, pre-law, accounting,
  engineering — have weaker school-effects than
  generalist humanities / social sciences), four-year-vs-
  five-year-completion (graduation-rate variance is a
  load-bearing axis — schools with 60% 4-year-graduation
  rates effectively cost 20%+ more than schools with 85%
  4-year-graduation rates; on-time completion correlates
  with class size, advising density, and selectivity, NOT
  with sticker price), debt-burden-per-program-and-
  cohort-default-rate (the College Scorecard publishes
  median federal debt at graduation and 3-year-cohort-
  default-rate by program; programs with high-debt /
  high-CDR are typically for-profit or low-selectivity
  private schools and should be approached with extreme
  caution), prestige-as-network-and-recruiting-funnel-
  for-target-careers (target-school recruiting at BB
  finance / MBB consulting / FAANG-new-grad-tech is
  concentrated at ~30 schools nationally; "school doesn't
  matter" is true for most careers and very false for
  these specific recruiting funnels — the framing
  honesty is to name which careers depend on the
  prestige tier), legacy-and-need-blind-vs-need-aware
  admissions (most flagship publics are need-blind in
  admissions for in-state; many privates are need-blind
  for first-time freshmen but need-aware for transfers
  and waitlists; some schools — Tufts, Wesleyan, several
  others — are explicitly need-aware which means the
  family's CSS-Profile EFC affects admission likelihood;
  this is opaque to most applicants).
- **Sample situations**:
  - "Daughter admitted to in-state flagship at $32k/yr net
    and to a T20 private at $58k/yr net (merit). Both
    offer engineering. The private has a stronger campus-
    recruiting pipeline but the public has the in-state
    network. 4-year cost delta is $104k. Worth it?"
  - "Son admitted to Cornell (CSS-Profile EFC came in at
    $48k/yr, sticker $85k, net offer $42k after grants)
    and to UNC-Chapel Hill out-of-state ($55k/yr net, no
    merit). I'd assumed Cornell would be out of reach;
    how do I read this and what's the negotiation lever?"
  - "Daughter wants to go to a small liberal-arts college
    with a $66k/yr net price for an English major. State
    flagship would be $19k/yr. Family has $180k saved.
    She'll qualify for federal Direct loans plus we can
    do Parent PLUS. How should we frame the conversation?"

## 6. 529 vs Roth-as-college-funding-substitute vs taxable brokerage vs UGMA/UTMA vs Coverdell mix

- **Scope**: Parent deciding the *vehicle-mix* for college funding
  given a discrete savings rate (e.g. $1,000/month earmarked for
  the kid's college over 18 years). The five vehicles each have
  distinct tax treatment, financial-aid implications, control
  characteristics, and flexibility profiles. The decision is
  rarely "one vehicle" — well-constructed plans typically
  combine 2–3 vehicles to hedge across the "kid goes to expensive
  private", "kid goes in-state cheap", "kid skips college", and
  "parent loses job and needs the money" scenarios. Distinct
  from decision 3 (the contribution-cadence question within a
  chosen vehicle) and decision 7 (loan-source mix once savings
  have been exhausted). Cross-routes `personal-finance` heavily
  (asset location, kiddie-tax §1(g), 529-to-Roth SECURE 2.0
  rollover, custodial-account basis-transfer — boundary
  decision 3 / decision 6 in personal-finance).
- **Framing-axes-covered**: 529-vs-Roth-tradeoff-on-state-tax-
  and-flexibility (529 has state-deduction-on-contribution +
  tax-free-growth-and-qualified-distribution + no flexibility
  for non-college use except via the 10% penalty + ordinary-
  income clawback on earnings; Roth has no state deduction +
  tax-free-growth + tax-free-after-59.5 + full flexibility
  to leave for retirement if not needed for college; the
  framing tension is "lock in the state deduction now vs
  preserve full flexibility for retirement"; the 529-to-Roth
  SECURE 2.0 §126 rollover after 2024 partially closes the gap
  but with strict caps — see next axis), SECURE-2.0-§126-529-
  to-Roth-rollover-mechanics-and-15-year-clock (effective
  2024+, a 529 with at least 15 years of seasoning can roll
  up to $35k lifetime into a Roth IRA in the *beneficiary's*
  name, subject to the annual-Roth-contribution limit, the
  beneficiary having earned income, and the 5-year-clock on
  recent contributions; this means a 529 funded heavily in
  the 2025–2027 window cannot roll to Roth until 2040–2042;
  this is a long-clock partial-flexibility hedge, not a
  near-term-flexibility solution; many financial-press
  outlets oversold the mechanic when SECURE 2.0 passed),
  custodial-account-UGMA-UTMA-basis-transfer-and-kiddie-tax
  (UGMA/UTMA is technically the *child's* asset with
  parent-as-custodian; assets transfer to child's control at
  the state's age-of-majority — 18, 19, or 21 depending on
  state; the kiddie-tax §1(g) applies parent's marginal rate
  to all unearned income above $2,600/year — 2026 indexed
  threshold; the EFC drag on UGMA/UTMA is severe — 20% of
  asset value vs 5.64% for parent-owned 529 — which is the
  load-bearing reason to avoid heavy UGMA/UTMA funding when
  financial-aid eligibility is plausible), taxable-brokerage-
  flexibility-and-capital-gains-positioning (taxable has no
  tax preference on growth but full flexibility; in
  combination with a 0%-LTCG-bracket harvest in low-income
  years — typical for parents in early-retirement or
  sabbatical — taxable can approach 529 efficiency with
  much more flexibility; downside is reportable as parent
  asset on FAFSA at 5.64% drag), Coverdell-ESA-niche-use
  (limited to $2k/year contribution per beneficiary —
  largely supplanted by 529's higher limits + K–12-tuition
  qualified-distribution rules added by TCJA — Coverdell
  retains a slight edge for K–12-private-school funding
  but for higher-ed it's mostly obsolete except as a
  flexibility complement), 529-K-12-tuition-distribution-
  TCJA-rule ($10k/year per beneficiary qualified distribution
  for K-12 private-school tuition was added by TCJA — this
  changes the 529 from a college-only vehicle to a
  K-12-plus-college vehicle, which complicates the
  funding-cadence calculus and matters for families using
  private K-12), parental-retirement-readiness-as-the-
  load-bearing-question (the single most important framing
  in this decision is whether the parents are themselves on
  track for retirement; the personal-finance community
  consensus is that prioritizing kids' 529 over parents'
  Roth/401k contributions is one of the highest-regret
  patterns — students can borrow for college, parents
  cannot borrow for retirement; this is the cross-edge to
  personal-finance decision 1 — boundary contribution
  ordering).
- **Sample situations**:
  - "Newborn, $1,500/month earmarked. We're behind on our
    own retirement (parents ages 38, 40, combined ~$200k in
    retirement). 100% to 529, split with Roth, or stuff
    parental retirement first?"
  - "Kid is 14; we've over-saved in a 529 ($240k) because
    we feared underfunding; now we're nervous about the 10%
    penalty + ordinary-income tax on the leftover if she
    goes to a cheaper school. Do we slow contributions, plan
    a 529-to-Roth runway, or shift to taxable now?"
  - "Two kids 8 and 5; we want to seed UGMA accounts with
    appreciated stock from a brokerage to step up the basis
    against the kids' lower brackets — what's the actual
    tax math after kiddie-tax and what does it do to FAFSA?"

## 7. Parent PLUS vs student federal subsidized/unsubsidized vs private with cosigner mix

- **Scope**: Family with insufficient savings to fully fund a
  chosen college and now selecting *which loans* to take. The
  federal student-loan structure differentiates Direct
  Subsidized (for demonstrated need, undergrad only, interest
  paid by government while in school) from Direct Unsubsidized
  (no need requirement, interest accrues during school), and
  caps these at $5,500–$7,500/year for dependent undergrads
  ($31k aggregate undergrad cap). Anything above the cap is
  filled by Parent PLUS (the parent borrows in their name,
  no aggregate cap, originates with a 4.228% fee — 2026 rate
  — and a fixed rate set annually that for 2025–26 is in the
  high-7s%), Grad PLUS (similar mechanics, student-borrower,
  for grad school), or private loans (typically with a
  parent cosigner for undergrad). Distinct from decision 1
  (refi *after* origination) and decision 5 (school choice).
  Cross-routes `personal-finance` on the parental-debt-vs-
  retirement-priority framing and `housing` on the
  HELOC-as-college-funding-alternative framing (boundary
  housing decision 8 — cash-out refi vs HELOC).
- **Framing-axes-covered**: federal-cap-stack-and-the-PLUS-
  premium (federal subsidized + unsubsidized is the cheap
  capital; everything above that is at a 1.5–2.5% premium
  for Parent PLUS — the 2025–26 PLUS rate is 9.08% with a
  4.228% origination fee, effective APR closer to 9.5%; this
  is materially more expensive than student-direct), Parent-
  PLUS-as-parental-debt-vs-student-debt-and-cosigner-
  asymmetry (Parent PLUS is the *parent's* legal debt — the
  student is not on the loan; private loans are typically
  in the student's name with parent cosigner — cosigner
  release after 12–48 months on-time depending on lender,
  re-underwrite required; the asymmetry matters for estate-
  planning — Parent PLUS discharges on the parent's death
  under §437(a), private loans typically do not), private-
  loan-rate-vs-PLUS-tradeoff (private undergrad loans with
  a strong-credit cosigner are routinely priced at 200–400bp
  below Parent PLUS; the trade-off is loss of federal
  benefits — IDR, PSLF (only matters for grad), death-
  discharge, in-school-deferment under federal terms), HELOC-
  or-cash-out-refi-as-alternative-funding (HELOC at prime
  + small spread can undercut PLUS by 100–300bp depending
  on rate environment; trade-off is home-equity at risk +
  HELOC variable-rate vs PLUS fixed-rate + loss of federal
  protections; cash-out refi locks in a rate but resets the
  amortization clock — boundary housing decision 8), Pay-As-
  You-Earn-and-Borrower-Defense-on-private-debt (private
  loans have NO IDR equivalent — the only repayment-
  hardship lever is lender-discretion forbearance, which is
  typically 12 months max and accrues interest; Borrower
  Defense to Repayment under §455(h) only applies to federal
  loans; this asymmetry is the load-bearing case for
  topping out federal first), federal-aggregate-undergrad-
  cap-and-the-shape-of-the-decision (the $31k aggregate
  undergrad cap on federal direct means the decision IS
  essentially "we max federal direct, then everything above
  that is PLUS vs private — and PLUS-vs-private is rate-
  sensitive but federal-protection-asymmetric"; framing the
  decision as "federal first" is the community-default
  starting point), in-school-payment-vs-deferment-trade-off
  (federal direct subsidized has interest paid by government
  during school; everything else accrues interest during
  school which capitalizes at repayment-entry; making in-
  school interest-only payments on Unsubsidized / PLUS /
  private avoids capitalization and dramatically reduces
  the total-cost-of-borrowing — typically 10–20% on a 4-year
  loan).
- **Sample situations**:
  - "Daughter's first year at a $58k/yr net-cost school. We
    have $30k/yr we can pay from cash flow; need to borrow
    $28k. She's eligible for $5,500 federal direct
    subsidized + $2,000 unsubsidized. The remaining $20,500
    — Parent PLUS at 9.08% or Sallie Mae private at 7.75%
    with my cosigner?"
  - "We've been doing Parent PLUS for 3 years on our oldest
    ($65k total at 8.5% weighted avg). HELOC available at
    prime + 0.5% (~8% currently). Move it all to the HELOC
    and lose federal protections, or stay on PLUS?"
  - "Son entering grad school. Direct Unsubsidized cap is
    $20.5k/yr but his program costs $75k/yr. Grad PLUS or
    private? PSLF is in the picture because he's going into
    public defender work post-JD."

## 8. FAFSA / CSS-Profile asset positioning and base-year timing

- **Scope**: Family in the 2 years pre-college-enrollment (or
  earlier if planning a 529 funding cadence with FAFSA in mind)
  positioning assets and income to optimize Expected Family
  Contribution / Student Aid Index. Under FAFSA Simplification
  Act, beginning 2024–25 award year: (a) parent-of-record on
  the FAFSA is now the *higher-income parent* in divorce, not
  custodial-by-time; (b) small-business and family-farm assets
  are NO LONGER reportable on FAFSA (but ARE on CSS Profile);
  (c) grandparent-529 distributions are NOT student income
  (formerly the "grandparent 529 trap"); (d) Pell-eligibility
  formula simplified to family-size-and-AGI; (e) the term
  "EFC" was replaced with "SAI" but conceptually similar.
  CSS Profile (used by ~200 mostly-private schools for
  institutional aid) is more granular than FAFSA — counts
  home equity in primary residence, asks about non-retirement
  assets in greater detail, asks about divorced non-custodial-
  parent income separately. Distinct from decisions 5
  (school-choice) and 9 (employer-tuition mechanics).
  Cross-routes `family-planning` (divorced-parent FAFSA
  mechanics, custodial-account drag — UGMA/UTMA is reported
  as student asset at 20% drag), `personal-finance` (asset
  location for FAFSA optimization, Roth-vs-529 mix, retirement-
  account-exclusion from both FAFSA and CSS), `entrepreneurship`
  (self-employed parent income reporting, S-corp salary-vs-
  distribution affecting AGI), and `housing` (primary-
  residence excluded from FAFSA but included on CSS Profile
  for many schools).
- **Framing-axes-covered**: base-year-is-prior-prior-year
  (FAFSA uses the tax year *two years* before the award year
  — so for 2025–26 awards, 2023 tax year is base; this means
  the AGI to manage is 2 years before college start, which
  means strategic Roth-conversions, capital-gains-harvests,
  business-sale-timings should be made BEFORE the base year
  starts to avoid inflating reported income at the FAFSA cliff
  age), retirement-account-exclusion-and-the-shelter-trade-off
  (FAFSA AND CSS Profile both exclude retirement-account
  balances — 401k, IRA, Roth, 403b — but include non-
  retirement assets including taxable brokerage; this creates
  a powerful incentive to maximize retirement-contribution
  in the pre-base-year window, which is also good
  personal-finance regardless of FAFSA — boundary
  personal-finance decision 1), custodial-account-drag-and-
  basis-transfer-timing (UGMA/UTMA is student asset, 20%
  drag on FAFSA; parent-owned 529 is 5.64% drag; transferring
  appreciated UGMA/UTMA assets to a custodial-529-for-same-
  beneficiary is possible BUT triggers capital-gains at the
  child's basis; many families do this transfer in
  early-to-mid teen years to convert drag from 20% to 5.64%
  — but only if the unrealized gain is small enough that
  the kiddie-tax + LTCG cost is less than the FAFSA-drag
  savings), divorced-parent-of-record-post-simplification
  (the FAFSA Simplification Act of 2020 changed parent-of-
  record from custodial-by-time to *higher-income-of-the-
  two-parents*; this means divorced couples need to model
  which parent's income produces a better aid result, and
  custody timing is no longer a lever for FAFSA — though
  CSS Profile schools still ask about both parents
  separately and most require the non-custodial-parent CSS
  unless the school has formally waived it), CSS-Profile-vs-
  FAFSA-asymmetric-disclosure (CSS counts home equity in
  primary residence — typically capped at 1.2–2.4× income at
  schools with home-equity caps, uncapped at others —
  while FAFSA does not; CSS counts small-business assets
  while FAFSA does not since 2024; the dual-reporting means
  CSS schools see a richer asset picture than FAFSA schools,
  which is why some families with significant home equity
  +/or small business assets see CSS-school EFCs much
  higher than FAFSA-school SAIs), professional-judgment-
  appeal-mechanism (financial-aid offices have discretionary
  authority under §479A to adjust the data elements in the
  FAFSA / CSS to reflect special circumstances —
  loss-of-job, divorce mid-process, medical-expense, business
  loss; this is the appeal lever and the most-overlooked
  one), grandparent-529-and-the-removed-trap (under the new
  FAFSA, grandparent-529 distributions are NOT reported as
  student income; this was the highest-impact change in the
  Simplification Act for many funder strategies — boundary
  decision 3 cadence).
- **Sample situations**:
  - "Daughter starts college fall 2027. We're considering a
    large Roth-conversion in 2024 to use up some bracket
    headroom — but that's our base year for her FAFSA.
    How do we sequence the conversion vs FAFSA optimization?"
  - "Divorced; my ex makes $280k, I make $130k; under the new
    rules my ex is the FAFSA parent-of-record. But she's
    applying to two CSS Profile schools that ask about both
    parents — does it matter that my ex won't share her
    data?"
  - "Self-employed via S-corp; I take a $90k salary +
    $180k distribution. FAFSA only looks at AGI but CSS asks
    about business assets and asks the salary-vs-distribution
    question. How do I model both?"

## 9. Employer tuition reimbursement ($5,250 §127 exclusion + retention clawback) vs scholarship-stacking vs self-pay

- **Scope**: Working professional considering enrolling in a
  degree program (part-time MBA, MS-CS executive, JD-part-time,
  certificate or stackable-credential) where the employer
  offers tuition reimbursement up to the IRC §127 exclusion
  cap ($5,250/year tax-free) or above the cap. Decision spans
  whether to use employer reimbursement at all (it locks in
  retention via clawback windows — typically 1–4 years post-
  reimbursement, prorated), whether to stack employer
  reimbursement with external scholarships, and how to
  sequence enrollment across years to maximize §127 usage.
  Distinct from decision 2 (the full-time graduate-school
  decision, which is the alternative path) and decision 6
  (general funding-source mix). Cross-routes `tech-career`
  heavily on the retention-clawback-as-golden-handcuffs
  framing, and `personal-finance` on the W-2-imputed-income
  treatment of reimbursement above the §127 cap.
- **Framing-axes-covered**: §127-exclusion-cap-and-the-
  above-cap-imputed-income (IRC §127 allows up to $5,250
  per calendar year of employer-paid tuition + fees + books
  + supplies to be excluded from W-2 income; anything above
  $5,250 is imputed taxable wages on the W-2 unless the
  employer also runs a §132(d) Working-Condition-Fringe
  exclusion for job-related courses — most employers do
  NOT distinguish, so above-cap reimbursement gets taxed
  at marginal rate + payroll; this changes the effective
  reimbursement value materially), retention-clawback-as-
  embedded-noncompete (most large-tech / consulting /
  finance tuition-reimbursement programs require continued
  employment for 1–4 years post-reimbursement, with full
  proration; this is functionally a golden-handcuff
  agreement — leaving in year 1 of the clawback period
  triggers repayment of 80–100% of the tuition; the
  community framing is "tuition reimbursement is comp
  with a retention lock"; cross-references `tech-career`
  decision 5 on cliff-equity-vs-leave timing), part-time-
  enrollment-and-tuition-per-credit-hour-arithmetic (most
  graduate part-time programs price per-credit-hour;
  $5,250/year of §127 covers ~1.5–2 credits at $3,000/credit
  T15 MBA pricing, ~3 credits at $1,600/credit state-flagship
  pricing; this means §127 is a partial subsidy for most
  part-time MBA programs, full subsidy for many cheaper
  programs), employer-pre-approval-and-pre-enrollment-
  paperwork (most §127 plans require pre-enrollment
  approval; the program must be on the employer's approved-
  list OR the course must be job-related under §132(d);
  late filing forfeits the §127 status), scholarship-
  stacking-and-displacement (most institutional scholarships
  do NOT stack with employer reimbursement for the same
  cost — the school adjusts the scholarship downward if
  the employer pays first; the order of application
  matters; some scholarships are tax-free under §117(a)
  for tuition + required fees but employer reimbursement
  for the same is §127 — overlap is treated as a wash,
  not stacked), grad-school-attendance-during-employment-
  vs-leap (the §127 path lets the user pursue a degree
  with no opportunity-cost on income — this is what makes
  it the dominant strategy for engineers / consultants /
  finance pros pursuing MBA / MS-CS / JD-part-time as long
  as the program quality is acceptable; the trade-off is
  the time-cost — typical part-time MBA is 3 years at
  20–25 hours/week, much harder on the employee's life
  than a 2-year full-time program; see decision 2 for the
  full opportunity-cost framing).
- **Sample situations**:
  - "Big-tech engineer, $250k comp, considering part-time
    MBA at a T15 ($88k/yr total cost). Employer offers
    full reimbursement up to $20k/yr with a 3-year retention
    clawback. Stack the cap, plan around the clawback, or
    self-pay for portability?"
  - "Consultant, $185k base + bonus, accepted at exec-MS-CS
    program at Georgia Tech (OMSCS, $7k total). Employer
    reimbursement: $5,250/yr, 2-year clawback. Just self-pay
    given the low total cost and skip the clawback?"
  - "Mid-career analyst, $140k, considering JD-part-time at
    state-flagship night program ($25k/yr). Employer offers
    $7,500/yr (above-§127-cap gets imputed). 4-year program,
    4-year clawback — that's an 8-year total commitment
    when you stack. Do the math vs taking the loan and
    keeping mobility."

## 10. PSLF qualification (120-payment count + 501(c)(3) employment + employment-certification cadence) vs IDR-25-year-forgiveness

- **Scope**: Federal-loan borrower employed (or considering
  employment) at a 501(c)(3) nonprofit, government agency,
  AmeriCorps, Peace Corps, or other qualifying public-service
  employer — evaluating whether to pursue PSLF (Public Service
  Loan Forgiveness under §455(m)). PSLF requires 120 qualifying
  monthly payments while employed by a qualifying employer on
  a qualifying repayment plan (any IDR plan, or 10-year
  standard which would have zero balance left at month 120
  anyway making PSLF useful primarily under IDR). The
  attractive feature is **§108(f)(1) excludes PSLF-forgiven
  balances from federal taxable income** — there is no "tax
  bomb" — distinguishing PSLF from IDR 20/25-year forgiveness
  which IS taxable absent ARPA extension. The decision is
  *whether to pursue PSLF as the dominant strategy*, given
  career flexibility constraints. Distinct from decision 4
  (IDR + tax-bomb planning, which applies to non-PSLF
  borrowers) and decision 1 (whether to refi — refi out of
  federal kills PSLF eligibility permanently). Cross-routes
  `tech-career` on the public-service-vs-private-tech career
  framing.
- **Framing-axes-covered**: 120-qualifying-payment-count-
  and-the-account-adjustment (the 2022–2024 IDR / PSLF
  account-adjustment moved millions of borrowers' qualifying-
  payment counts forward, capturing months previously stuck
  in forbearance / non-IDR plans; borrowers who haven't
  applied for the account-adjustment review through
  StudentAid.gov should do so before the adjustment window
  closes — historically MOHELA / Nelnet underreported
  qualifying payments and the adjustment is the corrective),
  qualifying-employer-and-the-501(c)(3)-test (qualifying =
  federal / state / local / tribal government + 501(c)(3)
  + AmeriCorps / Peace Corps / public defender / public-
  health-corps; NOT 501(c)(4) advocacy nonprofits, NOT
  for-profit contractors to government, NOT partisan
  political; the employer must complete a PSLF Employment
  Certification Form (formerly Form 25 / W-9s; now combined
  ECF) and the PSLF Help Tool at StudentAid.gov is the
  workflow), employment-certification-cadence-as-the-
  hygiene-protocol (the community-default is to file an ECF
  *annually* AND every time the borrower changes employer;
  this prevents the year-9 surprise where MOHELA finds the
  employer non-qualifying and zeroes 8 years of work; the
  ECF is treated as the load-bearing procedural hygiene of
  PSLF), buyback-of-deferment-or-forbearance-months (the
  2024 PSLF Buyback program allows borrowers to "buy back"
  qualifying months from deferment / forbearance / non-IDR
  periods by paying the equivalent of what their IDR
  payment would have been during those months; this is
  particularly valuable for borrowers who were
  forbearance-steered by their servicer — a documented
  pattern in the 2010–2018 Navient / FedLoan era —
  Borrower-Defense-style relief is possible for the
  affected period), §108(f)(1)-tax-free-vs-IDR-25-year-
  taxable (the most powerful selling point of PSLF: the
  forgiveness is fully excluded from federal taxable
  income under §108(f)(1) — no tax bomb; non-PSLF IDR
  forgiveness is taxable absent ARPA extension; this means
  a $200k PSLF forgiveness is $200k of net benefit, vs
  $130k after-tax for the same balance forgiven via 25-year
  IDR — the tax-bomb math meaningfully changes the
  decision), career-flexibility-cost-as-the-real-trade-off
  (PSLF requires 10 years at a qualifying employer; a
  software engineer who could be earning $300k at a
  for-profit but is earning $130k at a 501(c)(3) is paying
  $170k/year × 10 years = $1.7M in lost comp for the
  PSLF benefit — which is often larger than the loan
  balance; PSLF makes sense when the borrower genuinely
  prefers public-service work AND has loans, NOT as a pure
  financial-optimization play; the community framing is
  "PSLF is a comp-floor for public-service careers, not a
  reason to take a public-service career"), Federal-Student-
  Aid-Ombudsman-as-escalation-channel (when MOHELA /
  Nelnet / EdFinancial fail to count qualifying payments
  correctly, file via the PSLF Help Tool → if denied,
  appeal in writing → if denied, file with the FSA
  Ombudsman Group → if still denied, escalate to the
  Student Loan Borrower Assistance Project / NCLC /
  Student-Loan Servicer Litigation cases pending in
  various district courts — this escalation ladder has
  been the operative path for most PSLF disputes since
  2018).
- **Sample situations**:
  - "Public defender, year 7 of PSLF, $180k balance, on
    PAYE. SAVE was supposed to lower my payment but is
    in administrative forbearance — those months are
    counting for PSLF but not for IDR-forgiveness, which
    is fine for me because PSLF will fire at year 10. Am
    I missing anything?"
  - "Government civil engineer, year 4 of PSLF, just got
    a private-sector job offer at $80k more. The 6
    remaining years of PSLF would forgive ~$160k; the
    private-sector comp delta over 6 years is $480k. Stay
    or leap?"
  - "501(c)(3) nonprofit researcher, 9 years in, just
    realized my employer was classified by MOHELA as
    501(c)(4) for 3 of those 9 years due to an employer
    name change. PSLF Buyback program available — what's
    the path to recover the 3 years?"

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the axes
  above cluster into ~10–12 reusable framings — federal-optionality-
  as-embedded-put-option, tax-bomb-arithmetic-and-sinking-fund,
  net-price-and-financial-aid-leverage, lost-income-as-the-largest-
  cost-of-graduate-school, 529-state-deduction-vs-flexibility,
  retirement-readiness-before-college-funding, FAFSA-base-year-and-
  asset-positioning, §127-exclusion-and-retention-clawback,
  §108(f)(1)-PSLF-tax-free-vs-IDR-taxable, custodial-account-
  EFC-drag-and-basis-transfer, SECURE-2.0-§126-529-to-Roth-
  rollover-15-year-clock, ARPA-tax-bomb-cliff-2025. Several of
  these have direct parallels in `personal-finance/framings.md`
  (asset-location, tax-bracket-arbitrage, retirement-account-
  contribution-ordering) — Triage's two-pass labeling should
  route cross-cutting situations to both domains rather than
  forcing a single primary.
- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  decisions 1, 4, 6, 8, 10 are highest-density. Refinancing
  federal away (1) erases optionality the borrower thought was
  cheap; the tax-bomb sinking fund on IDR (4) is the most
  systematically-missed liability; the 529-vs-Roth and parental-
  retirement-priority framing (6) is the highest-regret pattern
  in the community; FAFSA base-year-and-divorced-parent-of-record
  changes (8) are still poorly known 2+ years after the
  Simplification Act; PSLF employment-certification hygiene (10)
  is the load-bearing procedural difference between PSLF success
  and a year-9 surprise. Decision 1's federal-optionality
  erasure has the highest single-dollar tail risk per mis-step
  because it is permanent and irreversible (no re-federalization
  path exists).
- **Cross-domain edges**: 3, 4, 6, 8 boundary `personal-finance`
  (529-vs-Roth mix, asset location, tax-bracket arbitrage,
  retirement-account exclusion, SECURE 2.0 529-to-Roth rollover,
  kiddie-tax §1(g)); 2, 9 boundary `tech-career` (full-time-MBA-
  ROI on engineering tracks, §127 retention-clawback as golden-
  handcuffs); 3, 6, 8 boundary `family-planning` (529 inter-
  generational gifting, UGMA/UTMA basis transfer, divorced-parent
  FAFSA post-simplification, custodial-account drag); 7, 8
  boundary `housing` (HELOC-as-college-funding alternative,
  cash-out refi vs Parent PLUS, primary-residence non-reportable
  on FAFSA vs reportable on CSS Profile); 3, 8 boundary
  `entrepreneurship` (self-employed parent S-corp salary-vs-
  distribution affecting AGI / FAFSA EFC, business assets on CSS
  not FAFSA post-2024). Edges are documentation; routing across
  edges is V2-Triage's job.
- **High-stakes posture** (selective rather than uniform):
  `education-funding` is `high_stakes: false` per
  `_meta_ontology.md` §7 — most decisions are slow-clocked and
  reversible (refinance back to better rate, switch repayment
  plan, defer enrollment, transfer 529 beneficiary, take a leave
  of absence, file appeals, redo FAFSA in a subsequent year);
  Mechanism E uniform deferral is NOT applied. The Editor layer
  should NOT blanket-defer every decision to a professional.
  Selective referral is warranted for: decision 1 (refinancing
  decisions where PSLF or disability-discharge optionality is
  plausibly load-bearing — student-loan attorney / Student Loan
  Borrower Assistance Project), decision 3 (large 5-year-
  election lump-sums where Form 709 filing or state-deduction-
  recapture mechanics matter — retirement-experienced CPA),
  decision 4 (IDR borrowers with $150k+ balance needing
  tax-bomb sinking-fund design and Roth-conversion-coordination
  — CPA + fee-only fiduciary CFP), decision 5 (financial-aid
  appeal letters and merit-aid negotiation — NACAC-member
  college counselor; high-school counselor for dependent students),
  decision 6 (529-vs-Roth-vs-taxable-vs-UGMA mix where parental
  retirement readiness is itself in question — fee-only fiduciary
  CFP), decision 8 (CSS-Profile divorced-parent or business-asset
  reporting and professional-judgment appeals — financial-aid
  counselor + CPA), decision 10 (PSLF qualifying-employment
  disputes after a denied appeal; PSLF Buyback program filings
  — student-loan attorney / FSA Ombudsman Group as $0-cost
  escalation). The posture remains "decision-support framing
  rather than legal or financial advice"; the Editor surfaces
  the appropriate specific category inline rather than blanket-
  mandating one on every decision. Over-referral degrades signal;
  under-referral on the irreversible-decision (1) and the
  large-tail-risk decisions (4, 8, 10) creates harm. State Bar
  / SEC-FINRA BrokerCheck / NACAC-directory verification on any
  individual professional recommended is the $0-friction
  procedural floor — surfaced on every individual-professional
  referral. The FSA Ombudsman Group is uniquely a $0-cost
  escalation channel that should be tried before retaining
  paid counsel on servicer-dispute decisions (1, 4, 10). This
  selective-referral posture is the calibration that
  distinguishes `education-funding` from the uniformly-Mechanism-
  E-gated `personal-finance` / `health-insurance` / `immigration`
  / `family-planning` / `legal-disputes` domains, and mirrors
  the `housing` / `entrepreneurship` precedent.
