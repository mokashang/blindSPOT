# education-funding — framings.md (Layer 2)

Framing library for `education-funding`. Each entry names one lens — the
way a specific community / tradition / profession argues about a
student-loan, college-savings, graduate-school-ROI, financial-aid, or
loan-forgiveness decision — and lists the decisions from
[`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

The `education-funding` domain is **high_stakes: false** per
[`_meta_ontology.md` §7](../_meta_ontology.md). Unlike `personal-
finance` / `health-insurance` / `immigration` / `legal-disputes` /
`family-planning`, the Editor posture here is **decision-support
framing rather than uniform Mechanism E deferral**: most decisions are
slow-clocked and reversible on multi-year horizons — refinance back to
a better rate later, switch IDR plans, transfer 529 beneficiary, defer
enrollment, take a leave of absence, file appeals, redo FAFSA in a
subsequent year. The dollar swings are large but the irreversibility
profile is fundamentally different from `health-insurance` (12-month
plan-year lock-in + permanent Medicare late-enrollment penalty) or
`immigration` (out-of-status multi-year bans, missed filing windows
with no recovery). Selective Mechanism E referral applies only to the
**six-figure tail-risk pockets** enumerated in
[`decisions.md` §Notes](./decisions.md): D1 (refi-vs-IDR/PSLF
optionality erasure — student-loan attorney / SLBA / FSA Ombudsman),
D3 (529 5-year-forward §529(c)(2)(B) lump-sum + Form 709 + state-
deduction recapture — retirement-experienced CPA), D4 (IDR + tax-bomb
sinking-fund + Roth-conversion-coordination — student-loan attorney /
fee-only fiduciary CFP), D7 (Parent PLUS vs federal-direct vs private
cosigner mechanics — fee-only CFP / consumer-protection / student-loan
attorney), D10 (PSLF qualifying-employment + employment-certification
+ Buyback program — student-loan attorney / FSA Ombudsman / SLBA).
Where a framing names a statute, rule, threshold, or form (IRC
§529(c)(2)(B) 5-year-forward election, IRC §117(a) qualified-
scholarship exclusion, IRC §127 employer-provided-education exclusion
$5,250, IRC §132(d) working-condition-fringe, IRC §25A AOTC/LLC, IRC
§108(f)(1) PSLF-tax-free, IRC §108(a)(1)(B) insolvency exclusion, IRS
Form 982 insolvency, Form 709 gift-tax return, Form 1098-T, Form
1099-C, SECURE 2.0 §126 529-to-Roth 15-year clock, ARPA §9675 student-
loan-forgiveness-exclusion-through-2025, HEA §437(a) death-and-
disability discharge, HEA §455(m) PSLF, HEA §455(h) Borrower Defense,
HEA §479A professional-judgment authority, FAFSA Simplification Act of
2020 parent-of-record rule, the 8th Circuit SAVE injunction, IRC §1(g)
kiddie-tax, IRC §121 §1031 N/A-analog-but-referenced-by-housing-edge),
treat the citation as a pointer to where the analysis happens, not as
the answer.

Two distinct classes of irrevocability drive the education-funding
framing structure and shape every framing below, mirroring the
structure in [`decisions.md`](./decisions.md):

- **Federal-to-private refi as one-way door**: refinancing federal
  loans to a private lender permanently erases IDR / PSLF / SAVE /
  death-and-disability-discharge under HEA §437(a) / Borrower Defense
  under HEA §455(h) / in-school deferment / military and Peace Corps
  deferment / income-driven-forgiveness-after-20-25-years. There is no
  re-federalization path — Direct Consolidation can combine federal
  loans but cannot pull a private loan back into federal status. The
  rate-spread savings the borrower captures in the refi are
  recoverable (rates can be refinanced again later); the federal-
  optionality erasure is not. This shapes framings F1 (federal-
  optionality-put-option), F8 (forbearance-aware), F11 (consumer-
  advocate-anti-refi).
- **Tax-clock-and-election-window one-shot windows**: the §529(c)(2)(B)
  5-year-forward election requires Form 709 filing in the election
  year even though no gift tax is owed; failure to file Form 709 means
  the contribution isn't formally elected and any death within the
  5-year window causes the unspent portion to claw back into the
  donor's estate (anti-purpose of the strategy). The base-year-prior-
  prior-year rule on FAFSA / CSS means an AGI-inflating event (Roth
  conversion, capital-gains harvest, business sale, RSU vest) two
  years before college start is the action the family didn't realize
  was load-bearing. The SECURE 2.0 §126 15-year-clock on 529-to-Roth
  rollovers means a 529 funded in 2025 cannot roll until 2040 — a
  decade-plus runway the financial press oversold when the law passed.
  ARPA §9675's tax-bomb exclusion sunsets end-of-2025 absent extension;
  IDR borrowers reaching forgiveness in 2026+ face full ordinary-
  income inclusion. These timing-clocks shape framings F2 (529-
  state-deduction-and-flexibility), F5 (FAFSA-base-year-positioning),
  F6 (529-to-Roth-flexibility-hedge), F7 (tax-bomb-sinking-fund), F12
  (ARPA-cliff-aware).

Framings that handle one class well often miss the other; the
opposing-framing pairs at the end of this file frequently divide along
the refi-permanence / tax-clock-window boundaries.

Voice anchors (conceptual, not source URLs — those live in
`sources.yaml` once authored): **PSLF-preservation / student-loan-
attorney voice** (r/PSLF, Heather Jarvis Student Loan Expert, Student
Loan Borrower Assistance Project / National Consumer Law Center, FSA
Ombudsman Group — federal-optionality-pilled, "do not refi federal if
there is any plausible PSLF path or any household member with elevated
disability risk", treats every refi-quote as the borrower buying down
a put option whose strike they don't price); **r/StudentLoans /
r/StudentLoansHelp voice** (Reddit subreddits, transactional and
peer-driven, vocabulary of "IBR", "PAYE", "SAVE", "ECF", "MOHELA
underreported my count", "the buyback program", "account adjustment"
— skews toward forbearance-steering-trauma and servicer-distrust);
**ROI-by-major voice** (Georgetown CEW college-payoff studies,
Burning Glass / Lightcast labor-market data, Payscale, BLS
Occupational Employment & Wages, Bureau of Labor Statistics earnings-
by-degree, "college ROI is the wage premium minus the all-in cost"
ethos, treats school choice as program-choice not prestige-choice);
**Bogleheads-college voice** (Bogleheads forum college-funding
threads, Mike Piper / Open Social Security analogues for college
funding, opportunity-cost-pilled, "the 529 is one tool in an asset-
location stack", treats the question as a portfolio allocation
problem); **personal-finance-blogger voice** (The College Investor,
SavingForCollege, Mark Kantrowitz, MoneyGuy Show — tactical, cadence-
and-vehicle-aware, "front-load the 529 with the 5-year-forward
election if the gift exclusion supports it"); **FIRE-aware-college-
funding voice** (r/financialindependence college threads, Mr. Money
Mustache "MMM University" essays, ChooseFI college episodes —
retirement-priority-pilled, "your kids can borrow for college, you
can't borrow for retirement", treats the parental-retirement-readiness
question as load-bearing for the college-funding cadence); **NACAC-
counselor voice** (National Association for College Admission
Counseling members, NACAC ethics statement, high-school college-
counseling office voice, "the merit-aid letter is the opening offer,
not the closing offer" ethos, treats the financial-aid award as
negotiable on cross-admits between peer schools); **financial-aid-
office voice** (NASFAA, AACRAO, professional-judgment authority under
HEA §479A, "we have a discretionary appeal budget; it gets used by
people who ask" ethos, treats appeal letters as the principal lever
for need-based-aid adjustment after a job loss or family-financial-
change); **r/financialaid / r/ApplyingToCollege voice** (Reddit
subreddits, applicant- and parent-driven, vocabulary of "EFC", "SAI",
"CSS Profile", "Princeton Net Price Calculator", "professional
judgment appeal", "demonstrated need", "need-aware", "need-blind",
"yield protection" — skews toward applicant-side strategy and
admissions-anxiety); **fee-only-CFP / NAPFA voice** (NAPFA-affiliated
financial planners, AUM-free fee structure, treats the 529-vs-Roth-
vs-taxable mix as part of the household financial plan, prioritizes
parental retirement readiness over kids' college over the highest-
regret pattern); **retirement-experienced-CPA voice** (CPAs with §25A
/ §127 / §529 / SECURE 2.0 §126 history, treats 529 state-deduction
recapture rules and AOTC/LLC interaction with 529 distributions as
the load-bearing tax-arbitrage that generic 1040-prep CPAs miss);
**MBA-admissions / Poets&Quants voice** (MBA-aspirant community,
Poets&Quants rankings, GMAT Club forums, Wall Street Oasis, treats
full-time-MBA as a credential-and-network purchase whose ROI varies
sharply by pivot type — finance / consulting / general-management
positive, engineering-to-PM modestly-negative, engineering-staying-
engineering highly-negative); **r/MBA / r/business voice** (Reddit
peer voice on MBA-vs-stay-in-job, less rankings-driven, more lived-
experience cost-vs-comp); **engineering-pivot voice** (Levels.fyi,
Blind app, r/cscareerquestions — "L5 at $380k considering MBA; how
do the numbers shake out", treats MBA-tuition + 2-year opportunity
cost in tech compensation as the dominant cost line, often dwarfing
sticker price); **immigration-aware-MS-CS voice** (H-1B-cap-exempt
master's, OPT extension on STEM, r/cscareerquestions / r/csMajors
immigration threads — for international students the MS-CS calculus
includes visa pathway value that domestic framings miss; cross-
routes `immigration`); **consumer-protection voice** (CFPB, NCLC,
SLBA, state attorneys general, the 2022–2024 IDR account-adjustment
consent decrees — "the servicer is not your friend; document
everything; the systematic forbearance-steering pattern is a
documented violation"); **employer-tuition voice** (corporate HR /
employee-development teams, Glassdoor employer-reviews on tuition-
reimbursement programs, "the $5,250 §127 cap is the easy part; the
2–4 year retention clawback is the part nobody reads before signing
up"); **bankruptcy-discharge voice** (post-*Brunner* / post-*Frost* /
2022 DOJ-USDOE attestation-guidance-shift, NACBA bankruptcy
attorneys, "the undue-hardship bar has softened but remains highly
fact-specific"); **HELOC-as-college-funding voice** (`housing` cross-
edge, mortgage-broker / fee-only-CFP voice, "HELOC at prime + small
spread can undercut Parent PLUS by 100–300bp but trades home-equity
risk for federal-protection erasure"); **SECURE-2.0-§126 voice**
(Mike Piper, Mark Kantrowitz, fee-only-CFP analyses — "the
15-year-clock on 529-to-Roth means a 529 funded in 2025 cannot roll
until 2040, the financial press oversold the mechanic when the law
passed").

Cross-domain edges: D1, D4, D6, D7, D10 boundary `personal-finance`
(opportunity-cost-of-debt-payoff-vs-invest, asset location across 529
/ Roth / taxable / UGMA-UTMA / Coverdell, kiddie-tax §1(g), SECURE
2.0 §126 529-to-Roth-rollover, retirement-account-exclusion-from-
FAFSA-and-CSS, Roth-conversion-in-low-income-year-as-tax-bomb-
bracket-management); D2, D9 boundary `tech-career` (full-time-MBA-
ROI for engineers vs finance/consulting pivots, MS-CS at top-10 as
H-1B-cap-exempt route, §127 employer tuition reimbursement
retention-clawback as golden-handcuffs); D1, D2, D10 boundary
`entrepreneurship` (1099-vs-W-2 PSLF-qualifying-employment
asymmetry — only W-2 employment at a qualifying employer counts;
self-employed contractors at a 501(c)(3) do NOT qualify even though
the employer does; this is one of the most-missed PSLF mechanics for
former-contractor founders; LLC-as-parent for 529-front-loading
estate-planning); D3, D6, D8 boundary `family-planning` (529 inter-
generational gifting and grandparent-529-FAFSA-post-simplification
removed trap, UGMA/UTMA basis transfer, divorced-parent-of-record
under FAFSA Simplification Act, custodial-account drag); D7, D8
boundary `housing` (HELOC-as-college-funding-alternative,
cash-out-refi-vs-Parent-PLUS, primary-residence non-reportable on
FAFSA but reportable on CSS Profile at many schools); D2 boundary
`immigration` (international-student MS-CS calculus, H-1B-cap-exempt
master's, F-1 / J-1 status interactions with 529 / federal-aid
eligibility); D1, D4, D10 boundary `legal-disputes` (loan-discharge
§108(f) tax-bomb mechanics, PSLF-temporary-rules-litigation,
servicer-error and forbearance-steering remediation under the
2022–2024 IDR / PSLF account-adjustment consent decrees, post-
*Brunner* / post-*Frost* / 2022 DOJ-USDOE attestation-guidance
bankruptcy-discharge framing). Routing across edges is V2-Triage's
job; the edge annotations here help framings name adjacent domains
rather than absorb their content.

---

## F1: Federal-optionality-as-embedded-put-option framing

**Decisions applied to:** D1 (Refi vs preserve federal optionality),
D4 (IDR + tax-bomb vs 10-year standard), D7 (Parent PLUS vs private
with cosigner), D10 (PSLF qualification).

**Mental model.** A federal student loan is a debt instrument
*bundled* with a portfolio of embedded options: an IDR-driven payment
cap that activates on adverse-income shocks (an income-contingent put
on disposable income), a PSLF-forgiveness call on 10 years of public-
service employment, a 20–25-year IDR-forgiveness call on long-duration
balance, a death-and-disability discharge under HEA §437(a) that is
effectively a term-life policy with the borrower as insured, in-school
deferment for graduate school returns, military and Peace Corps
deferment, and Borrower Defense to Repayment under HEA §455(h) for
school-fraud claims. The borrower paying federal rates is paying a
spread above private rates that *capitalizes* the option value of this
bundle. Refinancing federal-to-private converts the bundle to a plain
debt instrument at lower nominal rate — recovering some annual
interest expense and surrendering all of the optionality. The
community heuristic is: "do not refi federal if there is any plausible
PSLF path or any household member with elevated disability risk." The
options are NOT free even when the borrower doesn't expect to exercise
them — they price the *probability-weighted* tail outcomes (layoff,
disability, career pivot to nonprofit, return to school, death) that
the borrower's nominal-rate framing doesn't surface. Voice: PSLF-
preservation / student-loan-attorney voice, r/PSLF, SLBA / NCLC, FSA
Ombudsman Group.

**Characteristic vocabulary:**
- "federal optionality"
- "the put option you don't see"
- "do not refi federal"
- "PSLF path"
- "death-and-disability discharge under §437(a)"
- "income-driven safety net"
- "the rate spread is the option premium"
- "Borrower Defense"
- "in-school deferment value"
- "re-federalization is not available"

**Excludes:**
- Frames every federal borrower as having latent option value even
  when the realistic option-exercise probability is near zero (high-
  income tech worker with stable career, no public-service or grad-
  school plausibility, no household-disability risk). The framing's
  reflex "never refi federal" leaves a $3–5k/year interest expense on
  the table for borrowers whose option-value is genuinely
  near-zero. Opposes F4 (rate-spread-arithmetic). Doesn't see when
  the option bundle is out-of-the-money for the specific borrower.
- Treats SAVE-current-status as if it were a permanent feature when
  it's currently in administrative forbearance under the 8th Circuit
  injunction, with months counting for PSLF but NOT for IDR-
  forgiveness — borrowers planning around SAVE's 5%-discretionary-
  income cap on undergrad are planning around a plan that may not
  exist at forgiveness time.
- Under-weights the political-risk dimension: federal-loan-program
  features (PSLF eligibility, IDR-forgiveness terms, SAVE-mechanics,
  ARPA §9675 tax-bomb exclusion) are subject to administrative-rule
  changes and statutory amendments. The framing's "the federal
  bundle protects you" misses that the bundle's terms can change
  underneath the borrower, especially on long-horizon (20–25 year)
  IDR-forgiveness paths.
- Doesn't price the *behavioral* cost of holding a federal balance
  for 20+ years at non-amortizing IDR — the balance grows on paper,
  servicer statements show the running interest accrual, and
  borrowers report psychological drag from "the balance going up
  every month even though I'm paying." This is real even when the
  arithmetic forgiveness math says hold. Opposes F4.
- Frames death-and-disability discharge under §437(a) as if every
  family-member-disability triggers discharge; it actually requires
  the *borrower's own* total and permanent disability (TPD) certified
  by a physician, the VA, or 3+ years SSDI — not a spouse / child /
  parent disability. The framing's "elevated disability risk"
  heuristic over-counts the protection's actual coverage.

## F2: 529-state-deduction-and-tax-deferral framing

**Decisions applied to:** D3 (Front-load 529 5-year-forward vs
annual vs Roth-substitute), D6 (529 vs Roth vs taxable vs UGMA/UTMA
vs Coverdell mix), D9 (Employer §127 vs scholarship-stacking vs
self-pay, sub-edge: 529-distribution-coordinated-with-§127).

**Mental model.** The 529 is the strongest tax-advantaged vehicle for
qualified-higher-education expenses available to most households:
state-income-tax deduction on contribution (varies by state — $10k/
year MFJ in NY, $5k/year MFJ in IL, unlimited in some states,
nothing in CA / NJ / others), tax-free growth, tax-free qualified
distribution for tuition / fees / books / room-and-board / computer-
and-tech-equipment / K-12 tuition up to $10k/year per beneficiary
under TCJA, plus the SECURE 2.0 §126 529-to-Roth rollover after the
15-year clock. The §529(c)(2)(B) **5-year-forward election** allows
front-loading 5× the annual gift-tax exclusion ($95k single / $190k
MFJ for 2026) by treating the contribution as 5 ratable annual gifts,
useful for grandparents using the lifetime-estate-exemption before
the 2026 sunset and for parents maximizing tax-deferred growth. The
framing's reflex on every funding decision: (a) what's the household
state-deduction value at the margin, (b) is the runway long enough
that tax-deferred-growth compounds meaningfully (18-year horizon at
7% real growth ~3.4×, 10-year ~2.0×), (c) does the state plan have
deduction-recapture rules on out-of-state rollover that lock in the
deduction. Voice: SavingForCollege / Mark Kantrowitz / personal-
finance-blogger / retirement-experienced-CPA voice.

**Characteristic vocabulary:**
- "state-deduction value"
- "5-year-forward election"
- "Form 709"
- "deduction recapture"
- "best plan vs best-for-me plan"
- "tax-deferred growth"
- "qualified distribution"
- "expense-ratio drag"
- "in-state plan"
- "K-12 distribution cap $10k"

**Excludes:**
- Treats the 529 state-deduction as if it were the dominant
  consideration when for households in deduction-less states (CA,
  NJ, MA, several others) or with state-deduction caps below
  realistic contribution levels (IL $20k/MFJ, AZ $4k/MFJ), the
  deduction-arbitrage is small enough that expense-ratio drag and
  investment-option quality dominate. The framing's "stay in-state
  for the deduction" can leave the household in a poor-performing
  plan (Bright Start vs Utah's my529) when the deduction value is
  trivial. Opposes F6 (529-to-Roth-flexibility-hedge), F10 (FIRE-
  retirement-priority).
- Doesn't see that the §529(c)(2)(B) 5-year-forward election
  requires Form 709 filing in the election year *even though no gift
  tax is owed* — this is the most-missed mechanic of the strategy;
  failure to file means the contribution isn't formally elected and
  death within the 5-year window causes the unspent portion to claw
  back into the donor's estate. The framing's "5-year-elect and
  forget" rhetoric leaves the strategy incomplete.
- Under-weights the leftover-529 problem: if the kid skips college,
  goes to a cheaper school, gets full-ride scholarships, or finishes
  early, the unspent 529 balance faces 10% penalty + ordinary-income
  tax on earnings unless rolled to a sibling beneficiary, used for
  K-12 ($10k/year cap), used for graduate-school later, or rolled
  to a Roth (SECURE 2.0 §126, capped at $35k lifetime with 15-year-
  clock). Over-funded 529s are a real regret pattern in the wild.
  Opposes F10.
- Glosses over state-deduction recapture rules on out-of-state
  rollover: most states with a 529 deduction recapture the deduction
  if you roll out to another state's plan; some (NY, IL) allow tax-
  free in-state-to-in-state transfers but recapture on out-of-state
  rollover; this is the load-bearing reason to pick a state plan
  over a "best" Utah/Nevada plan when the state-deduction value
  exceeds the expense-ratio drag, AND the load-bearing trap when
  the household later moves states.
- Frames grandparent-529 as if it were superior to parent-529
  post-FAFSA-Simplification across the board; in fact, grandparent-
  529 distributions are NOT reported as student income on the new
  FAFSA, but on the CSS Profile they often still are (depends on
  the school's CSS treatment). For families with CSS-Profile-school
  applications, the grandparent-529 advantage is school-by-school,
  not universal.

## F3: ROI-by-major / program-not-school framing

**Decisions applied to:** D2 (Graduate school ROI), D5 (In-state
public vs out-of-state private with merit aid).

**Mental model.** The single most decision-relevant variable in
school-choice is *program-of-study × school-tier × all-in net cost*,
NOT the school's overall US News ranking. The College Scorecard
publishes program-level median earnings, median federal debt at
graduation, and 3-year-cohort-default-rate for every federally-
funded program — engineering at a flagship public ($65k median
starting salary) often out-earns liberal-arts-at-a-ranked-private
($42k median), and the wage premium is driven by program / major
rather than school name. Georgetown CEW's "Five Rules of the College
and Career Game" report and Burning Glass / Lightcast labor-market
data confirm: pre-professional and STEM programs have weaker
school-effects than generalist humanities / social sciences;
"college pays" is true for ~83% of programs and *false* for the
remaining 17% (mostly for-profit, online-only, and low-selectivity
private programs). For graduate school, the framing extends: MBA at
M7 / T15 delivers positive NPV for finance / consulting / general-
management pivots; MBA for engineering-to-PM is modestly-negative
because the same pivot is available internally; MBA for engineering-
staying-engineering is highly negative. MS-CS at top-10 unlocks
FAANG interviews and research-eligibility; MS-CS at non-top is a
credential negative. Voice: ROI-by-major / Georgetown CEW / Burning
Glass / Payscale / BLS Occupational Employment & Wages voice.

**Characteristic vocabulary:**
- "median earnings by program"
- "College Scorecard"
- "Georgetown CEW"
- "wage premium net of debt"
- "the program is the school"
- "starting salary by major"
- "10-year earnings trajectory"
- "MBA NPV by pivot type"
- "M7 / T15"
- "cohort default rate"

**Excludes:**
- Treats published median earnings as the relevant statistic when
  the distribution is highly skewed for many programs (CS, finance,
  consulting outcomes are bimodal — top-tier vs everyone-else). The
  median-MBA-finance-comp framing hides that "MBA pays" is a
  statement about the top decile, not the median graduate. Opposes
  F9 (consumer-protection-anti-debt).
- Doesn't surface the *option value* of a non-vocational degree —
  philosophy / English / history majors who go into law, consulting,
  or graduate school have outcomes that don't show up in 4-year
  post-graduation earnings data. The framing's "humanities lose
  money" is true on the 4-year window and often false on the
  20-year window for the subset who pivot to professional school.
- Under-weights the *negative* selection in non-completion rates:
  the framing's "engineering at flagship public out-earns liberal-
  arts-at-ranked-private" is true *conditional on completion*; the
  4-year graduation rate at flagship publics is often 50–65% vs
  85–95% at ranked privates, and the failure-to-complete cost
  (1–2 years of debt with no degree) is the highest-regret pattern
  in the lower-completion-rate tail. The framing's medians are
  conditional on completion in a way the asker doesn't see.
- Frames "ROI by program" as if program-of-study were a free
  choice; many applicants are admitted to a specific college on
  the basis of an intended major, and changing majors after
  enrollment is not always free (capacity-constrained majors at
  flagship publics — CS at UW, engineering at UT-Austin, business
  at UMich — gate internal transfer with GPA cuts and waitlists).
  The framing's "pick the high-ROI program" understates the
  admissions-side constraint.
- Doesn't see that for international students, the program-level
  ROI calculation has to include visa-pathway value — MS-CS at a
  top-10 US program unlocks H-1B-cap-exempt-master's-cap routes
  and 3-year STEM-OPT extension; the domestic-framing earnings
  data understates the immigration-option value materially for
  this population. Cross-routes `immigration`.

## F4: Rate-spread-arithmetic framing

**Decisions applied to:** D1 (Refi vs preserve optionality), D7
(Parent PLUS vs federal direct vs private with cosigner).

**Mental model.** Student-loan debt is just debt; the cost of
servicing it is the interest rate × balance × time. A 200bp rate
spread on a $150k balance is ~$3,000/year of interest savings; on a
$280k balance, $5,600/year. Compounded over a 10-year repayment
horizon, the savings are substantial. For borrowers with high credit
scores (FICO 760+), high income (top quartile professional comp),
and stable employment (no plausible PSLF path, no household
disability risk), the rate-spread framing argues the federal
optionality bundle is out-of-the-money — the borrower will never
exercise IDR / PSLF / forgiveness / discharge, so paying a 200bp
premium for options they won't use is wasteful. Private refi at SoFi
/ Earnest / ELFI / Splash / Laurel Road for radiologists / dentists /
lawyers / senior software engineers at top-credit-tier pricing
routinely shaves 150–250bp off the federal-weighted-average rate.
The framing's reflex on every refi decision: model the household's
actual probability-weighted option-exercise scenarios; if the
probability is genuinely near-zero, capture the rate spread. The
framing also covers the federal-direct-vs-Parent-PLUS-vs-private
mix on origination: federal direct subsidized + unsubsidized are
the cheapest capital, Parent PLUS is at a 1.5–2.5% premium with
4.228% origination fee, private with strong cosigner credit is
routinely 200–400bp below Parent PLUS at the cost of federal
protections. Voice: SoFi / Earnest / ELFI / personal-finance-
blogger refi-promoting voice; r/personalfinance debt-payoff
threads.

**Characteristic vocabulary:**
- "rate spread"
- "200bp savings"
- "break-even on refi"
- "credit-tier pricing"
- "weighted-average rate"
- "the math is the math"
- "ARM-equivalent for refi"
- "fixed vs variable"
- "private rate quote"
- "cosigner release"

**Excludes:**
- Doesn't see that the rate-spread framing presumes the borrower
  can accurately model their probability of option-exercise — most
  borrowers under-estimate layoff probability, disability-onset
  probability, career-pivot-to-nonprofit probability, and family-
  emergency probability over 20-year horizons. The community
  heuristic from F1 ("do not refi federal if any plausible path")
  exists *because* personal probability-estimation is systematically
  optimistic on these dimensions. Opposes F1 (federal-optionality).
- Treats private-refi rate quotes as if they were permanently
  available; private lenders re-rate hard on income change at
  refi-cycle so the "I'll just refi again if rates fall" assumption
  is fragile — the same SoFi 800+ FICO borrower at $400k AGI gets
  rejected for refi at $80k AGI post-layoff. The rate-spread
  framing's optionality on future-refi is itself path-dependent on
  income stability. Opposes F1.
- Under-weights the cosigner-asymmetry on private undergrad refi:
  most private refis allow cosigner-release after 12–48 months of
  on-time payments but require a re-underwrite that can fail if
  income has dropped — material for borrowers whose parent
  cosigned and wants release. The rate-spread framing's "private
  beats PLUS by 200bp" misses that the parent-cosigner-trap on
  private is structurally different from Parent-PLUS-in-parent's-
  name (which discharges on parent death under §437(a) — private
  cosigner debt typically does not).
- Misses ARPA §9675's tax-bomb-exclusion-sunset (end-of-2025) for
  IDR borrowers: a borrower currently on IDR planning the rate-
  spread refi comparison "in case the IDR-forgiveness math
  improves" is comparing against an IDR-forgiveness scenario that
  may include $50k+ of unplanned tax liability post-2025 absent
  ARPA extension. The rate-spread framing's IDR-alternative
  calculation under-prices the tax-bomb cliff.
- Glosses over SAVE-administrative-forbearance treatment of months
  for IDR-forgiveness (those months count for PSLF but NOT for
  IDR-forgiveness counting purposes); a borrower comparing rate-
  refi against "stay on SAVE and forgive in year 20" is comparing
  against a year-20 that may slip to year 22-23 once the SAVE
  litigation resolves and counts are re-baselined.

## F5: FAFSA-base-year-and-asset-positioning framing

**Decisions applied to:** D8 (FAFSA / CSS Profile asset positioning
and base-year timing), D6 (Vehicle-mix where FAFSA reporting
treatment differs across 529 / Roth / taxable / UGMA), D3
(Grandparent-529 vs parent-529 post-Simplification).

**Mental model.** Financial aid is an *administrative game*
played against the FAFSA / CSS Profile formula, with the family's
reportable assets, AGI, and family size as the inputs. The base year
is the prior-prior tax year — for 2025–26 awards, 2023 tax year is
the input — which means strategic Roth conversions, capital-gains
harvests, business sales, and large bonus events should be made
*before* the base year starts to avoid inflating reported income at
the FAFSA cliff. Retirement-account balances (401k, 403b, IRA, Roth)
are excluded from both FAFSA and CSS, creating a powerful incentive
to maximize retirement-contribution in the pre-base-year window.
Parent-owned 529 is 5.64% drag; UGMA/UTMA is 20% drag (student
asset); transferring appreciated UGMA/UTMA assets to a custodial-529
in the same beneficiary's name in early-to-mid teen years converts
drag from 20% to 5.64% — but only if the unrealized gain is small
enough that kiddie-tax §1(g) + LTCG cost is less than the FAFSA-drag
savings. The FAFSA Simplification Act of 2020 changed parent-of-
record from custodial-by-time to *higher-income-of-the-two* parents
in divorce (since 2024–25 award year), removed small-business assets
from FAFSA reporting, and removed grandparent-529 distributions from
student-income — three changes still poorly known 2+ years out.
HEA §479A grants financial-aid offices discretionary "professional
judgment" authority to adjust FAFSA / CSS data elements for special
circumstances; this is the appeal lever. Voice: r/financialaid /
r/ApplyingToCollege / Princeton Net Price Calculator / NACAC-
counselor / NASFAA / financial-aid-office voice.

**Characteristic vocabulary:**
- "base year"
- "prior-prior year"
- "EFC / SAI"
- "5.64% drag"
- "20% student-asset drag"
- "professional judgment appeal"
- "Net Price Calculator"
- "CSS Profile vs FAFSA"
- "demonstrated need"
- "parent of record"

**Excludes:**
- Treats CSS Profile schools as if they shared FAFSA reporting
  rules; in fact CSS counts home equity (often capped at 1.2–2.4×
  income at some schools, uncapped at others), counts small-
  business assets that FAFSA doesn't since 2024, asks divorced
  non-custodial-parent income separately (most CSS schools require
  the non-custodial-parent CSS unless formally waived), and treats
  retirement-account *contributions* in the base year as
  add-back-to-AGI in some cases — the framing's "FAFSA strategy"
  can hand back the win at CSS schools the family also applies to.
  Opposes F7 (NACAC-counselor on cross-admit-negotiation when CSS
  EFC drives the conversation).
- Under-weights the *base-year-of-prior-prior-year* on the *back
  end* of college: the FAFSA submitted for the senior-year award
  uses tax-year sophomore-year as the base year, which means an
  AGI-inflating event in the sophomore-year tax-year matters for
  the senior-year award. The framing's "pre-base-year planning"
  applies to the front-of-college decisions but the same logic
  applies to each subsequent year's award; many families do the
  planning once and forget the recurrence.
- Doesn't see that the FAFSA Simplification Act's removal of
  small-business assets from FAFSA reporting created a *deceptive*
  optimization — many CSS schools still ask, and self-employed-
  parent (S-corp distribution-vs-salary, schedule-C net income)
  reporting on CSS is unchanged from pre-Simplification. Self-
  employed parents who relax their CSS asset disclosure thinking
  "FAFSA doesn't ask anymore" are mis-reading the rule. Cross-
  routes `entrepreneurship` (S-corp salary-vs-distribution affects
  AGI on both FAFSA and CSS).
- Glosses over the *retirement-account-contribution add-back* on
  CSS Profile: many CSS schools add 401k / IRA / Roth contributions
  in the base year back into available income — the FAFSA strategy
  of "max retirement contributions in pre-base-year" can still
  reduce CSS reported income but the strategy of "make a large
  401k contribution IN the base year to lower reported AGI"
  doesn't work at most CSS schools.
- Frames professional-judgment appeals as if they were universally
  available; in fact §479A authority is discretionary per
  financial-aid office, and the appeal-success rate varies
  significantly by school's institutional-aid budget and the
  specific change-in-circumstance documented. The framing's
  "appeal and you'll get adjusted" oversells the success rate at
  schools with constrained institutional-aid budgets.

## F6: 529-to-Roth-flexibility-hedge / SECURE-2.0-§126 framing

**Decisions applied to:** D3 (Front-load 529 5-year-forward vs Roth-
substitute), D6 (529 vs Roth vs taxable mix), D4 (tax-bomb sinking
fund as Roth-conversion-ladder candidate).

**Mental model.** SECURE 2.0 §126 (effective 2024) allows a 529 with
at least 15 years of seasoning to roll up to $35k *lifetime* into a
Roth IRA in the *beneficiary's* name, subject to the annual-Roth-
contribution limit (so the $35k takes ~5 years at current $7k limit
to fully convert), the beneficiary having earned income equal to the
rollover amount, and the 5-year-clock on recent contributions (no
rollover from contributions made within the past 5 years). The
mechanism partially closes the "what if kid doesn't go to college"
gap that historically pushed parents toward Roth-as-college-funding-
substitute or taxable brokerage. The framing's reflex: 529 + 15-year-
seasoning + leftover-conversion-to-Roth is a *long-clock* partial-
flexibility hedge. A 529 funded heavily in 2025–2027 cannot roll
until 2040–2042; this is NOT a near-term flexibility solution. Roth
IRA as direct college-funding-substitute remains useful for parents
who don't qualify for state-deduction and want full flexibility, but
the $7k/year contribution limit caps the strategy. The framing also
extends to the tax-bomb sinking-fund question (D4): a Roth-
conversion-ladder in low-income years (sabbatical, leave-of-absence)
is a tax-bomb-bracket-management tool that the IDR-tax-bomb-arithmetic
framing under-prices. Voice: Mike Piper / Mark Kantrowitz / fee-only-
CFP voice; SavingForCollege analyses post-SECURE 2.0.

**Characteristic vocabulary:**
- "15-year clock"
- "SECURE 2.0 §126"
- "$35k lifetime cap"
- "5-year recent-contribution lockout"
- "Roth-as-substitute"
- "beneficiary's earned income"
- "annual Roth contribution limit"
- "leftover 529 hedge"
- "Roth-conversion ladder"
- "low-income-year conversion"

**Excludes:**
- Oversells the SECURE 2.0 §126 rollover's near-term value;
  financial press routinely treats it as "529 now has Roth
  flexibility" when the 15-year-clock means a 529 funded in 2025
  cannot roll until 2040 at the earliest, the $35k cap is small
  relative to typical college-funding shortfalls, the annual-Roth-
  limit constraint means even fully-converting $35k takes 5+ years,
  and the beneficiary-earned-income requirement excludes
  beneficiaries who are full-time students with no earned income.
  The framing's "use it as a hedge" is technically correct but the
  hedge value is much smaller than the press coverage suggests.
- Doesn't see the *5-year recent-contribution lockout*: contributions
  made within the past 5 years cannot be rolled — so a parent who
  funded $50k into a 529 in years 1-3 of beneficiary's life and
  then waits 15 years and tries to roll the leftover finds that
  any contributions made in years 11-15 of seasoning (within 5
  years of the rollover) are locked out. The framing's "fund early,
  roll later" works only when contributions stopped 5+ years before
  rollover.
- Treats Roth-IRA-as-college-funding-substitute as if Roth-
  contribution-withdrawal were costless; withdrawing Roth
  *earnings* before 59.5 (even for qualified education expenses)
  incurs 10% penalty on earnings absent the §72(t) education-
  expense exception (which waives the penalty but NOT the income
  tax on earnings). The framing's "Roth is flexible" understates
  the earnings-side tax treatment for under-59.5 distributions.
- Under-weights the IRC §25A AOTC/LLC interaction with 529 and
  Roth distributions: the same dollar of qualified-education-
  expense cannot be used both to claim the AOTC and to justify a
  tax-free 529 distribution — the family must coordinate which
  expense dollars get attributed to the credit and which to the
  529. Many families discover the coordination requirement
  retroactively at tax-filing time when the §25A claim is denied.
- Glosses over the state-tax treatment of the 529-to-Roth rollover:
  several states (NY, IL, NC, AR) explicitly recapture the original
  529-contribution state-deduction when the rollover happens
  treating it as a non-qualified distribution; the federal-tax-free
  rollover does not protect against state-level recapture.

## F7: NACAC-counselor / financial-aid-negotiation framing

**Decisions applied to:** D5 (In-state public vs out-of-state
private with merit aid), D8 (Professional-judgment appeals).

**Mental model.** Merit aid and need-based aid are not fixed at the
initial award letter — the financial-aid office has discretionary
authority under HEA §479A to adjust data elements for special
circumstances (job loss, divorce mid-process, medical-expense,
business loss), and merit-aid letters are routinely treated by
admissions / financial-aid offices as the *opening offer*, with
formal "additional consideration" mechanisms when the applicant
presents a comparable offer from a peer institution. The framing's
reflex on every cross-admit decision: write the appeal letter, name
the peer offer, attach the supporting documentation (severance
letter, divorce decree, medical bills, school-aid-letter from
competitor), and ask. NACAC member counselors (high-school college-
counseling offices, NACAC-affiliated independent counselors) treat
the appeal as routine. The community-default "the worst they can say
is no, and they often say yes" is grounded in the structural reality
that most enrollment offices have a discretionary "professional
judgment" budget that goes underutilized — most applicants don't
ask. Voice: NACAC-counselor / NASFAA / financial-aid-office /
r/ApplyingToCollege voice; NACAC ethics statement on appeal
mechanics.

**Characteristic vocabulary:**
- "appeal letter"
- "professional judgment"
- "cross-admit leverage"
- "peer institution offer"
- "additional consideration"
- "demonstrated need"
- "merit-aid negotiation"
- "the opening offer"
- "yield protection"
- "demonstrated interest"

**Excludes:**
- Treats appeal-success as universal; in fact §479A authority is
  discretionary per office, success rates vary significantly by
  school's institutional-aid budget (Princeton / Harvard / Yale /
  Stanford with large endowments and need-blind-and-meets-full-
  need policies have different appeal-economics than mid-tier
  privates and tuition-dependent regionals), and the
  documentation-quality of the appeal materially affects the
  outcome. The framing's "ask and you'll get more" oversells the
  base rate for mid-tier schools. Opposes F3 (ROI-by-major) when
  ROI-by-major routes the family toward a higher-ROI lower-aid
  option.
- Doesn't see *yield-protection* and *demonstrated-interest* as
  factors that can work against the strong-applicant appeal: top-
  cross-admit applicants are sometimes "yield-protected" by mid-
  tier schools (assumed to be using the school as a safety, given
  less merit aid than weaker applicants who are likely to enroll).
  The framing's "cross-admit leverage" can backfire on yield-
  protecting schools that withhold aid from likely-to-go-elsewhere
  applicants.
- Glosses over the *timing* of the appeal: most schools have an
  internal deadline for professional-judgment appeals (often within
  30 days of the award letter, sometimes by May 1 commitment
  deadline), and late appeals are de-prioritized or denied
  outright. The framing's "write the appeal letter" loses force
  when the family doesn't know the school's appeal-cycle calendar.
- Under-weights the difference between FAFSA appeals (need-based,
  driven by AGI / asset changes) and CSS-Profile appeals
  (institutional-aid-budget driven, more discretionary), which
  follow different procedural paths at most schools — the framing's
  generic "appeal" doesn't distinguish the two and applicants who
  appeal FAFSA when they need to appeal CSS-driven institutional
  aid miss the mark.
- Frames merit-aid as fully negotiable when in fact some schools
  (especially those with formula-driven merit-aid awards based on
  GPA / test-score cutoffs — many flagship publics' automatic
  scholarships, large-state-system merit programs) do NOT negotiate
  on merit because the awards are formula-mechanical. The framing's
  "merit-aid is the opening offer" applies to discretionary merit
  but not formula merit.

## F8: Tax-bomb-arithmetic-and-sinking-fund framing

**Decisions applied to:** D4 (IDR + tax-bomb savings vs 10-year
standard), D10 (PSLF-§108(f)(1)-tax-free-vs-IDR-25-year-taxable
distinction).

**Mental model.** IDR-forgiveness at 20–25 years is *taxable* as
ordinary income on the forgiveness-year 1099-C absent the ARPA §9675
exclusion (which expires end-of-2025 absent extension); PSLF-
forgiveness under HEA §455(m) is *tax-free* under IRC §108(f)(1).
For a borrower with a $200k balance forgiven after 20 years on IDR
at 35% marginal bracket, the tax liability is $70k due in cash that
year. The framing's reflex: build a sinking fund NOW, contributed
in a taxable brokerage growing at market rate, sized to the future-
value of the tax liability discounted back to today. For a 20-year-
out tax bomb of $70k, the sinking-fund contribution today is
~$30–40k depending on assumed return — and this calculation is the
*load-bearing fact* the "I'll just be on IDR forever" framing
systematically misses. The framing also extends to IRC §108(a)(1)(B)
insolvency exclusion: if forgiven amount + other income leaves the
borrower with negative net worth at the moment of forgiveness, the
forgiveness is excluded under the insolvency rule (filed with Form
982 — fact-specific, CPA-supervised). And to state-level tax-bomb:
state taxation of forgiven loans varies (CA, MS, IN, NC, WI treated
the 2022 one-time forgiveness wave as state-taxable even when
federally excluded). Voice: r/StudentLoans / r/PSLF / Heather Jarvis
Student Loan Expert / retirement-experienced-CPA voice.

**Characteristic vocabulary:**
- "tax bomb"
- "sinking fund"
- "ARPA cliff"
- "§108(f)(1) tax-free"
- "insolvency exclusion"
- "Form 982"
- "state-level tax bomb"
- "1099-C ordinary income"
- "future value of liability"
- "Roth-conversion-ladder bracket management"

**Excludes:**
- Treats the tax-bomb-sinking-fund as if the ARPA §9675 exclusion
  will definitely sunset; in fact further extension is plausible
  given political dynamics, and a sinking fund that grows for 20
  years against a tax liability that gets excluded leaves the
  borrower with $30–40k of taxable brokerage that did NOT need to
  be earmarked for taxes. The framing's "build the sinking fund"
  is correct on expected-value but over-states the certainty of
  the tax-liability materializing. Opposes F12 (ARPA-cliff-aware-
  but-pragmatic).
- Doesn't see the *insolvency-exclusion-§108(a)(1)(B)* path
  clearly: insolvency at the moment of forgiveness can fully
  exclude the forgiven amount from federal income, but it requires
  documenting that liabilities exceeded assets *immediately before
  the discharge* — a fact-specific calculation that requires CPA
  analysis and Form 982 filing. For borrowers with significant
  retirement-account balances (which count as assets for insolvency
  purposes despite being excluded from FAFSA), the insolvency path
  is often unavailable; the framing's "insolvency-exclusion is the
  backstop" overstates the realistic availability of this exit.
- Glosses over the state-level tax-bomb on the forgiven amount:
  even when ARPA §9675 excludes federally, state conformity is
  uneven — CA, MS, IN, NC, WI did NOT conform to the 2022 one-time
  exclusion. A borrower in a non-conforming state faces state tax
  on the forgiven balance even when federal tax is excluded. The
  framing's "tax bomb math" needs to be done at the state-tax level
  separately, and many borrowers ignore the state piece.
- Under-weights the *Roth-conversion-ladder in low-income years* as
  a complementary strategy: in years where the borrower has
  structurally low income (sabbatical, leave-of-absence, between
  jobs), accelerating Roth conversions to use up bracket headroom
  is a partial pre-payment of the future tax-bomb liability. The
  framing names this in passing but most borrowers don't operate
  the strategy because the years of low-income are unpredictable.
- Frames the sinking-fund-in-taxable-brokerage as if taxable
  growth were free; taxable LTCG on the sinking fund itself is
  taxed, and dividends are ordinary or qualified depending on the
  fund — the net-of-tax growth rate on the sinking fund is below
  market rate. Borrowers building the sinking fund at "expected
  market return" under-state the after-tax accumulation needed.

## F9: Consumer-protection / anti-predatory-lending framing

**Decisions applied to:** D1 (Refi mechanics — disclosure quality),
D5 (For-profit and low-selectivity privates with high CDR), D7
(Parent PLUS vs private with cosigner — origination disclosures).

**Mental model.** The student-loan industry has a documented history
of predatory practices: forbearance-steering by servicers under the
2010–2018 Navient / FedLoan era (now subject to the 2022–2024 IDR /
PSLF account-adjustment consent decrees and Borrower Defense relief
cohorts), aggressive private-lender refinance marketing to
borrowers with PSLF-eligible employment, for-profit colleges
(Corinthian, ITT Tech, Argosy, others) with cohort-default-rates
above 30% targeting first-generation and military-veteran
populations, and Parent-PLUS origination practices that consistently
under-disclose to parent-borrowers that the loan is in *their* name
(not the student's) and is therefore parental debt with parental-
credit implications. The framing's reflex on every funding-side
decision: read the CFPB student-loan complaint database for the
specific lender / servicer / school under consideration, check the
College Scorecard cohort-default-rate for the program, verify the
school's HEA Title IV eligibility status, and treat every
refinance solicitation as adversarial until proven otherwise. The
SLBA / NCLC / state-AG enforcement actions and the post-2022 DOJ-
USDOE attestation-guidance-shift on bankruptcy-discharge are the
substantive operating reality this framing reasons from. Voice:
CFPB / NCLC / SLBA / state-AG / consumer-protection-attorney voice;
post-*Brunner* / post-*Frost* / 2022 DOJ-USDOE-guidance bankruptcy
voice.

**Characteristic vocabulary:**
- "forbearance steering"
- "the servicer is not your friend"
- "cohort default rate"
- "CFPB complaint database"
- "HEA Title IV eligibility"
- "account adjustment review"
- "Borrower Defense"
- "Brunner / Frost / DOJ guidance"
- "consent decree"
- "predatory marketing"

**Excludes:**
- Treats every private-lender refinance solicitation as adversarial
  when many private refinance products are *appropriate* for the
  borrower's situation (high-credit-tier professional with no
  plausible PSLF path); the framing's anti-private-refi reflex
  costs borrowers who would benefit from refinancing the rate
  savings. Opposes F4 (rate-spread-arithmetic). The framing's
  "the servicer is not your friend" is true in expectation but
  over-applied creates over-caution.
- Doesn't see that the post-2022 DOJ-USDOE bankruptcy-discharge
  attestation guidance has softened the *Brunner* / *Frost* bar
  but the discharge bar remains highly fact-specific — the
  framing's "discharge is now possible" oversells the realistic
  rate of successful discharges (still well under 50% even in
  favorable-jurisdictions when the borrower actually files). Many
  borrowers learn the discharge path but don't pursue it because
  the bankruptcy-itself cost dominates.
- Under-weights the *operational* path through the FSA Ombudsman
  Group → SLBA / NCLC referral → state-AG complaint → district-
  court litigation — the framing names the escalation ladder but
  the time-to-resolution at each step is months to years and the
  framing's "use the escalation channel" understates the lived
  cost of navigating it. Borrowers in active servicer disputes
  often pay down the disputed balance rather than wait on the
  escalation outcome.
- Glosses over the *parent-borrower* informed-consent gap on
  Parent PLUS: many parents don't realize Parent PLUS is debt in
  *their* name (not the student's) until the first credit-report
  pull or co-signed apartment lease. The framing's "Parent PLUS
  disclosure is inadequate" is correct but the operational fix
  (re-papering the loan into the student's name via private refi)
  has the federal-protection-erasure cost the framing's own anti-
  private-refi reflex should object to — internal tension within
  the framing.
- Frames for-profit-college-targeting as if it had been resolved
  by Borrower Defense and the 2015-and-after enforcement actions;
  the underlying population of borrowers who attended Corinthian
  / ITT / Argosy / DeVry / similar still face credit-damage,
  spousal-credit-pull complications, and ongoing loan-balance-
  with-no-degree even after Borrower Defense relief. The framing's
  "the bad-actor schools are closed" understates the surviving-
  borrower population's ongoing exposure.

## F10: FIRE-aware-college-funding / retirement-priority framing

**Decisions applied to:** D3 (Front-load 529 vs annual vs Roth-
substitute), D6 (529 vs Roth vs taxable vs UGMA mix), D7 (Parent
PLUS vs federal direct vs HELOC — parental retirement readiness as
load-bearing).

**Mental model.** The single most important framing in college-
funding decisions is whether the parents are themselves on track for
retirement. The personal-finance community consensus — strongest in
the r/financialindependence, Mr. Money Mustache "MMM University"
essay tradition, ChooseFI, and Bogleheads-retirement-priority voices —
is that prioritizing kids' 529 over parents' Roth/401k contributions
is one of the highest-regret patterns in the community: *students can
borrow for college; parents cannot borrow for retirement.* The
framing's reflex on every funding decision: model parental retirement
readiness first (target retirement-savings rate ~15-25% of gross
income, target retirement-account balance multiples by age — 1× by
30, 3× by 40, 6× by 50, 8× by 60 per Fidelity's commonly-cited
heuristic), and only earmark surplus for kids' college after the
retirement target is on track. Parent PLUS at 9.08% is *worse* than
401k-match-driven savings at any reasonable expected return; HELOC-
as-college-funding puts the parent's primary residence at risk for
the kids' education. The framing's "max retirement first, college
second" extends to: federal-direct student loans for the kid are
appropriate borrowing (the kid's optionality is preserved through
the federal protections); Parent PLUS / private cosigner / HELOC is
the parent shifting their own retirement-funding into the kid's
education. Voice: r/financialindependence / Mr. Money Mustache /
ChooseFI / NAPFA-fee-only-CFP / Bogleheads-retirement-priority voice.

**Characteristic vocabulary:**
- "secure your own oxygen mask first"
- "kids can borrow, you can't"
- "retirement-savings rate"
- "Fidelity 1× / 3× / 6× / 8× targets"
- "the highest-regret pattern"
- "MMM University"
- "401k-match-as-100%-return"
- "Parent PLUS is parental retirement"
- "HELOC puts the house at risk"
- "fund your retirement, then theirs"

**Excludes:**
- Treats parental-retirement-readiness as binary (on-track vs not)
  when in reality the distribution is continuous and the marginal
  529 dollar trades against the marginal 401k dollar at a household-
  specific rate of return. The framing's "fund retirement to 15-25%
  THEN start the 529" creates a discrete cutoff that doesn't match
  the actual optimization — many households can productively fund
  both at lower rates than the targets suggest, especially when the
  household income is high enough that retirement-account
  contribution limits are binding. Opposes F2 (529-state-deduction)
  when state-deduction value at the margin is significant.
- Doesn't see that the *parent-401k-contribution* and *kid-529-
  contribution* may live in different decision-makers' control
  (e.g. employed-parent's 401k, household-budget-decision-maker
  funds the 529 from after-tax income); the framing's "parents
  fund retirement first" assumes unified household optimization
  that doesn't always exist in two-income households with
  different account-decision-rights.
- Under-weights the *grandparent-funding* path that doesn't trade
  off against parental retirement at all — grandparent-529
  (especially post-Simplification with grandparent-distributions
  removed from student-income) is a funding source independent of
  the parental-retirement question; the framing's "retirement
  priority" applies to the parent-as-funder but the same household
  may have grandparent-funding-availability the framing under-
  prices. Cross-routes `family-planning`.
- Glosses over the *positional* / status component of college-
  funding decisions: many parents whose retirement is genuinely
  on-track still under-fund kids' college relative to peer-group
  norms (the framing's "retirement-first ethos" is alien to
  households where neighbors / extended family treat private-
  school funding as table-stakes). The framing's prescriptive
  ethos applies cleanly in r/financialindependence but bumps
  against social-context for many families.
- Frames Parent PLUS as uniformly worse than 401k-contribution
  on rate-of-return grounds when in fact Parent PLUS interest is
  deductible under IRC §221 (student-loan-interest deduction up
  to $2,500/year, AGI phase-out), so the after-tax effective rate
  is lower than the nominal 9.08% — the framing's rate comparison
  needs to be net-of-deduction for the parents in the AGI phase-
  in range.

## F11: Employer-tuition / §127-retention-clawback framing

**Decisions applied to:** D2 (Graduate school ROI — full-time vs
part-time with employer reimbursement), D9 (Employer §127 vs
scholarship-stacking vs self-pay).

**Mental model.** IRC §127 allows up to $5,250/year of employer-paid
tuition + fees + books + supplies to be excluded from W-2 income;
anything above the $5,250 cap is imputed taxable wages on the W-2
unless the employer also runs a §132(d) Working-Condition-Fringe
exclusion for job-related courses (most employers don't distinguish,
so above-cap reimbursement gets taxed at marginal + payroll rates,
materially reducing effective reimbursement value). The framing's
load-bearing observation: most large-employer tuition-reimbursement
programs come with a 1–4 year retention clawback — leaving in year
1 of the clawback period triggers repayment of 80–100% of the
tuition. The community-default framing is "tuition reimbursement is
comp with a retention lock" — the program is functionally a
golden-handcuff agreement. The framing's reflex: model the §127
cap-as-partial-subsidy ($5,250/year covers ~1.5–2 credits at $3,000/
credit T15 MBA pricing, ~3 credits at $1,600/credit state-flagship,
full subsidy for Georgia Tech OMSCS at $7k total); model the
retention-clawback as a fully-priced retention obligation; and weigh
the partial-subsidy + retention-lock combination against full-time-
program (decision 2) + self-pay alternatives. Most institutional
scholarships do NOT stack with employer reimbursement — the school
adjusts the scholarship downward if the employer pays first; some
scholarships are tax-free under IRC §117(a) for tuition + required
fees but employer reimbursement for the same is §127, overlap is
treated as a wash not stacked. Voice: r/MBA / Wall Street Oasis /
employer-tuition voice (corporate HR, Glassdoor); cross-routes
`tech-career` heavily.

**Characteristic vocabulary:**
- "§127 cap $5,250"
- "above-cap imputed income"
- "retention clawback"
- "golden handcuffs"
- "§132(d) working-condition fringe"
- "tuition reimbursement is comp"
- "pre-enrollment approval"
- "scholarship displacement"
- "§117(a) qualified scholarship"
- "the 8-year commitment"

**Excludes:**
- Treats every employer-tuition program as having the same clawback
  structure when in fact the clawback windows, proration formulas,
  pre-approval requirements, and approved-program-lists vary widely
  by employer; the framing's "tuition reimbursement is comp with a
  retention lock" is structurally correct but the specific terms at
  any given employer often deviate from the typical 2-year prorated-
  clawback — borrowers need to read their employer's tuition-
  reimbursement plan document, not the framing's generic terms.
- Doesn't see the *§127 cap timing* mechanic: §127 is an annual cap
  ($5,250/calendar year), so a 2-year part-time program can use
  $10,500 total of §127 exclusion across 2 tax years; a 1-year
  intensive program loses half the §127 capacity. The framing
  generally optimizes for the 2–3 year part-time program where
  §127 cap is fully amortized but applicants often choose a
  shorter program for non-financial reasons and lose the
  optimization.
- Under-weights the *scholarship-displacement* mechanic in detail:
  the school adjusts the scholarship downward if the employer pays
  first, but the *order of application* matters — submitting the
  scholarship application before the employer-reimbursement
  enrollment can sometimes preserve the scholarship and stack with
  employer reimbursement at the §127-cap-only level. The framing's
  "scholarships don't stack" is true on the modal path but
  applicants who optimize the timing can sometimes get partial-
  stack. Opposes F7 (NACAC-counselor) when the school's
  scholarship and the employer's reimbursement compete.
- Glosses over the *career-pivot-during-program* problem: enrolling
  in a 3-year part-time MBA with employer reimbursement creates a
  career-lock during the program (you can't quit mid-program
  without triggering clawback), so a layoff or a competing job
  offer during years 1-2 creates a forced choice between
  completing the program (potentially without employer support if
  laid off) and pursuing the new opportunity. The framing's
  "tuition reimbursement is comp" doesn't price the *embedded
  call-on-the-employee* during the program window.
- Frames the §127 exclusion as if Working-Condition-Fringe §132(d)
  were practically available; in practice most HR / payroll
  departments don't have the systems to distinguish §127 from
  §132(d) tracking and they default to §127 reporting for
  everything, which means above-cap reimbursement gets imputed
  even when the course is job-related enough to qualify for
  §132(d). The framing's "use §132(d) for above-cap" is correct on
  paper but rarely operationally accessible at large employers.

## F12: ARPA-cliff-aware / political-risk framing

**Decisions applied to:** D1 (Refi timing relative to political-
status), D4 (IDR borrowers reaching forgiveness in 2026+), D10
(PSLF political-risk and account-adjustment-window).

**Mental model.** Federal-loan-program features are NOT permanent
fixtures — they are subject to administrative rule-making,
statutory amendment, and litigation-induced suspension. ARPA §9675
excluded student-loan forgiveness from federal taxable income for
forgiveness events 2021–2025; absent extension, IDR borrowers
reaching forgiveness in 2026+ face full ordinary-income inclusion.
The SAVE plan is in administrative forbearance under the 8th
Circuit injunction with months counting for PSLF but NOT for IDR-
forgiveness, materially changing the refi-vs-IDR math. The 2022–
2024 IDR / PSLF account-adjustment captured millions of borrowers'
qualifying-payment counts forward — borrowers who haven't applied
for account-adjustment review should do so before the window
closes. The political-risk dimension extends to: PSLF eligibility
rules can change (the framing's reflex is to file ECF annually to
lock in qualifying-employment-and-payment-counts on the *current*
rule set); IDR-forgiveness terms can change retroactively (less
likely but documented at the rule-making level); the federal-loan-
program itself can be reformed by Congress (rare but legally
possible). The framing's reflex: don't plan around a single
administrative state of the federal-loan-program lasting 20+ years;
build in optionality and document everything at the time of
qualifying events. Voice: Heather Jarvis Student Loan Expert / r/PSLF
/ SLBA / NCLC / Federal Student Aid policy-tracking voice;
political-risk-aware consumer-finance journalism (Wall Street
Journal, ProPublica, Washington Post higher-ed coverage).

**Characteristic vocabulary:**
- "ARPA cliff"
- "SAVE administrative forbearance"
- "account adjustment window"
- "PSLF Buyback program"
- "the 8th Circuit injunction"
- "political risk on the federal bundle"
- "document everything"
- "the rules can change"
- "ECF annually"
- "lock in on current rules"

**Excludes:**
- Treats political-risk as if it cuts uniformly against the
  borrower; in fact some political risks cut *in favor of* the
  borrower (the 2022 Biden one-time forgiveness, the SAVE plan's
  5%/225%-poverty mechanics when it was active, the 2022–2024
  account-adjustment that captured millions of qualifying
  payments). The framing's "the rules can get worse" anchors on
  loss but the population of recent rule-changes is net-positive
  for low-and-middle-income borrowers. Opposes F8 (tax-bomb-
  arithmetic) when tax-bomb planning assumes the ARPA cliff hits.
- Doesn't see that the *account-adjustment* is a one-time
  opportunity with a closing window; borrowers who haven't filed
  by the deadline lose the corrective for prior forbearance /
  non-IDR periods. The framing names the window but understates
  the urgency for borrowers whose servicer-history includes
  documented forbearance-steering. Many borrowers learn about the
  adjustment after the window has closed.
- Under-weights the *Borrower Defense to Repayment* path under HEA
  §455(h) for borrowers attending schools later found to have
  engaged in misrepresentation — Borrower Defense relief can fully
  discharge federal balances and includes tax-free treatment under
  §108(f)(1)-analog mechanics. The framing's "political risk on
  the federal bundle" doesn't surface Borrower Defense as a
  political-risk *opportunity* (relief expansion under the 2022-
  2024 cohorts) vs threat.
- Glosses over the *state-conformity* dimension to political-risk:
  even when federal ARPA §9675 excludes the forgiven amount, state
  conformity is uneven and changes year-to-year — CA, MS, IN, NC,
  WI didn't conform to the 2022 one-time exclusion. The framing's
  "political risk on the federal bundle" needs to extend to state-
  conformity decisions made independently by each state legislature.
- Frames the federal-loan-program as if its future were
  unpredictable; in fact the program's *core* features (Direct
  loans, IDR plans, PSLF, the federal interest-rate-set-annually-by-
  statute) have been remarkably stable across administrations even
  through rulemaking churn on the specific IDR terms. The framing's
  "the rules can change" over-states the systemic risk relative to
  the documented pace of meaningful change.

## F13: Bankruptcy-discharge-and-default-recovery framing

**Decisions applied to:** D1 (Default-rehabilitation as alternative
to refi), D4 (Failed-IDR-payments as discharge predicate), D10 (PSLF
denial → escalation ladder → discharge consideration).

**Mental model.** Federal student loans are dischargeable in
bankruptcy under 11 U.S.C. §523(a)(8) only on a showing of "undue
hardship" — historically interpreted under the *Brunner* test (3
prongs: minimal standard of living, persistence over a significant
portion of repayment period, good-faith efforts to repay) and the
*Frost* test in the 1st Circuit (totality of circumstances). The
2022 DOJ-USDOE Joint Attestation Guidance materially softened the
discharge bar by directing US Attorneys to stipulate to discharge
where the borrower's attestation supports undue-hardship — discharge
rates among borrowers who file for discharge have risen from
~0.1–0.5% pre-2022 to ~30%+ in some districts post-guidance. The
framing's reflex on default and severe-distress decisions: (a)
exhaust default-rehabilitation (9 on-time payments over 10 months
on a federal income-driven plan restores eligibility for IDR /
PSLF / federal protections; collection fees are removed; credit
report is corrected); (b) if rehabilitation isn't viable, evaluate
the discharge path with NACBA / NCLC-affiliated bankruptcy counsel;
(c) treat the *Brunner-softening-post-2022* as the operating
reality, NOT as theoretical. The framing also extends to *Borrower
Defense* discharge for fraud-school-attended borrowers and to
death-and-disability discharge under HEA §437(a). Voice: NACBA
bankruptcy-attorney voice; SLBA / NCLC consumer-protection voice;
post-2022 DOJ-USDOE-attestation-guidance voice.

**Characteristic vocabulary:**
- "Brunner test"
- "Frost totality"
- "undue hardship"
- "DOJ attestation guidance"
- "discharge stipulation"
- "default rehabilitation"
- "9-of-10 payments"
- "NACBA"
- "Borrower Defense to Repayment"
- "death-and-disability discharge"

**Excludes:**
- Oversells the post-2022 DOJ guidance softening of *Brunner*;
  while discharge rates have risen, the realistic rate is still
  well under 50% in most districts even when borrowers actually
  file. Many borrowers learn about the discharge path but don't
  file because the bankruptcy-itself cost (credit damage,
  attorney fees, chapter-7-or-13 procedural complexity) dominates.
  The framing's "discharge is now possible" is true but the
  operational rate is much lower than the headline suggests.
- Doesn't see that the *default-rehabilitation* path has a
  one-time-per-loan limit; a borrower who rehabilitates and then
  defaults again has used the rehabilitation card. The framing's
  "rehabilitate then choose IDR" is the right starting move but
  the lifetime-limit means it's not a repeatable strategy. Cross-
  routes consumer-protection (F9) on the servicer-distress
  pattern.
- Under-weights the *post-discharge* tax-treatment: bankruptcy
  discharge of student-loan debt is excluded from income under
  IRC §108(a)(1)(A), so there's no tax-bomb on discharged
  balances. The framing names this in passing but many borrowers
  comparing discharge against IDR-forgiveness don't see that
  discharge is *tax-free* even when ARPA cliffs out and IDR-
  forgiveness becomes taxable.
- Glosses over the *spousal-credit-pull* implications of
  bankruptcy: in community-property states, a spouse's
  bankruptcy can affect the non-filing spouse's credit, and joint
  accounts get discharged-or-not based on the filing structure
  (Chapter 7 vs Chapter 13). The framing's "discharge frees the
  borrower" understates the household-credit knock-on for married
  filers.
- Frames *death-and-disability discharge* under HEA §437(a) as
  cleanly available; in fact total-and-permanent-disability (TPD)
  certification requires physician attestation, VA disability
  rating of 100%, or 3+ years of SSDI — and a 3-year monitoring
  period applies post-discharge during which earned income above
  the poverty-line threshold reverses the discharge. The framing's
  "disability discharges the loan" misses the 3-year monitoring
  trap.

## F14: 1099-vs-W-2-PSLF-asymmetry / contractor-trap framing

**Decisions applied to:** D10 (PSLF qualification — employment-type
test), D2 (Graduate school for self-employed pivots — PSLF-
eligibility post-degree).

**Mental model.** PSLF qualifying employment requires *W-2
employment* at a qualifying employer (federal / state / local /
tribal government, 501(c)(3) nonprofit, AmeriCorps / Peace Corps /
public-defender / public-health-corps). 1099 contractors at a
501(c)(3) — even one performing identical work to W-2 employees —
do NOT qualify for PSLF, full stop. This is one of the most-missed
PSLF mechanics for former-contractor founders, gig-economy workers
at nonprofit clients, and consulting-firm-staff serving government /
501(c)(3) clients (the consulting firm is for-profit; the contractor
is doing 501(c)(3)-work-as-a-contractor; neither qualifies). The
framing's reflex on every PSLF-eligibility decision: (a) verify W-2
status at the qualifying employer (the PSLF Employment Certification
Form — ECF — is the load-bearing document); (b) for borrowers
considering a 1099-to-W-2 conversion at the same employer, model
the wage / benefits delta against the PSLF qualifying-payment value;
(c) for borrowers considering self-employment / consulting / LLC-
formation at the boundary of PSLF qualification, recognize that
forming an LLC / S-corp generally converts the borrower OUT of PSLF
qualification even when the LLC's clients are 501(c)(3). The
framing also covers full-time-equivalence: ≥30 hours/week or the
employer's full-time definition (whichever is lower); part-time
work at qualifying employers can be aggregated across two qualifying
employers to reach the threshold. Voice: r/PSLF / Heather Jarvis
Student Loan Expert / employment-classification consumer-protection
voice; cross-routes `entrepreneurship` heavily.

**Characteristic vocabulary:**
- "W-2 vs 1099 PSLF"
- "ECF Employment Certification Form"
- "full-time-equivalence ≥30 hours"
- "qualifying employer test"
- "501(c)(3) clients vs 501(c)(3) employer"
- "LLC kills PSLF"
- "the contractor trap"
- "aggregating qualifying employment"
- "Schedule C vs W-2"
- "consulting firm exit and PSLF"

**Excludes:**
- Treats W-2-vs-1099 as a clean line when in fact the
  classification is contested in many gig-economy / consulting /
  fractional-roles — a worker classified as 1099 may be a W-2
  employee under the IRS common-law-employee test or under state-
  law AB-5-style ABC tests, and reclassification (forced or
  voluntary) can retroactively change PSLF qualifying-payment
  status. The framing's "1099 doesn't qualify" misses the
  reclassification path that some borrowers pursue. Cross-routes
  `entrepreneurship`.
- Doesn't see that *part-time aggregation* across two qualifying
  employers requires both to certify on separate ECFs and the
  borrower to track full-time-equivalence calculation
  proactively — many borrowers in part-time roles at two
  501(c)(3)s assume they qualify without doing the ECF paperwork
  for both; the year-9 surprise pattern (MOHELA finds only one
  employer's certification, zeroes the other employer's months)
  is documented.
- Under-weights the *S-corp-formation-at-501(c)(3)* trap: a
  borrower who incorporates as an S-corp to serve a 501(c)(3)
  client (consulting structure) typically becomes the W-2
  employee of their OWN S-corp, NOT the 501(c)(3) — and the
  S-corp is for-profit, so the borrower's W-2 employment is at a
  for-profit and does not qualify for PSLF even when the
  underlying work is for a 501(c)(3). The framing's "501(c)(3)
  employer" test is more restrictive than the work-content test
  many borrowers assume.
- Glosses over the *501(c)(4) exclusion*: advocacy nonprofits
  organized under §501(c)(4) (issue-advocacy, lobbying, political-
  action) do NOT qualify for PSLF even though they are tax-exempt
  nonprofits — a frequent surprise for borrowers at think-tanks
  and policy-advocacy organizations that operate as §501(c)(4) for
  lobbying-flexibility reasons. The framing names "NOT 501(c)(4)"
  but borrowers don't always know their employer's tax-exempt
  classification.
- Frames *partisan political* employment as cleanly excluded; in
  fact some borrowers at nonprofit-research arms of partisan
  organizations face complicated classification — the parent
  organization is §501(c)(4) or §527 (political organization),
  but the research-and-policy arm is §501(c)(3); ECF certification
  follows the employer-of-record on the W-2, which can be either
  entity depending on the org's structure. The framing's "no
  partisan" doesn't surface the entity-of-record subtlety.

---

## Coverage map

Per `_schema.md`, every decision needs ≥ 3 framings.

| Decision | Framings that cover it | Count |
|---|---|---|
| D1 Refi vs preserve federal optionality | F1, F4, F8, F9, F12, F13 | 6 |
| D2 Graduate school ROI given career stage | F3, F11, F14 | 3 |
| D3 Front-load 529 5-year-forward vs annual vs Roth | F2, F5, F6, F10 | 4 |
| D4 IDR + tax-bomb vs 10-year standard | F1, F4, F8, F12, F13 | 5 |
| D5 In-state public vs out-of-state private merit | F3, F7, F9 | 3 |
| D6 529 vs Roth vs taxable vs UGMA vs Coverdell mix | F2, F5, F6, F10 | 4 |
| D7 Parent PLUS vs federal direct vs private cosigner | F1, F4, F9, F10 | 4 |
| D8 FAFSA / CSS Profile asset positioning, base-year | F5, F7, F9 | 3 |
| D9 Employer §127 vs scholarship-stacking vs self-pay | F2, F11 | 2 + cross-cutting |
| D10 PSLF qualification (120-payment, 501(c)(3), ECF) | F1, F8, F12, F13, F14 | 5 |

D9 (Employer §127) has F2 and F11 directly assigned plus cross-
cutting reach from F3 (ROI-by-major-and-program — the part-time
employer-funded path is the dominant strategy for engineers /
consultants / finance pros pursuing MBA / MS-CS / JD-part-time when
program quality is acceptable, satisfying the ≥3 framings minimum
through cross-cutting application). All 10 decisions satisfy the
≥3 framings minimum. D1 (refi vs preserve optionality) is the
densest coverage at 6 framings — refi is the most-contested
decision in the domain with active framings from federal-
optionality, rate-arithmetic, consumer-protection, political-risk,
and bankruptcy-default-recovery perspectives. D4 (IDR + tax-bomb)
and D10 (PSLF) are the next-densest, reflecting the layered
optionality / arithmetic / political-risk / employment-type-test
complexity that defines the federal-loan landscape.

## Cross-framing tensions (opposing-framing pairs)

These are the direct axiom-level oppositions to surface in Layer 3
and for Triage / Risk Officer routing when the asker's prompt
vocabulary lands on one side:

- **F1 (federal-optionality-as-put-option) ↔ F4 (rate-spread-
  arithmetic)** on D1 / D4 / D7. F1 says: the option bundle is
  worth multiples of the 200bp rate spread for any borrower with
  non-trivial layoff / disability / PSLF / graduate-school
  probability; don't refi federal. F4 says: model the household's
  *actual* probability-weighted option-exercise scenarios; for
  borrowers in stable high-income roles with no plausible option-
  exercise, the rate-spread is real money the federal-optionality
  framing leaves on the table. Same borrower, same numbers,
  opposite advice — F1 reasons from option-value, F4 reasons from
  realized cash-flow. Triage should surface F4 when the asker's
  prompt reads as F1-anchored ("never refi federal") on borrowers
  with genuinely near-zero option-exercise probability, and vice
  versa.

- **F2 (529-state-deduction-and-tax-deferral) ↔ F6 (529-to-Roth-
  flexibility-hedge)** on D3 / D6. F2 says: front-load the 529 with
  the 5-year-forward election to maximize state-deduction-on-
  contribution and tax-deferred growth on the longest possible
  runway. F6 says: the Roth-substitute path preserves flexibility
  for the "kid doesn't go" scenario at the cost of state-deduction
  value; the SECURE 2.0 §126 rollover is a long-clock partial
  hedge that doesn't help if the kid doesn't go to college at all.
  The framings agree the 529 is the dominant vehicle for the
  household whose kid will go to college and disagree on how much
  flexibility-cost to pay for the kid-doesn't-go scenario.

- **F2 (529-state-deduction) ↔ F10 (FIRE-retirement-priority)** on
  D3 / D6 / D7. F2 says: the state-deduction value plus tax-
  deferred growth makes the 529 the dominant vehicle for college-
  funding, fund it aggressively. F10 says: the parental-retirement-
  funding question is load-bearing; fund retirement-first, college-
  second; over-funding 529 ahead of retirement is the highest-
  regret pattern in the personal-finance community. Same household,
  same surplus dollars, opposite advice — F2 reasons from per-
  vehicle tax-arbitrage, F10 reasons from household-allocation-
  priority. Triage should surface F10 when the asker's prompt
  reads as 529-focused on households whose retirement-savings rate
  is below target.

- **F3 (ROI-by-major) ↔ F7 (NACAC-counselor-aid-negotiation)** on
  D5. F3 says: program-of-study × school-tier × all-in-net-cost
  drives the wage premium; pick the higher-ROI program. F7 says:
  the financial-aid award is the opening offer; appeal, negotiate,
  surface the cross-admit leverage, and the net cost shifts in the
  family's favor. The framings agree on net-price-not-sticker-price
  but diverge on whether to accept the initial award as the
  comparison input or treat it as the *initial* input that an
  appeal will move. The right answer depends on the family's
  willingness to invest in the appeal process and the school's
  institutional-aid-budget context.

- **F5 (FAFSA-base-year-and-asset-positioning) ↔ F10 (FIRE-
  retirement-priority)** on D8. F5 says: retirement-account
  contributions are excluded from FAFSA / CSS asset calculations,
  so max retirement-contributions in pre-base-year for the FAFSA
  win. F10 says: max retirement-contributions because retirement
  is the priority — and the FAFSA-shelter is a *complementary*
  win, not the driving rationale. The framings agree on the
  action but disagree on the framing: F5 treats retirement-
  shelter as a FAFSA-optimization strategy; F10 treats it as the
  household-priority that happens to also yield FAFSA benefits.
  The tension matters when the household's retirement-contribution
  capacity is below maximum and the family must trade off
  retirement-funding against college-funding cadence.

- **F8 (tax-bomb-arithmetic-and-sinking-fund) ↔ F12 (ARPA-cliff-
  aware-political-risk)** on D4 / D10. F8 says: build the tax-bomb
  sinking fund NOW for the IDR-forgiveness 20+ years out; the
  arithmetic is load-bearing. F12 says: the ARPA exclusion may
  extend, the federal-loan-program features are political-risk-
  driven, and a sinking fund that grows for 20 years against a
  tax liability that gets excluded leaves the borrower with
  $30–40k of taxable brokerage earmarked for taxes that did not
  need to be earmarked. The framings agree the political-risk
  exists and disagree on which direction it cuts.

- **F9 (consumer-protection-anti-predatory) ↔ F4 (rate-spread-
  arithmetic)** on D1. F9 says: treat every private-lender refi
  solicitation as adversarial; the federal protections are
  load-bearing; the post-2022 IDR / PSLF account-adjustment shows
  servicer-borrower asymmetry. F4 says: for high-credit-tier
  borrowers with stable income and no plausible PSLF path, the
  rate-spread savings are real and the federal protections are
  out-of-the-money; refi capture the spread. Same borrower-
  population framed differently. Triage should surface F9 when the
  asker is in active servicer-dispute or near a PSLF / disability
  threshold, and F4 when neither holds.

- **F11 (§127-retention-clawback) ↔ F3 (ROI-by-major)** on D2 /
  D9. F11 says: tuition reimbursement is comp with a retention
  lock; the part-time-with-employer-funding path dominates for
  most working professionals because it eliminates opportunity-
  cost-on-income. F3 says: the dominant variable is program-of-
  study × school-tier ROI; if the part-time-employer-funded
  program has weaker outcomes than the full-time-program-the-
  employer-doesn't-fund, the §127 subsidy doesn't compensate for
  the program-quality delta. The framings agree on cost-
  minimization and disagree on whether program-quality dominates.

- **F13 (bankruptcy-discharge-and-default-recovery) ↔ F9
  (consumer-protection-anti-predatory)** on default and severe-
  distress decisions. F13 says: the post-2022 DOJ guidance has
  softened the *Brunner* bar; discharge is now realistically
  available and is tax-free under §108(a)(1)(A) — pursue
  discharge for borrowers in severe distress. F9 says: the
  predatory-servicer / account-adjustment / Borrower Defense path
  may yield relief without bankruptcy's credit-damage cost; exhaust
  the consumer-protection escalation ladder first. Same borrower,
  different path — F13 reasons from discharge-availability, F9
  reasons from non-bankruptcy-relief-availability. The right
  answer depends on the specific servicer-dispute facts and the
  borrower's tolerance for bankruptcy's collateral consequences.

- **F14 (1099-vs-W-2-PSLF-asymmetry) ↔ F11 (§127-retention-
  clawback)** on D2 / D10. F14 says: PSLF requires W-2 employment
  at a qualifying employer; 1099 contractors don't qualify even at
  501(c)(3) clients; self-employment / LLC formation typically
  kills PSLF. F11 says: employer-funded part-time education is the
  dominant strategy because it eliminates opportunity-cost-on-
  income; for engineers / consultants considering 1099-to-W-2
  conversion at a qualifying employer, the §127 subsidy + PSLF
  qualifying-employment is doubly valuable. The framings agree on
  W-2-employment-at-qualifying-employer as load-bearing and apply
  different mechanisms (one for forgiveness, one for tuition-
  subsidy) to the same population.

## Voice anchors for Layer 3 (blindspots) and Layer 4 (sources.yaml)

Layer 3 (`blindspots.md`) will draw from these conceptual
communities — each carries a recognizable voice, vocabulary, and
characteristic blind spots OF its own framing. These are voice-
anchors, not source URLs; `sources.yaml` (the next sub-item) will
attach concrete sources to each.

- **PSLF-preservation voices** — r/PSLF, Student Loan Borrower
  Assistance Project / National Consumer Law Center, FSA
  Ombudsman Group, Heather Jarvis Student Loan Expert. Primary
  source for F1 (federal-optionality), F9 (consumer-protection),
  F12 (political-risk), F14 (1099-vs-W-2-asymmetry). Blind spot of
  *this* community: over-applies "never refi federal" to borrowers
  with genuinely-low option-exercise probability; over-credits the
  post-2022 account-adjustment as universal relief when many
  borrowers still face servicer-dispute residue.

- **ROI-by-major / labor-market voices** — Georgetown Center on
  Education and the Workforce (CEW), Burning Glass / Lightcast,
  Payscale, BLS Occupational Employment and Wages, College
  Scorecard. Primary source for F3 (ROI-by-major). Blind spot:
  routes everything through earnings-medians, under-prices the
  option value of non-vocational degrees and the path-from-low-
  immediate-earnings-to-professional-school pivots; over-confident
  on median outcomes that hide bimodal distributions.

- **FIRE-aware-college-funding voices** — r/financialindependence
  college threads, Mr. Money Mustache "MMM University" essays,
  ChooseFI, The College Investor (FIRE-adjacent), retirement-
  priority Bogleheads threads. Primary source for F10
  (FIRE-retirement-priority). Blind spot: applies prescriptive
  ethos uniformly to households for whom the social-context
  doesn't support it; under-prices the consumption-value of
  college-funding-as-family-status-signal.

- **NACAC-counselor voices** — National Association for College
  Admission Counseling members, NACAC Ethics Statement, high-
  school college-counseling office voice, independent-counselor
  associations (IECA, HECA). Primary source for F7 (NACAC-counselor-
  aid-negotiation). Blind spot: over-confident on appeal-success
  rates for mid-tier schools with constrained institutional-aid
  budgets; under-weights yield-protection by mid-tier schools
  against likely-cross-admit applicants.

- **529 voices** — Mark Kantrowitz (SavingForCollege founder),
  SavingForCollege.com analyses, Mike Piper Open Social Security
  analogues for college funding, Bogleheads 529-discussion
  threads, The College Investor 529 coverage. Primary source for
  F2 (529-state-deduction), F6 (529-to-Roth-flexibility-hedge).
  Blind spot: oversells the SECURE 2.0 §126 rollover's near-term
  value; under-weights the leftover-529 problem for over-funded
  households; treats state-deduction-arbitrage as universally
  valuable when many states have no deduction.

- **CSS-Profile-aware voices** — r/financialaid, r/ApplyingTo
  College, Princeton Net Price Calculator, Form CSS specialists
  (NCAN, IECA-affiliated), school-specific net-price-calculator
  publications. Primary source for F5 (FAFSA-base-year-and-asset-
  positioning), F7 (NACAC-counselor-aid-negotiation). Blind spot:
  treats CSS Profile schools as if they followed FAFSA rules;
  under-weights the home-equity-and-business-asset-reporting
  differential.

- **r/StudentLoans / r/StudentLoansHelp / r/PSLF voices** —
  Reddit subreddits, transactional-and-peer-driven, MOHELA /
  Nelnet / EdFinancial-distrust ethos. Primary source for F1,
  F8 (tax-bomb-arithmetic), F12 (political-risk), F13 (bankruptcy
  -discharge). Blind spot: skews toward forbearance-steering-
  trauma cases; over-estimates servicer-error frequency for
  borrowers with clean account histories; under-weights the
  borrower's own role in account-status (missed recertifications,
  forbearance-elections).

- **MBA-admissions voices** — Poets&Quants, GMAT Club forums,
  Wall Street Oasis, r/MBA, Stacy Blackman / mbaMission /
  Personal MBA Coach admissions consultants. Primary source for
  F3 (ROI-by-major MBA-specific subset). Blind spot: over-credits
  M7 / T15 ranking value; under-prices engineer-pivot-to-PM
  internal-mobility as a substitute for MBA; conflates median MBA
  comp with what most graduates actually realize.

- **r/cscareerquestions / r/csMajors / Levels.fyi / Blind voices**
  — software-engineering-comp-aware, treats MBA tuition + 2-year
  opportunity cost in tech compensation as the dominant cost line.
  Primary source for F3 MS-CS subset and F11 (§127 employer-
  reimbursement for part-time MS-CS). Blind spot: under-weights
  the credentialing-value-for-non-tech pivots (MBA-to-VC, MBA-to-
  consulting); over-weights the engineer-staying-engineer case.

- **Consumer-protection voices** — CFPB student-loan complaint
  database, NCLC publications, SLBA / SLBI publications, state-AG
  enforcement actions, NACBA bankruptcy-attorney publications,
  post-*Brunner* / post-*Frost* / 2022 DOJ-USDOE-attestation-
  guidance coverage. Primary source for F9 (consumer-protection),
  F13 (bankruptcy-discharge), F14 (1099-vs-W-2-asymmetry, for
  classification-disputes). Blind spot: treats every private-
  lender / servicer as adversarial; under-credits the post-2022
  account-adjustment relief as systemic improvement; routes
  everything through litigation-or-escalation when many disputes
  resolve at the customer-service tier.

- **NAPFA fee-only-CFP voices** — NAPFA member directory, fee-
  only-CFP publications, Garrett Planning Network. Primary source
  for F10 (FIRE-retirement-priority) and F6 (529-to-Roth-flexibility
  -hedge). Blind spot: routes everything through the financial-plan
  lens at the cost of non-financial values; under-prices the
  family-status-signal of college-funding.

- **Retirement-experienced-CPA voices** — CPAs with §25A / §127 /
  §529 / SECURE 2.0 §126 / Form 709 / Form 982 history (NOT
  generic 1040-prep CPAs). Primary source for F2 (529-state-
  deduction-and-tax-deferral), F8 (tax-bomb-arithmetic and
  insolvency-exclusion), F11 (§127-retention-clawback). Blind
  spot: routes everything through tax-arbitrage at the cost of
  non-financial considerations; sometimes mis-applies federal
  rules to state-conformity-non-conforming situations.

- **HELOC-as-college-funding voices** — cross-edge with `housing`,
  mortgage-broker and fee-only-CFP voices on the HELOC-vs-Parent-
  PLUS comparison. Primary source for F4 (rate-spread-arithmetic)
  and F1 (federal-optionality, anti-HELOC side). Blind spot:
  understates the home-equity-at-risk dimension when the HELOC is
  being used for college funding rather than home-improvement.

- **Bankruptcy-discharge voices** — NACBA, NCLC, post-*Brunner* /
  post-*Frost* / 2022 DOJ-USDOE-attestation-guidance coverage,
  district-court Adversary Proceeding decisions in student-loan-
  discharge cases. Primary source for F13 (bankruptcy-discharge-
  and-default-recovery). Blind spot: oversells the post-2022
  softening; understates the bankruptcy-itself cost; doesn't
  consistently surface that bankruptcy discharge of federal
  student loans requires an *Adversary Proceeding* — a separate
  lawsuit-within-the-bankruptcy — not automatic discharge with
  the main bankruptcy filing.

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  every `Excludes` bullet above is a Layer 3 candidate. Highest-
  density candidates are F1 (federal-optionality — option-exercise-
  probability-mis-estimation, SAVE-administrative-forbearance trap,
  death-and-disability over-coverage assumption), F2 (529-state-
  deduction — Form 709 missing-filing trap, leftover-529 problem,
  out-of-state-rollover-recapture), F4 (rate-spread-arithmetic —
  refi-quote-impermanence, cosigner-asymmetry, ARPA-cliff-mis-
  estimation), F5 (FAFSA-base-year — CSS-vs-FAFSA asymmetric-
  reporting, CSS-retirement-contribution-add-back, every-year-
  prior-prior recurrence), F8 (tax-bomb-arithmetic — ARPA-cliff-
  certainty, insolvency-exclusion-availability, state-conformity),
  F10 (FIRE-retirement-priority — binary cutoff treatment, two-
  decision-maker households), F12 (ARPA-cliff-aware — political-
  risk-cuts-both-ways, account-adjustment-window-closing), F14
  (1099-vs-W-2 — S-corp-at-501(c)(3)-trap, 501(c)(4)-exclusion,
  reclassification-path). Sweep all 14 framings × ~5 bullets each
  = ~70 blindspot candidates; promote ≥ 5 per framing into
  `blindspots.md` per the [`_schema.md`](../_schema.md) minimum.

- **High-stakes posture (Mechanism E partial)**: `education-funding`
  is `high_stakes: false` per `_meta_ontology.md` §7 (most outcomes
  reversible at modest cost on multi-year horizons — refinance back
  to better rate, switch repayment plan, defer enrollment, transfer
  529 beneficiary, file appeals, redo FAFSA), but selected
  decisions carry six-figure tail risks where professional referral
  is the correct framing exit: D1 (refi-vs-federal-optionality
  where PSLF or disability-discharge optionality is plausibly
  load-bearing — student-loan attorney / Student Loan Borrower
  Assistance Project / FSA Ombudsman Group as $0-cost escalation
  before retaining paid counsel), D3 (large §529(c)(2)(B) 5-year-
  forward lump-sums where Form 709 filing or state-deduction-
  recapture mechanics matter — retirement-experienced CPA), D4
  (IDR borrowers with $150k+ balance needing tax-bomb sinking-
  fund design and Roth-conversion-coordination — CPA + fee-only
  fiduciary CFP), D5 (financial-aid appeal letters and merit-aid
  negotiation — NACAC-member college counselor; high-school
  counselor for dependent students), D7 (Parent PLUS vs federal
  direct vs private cosigner mechanics where federal-protection-
  asymmetry and cosigner-release-mechanics matter — fee-only CFP +
  consumer-protection-anti-predatory perspective + student-loan
  attorney for severe cases), D8 (CSS-Profile divorced-parent or
  business-asset reporting and professional-judgment appeals —
  financial-aid counselor + CPA), D10 (PSLF qualifying-employment
  disputes after a denied appeal; PSLF Buyback program filings;
  1099-vs-W-2 reclassification — student-loan attorney / FSA
  Ombudsman Group as $0-cost escalation). The posture is
  "decision-support framing rather than legal or financial
  advice"; the Editor surfaces the appropriate specific category
  inline rather than blanket-mandating one on every decision.
  Over-referral degrades signal; under-referral on the
  irreversible-decision (D1 federal-to-private refi) and the
  large-tail-risk decisions (D4, D8, D10) creates harm. State Bar
  / SEC-FINRA BrokerCheck / NACAC-directory verification on any
  individual professional recommended is the $0-friction
  procedural floor — surfaced on every individual-professional
  referral. The FSA Ombudsman Group is uniquely a $0-cost
  escalation channel that should be tried before retaining paid
  counsel on servicer-dispute decisions (D1, D4, D10). This
  selective-referral posture mirrors the `housing` and
  `entrepreneurship` precedent (partial-gating Mechanism E
  per high_stakes:false), and distinguishes `education-funding`
  from the uniformly-Mechanism-E-gated `personal-finance` /
  `health-insurance` / `immigration` / `family-planning` /
  `legal-disputes` domains. `domain_pack.md` (a later sub-item)
  should encode these as selective referrals, not blanket-defer
  language.

- **Triage routing notes**: framings F1 (federal-optionality), F8
  (tax-bomb-arithmetic), F10 (FIRE-retirement-priority), F11
  (§127-retention-clawback), and F14 (1099-vs-W-2-asymmetry)
  carry the most distinctive vocabulary signatures and should be
  high-confidence routing matches ("federal optionality", "tax
  bomb", "sinking fund", "secure your own oxygen mask first",
  "§127 cap", "1099 doesn't qualify for PSLF"). Framings F3
  (ROI-by-major), F5 (FAFSA-base-year), and F7 (NACAC-counselor)
  carry vocabulary that overlaps with general admissions /
  career-planning conversations outside education-funding —
  disambiguation against `tech-career` and `family-planning`
  adjacency is needed once V2 two-pass Triage is wired. Framings
  F9 (consumer-protection) and F12 (political-risk) have
  distinctive vocabulary but apply broadly across nearly every
  federal-loan decision — they are posture-framings rather than
  decision-framings.

- **Cross-domain edges from `decisions.md`**: F1 (federal-
  optionality), F8 (tax-bomb-arithmetic), F10 (FIRE-retirement-
  priority) cross-route `personal-finance` (debt-payoff-vs-invest
  prioritization, asset location, Roth-conversion-ladder bracket-
  management, retirement-account-exclusion-from-FAFSA, kiddie-tax
  §1(g) on UGMA/UTMA); F3 (ROI-by-major), F11 (§127-retention-
  clawback) cross-route `tech-career` (engineering-pivot-to-PM,
  MS-CS-as-H-1B-cap-exempt-route, employer-funded-part-time-MBA
  retention-clawback as golden-handcuffs); F14 (1099-vs-W-2-PSLF-
  asymmetry) cross-routes `entrepreneurship` heavily (worker-
  classification, S-corp-formation-killing-PSLF, LLC-as-parent-
  for-529-front-loading); F2 (529-state-deduction), F5 (FAFSA-
  base-year), F7 (NACAC-counselor) cross-route `family-planning`
  (529 inter-generational gifting, UGMA/UTMA basis transfer,
  divorced-parent-of-record post-Simplification, custodial-account
  drag); F4 (rate-spread-arithmetic) cross-routes `housing` (HELOC-
  as-college-funding-alternative, cash-out-refi-vs-Parent-PLUS,
  primary-residence non-reportable on FAFSA but reportable on CSS
  Profile); F3 (ROI-by-major) MS-CS subset cross-routes
  `immigration` (H-1B-cap-exempt master's, OPT extension on STEM,
  F-1 / J-1 status interactions); F13 (bankruptcy-discharge-and-
  default-recovery) cross-routes `legal-disputes` (post-*Brunner* /
  post-*Frost* / 2022 DOJ-USDOE-attestation-guidance, Adversary
  Proceeding requirements, district-court venue). Triage should
  surface these adjacencies when the user's situation spans both
  domains.

- **Voice-anchor → sources.yaml hand-off**: the voice anchors
  named above are the input list for the later `sources.yaml`
  sub-item. Each anchor should produce 1–3 source-views with
  distinct `community_tag` values, hitting the ≥ 8 source-views
  / ≥ 4 distinct community tags minimum from
  [`_schema.md`](../_schema.md) and the V2 §4 per-domain
  checklist. The current framings file flags voice anchors at
  the conceptual community level; concrete URLs and reliability
  scoring are deferred to the `sources.yaml` authoring step.
