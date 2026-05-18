# entrepreneurship — framings.md (Layer 2)

Framing library for `entrepreneurship`. Each entry names one lens — the
way a specific community / tradition / profession argues about a
founding-and-running-a-company decision — and lists the decisions from
[`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

The `entrepreneurship` domain is **high_stakes: false** per
[`_meta_ontology.md` §6](../_meta_ontology.md). Unlike
`personal-finance` / `health-insurance` / `immigration` /
`legal-disputes` / `family-planning`, the Editor posture here is
**decision-support framing rather than uniform Mechanism E deferral**:
failure is the modal outcome (75-90% of startups fail per the standard
CB Insights / Statistic Brain distributions) and is generally
survivable for a knowledge-worker founder who retained a credible
day-job-return path. The dollar swings are large but the
irreversibility profile is fundamentally different from the uniformly-
gated high-stakes domains — most entrepreneurship-domain errors
compress to "lost 12-36 months of opportunity cost plus moderate-to-
large dollar loss", recoverable on a typical 30-year career horizon.
Selective Mechanism E referral applies only to the **six-figure tail-
risk pockets** enumerated in
[`decisions.md` §Notes](./decisions.md) — founder-side startup attorney
on D1 / D5 / D11, S-corp-experienced CPA on D4 / D8, employment-law
attorney on D7 / D11. Where a framing names a statute, rule, or
threshold (IRC §1202 QSBS 5-year-hold, IRC §83(b) 30-day election,
IRC §199A QBI / SSTB phase-out, IRC §409A FMV pricing, IRS Watson v US
2012 reasonable-salary precedent, CA Labor Code §2870 inventions
carve-out, CA Labor Code §16600 non-compete-void, CA AB-5 + ABC test,
FTC 2024 non-compete rule (status in litigation), 11 USC §523 / §727
discharge-and-veil-piercing precedents, SEC Reg D 506(b) / 506(c)
private-placement, Delaware General Corporation Law §141 / §211 /
§220, IRS Form 2553 S-corp election, Form 8832 entity classification
election, Form SS-4 EIN, Form 1099-NEC / W-2 / W-9, Form 5500 for
solo-401(k) > $250k), treat the citation as a pointer to where the
analysis happens, not as the answer.

Three distinct classes of irrevocability drive the entrepreneurship-
domain framing structure and shape every framing below, mirroring the
structure in [`decisions.md`](./decisions.md):

- **Tax-clock-and-election-window one-shot windows**: the 83(b)
  election is a 30-day-from-grant window with no extension and no
  recovery mechanism — missing it converts each future vesting tranche
  into ordinary-income at then-current FMV, which can approach 50%+
  of equity value at a high-growth exit (a tax-poison-pill that has
  killed founder net-worth on otherwise-successful outcomes). The
  QSBS Section-1202 5-year-hold-period starts at C-corp stock
  issuance — NOT at SAFE issuance, NOT at LLC formation, NOT at the
  founder's first day of work — and 18-24 months of SAFE-sitting
  silently delays the clock with no warning from generic CPAs. IRS
  Form 2553 S-corp election must be filed within 75 days of the
  beginning of the tax year for the election to apply to that year
  (later-year retroactive elections require Rev Proc 2013-30 relief
  with cause-statement). The cumulative effect is a set of timing
  decisions that cannot be redone after their windows close.
- **Cap-table-and-equity-allocation permanence**: equity issued is
  effectively impossible to claw back without consideration or for-
  cause termination — over-granting advisor or co-founder equity in
  the first 90 days is the modal founder regret. SAFEs with MFN
  clauses auto-upgrade to the best subsequent terms; stacking 5+
  SAFEs at various caps causes silent multiplied dilution at
  conversion that founders routinely miscalculate. Pro-rata side-
  letters compound across rounds. Cap-table mistakes don't reverse
  cleanly; they get repapered at the next round at the cost of
  additional dilution and negotiated buybacks.
- **Worker-classification-and-IP-assignment irrevocability**:
  misclassifying a CA employee as 1099 contractor under AB-5 / ABC
  test creates exposure that ages with the lookback period (typically
  4 years CA statute-of-limitations, longer with continuing
  violation theory) and cannot be cured by re-classifying going
  forward — back-wages, payroll-tax-liability, PAGA penalties
  ($100/pay-period/employee initial, $200 subsequent), waiting-time
  penalties under CA Labor Code §203 (up to 30 days additional
  wages), attorney fees, and interest stack to many-fold the original
  unpaid compensation. CIIAA IP-assignment carve-outs from a prior
  W-2 employer must be documented before founder work begins on the
  carved-out IP — retrospectively claiming a carve-out at exit, when
  the prior employer's interest is most concentrated, is the
  litigation-loss pattern that has destroyed founder net-worth at
  acquisition.

Framings that handle one of these classes well often miss the others;
the opposing-framing pairs below frequently divide along the
tax-clock-window / cap-table-permanence / IP-assignment-irrevocability
boundaries.

Voice anchors (conceptual, not source URLs — those live in
`sources.yaml` once authored): **Indie Hackers voice**
(indiehackers.com community, podcast and forum, bootstrapped-SaaS
case studies, MRR transparency culture, anti-VC default, "stay small
and profitable" ethos); **r/Entrepreneur voice** (Reddit subreddit
with mixed-quality signal — strong on small-business mechanics and
side-project economics, weaker on venture-scale strategy); **r/Small
Business voice** (Reddit subreddit, brick-and-mortar plus services
plus retail, regulatory-compliance focus, payroll and worker-
classification ground truth from in-the-trenches operators);
**Hacker News startup voices** (news.ycombinator.com Show HN and
Ask HN threads, Paul Graham essays at paulgraham.com — *Do Things
That Don't Scale*, *Default Alive or Default Dead*, *Maker's
Schedule, Manager's Schedule*, *Founder Mode*; Sam Altman essays at
blog.samaltman.com — *Startup Playbook*, *How To Be Successful*;
Garry Tan / Initialized commentary on YC X-cohorts); **Patio11 /
Patrick McKenzie voice** (Bingo Card Creator post-mortem, Stripe
Atlas founder docs, Kalzumeus blog — anti-platitude "calling a wave
of fans does not produce $4MRR", first-principles thinking on
software-business economics, pricing-as-load-bearing-decision,
salary-negotiation-for-founders, Japan-Form-Tax-Treaty edge cases);
**YC playbooks voice** (How To Start A Startup CS183B Stanford
lectures, YC Startup School curriculum, YC Library at
ycombinator.com/library — Jessica Livingston / Michael Seibel /
Dalton Caldwell / Aaron Epstein — Series-A advice, ramen-profitability
metric, the "default alive" question, focus-and-talk-to-users
discipline); **SaaStr / Jason Lemkin voice** (saastr.com, SaaStr
Annual, Jason's daily blog and podcast — SaaS metrics dogma: ARR /
NRR / CAC payback / LTV-to-CAC / Magic Number, $1-10M ARR-as-the-
hard-part, sales-led-growth-vs-product-led-growth, BDR / SDR /
AE / CSM hiring sequence); **Tomasz Tunguz / Redpoint blog voice**
(tomtunguz.com, Redpoint-portfolio data — Series-A burn-multiple
benchmarks, sales-efficiency metrics, AI-startup pricing model
analysis, board-meeting deck templates); **Lenny Newsletter voice**
(lennysnewsletter.com Lenny Rachitsky — product / PM growth-loops,
B2B-vs-B2C product metrics, hiring playbooks, OKR templates, user
research patterns); **First Round Review voice** (firstround.com/review
— operator-interview format from FR-portfolio executives, hiring /
management / scaling tactical playbooks, IC-to-VPE transitions);
**a16z growth essays voice** (a16z.com — growth-stage thinking,
network-effects taxonomy, PMF measurement frameworks, marketplaces
chicken-and-egg); **Founder Collective voice** (David Frankel /
Eric Paley — anti-venture-trap commentary, "venture-as-debt"
framing, capital-efficiency as competitive moat); **The Finance
Buff voice** (thefinancebuff.com Harry Sit — solo-401(k) plan-
document analysis for Mega-Backdoor-Roth eligibility, SEP-IRA-vs-
solo-401(k) pro-rata-trap mechanics, S-corp W-2-vs-distribution
arithmetic — this voice is shared with `personal-finance` framings.md
and carries the same procedural-floor authority on tax-mechanic
disputes); **Clerky voice** (clerky.com founder-stage incorporation
docs — Delaware C-corp formation templates, 83(b) filing
instructions and certified-mail mechanics, SAFE templates and
counter-signature flow, option-grant docs and 409A coordination);
**Stripe Atlas voice** (stripe.com/atlas — Delaware C-corp formation
for non-US-resident founders, Mercury Bank coordination, founder
agreement boilerplate, founder community Slack); **IRS-publication-
authority voice** (Pub 535 business expenses, Pub 583 starting a
business, Pub 587 home-office deduction, Pub 463 travel /
entertainment, Pub 15 employer-tax-guide; Pub 590-A IRA basis,
Pub 590-B IRA distributions, Pub 560 retirement plans for small
business — overlapping with `personal-finance` framings.md ground
truth on retirement-plan mechanics); **state-bar lawyer-referral-
service voice** (state-bar lawyer-referral-services NOT for-profit
finders; California Lawyers Association Business Law Section;
American Bar Association Section of Business Law) as the $0-
friction procedural floor for any individual attorney recommended;
**SEC EDGAR / FINRA BrokerCheck voice** (sec.gov/cgi-bin/browse-edgar
for any institutional investor's Form D filings, brokercheck.finra.org
for any individual broker-dealer recommendation) for diligence on
any institutional-investor or broker recommended.

Cross-domain edges: F1 (raise-and-scale) carries the principal cross-
cutting role into `personal-finance` (D2 founder-stock 83(b) election
and QSBS Section-1202 clock-start at conversion, NOT at SAFE
issuance — load-bearing tax-tail), `tech-career` (D3 employer-IP-
assignment carve-out from prior W-2, golden-handcuffs RSU-cliff cost
of leap), and `housing` (HELOC / cash-out-refi as bridge capital,
mortgage qualification with 1099 / S-corp distribution income that
lenders treat with sharply higher scrutiny). F4 (SE-tax-and-entity-
arbitrage) routes into `personal-finance` (solo-401(k) employee
deferral on W-2 salary vs SEP-IRA on net SE earnings — the S-corp
election trade-off; QBI Section-199A reduction by W-2 salary
portion; pro-rata-IRA-trap on backdoor-Roth from SEP balance), and
`housing` (mortgage-qualification with S-corp-distribution income
discounted 75% with 2 years of returns required). F5 (QSBS-and-tax-
tail-event) routes into `personal-finance` heavily (Section 1202
$10M-or-10x-basis gain exclusion, 5-year-hold-period and "originally
issued" stock requirement, federal-state divergence on QSBS — CA
does NOT conform, NY and NJ do not fully conform), and `legal-
disputes` (QSBS reset-on-incomplete-stock-issuance disputes). F7
(ABC-test-and-worker-classification) routes into `legal-disputes`
heavily (CA PAGA Private Attorneys General Act exposure, wage-and-
hour class-action precedent, FTC 2024 non-compete rule status in
litigation), and `tech-career` (founder hiring former W-2 colleague
with non-compete from prior employer). F6 (liability-shield /
corporate-veil) routes into `legal-disputes` (piercing-the-corporate-
veil precedents, fraudulent-conveyance look-back, undercapitalization
defense), `personal-finance` (umbrella-policy coordination with
business E&O and D&O), and `housing` (LLC-titled-real-property and
mortgage-due-on-sale-clause interaction). F8 (day-job-fallback /
opportunity-cost) routes into `tech-career` (the day-job-fallback-
option-value erodes with time-away-from-market; deep-tech roles
have a 12-24-month freshness window; golden-handcuffs from RSU
vesting cliffs create implicit per-month opportunity cost), and
`personal-finance` (Roth-conversion window opens in a low-income
year; emergency-fund sizing and asset-allocation shifts when
household income drops). F11 / F12 (founder-mode vs manager-mode)
route into `tech-career` (the founder's recruitment voice as
hiring asymmetry; founder-led-hiring vs delegated-hiring at scale).
Routing across edges is V2-Triage's job; these edges help framings
name adjacent domains rather than absorb their content.

---

## 1. Raise-and-scale / venture-capital framing

- **Decisions it applies to**: D2 (bootstrap vs raise — the central
  decision-input), D5 (SAFE vs priced seed — the instrument choice
  once raising is decided), D10 (first-employee-vs-contractor-vs-
  offshore — where venture funding enables US-W-2-senior hires the
  bootstrap path cannot afford), and D1 secondarily (co-founder
  equity structuring assumes a venture-trajectory cap-table with
  10-20% option pool reserved for hiring).
- **Mental model summary**: Time-to-product-market-fit is the
  binding constraint, and outside capital is *fuel that compresses
  calendar time* by enabling parallel experimentation (multiple
  builds, multiple growth-marketing channels tested in parallel,
  multiple senior hires onboarded simultaneously) that bootstrap
  forces serially. The framing reasons in venture-portfolio-math
  terms: ~1-in-10 of seed-funded companies returns the fund at
  10x+, so the framing pre-commits to the swing-for-the-fences
  trajectory and accepts that lifestyle-business outcomes ($5M-ARR-
  comfortable) are *failures* relative to the implicit venture
  contract. Implementation: raise pre-seed $500k-1M to compress
  the team-formation phase; raise priced seed $2-4M once early
  signal appears (10-50 customers, $20-100k MRR, or strong
  qualitative signal); raise Series A $8-15M at $40-60M post on
  $1-3M ARR with 3x+ YoY growth. Characteristic move: build the
  3-year burn-and-hiring plan against a target ARR-curve, then
  raise enough capital + 25-50% buffer for the plan; default to
  taking the highest-quality lead investor's term sheet at the
  cap they offer, then optimize secondary terms. Anchor: pre-seed
  $500k on 5M post = 10% dilution; seed $2M on 12M post = ~17%
  additional; Series A $10M on 40M post = ~25% additional;
  founders who do all three rounds with no unusual amounts
  retain ~50-55% combined pre-Series-B.
- **Characteristic vocabulary**: "default alive vs default dead",
  "venture-scale outcome", "PMF first then scale", "compress
  time-to-PMF", "burn multiple", "Magic Number", "CAC payback
  period", "LTV-to-CAC ratio", "NRR (net revenue retention)",
  "ARR ramp / triple-triple-double-double-double", "Rule of 40",
  "the next round is always closer than you think", "fundraising
  is full-time job for the CEO", "lead investor sets the terms",
  "post-money cap on YC SAFE", "Series A signal threshold",
  "board-of-directors composition post-A."
- **Excludes**:
  - The "raise to compress time-to-PMF" reflex assumes capital
    actually *accelerates* the PMF discovery — but pre-PMF spend
    typically discovers the wrong thing faster, not the right
    thing faster (hiring 5 engineers to build a thing nobody
    wants takes 6 months instead of 18 months but ends in the
    same dead-end). The framing under-engages with the *what to
    spend on* problem at pre-PMF and routinely produces well-
    funded companies that ran out of runway without finding
    PMF, a failure mode the bootstrap-default-alive framing
    catches via forced ruthless prioritization. Opposes F2
    (bootstrap / default-alive) on D2.
  - The venture math (~1-in-10 returns the fund) requires that
    founders accept *failure of the company* as the modal
    outcome, but the founder personal-finance and reputation
    consequences of an outright shutdown are routinely
    understated in the "swing for the fences" framing — failed
    venture-backed founders often face investor-relationship
    cost, board-removal-via-protective-provisions, and "the
    company that didn't work" stigma that affects subsequent
    fundraising. The framing's portfolio-thinking is correct at
    the *investor* level but mis-applied at the *founder*
    level where outcomes are concentrated rather than
    diversified. Opposes F13 (optionality-preservation).
  - Institutional capital is *not free* in the dilution
    arithmetic — board seats, information rights, protective
    provisions (investor consent required for sale, debt above
    $X, new equity issuance, material change of business),
    and pro-rata side-letters compound across rounds in ways
    founders systematically under-model. The framing's "take
    the best lead's term sheet" reflex routinely produces
    founders surprised at Series B by the cumulative
    protective-provision lock-in from earlier rounds.
    Founder Collective voice catches this; YC voice often
    doesn't.
  - The framing assumes a *liquid* venture market — but
    venture-funding availability is *cyclical* (2021 ZIRP
    boom collapsed to 2023-2024 pullback; sub-Series-A
    rounds in cyclical-downturns can take 6-12 months and
    require 100+ investor meetings; the "raise quickly and
    focus on building" timeline assumes market conditions
    that do not hold across cycles). The framing's
    24-month-runway-target-against-known-burn calculus needs
    explicit market-condition awareness; SaaStr / Lemkin
    voices catch the cyclicality, YC playbooks often
    abstract it. Boundary `tech-career` on layoff-cycle
    interaction.

## 2. Bootstrap / default-alive framing

- **Decisions it applies to**: D2 (bootstrap vs raise — the
  central decision-input), D3 (quit day job vs nights-and-weekends
  — the signal-threshold for the leap when no outside capital
  cushions the risk), D9 (pricing model selection — where the
  bootstrap path forces price discipline because unit-economics
  must work from day 1, not "at scale"), and as a meta-framing
  on D10 (first hire — bootstrap forces ruthless prioritization
  of cash-positive hires over cultural-foundation hires the
  venture path can absorb).
- **Mental model summary**: Calendar-time-on-revenue is the
  founder's most-valuable asset and the only one that
  compounds — every additional month spent learning what
  customers will actually pay for is irreplaceable, while
  capital can be raised later (and at materially better terms
  once revenue is established). The framing reasons in unit-
  economics-from-day-1 terms: if CAC > LTV at small scale,
  scaling the model worsens the problem; ramen-profitability
  ($50-100k MRR covering founder + co-founder modest salary
  plus modest hosting / tools / contractor budget) is the
  signal that the business is *real* and unlocks the
  fundraising-from-leverage option without the desperation
  discount. Implementation: charge customers from day 1 (no
  freemium-to-postpone-pricing-decision); minimize fixed
  costs (founder-as-only-employee for 12-18 months is
  default, not exception); take customer money as the
  validation signal that the product is real; expand only
  out of organic cash flow; raise from a position of strength
  ("we don't need this money") or not at all. Characteristic
  move: Paul Graham's *Default Alive or Default Dead* test —
  if you continue your current growth-and-burn rate, do you
  reach profitability before running out of money? If yes,
  default alive (no need to raise); if no, raise or change
  the trajectory. Anchor: most SaaS / service / niche-B2B
  businesses can sustain founder + small team on $200k-$1M
  ARR; this is a *fine outcome* and does not require the
  venture-portfolio math (Patio11 / Indie Hackers voice on
  this).
- **Characteristic vocabulary**: "default alive vs default
  dead", "ramen-profitable", "bootstrap to revenue", "unit
  economics must work at small scale", "the customer is the
  best investor", "calendar-time-on-revenue is irreplaceable",
  "raise from a position of strength", "venture trap",
  "lifestyle business as a feature not a bug", "$1M ARR is
  fine", "MRR transparency", "ProfitWell metrics", "burn
  multiple < 1.0", "capital efficiency as moat", "$10M ARR
  with 5 employees", "no-meeting-week", "small-team
  productivity premium."
- **Excludes**:
  - The "raise from a position of strength or not at all"
    posture works when the market opportunity is durable and
    competitor capital-intensity is low — but in network-
    effects-heavy categories (marketplaces, social,
    payments, B2B-with-procurement-stickiness), losing 18
    months of growth velocity to bootstrap-pace can hand the
    category to a venture-backed competitor that achieves
    irreversible distribution advantage. The framing's
    "calendar-time-on-revenue" reasoning understates the
    *category-specific* time-pressure where winner-take-most
    dynamics apply. Opposes F1 on D2.
  - The "unit economics must work at small scale" reflex
    correctly catches the unit-economics-rationalization
    pattern (companies that "lose money on every sale but
    make it up in volume"), but it under-engages with the
    legitimate-investment-phase distinction — there are
    real categories where customer acquisition is structurally
    cheaper at scale (network-effects-driven referral, content-
    SEO compounding, brand-equity ROI on enterprise sales)
    and the small-scale unit-economics are *expected* to be
    worse than at scale. The framing risks dismissing
    legitimate scale-dependent business models as
    "rationalization." Boundary `personal-finance` on
    capital-efficiency framing.
  - Bootstrap forces *founder personal-runway compression*
    — the founder's 18-24-month personal savings are
    functionally a $X/year personal-salary forgone
    investment in the business, and the framing rarely
    surfaces this implicit-cost or the household-risk-
    bearing-capacity (single-income-with-kids-and-mortgage
    vs dual-income-no-dependents) constraint that
    determines whether bootstrap is even feasible. Indie
    Hackers voice tends to assume single-no-dependents;
    r/Entrepreneur voice catches the household-context
    constraint better. Boundary `personal-finance` D2.
  - "Ramen-profitability" as the success metric encourages
    *under-investment in growth* when growth would have
    durably increased enterprise value — founders happily at
    $40k MRR for 3 years may be missing the legitimate
    moment to hire 2 growth engineers and accelerate to
    $200k MRR. The framing's "small-team productivity premium"
    can rationalize the *under*-investment side just as F1
    rationalizes the over-investment side. Opposes F14
    (conviction-commitment) on growth-rate-as-success-signal.

## 3. Founder-fairness-and-vesting framing

- **Decisions it applies to**: D1 (co-founder selection and
  equity structuring — central), D11 (co-founder departure /
  cap-table-buyback — where the vesting-and-acceleration
  structure determines what the departing founder owns), and
  as a meta-framing on D10 (early-employee equity grants
  follow the same vesting / acceleration / IP-assignment
  conventions established for co-founders).
- **Mental model summary**: Equity is the *durable mechanism
  for aligning founder incentive with company outcome over
  the 4-10-year build cycle*, and getting the structure right
  up-front prevents most founder-relationship-failure modes
  that destroy companies pre-PMF. The framing reasons in
  vesting-as-fairness terms: 4-year vesting with 1-year cliff
  is market-standard because it gives both founders a year
  to confirm fit before equity becomes irrevocable, and
  monthly vesting afterward smooths the cliff. Double-trigger
  acceleration on change-of-control protects founders against
  acquirer-fires-them-post-close while preserving acquirer
  ability to retain key talent; single-trigger is rare and
  acquirer-hostile. The CIIAA Confidential-Information-and-
  Invention-Assignment Agreement is the load-bearing IP
  document; prior-art carve-outs (what each founder is
  bringing in from prior work that the company does NOT
  own) must be enumerated explicitly in writing at signing,
  because retroactively claiming a carve-out at exit is the
  litigation-loss pattern. Noam Wasserman's *Founder's
  Dilemmas* data shows 50/50 splits correlate with higher
  post-Series-A founder-conflict; vesting-asymmetric with
  the same end-state but different cliffs / acceleration is
  the more honest framing when contributions are genuinely
  asymmetric. Characteristic move: structure the cap-table
  + vesting + IP-assignment + 83(b) election before issuing
  any stock; treat the 30-day 83(b) window as a hard
  deadline; document prior-IP carve-outs in writing on day
  one. Anchor: 83(b) election is filed via certified mail
  to IRS service center within 30 days of grant date (not
  incorporation date), with copy attached to the founder's
  personal 1040 for that year; missing it converts each
  vesting tranche to ordinary-income at then-current FMV.
- **Characteristic vocabulary**: "4-year vesting with 1-year
  cliff", "double-trigger acceleration on change-of-control",
  "single-trigger acceleration is acquirer-hostile", "CIIAA
  Confidential-Information-and-Invention-Assignment", "prior-
  inventions schedule", "California Labor Code §2870 carve-
  out", "83(b) election 30-day window", "founder restricted
  stock", "reverse-cliff for asymmetric contribution", "good
  reason resignation", "for-cause termination definition",
  "Wasserman's Founder's Dilemmas", "Noam Wasserman 50/50
  data", "buyback at FMV via right of first refusal", "401(k)
  is the company's plan, founder is just another participant."
- **Excludes**:
  - The "4/1 vesting standard with 83(b)" reflex assumes the
    founders are W-2 employees of a Delaware C-corp issued
    founder restricted stock at incorporation — but LLC-
    formed companies issue *membership interests* (not
    stock), and 83(b) elections on LLC profits-interests vs
    capital-interests have materially different mechanics
    (Rev Proc 93-27 safe-harbor for profits-interests; capital-
    interests get 83(b) like restricted stock); founders
    converting LLC to C-corp later face complex tax-
    consequence analysis on the entity-change. The framing's
    Delaware-C-corp-default obscures the LLC-or-S-corp-then-
    convert path that bootstrap founders often take.
    Boundary `personal-finance` D6 on 83(b) mechanics.
  - "50/50 splits correlate with higher post-Series-A
    conflict" is a *statistical correlation* in Wasserman's
    data, not a causal mandate to avoid 50/50 — many
    successful companies have 50/50 splits, and forcing
    asymmetry where contributions are genuinely equal
    creates its own resentment cost. The framing's "asymmetric
    vesting is more honest" advice can produce founder-
    relationship damage when applied to genuinely-equal
    contributions. The Indie Hackers / r/Entrepreneur voice
    leans 50/50-is-fine; the YC playbook voice leans away.
    Both framings are defensible.
  - The framing under-engages with *post-incorporation co-
    founder addition* — bringing in a "technical co-founder"
    4 months after incorporation when the existing founders
    are 4/48 vested into their grant requires either (a)
    granting the new co-founder a fresh 4-year-vesting grant
    starting at their join date (which means they will be
    under-vested relative to the original founders for years),
    (b) restructuring the original founders' grants to align
    vesting starts (creates new 83(b) windows for the
    original founders that may already be past 30 days), or
    (c) treating the new co-founder as an early-employee with
    standard option pool grant instead of co-founder equity
    (which under-aligns incentive). All three have non-trivial
    trade-offs the framing rarely surfaces. Boundary
    `legal-disputes` D11.
  - "For-cause termination" is the load-bearing legal text
    in any departure scenario, and the standard founder
    agreement template often leaves it vague — "fraud,
    willful misconduct, material breach" without enumerating
    specific behavioral triggers — which becomes the dispute
    ground when a founder is asked to leave for performance
    or culture reasons that don't clearly meet "willful
    misconduct." The framing's "use the standard agreement"
    reflex passes through the vagueness; the load-bearing
    move is to negotiate explicit triggers and remedies at
    signing, when relationships are positive and counsel is
    cheap. Boundary `legal-disputes`.

## 4. SE-tax-and-entity-arbitrage framing

- **Decisions it applies to**: D4 (LLC pass-through vs S-corp
  election — central), D6 (sole-prop vs LLC formation timing
  — entity-choice precedes tax-election), D8 (solo-401(k) vs
  SEP-IRA vs SIMPLE — the retirement-vehicle math depends
  critically on the W-2-salary-vs-net-SE-distribution split
  the S-corp election creates), and as a meta-framing on D7
  (first W-2 employee triggers the founder's own W-2-vs-1099
  classification clarification — founders of S-corps must be
  W-2 employees of their own company per Watson v US).
- **Mental model summary**: Self-employment income subjects
  the founder to *15.3% FICA* (Social Security 12.4% on first
  $168,600 of net SE earnings in 2025 wage base + Medicare
  2.9% uncapped, plus 0.9% Additional Medicare for high
  earners above $200k single / $250k MFJ) — this stacks on
  top of ordinary income tax and represents the largest
  recoverable tax-leak for founders crossing the ~$80-150k
  net SE income threshold. The S-corp election (filed via
  IRS Form 2553 within 75 days of the tax year for in-year
  effect; later requires Rev Proc 2013-30 relief) splits net
  income into (a) reasonable W-2 salary subject to FICA, and
  (b) distributions exempt from FICA — saving 15.3% × the
  distribution portion. Reasonable-salary defensibility per
  IRS Watson v US (8th Cir 2012) — a CPA paid himself $24k
  on $200k+ S-corp net income, IRS reclassified $67k as
  additional salary subject to FICA, the court upheld — sets
  the load-bearing constraint: salary too low triggers audit
  reclassification; salary too high gives up the arbitrage.
  The Section §199A QBI deduction interacts non-trivially:
  20% pass-through deduction is reduced by S-corp reasonable
  salary (which is W-2, not QBI), so a high-salary-low-
  distribution split reduces both SE tax AND QBI deduction;
  for SSTB founders (consulting, law, accounting, health —
  the "specified service trade or business" categories phasing
  out at $241,950 single / $483,900 MFJ 2024 thresholds —
  verify 2025) the QBI deduction phases out entirely above
  the threshold, eliminating that side of the trade-off.
  State-S-corp recognition varies (CA 1.5% S-corp tax with
  $800 minimum; NY-NYC unincorporated business tax stacks;
  TN franchise tax; LA / DC do not recognize S-corp election
  at state level — taxes as C-corp). Implementation: model
  break-even by state, net-income, SSTB-status, and target
  retirement-contribution; file Form 2553 within 75 days of
  the target tax year; set up payroll service (Gusto /
  Justworks / Rippling) to handle W-2 mechanics; document
  reasonable-salary benchmark via RCReports or BLS data
  before the first audit. Characteristic move: a CPA with
  S-corp / multi-state / startup experience (NOT a generic
  1040-prep CPA) models the trade-off explicitly with
  current-year and 3-year projections.
- **Characteristic vocabulary**: "self-employment tax 15.3%",
  "Social Security wage base $168,600 2025", "Medicare 2.9%
  uncapped + 0.9% Additional Medicare", "Form 2553 S-corp
  election", "75-day window from tax year", "Rev Proc 2013-30
  late-election relief", "reasonable salary per Watson v US",
  "RCReports benchmark", "BLS Occupational Employment Survey",
  "S-corp distribution portion exempt from FICA", "QBI
  Section-199A 20% deduction", "SSTB phase-out", "specified
  service trade or business", "California 1.5% S-corp tax +
  $800 minimum", "NY-NYC unincorporated business tax", "the
  $80-100k crossover (state-dependent)", "Schedule SE 1040",
  "Schedule C sole-prop", "K-1 partnership distribution."
- **Excludes**:
  - The "$80-100k crossover" heuristic is *state-and-
    practice-dependent* and the framing's clean break-even
    presentation hides material variance: CA-with-1.5%-S-corp-
    tax pushes the crossover to ~$100-120k; TX-with-no-state-
    income-tax brings it down to ~$60-80k; SSTB founders
    above the QBI phase-out threshold lose the QBI deduction
    entirely and re-shift the trade-off. Generic-CPA voices
    on Reddit / personal-finance subforums commonly quote
    "$80k" without state-and-SSTB adjustment. Boundary
    `personal-finance` D4 / D7.
  - S-corp election interacts adversely with *retirement-
    contribution maximization* — sole-prop with $200k net
    income can contribute $23,500 employee deferral + ~$36k
    profit-sharing = $59.5k solo-401(k); S-corp at $200k net
    paying $60k W-2 + $140k distribution can contribute
    $23,500 + $15k = $38.5k (profit-sharing capped at 25% of
    W-2 salary). The S-corp election SAVES SE tax but COSTS
    retirement-contribution capacity — the joint optimization
    is non-trivial and CPA-supported. The framing's "elect
    S-corp at $80k" reflex understates this trade-off,
    particularly for founders trying to maximize tax-
    advantaged retirement savings. Boundary `personal-finance`
    D8.
  - "Reasonable salary" defensibility is *practice-dependent*
    — IRS audit attention concentrates on S-corps paying
    obviously-low salaries (sub-$30k on six-figure-net-income
    is the high-audit-risk pattern), but the safe-zone is
    not a bright line and IRS audit-trigger-rules are not
    public. RCReports and BLS Occupational Employment Survey
    provide *defensible* benchmarks but do not guarantee
    safety; a founder choosing a salary at the bottom of the
    benchmark range is more exposed than one at the median.
    The framing's "use RCReports" reflex understates that
    audit-risk is non-binary and depends on the specific
    occupation, industry, and pattern of comparables. Watson
    v US is the leading authority but the universe of post-
    Watson IRS audit-and-litigation patterns is broader than
    the case itself.
  - The framing assumes the founder's W-2-vs-1099 status is
    *clear* — but founders of multi-member LLCs who are
    *also* W-2 employees of the LLC face material complexity
    (member-managers in some states cannot be W-2 employees
    of the same LLC; partnerships generally cannot pay
    members W-2 wages — must use guaranteed payments under
    IRC §707(c) instead, which have different FICA treatment
    than W-2 salary). Multi-member-LLC tax treatment as
    partnership (Form 1065 with K-1 to each member) has its
    own arbitrage geometry that the single-member-LLC-to-
    S-corp framing skips. Boundary `legal-disputes` on
    partnership disputes.

## 5. QSBS-and-tax-tail-event framing

- **Decisions it applies to**: D1 (co-founder selection — the
  "originally issued" requirement for QSBS means stock must
  be issued from C-corp directly to the founder, not bought
  on secondary; 83(b) election interacts with QSBS holding
  period), D4 (LLC pass-through vs S-corp election — QSBS
  requires C-corp; LLC must convert to C-corp to start the
  clock and conversion mechanics matter), D5 (SAFE vs priced
  seed — the QSBS 5-year-hold-period starts at C-corp stock
  issuance, NOT at SAFE issuance — load-bearing tax tail),
  D8 (solo-401(k) vs SEP — high-balance solo-401(k) plus QSBS
  exit can together cap retirement-side gain exclusion).
- **Mental model summary**: IRC Section 1202 Qualified Small
  Business Stock provides federal-income-tax exclusion of up
  to $10M or 10x adjusted basis (whichever is *greater*) on
  gain from sale of qualifying stock — meaning a founder
  with $1M basis can exclude up to $10M of gain, a founder
  with $5M basis can exclude up to $50M. For high-growth
  exits this is among the largest single tax benefits in the
  US Internal Revenue Code, and getting the eligibility
  mechanics right is the highest-leverage tax-tail decision
  available to a founder. Eligibility requirements (all
  must be met): (1) stock acquired directly from the
  issuing C-corp ("originally issued") in exchange for cash,
  property, or services — NOT acquired on secondary market;
  (2) corporation has aggregate gross assets ≤ $50M at and
  immediately after issuance (TCJA-era proposals to raise
  this to $75M have not passed); (3) corporation is a
  domestic C-corp throughout substantially-all of the
  holding period; (4) corporation conducts an active trade
  or business (not investment / financial / hospitality /
  farming — see §1202(e)(3) excluded businesses, where most
  professional-services excluded categories sit); (5) holder
  holds for at least 5 years before sale; (6) stock is held
  as a stock, NOT through an intermediate entity like an
  LLC. State conformity is *uneven*: federal §1202 fully
  excludes; CA does NOT conform (CA taxes the federally-
  excluded gain at full state ordinary rates); NY partially
  conforms; NJ does not fully conform; TX has no state
  income tax so conforms trivially. The 5-year-hold-period
  starts at C-corp stock issuance — *NOT at SAFE issuance,
  NOT at LLC-to-C-corp conversion in a way that doesn't
  satisfy original-issuance, NOT at option-grant before
  exercise* — and is the load-bearing planning question.
  Founders sitting on SAFEs for 18-24 months pre-priced-
  round are losing 18-24 months of QSBS clock; if a priced
  round is foreseeable within 6 months, accelerating
  conversion via a formal priced round (vs continuing on
  SAFE) can preserve QSBS clock — among the highest-leverage
  tax considerations for founder eventual-exit-net-worth
  and almost universally missed by non-startup-CPAs.
  Characteristic move: at every cap-table event (formation,
  SAFE issuance, priced round, option exercise, secondary
  sale, stock split, M&A) ask "what does this do to QSBS
  eligibility and clock?"; consult a startup-experienced CPA
  or tax attorney; track holding period explicitly with
  basis records.
- **Characteristic vocabulary**: "IRC §1202 QSBS gain
  exclusion", "$10M or 10x basis (whichever greater)",
  "5-year hold period", "originally issued stock requirement",
  "$50M aggregate gross assets at and immediately after
  issuance", "active trade or business §1202(e)(3) excluded
  categories", "QSBS clock doesn't start on SAFE", "QSBS
  clock starts at C-corp stock issuance", "stacking via
  gifts to family members", "Section 1045 rollover to new
  QSBS within 60 days", "California does NOT conform to QSBS",
  "federal-state conformity table for §1202", "track basis
  with each cap-table event", "redemption-tests that
  disqualify QSBS", "$10M family limit", "stacking strategies
  via non-grantor trusts."
- **Excludes**:
  - The "5-year hold from C-corp stock issuance" reflex
    catches the SAFE-conversion-delay case but routinely
    misses *redemption tests that disqualify QSBS*: §1202(c)(3)
    and (4) disqualify stock if the corporation makes
    significant redemptions of its own stock from the issuing
    shareholder (within 1 year before or after) or from
    other shareholders (within 4-year-window-2-years-before-
    and-2-years-after-issuance, threshold 5% of aggregate
    value); buyback programs and tender offers can silently
    disqualify QSBS for all shareholders. The framing's
    clock-discipline alone doesn't catch redemption-disqualification
    — this is among the most-litigated QSBS edge cases.
    Boundary `legal-disputes` on QSBS reset disputes.
  - The "$10M or 10x basis" limit is *per-issuer-per-
    taxpayer*, but families can *stack* the limit across
    family members and across non-grantor trusts — a
    founder with $50M+ projected gain can split equity
    pre-issuance to spouse, kids (via non-grantor trusts to
    avoid attribution), or to multiple non-grantor trusts,
    each of which gets a separate $10M exclusion. The
    framing's solo-founder reflex misses the stacking
    geometry that can multiply the exclusion 3-10x for
    high-tail-outcome cases. Requires estate-attorney
    coordination at formation, NOT at exit (post-exit
    stacking is materially harder). Boundary
    `personal-finance` D10 and `family-planning`.
  - LLC-to-C-corp conversion mechanics are *non-trivial for
    QSBS* — the conversion is generally a Section 351 tax-
    free exchange (LLC members exchange membership interests
    for C-corp stock), but the QSBS holding-period and
    "originally issued" requirements interact in ways CPAs
    routinely get wrong. The IRS has held that stock received
    in a §351 exchange from a *qualifying* property can
    inherit QSBS treatment if the underlying property would
    have been QSBS-eligible, but the LLC interest being
    exchanged is not stock and the analysis turns on whether
    the LLC was conducting an active trade or business that
    qualifies. Founders converting LLC to C-corp for QSBS
    purposes should expect the conversion analysis to require
    startup-experienced CPA and tax attorney coordination,
    NOT just generic CPA filing of conversion docs. Boundary
    `personal-finance` D1.
  - State-conformity divergence is *load-bearing for founders
    in non-conforming states* — California's NON-conformity
    means a CA-resident founder with $10M federally-excluded
    QSBS gain still pays CA state ordinary rates (top
    bracket 13.3% — so $1.33M state tax on the "tax-free"
    federal exit). The framing's "QSBS is tax-free" reflex
    is *only correct at the federal level* for CA / non-
    conforming-state residents. The recovery move is
    residency-planning before the liquidity event — but
    California treats residency tests strictly and 1-2-year-
    pre-exit relocations are scrutinized. Boundary
    `personal-finance` F4 and `housing` on residency
    planning.

## 6. Liability-shield / corporate-veil framing

- **Decisions it applies to**: D6 (sole-prop vs LLC formation
  — the shield is the primary functional benefit of an LLC),
  D7 (first W-2 employee — entity formation typically
  precedes hiring because the LLC is the contracting and
  employing entity), D10 (offshore-direct-contractor vs EOR
  vs staffing-agency — EOR shifts liability to EOR, direct
  exposes the company to local-jurisdiction labor law), and
  as a meta-framing on D1 (CIIAA / IP-assignment is the
  parallel "veil" for intellectual property — the formal
  structure that determines whether the company actually
  owns the IP the founders built).
- **Mental model summary**: The LLC and C-corp limited-
  liability shield separates personal assets from business
  obligations — members / shareholders are not personally
  liable for entity debts and judgments, with material
  exceptions: (a) piercing-the-corporate-veil for
  undercapitalization, commingling personal and business
  funds, failure to follow corporate formalities (annual
  reports, separate bank accounts, signed-as-entity not as
  individual), or alter-ego use; (b) personal guarantees on
  contracts or debt (most early-stage SBA loans and
  commercial leases require personal guarantee, eviscerating
  the shield for those obligations); (c) direct-tort by the
  member (a member personally driving negligently, even on
  company time, is personally liable for the tort); (d)
  fiduciary-breach by officers / directors (D&O exposure);
  (e) trust-fund taxes (payroll withholding, sales tax) are
  *personally collectible* from "responsible persons" under
  IRC §6672 and state-trust-fund statutes regardless of
  entity. The framing reasons in *which-risk-surface, which-
  formality, which-shield-exception* terms: physical-premises
  business with customer foot traffic and slip-and-fall risk
  → LLC + general-liability insurance + workers-comp; solo
  software consulting → LLC + professional E&O insurance
  (the shield does little; the contract clauses do most of
  the work); pure online newsletter business → DBA may
  suffice; licensed-professional (lawyer, doctor, architect)
  → professional-liability is not shielded by entity,
  malpractice insurance is the primary protection. State-
  fee variation matters: CA $800/year minimum franchise tax
  regardless of income; NY publication requirement
  $1,000-$2,000 one-time; DE $300 annual report + registered-
  agent; TX no franchise tax until $1.23M revenue (2024) but
  annual public-information report. Characteristic move:
  before forming, identify the specific liability surface(s),
  match the entity form to those surfaces, and acquire
  appropriate insurance (general-liability, professional-
  E&O, D&O at funded-company stage, cyber for data
  handlers, employment-practices-liability when employees
  are hired). Anchor: separate business bank account + EIN
  + clean books = the minimum hygiene that preserves the
  shield; commingling personal and business funds is the
  fastest way to pierce the veil even when an LLC exists.
- **Characteristic vocabulary**: "limited-liability shield",
  "piercing the corporate veil", "alter-ego doctrine",
  "undercapitalization defense", "commingling of personal
  and business funds", "corporate formalities", "personal
  guarantee on lease / loan", "general partner unlimited
  liability vs LLC member shield", "trust-fund taxes
  collectible from responsible persons (IRC §6672)", "direct-
  tort by the member", "professional liability not shielded
  by entity", "D&O directors-and-officers insurance",
  "general-liability insurance", "professional-E&O", "cyber-
  liability", "employment-practices-liability EPLI", "CA
  $800 franchise tax", "NY publication requirement", "DE
  registered-agent service", "homestead exemption (for
  founder personal assets)", "EOR Employer-of-Record
  liability shift."
- **Excludes**:
  - The framing's "form an LLC for the shield" reflex
    overstates the protection benefit for *solo software
    consulting and other low-liability-surface businesses*
    where the shield does little — the work-product is the
    only liability surface, and a well-drafted contract E&O
    clause + professional-E&O insurance does most of the
    actual protective work. For sub-$50k-revenue side-
    businesses in low-liability categories, CA's $800/year
    franchise tax can exceed the LLC's effective benefit.
    The Indie Hackers / r/Entrepreneur voice catches this
    cost-benefit analysis; generic "always form an LLC"
    advice (often from accounting / legal marketing) does
    not. Boundary `personal-finance` D6.
  - "Piercing the corporate veil" precedents are *highly
    state-and-fact-specific* and the framing's "follow
    formalities" reflex captures only the easy cases (don't
    commingle funds, sign contracts as entity, file annual
    reports). Hard cases — undercapitalization, alter-ego,
    fraudulent-conveyance to defeat creditors, dominating-
    parent-corporation doctrine, single-economic-enterprise
    treatment — are litigated extensively and outcomes
    depend on state precedent (TX *Castleberry v Branscum*
    factors vs DE Trevino-and-Mason factors vs CA *Sonora
    Diamond Corp* alter-ego standard). Founders relying on
    "we have an LLC so we're safe" misunderstand the
    extensive case-law that erodes the shield in close
    cases. Boundary `legal-disputes`.
  - The framing under-engages with *trust-fund tax personal
    liability* under IRC §6672 (federal payroll-withholding,
    income-tax-withholding) and parallel state trust-fund
    statutes — these are NOT shielded by entity, and any
    "responsible person" (typically defined as any officer
    with check-signing authority and duty to pay payroll
    taxes) is personally collectible for unpaid amounts
    plus 100% penalty. Founders who fall behind on payroll
    tax during a cash-crunch face personal collection from
    the IRS even after the company files Chapter 7 — this
    pierces all corporate-form shields. The framing's
    "shield protects me from business debts" reflex misses
    this trust-fund exception. Boundary `personal-finance`
    and `legal-disputes`.
  - LLC-vs-C-corp shield strength is *commonly assumed
    equal* — but they differ on (a) tax treatment (LLC
    pass-through by default, C-corp double-tax — see F4),
    (b) shareholder / member fiduciary duties (C-corp
    directors have stricter duties of loyalty and care
    under DGCL §141; LLC members can structure duties down
    via operating agreement subject to state restrictions),
    (c) investor expectations (institutional VCs require
    Delaware C-corp for priced rounds; SAFEs and convertible
    notes typically presume C-corp issuer), (d) QSBS
    eligibility (C-corp only — see F5). The framing's
    "form an LLC" default works for non-venture trajectories
    but creates conversion-and-tax-friction for founders who
    later raise priced equity. Boundary `personal-finance` F6.

## 7. ABC-test / worker-classification framing

- **Decisions it applies to**: D7 (first W-2 employee vs 1099
  contractor — central), D10 (subsequent hires including
  offshore — the ABC test applies to US-based workers
  regardless of company growth stage; offshore via EOR
  shifts the classification analysis to the EOR's
  jurisdiction), D11 (co-founder departure — non-compete
  enforceability, non-solicit drafting, and IP-trailing-
  claim posture are employment-law adjacent), and as a meta-
  framing on D1 (CIIAA scope and prior-art carve-out are
  the IP-side parallel to wage-and-hour classification —
  both are employment-law-adjacent contracts that determine
  who owns what at separation).
- **Mental model summary**: Worker misclassification —
  treating an employee as a 1099 contractor to avoid
  payroll-tax, benefits, and employment-law exposure — is
  among the most-litigated employment-law categories and
  among the highest-financial-tail-risk founder errors. The
  IRS uses the *common-law-control test* (20+ factors
  covering behavioral control, financial control, and
  relationship-type) but most states use stricter tests:
  California, Massachusetts, New Jersey, Illinois, Nevada,
  and others use the *ABC test* — a worker is an employee
  unless ALL of (A) free from control and direction of the
  hiring entity, (B) work performed outside the usual
  course of the hiring entity's business, (C) customarily
  engaged in an independently established trade. CA's AB-5
  (2019) codified ABC broadly for nearly all workers
  (carving out limited business-to-business and bona-fide-
  freelancer exceptions); subsequent AB-2257 and Prop 22
  carved out specific industries (transportation, app-based
  drivers — Prop 22 currently in litigation). The "(B)
  outside usual course of business" prong is the load-
  bearing test: a software company *cannot* legitimately
  classify a software engineer as 1099 in California
  because software is the company's usual course of
  business — regardless of the engineer's preferences, work
  schedule, tool ownership, or contractor agreement
  language. CA-PAGA (Private Attorneys General Act) allows
  a misclassified employee to sue on behalf of the state
  for civil penalties ($100/pay-period/employee initial,
  $200 subsequent) applicable to the lookback period (CA
  statute of limitations 4 years for wage-and-hour, longer
  with continuing-violation theory), plus unpaid overtime,
  waiting-time penalties under CA Labor Code §203 (up to
  30 days of additional wages), meal-and-rest-break
  penalties, attorney fees, and pre-judgment interest. A
  CA-misclassified-software-engineer case can exceed
  $100k+ in total exposure on a single worker at modest
  1099 rates. Out-of-state founders hiring CA workers as
  1099 are routinely caught here; the recovery is to
  apply the strictest applicable state's test, and when
  in doubt classify as W-2 with payroll service (Gusto /
  Justworks / Rippling). Characteristic move: identify the
  worker's state of residence; apply the strictest
  applicable test (ABC if in ABC state); err W-2 when the
  worker performs the company's usual-course-of-business
  work for any sustained period; engage employment-law
  counsel for any sustained 1099 relationship in ABC
  states. Anchor: misclassification damages accrue
  silently through the limitations period — the founder
  who "saved $30k/year on payroll tax" by 1099-ing a CA
  engineer for 3 years faces $200k+ exposure if the
  engineer files a wage-and-hour claim post-departure.
- **Characteristic vocabulary**: "IRS common-law control
  test (20-factor)", "ABC test (CA, MA, NJ, IL, NV)",
  "CA AB-5 codification", "AB-2257 carve-outs", "Prop 22
  status in litigation", "(B) outside the usual course of
  business", "PAGA Private Attorneys General Act",
  "$100/pay-period/employee penalty (initial)", "$200
  subsequent", "CA Labor Code §203 waiting-time penalties
  up to 30 days wages", "meal-and-rest-break penalties",
  "Industrial Welfare Commission wage orders", "Form
  1099-NEC vs W-2", "Form SS-8 IRS classification
  determination request", "back-payroll-tax assessment",
  "responsible-person personal liability under IRC §6672",
  "FTC 2024 non-compete rule (status in litigation)",
  "DTSA Defend Trade Secrets Act federal cause of action",
  "CA Labor Code §16600 non-compete void."
- **Excludes**:
  - The framing's strict "classify as W-2 when in doubt"
    reflex is correct for sustained engagements but
    *over-applies* to legitimately bounded 1099
    relationships (3-6 month project with clear
    deliverables, parallel-clients, own tools — the
    archetypal *bona fide* independent contractor). Some
    founders over-correct by W-2-ing every contractor
    regardless of relationship structure, which creates
    unnecessary payroll overhead and benefits-eligibility
    complexity. The framing's risk-aversion is rational
    but doesn't always degrade-gracefully to the
    legitimate contractor case. The r/SmallBusiness voice
    catches this distinction better than the
    `legal-disputes`-litigation voice does.
  - "Contractor through their own LLC" does NOT immunize
    the hiring entity from misclassification analysis —
    the ABC test applies to the *substance of the working
    relationship*, not the form of the payment vehicle. A
    CA software engineer billing through their single-
    member-LLC is still subject to the ABC test analysis;
    the LLC structure may help the worker's own tax
    position but does not protect the hiring company from
    PAGA / wage-and-hour claims. The framing's "they have
    their own LLC, so they're a real contractor" reflex
    misroutes commonly. The state-by-state variation
    matters: TX is much more permissive.
  - Non-compete enforceability is *rapidly shifting*: CA's
    §16600 has voided non-competes for decades; the FTC
    issued a rule in 2024 broadly banning non-competes
    nationally (with limited carve-outs); the rule has
    been stayed and partially-struck in litigation
    (Northern District of Texas in *Ryan LLC v FTC*);
    status of rule at any given moment requires
    verification with employment-law counsel. The framing's
    "check your state's non-compete law" reflex understates
    the federal-rule-volatility and the time-sensitivity of
    the analysis. Non-solicit covenants (customer or
    employee) are *more broadly enforceable* than non-
    competes — even CA enforces narrow non-solicit with
    consideration and reasonable scope — but the framing
    often treats non-compete and non-solicit
    interchangeably. Boundary `legal-disputes`.
  - The framing under-engages with *contractor's own
    perspective and bargaining power* — a senior contractor
    with multiple parallel clients may *prefer* 1099 for
    tax-optimization reasons (Schedule C deductions,
    SEP-IRA / solo-401(k) contribution capacity, QBI
    deduction availability that doesn't apply to W-2
    income), even when the relationship is sustained
    enough to qualify as W-2 under the ABC test. The
    company's misclassification exposure is asymmetric:
    the contractor benefits while the engagement runs
    smoothly, then has the option to file a misclassification
    claim post-separation, capturing both the contractor-
    tax-benefits and the misclassification-damages. The
    framing's "the company is exposed" framing is correct
    but the contractor-side incentive structure deserves
    explicit recognition. Boundary `tech-career` on
    senior-contractor positioning.

## 8. Day-job-fallback / opportunity-cost framing

- **Decisions it applies to**: D3 (quit day job vs nights-
  and-weekends — central), D2 (bootstrap vs raise — the
  bootstrap path stretches founder runway against the day-
  job-fallback decay), D11 (co-founder departure — the
  departing founder's market-position and re-employability
  determine the negotiation leverage on severance / non-
  compete / acceleration), and as a meta-framing on D1
  (the co-founder selection question depends on the
  alternative-employment-cost each co-founder faces, which
  is part of the implicit cap-table negotiation).
- **Mental model summary**: The aspiring founder with a day
  job is making a decision about *option value over time*,
  not just *income vs equity today*. The day-job-fallback
  is itself a depreciating asset: the longer the founder is
  out of market, the harder the return to comparable W-2
  income — at FAANG and senior IC levels, the freshness
  window is approximately 12-24 months (deep-tech and ML
  roles depreciate faster as the field shifts; senior
  product / engineering management roles depreciate more
  slowly). Golden-handcuffs from RSU vesting cliffs create
  implicit per-month opportunity cost: $200k of unvested
  RSU at 12 months out is a $200k/12 = ~$17k/month implicit
  cost of leaving early, separate from the salary loss.
  Household risk-bearing capacity (single vs dual-income,
  kids, mortgage, health-insurance-dependence on employer
  plan) sets the bound on personal-runway-available.
  Implementation: maximize day-job earnings during the
  side-project phase to extend personal runway; vest as
  much equity as feasible before leaping (timing the leap
  for the day-after a cliff or significant vest event);
  carve out the side-project IP in writing with the
  employer before any meaningful work (CA Labor Code §2870
  protects only inventions made on the employee's own
  time without employer equipment, NOT related to the
  employer's actual or anticipated business — "anticipated
  business" is the load-bearing fuzzy term); use
  severance-event windows (layoff, restructuring,
  performance-improvement-plan exit, voluntary separation
  with package) as runway extenders. Characteristic move:
  build the explicit cost-benefit-table comparing (a)
  next-12-months expected day-job income + vesting, (b)
  next-12-months expected startup income + equity-EV
  (heavily discounted for failure probability), (c) the
  re-employability discount at 12-month-out vs 24-month-
  out vs 36-month-out return, (d) household-cash-flow
  needs floor; leap only when the table clears the leap-
  threshold with appropriate buffer. Anchor: median FAANG
  tenure is ~2 years; PIP / RIF probability non-trivial;
  the day-job is itself not riskless income and the
  framing's "stable W-2 income" assumption needs explicit
  tenure-and-layoff-risk adjustment.
- **Characteristic vocabulary**: "day-job-fallback option
  value", "golden-handcuffs RSU cliff cost", "freshness
  window for return to W-2", "personal runway and burn
  rate honesty", "household risk-bearing capacity",
  "single-vs-dual-income leap threshold", "MRR cover
  expenses threshold ($X MRR = quit signal)", "Paul Graham
  *Maker's Schedule, Manager's Schedule*", "context-switching
  cost between day job and startup", "moonlight IP-
  assignment exposure", "CA Labor Code §2870 carve-out",
  "anticipated business as load-bearing fuzzy term",
  "Roth-conversion window on low-income year", "severance-
  event as runway extender", "COBRA bridge 18 months at
  full-cost-plus-2%", "ACA Special-Enrollment-Period on
  loss of employer coverage."
- **Excludes**:
  - The framing's "day-job-as-stable-income" baseline
    overstates W-2 stability — median FAANG tenure is ~2
    years, PIP / RIF probability is non-trivial across
    cycles, and the implicit assumption that the day-job
    continues at current comp for the next 18-36 months is
    optimistic across cycles. The 2022-2024 tech layoff
    cycle (Meta, Amazon, Google, Microsoft, Salesforce,
    smaller startups) demonstrated that *not leaping* also
    has tail-risk. The framing's "the day-job is the safe
    baseline" assumption needs explicit cycle-and-tenure
    adjustment; Tomasz Tunguz / SaaStr voices catch the
    cyclicality. Boundary `tech-career`.
  - "Anticipated business" in employer IP-assignment
    clauses is *deliberately fuzzy* and the framing's
    "carve out the side-project in writing" reflex
    underestimates the practical difficulty: many
    employers refuse explicit carve-outs (so the founder
    is forced to either drop the side-project, hide it,
    or quit to pursue it); HR / Legal often treats the
    request itself as evidence the side-project competes
    with the employer's anticipated business and tightens
    enforcement; the carve-out request can accelerate the
    leap timeline beyond the founder's preferred schedule.
    The Patio11 voice catches this dynamic; the standard
    "ask for carve-out in writing" advice often does not
    engage with the employer-side response patterns.
    Boundary `tech-career` and `legal-disputes`.
  - The framing under-engages with the *Roth-conversion-
    window on low-income years* — a year of reduced or
    zero W-2 income from the leap creates a uniquely-
    high-leverage Roth-conversion opportunity: traditional-
    401(k) or traditional-IRA balances can be converted to
    Roth at the founder's low marginal rate (potentially
    0%-12% federal bracket if the year is genuinely zero-
    income), locking in the rate forever. This is almost
    universally missed by founders who don't have
    integrated personal-finance and entrepreneurship
    advisors. Boundary `personal-finance` D7.
  - "Quit when MRR covers 50% of expenses" / "quit at
    $10k MRR" / "quit at $30k MRR" heuristics are *under-
    engaged with growth-slope* — the load-bearing variable
    is not the absolute MRR level but the *growth slope
    change a full-time commitment would produce*: a $4k
    MRR business growing 25%/month with 60+hr/week day-job
    is a stronger leap candidate than a $30k MRR business
    growing 2%/month, because the full-time commitment
    will not change the slope on the latter. The
    heuristics-treated-as-rules cause founders to either
    leap too early (chasing absolute-MRR without slope
    signal) or stay too long (waiting for an MRR threshold
    a stagnant business will never reach). Indie Hackers
    voice tends toward absolute-MRR; YC playbook voice
    tends toward growth-slope. Both have rationalization
    failure modes.

## 9. Product-led-growth / PLG framing

- **Decisions it applies to**: D9 (pricing model selection
  — central; PLG is structurally tied to freemium /
  self-serve / low-friction signup models), D10 (first
  hire vs contractor vs offshore — PLG companies hire
  growth-engineers and PMs before they hire sales reps;
  hiring sequence reflects motion), and as a meta-framing
  on D2 (bootstrap-vs-raise — PLG models can bootstrap
  further on lower-CAC self-serve acquisition before
  needing the sales-led-growth capital).
- **Mental model summary**: Product-Led-Growth is a go-to-
  market motion where the product itself is the primary
  acquisition, activation, and conversion driver — users
  find the product (through search / SEO / word-of-mouth /
  community), self-serve sign-up without sales contact,
  experience value within minutes, and convert from free
  to paid (or higher tier) through in-product upsell.
  Canonical examples: Slack (free team workspaces convert
  via Pro / Business / Enterprise on workspace size and
  features), Notion (free personal converts via Plus /
  Business / Enterprise), Figma (free editor seats convert
  via Pro / Org / Enterprise), Linear (free for small teams
  converts via Plus / Business), Atlassian (Jira / Confluence
  with freemium + self-serve PLG bridge before sales-led
  enterprise). The framing reasons in product-as-funnel
  terms: activation rate (% of signups reaching aha-moment
  within first session), TTV time-to-value (minutes from
  signup to first delivered value), PQL product-qualified-
  lead score (which free users are most likely to convert
  to paid based on behavioral signals), expansion-rev
  mechanics (per-seat expansion as teams add users,
  feature-upsell on usage-thresholds, capability-upsell
  on Pro features). PLG demands extreme product polish on
  the free experience: a free user with a confusing
  onboarding churns silently and never converts; the
  activation metric is the single most-watched leading
  indicator. The build-cost is the founder error pattern —
  founders underestimate the engineering and PM investment
  required for PLG-grade onboarding, in-product growth
  surfaces, instrumentation and experiment infrastructure,
  and the supporting analytics / data-eng / experimentation
  platform. Implementation: instrument every step of the
  funnel; activate ruthlessly; build pricing tiers that
  reflect customer-value-tiers (per-seat for collaborative
  products, usage-based for infrastructure / API,
  capability-tier for consumer / SMB); price the entry tier
  low enough to remove conversion friction; capture
  enterprise upside via top-tier with sales-light-touch.
  Characteristic move: when a founder asks "should I hire
  a sales rep," PLG framing first asks "is my activation
  rate high enough that self-serve fills the top of funnel?"
  — premature sales-hire on a leaky funnel wastes salary
  and dilutes founder time from the product polish that
  would have made sales unnecessary. Anchor: Lenny Newsletter
  / Reforge / OpenView Partners published PLG benchmarks —
  activation 25-50% best-in-class, free-to-paid conversion
  1-5% freemium / 10-30% free-trial, NRR (net revenue
  retention) > 120% on healthy SaaS, expansion-revenue 30-
  50% of new ARR for mature PLG companies.
- **Characteristic vocabulary**: "Product-Led-Growth (PLG)",
  "freemium-to-paid conversion funnel", "activation rate",
  "time-to-value (TTV)", "aha-moment", "PQL Product-
  Qualified-Lead", "in-product upsell", "expansion revenue",
  "net revenue retention (NRR)", "self-serve onboarding",
  "no-sales-touch tier", "per-seat pricing with team-
  expansion", "usage-based pricing for infra", "feature-
  flag-driven gating", "experiment infrastructure", "OpenView
  Partners benchmarks", "Reforge growth-loops", "Slack /
  Notion / Figma / Linear / Atlassian as PLG canon."
- **Excludes**:
  - The "product-as-funnel" reflex assumes the buying
    decision is *individual or small-team* (where the
    user can sign up, try, and pay without procurement
    involvement) — but mid-market and enterprise sales
    fundamentally require human navigation of procurement,
    security review (SOC 2, SIG / SIG-Lite questionnaires,
    vendor-onboarding checklists), MSA / DPA negotiation,
    and multi-stakeholder buy-in. PLG-only motions cap at
    the SMB / individual-power-user segment and routinely
    leave 5-10x revenue on the table by not also building
    sales-led capacity for the larger deals. Opposes F10
    (sales-led-growth) on D9 / D10.
  - The framing's "low entry-tier price to remove
    friction" reflex *systematically under-prices early*
    — founders set "Pro at $10/month" or "Team at $5/seat"
    because the freemium-to-paid conversion would suffer at
    higher prices, then can never raise prices on early
    cohorts without grandfathering complexity. Patrick
    Campbell / ProfitWell research repeatedly shows PLG
    companies under-price entry tiers by 2-5x relative to
    customer willingness-to-pay; the recovery is to price
    higher and let conversion-rate-drop be observed before
    optimizing. Boundary `personal-finance` on pricing-
    psychology.
  - PLG-canon companies (Slack, Notion, Figma, Linear,
    Atlassian) are *survivorship bias examples* — the
    framing rarely surfaces the 100s of failed PLG attempts
    in adjacent categories (project management, CRM,
    knowledge management, design tools) where the
    activation-rate or conversion-rate fundamentals didn't
    work and the companies ran out of runway trying to
    optimize them. PLG works in *specific category-product
    fits* and is not a universal motion; founders forcing
    PLG on a category that doesn't naturally support self-
    serve (anything requiring data integration, multi-
    stakeholder configuration, or post-sale onboarding
    services) face a dead-end the framing's canon doesn't
    acknowledge.
  - "Instrumentation and experimentation infrastructure"
    is the *invisible engineering cost* of PLG that the
    framing under-prices — building a proper experimentation
    platform (Amplitude / Mixpanel / Segment / dbt / data
    warehouse / experiment framework / feature-flag system
    / reverse-ETL) easily costs 1-2 senior engineers full-
    time for 6-12 months at pre-Series-A scale. Founders
    starting PLG without this infrastructure run blind on
    activation experiments and waste 12-18 months running
    intuition-driven changes that they cannot measure.
    Lenny Newsletter / Reforge voices catch this; the
    "Slack-style PLG" headline-version often doesn't.
    Boundary `tech-career` on data-eng hiring sequence.

## 10. Sales-led-growth / enterprise framing

- **Decisions it applies to**: D9 (pricing model selection
  — central; sales-led-growth is structurally tied to
  custom-quoted, multi-year, list-with-discount enterprise
  pricing models), D10 (first hire vs contractor vs offshore
  — sales-led companies hire AE / BDR / SDR / CSM ahead of
  product-management at the same stage PLG companies do
  the reverse), and as a meta-framing on D2 (bootstrap-vs-
  raise — sales-led typically requires Series A capital
  for the AE-and-CS-team buildout before revenue ramps).
- **Mental model summary**: Sales-Led-Growth (SLG) is the
  enterprise-default motion where human salespeople (AE
  Account Executives, BDR / SDR Business / Sales Development
  Reps, CSM Customer Success Managers, SE Solutions
  Engineers) drive multi-stakeholder buying processes
  involving procurement, legal, security, and budget-
  approval cycles. The framing reasons in SaaS-metrics-
  dogma terms: CAC payback period (months to recover the
  cost of acquiring a customer through gross-margin
  contribution — target < 18 months for healthy enterprise
  SaaS, < 12 months for SMB / mid-market), LTV-to-CAC
  ratio (target 3:1 minimum, 5:1+ excellent), Magic Number
  (net-new ARR for the quarter ÷ S&M spend for the
  prior quarter — target > 0.75), Rule of 40 (growth-rate
  + operating-margin > 40), Net Revenue Retention (target
  > 110% healthy, > 130% best-in-class on enterprise),
  Gross Revenue Retention (target > 95% healthy, > 98%
  best-in-class). Sales-cycle calibration: SMB 1-3 month
  cycle; mid-market 3-6 month; enterprise 6-12+ month;
  bottom-up POC-to-enterprise can be 9-18 month. List
  price vs actual price: enterprise customers expect to
  negotiate; list price is the anchor, actual price is
  typically 20-40% off list with multi-year commits, plus
  procurement adds standard requirements (SOC 2 Type II,
  security questionnaires SIG / CAIQ, payment terms net-
  30 / net-45 / net-60, MSA / DPA / BAA negotiation, e-
  signature via DocuSign / PandaDoc, MFA enforcement,
  audit-log retention). Founders moving from PLG-self-
  serve to enterprise are surprised by the 3-6-month
  sales cycle and the discounting expectation; the
  recovery is to bake discount expectation into list-
  price-setting from the start — quote list at 1.3-1.5x
  desired-realized-price. Hiring sequence is structurally
  different from PLG: first AE (typically a senior with
  existing book of relationships) hired pre-Series-A on
  $200-300k OTE; sales-engineer hired alongside; SDR for
  outbound prospecting at $80-120k OTE; CSM at $90-130k
  OTE for renewal management — the team builds in advance
  of revenue, creating the early-quarters S&M-burn that
  Series A capital funds. Characteristic move: invest in
  the AE-and-CS process design before hiring the first
  rep (CRM in Salesforce / HubSpot, MEDDIC / MEDDPICC /
  Command-of-the-Message sales methodology, ICP Ideal
  Customer Profile definition, persona / use-case
  segmentation, win-loss analysis discipline); hire the
  first AE only after the founder has personally closed
  10+ deals to validate the playbook is real; expect 30-
  60 day ramp on a senior AE and 90-180 day ramp on a
  junior.
- **Characteristic vocabulary**: "Sales-Led-Growth (SLG)",
  "Account Executive (AE)", "BDR / SDR Business / Sales
  Development Rep", "Customer Success Manager (CSM)",
  "Solutions Engineer (SE)", "MEDDIC / MEDDPICC",
  "Command of the Message", "ICP Ideal Customer Profile",
  "OTE on-target earnings", "quota / pipeline / coverage
  ratio", "CAC payback period", "LTV-to-CAC ratio",
  "Magic Number", "Rule of 40", "Net Revenue Retention
  (NRR)", "Gross Revenue Retention (GRR)", "SOC 2 Type
  II", "SIG questionnaire", "MSA Master Service
  Agreement", "DPA Data Processing Agreement", "BAA
  Business Associate Agreement (HIPAA)", "list price at
  1.3-1.5x desired-realized", "Salesforce / HubSpot CRM
  hygiene", "SaaStr / Jason Lemkin metrics", "Tomasz
  Tunguz benchmarks", "Bessemer / OpenView Index data."
- **Excludes**:
  - The framing's enterprise-sales playbook is *capital-
    intensive in a way bootstrap fundamentally cannot
    afford* — building an AE-CSM-SE team requires
    Series A capital, and the framing routinely
    *implicitly assumes* the company has raised. Bootstrap
    founders pushing for enterprise customers without
    sales-team capital face the founder-as-perpetual-
    salesperson trap (founder time as primary salesperson
    permanently caps revenue growth at founder bandwidth)
    that the framing doesn't address. Opposes F2
    (bootstrap default-alive) on D9 / D10.
  - "MEDDIC / MEDDPICC discipline" and "first AE only
    after founder has closed 10+ deals" are correct
    process guardrails, but the framing under-engages
    with the *founder-as-AE failure mode*: technical
    founders without sales background routinely close
    early deals through technical-credibility and
    customer-love rather than through reproducible sales
    process, then cannot hire someone to replicate
    because the playbook was never legible. The first AE
    underperforms, founder doubts the AE rather than the
    transferability of their own approach, and the
    company churns AEs while founder bandwidth caps
    growth. The framing's "you have a playbook" reflex
    overstates how often early founder-led-sales is
    actually a transferable playbook. Boundary `tech-
    career` on sales-management hiring asymmetry.
  - List-price-at-1.3-1.5x-desired-realized is a *good
    discounting hygiene* but the framing under-engages
    with the *discount-creep* dynamic: AEs paid on quota
    have implicit incentive to discount to close, and
    without a strong deal-desk / pricing-committee
    discipline, list price erodes 30-50% within 2 years
    as AEs build muscle around what they can give away.
    The recovery is a deal-desk process (every discount
    above X% requires VP-Sales or CFO approval) — but
    early-stage companies often skip this and discover
    the erosion at the second-year board deck. Tomasz
    Tunguz / SaaStr voices catch this; First Round Review
    voice catches it in management-system framing.
  - SaaS-metrics dogma (CAC payback, LTV/CAC, Magic Number)
    *assumes the metric calculations are clean* — but
    most early-stage companies' metric calculations are
    *materially wrong* in ways that flatter the picture:
    CAC underweights founder-time-as-S&M (founder spending
    20 hrs/week on sales-and-marketing without W-2
    compensation depresses CAC artificially); LTV based
    on first-12-months data extrapolated to "lifetime"
    misses the actual churn curve; NRR including up-sells
    from existing accounts mixes apples with oranges
    (upsell driven by good-product vs by sales-discount-
    expansion). The framing's "use these metrics" reflex
    understates how easy it is to deceive yourself with
    metrics that look correct but encode bad assumptions.
    Boundary `data:analyze`.

## 11. Founder-mode / hands-on-management framing

- **Decisions it applies to**: D10 (first employee vs
  contractor vs offshore — the founder-mode reflex is to
  hire ICs the founder personally onboards / mentors / sets
  standards for; less manager-layer delegation), D11 (co-
  founder departure — founder-mode companies struggle with
  co-founder departures because so much is concentrated in
  the remaining founders' direct relationships), and as a
  meta-framing on D9 (pricing — founder-mode CEOs often
  personally negotiate every enterprise deal until well past
  the point a sales team would scale better).
- **Mental model summary**: Paul Graham's *Founder Mode*
  (Sep 2024 essay) — drawing on Brian Chesky's experience
  at Airbnb and earlier YC observations — argues that
  *startup CEOs in growth phase should NOT manage like
  professionally-trained managers manage*. The conventional
  manager-mode playbook (hire great people, delegate fully,
  trust them to do their jobs, intervene only on metrics)
  was developed for *large companies* with established
  cultures and known-good operating systems; applying it to
  early-stage startups (where the operating system is being
  invented and culture is being established) systematically
  destroys startups by introducing political dynamics and
  metric-gaming before the company is ready. Founder-mode
  is its own thing: the founder maintains direct contact
  with the lowest-level engineers (Steve Jobs's "skip-level"
  meetings, Brian Chesky's design-review involvement); the
  founder personally interviews and onboards key hires;
  the founder sets the bar for what "good" looks like
  through direct demonstration; the founder maintains a
  small inner-circle of trusted ICs and pulls them into
  major decisions regardless of org-chart layer. Garry Tan
  / Sam Altman / Brian Chesky voices reinforce: founder-
  mode CEOs are more involved in product, hiring, and
  customer-facing detail than the same-CEO would be under
  the "delegate to your team" conventional advice. The
  framing reasons in *direct-line-of-sight* terms: the
  founder's brain is the company's strategic compute, and
  filtering everything through an executive layer
  systematically degrades the signal that informs strategy.
  Implementation: maintain founder presence in product-
  detail, hiring-detail, and key-customer-detail through
  Series B (and beyond, if scale permits); reject the
  "as-CEO-I-shouldn't-need-to-know-this" instinct that
  professional managers bring from BigCo; structure the
  org so the founder can dip into any level without it
  being a special event. Characteristic move: when an
  early company hires an experienced VP of X who pushes
  the founder to "stop being in the weeds," founder-mode
  framing asks whether the VP's mental model is calibrated
  to the company's actual stage or to their last BigCo
  experience — typically the latter.
- **Characteristic vocabulary**: "Founder Mode (PG 2024
  essay)", "skip-level meetings", "Brian Chesky / Airbnb
  founder-mode case study", "Steve Jobs design-review
  involvement", "stay in the details", "direct line of
  sight", "the founder's brain is the strategic compute",
  "professional-manager-from-BigCo applied to startup
  destroys things", "Garry Tan / Initialized perspective",
  "Sam Altman *How To Be Successful*", "high-agency
  individual contributors", "the inner circle / kitchen
  cabinet", "no executive-layer between founder and
  product", "founder-CEO until exit or fired", "what would
  Steve Jobs do (in product review)."
- **Excludes**:
  - The "founder-mode" reflex *can rationalize micro-
    management* and damage early hires who joined
    expecting autonomy — when the founder dips into every
    detail across product / hiring / customer / financial,
    the senior hires the company needs to scale leave
    because their bandwidth is consumed managing the
    founder's interventions. Brian Chesky's Airbnb example
    is *successful founder-mode after the company had
    found PMF and product DNA* — applying the same
    intensity pre-PMF without a stable product DNA can
    chaotic-ize the company and exhaust the team. The
    framing rarely surfaces the stage-conditioning that
    makes founder-mode work. Opposes F12 (manager-mode)
    on D10 / D11.
  - "Skip-level meetings" and "stay in the details" are
    practices that *do not scale beyond ~200 person
    company* without explicit org-design support — the
    founder can dip into every project at 30 people, can
    rotate across major projects at 100 people, but
    cannot maintain direct-line-of-sight at 500+ without
    designating "founder-led-projects" vs "manager-led-
    projects" explicitly. The framing's PG-essay version
    sidesteps the scaling question, which is the actual
    hard part for growth-stage CEOs. SaaStr / Lemkin
    voices catch this; PG-essay voice often doesn't.
    Boundary `tech-career` on engineering-management
    scaling.
  - The framing's "founder-mode" terminology carries
    *implicit founder-identity affirmation* that can
    obscure poor performance — a struggling founder
    rationalizing "I'm just in founder-mode, that's why
    I'm not delegating" can avoid the harder question of
    whether they're an effective CEO at this stage. The
    framing's positive valence makes it easy to use as
    self-flattering label rather than as analytical
    framework. Critique-from-the-team and self-critique
    are the corrections, but founder-mode rhetoric can
    silence both.
  - Founder-mode under-engages with *board / investor
    expectations at scale* — investors past Series B
    typically expect to see clear professional-management
    layer, succession planning, and executive bench depth
    that founder-mode-only org structures lack. The
    framing's "stay founder-mode forever" rhetoric runs
    into board friction at growth stage; some founders
    respond by changing boards (when possible — protective
    provisions and board composition constrain this) or
    accepting the management-layer reluctantly. The
    framing rarely surfaces the board-relationship cost
    of sustained founder-mode. Boundary `legal-disputes`
    on board governance.

## 12. Manager-mode / scalable-org framing

- **Decisions it applies to**: D10 (first employee vs
  contractor vs offshore — manager-mode framing emphasizes
  hiring an executive layer early to delegate-to; first
  VP / Head-of hires before IC scale), D11 (co-founder
  departure — manager-mode companies handle departures
  better because the org-chart absorbs the loss), D7 (first
  W-2 employee — manager-mode prefers W-2 with full
  benefits to build a "real company" culture), and as a
  meta-framing on D9 (pricing — manager-mode CEOs build a
  sales / pricing process and delegate execution, vs
  founder-mode personal-deal-by-deal).
- **Mental model summary**: Building a *scalable
  organization* is itself a load-bearing competence, and
  founder-CEOs who refuse to invest in the management
  layer cap company growth at founder bandwidth — a self-
  imposed ceiling that destroys companies past ~50-100
  employees. The framing reasons in *delegation-and-
  scalability* terms: the CEO's job is to (a) set strategy
  and core priorities, (b) hire and develop the executive
  team, (c) allocate capital, (d) represent the company
  externally to investors / press / key partners; not to
  personally do product-detail / hiring-detail / customer-
  detail at every level. Implementation: hire VP-of-X
  ahead of growth needs (VP Eng around 8-15 engineers,
  VP Sales around $1M ARR, VP Product around 3-5 PMs); use
  hiring scorecards and structured interviews to remove
  founder-personal-judgment as the hiring bottleneck;
  build operating system (OKRs / V2MOM / EOS / 4DX —
  whichever framework, applied with discipline); separate
  IC track from manager track to retain senior ICs;
  document playbooks for repeated processes (sales,
  onboarding, customer success, engineering review)
  so they're transferable. First Round Review / Lenny
  Newsletter / Reforge voices reinforce: building the
  management system is itself the work, not a distraction
  from the work; companies that don't build it hit a
  wall at 50-100 employees and stall there. Characteristic
  move: when a founder is bottlenecked across multiple
  functional areas (product, sales, hiring), manager-mode
  framing recommends investing in the next-level VP / Head-
  of even when the immediate financial case is weak,
  because the founder-bottleneck cost is the bigger
  number. Anchor: BigCo experience-from-Google / Facebook
  / Stripe / Snowflake is *not always wrong* for early-
  stage despite founder-mode pushback — the trick is to
  hire BigCo-experienced people who *also* understand
  early-stage chaos, not BigCo people who try to install
  BigCo process at startup scale.
- **Characteristic vocabulary**: "scalable organization",
  "build the management system", "OKR Objectives and Key
  Results", "V2MOM (Vision / Values / Methods / Obstacles /
  Measures)", "EOS Entrepreneurial Operating System", "4DX
  Four Disciplines of Execution", "VP-of-X hiring ahead of
  growth", "founder-bottleneck cost", "delegation and
  trust", "hiring scorecard", "structured interview loop",
  "IC track vs manager track", "principal engineer
  ladder", "First Round Review *The Manager's Playbook*",
  "Lenny *building the OS*", "professional management
  from Google / FB / Stripe", "executive-coaching from
  BetterUp / Reboot", "succession planning at growth-
  stage."
- **Excludes**:
  - The framing's "hire VP-of-X ahead of growth needs"
    reflex *over-hires the executive layer relative to
    company stage* — VP-Sales hired at $500k ARR before
    the founder has personally validated the sales
    playbook installs BigCo sales process onto a company
    that doesn't yet have product-market-fit, accelerating
    burn without accelerating revenue. The framing's
    Salesforce / Snowflake hiring-sequence-template is
    calibrated to *post-PMF growth-stage* companies, not
    to pre-PMF early-stage, and applying it pre-PMF
    creates the very founder-bottleneck-vs-executive-
    layer-mismatch the framing claims to solve. Opposes
    F11 (founder-mode) on D10 / D11.
  - "BigCo experience is valuable at startup" is *true on
    average* but *highly individual-dependent* — the
    distribution of BigCo-experienced executives includes
    a substantial fraction whose effectiveness is
    inseparable from BigCo infrastructure (large eng
    teams, mature data platforms, professional recruiting
    pipelines, in-house counsel, established brand) and
    who do *not* adapt to startup-resource-constraints.
    The framing's "hire from Google / FB / Stripe" reflex
    obscures the calibration question — *which* BigCo
    person, with *what* prior startup adjacency, *for
    what* role-at-stage. The hiring-error cost is
    severe: a wrong VP hire at growth stage can set the
    company back 18-24 months on the function they ran.
    Boundary `tech-career` on senior-leader hiring.
  - "Operating system" implementations (OKRs, V2MOM, EOS,
    4DX) are *cargo-culted* with high frequency — founders
    install the framework's artifacts (OKR documents,
    quarterly planning meetings, scorecards) without the
    underlying discipline (writing genuine objectives,
    holding teams accountable to outcomes vs activities,
    pruning low-impact work). The framework becomes
    process-theater that consumes team time without
    producing strategy clarity, and the founder concludes
    "OKRs don't work" when the framework was never really
    in place. The framing's "use a framework" reflex
    under-prices the discipline-vs-artifact distinction.
    First Round Review voice catches this; the consultant-
    voice version often doesn't.
  - The framing under-engages with *the founder's own
    capacity-to-delegate* — many founder-CEOs are
    *constitutionally unable* to genuinely let go of
    decisions even after hiring strong executives, and the
    "build the management system" advice without
    addressing the founder's own behavioral pattern
    produces an executive layer that the founder
    chronically undermines through second-guessing,
    skip-level interventions, and decision-reversal. The
    framing's professional-management ideal assumes a
    founder-personality that many founders don't have, and
    the failure mode is acrimonious VP-departures and a
    company stuck in the same place. Executive-coaching is
    sometimes the load-bearing intervention here, not
    structural-org-redesign. Boundary `tech-career` on
    individual-effectiveness work.

## 13. Optionality-preservation / multiple-paths framing

- **Decisions it applies to**: D2 (bootstrap vs raise —
  preserve the option to do either), D3 (quit day job —
  preserve the option to return; preserve the option to
  carve out IP), D5 (SAFE vs priced seed — SAFE preserves
  optionality on terms longer; priced seed locks in but
  also locks out further-SAFE-stacking), D6 (sole-prop vs
  LLC — formation can be deferred to preserve optionality
  on entity choice), D8 (solo-401(k) vs SEP-IRA — solo-
  401(k) preserves the backdoor-Roth optionality that SEP
  destroys via pro-rata trap), and D1 secondarily (delay
  irrevocable cap-table commitments past initial
  exploration).
- **Mental model summary**: At every decision-point the
  founder should ask "does this preserve or close future
  options?" and bias toward preservation when the cost is
  low. The framing reasons in *real-options* terms (drawing
  on financial-options theory and Patio11's anti-platitude
  posture): the value of a startup founder's situation is
  the sum of present-value-of-current-trajectory *plus*
  optionality-value-of-future-pivots, and many founder
  decisions destroy optionality without commensurate
  current-trajectory upgrade. Specific high-leverage
  preservation moves: (a) maintain day-job-IP-carve-out in
  writing before the leap, so the prior employer's claim
  on side-project IP doesn't surface at acquisition; (b)
  delay LLC formation until revenue or liability triggers
  it, avoiding $800/year CA franchise tax on a $0-revenue
  side-project; (c) choose solo-401(k) over SEP-IRA so
  backdoor-Roth remains available; (d) prefer SAFE over
  priced seed when foreseeable round-terms haven't crystallized
  (priced seed locks in terms; SAFE postpones to a future
  market-condition); (e) avoid co-founder 50/50 splits
  with full immediate-vesting when one founder might not
  show up — vesting-and-cliff IS the optionality preservation
  on the co-founder commitment; (f) document everything
  important in writing because retroactive memory is
  unreliable and lawsuits turn on documentation. Anchor:
  Patio11 / Bingo Card Creator voice — most founder
  decisions are *not* one-way doors; identifying which
  *are* one-way doors and pausing before stepping through
  them is the load-bearing discipline. Characteristic
  move: when facing a decision, name the one-way-door
  features explicitly ("this commits us to X for at least
  Y months; this loses option Z permanently") and only
  step through with conscious commitment.
- **Characteristic vocabulary**: "real-options thinking",
  "preserve optionality", "one-way door vs two-way door",
  "Jeff Bezos two-way-door decisions", "Patio11 anti-
  platitude", "calling a wave of fans does not produce
  $4MRR", "default-think-about-the-default", "the path
  not taken is also a path", "vesting-and-cliff as
  optionality preservation on co-founder", "SAFE
  postpones to future market", "solo-401(k) preserves
  backdoor-Roth", "IP carve-out in writing", "delay LLC
  formation until trigger", "document everything",
  "retroactive memory is unreliable", "lawsuits turn on
  documentation."
- **Excludes**:
  - The "preserve optionality" reflex can rationalize
    *failure to commit* — the founder who never quits
    the day job, never forms the LLC, never issues SAFEs,
    and never hires the first employee is preserving
    optionality at the cost of never actually building
    the company. Optionality is valuable only when
    eventually exercised; permanent optionality is
    indistinguishable from inaction. The framing's
    "two-way door" rhetoric can mask the deeper question
    of whether the founder will *ever* commit. Opposes
    F14 (conviction-commitment) directly on D2 / D3 /
    D5.
  - "Document everything in writing" is *correct discipline*
    but routinely *under-practiced because of inter-
    personal friction* — co-founders pushing for written
    operating agreements, IP-assignment carve-outs, and
    role-clarity documents can come across as
    untrusting, and the relationship cost of asking
    creates pressure to defer. The framing's "document
    everything" reflex catches the discipline; the
    framing rarely engages with the *interpersonal
    dynamics* that prevent the documentation from
    happening. Indie Hackers / r/SmallBusiness voices
    catch the interpersonal dynamics; Patio11 voice
    catches the discipline. Boundary `legal-disputes`.
  - The framing under-engages with *option-value-
    decay-over-time* — many "optionality preservation"
    moves preserve options that *also depreciate*: the
    day-job-fallback decays at 12-24-month freshness
    (F8); the SAFE-stacking-as-postponement accumulates
    silent dilution; the LLC-formation-deferred-until-
    trigger may miss the optimal entity-choice timing
    (state-fee variation, S-corp election window).
    Optionality is not free, and the framing's "preserve
    options" reflex can mask the carrying-cost of those
    options. Calculating option-value-net-of-carrying-cost
    is the load-bearing math the framing rarely surfaces.
  - "Real-options thinking" is *mathematically
    sophisticated* but founder use of it is *typically
    qualitative* — founders rarely actually compute
    option-values, so the framing produces directional-
    guidance without quantitative discipline. The result
    is selective application: founders preserve
    optionality when the loss-aversion bias is dominant
    (don't quit the day job) and forsake it when the
    excitement-bias is dominant (sign the SAFE without
    reading the MFN clause). Calibration requires
    explicit option-value modeling that most founders
    do not do. Boundary `personal-finance` on real-
    options finance.

## 14. Conviction-commitment / burn-the-boats framing

- **Decisions it applies to**: D2 (bootstrap vs raise —
  the conviction-committed founder typically raises and
  scales aggressively rather than hedging), D3 (quit day
  job — the conviction-committed founder leaps without
  the safety-net the optionality framing preserves), D5
  (SAFE vs priced seed — conviction-committed founders
  often prefer priced rounds with full term-sheet
  commitments over open-ended SAFE-stacking), and as a
  meta-framing on D10 (the hiring philosophy of conviction-
  committed founders biases toward "all-in" hires who
  match the founder's commitment level, vs the
  optionality-preserved fractional-or-bounded-engagement
  bias).
- **Mental model summary**: Startup success requires
  *durable founder commitment over a 7-10-year build
  cycle*, and the half-hearted founder hedging across
  multiple paths systematically underperforms the
  conviction-committed founder who burns the boats and
  goes all-in. The framing reasons in *commitment-as-
  selection-mechanism* terms: the universe of plausible
  startups is far larger than the universe of founders
  willing to commit; the conviction-committed founder
  out-competes the hedging founder on attention, energy,
  decision-velocity, and team-recruitment (great hires
  follow conviction, not optionality); investors back
  conviction over hedging in close calls; customers feel
  the difference between a founder who'd happily go back
  to their day-job and one who can't and won't. Implementation:
  quit the day-job on signal, not on perfect-timing-
  threshold (waiting for the perfect signal is itself a
  hedging behavior); raise enough capital to build, not
  to hedge multi-year personal runway; commit to the
  cap-table structure that signals founder all-in (4/1
  vesting with no early-out, full-time-only no-moonlight,
  founder-takes-no-salary-for-12-months until milestone);
  hire people who match commitment (full-time, equity-
  significant, willing to bet career on the company);
  reject the "optionality" framing as risk-aversion
  rationalization. Sam Altman / PG (in *How To Start A
  Startup* lectures) / Brian Chesky voices reinforce:
  conviction is the most-undervalued founder asset, and
  the asks made of founders ("are you really committed?
  / can you do this for 10 years? / is this the most
  important thing in your life?") are calibration
  questions, not platitudes. Characteristic move: when
  considering a decision, ask "what would the all-in
  version of this look like?" and bias toward it unless
  the all-in version has explicit, named downside that
  cannot be mitigated. Anchor: "burn the boats" rhetoric
  from Cortez / Sun Tzu (in popular distortion) — the
  point is not the literal boat-burning, but the
  removal of the implicit fallback that distracts
  effort.
- **Characteristic vocabulary**: "burn the boats",
  "conviction over optionality", "founder all-in", "is
  this the most important thing in your life", "Sam
  Altman *How To Be Successful*", "PG *How To Start A
  Startup*", "Brian Chesky founder-commitment", "ten-
  year-time-horizon", "no Plan B", "no moonlight,
  full-time only", "founder-takes-no-salary until
  milestone", "raise to win not to hedge", "great hires
  follow conviction", "customers feel commitment",
  "investors back conviction over hedging", "the
  startup is not an experiment", "this is the bet."
- **Excludes**:
  - The "burn the boats" reflex *destroys household
    financial stability* for founders with dependents,
    mortgage, and family obligations — single-no-
    dependents founders can rationally leap with $20k
    savings and a credit card, but a single-income-with-
    kids-and-mortgage founder applying the same standard
    bankrupts the family if the startup fails (which is
    the modal outcome). The framing's commitment-as-
    selection-mechanism is a *founder-personal-finance
    selection mechanism* that biases against family-
    obligation founders, who are not necessarily lower-
    quality but face higher commitment-cost. The Indie
    Hackers / r/SmallBusiness voices catch the household-
    context-conditioning; YC playbook voice often
    abstracts it. Opposes F13 (optionality-preservation)
    on D3 / D2. Boundary `personal-finance` D2.
  - "Founder takes no salary for 12 months until
    milestone" is *correct posture for founders with
    runway* but *destructive for founders without* —
    the discipline can become rationalization for
    accepting catastrophic personal-finance damage
    (deferred medical care, deferred dental, missed 401(k)
    contribution years, accumulated credit-card debt at
    20%+ APR that destroys future net-worth even at
    successful exit). The framing's "all-in" reflex
    rarely engages with the *non-trivial* personal-
    finance cost of going-without, particularly the
    catastrophic-and-irreversible-medical-event tail
    risk. Boundary `health-insurance` and `personal-
    finance`.
  - "Customers feel commitment" / "investors back
    conviction" are *plausible but not measurably
    falsifiable* claims — the framing's rhetoric is
    self-reinforcing in a way that makes it hard to
    distinguish from *founder-self-flattery rhetoric*.
    Empirically, many investors back hedged-founders
    (after-all-the-spouse-is-CEO-elsewhere arrangements,
    fractional-CEO-shared-with-other-portfolio cases,
    founder-on-sabbatical-from-BigCo), and many
    customers buy from companies they think are
    sustainable specifically because they have hedged-
    founders with reliable financial footing. The
    framing's strong-claims about commitment-as-asset
    are partially-correct narrative; the strong-version
    is rhetorical rather than measured. PG voice tends
    to the strong version; the empirical research is
    more mixed.
  - The framing under-engages with *commitment-as-
    sunk-cost-rationalization* — founders 4 years into
    a company that isn't working can use "I'm committed,
    I won't quit" to justify continued effort on a path
    that data suggests should be abandoned. The
    conviction-rhetoric makes pivoting or shutting-down
    feel like personal failure rather than rational
    capital-allocation, and the framing rarely surfaces
    the *when-to-quit* calibration. The optionality-
    preservation framing's "two-way door" thinking
    catches this; the conviction-commitment framing's
    rhetoric resists it. Opposes F13 on D2 (when to
    abandon a non-working trajectory).

---

## Coverage map

Per `_schema.md`, every decision needs ≥ 3 framings.

| Decision | Framings that cover it | Count |
|---|---|---|
| D1 Co-founder selection / equity / vesting / IP-assignment | F3, F5, F8, F13 | 4 |
| D2 Bootstrap vs raise pre-seed / seed | F1, F2, F13, F14 | 4 |
| D3 Quit day job vs nights-and-weekends | F2, F8, F13, F14 | 4 |
| D4 LLC pass-through vs S-corp election | F4, F5, F6 | 3 |
| D5 SAFE post-money cap vs priced seed | F1, F5, F13, F14 | 4 |
| D6 Sole-prop vs LLC formation timing | F4, F6, F13 | 3 |
| D7 First W-2 employee vs 1099 contractor | F6, F7, F12 | 3 |
| D8 Solo-401(k) vs SEP-IRA vs SIMPLE | F4, F5, F13 | 3 |
| D9 Pricing model selection | F2, F9, F10 | 3 |
| D10 First employee vs contractor vs offshore | F1, F9, F10, F11, F12 | 5 |
| D11 Co-founder departure / cap-table-buyback / dispute resolution | F3, F7, F11, F12 | 4 |

All 11 decisions satisfy the ≥3 framings minimum. F13 (optionality-
preservation) is the cross-cutting hedging framing applied to
nearly every irreversible-commitment decision; F14 (conviction-
commitment) is its direct opposite and applies most prominently
to the leap-or-don't-leap and raise-or-not decisions; both
function as Critic / Editor meta-context framings on top of any
primary decision lens. F11 (founder-mode) and F12 (manager-mode)
similarly apply most heavily to hiring-and-management decisions
(D10 / D11) but inflect every founder-execution decision implicitly.

## Cross-framing tensions

Direct axiom-level oppositions to surface in Layer 3 and to flag
for Triage / Risk Officer routing when the asker's prompt
vocabulary lands on one side:

- **F1 (raise-and-scale) ↔ F2 (bootstrap / default-alive)**.
  Same company, same product, same founder pair — opposite
  capital-strategy recommendation. F1 says raise pre-seed to
  compress time-to-PMF and add senior hires; F2 says
  ramen-profitability is the validation signal and capital
  postpones the discovery of what customers will actually pay
  for. Triage should surface F1 when the asker mentions VC
  fundraising, board structure, dilution math, or names
  venture-scale targets; surface F2 when the asker mentions
  MRR transparency, ramen-profitability, indie-hackers ethos,
  or names lifestyle-business-acceptable outcomes. The
  conflict is most visible on D2 directly and inflects D9
  (pricing — PLG-friction-minimization vs revenue-from-day-1
  capture).

- **F9 (PLG / product-led-growth) ↔ F10 (SLG / sales-led-
  growth)**. Same SaaS product, opposite go-to-market
  motion and opposite hiring sequence. F9 says invest in
  product polish + self-serve onboarding + activation
  metrics + freemium-to-paid funnel; F10 says invest in AE /
  BDR / CSM hire ahead of revenue, build the enterprise
  sales process, target high-ACV deals. The decision
  surface is D9 (pricing model) and D10 (hiring sequence)
  jointly. Triage should surface F9 when the asker mentions
  freemium / self-serve / activation / NRR-from-expansion /
  PLG-canon (Slack / Notion / Figma); surface F10 when the
  asker mentions enterprise / SOC 2 / MEDDIC / quota /
  AE-OTE / CAC-payback. Hybrid PLG-with-sales-overlay
  motions are increasingly common (Notion-for-Enterprise,
  Atlassian Enterprise) and the framings can co-exist
  rather than purely conflict.

- **F11 (founder-mode) ↔ F12 (manager-mode)**. Same
  CEO, opposite scaling philosophy. F11 says stay in the
  details across product / hiring / customer through Series
  B and beyond; F12 says invest in the executive layer and
  delegate to scale past founder bandwidth. The conflict
  surfaces on D10 (hiring philosophy — IC-deep vs VP-layer-
  first) and D11 (departure handling — founder-mode
  companies struggle, manager-mode companies absorb).
  Triage should surface F11 when the asker mentions PG
  *Founder Mode* / Brian Chesky / Steve Jobs / skip-level /
  stay-in-the-details; surface F12 when the asker mentions
  scalable-org / OKR / VP-of-X / professional-management /
  hire-from-Google. The framings are both partially-correct
  at different company-stages and depend critically on
  founder personality and company-stage; experienced VCs
  often coach toward F11 pre-PMF and F12 post-Series-A,
  but both extreme versions have failure modes.

- **F13 (optionality-preservation) ↔ F14 (conviction-
  commitment)**. Same founder, opposite philosophy on
  hedging. F13 says preserve the day-job-IP-carve-out,
  delay LLC formation, choose SAFE over priced, document
  everything to keep two-way doors open; F14 says burn
  the boats, quit the day job on conviction, commit to
  the cap-table structure that signals all-in, hire
  people who match commitment-level. The conflict surfaces
  most visibly on D3 (quit-day-job vs nights-and-weekends),
  D2 (bootstrap vs raise), and D5 (SAFE postponement vs
  priced commitment). Triage should surface F13 when the
  asker mentions runway / fallback / preserve-options /
  two-way-door / Patio11 anti-platitude; surface F14 when
  the asker mentions ten-year-horizon / no-Plan-B /
  founder-all-in / burn-the-boats / Sam-Altman-conviction.
  Both framings have rationalization failure modes (F13
  → indefinite indecision; F14 → sunk-cost continuing
  past data-driven quit signal).

- **F5 (QSBS / tax-tail-event) ↔ F2 (bootstrap / default-
  alive) on D5**. F5 argues for early C-corp conversion
  and priced-round timing to start the QSBS clock on
  founder stock — the 5-year-hold-period is a tax-tail
  worth tens of millions on successful exit. F2 argues
  for LLC simplicity and delayed-formation, treating the
  entity question as second-order to revenue-and-customer
  validation. Same founder pre-formation, opposite
  recommendation. The conflict resolves on whether the
  founder-and-business is plausibly venture-scale (F5
  dominates) or lifestyle / niche (F2 dominates with QSBS
  having low practical relevance). Triage should surface
  F5 when the asker mentions VC raising / liquidity event
  / exit / $10M+ outcome; surface F2 when the asker
  mentions SaaS / consulting / niche-B2B / lifestyle
  business.

- **F8 (day-job-fallback / opportunity-cost) ↔ F14
  (conviction-commitment) on D3**. F8 says wait until
  the next vest cliff, carve out the side-project IP in
  writing, maintain the day-job as the safe baseline.
  F14 says the day-job-as-baseline is itself a hedge
  that signals lack of conviction, and customers /
  investors / hires can feel it. Same household-context,
  same MRR-level, opposite leap-recommendation. Triage
  should surface F8 when the asker mentions vesting
  cliff / RSU schedule / household-runway / health-
  insurance / spouse-income; surface F14 when the asker
  mentions conviction / commitment / ten-year-horizon /
  no-Plan-B. The conflict often resolves on the asker's
  personal-finance situation (dependents, household-
  income-diversification) rather than on principle.

- **F4 (SE-tax-and-entity-arbitrage) ↔ F5 (QSBS / tax-
  tail-event) on D4**. F4 says S-corp election saves
  15.3% × distribution-portion of FICA arbitrage starting
  at the ~$80-100k crossover. F5 says S-corp is INCOMPATIBLE
  with QSBS — QSBS requires C-corp throughout
  substantially-all of the 5-year-hold-period, so the
  S-corp election eliminates QSBS eligibility. For
  potentially-venture-scale founders, F5 dominates the
  arbitrage entirely: locking in 15.3% × $100k = $15k/yr
  of SE-tax savings is a poor trade for eliminating a
  potential $10M+ QSBS exclusion. For non-venture-scale
  consulting / service businesses, F4 dominates because
  QSBS is practically irrelevant. The conflict resolves
  on plausible-exit-trajectory; founders straddling
  the boundary should explicitly model both paths with
  a startup-experienced CPA. Boundary `personal-finance`
  F4 / F8 / F10 on QSBS-and-S-corp coordination.

- **F11 (founder-mode) ↔ F12 (manager-mode) at growth-
  stage transition**. The same founder, having succeeded
  in founder-mode pre-Series-A, faces the question of
  whether to *continue* founder-mode at 100+ employees
  or transition to manager-mode. F11 says the founder's
  direct-line-of-sight is still the highest-leverage
  signal source; F12 says the founder-bottleneck cost
  exceeds the founder-detail-value past a certain
  employee count. The transition is *the* hardest
  scaling decision and many founders mis-time it in
  either direction (transitioning too early loses the
  founder-DNA advantage; transitioning too late caps
  growth). Triage should surface this tension when the
  asker mentions employee-count > 50, post-Series-A
  scaling questions, executive-team-design, or VP-hire
  decisions. Boundary `tech-career` on engineering-
  management scaling.

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  every `Excludes` bullet above is a Layer 3 candidate.
  Highest-density candidates are framings 1 (raise-and-
  scale — well-funded-pre-PMF burning-without-discovery,
  founder-level-failure-asymmetry-vs-investor-portfolio,
  cumulative protective-provision lock-in, market-cyclicality
  abstraction), 2 (bootstrap — network-effects category
  hand-off to venture-backed competitor, legitimate-
  investment-phase distinction missed, household-context-
  constraint elision, under-investment in growth at
  ramen-profitable), 3 (founder-fairness — LLC-vs-Delaware-
  C-corp 83(b) mechanics divergence, 50/50-as-statistical-
  correlation-not-mandate, post-incorporation co-founder
  addition mechanics, vague for-cause definition becoming
  dispute-ground), 4 (SE-tax — state-and-SSTB-adjusted
  crossover variation, S-corp-retirement-contribution
  trade-off, RCReports-not-bright-line audit-risk,
  multi-member-LLC tax-treatment complexity), 5 (QSBS —
  redemption-tests disqualification, family-stacking
  geometry, LLC-to-C-corp conversion mechanics, state-
  conformity divergence for CA-NY-NJ residents), 6
  (liability-shield — solo-software-consulting-over-LLC,
  veil-piercing case-law state-variation, trust-fund-tax
  personal-liability under IRC §6672, LLC-vs-C-corp
  shield-equivalence assumption), 7 (ABC-test — over-W-2-ing
  legitimate-bounded-1099, contractor-own-LLC doesn't
  immunize hiring entity, FTC non-compete rule rapidly
  shifting, contractor-bargaining-power asymmetric
  exposure post-separation), 8 (day-job-fallback —
  W-2-stability-overstated, anticipated-business-as-fuzzy-
  term employer-response-pattern, Roth-conversion-window
  under-engaged, MRR-threshold-not-growth-slope), 11
  (founder-mode — micro-management rationalization,
  beyond-200-person scaling, identity-affirmation
  masking-poor-performance, board-relationship cost),
  12 (manager-mode — over-hiring-executive-layer-pre-
  PMF, BigCo-individual-calibration-question, OS-
  framework cargo-culting, founder-capacity-to-delegate
  not addressed), 13 (optionality-preservation — failure-
  to-commit rationalization, interpersonal-friction
  preventing documentation, option-value-decay-over-time,
  founder use is qualitative not quantitative), and 14
  (conviction-commitment — household-financial-stability
  destruction, no-salary discipline catastrophic personal-
  finance damage, commitment-claims rhetorical-not-
  measured, sunk-cost rationalization). Sweep all 14
  framings × ~4 bullets each = ~56 blindspot candidates;
  promote ≥5 per framing into `blindspots.md` per the
  [`_schema.md`](../_schema.md) minimum.

- **High-stakes posture (Mechanism E selective rather
  than uniform)**: this domain is `high_stakes: false` per
  `_meta_ontology.md` §6, so the Editor layer should NOT
  blanket-defer every decision to a professional. Editor
  on any answer that lands on these framings should
  (per `domain_pack.md` once authored) explicitly label
  the output as "decision-support framing rather than
  professional advice" and route to the *specific
  category-appropriate professional* only on the six-
  figure-tail-risk pockets enumerated in
  [`decisions.md` §Notes](./decisions.md) — startup-
  attorney with founder-side experience (Cooley /
  Gunderson / WSGR / Orrick / Fenwick high-end; Clerky /
  Stripe Atlas / Atomic / Mintz accessible) for D1
  (co-founder equity + IP-assignment), D5 (SAFE-to-
  priced-seed conversion + priced rounds), and D11
  (any disputed departure with >10% equity at stake or
  non-compete / non-solicit / IP-trailing claim);
  S-corp-experienced CPA (NOT generic 1040-prep) for
  D4 (S-corp election with multi-state nexus or SSTB
  phaseout) and D8 (retirement-vehicle selection
  coupled with S-corp election); employment-law
  attorney for D7 (first W-2 employee in ABC-test-strict
  state) and D11 (co-founder departure with non-compete
  / non-solicit dispute). State Bar / FINRA BrokerCheck /
  state-bar-grievance lookup on any individual
  professional recommended is the $0-friction
  procedural floor. The Critic must apply stricter
  grounding on citation-bearing claims (IRC §1202 QSBS,
  IRC §83(b), IRC §199A QBI / SSTB, IRC §409A FMV
  pricing, IRC §351 §721 entity-conversion, IRS Watson
  v US 2012 reasonable-salary, CA Labor Code §2870 /
  §16600 / AB-5 / PAGA, FTC 2024 non-compete rule,
  Delaware General Corporation Law §141 / §211 / §220,
  11 USC §523 / §727 discharge-and-veil-piercing, IRS
  Form 2553 / Form 8832 / Form SS-4 / Form 1099-NEC /
  Form W-2 / Form 5500); generic "the law says X"
  claims unanchored to a cite should fail Critic
  review. The selective-referral posture is the
  calibration that distinguishes `entrepreneurship`
  from the uniformly-Mechanism-E-gated
  `personal-finance` / `health-insurance` /
  `immigration` / `family-planning` / `legal-disputes`
  domains.

- **Triage routing notes**: framings 4, 5, 7, 9, 10
  carry the most distinctive vocabulary signatures
  (Form 2553 / Schedule SE / Watson v US / §199A QBI;
  IRC §1202 / 5-year-hold / "originally issued" /
  $10M-or-10x basis / CA-NY-NJ non-conformity;
  ABC-test / AB-5 / PAGA / §16600 / FTC-non-compete-rule;
  PLG / activation-rate / NRR / freemium-to-paid;
  MEDDIC / MEDDPICC / AE / quota / CAC-payback) and
  should be high-confidence routing matches. Framings
  1, 2, 3, 6, 8, 13, 14 share vocabulary with general
  entrepreneurship content and will need disambiguation
  against adjacent domain packs once V2 two-pass
  Triage is wired — particularly against
  `personal-finance` (which overlaps F4 / F5 / F8 on
  tax-mechanics, retirement vehicles, and Roth-
  conversion timing), `tech-career` (which overlaps
  F8 deeply on day-job-fallback / opportunity-cost
  and golden-handcuffs RSU mechanics), `legal-disputes`
  (which overlaps F3 / F7 / F11 / F12 on founder /
  employment / co-founder disputes), and `health-
  insurance` (which overlaps F8 on coverage-loss-at-
  leap and F12 on small-group eligibility on first
  W-2 hire). F11 (founder-mode), F12 (manager-mode),
  F13 (optionality-preservation), and F14 (conviction-
  commitment) are Critic / Editor meta-context
  framings; they should NOT route as the primary
  decision-framing on most answers but should be
  available for Editor framing-aware completions on
  top of a primary decision lens.

- **Cross-domain edges from `decisions.md`**: F1
  (raise-and-scale) crosses into `personal-finance`
  (founder-stock 83(b) and QSBS Section-1202 timing),
  `tech-career` (employer-IP-assignment carve-out from
  prior W-2, golden-handcuffs RSU-cliff cost of leap),
  and `housing` (HELOC / cash-out-refi as bridge
  capital, mortgage-qualification with 1099 / S-corp
  distribution income). F4 (SE-tax-and-entity-arbitrage)
  routes into `personal-finance` (solo-401(k) employee
  deferral on W-2 salary, SEP-IRA on net SE earnings;
  QBI Section-199A reduction by W-2-salary portion;
  pro-rata-IRA-trap on backdoor-Roth from SEP balance),
  and `housing` (mortgage-qualification with S-corp-
  distribution income discounted 75% with 2 years of
  returns required). F5 (QSBS / tax-tail-event) routes
  into `personal-finance` heavily (Section 1202 $10M-
  or-10x-basis gain exclusion, 5-year-hold-period,
  federal-state divergence on QSBS — CA / NY / NJ
  non-conformity), and `legal-disputes` (QSBS reset-on-
  incomplete-stock-issuance disputes). F7 (ABC-test-
  and-worker-classification) routes into `legal-disputes`
  heavily (CA PAGA exposure, wage-and-hour class-action
  precedent, FTC 2024 non-compete rule status in
  litigation), and `tech-career` (founder hiring former
  W-2 colleague with non-compete from prior employer).
  F6 (liability-shield / corporate-veil) routes into
  `legal-disputes` (piercing-the-corporate-veil
  precedents, fraudulent-conveyance look-back,
  undercapitalization defense), `personal-finance`
  (umbrella-policy coordination with business E&O /
  D&O), and `housing` (LLC-titled-real-property and
  mortgage-due-on-sale-clause interaction). F8 (day-
  job-fallback / opportunity-cost) routes into
  `tech-career` (day-job-fallback-option-value
  decay, golden-handcuffs from RSU vesting cliffs),
  `personal-finance` (Roth-conversion window on
  low-income year; emergency-fund sizing and asset-
  allocation shifts), and `health-insurance` (loss of
  employer coverage on leap, ACA vs spousal vs COBRA).
  F11 (founder-mode) and F12 (manager-mode) route
  into `tech-career` (founder recruitment voice as
  hiring asymmetry; founder-led-hiring vs delegated-
  hiring at scale). Triage should surface these
  adjacencies when the user's situation spans both
  domains.

- **Voice-anchor → sources.yaml hand-off** (Layer 4
  forward-pointer): the conceptual voices named in
  the intro map to these candidate source-view
  families. Indie Hackers → indiehackers.com community
  + podcast + interview archive, Hacker News bootstrap-
  themed Show HN / Ask HN threads. r/Entrepreneur →
  Reddit subreddit pinned posts and weekly threads,
  with quality filter for top-voted multi-comment
  threads vs single-noise posts. r/SmallBusiness →
  Reddit subreddit pinned posts and operator-
  experience threads with payroll / worker-classification
  / state-tax ground truth from in-the-trenches voices.
  Hacker News startup voices → news.ycombinator.com
  Show HN / Ask HN threads, paulgraham.com essay
  archive (*Default Alive or Default Dead*, *Founder
  Mode*, *Maker's Schedule, Manager's Schedule*, *Do
  Things That Don't Scale*), blog.samaltman.com
  archive (*Startup Playbook*, *How To Be Successful*),
  Garry Tan / Initialized commentary (Twitter and
  Initialized blog). Patio11 / Patrick McKenzie →
  Bingo Card Creator post-mortem at
  kalzumeus.com/category/bingo-card-creator, Stripe
  Atlas founder docs and articles at
  stripe.com/atlas/guides, Kalzumeus blog at
  kalzumeus.com (anti-platitude posts, salary-
  negotiation, software-business economics), now
  patio11.substack.com. YC playbooks → How To Start A
  Startup CS183B Stanford lectures (full transcripts
  publicly available), YC Startup School curriculum
  at startupschool.org, YC Library at
  ycombinator.com/library (especially Jessica
  Livingston / Michael Seibel / Dalton Caldwell /
  Aaron Epstein content). SaaStr / Jason Lemkin →
  saastr.com daily blog and podcast archive, SaaStr
  Annual conference videos, *From Impossible to
  Inevitable*. Tomasz Tunguz / Redpoint blog →
  tomtunguz.com (Series A burn-multiple benchmarks,
  sales-efficiency metrics, AI-startup pricing
  analysis). Lenny Newsletter →
  lennysnewsletter.com (product / PM growth-loops,
  hiring playbooks, OKR templates, user research
  patterns, podcast archive). First Round Review →
  firstround.com/review (operator-interview format
  from First Round portfolio executives, hiring /
  management / scaling tactical playbooks). a16z
  growth essays → a16z.com (growth-stage thinking,
  network-effects taxonomy, PMF measurement
  frameworks). Founder Collective → David Frankel /
  Eric Paley commentary at foundercollective.com
  (anti-venture-trap framing, capital-efficiency
  moat). The Finance Buff → thefinancebuff.com Harry
  Sit (solo-401(k) plan-document analysis for Mega-
  Backdoor-Roth eligibility, SEP-IRA-vs-solo-401(k)
  pro-rata-trap mechanics, S-corp arithmetic — shared
  voice with `personal-finance` framings.md). Clerky
  → clerky.com handbook and incorporation docs (83(b)
  filing instructions, SAFE templates, option-grant
  docs and 409A coordination). Stripe Atlas →
  stripe.com/atlas (Delaware C-corp formation,
  Mercury Bank coordination, founder agreement
  boilerplate, founder Slack community). IRS-
  publication-authority → IRS Pub 535 (business
  expenses), Pub 583 (starting a business), Pub 587
  (home-office deduction), Pub 463 (travel /
  entertainment), Pub 15 (employer-tax-guide), Pub
  560 (retirement plans for small business). State-bar
  lawyer-referral → state-bar lawyer-referral-services
  (NOT for-profit finders), CLA Business Law Section,
  ABA Section of Business Law. SEC EDGAR / FINRA
  BrokerCheck → sec.gov/cgi-bin/browse-edgar for any
  institutional investor's Form D filings,
  brokercheck.finra.org for individual broker-dealer
  diligence. Sources author should weight reliability
  and keyword_filter per `_schema.md`; the selective-
  referral posture means reliability ≥3 is sufficient
  for general framing claims, with ≥4 required for
  direct citation in Editor framing-claims on the six-
  figure-tail-risk pockets (D1 / D4 / D5 / D7 / D8 /
  D11). IRS-publication-authority and state-bar
  voices are uniquely permitted to ground statute-and-
  rule claims that conflict with practitioner-blog
  interpretations.
