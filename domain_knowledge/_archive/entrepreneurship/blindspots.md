# entrepreneurship — blindspots.md (Layer 3)

Blindspot catalogue for `entrepreneurship`. Each entry names what a real
practitioner in the relevant framing would say is missed — anchored to
either an `Excludes` line in [`framings.md`](./framings.md), a cross-
domain edge in [`decisions.md`](./decisions.md), or a named community
voice (Indie Hackers / r/Entrepreneur / r/SmallBusiness / Hacker News /
Patio11 / YC playbooks / SaaStr / Tomasz Tunguz / Lenny / First Round
Review / a16z / Founder Collective / The Finance Buff / Clerky / Stripe
Atlas / IRS-publication-authority). Per [`_schema.md`](../_schema.md),
every entry is relative to a framing and ships with a trigger pattern, a
failure-mode dollar figure, and a concrete recovery move.

The `entrepreneurship` domain is **high_stakes: false** per
[`_meta_ontology.md` §6](../_meta_ontology.md) — failure is the modal
outcome (75-90% of startups per CB Insights distributions) and is
generally survivable for a knowledge-worker founder who retained a
credible day-job-return path. Unlike the uniformly-Mechanism-E-gated
domains (`personal-finance` / `health-insurance` / `immigration` /
`family-planning` / `legal-disputes`), Recovery moves here are
**selectively** routed to professional counsel only on the six-figure-
tail-risk pockets enumerated in [`decisions.md` §Notes](./decisions.md):

- **D1** (co-founder equity split + vesting + IP-assignment): startup
  attorney with founder-side experience (Cooley / Gunderson / WSGR /
  Orrick / Fenwick high-end; Clerky / Stripe Atlas / Atomic / Mintz
  accessible).
- **D4** (LLC vs S-corp election + multi-state nexus + SSTB phase-out):
  S-corp-experienced CPA (NOT generic 1040-prep CPA) modeling break-
  even by state, net-income, SSTB-status, and target retirement-
  contribution.
- **D5** (SAFE post-money cap vs priced seed for any priced round):
  startup attorney for cap-table modeling and term-sheet negotiation;
  founder-side counsel separate from any investor-recommended counsel.
- **D7** (first W-2 employee vs 1099 in any ABC-test state — CA, MA,
  NJ, IL, NV, others): employment-law attorney for classification
  analysis and worker-misclassification exposure.
- **D8** (solo-401(k) vs SEP-IRA vs SIMPLE retirement vehicle coupled
  with S-corp election arithmetic): CPA with retirement-plan and
  S-corp experience; The Finance Buff voice as the procedural floor on
  plan-document analysis for Mega-Backdoor-Roth eligibility.
- **D11** (co-founder departure with >10% equity at stake or any non-
  compete / non-solicit / IP-trailing claim): both startup attorney
  (cap-table / IP) and employment-law attorney (separation / non-
  compete); consider engaging counsel on BOTH sides for clean
  separation.

State Bar / FINRA BrokerCheck / state-bar-grievance lookup on any
individual professional recommended is the $0-friction procedural floor
named on every individual-professional referral. For framings that do
NOT land on D1 / D4 / D5 / D7 / D8 / D11 (i.e. F2 bootstrap / F8 day-
job-fallback / F9 PLG / F10 SLG / F11 founder-mode / F12 manager-mode /
F13 optionality-preservation / F14 conviction-commitment when they
operate on non-tail-risk decisions), Recovery moves are **self-
directed** with named-resource pointers (Indie Hackers community,
r/Entrepreneur top-voted threads, Patio11 essays, YC Library, SaaStr
playbooks, Lenny Newsletter, First Round Review, Clerky / Stripe Atlas
handbooks, IRS Pub 535 / 583 / 587 / 463 / 15 / 560).

Each blindspot lists:
- **Statement** — 1-3 sentences naming the specific wrong belief or
  omission, written in the voice of the asker who would hold it
- **Source-evidence** — the framing-Excludes anchor, the
  decisions.md cross-domain edge, or the named community-voice
  audit line this blindspot was extracted from (not invented)
- **Trigger** — the specific situation pattern (exact $-threshold,
  employee count, state-nexus event, conversion event, departure
  scenario) the Triage / Risk Officer should match against
- **Failure-mode** — the concrete dollar / equity / liability loss the
  blind spot causes if not surfaced
- **Recovery-move** — the concrete action that resolves it; for the
  six-figure-tail-risk pockets (D1 / D4 / D5 / D7 / D8 / D11) routed
  to the specific category-appropriate professional channel; for
  other pockets self-directed with named-resource pointer

The framing names below match [`framings.md`](./framings.md) F1-F14
exactly; all 14 are covered with ≥ 5 entries each (≥ 70 total). Where a
blindspot lives at a cross-domain edge, the adjacent domain is named
inline (`personal-finance` / `tech-career` / `legal-disputes` /
`housing` / `health-insurance`) so V2 two-pass Triage can route the
adjacency.

---

## 1. Raise-and-scale / venture-capital framing (F1)

### F1.1 Pre-PMF capital accelerates discovery of the wrong thing, not the right thing

- **Statement.** "We raised $2M pre-seed so we could hire 5 engineers
  and ship faster — capital compresses time-to-PMF." The framing
  treats outside capital as monotonically PMF-accelerating, but pre-
  PMF spend typically discovers the *wrong* thing faster: a 6-month
  build of a thing nobody wants ends in the same dead-end as an 18-
  month build of a thing nobody wants, only with more engineers
  invested in the dead-end and a higher psychological cost of pivoting.
- **Source-evidence.** `framings.md` F1 first Excludes bullet — "pre-
  PMF spend typically discovers the wrong thing faster, not the right
  thing faster"; Bootstrap / default-alive voice (F2) and Patio11
  voice as the structural correctives.
- **Trigger.** Founder has raised $1M+ pre-seed with no paying
  customers AND no validated willingness-to-pay signal beyond design-
  partner LOIs / verbal intent AND is hiring 3+ engineers within the
  first 90 days post-close.
- **Failure-mode.** 18-24 months of $80-120k/month burn ($1.5-3M total)
  spent building features against a hypothesis customers don't validate
  with cash; the company runs out of runway in a market downturn unable
  to raise a bridge without revenue traction; full shutdown with
  founder reputation cost on the venture circuit.
- **Recovery-move.** Before deploying raised capital, force the
  ramen-profitable test: would 10 customers pay $X/month right now
  for the thing the team is about to build? If no, the capital is
  funding hypothesis-testing rather than scaling; shrink the team
  and lengthen the runway. Self-directed: Paul Graham *Default Alive
  or Default Dead* essay; YC Library customer-discovery materials.

### F1.2 Founder failure-asymmetry vs investor portfolio diversification

- **Statement.** "Venture math says 1-in-10 returns the fund, so we
  accept that failure is the modal outcome." The framing imports
  portfolio-thinking from the investor level to the founder level
  without adjusting for the asymmetry: investors diversify across
  20-40 portfolio companies and only need one to return; the founder
  has one company and *all* the founder's career-capital-and-time is
  concentrated in that single outcome.
- **Source-evidence.** `framings.md` F1 second Excludes bullet —
  "venture math requires founders accept failure of the company as
  modal outcome, but founder personal-finance and reputation
  consequences are routinely understated"; Founder Collective voice
  (David Frankel / Eric Paley) on "venture-as-debt" framing.
- **Trigger.** Founder is comparing venture-portfolio expected-value
  arithmetic ("1-in-10 returns the fund") to their own personal
  decision AND has no household-financial-stability backstop (single-
  income, dependents, mortgage) AND no validated re-employability path
  (no maintained network, no recent technical-skill freshening, no
  carved-out side-project IP).
- **Failure-mode.** Company shuts down at year 3; founder faces 6-12
  months of unemployment + investor-relationship cost + "the company
  that didn't work" reputation friction on subsequent fundraising;
  household exhausts savings, deferred medical / dental / retirement-
  contribution years compound into a $200k+ personal-net-worth-vs-
  counterfactual hit.
- **Recovery-move.** Model the founder-personal-finance scenario at
  the venture-failure modal outcome separately from the company-
  outcome — what does the household look like at month 36 with a
  shut-down company, $0 founder savings, and 6 months of unemployed
  job-search? If that scenario is catastrophic rather than survivable,
  the founder-level risk profile doesn't match the investor's
  portfolio-level risk profile. Cross-domain edge: `personal-finance`
  (emergency-fund sizing per F8 day-job-fallback).

### F1.3 Cumulative protective-provision lock-in across rounds

- **Statement.** "Take the best lead investor's term sheet at the cap
  they offer — secondary terms are negotiable later." The framing
  treats round-by-round term-sheet negotiation as independent events,
  missing that protective provisions (investor consent for sale, debt
  above $X, new equity issuance, material change of business), board-
  seat-and-observer rights, and pro-rata side-letters *compound*
  across rounds in ways the founder systematically under-models at
  Series A and discovers at Series B / acquisition.
- **Source-evidence.** `framings.md` F1 third Excludes bullet —
  "institutional capital is not free in the dilution arithmetic —
  board seats, information rights, protective provisions, and pro-
  rata side-letters compound across rounds"; Founder Collective voice
  catches this; YC playbook voice often doesn't.
- **Trigger.** Founder is raising Series A and the term sheet includes
  standard NVCA-template protective provisions AND the cap-table
  already has 1-2 prior SAFE / convertible-note / seed-round investors
  with their own protective provisions or pro-rata letters AND no
  startup attorney has modeled the cumulative consent-stack required
  for major-corporate-actions at Series B / acquisition.
- **Failure-mode.** Year 5 acquisition offer for $50M with founders
  retaining 35% combined; the deal requires consent of 60% of
  preferred (Series A + Series B); a single Series A investor with
  10% economic ownership controls the consent because of a protective-
  provision majority threshold; investor blocks the deal seeking a
  higher price; founders watch the acquisition collapse; subsequent
  shop-around lands at $30M nine months later. Net founder cost: $5-
  8M in lost deal value plus 9 months of distraction.
- **Recovery-move.** **D5 high-stakes pocket — consult a startup
  attorney with founder-side experience** (Cooley / Gunderson / WSGR /
  Orrick / Fenwick) to model the cumulative protective-provision
  stack across all existing rounds plus the proposed new round BEFORE
  signing the term sheet; specifically request the attorney compute
  the major-corporate-action consent threshold at Series B and
  acquisition under the combined documents. State Bar verification on
  the recommended attorney via the state-bar member-search before
  engagement.

### F1.4 Venture-market cyclicality treated as background noise

- **Statement.** "Raise quickly and focus on building" — the framing
  treats venture-market liquidity as a stable backdrop, missing that
  funding availability is *cyclical* (2021 ZIRP boom collapsed to
  2023-2024 pullback; sub-Series-A rounds in cyclical-downturns can
  take 6-12 months and require 100+ investor meetings) and the
  founder's 24-month-runway-target-against-known-burn calculus needs
  explicit market-condition awareness.
- **Source-evidence.** `framings.md` F1 fourth Excludes bullet — "the
  framing assumes a liquid venture market — but venture-funding
  availability is cyclical"; SaaStr / Tomasz Tunguz voices catch the
  cyclicality, YC playbooks often abstract it. Cross-domain edge to
  `tech-career` on layoff-cycle interaction (founder hiring becomes
  cheaper in a tech-layoff cycle but customer-buying-budgets also
  contract).
- **Trigger.** Founder is raising in 2024-2025 cycle conditions
  (downturn / partial-recovery) with 18 months of runway AND has not
  modeled a scenario where the next round takes 9-12 months instead of
  3-4 months AND has no signal-validated growth metrics
  (deterministic-multiple-on-revenue, not anecdotal LOIs).
- **Failure-mode.** Founder targets close-by-month-15 with a 3-month
  fundraising process; reality is 9-month process with 80 investor
  meetings; runway exhausts at month 18 mid-process; company is forced
  into a bridge / down-round at 50% discount to last round; founders
  face additional 30-40% dilution they didn't budget for.
- **Recovery-move.** Build the explicit cycle-condition runway model
  with three scenarios — fast-raise (3 months), normal-raise (6
  months), slow-raise (9-12 months) — and confirm the runway clears
  the slowest scenario plus 3-month buffer before deploying capital
  on hires. Self-directed: SaaStr "From Impossible to Inevitable"
  fundraising chapter; Tomasz Tunguz quarterly venture-market
  analysis.

### F1.5 The "lead investor sets the terms" reflex blocks shopping the round

- **Statement.** "The lead sets the terms; secondary investors fill
  the round." The framing's lead-centric posture treats the term
  sheet as a single negotiation with the chosen lead, missing that
  *shopping* the round (running parallel-process with 3-5 leads
  competing) materially improves valuation, board structure, and
  protective-provision flexibility — particularly for founders with
  signal-strong traction in a tight market.
- **Source-evidence.** Hacker News / Founder Collective voice on
  fundraising-as-negotiation; Tomasz Tunguz quarterly venture-market
  analysis on lead-investor competitive dynamics; YC playbook voice
  on "shopping the round" as a Series-A move.
- **Trigger.** Founder has 2+ interested leads with verbal-strong
  signals AND is reflexively pursuing the first-mover's term sheet
  AND has not run an explicit parallel-process timeline (all leads
  delivering term sheets within a 1-week window).
- **Failure-mode.** Founder accepts first-mover term sheet at $30M
  pre-money with a 1.5x liquidation preference and a board seat; a
  competing lead would have offered $40M pre-money with 1x non-
  participating preference and observer-only board structure; founder
  forgoes $3-5M of valuation upside and accepts an extra protective-
  provision-stack burden that compounds at Series B (see F1.3).
- **Recovery-move.** Once first-meaningful-signal arrives from any
  lead, telegraph to all leads "term sheets by [date 10 business days
  out]" and run a parallel process. **D5 high-stakes pocket — consult
  a startup attorney** for term-sheet comparison framework BEFORE
  signing any single sheet; the attorney's comparison is 5-10x
  cheaper than the term-delta the founder negotiates against the
  benchmark.

---

## 2. Bootstrap / default-alive framing (F2)

### F2.1 Calendar-time-on-revenue cedes network-effects categories to venture-backed competitors

- **Statement.** "Calendar-time-on-revenue is the founder's most-
  valuable asset; bootstrap to revenue before raising." The framing's
  bootstrap-pace reasoning holds for durable-market categories but
  *loses categorically* in network-effects-heavy categories
  (marketplaces, social, payments, B2B-with-procurement-stickiness):
  18 months of bootstrap-pace growth can hand the category to a
  venture-backed competitor that achieves irreversible distribution
  advantage.
- **Source-evidence.** `framings.md` F2 first Excludes bullet — "in
  network-effects-heavy categories, losing 18 months of growth
  velocity to bootstrap-pace can hand the category to a venture-
  backed competitor"; a16z growth-essays voice on network-effects
  taxonomy as the structural corrective.
- **Trigger.** Founder is bootstrapping in a category that exhibits
  any of: (a) explicit two-sided marketplace mechanics, (b) strong
  network-value (the product becomes more valuable as more users
  adopt it), (c) procurement-stickiness in B2B (vendor consolidation
  pressure favors incumbent vendors), (d) data-network-effects (more
  users → more data → better product) AND a well-funded competitor
  has emerged in the same category within the past 12 months.
- **Failure-mode.** Year 2: bootstrap-pace business at $400k ARR with
  20% YoY growth; venture-backed competitor at $4M ARR with 200% YoY
  growth and 5x distribution headcount; competitor signs the 3 largest
  enterprise prospects the bootstrap founder had been courting;
  category consolidates around competitor by year 3; bootstrap founder
  forced into niche-pivot or shutdown.
- **Recovery-move.** Categorize the market explicitly — does it
  exhibit winner-take-most dynamics or fragmented-stable dynamics? If
  winner-take-most AND venture-backed competition is real, the
  bootstrap default does not apply categorically and the founder
  should model an explicit raise-or-exit decision. Self-directed:
  a16z "Network Effects Manual" / "When Network Effects Fail"
  essays; review the canonical PLG-canon list (F9.3) for category
  precedents that did vs did NOT support bootstrap-pace winning.

### F2.2 Unit-economics-at-small-scale dismisses legitimate scale-dependent business models

- **Statement.** "Unit economics must work at small scale; companies
  that 'lose money on every sale but make it up in volume' are
  rationalizing." The framing correctly catches unit-economics
  rationalization patterns but over-applies, dismissing legitimate
  scale-dependent models where customer acquisition cost is
  structurally cheaper at scale (network-effects-driven referral,
  content-SEO compounding, brand-equity ROI on enterprise sales).
- **Source-evidence.** `framings.md` F2 second Excludes bullet —
  "under-engages with the legitimate-investment-phase distinction —
  there are real categories where customer acquisition is structurally
  cheaper at scale"; boundary `personal-finance` on capital-efficiency
  framing.
- **Trigger.** Founder is in a category that exhibits one of: (a)
  content-SEO compounding (organic-traffic CAC declines with content
  inventory), (b) referral-loop network effects (each user produces
  new users at zero marginal CAC), (c) brand-equity enterprise sales
  (year-3 win-rate materially higher than year-1 because of pattern-
  recognition by enterprise procurement) AND is benchmarking against
  the Indie Hackers default of "unit economics at month 1."
- **Failure-mode.** Founder kills a content-SEO-driven SaaS at month
  18 because CAC is $200 with LTV of $400 (2x — fails the
  Indie Hackers 3x bar); the model would have hit CAC of $40 with
  LTV of $400 (10x) by month 30 as content inventory compounded;
  founder forgoes a $5-10M ARR business that would have emerged from
  the legitimate scale-dependent compounding.
- **Recovery-move.** Distinguish between *rationalization* (the
  business has no real path to better unit economics — bad) and
  *legitimate investment phase* (the business has a mechanically-
  understood path where unit economics improve with scale — fine).
  Specify the mechanical reason unit-economics will improve and the
  expected timeline; if the answer is "scale will fix it" without a
  specified mechanism, F2's rationalization-detection is correct;
  if the answer names content-inventory / referral-loops / brand-
  equity-compounding, the F2 default does not apply. Self-directed:
  First Round Review on content-marketing economics; a16z on growth-
  loops taxonomy.

### F2.3 Founder personal-runway is the binding bootstrap constraint, not market opportunity

- **Statement.** "Bootstrap to revenue, raise from a position of
  strength." The framing rarely surfaces that bootstrap requires
  18-24 months of founder personal-runway as an implicit $X/year
  personal-salary forgone investment, and household-risk-bearing-
  capacity (single-income-with-kids-and-mortgage vs dual-income-no-
  dependents) determines whether bootstrap is even feasible.
- **Source-evidence.** `framings.md` F2 third Excludes bullet —
  "Bootstrap forces founder personal-runway compression — the
  founder's 18-24-month personal savings are functionally a $X/year
  personal-salary forgone investment, and the framing rarely surfaces
  this implicit-cost"; r/Entrepreneur voice catches the household-
  context constraint better than Indie Hackers voice. Cross-domain
  edge: `personal-finance` D2 (emergency-fund sizing for self-employed
  households).
- **Trigger.** Founder is reasoning from Indie Hackers / r/SmallBusiness
  content that assumes single-no-dependents AND has dependents +
  mortgage + sole-income status AND has not modeled an 18-24-month
  zero-income household scenario with healthcare costs, school costs,
  and emergency-event-reserve.
- **Failure-mode.** Bootstrap founder with dependents drains $80k
  emergency fund + $40k credit-card debt at 24% APR + $30k 401(k)
  early-withdrawal (10% penalty + ordinary income) over 18 months;
  business hits $4k MRR at month 18; founder forced back to W-2 for
  household-cashflow reasons; the business dies not from lack of
  product-market-fit but from household-financial-collapse before PMF
  emerged.
- **Recovery-move.** Build the explicit household-cashflow model with
  18 / 24 / 30-month zero-income scenarios; confirm at least 24
  months of cleared expenses (PITI, healthcare, school, emergency-
  event-reserve at $20k floor) before the bootstrap leap. Cross-
  domain edge to `personal-finance`: keep the emergency fund OUTSIDE
  the bootstrap-runway calculation. Self-directed: r/SmallBusiness
  "first year" threads; The Finance Buff on household-runway for
  self-employed; consider `health-insurance` cross-domain (COBRA-to-
  Marketplace transition under F8.5).

### F2.4 Ramen-profitability as ceiling rather than floor for growth investment

- **Statement.** "I'm ramen-profitable at $40k MRR; the bootstrap
  path is working." The framing's celebration of small-team
  productivity premium can rationalize *under-investment in growth*
  when growth would have durably increased enterprise value —
  founders happily at $40k MRR for 3 years may be missing the
  legitimate moment to hire 2 growth engineers and accelerate to
  $200k MRR.
- **Source-evidence.** `framings.md` F2 fourth Excludes bullet —
  "Ramen-profitability as the success metric encourages under-
  investment in growth when growth would have durably increased
  enterprise value"; Indie Hackers voice biases this way; YC playbook
  voice catches the under-investment failure mode.
- **Trigger.** Founder is at $30-100k MRR for 24+ months with 2-10%
  month-over-month growth AND identifies specific growth-investment
  hypotheses (content team, SEO, paid acquisition, sales-augmented
  PLG funnel) with hypothesized 30-50% growth lift AND is choosing
  to NOT invest because "we're profitable now."
- **Failure-mode.** Year 4: still at $50k MRR while a less-disciplined
  competitor with $2M in capital reaches $500k MRR and starts compress-
  ing the founder's category; founder watches the moat erode and
  realizes they should have invested 2 years earlier; the option to
  re-raise from strength has weakened because growth-curve no longer
  shows the curve venture investors fund.
- **Recovery-move.** Explicit growth-investment hypothesis review
  every 12 months at any sustained ramen-profitable state: name 2-3
  specific growth experiments with cost / hypothesized-lift /
  required-team; deploy retained earnings (not raised capital) to
  test the highest-ROI experiment for 6 months; if the lift
  materializes, scale the experiment rather than rest on ramen-
  profitability. Self-directed: First Round Review on bootstrap-to-
  growth transition; SaaStr on the $1-10M ARR-as-the-hard-part
  curve.

### F2.5 The "raise from strength or not at all" reflex misses the strategic-window timing

- **Statement.** "We don't need this money so we won't raise" — the
  framing's commitment to capital-efficiency can rationalize *missing*
  a strategic fundraising window where the company genuinely benefits
  from capital (talent-market shift, distribution-channel-window
  closing, M&A-platform-roll-up opportunity) and the future window
  may not re-open in similar conditions.
- **Source-evidence.** Founder Collective / Tomasz Tunguz voices on
  strategic-fundraising-timing; cross-domain edge to `tech-career`
  on talent-market-window (a tech layoff cycle creates a 6-12 month
  window to hire senior engineers at 20-30% below normal comp).
- **Trigger.** A specific strategic event has emerged that capital
  would enable (a category-leading senior hire is suddenly available,
  a distribution-partner deal requires capital to commit, a roll-up
  acquisition is on the table) AND the founder is reflexively
  declining-to-raise on capital-efficiency-as-virtue grounds AND has
  not modeled the strategic-window cost separately from the
  capital-efficiency baseline.
- **Failure-mode.** Senior-eng-hire-of-a-decade is available at a
  20% discount due to layoff cycle for a 3-month window; founder
  declines to raise the $1M that would have funded the hire on
  bootstrap-purity grounds; senior hires at competitor; competitor
  ships the product the founder was building 12 months earlier than
  the founder will.
- **Recovery-move.** Distinguish between *general* fundraising
  reflex and *strategic-window* opportunistic capital. Model the
  specific strategic event in isolation — what does the company look
  like if we have the capital and act, vs if we don't? If the
  strategic event genuinely produces 18-24 months of compressed
  advantage, the bootstrap default doesn't apply for this event
  specifically. Self-directed: Founder Collective on "venture-as-
  debt" framing; Tomasz Tunguz on talent-market-window analysis.

---

## 3. Founder-fairness-and-vesting framing (F3)

### F3.1 Delaware-C-corp-default obscures the LLC-to-C-corp-conversion path bootstrap founders take

- **Statement.** "Issue founder restricted stock with 4/1 vesting and
  file 83(b) within 30 days." The framing's Delaware-C-corp-default
  reflex obscures that LLC-formed companies issue *membership
  interests* (not stock), 83(b) elections on LLC profits-interests
  vs capital-interests have materially different mechanics (Rev Proc
  93-27 safe-harbor for profits-interests; capital-interests get
  83(b) like restricted stock), and founders converting LLC to
  C-corp later face complex tax-consequence analysis.
- **Source-evidence.** `framings.md` F3 first Excludes bullet — "the
  framing's Delaware-C-corp-default obscures the LLC-or-S-corp-then-
  convert path that bootstrap founders often take"; boundary
  `personal-finance` D6 on 83(b) mechanics.
- **Trigger.** Founders are forming as LLC (cost / tax-passthrough /
  state-fee considerations) OR have already formed as LLC and are
  considering C-corp conversion in 6-18 months AND are reading
  Delaware-C-corp-default founder-restricted-stock advice without
  adjusting for LLC-membership-interest mechanics.
- **Failure-mode.** Founders form LLC, "skip" 83(b) thinking it
  applies only to stock; year 2 LLC converts to C-corp for a priced
  round; founder discovers each future vesting tranche from the
  prior LLC profits-interests is now subject to ordinary-income tax
  at then-current FMV during conversion; tax bill at conversion is
  $80-150k on a $500k FMV conversion event.
- **Recovery-move.** **D1 high-stakes pocket — consult a startup
  attorney with founder-side experience plus an S-corp / LLC-tax-
  experienced CPA** (NOT generic CPA) BEFORE issuing any LLC
  membership interests; specifically request analysis of profits-
  interests vs capital-interests treatment, Rev Proc 93-27 safe-
  harbor applicability, and the planned LLC-to-C-corp conversion
  path's tax implications. State Bar verification on the attorney;
  CPA's prior LLC-to-C-corp conversion experience verified before
  engagement.

### F3.2 50/50-as-statistical-correlation forced into mandate creates relationship damage

- **Statement.** "Wasserman's data shows 50/50 splits correlate with
  post-Series-A founder conflict, so vesting-asymmetric is the
  honest framing." The framing's "asymmetric vesting is more honest"
  advice misapplies a statistical correlation as a causal mandate;
  forcing asymmetry where contributions are genuinely equal creates
  its own resentment cost and damages the founder relationship at
  the moment when the relationship is most valuable (pre-product
  pivot, pre-PMF discovery).
- **Source-evidence.** `framings.md` F3 second Excludes bullet —
  "'50/50 splits correlate with higher post-Series-A conflict' is a
  statistical correlation in Wasserman's data, not a causal mandate
  to avoid 50/50"; Indie Hackers / r/Entrepreneur voice leans 50/50-
  is-fine; YC playbook voice leans away.
- **Trigger.** Two co-founders with genuinely-equal contributions
  (similar time-commitment, similar technical/business contribution,
  similar pre-incorporation work, similar risk-bearing on the leap)
  are being pressured by advisor / lawyer / accelerator-mentor
  toward asymmetric split on Wasserman-data grounds without
  attention to the specific founder-pair contribution distribution.
- **Failure-mode.** Founders accept 60/40 split with junior founder
  ceding equity on advisor pressure; relationship is poisoned within
  6 months by resentment ("we agreed it was equal"); junior founder
  departs at month 14 with mostly-vested equity but no continuing
  contribution; company faces departure-renegotiation distraction
  + cap-table mess at the moment product is finding traction.
- **Recovery-move.** Distinguish *contribution-asymmetry* (one
  founder is bringing materially more time / technical-skill /
  network / pre-incorporation-work) from *role-asymmetry* (different
  but equal-value contributions like technical vs business);
  asymmetric vesting is justified for contribution-asymmetry, NOT
  for role-asymmetry. **D1 high-stakes pocket — consult a startup
  attorney** for the equity-split conversation if there is any
  founder-disagreement, but reject "always asymmetric" advice that
  treats Wasserman's correlation as causation. Self-directed: Noam
  Wasserman *Founder's Dilemmas* (the book itself, NOT advisor
  citation-of-the-statistic in isolation).

### F3.3 Post-incorporation co-founder addition mechanics rarely surfaced

- **Statement.** "We're adding a technical co-founder 4 months after
  incorporation — they'll get standard founder equity." The framing
  rarely surfaces that post-incorporation co-founder addition has
  three non-trivial paths — (a) fresh 4-year-vesting grant starting
  at join date (under-vested for years vs original founders), (b)
  restructuring original founders' grants to align starts (creates
  new 83(b) windows possibly past 30 days), (c) treating as early-
  employee with option pool grant (under-aligns incentive) — and the
  trade-offs interact with the 83(b) window irreversibility.
- **Source-evidence.** `framings.md` F3 third Excludes bullet —
  "framing under-engages with post-incorporation co-founder addition
  — all three approaches have non-trivial trade-offs"; boundary
  `legal-disputes` D11.
- **Trigger.** Founders are adding a third / fourth co-founder 3+
  months post-incorporation AND are reflexively granting "founder-
  equivalent" equity at the new co-founder's join date AND have not
  consulted a startup attorney on the 83(b) timing implications for
  the original founders' grants if grants are restructured.
- **Failure-mode.** Restructuring path chosen; original founders'
  grants are re-issued with new vesting start dates; the re-issuance
  is treated as a new grant for 83(b) purposes but the 30-day
  window from re-issuance was missed because founders thought their
  original 83(b) covered the new grant; each future vesting tranche
  now triggers ordinary-income at then-current FMV (potentially $200-
  500k tax exposure at successful exit on a $5-10M founder stake).
- **Recovery-move.** **D1 high-stakes pocket — consult a startup
  attorney BEFORE adding any post-incorporation co-founder** to
  model the three paths with explicit 83(b) timing analysis and the
  CIIAA / prior-IP-carve-out re-papering required for original
  founders. Document the chosen path with original-founders' written
  consent; file any required 83(b) elections within 30 days of any
  re-issuance event with certified-mail confirmation. Self-directed
  baseline: Clerky handbook on multi-founder grant mechanics.

### F3.4 Vague "for-cause termination" definitions become litigation grounds

- **Statement.** "Use the standard founder agreement template — for-
  cause is defined as fraud, willful misconduct, material breach."
  The framing's "use the standard" reflex passes through definitional
  vagueness that becomes the dispute ground when a founder is asked
  to leave for performance or culture reasons that don't clearly meet
  "willful misconduct"; the load-bearing move is to negotiate
  explicit triggers and remedies at signing, when relationships are
  positive and counsel is cheap.
- **Source-evidence.** `framings.md` F3 fourth Excludes bullet —
  "'for-cause termination' is the load-bearing legal text in any
  departure scenario, and the standard founder agreement template
  often leaves it vague"; boundary `legal-disputes`.
- **Trigger.** Founders are signing founder-agreement / IP-assignment
  / equity-grant documents from a template (Clerky / Stripe Atlas /
  Cooley-template / accelerator-template) WITHOUT a separate review
  of for-cause / good-reason / acceleration-trigger definitions AND
  there is any contribution-asymmetry or skill-asymmetry between
  founders (the asymmetric-side has more dispute-incentive at
  departure).
- **Failure-mode.** Year 3 founder is asked to leave for performance
  reasons; the standard for-cause definition is ambiguous about
  whether sustained underperformance qualifies; departing founder
  refuses to accept buyback and threatens litigation; company faces
  6-12 months of distraction + $50-150k of attorney fees + cap-table
  unresolution at the moment a Series A round is being raised; round
  closes at 30% lower valuation due to disclosed founder dispute.
- **Recovery-move.** **D1 high-stakes pocket — consult a startup
  attorney** to draft explicit for-cause / good-reason / acceleration
  triggers at signing (specific behavioral / performance / time-based
  triggers; defined remedies; documented review-and-cure process);
  reject templated vagueness. The signing-time cost is $3-8k; the
  dispute-time cost is 10-50x. State Bar verification on the
  attorney; consider both-side counsel for genuinely asymmetric
  founder pairs.

### F3.5 Double-trigger-acceleration framing obscures the negotiation surface

- **Statement.** "Double-trigger acceleration on change-of-control
  is the market-standard founder protection." The framing treats
  "double-trigger" as a single binary, missing that the *definitions*
  inside double-trigger (what counts as change-of-control, what
  counts as good-reason termination, what percentage accelerates,
  what time-window) carry the real negotiation surface and the
  template defaults are routinely acquirer-favorable.
- **Source-evidence.** `framings.md` F3 mental-model framing on
  double-trigger; Founder Collective / startup-attorney blog voice
  on the negotiation-surface inside the template; boundary
  `legal-disputes` on M&A negotiations.
- **Trigger.** Founder is in late-stage negotiation OR M&A diligence
  AND is reading "double-trigger acceleration" as a single feature
  in the term sheet WITHOUT understanding the underlying definitional
  parameters (CoC definition, good-reason definition, acceleration
  percentage 25/50/75/100%, time-window 12/24 months).
- **Failure-mode.** Acquisition closes; acquirer terminates founder
  90 days post-close citing "restructuring"; founder believed double-
  trigger acceleration would apply, but the good-reason definition
  in the original grant required a specific list of triggering
  events that doesn't include the acquirer's stated reason; founder
  walks away with 60% unvested instead of 100% accelerated; net
  founder loss: $500k-$3M depending on the equity-and-exit size.
- **Recovery-move.** **D1 high-stakes pocket — consult a startup
  attorney** at the original-grant moment to negotiate the
  definitional details inside double-trigger (broad good-reason
  definition; full 100% acceleration; 12-month-post-close time-
  window; "constructive termination" coverage). Re-confirm at any
  subsequent equity event (refresh grants at Series B, secondary
  sales, etc.) that the original double-trigger terms carry through.

---

## 4. SE-tax-and-entity-arbitrage framing (F4)

### F4.1 $80-100k crossover hides material state-and-SSTB variance

- **Statement.** "S-corp election saves SE tax at the $80-100k net-
  income crossover." The framing's clean-break-even presentation
  hides material state-and-practice variance: CA's 1.5% S-corp tax +
  $800 minimum pushes the crossover to ~$100-120k; TX's no-state-
  income-tax brings it down to ~$60-80k; SSTB founders above the
  QBI Section-199A phase-out threshold lose the QBI deduction
  entirely and re-shift the trade-off.
- **Source-evidence.** `framings.md` F4 first Excludes bullet — "the
  '$80-100k crossover' heuristic is state-and-practice-dependent and
  the framing's clean break-even presentation hides material
  variance"; cross-domain edge to `personal-finance` D4 / D7;
  generic-CPA voices on Reddit commonly quote "$80k" without
  state-and-SSTB adjustment.
- **Trigger.** Founder is at $80-150k net SE income AND is reading
  generic "elect S-corp at $80k" advice from Reddit / generic-CPA /
  bookkeeping-blog content WITHOUT state-specific or SSTB-specific
  modeling AND is in a state with non-trivial S-corp-recognition
  variance (CA 1.5% + $800; NY-NYC UBT; TN franchise tax; LA / DC
  no S-corp recognition) OR is in an SSTB category (consulting, law,
  accounting, health, financial services).
- **Failure-mode.** CA-resident founder elects S-corp at $90k net
  income on generic-CPA advice; CA 1.5% S-corp tax + $800 minimum
  + payroll service ($1.5k/yr) + additional return-prep cost
  ($1.5k/yr) consume the entire SE-tax-savings; net annual benefit
  is -$200 instead of the +$3k the founder expected; founder is
  now locked into 5-year S-corp election with no benefit and
  significant administrative overhead.
- **Recovery-move.** **D4 high-stakes pocket — consult an S-corp-
  experienced CPA** (NOT generic 1040-prep CPA) to model the
  state-and-SSTB-adjusted break-even with current-year actuals and
  3-year projection; specifically request analysis of the QBI
  Section-199A interaction, state S-corp recognition, and payroll-
  service cost impact. State Bar (for CPA-attorney joint engagement)
  / CPA-license verification with the state board of accountancy.
  Self-directed baseline: The Finance Buff on S-corp arithmetic; IRS
  Pub 535 on business expenses.

### F4.2 S-corp election destroys retirement-contribution capacity by 30-40%

- **Statement.** "Elect S-corp at $80k to save SE tax." The framing's
  SE-tax-savings reflex understates that S-corp election COSTS
  retirement-contribution capacity: sole-prop with $200k net income
  can contribute $23,500 employee deferral + ~$36k profit-sharing =
  $59.5k solo-401(k); S-corp at $200k net paying $60k W-2 + $140k
  distribution can contribute $23,500 + $15k = $38.5k (profit-
  sharing capped at 25% of W-2 salary).
- **Source-evidence.** `framings.md` F4 second Excludes bullet —
  "S-corp election interacts adversely with retirement-contribution
  maximization — joint optimization is non-trivial and CPA-
  supported"; boundary `personal-finance` D8; The Finance Buff voice
  as the procedural floor on solo-401(k) plan-document analysis.
- **Trigger.** Founder is electing S-corp primarily for SE-tax
  arbitrage AND is also maximizing solo-401(k) contributions
  ($59.5k+ in 2024 for under-50; $66k+ for over-50) AND has not
  modeled the joint S-corp + retirement-contribution arithmetic
  with current-year actuals AND has not consulted a CPA experienced
  with BOTH S-corp election AND retirement-plan mechanics.
- **Failure-mode.** Founder elects S-corp at $200k net income with
  $50k W-2 salary; saves $11.5k in SE tax (15.3% × $75k
  distribution-above-FICA-wage-base) but loses $21k in retirement-
  contribution capacity vs sole-prop; net effective tax cost is
  +$3-5k/year depending on marginal-rate-trajectory (retirement
  contributions deferred at current rate, withdrawn at future rate).
  Over 20 years of compounded retirement-contribution-loss the
  founder's effective net-worth is $200-500k lower.
- **Recovery-move.** **D4 + D8 high-stakes pocket — consult an
  S-corp-AND-retirement-plan-experienced CPA** to model the joint
  optimization with explicit 20-year retirement-contribution-
  compounding analysis; specifically request the Mega-Backdoor-Roth
  eligibility analysis on the solo-401(k) plan-document. The Finance
  Buff voice on plan-document mechanics is the procedural floor for
  self-directed verification of the CPA's analysis.

### F4.3 Reasonable-salary defensibility is not a bright line; RCReports is insufficient alone

- **Statement.** "Use RCReports for reasonable-salary defensibility."
  The framing's "use RCReports" reflex understates that audit-risk
  is non-binary: IRS audit attention concentrates on S-corps paying
  obviously-low salaries (sub-$30k on six-figure-net-income is high-
  audit-risk), but the safe-zone is not a bright line — RCReports
  and BLS provide defensible benchmarks but a founder choosing a
  salary at the bottom of the benchmark range is more exposed than
  one at the median.
- **Source-evidence.** `framings.md` F4 third Excludes bullet —
  "'reasonable salary' defensibility is practice-dependent — IRS
  audit attention concentrates on obviously-low salaries, but the
  safe-zone is not a bright line"; Watson v US (8th Cir 2012) as
  the leading authority but the universe of post-Watson IRS audit-
  and-litigation patterns is broader than the case itself.
- **Trigger.** Founder is paying themselves W-2 salary at the bottom
  of the RCReports / BLS Occupational Employment Survey benchmark
  range (e.g., 10th percentile of comparable occupation) AND has
  net income above 3x the W-2 salary AND has not documented the
  reasonable-salary determination in a written file (RCReports
  output + occupational comparison + scope-of-work justification).
- **Failure-mode.** IRS audit at year 3 reclassifies $50k of
  distribution as additional W-2 salary subject to FICA; back-tax +
  interest + 20% accuracy-related penalty (IRC §6662) + state
  back-tax assessment; total exposure $20-40k for 3 prior years +
  legal / CPA defense fees $10-20k; founder also loses confidence
  in the S-corp arbitrage going forward and may exit the election.
- **Recovery-move.** **D4 high-stakes pocket — consult an S-corp-
  experienced CPA** for written reasonable-salary determination at
  median-or-higher of the occupational benchmark range AND maintain
  a contemporaneous written file (RCReports output, BLS data,
  scope-of-work-comparable, year-over-year-rationale) updated
  annually. Self-directed baseline: RCReports / BLS / Watson v US
  case-text + IRS S-corp audit guide (publicly available).

### F4.4 Single-member LLC-to-S-corp framing misses multi-member partnership complexity

- **Statement.** "Elect S-corp on the single-member LLC to save SE
  tax." The framing assumes the founder's W-2-vs-1099 status is
  clear, missing that founders of multi-member LLCs who are *also*
  W-2 employees of the LLC face material complexity: member-managers
  in some states cannot be W-2 employees of the same LLC;
  partnerships generally cannot pay members W-2 wages and must use
  guaranteed payments under IRC §707(c) with different FICA
  treatment.
- **Source-evidence.** `framings.md` F4 fourth Excludes bullet —
  "framing assumes the founder's W-2-vs-1099 status is clear — but
  founders of multi-member LLCs face material complexity"; boundary
  `legal-disputes` on partnership disputes.
- **Trigger.** Two-or-more co-founders forming multi-member LLC AND
  electing S-corp tax classification (via Form 8832 + Form 2553) AND
  paying themselves W-2 salary plus distributions WITHOUT consulting
  a CPA / attorney familiar with multi-member LLC partnership tax
  mechanics and the IRC §707(c) guaranteed-payments alternative.
- **Failure-mode.** IRS audit reclassifies multi-member LLC as
  partnership for state-law purposes; member-manager W-2 salary is
  disallowed; payroll-tax filings are amended (Forms 941, 940);
  guaranteed-payment treatment retroactively applied with different
  SE-tax-and-Medicare-tax calculation; founders face $30-80k in
  back-tax + penalty + amended-return-prep costs across 3 years.
- **Recovery-move.** **D4 high-stakes pocket — consult an S-corp-
  AND-partnership-experienced CPA** before forming a multi-member
  LLC with S-corp election AND state-specific employment-law
  attorney to confirm member-manager-as-W-2-employee status under
  state law. Document the chosen tax structure with written CPA
  opinion-letter for audit defense. Self-directed baseline: IRS
  Pub 541 (partnerships) + Pub 583 (starting a business).

### F4.5 Cross-state nexus from remote-W-2 hire ignored in S-corp arbitrage math

- **Statement.** "Elect S-corp and hire the first W-2 employee."
  The framing's domestic-state-of-incorporation reflex understates
  that hiring a W-2 employee in a different state creates *nexus*
  in that state for payroll, income-tax, and franchise-tax purposes;
  the S-corp's reasonable-salary math now has to clear *two* state
  S-corp regimes plus federal, and the multi-state apportionment
  arithmetic can erode the SE-tax-savings entirely.
- **Source-evidence.** Cross-domain edge: `tech-career` (remote-W-2
  hire nexus mechanics); r/SmallBusiness voice on multi-state
  payroll; The Finance Buff on cross-state S-corp mechanics; IRS
  Pub 15 (employer tax guide).
- **Trigger.** Founder is in S-corp election in State A AND is
  hiring first W-2 employee in State B (remote) AND has not
  consulted a CPA on the State B nexus implications (payroll
  registration, income-tax apportionment, franchise-tax exposure)
  AND has not budgeted for the multi-state payroll-service cost
  uplift ($1-3k/yr per additional state).
- **Failure-mode.** First W-2 hire in CA from a TX-incorporated
  S-corp; CA franchise-tax board asserts nexus on the entire
  company; $800 minimum CA franchise tax + 1.5% CA S-corp tax on
  the apportioned CA-income share + employer-side CA SDI / SUI /
  ETT registration + payroll-service multi-state uplift; net
  additional annual cost $3-6k that wipes out 30-50% of the
  expected SE-tax-arbitrage benefit.
- **Recovery-move.** **D4 + D7 high-stakes pocket — consult an
  S-corp-AND-multi-state-experienced CPA** BEFORE the first cross-
  state W-2 hire to model the nexus implications and update the
  S-corp arbitrage break-even. Engage a multi-state payroll service
  (Gusto / Justworks / Rippling) configured for the specific state
  combination. Self-directed baseline: IRS Pub 15; state-board-of-
  accountancy / state-employment-development-department for the
  hire-state.

---

## 5. QSBS-and-tax-tail-event framing (F5)

### F5.1 Redemption-tests silently disqualify QSBS for all shareholders

- **Statement.** "Hold 5 years from C-corp stock issuance for QSBS
  eligibility." The framing's clock-discipline alone catches the
  SAFE-conversion-delay case but routinely misses *redemption tests
  that disqualify QSBS*: §1202(c)(3) and (4) disqualify stock if the
  corporation makes significant redemptions of its own stock from
  the issuing shareholder (within 1 year before or after) or from
  other shareholders (within a 4-year window — 2 years before and
  2 years after issuance, threshold 5% of aggregate value);
  buyback programs and tender offers can silently disqualify QSBS
  for all shareholders.
- **Source-evidence.** `framings.md` F5 first Excludes bullet — "the
  '5-year hold from C-corp stock issuance' reflex catches the SAFE-
  conversion-delay case but routinely misses redemption tests that
  disqualify QSBS"; boundary `legal-disputes` on QSBS reset disputes;
  among the most-litigated QSBS edge cases.
- **Trigger.** Company is contemplating any stock-redemption event
  (employee secondary, founder secondary, departing-cofounder
  buyback, treasury-stock-repurchase program) AND any shareholder
  is relying on QSBS eligibility for their stake AND no startup-
  experienced tax attorney has reviewed the redemption against
  §1202(c) tests.
- **Failure-mode.** Company executes $2M employee-secondary tender
  offer in year 4; the tender exceeds the 5% aggregate-value
  threshold within the 4-year window; ALL shareholders' QSBS
  eligibility on stock issued within 2 years before the tender is
  silently disqualified; year 6 acquisition produces $20M founder
  gain that the founder believed was QSBS-eligible ($10M-or-10x-
  basis exclusion); actual federal tax bill is $4-5M instead of $0-
  1M; founder discovers the disqualification only during exit
  diligence.
- **Recovery-move.** **D1 + D5 high-stakes pocket — consult a
  startup-experienced tax attorney AND CPA** BEFORE any stock
  redemption event to model §1202(c) test compliance for all
  affected shareholders; structure the redemption to stay below
  thresholds or sequence it outside the 4-year window. Document
  the analysis in writing for audit / acquirer-diligence defense.
  State Bar verification on the tax attorney.

### F5.2 Family-stacking via non-grantor trusts unwound at exit-time

- **Statement.** "The $10M-or-10x-basis QSBS limit is per-issuer-
  per-taxpayer." The framing's solo-founder reflex misses the
  *stacking geometry*: families can stack the limit across family
  members and non-grantor trusts (each trust gets a separate $10M
  exclusion) — a founder with $50M+ projected gain can split equity
  pre-issuance to spouse, kids (via non-grantor trusts), or to
  multiple non-grantor trusts. But the stacking requires estate-
  attorney coordination at *formation*, NOT at exit (post-exit
  stacking is materially harder).
- **Source-evidence.** `framings.md` F5 second Excludes bullet —
  "the '$10M or 10x basis' limit is per-issuer-per-taxpayer, but
  families can stack the limit across family members and across
  non-grantor trusts"; boundary `personal-finance` D10 and
  `family-planning`.
- **Trigger.** Founder is at company-stage where projected exit
  value plausibly exceeds $10M-per-founder QSBS limit AND has not
  consulted an estate-and-tax attorney on family-stacking before
  significant stock issuance OR before SAFE-to-C-corp-conversion AND
  is family-formed (married, kids, parents-as-potential-trust-
  beneficiaries).
- **Failure-mode.** Founder is single-taxpayer at year 5 with $30M
  exit gain; uses $10M federal QSBS exclusion; remaining $20M is
  taxed at 23.8% federal (20% LTCG + 3.8% NIIT) = $4.76M federal
  tax. Pre-formation stacking via 2 non-grantor trusts for kids +
  spousal trust could have provided 3 additional $10M exclusions
  ($30M total) at $10-30k of formation cost; the founder forgoes
  $4-5M in tax savings by missing the formation-time window.
- **Recovery-move.** **D1 high-stakes pocket — consult a startup-
  experienced tax attorney AND estate-planning attorney TOGETHER**
  at formation or pre-priced-round if exit potential plausibly
  exceeds $10M-per-founder; specifically request non-grantor trust
  structures (Delaware / Nevada / Wyoming jurisdiction selection),
  attribution-rule analysis, and pre-issuance stock-transfer
  documentation. The formation-cost ratio to potential savings is
  1:100-1:500. State Bar verification on both attorneys.

### F5.3 LLC-to-C-corp conversion §351 mechanics require startup-experienced CPA

- **Statement.** "Convert LLC to C-corp before priced round to start
  QSBS clock." The framing's clean-conversion reflex understates
  that LLC-to-C-corp conversion mechanics are *non-trivial for
  QSBS*: the conversion is generally a §351 tax-free exchange, but
  the QSBS holding-period and "originally issued" requirements
  interact in ways CPAs routinely get wrong — the LLC interest
  being exchanged is not stock and the analysis turns on whether
  the LLC was conducting an active trade or business that qualifies.
- **Source-evidence.** `framings.md` F5 third Excludes bullet —
  "LLC-to-C-corp conversion mechanics are non-trivial for QSBS —
  CPAs routinely get the §351 exchange analysis wrong"; boundary
  `personal-finance` D1.
- **Trigger.** LLC is converting to Delaware C-corp for any reason
  (priced round, QSBS-clock-start, acquirer-preferred-structure)
  AND has been operating as LLC for 12+ months AND the conversion
  is being handled by a generic CPA (NOT one with startup / §351 /
  QSBS experience) AND no tax attorney has issued a written
  opinion on the QSBS-qualifying-property analysis.
- **Failure-mode.** Generic CPA files conversion documents without
  proper §351 documentation; year 6 exit at $40M founder gain; IRS
  / acquirer diligence challenges QSBS eligibility; the founder's
  position requires a costly retroactive opinion letter + amended
  returns + potentially full disqualification on the converted-stock
  portion; net loss $2-5M in tax + $30-80k in remediation legal /
  CPA cost.
- **Recovery-move.** **D1 + D4 high-stakes pocket — consult a
  startup-experienced CPA AND tax attorney with §351-and-QSBS
  expertise** BEFORE the LLC-to-C-corp conversion; specifically
  request a written opinion-letter on the qualifying-property
  analysis under §351 and the QSBS-eligibility analysis under
  §1202. Maintain conversion documentation (LLC's active-trade-or-
  business records, capital-account records, conversion-event-date
  evidence) for the duration of the QSBS holding period.

### F5.4 State-conformity divergence costs CA / NY / NJ founders the "tax-free" tail

- **Statement.** "QSBS provides federal exclusion up to $10M-or-10x-
  basis." The framing's "QSBS is tax-free" reflex is *only correct
  at the federal level* — California does NOT conform (CA-resident
  founder with $10M federally-excluded gain still pays CA top
  bracket 13.3% = $1.33M state tax); NY partially conforms; NJ
  does not fully conform. Residency-planning before liquidity event
  is the only recovery, and CA treats residency tests strictly.
- **Source-evidence.** `framings.md` F5 fourth Excludes bullet —
  "state-conformity divergence is load-bearing for founders in non-
  conforming states"; boundary `personal-finance` F4 and `housing`
  on residency planning.
- **Trigger.** Founder is CA / NY / NJ resident with anticipated
  QSBS-eligible exit in the next 24-36 months AND is reasoning from
  "QSBS is tax-free" content (Reddit / generic-startup-blog) AND
  has not modeled state-conformity divergence AND has not consulted
  a tax attorney on residency-planning timeline.
- **Failure-mode.** CA-resident founder believes the $10M exit is
  tax-free; receives $1.33M CA state tax bill + audit risk on
  any post-formation deductions taken at the CA rate; the founder's
  net-of-tax proceeds are materially lower than the planning model
  predicted; relocation-attempt at month 30 fails CA residency-
  test because CA's "domicile" analysis treats partial-year
  relocations as suspicious.
- **Recovery-move.** **D1 high-stakes pocket — consult a tax
  attorney with state-residency-planning experience** 18-24 months
  BEFORE the anticipated liquidity event; document the residency
  change with bright-line evidence (home sale + new home purchase
  in conforming state, driver's license, voter registration,
  professional licenses, primary medical-provider relocation, days-
  in-state log < 183 days). Cross-domain edge to `housing` on
  primary-residence relocation; `personal-finance` on the broader
  state-tax-residency analysis.

### F5.5 SAFE-stacking silently delays QSBS clock by 18-24 months

- **Statement.** "Raise on SAFEs until the priced round materializes."
  The framing's bootstrap-friendly SAFE-stacking reflex routinely
  misses that the QSBS 5-year-hold-period starts at C-corp stock
  issuance — NOT at SAFE issuance, NOT at LLC formation, NOT at the
  founder's first day of work; founders sitting on SAFEs for 18-24
  months pre-priced-round are silently losing 18-24 months of QSBS
  clock with no warning from generic CPAs.
- **Source-evidence.** `framings.md` F5 mental-model framing — "the
  5-year-hold-period starts at C-corp stock issuance — NOT at SAFE
  issuance"; reinforced in F5 third Excludes bullet on QSBS-clock
  load-bearing planning; one of the highest-leverage tax
  considerations for founder eventual-exit-net-worth and almost
  universally missed by non-startup-CPAs.
- **Trigger.** Company has raised 2+ SAFEs over 18+ months AND a
  priced round is foreseeable within 6 months AND the founders'
  QSBS-eligibility planning has not been reviewed by a startup-
  experienced CPA AND there is no documented analysis of whether
  to accelerate priced-round conversion to start the QSBS clock.
- **Failure-mode.** Founders raise 4 SAFEs over 24 months; priced
  Series A converts at month 26; QSBS clock starts at month 26;
  year-7 acquisition at month 86 (= 60 months from clock-start);
  full QSBS exclusion is achieved. But if priced round had been
  forced 12 months earlier, exit at month 86 would have been 72
  months from clock-start, with no QSBS-eligibility difference —
  HOWEVER, an earlier-foregone exit at month 74 from clock-start
  would have qualified vs. not. Specific scenario: $20M exit gain
  forgone QSBS-eligibility because clock was 4 months short; tax
  cost $4-5M federal + state.
- **Recovery-move.** **D5 high-stakes pocket — consult a startup-
  experienced CPA AND startup attorney** to model the SAFE-vs-
  priced-round QSBS-clock-start trade-off explicitly at every SAFE-
  issuance event; if priced round is foreseeable within 6-12 months
  AND exit potential is plausibly QSBS-relevant, model the cost-
  benefit of accelerating to priced round to start the clock. Self-
  directed baseline: Clerky handbook + Stripe Atlas QSBS-clock
  guidance.

---

## 6. Liability-shield / corporate-veil framing (F6)

### F6.1 LLC formation cost-benefit fails on solo-software-consulting

- **Statement.** "Form an LLC for the liability shield." The
  framing's shield-default reflex overstates the protection benefit
  for solo software consulting and other low-liability-surface
  businesses where the shield does little — the work-product is the
  only liability surface, and a well-drafted contract E&O clause +
  professional-E&O insurance does most of the actual protective
  work; for sub-$50k-revenue side-businesses in low-liability
  categories, CA's $800/year franchise tax can exceed the LLC's
  effective benefit.
- **Source-evidence.** `framings.md` F6 first Excludes bullet — "the
  framing's 'form an LLC for the shield' reflex overstates the
  protection benefit for solo software consulting and other low-
  liability-surface businesses"; Indie Hackers / r/Entrepreneur
  voice catches the cost-benefit analysis; boundary `personal-
  finance` D6.
- **Trigger.** Founder is solo software consultant / writer / digital-
  product seller AND is forming an LLC reflexively on accountant /
  registered-agent / online-formation-service recommendation AND
  has revenue under $50k AND is in a high-franchise-tax state (CA
  $800 minimum, NY publication requirement, MA $500 annual report)
  AND has no specific identified liability surface that the shield
  would meaningfully protect.
- **Failure-mode.** Solo consultant in CA forms LLC at $1,500
  formation cost + $800 CA franchise tax + $200/yr registered agent
  + $1,500/yr additional tax-return-prep; net annual administrative
  cost $2,500-$3,000 against revenue of $30k; the LLC provides no
  meaningful additional protection beyond what a well-drafted
  contract + $400/yr professional-E&O policy provides; the
  consultant's after-tax net income is 8-10% lower than the sole-
  prop counterfactual.
- **Recovery-move.** Self-directed: identify the specific liability
  surface BEFORE forming any entity; for solo software consulting,
  the recovery move is professional E&O insurance ($300-800/yr for
  a $1M-aggregate policy) + well-drafted MSA with explicit
  limitation-of-liability clauses, NOT entity-formation. Re-evaluate
  entity-formation when revenue crosses $80-100k OR when a specific
  liability surface emerges (employees hired, physical premises,
  customer data handled at scale). Self-directed baseline:
  r/SmallBusiness "do I need an LLC" threads; Patio11 essays on
  entity-formation timing.

### F6.2 Veil-piercing case-law varies sharply by state

- **Statement.** "Follow corporate formalities and the LLC shield
  holds." The framing's formality-discipline reflex captures only
  the easy cases (don't commingle funds, sign contracts as entity,
  file annual reports). Hard cases — undercapitalization, alter-ego,
  fraudulent-conveyance to defeat creditors, dominating-parent-
  corporation doctrine, single-economic-enterprise treatment — are
  litigated extensively and outcomes depend on state precedent
  (TX *Castleberry v Branscum* factors vs DE Trevino-and-Mason
  factors vs CA *Sonora Diamond Corp* alter-ego standard).
- **Source-evidence.** `framings.md` F6 second Excludes bullet —
  "'Piercing the corporate veil' precedents are highly state-and-
  fact-specific and the framing's 'follow formalities' reflex
  captures only the easy cases"; boundary `legal-disputes`.
- **Trigger.** Founder has formed LLC / C-corp AND is operating
  with thin capitalization (no separate business reserves, owner
  takes all available cash as distributions) OR has multiple related
  entities with shared management / shared accounts / shared
  premises AND is reasoning from generic "follow formalities"
  advice WITHOUT a state-specific veil-piercing risk review.
- **Failure-mode.** Year 3 customer dispute on a $200k contract
  goes to litigation; plaintiff's counsel pursues alter-ego /
  undercapitalization piercing theory; founder's personal assets
  ($300k home equity + $200k retirement) are now exposed; even if
  the piercing fails, founder spends $80-150k in legal defense and
  faces 18-24 months of dispute-distraction. Successful piercing
  produces personal judgment that follows the founder.
- **Recovery-move.** Self-directed for low-stakes operations: maintain
  separate bank accounts, sign as entity not individual, file
  annual reports / franchise-tax payments on time, maintain
  reasonable capitalization (at minimum 6 months of operating
  expenses in entity reserves). **D11 high-stakes pocket — consult
  a litigation-experienced business attorney** if facing actual
  veil-piercing claim OR if operating multiple related entities
  with thin capitalization; specifically request a state-specific
  factor analysis (e.g., CA *Sonora Diamond* factors). State Bar
  verification on the attorney.

### F6.3 Trust-fund taxes pierce all corporate shields under IRC §6672

- **Statement.** "The LLC shield protects me from business debts."
  The framing's shield-default reflex misses the trust-fund-tax
  exception: trust-fund taxes (payroll withholding, income-tax-
  withholding) under IRC §6672 and parallel state trust-fund
  statutes are NOT shielded by entity — any "responsible person"
  (typically defined as any officer with check-signing authority
  and duty to pay payroll taxes) is personally collectible for
  unpaid amounts plus 100% penalty.
- **Source-evidence.** `framings.md` F6 third Excludes bullet —
  "framing under-engages with trust-fund tax personal liability
  under IRC §6672 — these are NOT shielded by entity"; boundary
  `personal-finance` and `legal-disputes`.
- **Trigger.** Company has W-2 employees AND is experiencing cash-
  flow strain (any month where payroll-tax remittance is delayed
  or partially paid) AND the founder has check-signing authority
  AND no IRS / state-DOR voluntary-disclosure or installment-
  agreement has been initiated.
- **Failure-mode.** Cash-strained company falls 6 months behind on
  payroll-tax remittance ($80k unpaid trust-fund portion across 5
  employees); IRS Trust Fund Recovery Penalty assessment hits the
  founder personally at $80k + 100% penalty + interest = $160k+;
  company eventually files Chapter 7; the founder's personal IRS
  liability survives the bankruptcy (11 USC §523 trust-fund
  exception); IRS pursues wage garnishment / bank-account levy /
  asset seizure on the founder personally for years.
- **Recovery-move.** **D7 + D11 high-stakes pocket — consult an
  IRS-controversy-experienced attorney AND CPA immediately** if
  payroll-tax remittance is delayed beyond 1 month; initiate
  voluntary-disclosure / installment-agreement BEFORE IRS Trust
  Fund Recovery Penalty assessment (post-assessment options are
  materially narrower). The recovery move is to pay trust-fund
  taxes BEFORE any other creditor when cash-strained; this is the
  one obligation where the corporate shield does not protect the
  founder. Self-directed baseline: IRS Pub 15 employer tax guide.

### F6.4 LLC-vs-C-corp shield equivalence false; investor-expectations differ

- **Statement.** "LLC and C-corp shields are equivalent for liability
  purposes." The framing's "form an LLC" default treats the entity
  forms as shield-equivalent, but they differ on (a) tax treatment
  (LLC pass-through vs C-corp double-tax), (b) shareholder /
  member fiduciary duties (C-corp directors have stricter duties
  under DGCL §141; LLC members can structure duties down), (c)
  investor expectations (institutional VCs require Delaware C-corp
  for priced rounds; SAFEs typically presume C-corp issuer), (d)
  QSBS eligibility (C-corp only — see F5).
- **Source-evidence.** `framings.md` F6 fourth Excludes bullet —
  "LLC-vs-C-corp shield strength is commonly assumed equal — but
  they differ on tax treatment, fiduciary duties, investor
  expectations, QSBS eligibility"; boundary `personal-finance` F6.
- **Trigger.** Founder is choosing LLC over C-corp on cost / tax-
  passthrough / simplicity grounds AND has venture-trajectory
  intent (will raise priced round within 24-36 months) AND has not
  consulted a startup attorney on the eventual LLC-to-C-corp
  conversion cost / timing / QSBS-implications AND is reading
  generic "LLC is simpler" advice without venture-trajectory filter.
- **Failure-mode.** Founder forms LLC at month 0; raises 2 SAFEs at
  month 12; institutional VC at month 20 requires Delaware C-corp
  for priced Series A; conversion under §351 requires $15-30k of
  attorney + CPA fees + complex §351 documentation (see F5.3); the
  QSBS clock starts at month 20 instead of month 0 (loss of 20
  months); the founder's overall path costs an extra $20k + 20
  months of QSBS clock vs the Delaware-C-corp-from-day-1
  counterfactual.
- **Recovery-move.** **D1 high-stakes pocket — consult a startup
  attorney AT FORMATION** to choose entity form based on plausible
  trajectory (venture path → Delaware C-corp from day 1; bootstrap-
  only path → LLC fine; mixed / uncertain → C-corp at marginal
  $1-2k of initial-year cost over LLC, preserves optionality). If
  already LLC-formed and venture-path emerges, plan the conversion
  18+ months before priced round, NOT at term-sheet-signing pressure.
  Self-directed baseline: Clerky / Stripe Atlas entity-choice
  flowcharts.

### F6.5 Personal guarantees on commercial leases / SBA loans pierce the shield

- **Statement.** "The LLC shields me from business debt." The
  framing's general-shield reflex misses that most early-stage
  commercial obligations require *personal guarantees* — SBA loans
  (always require personal guarantee from 20%+ owners), commercial
  leases (most landlords require for leases under $1M / 5 years),
  business credit cards (personal guarantee standard), vendor
  trade-credit lines (variable). The shield protects only the
  founder against tort and non-guaranteed-contract claims; the
  guaranteed-contract claims pass through.
- **Source-evidence.** `framings.md` F6 mental-model framing on
  personal guarantee exceptions; r/SmallBusiness operator voice on
  SBA / commercial-lease / vendor-credit reality; cross-domain edge
  to `housing` (HELOC bridge capital with personal-guarantee
  passthrough) and `personal-finance` (umbrella-policy coordination
  with business E&O and D&O).
- **Trigger.** Founder is signing any of: SBA loan, commercial lease,
  business credit card, vendor trade-credit line AND has not read
  the personal-guarantee provisions AND is operating on the
  assumption that the LLC fully shields personal assets from the
  obligation AND has not negotiated guarantee-limitation (cap on
  guaranteed amount, time-decay of guarantee post-lease-expiration,
  release-on-financial-milestones).
- **Failure-mode.** Founder signs 5-year commercial lease for office
  space at $80k/yr with full personal guarantee on the entire lease
  term ($400k); company shuts down at month 18; landlord pursues
  founder personally for remaining 42 months of rent ($280k) +
  legal fees + interest; founder's personal assets exposed; this
  obligation survives Chapter 7 personal bankruptcy if not properly
  scheduled and discharged.
- **Recovery-move.** Read every personal-guarantee clause before
  signing; **D11 high-stakes pocket — consult a startup attorney**
  to negotiate guarantee-caps, time-decay, milestone-release. For
  SBA loans, personal-guarantee is non-negotiable but loan-amount
  can be sized to acceptable personal-risk; for commercial leases,
  negotiate to 6-12 months personal-guarantee with step-down or
  full release on milestone. Self-directed baseline: r/SmallBusiness
  threads on commercial-lease guarantee-negotiation; SBA loan
  guidance from sba.gov.

---

## 7. ABC-test / worker-classification framing (F7)

### F7.1 Over-W-2-ing legitimately bounded 1099 contractors creates unnecessary overhead

- **Statement.** "Classify as W-2 when in doubt." The framing's
  strict W-2-when-in-doubt reflex is correct for sustained
  engagements but *over-applies* to legitimately bounded 1099
  relationships (3-6 month project with clear deliverables, parallel-
  clients, own tools — the archetypal *bona fide* independent
  contractor). Some founders over-correct by W-2-ing every
  contractor regardless of relationship structure, which creates
  unnecessary payroll overhead and benefits-eligibility complexity.
- **Source-evidence.** `framings.md` F7 first Excludes bullet — "the
  framing's strict 'classify as W-2 when in doubt' reflex is correct
  for sustained engagements but over-applies to legitimately bounded
  1099 relationships"; r/SmallBusiness voice catches this
  distinction better than the `legal-disputes`-litigation voice does.
- **Trigger.** Founder is engaging a contractor for a defined,
  bounded project (specific deliverable, 3-6 month duration, defined
  scope) AND the contractor has multiple parallel clients AND uses
  their own tools / equipment AND has an independently-established
  business with marketing presence (LLC, website, prior client
  list) AND founder is reflexively W-2-ing on misclassification-
  risk-aversion grounds.
- **Failure-mode.** Founder W-2s a 4-month bounded designer contract
  at $25k total; payroll-service uplift ($300-500), employer-side
  payroll-tax (7.65% FICA + FUTA + SUI = ~$2.5k), benefits-
  eligibility complexity (does this person get health insurance for
  4 months?), and the additional administrative overhead consume
  10-20% of the contract value; the contractor wanted 1099 for
  Schedule C deductions and Sec 199A QBI eligibility and is
  unhappy.
- **Recovery-move.** Self-directed: apply the ABC test analytically
  to the specific engagement — does the contractor genuinely meet
  all three prongs? If yes AND the engagement is genuinely bounded
  (project-scoped, < 6 months, contractor has parallel clients),
  1099 is appropriate and W-2-when-in-doubt is over-correction. For
  any sustained engagement (> 6 months, no other clients, company-
  provided tools), default W-2. **D7 high-stakes pocket — consult
  an employment-law attorney** only if the engagement is borderline
  AND in an ABC-test state (CA, MA, NJ, IL, NV). Self-directed
  baseline: IRS Form SS-8 worker-classification determination
  guidance.

### F7.2 Contractor's own LLC does not immunize the hiring entity

- **Statement.** "They have their own LLC, so they're a real
  contractor." The framing's "real contractor" reflex routinely
  misroutes: "contractor through their own LLC" does NOT immunize
  the hiring entity from misclassification analysis. The ABC test
  applies to the *substance of the working relationship*, not the
  form of the payment vehicle. A CA software engineer billing
  through their single-member-LLC is still subject to ABC analysis;
  the LLC structure helps the worker's own tax position but does
  not protect the hiring company from PAGA / wage-and-hour claims.
- **Source-evidence.** `framings.md` F7 second Excludes bullet —
  "'contractor through their own LLC' does NOT immunize the hiring
  entity from misclassification analysis"; r/SmallBusiness voice on
  state-by-state variation (TX more permissive than CA).
- **Trigger.** Founder is hiring a sustained-engagement contractor
  in CA / MA / NJ / IL / NV AND the contractor invoices through
  their own LLC AND is performing work in the company's usual
  course of business (e.g., software engineer at a software
  company) AND founder is treating the LLC-payment-vehicle as
  conclusive evidence of contractor status.
- **Failure-mode.** CA-based software engineer "contractor" works
  for 24 months at $150k/yr invoicing through their LLC; contractor
  files PAGA claim post-departure on misclassification grounds;
  back-pay (overtime, meal-and-rest-break premium), waiting-time
  penalties (up to 30 days additional wages under CA Labor Code
  §203), PAGA penalties ($100/pay-period × ~52 = $5,200 initial +
  $200 × subsequent pay-periods × 4-year statute = $50k-150k total),
  unpaid employer-side payroll taxes + interest + attorney fees;
  total exposure $200-500k+ on a single misclassified worker.
- **Recovery-move.** **D7 high-stakes pocket — consult an
  employment-law attorney in the contractor's state of residence**
  before any sustained engagement in an ABC-test state; specifically
  request analysis of prong (B) "outside the usual course of
  business" — a software company hiring a software engineer
  through any payment vehicle does NOT pass prong B. If
  classification is borderline, default W-2. Self-directed baseline:
  CA Labor Commissioner's worker-classification guidance; AB-5 +
  AB-2257 statutory text.

### F7.3 FTC 2024 non-compete rule volatility requires verification timing

- **Statement.** "Check your state's non-compete law." The framing's
  state-default reflex understates the federal-rule-volatility on
  non-competes: CA's §16600 has voided non-competes for decades;
  the FTC issued a rule in 2024 broadly banning non-competes
  nationally (with limited carve-outs); the rule has been stayed
  and partially-struck in litigation (Northern District of Texas
  in *Ryan LLC v FTC*); status at any given moment requires
  verification with employment-law counsel.
- **Source-evidence.** `framings.md` F7 third Excludes bullet —
  "Non-compete enforceability is rapidly shifting: CA's §16600 has
  voided non-competes for decades; the FTC issued a rule in 2024
  broadly banning non-competes nationally"; non-solicit covenants
  (customer or employee) are more broadly enforceable than non-
  competes; boundary `legal-disputes`.
- **Trigger.** Founder is signing OR enforcing a non-compete clause
  in any jurisdiction (employee non-compete, founder non-compete
  on departure, M&A non-compete on acquisition) AND has not
  verified current FTC-rule status with employment-law counsel
  within the last 90 days AND is treating non-compete and non-
  solicit as equivalent in the analysis.
- **Failure-mode.** Founder enforces non-compete against departing
  co-founder on 2024-issued grounds that FTC rule blocks; co-
  founder counters with FTC-rule-citation; subsequent litigation
  costs $100-300k on a question that may resolve federally before
  the case concludes; meanwhile founder believes non-solicit
  (which would be enforceable) is equivalent and doesn't pursue
  the narrower non-solicit claim that would have actually held up.
- **Recovery-move.** **D11 high-stakes pocket — consult an
  employment-law attorney** for current FTC-rule status verification
  AND state-specific enforceability analysis BEFORE signing or
  enforcing any non-compete clause; specifically request analysis
  of non-solicit (customer + employee) as the narrower alternative
  that is more broadly enforceable than non-compete. Self-directed
  baseline: state-bar employment-law section publications; FTC
  non-compete-rule status tracker.

### F7.4 Contractor-side asymmetric exposure on post-separation misclassification claims

- **Statement.** "We've classified the engagement as 1099 with the
  contractor's agreement; we're protected." The framing's "the
  company is exposed" framing correctly identifies the company's
  risk but routinely under-engages with the *contractor-side
  incentive asymmetry*: a senior contractor with multiple parallel
  clients may *prefer* 1099 for tax-optimization reasons (Schedule
  C deductions, SEP-IRA / solo-401(k) capacity, QBI deduction)
  during the engagement, then retain the option to file a
  misclassification claim post-separation, capturing both the
  contractor-tax-benefits AND the misclassification-damages.
- **Source-evidence.** `framings.md` F7 fourth Excludes bullet —
  "framing under-engages with contractor's own perspective and
  bargaining power... the company's misclassification exposure is
  asymmetric"; boundary `tech-career` on senior-contractor
  positioning.
- **Trigger.** Founder is engaging a senior contractor (>$150k/yr
  total comp equivalent) in an ABC-test state on a sustained basis
  (>12 months) AND the contractor proactively requested 1099 status
  AND there is no written acknowledgment of the classification
  analysis OR no IRS Form SS-8 determination on file.
- **Failure-mode.** Senior contractor enjoys 18 months of 1099
  tax-optimization benefits (~$15-30k/yr); engagement ends in
  dispute; contractor files misclassification claim seeking
  back-wages + benefits + PAGA penalties + interest + attorney
  fees; total founder exposure $300-600k on the post-separation
  claim; the contractor's own front-end 1099 preference does NOT
  bar the claim because the ABC test is a statutory floor not a
  waivable contract term.
- **Recovery-move.** **D7 + D11 high-stakes pocket — consult an
  employment-law attorney** for any sustained-senior-contractor
  engagement in an ABC-test state; document the classification
  analysis in writing with contractor's signed acknowledgment of
  the analysis (the acknowledgment does NOT waive ABC-test
  application but provides evidentiary weight on intent). Better
  alternative: convert to W-2 with the contractor receiving
  benefits + employer-side tax + appropriate-comp adjustment.
  Self-directed baseline: IRS Form SS-8; CA Labor Commissioner
  guidance.

### F7.5 Lookback-period silently accumulates exposure during the engagement

- **Statement.** "We've been classifying correctly; we'll fix any
  issue going forward if it arises." The framing's "fix it going
  forward" reflex misses that misclassification damages accrue
  silently through the limitations period — CA's 4-year wage-and-
  hour statute (longer with continuing-violation theory), federal
  6-year statute on employment-tax claims; reclassifying going-
  forward does NOT cure the backward exposure, and the IRS's
  "responsible person" Trust Fund Recovery Penalty (F6.3) extends
  the personal-liability tail.
- **Source-evidence.** `framings.md` F7 mental-model framing on the
  4-year CA statute and continuing-violation theory; cross-domain
  edge to F6 trust-fund-tax personal liability (the misclassified
  worker's unwithheld payroll tax becomes responsible-person
  personal liability when the company can't pay).
- **Trigger.** Founder has been classifying borderline-cases as
  1099 for 12+ months in an ABC-test state AND now recognizes the
  classification is wrong AND is considering reclassifying going
  forward without addressing the backward exposure AND has not
  consulted employment-law counsel on the back-classification
  remediation paths (IRS Voluntary Classification Settlement
  Program, state-DOR voluntary disclosure, retroactive payroll-tax
  payment).
- **Failure-mode.** Founder reclassifies 3 contractors to W-2 at
  month 18; one contractor files misclassification claim 3 months
  later (within statute) for the 18-month historical period;
  founder's "we fixed it going forward" defense does NOT bar the
  historical claim; PAGA penalties + back-wages + waiting-time
  penalties on the historical period stack to $80-200k per
  contractor; founder's reclassification action is treated as
  admission of prior misclassification, weakening defense.
- **Recovery-move.** **D7 high-stakes pocket — consult an
  employment-law attorney AND IRS-controversy CPA** BEFORE
  reclassifying any worker from 1099 to W-2; specifically request
  analysis of IRS Voluntary Classification Settlement Program
  (VCSP) eligibility, state-DOR voluntary-disclosure availability,
  and structured remediation that minimizes plaintiff-counsel
  evidentiary leverage. The remediation cost is significant but
  uniformly less than the post-claim litigation cost.

---

## 8. Day-job-fallback / opportunity-cost framing (F8)

### F8.1 W-2-as-stable-baseline overstated across cycles

- **Statement.** "The day-job is the safe baseline; I'll leap when
  the startup signals are strong enough." The framing's "day-job-
  as-stable-income" baseline overstates W-2 stability — median FAANG
  tenure is ~2 years, PIP / RIF probability is non-trivial across
  cycles, and the implicit assumption that the day-job continues at
  current comp for the next 18-36 months is optimistic across
  cycles. The 2022-2024 tech layoff cycle demonstrated that *not
  leaping* also has tail-risk.
- **Source-evidence.** `framings.md` F8 first Excludes bullet — "the
  framing's 'day-job-as-stable-income' baseline overstates W-2
  stability — median FAANG tenure is ~2 years, PIP / RIF probability
  is non-trivial across cycles"; Tomasz Tunguz / SaaStr voices catch
  the cyclicality; boundary `tech-career`.
- **Trigger.** Founder is in tech / consulting / professional-services
  W-2 role AND is deferring startup leap on day-job-stability grounds
  AND has not modeled the W-2-tail-risk explicitly (probability of
  PIP / RIF / restructuring / acquisition-driven role-elimination)
  AND is in a sector showing layoff cycle conditions (current cycle:
  ad-tech / search / enterprise-software 2022-2024).
- **Failure-mode.** Founder defers leap 18 months on day-job-
  stability reasoning; receives RIF notice at month 12; severance
  is 3 months; founder now has 3 months of forced runway during
  which to leap (or job-search); the founder's "deferred-leap-on-
  stability" reasoning collapses; the founder also missed 18 months
  of side-project market-discovery that would have informed the
  leap timing better.
- **Recovery-move.** Self-directed: model the W-2-tail-risk
  explicitly with current cycle conditions (sector-layoff rates,
  PIP-probability for the role / level / company / tenure-cohort);
  add this probability-weighted-loss to the day-job-stability side
  of the leap calculus. Use severance-event windows (layoff, RIF,
  voluntary-separation, PIP-exit-package) as runway extenders. Cross-
  domain edge to `tech-career` on layoff-response and severance-
  negotiation. Self-directed baseline: SaaStr / Tomasz Tunguz tech-
  cycle analysis; r/cscareerquestions layoff-experience threads.

### F8.2 Anticipated-business as fuzzy term blocks employer-side carve-out

- **Statement.** "I'll carve out my side-project IP in writing with
  my employer." The framing's "carve out in writing" reflex
  underestimates that "anticipated business" in employer IP-
  assignment clauses is *deliberately fuzzy* — many employers refuse
  explicit carve-outs (so the founder is forced to drop, hide, or
  quit); HR / Legal often treats the request itself as evidence the
  side-project competes with employer's anticipated business and
  tightens enforcement; the carve-out request can accelerate the
  leap timeline beyond the founder's preferred schedule.
- **Source-evidence.** `framings.md` F8 second Excludes bullet — "the
  standard 'ask for carve-out in writing' advice often does not
  engage with the employer-side response patterns"; Patio11 voice
  catches this dynamic; boundary `tech-career` and `legal-disputes`.
- **Trigger.** Founder is moonlighting on a side-project that has
  any plausible relationship to the employer's actual or anticipated
  business AND is reasoning about asking for written carve-out from
  HR / Legal AND has not modeled the employer-side response (refuse,
  treat-as-evidence, accelerate-enforcement, force-leap-timing) AND
  has not consulted employment-law counsel on the protective steps
  to take BEFORE making the request.
- **Failure-mode.** Founder requests written carve-out from HR;
  request triggers internal review; employer asserts side-project
  competes with anticipated business; founder is placed on PIP /
  asked to choose between side-project and W-2; founder forced into
  premature leap with insufficient runway; OR continues side-project
  covertly with hardened employer-position on later IP-trailing
  claim at exit.
- **Recovery-move.** Self-directed first: document the side-project's
  pre-employment scope and any prior-art carve-outs in writing
  BEFORE making any employer request; use CA Labor Code §2870
  statutory carve-out language where applicable (CA only — "the
  invention does not relate to the employer's business or the
  employer's actual or demonstrably anticipated research or
  development"). **D11 high-stakes pocket — consult an employment-
  law attorney** in the founder's state of employment BEFORE making
  any written carve-out request to the employer; the attorney can
  often negotiate a narrower acknowledgment-without-disclosure that
  achieves the protective goal without triggering the disclosure-
  consequence.

### F8.3 Roth-conversion window on low-income leap year almost universally missed

- **Statement.** "I'll handle taxes when income returns." The
  framing's day-job-fallback focus under-engages with the *Roth-
  conversion-window on low-income years* — a year of reduced or
  zero W-2 income from the leap creates a uniquely-high-leverage
  Roth-conversion opportunity: traditional-401(k) or traditional-IRA
  balances can be converted to Roth at the founder's low marginal
  rate (potentially 0%-12% federal bracket if the year is genuinely
  zero-income), locking in the rate forever.
- **Source-evidence.** `framings.md` F8 third Excludes bullet — "the
  framing under-engages with the Roth-conversion-window on low-
  income years — this is almost universally missed by founders who
  don't have integrated personal-finance and entrepreneurship
  advisors"; boundary `personal-finance` D7.
- **Trigger.** Founder has just leaped from W-2 AND is in a leap-
  year with significantly reduced household income (founder zero-
  income, spousal-income reduced or zero) AND has $50k+ in
  traditional-401(k) and / or traditional-IRA balances AND has not
  consulted a CPA / fee-only-CFP on the Roth-conversion arithmetic
  for the current tax year (deadline: Dec 31 of the leap year).
- **Failure-mode.** Founder skips the conversion in the leap year;
  startup succeeds at year 5 with $500k+ income; founder is now in
  the 32-35% marginal bracket; the $50-200k traditional balance
  that could have been Roth-converted at 0-12% in the leap year
  will be withdrawn at 22-32% in retirement; net lifetime tax cost
  of $15-60k per $100k of traditional balance not converted.
- **Recovery-move.** Cross-domain edge to `personal-finance` D7
  Mechanism E: this is a uniformly-Mechanism-E-gated decision in
  `personal-finance` — consult a fee-only CFP or CPA on the Roth-
  conversion arithmetic for the leap year BEFORE Dec 31; specifically
  request analysis of (a) federal + state marginal rate at conversion
  vs projected retirement-rate, (b) IRMAA-bracket impact on Medicare
  premiums if conversion crosses thresholds, (c) ACA-subsidy
  interaction if on Marketplace insurance, (d) pro-rata-rule
  application if any after-tax IRA basis exists. Self-directed
  baseline: The Finance Buff on Roth-conversion math; Bogleheads
  wiki on conversion mechanics.

### F8.4 MRR-threshold heuristic ignores growth-slope as the load-bearing variable

- **Statement.** "Quit when MRR covers 50% of expenses" / "quit at
  $10k MRR" / "quit at $30k MRR." The framing's heuristics-treated-
  as-rules cause founders to either leap too early (chasing
  absolute-MRR without slope signal) or stay too long (waiting for
  an MRR threshold a stagnant business will never reach). The load-
  bearing variable is not the absolute MRR level but the *growth
  slope change a full-time commitment would produce*.
- **Source-evidence.** `framings.md` F8 fourth Excludes bullet —
  "'Quit when MRR covers 50% of expenses' / 'quit at $10k MRR' /
  'quit at $30k MRR' heuristics are under-engaged with growth-slope —
  the load-bearing variable is not the absolute MRR level but the
  growth slope change a full-time commitment would produce"; Indie
  Hackers voice tends toward absolute-MRR; YC playbook voice tends
  toward growth-slope.
- **Trigger.** Founder is using an MRR-threshold heuristic for leap-
  timing decision AND has not measured the growth-slope of the side-
  project for at least 6 months AND has not estimated the slope-
  change a full-time commitment would produce AND is in either of
  two scenarios: (a) low-MRR + high-slope, (b) high-MRR + low-slope.
- **Failure-mode (case a).** $4k MRR with 25%/month growth at 15
  hrs/week; founder stays in day-job waiting for the $30k threshold;
  growth-slope declines because founder bandwidth caps the growth-
  experiment velocity; the slope-change opportunity is missed; the
  business plateaus before reaching the threshold.
- **Failure-mode (case b).** $25k MRR with 2%/month growth at 15
  hrs/week; founder leaps thinking $25k is "close to the threshold";
  full-time commitment does NOT change the growth-slope (the
  product / market / channel is already saturated at current
  approach); founder is now full-time at $25k MRR with no scaling
  path; household-burn exceeds business-income; forced retreat to
  W-2 with reputational cost.
- **Recovery-move.** Self-directed: measure 6 months of growth-slope
  on the side-project; estimate explicitly what changes when full-
  time (specific experiments / channels / customer-interviews enabled
  by 5x time-investment); model the slope-change as the leap-
  signal, not the absolute MRR. Self-directed baseline: First Round
  Review on side-project-to-full-time transitions; YC Library on
  growth-slope as the load-bearing signal.

### F8.5 COBRA-to-Marketplace transition silently constrained on founder-leap

- **Statement.** "I'll figure out health insurance after I leap."
  The framing under-engages with the *health-insurance bridge
  decision* — loss of employer coverage on leap triggers a HIPAA
  Special-Enrollment-Period; COBRA 18 months at full-cost-plus-2%
  is the default but materially more expensive than Marketplace
  coverage; the Marketplace subsidy-cliff timing interacts with
  founder's projected leap-year income; transition mistakes can
  leave gaps with $20k+ tail-risk on a single medical event.
- **Source-evidence.** `framings.md` F8 mental-model framing on
  COBRA bridge mechanics and ACA SEP-on-loss-of-coverage; cross-
  domain edge to `health-insurance` (founder COBRA-to-Marketplace
  transition is the canonical case in the `health-insurance` domain).
- **Trigger.** Founder is within 60 days of W-2 termination event
  (leap, RIF, voluntary-separation) AND has not modeled the
  Marketplace subsidy vs COBRA cost-comparison for the leap-year
  household-income projection AND has dependents / preexisting
  conditions that constrain plan-network choice AND has not
  enrolled in continuation coverage by Day 60.
- **Failure-mode.** Founder leaps at month 0; declines COBRA at
  month 1 thinking Marketplace will be cheaper; HIPAA SEP window
  closes at Day 60; family experiences medical event at month 3
  uninsured; $30-100k+ out-of-pocket cost; future Marketplace
  enrollment limited to Open Enrollment (Nov-Jan) with coverage
  effective January 1 of following year; the gap is 9 months.
- **Recovery-move.** Cross-domain edge to `health-insurance` — this
  decision is uniformly-Mechanism-E-gated in the `health-insurance`
  domain: consult a health-insurance broker (fee-paid by insurer,
  no cost to founder) OR fee-only health-insurance advisor BEFORE
  the leap; specifically request COBRA-vs-Marketplace-vs-spousal
  comparison with founder's projected leap-year household income
  and the subsidy-cliff analysis. Self-directed baseline:
  healthcare.gov subsidy calculator; The Finance Buff on COBRA-vs-
  Marketplace decision; state-Marketplace-exchange guidance.

---

## 9. Product-led-growth / PLG framing (F9)

### F9.1 PLG-only motion caps at SMB / individual-power-user segment

- **Statement.** "Build a great product and the funnel will convert
  customers self-serve." The framing's product-as-funnel reflex
  assumes the buying decision is *individual or small-team* (sign
  up, try, pay without procurement involvement), but mid-market and
  enterprise sales fundamentally require human navigation of
  procurement, security review (SOC 2, SIG questionnaires, vendor-
  onboarding), MSA / DPA negotiation, and multi-stakeholder buy-in.
  PLG-only motions cap at SMB / individual-power-user segment and
  routinely leave 5-10x revenue on the table by not building sales-
  led capacity for larger deals.
- **Source-evidence.** `framings.md` F9 first Excludes bullet — "the
  product-as-funnel reflex assumes the buying decision is individual
  or small-team — PLG-only motions cap at the SMB / individual-
  power-user segment and routinely leave 5-10x revenue on the table";
  opposes F10 (sales-led-growth) on D9 / D10.
- **Trigger.** Founder is at $1-5M ARR on pure-PLG motion AND has
  identified that 30%+ of inbound interest is from companies with
  500+ employees AND has not built sales-overlay capacity (no AE,
  no security-questionnaire capability, no SOC 2 process) AND is
  deferring enterprise-sales investment on "we're a PLG company"
  grounds.
- **Failure-mode.** Inbound enterprise prospects ($50-200k ACV) are
  bounced into the self-serve $10/month flow; prospects churn back
  to competitors with sales-overlay capacity; founder forgoes $2-5M
  ARR over 18 months from missed enterprise expansion; competitor
  consolidates the enterprise segment; the PLG-purist position
  becomes a permanent ceiling.
- **Recovery-move.** Self-directed: hybridize the motion at the
  $1-3M ARR threshold — PLG remains the top-of-funnel for SMB but
  add light-touch sales for enterprise prospects (first AE at $5M
  ARR, SOC 2 Type I process at $2M ARR, security-questionnaire
  templates at $3M ARR). Self-directed baseline: Lenny Newsletter
  on PLG-with-sales-overlay (Notion-for-Enterprise, Atlassian
  Enterprise patterns); OpenView Partners benchmarks on hybrid
  motions; First Round Review on first-AE-at-PLG-company.

### F9.2 Entry-tier price systematically set 2-5x below willingness-to-pay

- **Statement.** "Set Pro at $10/month / Team at $5/seat — keep
  conversion friction low." The framing's "low entry-tier price to
  remove friction" reflex *systematically under-prices early* —
  founders set low prices because the freemium-to-paid conversion
  would suffer at higher prices, then can never raise prices on
  early cohorts without grandfathering complexity. Patrick Campbell
  / ProfitWell research repeatedly shows PLG companies under-price
  entry tiers by 2-5x relative to customer willingness-to-pay.
- **Source-evidence.** `framings.md` F9 second Excludes bullet — "the
  framing's 'low entry-tier price to remove friction' reflex
  systematically under-prices early — Patrick Campbell / ProfitWell
  research shows PLG companies under-price entry tiers by 2-5x";
  boundary `personal-finance` on pricing-psychology.
- **Trigger.** Founder is launching PLG product AND has set entry
  tier at $5-15/month / seat WITHOUT willingness-to-pay research
  (price-sensitivity surveys, Van Westendorp PSM, conjoint analysis,
  competitive-pricing analysis) AND is reasoning from "low price
  removes friction" intuition rather than data AND has not modeled
  the lifetime-revenue impact of higher entry-pricing with lower
  conversion-rate.
- **Failure-mode.** Founder launches at $10/month Pro tier; converts
  3% of free users; 18 months later realizes Pro should be $40-50
  based on willingness-to-pay analysis but can't raise on existing
  cohort without grandfathering complexity and churn-risk; new-
  cohort price increase is implemented at month 18 but 18 months
  of lower-priced contracts compound to $500k-$2M of forgone
  revenue.
- **Recovery-move.** Self-directed: run a Van Westendorp Price
  Sensitivity Meter or equivalent willingness-to-pay survey with 30+
  target customers BEFORE setting entry-tier pricing; set entry
  tier at the upper edge of the indifference-price-range; accept
  the lower conversion-rate as the price for higher lifetime-
  revenue. Self-directed baseline: ProfitWell / Patrick Campbell
  pricing research; Lenny Newsletter on PLG pricing iterations
  (Notion / Linear pricing history case studies).

### F9.3 PLG-canon companies are survivorship-bias examples

- **Statement.** "Slack / Notion / Figma / Linear / Atlassian
  succeeded with PLG — we can too." The framing's PLG-canon examples
  are *survivorship bias* — rarely surfaces the 100s of failed PLG
  attempts in adjacent categories (project management, CRM,
  knowledge management, design tools) where activation-rate or
  conversion-rate fundamentals didn't work; PLG works in *specific
  category-product fits* and is not a universal motion.
- **Source-evidence.** `framings.md` F9 third Excludes bullet — "PLG-
  canon companies (Slack, Notion, Figma, Linear, Atlassian) are
  survivorship bias examples — the framing rarely surfaces the 100s
  of failed PLG attempts"; PLG fails categorically for products
  requiring data integration, multi-stakeholder configuration, or
  post-sale onboarding services.
- **Trigger.** Founder is building in a category that requires any
  of: (a) data-integration with customer systems (most enterprise
  apps), (b) multi-stakeholder configuration (security / IT /
  compliance approvals), (c) post-sale onboarding services
  (training, migration, integration consulting), (d) high-context
  decision-making (purchasing on behalf of others) AND is forcing
  PLG motion on PLG-canon-aspiration grounds.
- **Failure-mode.** Founder builds enterprise data-platform with
  self-serve signup; signup-to-activation rate is 2% (vs PLG-canon
  25-50%) because integration-setup requires 4 hours of customer
  technical work; conversion rate is 0.3% (vs PLG-canon 1-5%);
  founder spends 18 months optimizing the funnel before recognizing
  the category fundamentally needs sales-overlay; net waste $1-3M
  in engineering / PM investment on the unwound PLG motion.
- **Recovery-move.** Self-directed: identify the structural category
  fit BEFORE committing to motion — does the product naturally fit
  PLG (consumer / small-team / individual-power-user / minutes-to-
  value) or does it require sales-overlay (enterprise / data-
  integration / multi-stakeholder)? Look at *failed* PLG attempts
  in the adjacent category as the calibration set, not the
  canon-success companies. Self-directed baseline: OpenView
  Partners benchmark on PLG fit-criteria; Lenny Newsletter on
  PLG-vs-sales-led category-fit decisions.

### F9.4 Instrumentation-and-experimentation infrastructure is the invisible cost

- **Statement.** "We'll build the PLG funnel and iterate on
  activation." The framing's iteration-on-funnel reflex under-prices
  the *invisible engineering cost* of PLG — building a proper
  experimentation platform (Amplitude / Mixpanel / Segment / dbt /
  data warehouse / experiment framework / feature-flag system /
  reverse-ETL) easily costs 1-2 senior engineers full-time for 6-12
  months at pre-Series-A scale.
- **Source-evidence.** `framings.md` F9 fourth Excludes bullet —
  "'Instrumentation and experimentation infrastructure' is the
  invisible engineering cost of PLG that the framing under-prices —
  founders starting PLG without this infrastructure run blind on
  activation experiments"; Lenny Newsletter / Reforge voices catch
  this; boundary `tech-career` on data-eng hiring sequence.
- **Trigger.** Founder is launching PLG motion AND has not built or
  invested in instrumentation infrastructure (no Amplitude /
  Mixpanel, no data warehouse, no experiment framework, no feature-
  flag system) AND is planning to iterate on activation / conversion
  metrics with intuition-driven A/B-testing.
- **Failure-mode.** Founder runs 30 product-experiments over 12
  months without proper instrumentation; cannot measure true impact
  (treatment-effect confounded by seasonality, cohort-effects,
  selection bias); 60% of experiments are wrong-direction (founder
  doesn't realize because measurement is broken); the iteration
  velocity is theatre rather than learning; product fails to find
  PLG-funnel-fit despite engineering hours invested.
- **Recovery-move.** Self-directed: budget 1-2 senior data-engineers
  for 6-12 months of infrastructure build BEFORE the PLG iteration
  phase OR adopt a managed-experimentation platform (Statsig /
  Eppo / GrowthBook) at $30-100k/year that compresses the
  infrastructure cost; expect $200-400k of total infrastructure
  investment before PLG-iteration produces reliable signal. Self-
  directed baseline: Reforge on growth-experimentation
  infrastructure; Lenny Newsletter on data-stack-for-PLG-companies.

### F9.5 Activation rate optimization can mask product-fundamental issues

- **Statement.** "We need to optimize activation; the funnel will
  convert once activation is up." The framing's activation-rate
  optimization reflex can mask product-fundamental issues — a
  product with weak retention or weak willingness-to-pay can show
  activation-rate improvements that don't translate to revenue
  because the activated users still churn or refuse to convert at
  retention-critical moments.
- **Source-evidence.** Lenny Newsletter / Reforge growth-loop voices
  on the activation-rate metric trap; Patrick Campbell / ProfitWell
  on the retention-vs-activation prioritization; PLG literature on
  the "value-delivered" metric distinction.
- **Trigger.** Founder is investing heavily in activation-rate
  optimization (onboarding, UX, first-session experience) AND has
  6-month retention < 30% (a structural retention problem) AND has
  not investigated whether the activation-rate-optimization gains
  are translating to retained-and-paying users (the "north-star
  metric" calibration).
- **Failure-mode.** Founder doubles activation rate from 15% to 30%
  over 6 months; retention rate stays flat at 25% 6-month; revenue
  per visitor barely changes because the additional activated users
  churn before paying; founder spends another 6 months convinced
  the next funnel-optimization will unlock revenue; the real
  problem is product-retention which requires a different intervention.
- **Recovery-move.** Self-directed: separate activation-rate from
  retention-rate from revenue-per-cohort as distinct optimization
  targets; if retention < 30%, prioritize retention work BEFORE
  activation work because activation-without-retention is wasted
  effort. Self-directed baseline: Reforge on retention vs activation
  prioritization; Lenny Newsletter on north-star metric selection
  for PLG companies.

---

## 10. Sales-led-growth / enterprise framing (F10)

### F10.1 Enterprise-sales playbook requires Series A capital bootstrap cannot afford

- **Statement.** "Build the enterprise sales motion with AE / CSM /
  SE team." The framing's enterprise-sales playbook is *capital-
  intensive in a way bootstrap fundamentally cannot afford* —
  building an AE-CSM-SE team requires Series A capital, and the
  framing routinely *implicitly assumes* the company has raised.
  Bootstrap founders pushing for enterprise customers without
  sales-team capital face the founder-as-perpetual-salesperson trap
  (founder time as primary salesperson permanently caps revenue
  growth at founder bandwidth).
- **Source-evidence.** `framings.md` F10 first Excludes bullet — "the
  framing's enterprise-sales playbook is capital-intensive in a way
  bootstrap fundamentally cannot afford"; opposes F2 (bootstrap
  default-alive) on D9 / D10.
- **Trigger.** Founder is bootstrapping AND targeting enterprise
  ACV ($50k+) deals AND has not raised AND is committing the
  founder's primary time to enterprise sales process (procurement,
  security, MSA, multi-stakeholder buy-in) AND has not modeled the
  founder-bandwidth ceiling explicitly.
- **Failure-mode.** Bootstrap founder spends 70% of bandwidth on
  3 enterprise deals at $80k ACV over 18 months ($240k total
  revenue); meanwhile SMB / mid-market opportunities are unhandled;
  the bootstrap-bandwidth-ceiling caps revenue growth at $300-500k
  ARR; competitor with Series A capital builds the enterprise
  motion and reaches $3-5M ARR over the same period.
- **Recovery-move.** Self-directed: distinguish *bootstrap-compatible
  sales motions* (founder-led + 1 SDR + inbound, ACV $5-30k) from
  *Series-A-required motions* (AE-team, ACV $50-200k+); for
  bootstrap path, optimize for the lower-ACV-higher-volume motion
  even if individual deals look smaller. **D5 high-stakes pocket
  — consult a startup attorney** ONLY if pivoting to raise Series A
  to fund the enterprise motion; the priced-round-decision is the
  load-bearing one. Self-directed baseline: Founder Collective on
  capital-efficient sales motions; Tomasz Tunguz on revenue-per-
  employee benchmarks across motions.

### F10.2 Founder-as-AE early closes don't transfer to first hired AE

- **Statement.** "Hire the first AE only after the founder has
  closed 10+ deals to validate the playbook." The framing's "you
  have a playbook" reflex overstates how often early founder-led-
  sales is *actually* a transferable playbook — technical founders
  without sales background routinely close early deals through
  technical-credibility and customer-love rather than reproducible
  sales process; then cannot hire someone to replicate because the
  playbook was never legible.
- **Source-evidence.** `framings.md` F10 second Excludes bullet —
  "the framing under-engages with the founder-as-AE failure mode —
  technical founders without sales background routinely close early
  deals through technical-credibility and customer-love rather than
  through reproducible sales process"; boundary `tech-career` on
  sales-management hiring asymmetry.
- **Trigger.** Founder has closed 10+ deals over 18 months AND has
  no documented sales-playbook (no qualification framework, no
  discovery-questions catalog, no objection-handling library, no
  ICP definition with explicit boundary conditions) AND is hiring
  the first AE on the assumption that the AE will replicate the
  founder's success AND has not validated playbook-transferability
  through any structured handoff (shadowing, recorded calls, co-
  sell ramp).
- **Failure-mode.** First AE hired at $200k OTE; AE pipeline 30%
  of founder's pipeline at month 6; AE wins 1 deal in 6 months;
  founder concludes "the AE is wrong" rather than "the playbook
  isn't transferable"; AE departs at month 9; founder hires a
  second AE who underperforms similarly; the company has spent
  $400k on sales hires that don't replicate the founder's results.
- **Recovery-move.** Self-directed: BEFORE hiring the first AE,
  document the playbook explicitly — record 10 founder sales calls
  with transcription; codify qualification questions, ICP boundaries,
  discovery framework, demo flow, objection handling, MEDDIC /
  MEDDPICC scoring; have a sales-experienced advisor review the
  playbook for transferability; structure the first AE's first
  90 days as shadow-and-co-sell rather than independent ownership.
  Self-directed baseline: SaaStr on founder-to-first-AE transition;
  Tomasz Tunguz on the predictable failure modes; First Round
  Review on first-AE hiring.

### F10.3 Discount-creep destroys list-price-anchor without deal-desk discipline

- **Statement.** "Set list price at 1.3-1.5x desired-realized; AEs
  will negotiate down." The framing's list-price-strategy is a
  *good discounting hygiene* but under-engages with the *discount-
  creep* dynamic: AEs paid on quota have implicit incentive to
  discount to close, and without strong deal-desk / pricing-
  committee discipline, list price erodes 30-50% within 2 years as
  AEs build muscle around what they can give away.
- **Source-evidence.** `framings.md` F10 third Excludes bullet —
  "the framing under-engages with the discount-creep dynamic — AEs
  paid on quota have implicit incentive to discount to close, and
  without strong deal-desk / pricing-committee discipline, list
  price erodes 30-50% within 2 years"; Tomasz Tunguz / SaaStr voices
  catch this.
- **Trigger.** Company has 3+ AEs hitting quota AND no formal deal-
  desk process (no approval threshold for discounts above X%, no
  pricing-committee, no quarterly discount-review) AND has not
  measured discount-creep across cohorts AND is treating "AEs hit
  their quota" as evidence the pricing-system is working.
- **Failure-mode.** Year 1 average realized-price is 75% of list;
  year 2 is 65%; year 3 is 55%; ARR appears to grow on volume but
  price-per-deal has eroded materially; renewal cohort at year 3
  faces difficult conversation when renewal price is set at the
  expired-deal price (which is now 40% above market); churn
  increases at renewal; the discount-creep is discovered at the
  year-3 board deck.
- **Recovery-move.** Self-directed: implement deal-desk process at
  the 2nd-or-3rd AE hire — discounts above 15% require VP-Sales or
  CFO approval; discounts above 30% require founder approval; track
  discount distribution by AE and quarter; review price-realization
  at quarterly business reviews. **D5 high-stakes pocket — consult
  a CFO advisor / fractional-CFO** if discount-creep is already
  visible in year-2 data and the renewal cohort is approaching.
  Self-directed baseline: SaaStr on deal-desk implementation; Tomasz
  Tunguz quarterly SaaS metrics benchmarks.

### F10.4 SaaS-metrics calculations frequently encode bad assumptions

- **Statement.** "We track CAC payback, LTV/CAC, Magic Number, and
  NRR." The framing's "use these metrics" reflex understates how
  easy it is to deceive yourself with metrics that look correct but
  encode bad assumptions: CAC underweights founder-time-as-S&M
  (founder spending 20 hrs/week on sales-and-marketing without W-2
  compensation depresses CAC artificially); LTV based on first-12-
  months data extrapolated to "lifetime" misses the actual churn
  curve; NRR including up-sells mixes good-product-driven expansion
  with sales-discount-driven expansion.
- **Source-evidence.** `framings.md` F10 fourth Excludes bullet —
  "SaaS-metrics dogma (CAC payback, LTV/CAC, Magic Number) assumes
  the metric calculations are clean — but most early-stage
  companies' metric calculations are materially wrong"; boundary
  `data:analyze`.
- **Trigger.** Company is reporting SaaS metrics to investors / board
  AND CAC is computed excluding founder-time-as-S&M AND LTV is
  extrapolated from < 18 months of data AND NRR combines good-
  product expansion and discount-driven expansion in a single number
  AND no quarterly audit of the metric-definitions has been
  performed.
- **Failure-mode.** Founder reports CAC of $5k with LTV of $50k
  (10:1 LTV-to-CAC, "excellent"); the real CAC including founder-
  time is $15k (3.3:1, "marginal"); the LTV based on actual cohort-
  churn-curve is $25k (1.7:1 against real CAC, "poor"); Series B
  investor diligence uncovers the discrepancy 12 months later;
  round terms shift unfavorably or the round collapses.
- **Recovery-move.** Self-directed: include founder-time at fully-
  loaded comp ($300-500k/yr for technical founder) in CAC
  computation; compute LTV from actual cohort churn-curve, not
  extrapolation; separate NRR into expansion-from-product (seat-
  growth, usage-growth) vs expansion-from-discount-recovery; report
  both clean metrics and the "as-investors-will-recompute" metrics
  in board materials. Self-directed baseline: ProfitWell on metric-
  computation discipline; Tomasz Tunguz on the metrics-that-actually-
  matter; SaaStr on board-deck honesty.

### F10.5 MEDDIC discipline applied to wrong stage produces process-theater

- **Statement.** "Apply MEDDIC / MEDDPICC to qualify every deal."
  The framing's MEDDIC discipline reflex is correct at $50k+ ACV
  with multi-stakeholder enterprise buying processes but
  *over-applies* at SMB / mid-market scale where the buying process
  is single-stakeholder and 1-3 month cycle; forcing MEDDIC on
  small-ACV deals creates process-theater that lengthens cycles
  without improving outcomes.
- **Source-evidence.** SaaStr / Tomasz Tunguz / Lenny Newsletter
  voices on sales-process calibration by ACV-and-stakeholder-
  complexity; cross-domain edge to `tech-career` on sales-process
  selection by role-and-stage.
- **Trigger.** Company is selling SMB / mid-market with ACV
  $5-30k AND is applying full MEDDIC framework (Metrics, Economic
  buyer, Decision criteria, Decision process, Identify pain,
  Champion) on every deal AND has 1-3 month sales cycles where
  buying process is genuinely single-stakeholder.
- **Failure-mode.** Sales-cycle inflates from 1 month to 3 months
  due to process-overhead; smaller deals don't generate the
  multi-stakeholder dynamics MEDDIC presumes; AEs spend time
  filling out qualification fields rather than closing; the win-
  rate drops without compensating ACV-increase; the founder
  concludes "we need a better sales process" when the actual
  problem is mis-calibrated process.
- **Recovery-move.** Self-directed: calibrate sales-process
  formality to ACV — for SMB / mid-market ($5-30k), use lighter
  qualification (BANT + Champion); for enterprise ($50k+), use
  full MEDDIC / MEDDPICC; for transactional ($1-5k), use
  self-serve plus light-touch SDR follow-up. Self-directed
  baseline: SaaStr on sales-process calibration by ACV; First
  Round Review on stage-appropriate sales-process selection.

---

## 11. Founder-mode / hands-on-management framing (F11)

### F11.1 Founder-mode rationalizes micro-management when applied pre-PMF

- **Statement.** "Stay in the details — founder-mode is the
  successful pattern." The framing's "founder-mode" reflex *can
  rationalize micro-management* and damage early hires who joined
  expecting autonomy — Brian Chesky's Airbnb example is *successful
  founder-mode after PMF and product DNA* — applying the same
  intensity pre-PMF without stable product DNA can chaotic-ize the
  company and exhaust the team.
- **Source-evidence.** `framings.md` F11 first Excludes bullet —
  "the 'founder-mode' reflex can rationalize micro-management and
  damage early hires who joined expecting autonomy — Brian Chesky's
  Airbnb example is successful founder-mode after the company had
  found PMF and product DNA"; opposes F12 (manager-mode) on D10 / D11.
- **Trigger.** Founder is pre-PMF (no clear repeat-customer-pattern,
  no validated retention curve) AND is applying founder-mode
  intensity (dipping into every detail across product / hiring /
  customer / financial) AND senior early hires are reporting
  bandwidth-consumed-by-founder-interventions OR are departing AND
  founder is citing Brian Chesky / PG essay as justification.
- **Failure-mode.** Senior PM hired at month 6 leaves at month 12
  citing "founder doesn't actually let me make decisions"; senior
  engineer hired at month 8 leaves at month 14 same reason; the
  company is now at month 18 still searching for PMF with no
  scalable hires; founder's defense ("I'm in founder-mode") doesn't
  change the senior-hire churn pattern.
- **Recovery-move.** Self-directed: distinguish founder-mode-pre-PMF
  (founder DOES need to be in product / customer / hiring detail
  because the operating-system-is-being-invented) from founder-mode-
  post-PMF (founder maintains direct-line-of-sight on strategy but
  delegates execution); for pre-PMF, hire fewer senior people and
  more execution-oriented ICs who want to ship-not-decide. Self-
  directed baseline: PG *Founder Mode* essay (full text, not
  summary); First Round Review on early-stage hiring; Brian Chesky
  Airbnb history (with explicit PMF-timing annotation).

### F11.2 Skip-level and direct-line-of-sight stop scaling at ~200 people

- **Statement.** "Maintain skip-level meetings and direct-line-of-
  sight as we scale." The framing's "stay in the details" practice
  *does not scale beyond ~200 person company* without explicit org-
  design support — the founder can dip into every project at 30
  people, can rotate across major projects at 100 people, but
  cannot maintain direct-line-of-sight at 500+ without designating
  "founder-led-projects" vs "manager-led-projects" explicitly.
- **Source-evidence.** `framings.md` F11 second Excludes bullet —
  "'Skip-level meetings' and 'stay in the details' are practices
  that do not scale beyond ~200 person company without explicit
  org-design support — the framing's PG-essay version sidesteps the
  scaling question, which is the actual hard part"; SaaStr / Lemkin
  voices catch this; boundary `tech-career` on engineering-management
  scaling.
- **Trigger.** Company is at 150-300 employees AND founder is
  attempting to maintain founder-mode practices (skip-level on every
  team, founder in every major customer call, founder reviews every
  hire) AND has not designated which projects are founder-led vs
  manager-led AND is experiencing founder-bandwidth exhaustion (15+
  hour days, missed reviews, increasingly-late responses).
- **Failure-mode.** Founder bottleneck caps growth velocity; senior
  hires that joined expecting autonomy leave or disengage; the
  exec-team-reporting structure becomes nominal because the founder
  routes around it; org-chart becomes purely cosmetic; growth-rate
  declines from 100% to 50% to 25% as bandwidth tightens; the
  company stalls at $20-50M ARR with structural founder-bottleneck.
- **Recovery-move.** Self-directed: at the 100-150 employee
  threshold, explicitly designate founder-led-projects (typically
  product DNA, key customer relationships, strategic hires) vs
  manager-led-projects (operations, geographic expansion, function-
  specific scaling); communicate the designation explicitly; allow
  manager-led-projects to be genuinely manager-led without founder
  intervention. Self-directed baseline: SaaStr on $1-10M-to-$100M
  scaling; First Round Review on founder-CEO-at-Series-B-and-beyond;
  *The Manager's Path* by Camille Fournier.

### F11.3 Founder-mode terminology can mask poor CEO performance

- **Statement.** "I'm in founder-mode, that's why I'm not delegating."
  The framing's "founder-mode" terminology carries *implicit founder-
  identity affirmation* that can obscure poor performance — a
  struggling founder can use the framing as self-flattering label
  rather than as analytical framework; critique-from-the-team and
  self-critique are the corrections, but founder-mode rhetoric can
  silence both.
- **Source-evidence.** `framings.md` F11 third Excludes bullet —
  "the framing's 'founder-mode' terminology carries implicit founder-
  identity affirmation that can obscure poor performance — a
  struggling founder rationalizing 'I'm just in founder-mode, that's
  why I'm not delegating' can avoid the harder question of whether
  they're an effective CEO".
- **Trigger.** Founder is citing founder-mode framing AND company
  metrics are deteriorating (revenue growth slowing, senior hire
  churn up, key-customer satisfaction down) AND team feedback
  cycles are blocked or silenced (no 360 reviews, no skip-level
  feedback, no executive coach) AND founder is reflexively framing
  team-critique as "they don't understand founder-mode."
- **Failure-mode.** Year 3: company is at $5M ARR with 18 months of
  flat growth; senior team turnover 40%/year; investors at
  Series B are asking hard questions; founder defends with founder-
  mode-citation rather than addressing performance signals;
  board eventually forces external-CEO recruitment OR founder is
  removed via protective-provisions; the entire intervention happens
  18-24 months later than it should have because founder-mode
  rhetoric blocked earlier self-correction.
- **Recovery-move.** Self-directed: implement 360-review process
  with the senior team annually; engage an executive coach (BetterUp,
  Reboot, individual practitioner) for monthly sessions with explicit
  permission to challenge founder-mode-rhetoric; treat sustained
  team-critique as data, not as evidence the team-doesn't-get-it.
  **D11 high-stakes pocket — consult a startup attorney** if board-
  level conflict is escalating; the protective-provision stack
  determines what removal-paths exist. Self-directed baseline:
  First Round Review on founder-CEO self-assessment; Reboot
  (Jerry Colonna) on CEO-leadership-development.

### F11.4 Board / investor expectations diverge from founder-mode at growth-stage

- **Statement.** "I'll stay founder-mode forever." The framing's
  "founder-mode forever" rhetoric runs into board friction at
  growth stage — investors past Series B typically expect to see
  clear professional-management layer, succession planning, and
  executive bench depth that founder-mode-only org structures lack;
  some founders respond by changing boards (when protective-
  provisions and board composition allow) or accepting the
  management-layer reluctantly.
- **Source-evidence.** `framings.md` F11 fourth Excludes bullet —
  "Founder-mode under-engages with board / investor expectations at
  scale — investors past Series B typically expect to see clear
  professional-management layer, succession planning, and executive
  bench depth"; boundary `legal-disputes` on board governance.
- **Trigger.** Founder is at Series B / C stage with board including
  institutional investors AND is committed to founder-mode-only
  org structure AND has not built executive bench depth (no VPs
  with autonomous decision-making, no documented succession plan
  in case of founder-incapacitation) AND board has raised concerns
  in recent meetings about scaling / management / succession.
- **Failure-mode.** Series C round: lead investor requires
  professional-CEO recruitment as condition of round; founder
  refuses; round collapses or closes at significantly worse terms;
  alternatively founder accepts professional-CEO but the transition
  is acrimonious and founder departs at month 12; the company
  loses 18-24 months of founder-DNA-value during the transition
  upheaval.
- **Recovery-move.** Self-directed: build the management-layer
  *before* board pressure forces it — VP-Eng / VP-Sales / VP-
  Product as autonomous decision-makers by $20-30M ARR; document
  succession plan covering founder-incapacitation scenarios; have
  early conversations with board about founder-CEO trajectory
  vs eventual professional-CEO transition. **D11 high-stakes pocket
  — consult a startup attorney** for protective-provision-stack
  analysis if board conflict is escalating. Self-directed baseline:
  First Round Review on founder-to-professional-CEO transitions
  (Brian Chesky / Patrick Collison case studies).

### F11.5 Inner-circle dependency creates single-point-of-failure on founder

- **Statement.** "I maintain a small inner-circle of trusted ICs."
  The framing's inner-circle / kitchen-cabinet practice creates a
  single-point-of-failure dependency on the founder — when major
  decisions route through informal personal relationships rather
  than formal org-chart authority, founder absence or burnout
  paralyzes decision-making, and the org-chart-as-cosmetic-only
  state cannot continue operating.
- **Source-evidence.** `framings.md` F11 mental-model framing on
  inner-circle / kitchen-cabinet practice; cross-domain edge to
  `tech-career` and `health-insurance` (founder-burnout
  consequences); First Round Review voice on management-system
  design.
- **Trigger.** Founder has structured the company with informal
  inner-circle decision-making (5-8 trusted ICs the founder pulls
  into major decisions regardless of org-chart layer) AND has not
  documented decision-rights formally AND founder has not modeled
  the "founder-incapacitated-for-3-months" scenario AND inner-
  circle members have implicit decision-authority that exceeds
  their formal title.
- **Failure-mode.** Founder takes 3-month medical leave; inner-
  circle members have no formal authority to make decisions in
  their domains; org-chart VPs don't have actual authority
  (founder always overruled them); the company stalls for 3
  months; key customer renewals slip; hiring freezes; the
  founder returns to a materially-weakened company.
- **Recovery-move.** Self-directed: document decision-rights
  formally — which decisions require founder, which require the
  inner-circle, which can be made by org-chart VPs autonomously;
  publish the document internally; conduct quarterly "what if the
  founder is out for 30 days" exercises; if inner-circle members
  have implicit authority exceeding their title, formalize the
  title or remove the implicit authority. Self-directed baseline:
  First Round Review on decision-rights documentation; *Multipliers*
  by Liz Wiseman on delegation discipline.

---

## 12. Manager-mode / scalable-org framing (F12)

### F12.1 VP-of-X-ahead-of-growth over-hires the executive layer pre-PMF

- **Statement.** "Hire VP-of-X ahead of growth needs to build the
  management system." The framing's "hire VP-of-X ahead of growth
  needs" reflex *over-hires the executive layer relative to company
  stage* — VP-Sales hired at $500k ARR before the founder has
  personally validated the sales playbook installs BigCo sales
  process onto a company that doesn't yet have product-market-fit,
  accelerating burn without accelerating revenue.
- **Source-evidence.** `framings.md` F12 first Excludes bullet — "the
  framing's 'hire VP-of-X ahead of growth needs' reflex over-hires
  the executive layer relative to company stage — VP-Sales hired at
  $500k ARR before the founder has personally validated the sales
  playbook installs BigCo sales process onto a company that doesn't
  yet have product-market-fit"; opposes F11 (founder-mode) on D10 /
  D11.
- **Trigger.** Company is pre-PMF (no validated retention curve, no
  clear ICP, no documented sales-playbook) AND is hiring VP-of-X
  (VP Sales, VP Marketing, VP Product) AND is following Salesforce /
  Snowflake hiring-sequence templates calibrated to post-PMF growth-
  stage AND has not validated whether the company-stage matches
  the template's stage.
- **Failure-mode.** $500k ARR pre-PMF company hires VP Sales at
  $300k base + $200k OTE; VP Sales installs MEDDIC / Salesforce /
  enterprise-process from previous-BigCo experience; the early
  product / market / customer-context doesn't support the BigCo
  process; sales cycle inflates; founder-team conflict escalates;
  VP Sales departs at month 12; company has burned $400k on the
  hire + 6 months of leadership-distraction + lost the founder-led-
  sales velocity.
- **Recovery-move.** Self-directed: stage-match hiring template to
  company stage — pre-PMF, hire scrappy founding-team members and
  IC senior-individual-contributors, NOT VP-of-X; post-PMF + $2-3M
  ARR, hire VP-of-X who has explicit early-stage-prior-experience
  (NOT just BigCo-prior-experience). Validate "do you understand
  resource-constraint" in interview before hiring. Self-directed
  baseline: First Round Review on stage-appropriate hiring; SaaStr
  on VP-Sales hiring at the right ARR threshold.

### F12.2 BigCo-experience valuable on average, highly individual-dependent

- **Statement.** "Hire from Google / Facebook / Stripe — BigCo
  experience is valuable at startup." The framing's BigCo-hiring
  reflex obscures the *calibration question* — *which* BigCo
  person, with *what* prior startup adjacency, *for what* role-at-
  stage. The hiring-error cost is severe: a wrong VP hire at growth
  stage can set the company back 18-24 months on the function they
  ran.
- **Source-evidence.** `framings.md` F12 second Excludes bullet —
  "'BigCo experience is valuable at startup' is true on average but
  highly individual-dependent — the distribution of BigCo-experienced
  executives includes a substantial fraction whose effectiveness is
  inseparable from BigCo infrastructure"; boundary `tech-career` on
  senior-leader hiring.
- **Trigger.** Company is hiring VP-of-X AND filtering candidates
  primarily on "where did they work" (Google / FB / Stripe / Snowflake)
  AND is NOT explicitly assessing the candidate's prior-startup-
  adjacency (have they been at a < 100-person company; have they
  led a function with < 5 reports; have they made resource-
  constrained trade-offs) AND has not done structured reference-
  checks on "how did they handle a resource-constrained moment".
- **Failure-mode.** VP-Eng hired from Google L7 background; expects
  the recruiting pipeline / data-platform / planning-system / IC-
  ladder that BigCo provides; resists building these from scratch
  ("that's not my job"); engineering velocity drops 40% as the
  org-design overhead consumes bandwidth; the hire is acknowledged
  as wrong 12-18 months later; company sets back 18-24 months on
  the engineering-org-design.
- **Recovery-move.** Self-directed: filter executive candidates
  primarily on prior-startup-adjacency, not on BigCo brand — at
  least 2 of the candidate's prior 4 roles should be at sub-200-
  person companies; structured reference-checks should specifically
  probe "how did they handle a resource-constrained moment";
  founder-led final-round interviews should test for the
  resource-constraint mindset. Self-directed baseline: First Round
  Review on executive hiring; Reforge on the "BigCo experience
  startup adjacency" assessment.

### F12.3 OKR / V2MOM / EOS / 4DX implementations are commonly cargo-culted

- **Statement.** "Implement OKRs to align the organization." The
  framing's "use a framework" reflex under-prices the *discipline-
  vs-artifact* distinction — founders install the framework's
  artifacts (OKR documents, quarterly planning meetings, scorecards)
  without the underlying discipline (writing genuine objectives,
  holding teams accountable to outcomes vs activities, pruning
  low-impact work). The framework becomes process-theater.
- **Source-evidence.** `framings.md` F12 third Excludes bullet —
  "'Operating system' implementations (OKRs, V2MOM, EOS, 4DX) are
  cargo-culted with high frequency — founders install the artifacts
  without the underlying discipline. The framework becomes process-
  theater"; First Round Review voice catches this; the consultant-
  voice version often doesn't.
- **Trigger.** Company is implementing OKRs / V2MOM / EOS / 4DX AND
  has 80% of quarterly OKRs being marked "complete" each quarter
  (a discipline-failure signal — well-written OKRs should be 60-
  70% achievement at the stretch level) AND is treating
  framework-completion as evidence of framework-success AND has
  not appointed an explicit framework-owner / chief-of-staff with
  accountability for discipline.
- **Failure-mode.** Quarterly OKR sessions consume 1 week of senior
  team time per quarter; the OKRs themselves are activity-not-
  outcome ("ship feature X" not "increase metric Y by Z%"); team
  reports 90% completion every quarter; meanwhile actual business
  metrics are stagnant; the founder concludes "OKRs don't work"
  when the framework was never really in place.
- **Recovery-move.** Self-directed: appoint an explicit framework-
  owner (chief-of-staff, head-of-operations, COO at scale) with
  accountability for discipline; require OKRs to be outcome-based
  (metric-with-target) not activity-based; require 60-70%
  achievement at stretch level (not 90%+ which indicates non-
  stretch); review framework health quarterly. Self-directed
  baseline: First Round Review on OKR discipline; *Measure What
  Matters* by John Doerr; Lattice / Workboard implementation case
  studies.

### F12.4 Founder's constitutional capacity-to-delegate often the bottleneck

- **Statement.** "Hire strong executives and the company will
  scale." The framing's "build the management system" advice
  without addressing the founder's own behavioral pattern produces
  an executive layer that the founder chronically undermines
  through second-guessing, skip-level interventions, and decision-
  reversal; many founder-CEOs are *constitutionally unable* to
  genuinely let go of decisions even after hiring strong executives.
- **Source-evidence.** `framings.md` F12 fourth Excludes bullet —
  "framing under-engages with the founder's own capacity-to-
  delegate — many founder-CEOs are constitutionally unable to
  genuinely let go of decisions even after hiring strong
  executives"; executive-coaching is sometimes the load-bearing
  intervention here, not structural-org-redesign; boundary `tech-
  career` on individual-effectiveness work.
- **Trigger.** Founder has hired strong VPs but is exhibiting one
  or more of: routinely overruling VP-decisions; reversing decisions
  after VP commits to direction; routing decisions around VPs to
  direct-reports; expressing frustration about VPs "not getting it"
  while continuing to undermine them; cycling through multiple VPs
  in the same role.
- **Failure-mode.** Year 3: company has had 3 VP Sales in 18
  months; each was a "good hire on paper" but departed citing
  founder-undermines-decisions; senior team morale is degraded;
  external recruiting reputation suffers; the company is structurally
  unable to retain the executive layer the manager-mode framing
  requires.
- **Recovery-move.** Self-directed: engage an executive coach (Reboot
  / individual practitioner) with explicit focus on delegation-
  capacity AND structured feedback from VPs about specific
  delegation-failure-patterns; consider whether the founder is
  better-suited to a CTO / Chief-Product role with a hired CEO
  rather than CEO seat with constitutional-delegation-block. **D11
  high-stakes pocket — consult a startup attorney** for
  founder-CEO-transition mechanics if the conclusion is to hire
  external CEO. Self-directed baseline: Reboot (Jerry Colonna) on
  founder-CEO-self-work; *The Hard Thing About Hard Things* on
  delegation-discipline.

### F12.5 Hiring scorecard discipline degrades to bias-laundering without rigor

- **Statement.** "Use hiring scorecards and structured interviews
  to remove founder-personal-judgment as the hiring bottleneck."
  The framing's hiring-scorecard reflex assumes the scorecard is
  rigorously calibrated; in practice scorecards drift toward
  bias-laundering (interviewers vote candidate-against-scorecard but
  the calibration of the scorecard is itself biased by recent
  hires' performance, founder preferences, BigCo-template
  importation); the framework becomes evidence-for-conclusion-
  already-reached.
- **Source-evidence.** First Round Review on hiring-scorecard
  discipline; cross-domain edge to `tech-career` on hiring-process
  design; Lenny Newsletter on hiring-rubric calibration.
- **Trigger.** Company is using hiring scorecards AND no quarterly
  audit of scorecard-vs-performance is performed AND scorecard
  ratings show < 10% disagreement across interviewers (a
  calibration-failure signal — well-calibrated scorecards should
  show 30-40% inter-rater disagreement) AND the founder is
  reflexively trusting scorecard outputs as bias-removed.
- **Failure-mode.** Hiring scorecards drift to match founder
  preferences; the framework becomes pseudo-objective vehicle for
  preference-bias; senior hires reflect founder's cognitive
  homogeneity (similar background, similar style, similar
  blindspots); the company misses the diverse-perspective hiring
  the framework was supposed to enable; 18-month senior-team
  homogenization undermines decision-quality on hard problems.
- **Recovery-move.** Self-directed: audit scorecard-vs-performance
  quarterly (do candidates rated 4/5 actually outperform 3/5
  candidates 2 years later?); require quarterly calibration
  sessions with explicit debiasing review; consider blind-resume
  + structured-work-sample for initial filtering; track hire-
  outcome metrics by interviewer to identify miscalibrated
  raters. Self-directed baseline: First Round Review on hiring-
  scorecard discipline; *Work Rules!* by Laszlo Bock on Google's
  hiring-calibration practices.

---

## 13. Optionality-preservation / multiple-paths framing (F13)

### F13.1 Permanent optionality is indistinguishable from inaction

- **Statement.** "Preserve optionality — never close a door." The
  framing's "preserve optionality" reflex can rationalize *failure
  to commit* — the founder who never quits the day job, never
  forms the LLC, never issues SAFEs, and never hires the first
  employee is preserving optionality at the cost of never actually
  building the company. Optionality is valuable only when eventually
  exercised; permanent optionality is indistinguishable from inaction.
- **Source-evidence.** `framings.md` F13 first Excludes bullet — "the
  'preserve optionality' reflex can rationalize failure to commit —
  the founder who never quits the day job, never forms the LLC,
  never issues SAFEs, and never hires the first employee is
  preserving optionality at the cost of never actually building
  the company"; opposes F14 (conviction-commitment).
- **Trigger.** Founder has been "exploring" for 12+ months without
  any irreversible commitment (no LLC formation, no co-founder
  agreement, no first customer revenue contract, no full-time
  commitment, no IP-carve-out request to employer) AND is reasoning
  from optionality-preservation framing AND has not identified
  what *would* trigger commitment.
- **Failure-mode.** Year 3: founder has been "exploring" 3 ideas for
  36 months total; no idea has reached the commitment threshold;
  the founder's career-clock has advanced 3 years; the day-job
  trajectory has continued (now 3 years more golden-handcuffs);
  the optionality-preservation has functionally been a no-decision-
  is-a-decision pattern producing zero startup-progress.
- **Recovery-move.** Self-directed: name the commitment-trigger
  explicitly — "I will form the LLC when MRR reaches $1k" / "I will
  quit the day job at $20k MRR with 6 months of growth" / "I will
  raise capital after 10 paying customers." Optionality preservation
  is fine; permanent optionality is failure to commit. If 12+ months
  pass without commitment AND the trigger is not crossed, re-examine
  whether the trigger is calibrated correctly or whether the founder
  is using "preserve optionality" as cover for indecision. Self-
  directed baseline: Patio11 essays on "calling a wave of fans does
  not produce $4MRR"; YC playbook on "you have to commit at some
  point."

### F13.2 Document-everything reflex blocked by interpersonal friction

- **Statement.** "Document everything in writing — co-founder
  agreements, IP-carve-outs, role clarity." The framing's "document
  everything" reflex is *correct discipline* but routinely *under-
  practiced because of interpersonal friction* — co-founders pushing
  for written operating agreements come across as untrusting; the
  relationship cost of asking creates pressure to defer.
- **Source-evidence.** `framings.md` F13 second Excludes bullet —
  "'Document everything in writing' is correct discipline but
  routinely under-practiced because of interpersonal friction —
  co-founders pushing for written agreements can come across as
  untrusting"; Indie Hackers / r/SmallBusiness voices catch the
  interpersonal dynamics; Patio11 voice catches the discipline;
  boundary `legal-disputes`.
- **Trigger.** Co-founders are operating without written agreement
  for 60+ days post-incorporation OR are deferring documentation
  on a major decision (equity split, role-definition, decision-
  rights) AND the deferral is rationalized by relationship-quality
  ("we trust each other," "writing it down feels unnecessary") AND
  has not been raised explicitly with a startup attorney.
- **Failure-mode.** Year 2 co-founder dispute over role / decision-
  rights / equity-allocation; verbal agreement from formation is
  remembered differently by each founder; no written record exists;
  the dispute extends 6-12 months with $50-150k of attorney costs;
  the cap-table dispute discloses to investors at the next round
  and impacts term-sheet quality.
- **Recovery-move.** **D1 high-stakes pocket — consult a startup
  attorney** within 30 days of forming OR within 30 days of any
  material change (new co-founder, role-change, equity-restructure);
  document founder-agreement / equity-allocation / IP-assignment /
  CIIAA / decision-rights / departure-mechanics in writing with
  both founders' signatures. The interpersonal friction of asking
  is materially less than the dispute-friction of not asking.
  Self-directed baseline: Clerky / Stripe Atlas founder-agreement
  templates as starting point, customized by attorney.

### F13.3 Option-value-decay-over-time silently erodes preserved options

- **Statement.** "I'll keep the day-job-fallback / IP-carve-out /
  SAFE-stacking optionality open." The framing under-engages with
  *option-value-decay-over-time* — many "optionality preservation"
  moves preserve options that *also depreciate*: day-job-fallback
  decays at 12-24-month freshness (F8); SAFE-stacking-as-
  postponement accumulates silent dilution; LLC-formation-deferred-
  until-trigger may miss the optimal entity-choice timing
  (state-fee variation, S-corp election window).
- **Source-evidence.** `framings.md` F13 third Excludes bullet —
  "the framing under-engages with option-value-decay-over-time —
  many 'optionality preservation' moves preserve options that also
  depreciate"; calculating option-value-net-of-carrying-cost is the
  load-bearing math the framing rarely surfaces.
- **Trigger.** Founder is preserving multiple options simultaneously
  (day-job + side-project + LLC-formation-deferred + SAFE-stacking)
  AND has not modeled the option-value-decay rate for each option
  AND has not computed the carrying cost of each option (foregone
  salary, accumulated SAFE-dilution, missed S-corp election
  windows, state-tax-cost of late entity-formation).
- **Failure-mode.** Year 3: founder still preserving options;
  day-job-fallback has decayed 60% (12-24-month freshness window
  exceeded); SAFE-stacking has accumulated 25%+ silent dilution
  through MFN-clause auto-upgrades; LLC formation deferred until
  year 3 misses 2 years of QSBS-clock potential; the cumulative
  cost of preserved-options approaches $500k-$2M in foregone value.
- **Recovery-move.** Self-directed: compute carrying-cost for each
  preserved option explicitly — what does it cost (in dollars,
  dilution, or foregone-arbitrage) per month to keep this option
  open? Sum the monthly carrying costs; if the sum exceeds the
  expected option-exercise-value, the optionality is no longer
  positive-EV and the founder should commit. Self-directed baseline:
  Founder Collective on capital-efficiency / cap-table arithmetic;
  Patio11 on calculating real-options-net-of-carrying-cost.

### F13.4 Real-options-thinking applied qualitatively misroutes selectively

- **Statement.** "I use real-options thinking on big decisions."
  The framing's real-options thinking is *mathematically
  sophisticated* but founder use of it is *typically qualitative* —
  founders rarely actually compute option-values, so the framing
  produces directional-guidance without quantitative discipline.
  The result is selective application: founders preserve optionality
  when loss-aversion bias is dominant (don't quit the day job) and
  forsake it when excitement-bias is dominant (sign the SAFE without
  reading the MFN clause).
- **Source-evidence.** `framings.md` F13 fourth Excludes bullet —
  "'Real-options thinking' is mathematically sophisticated but
  founder use of it is typically qualitative — selective application
  produces preserving optionality when loss-aversion bias is
  dominant and forsaking it when excitement-bias is dominant";
  boundary `personal-finance` on real-options finance.
- **Trigger.** Founder is using real-options language in decision-
  framing AND has not done quantitative option-valuation (Black-
  Scholes-style or scenario-tree-equivalent) for the specific
  decisions AND shows different optionality-preservation behavior
  in loss-domain decisions vs gain-domain decisions (preserve in
  loss, abandon in gain).
- **Failure-mode.** Founder qualitatively preserves day-job optionality
  (loss-domain — bias-aligned) while quantitatively-irrationally
  abandoning SAFE-stacking optionality (gain-domain — excitement-
  aligned) by signing post-money-cap SAFEs without modeling the
  MFN-cascade-dilution; the founder reports "I'm using real-options
  thinking" but the actual decisions are bias-driven.
- **Recovery-move.** Self-directed: compute option-values
  quantitatively for the 3-5 highest-leverage decisions explicitly
  (Black-Scholes for tradeable options, scenario-tree for
  startup-specific options); compare quantitative output to
  intuitive direction; if they diverge, follow the quantitative
  output rather than the intuition. **D5 high-stakes pocket —
  consult a startup attorney AND CPA** for cap-table modeling on
  SAFE-stacking decisions. Self-directed baseline: Founder
  Collective on dilution-modeling tools; Carta cap-table
  scenario-modeling.

### F13.5 Two-way-door rhetoric can mask actually-one-way decisions

- **Statement.** "This is a two-way door — we can reverse if it
  doesn't work." The framing's two-way-door rhetoric (Jeff Bezos)
  can mask decisions that are *actually one-way* — equity issued
  cannot be clawed back without consideration or for-cause
  termination; SAFE-stacking-with-MFN accumulates dilution that
  doesn't reverse; LLC-to-C-corp conversion is technically reversible
  but tax-friction makes it functionally one-way; CIIAA-IP-
  assignment without explicit carve-out is functionally permanent.
- **Source-evidence.** Patio11 voice on "one-way door vs two-way
  door" distinctions; Jeff Bezos shareholder-letter framing on
  two-way-door decisions; founder-attorney-blog voices on
  irreversibility of equity / IP / tax-election decisions.
- **Trigger.** Founder is framing a decision as "two-way door"
  AND has not enumerated the specific reversal mechanism
  ("if we do X, the reversal requires Y") AND the decision touches
  any of: equity issuance, IP-assignment, tax-election, contract-
  signing with personal-guarantee, regulatory-license-application
  AND has not consulted appropriate counsel.
- **Failure-mode.** Founder issues 5% advisor equity as "two-way
  door" thinking ("if it doesn't work we'll buy it back"); advisor
  vests immediately on grant; advisor disengages 6 months later
  but retains equity; buyback requires consideration (cash payment)
  the company doesn't have; the equity remains on cap-table for
  the duration; year-5 acquisition diligence flags the dormant-
  advisor equity as messy.
- **Recovery-move.** Self-directed: BEFORE framing a decision as
  two-way-door, enumerate the explicit reversal mechanism — what
  exactly does it take to reverse? If the reversal requires legal
  action, consideration payment, or material time-delay, the
  decision is *one-way for practical purposes* and should be
  treated with one-way-door discipline. **D1 high-stakes pocket —
  consult a startup attorney** before issuing any equity / IP /
  founder-grants to confirm reversal-mechanisms. Self-directed
  baseline: Patio11 essays on one-way vs two-way doors; Bezos
  shareholder letters with the original distinction (and the
  cases where Bezos clarifies the distinction is not always
  symmetric).

---

## 14. Conviction-commitment / burn-the-boats framing (F14)

### F14.1 Burn-the-boats destroys household financial stability for family-obligation founders

- **Statement.** "Burn the boats — commit fully to the startup."
  The framing's commitment-as-selection-mechanism *destroys household
  financial stability* for founders with dependents, mortgage, and
  family obligations — single-no-dependents founders can rationally
  leap with $20k savings and a credit card, but a single-income-
  with-kids-and-mortgage founder applying the same standard
  bankrupts the family if the startup fails (which is the modal
  outcome).
- **Source-evidence.** `framings.md` F14 first Excludes bullet —
  "the 'burn the boats' reflex destroys household financial stability
  for founders with dependents, mortgage, and family obligations —
  Indie Hackers / r/SmallBusiness voices catch the household-
  context-conditioning; YC playbook voice often abstracts it";
  opposes F13 (optionality-preservation) on D3 / D2; boundary
  `personal-finance` D2.
- **Trigger.** Founder is reading conviction-commitment / burn-the-
  boats content from YC / Sam Altman / Brian Chesky voice AND has
  family obligations (dependents, mortgage, sole-income, no
  household-runway floor) AND is applying the single-no-dependents
  default leap-standard without household-context adjustment AND
  has not consulted a financial advisor on the household-runway
  floor.
- **Failure-mode.** Sole-income father-of-3 with $400k mortgage and
  $40k household-runway leaps fully on "burn the boats" reasoning;
  startup fails at month 18; household has exhausted savings +
  drained $80k from retirement (10% penalty + ordinary-income
  tax) + accumulated $40k credit-card debt at 24% APR; family
  forced to sell home in a down market; net household-net-worth
  loss $300-500k vs the dual-track counterfactual; recovery to
  pre-leap financial state takes 5-8 years.
- **Recovery-move.** Self-directed: distinguish household-context
  before applying conviction-framing content — single-no-dependents
  founders apply YC default; family-obligation founders MUST adjust
  for household-runway floor (minimum 18-24 months of cleared
  household expenses + medical + emergency-event-reserve). Cross-
  domain edge to `personal-finance` D2 (emergency-fund sizing);
  `health-insurance` D5 (COBRA-to-Marketplace transition). Self-
  directed baseline: r/SmallBusiness / Indie Hackers threads on
  family-context founding; The Finance Buff on household-runway-
  for-self-employed; consider whether bootstrap or part-time
  founding is the correct fit before applying YC default.

### F14.2 Founder-takes-no-salary discipline destroys retirement-trajectory

- **Statement.** "Founder takes no salary for 12 months until
  milestone." The framing's "founder takes no salary" discipline is
  *correct posture for founders with runway* but *destructive for
  founders without* — the discipline can become rationalization for
  accepting catastrophic personal-finance damage (deferred medical /
  dental care, missed 401(k) contribution years, accumulated credit-
  card debt at 20%+ APR that destroys future net-worth even at
  successful exit).
- **Source-evidence.** `framings.md` F14 second Excludes bullet —
  "'Founder takes no salary for 12 months until milestone' is
  correct posture for founders with runway but destructive for
  founders without — the framing's 'all-in' reflex rarely engages
  with the non-trivial personal-finance cost of going-without,
  particularly the catastrophic-and-irreversible-medical-event
  tail risk"; boundary `health-insurance` and `personal-finance`.
- **Trigger.** Founder is committed to no-salary-until-milestone
  AND has dependents OR has > $20k in revolving credit-card debt
  AND has missed > 6 months of 401(k) contributions AND is
  deferring routine medical / dental care to preserve cashflow.
- **Failure-mode.** Founder operates no-salary for 24 months;
  accumulates $60k credit-card debt at 22% APR; misses $40k of
  401(k) employer-match + employee-contribution + investment-
  growth opportunity ($40k contribution + employer-match opportunity
  + 20+ years of compounded growth = $300-500k forgone retirement);
  defers dental work that becomes $25k of urgent-care; even if
  startup exits at $5M, the personal-finance net-position is
  $400-700k lower than the modest-salary counterfactual.
- **Recovery-move.** Self-directed: budget a minimum-viable founder
  salary covering basic household expenses + 401(k) contributions
  + routine medical / dental care + emergency-event-reserve;
  the "no-salary" discipline applies to ego-driven salary
  preservation, not to genuine subsistence. Cross-domain edge to
  `personal-finance` (emergency-fund + retirement-contribution
  continuity) and `health-insurance` (do NOT defer preventive
  care). Self-directed baseline: r/personalfinance threads on
  founder-comp baseline; The Finance Buff on retirement-contribution
  continuity for self-employed.

### F14.3 "Customers feel commitment" claim is rhetorical not measured

- **Statement.** "Customers feel commitment, investors back
  conviction." The framing's strong-claims about commitment-as-
  asset are *partially-correct narrative; the strong-version is
  rhetorical rather than measured*. Empirically, many investors back
  hedged-founders (spouse-is-CEO-elsewhere, fractional-CEO, founder-
  on-sabbatical-from-BigCo), and many customers buy from companies
  they think are sustainable specifically because they have
  hedged-founders with reliable financial footing.
- **Source-evidence.** `framings.md` F14 third Excludes bullet —
  "'Customers feel commitment' / 'investors back conviction' are
  plausible but not measurably falsifiable claims — the framing's
  rhetoric is self-reinforcing in a way that makes it hard to
  distinguish from founder-self-flattery rhetoric"; PG voice tends
  to strong-version; empirical research is more mixed.
- **Trigger.** Founder is making leap-decision OR raising-decision
  AND citing "customers / investors will sense commitment" as
  primary argument AND has not modeled the specific customer-
  decision-criterion or investor-decision-criterion AND is treating
  commitment-as-asset as evidence rather than as hypothesis.
- **Failure-mode.** Founder leaps fully on conviction-rhetoric;
  customers in target segment actually value financial-sustainability
  signals (longer runway, professional team, payment-reliability)
  more than commitment-signals; founder's "all-in" posture comes
  across as unstable rather than reassuring; enterprise sales-
  cycles suffer because procurement views the company as risky;
  the rhetorical commitment-advantage doesn't materialize.
- **Recovery-move.** Self-directed: separate the commitment-as-
  customer-asset hypothesis from the commitment-as-personal-
  necessity argument — the personal commitment may be necessary
  for founder-execution, but it's not necessarily a customer-
  facing asset; test the commitment-as-customer-asset hypothesis
  empirically (do customers buy more from highly-committed founders?
  what's the actual evidence in your segment?). Self-directed
  baseline: First Round Review interviews where customers explain
  their actual buying criteria; Lenny Newsletter on enterprise
  buying-process realities.

### F14.4 Sunk-cost rationalization disguised as conviction-discipline

- **Statement.** "I'm committed — I won't quit." The framing's
  conviction-rhetoric resists *when-to-quit* calibration —
  founders 4 years into a company that isn't working can use
  "I'm committed, I won't quit" to justify continued effort on a
  path that data suggests should be abandoned. The conviction-
  rhetoric makes pivoting or shutting-down feel like personal
  failure rather than rational capital-allocation.
- **Source-evidence.** `framings.md` F14 fourth Excludes bullet —
  "the framing under-engages with commitment-as-sunk-cost-
  rationalization — founders 4 years into a company that isn't
  working can use 'I'm committed' to justify continued effort";
  the optionality-preservation framing's "two-way door" thinking
  catches this; the conviction-commitment framing's rhetoric
  resists it; opposes F13 on D2 (when to abandon).
- **Trigger.** Founder is at year 3+ AND business metrics have
  been flat or declining for 12+ months AND founder is reasoning
  from conviction-commitment framing to justify continuation AND
  has not done structured pivot-or-shutdown analysis (cohort-
  retention curve, market-fit signal-strength, alternative-use-of-
  capital and time).
- **Failure-mode.** Founder continues at $50k MRR with 18 months
  of flat growth; 2 additional years pass with no improvement; net
  founder-opportunity-cost of the additional 2 years is $400-600k
  in foregone salary + $200-300k in foregone retirement-
  contribution + 2 years of life-trajectory delay; the founder
  eventually shuts down at year 6 with same net result as
  shutting down at year 4 would have produced, but with 2 years
  of additional personal cost.
- **Recovery-move.** Self-directed: implement annual "shutdown
  review" process — explicit annual evaluation of (a) actual
  metrics vs starting hypothesis, (b) alternative-use-of-capital
  / time at current point, (c) pivot-vs-shutdown-vs-continue
  decision with explicit criteria; engage an external advisor
  (mentor, executive coach, fellow founder) for structured pivot-
  decision conversations; treat shutdown-as-rational-allocation
  rather than personal-failure framing. Self-directed baseline:
  Founder Collective on capital-efficiency / pivot-discipline;
  Patio11 on when to quit; YC Library on the difficult-conversations
  founders need to have with themselves.

### F14.5 Hires-who-match-commitment-level overfits to founder-clone hiring

- **Statement.** "Hire people who match commitment — full-time,
  equity-significant, willing to bet career on the company." The
  framing's "match commitment-level" hiring reflex *overfits to
  founder-clone hiring* — the company ends up with senior team that
  mirrors founder's risk-tolerance, household-context, and life-
  stage, which produces cognitive homogeneity and excludes senior
  talent with family obligations or career-risk constraints.
- **Source-evidence.** `framings.md` F14 mental-model framing on
  "hire people who match commitment"; cross-domain edge to `tech-
  career` on senior-hiring distribution-shifts; Lenny Newsletter
  on diverse-perspective hiring at startups.
- **Trigger.** Founder is hiring senior team members AND filtering
  candidates primarily on commitment-signal (will-they-take-equity-
  over-salary, will-they-work-80-hour-weeks, will-they-skip-vacation)
  AND the senior team is becoming homogeneous (similar age, similar
  family-stage, similar background) AND no diverse-perspective
  hiring goal is explicit.
- **Failure-mode.** Year 2 senior team is 5 single-no-dependents
  20-something-engineers; the team produces high-velocity but
  systematically misses the family-context customer segment (which
  is 60% of the market); customer-research suffers from team-
  context blindness; the company's product evolves to serve the
  team's context, not the broader market; competitor with diverse
  team captures the family-context segment.
- **Recovery-move.** Self-directed: explicitly recruit for diverse-
  perspective (family-stage, background, prior-industry, life-
  experience) rather than commitment-clone; structure roles to
  accommodate diverse-life-context (parents with flexible hours,
  caregivers with reduced-availability windows, senior contributors
  with constrained work-windows); measure hiring distribution
  quarterly to detect homogenization. Self-directed baseline: First
  Round Review on diverse-perspective hiring; Lenny Newsletter on
  senior-talent recruiting beyond founder-network defaults.

---

## Cross-framing tensions

These call out where blindspots in one framing are the *recovery
move* of another, mirroring the structure in
[`framings.md` "Cross-framing tensions"](./framings.md). The pairings
are useful for the Triage / Risk Officer when the asker is clearly
inside one framing — the contrarian framing's blindspot list is often
the right intervention.

- **F1 (raise-and-scale) ↔ F2 (bootstrap / default-alive) on D2.**
  F1's "raise to compress time-to-PMF" misses F2's recognition that
  pre-PMF capital accelerates discovery of the wrong thing (F1.1);
  F2's "bootstrap to revenue" misses F1's recognition that network-
  effects categories cede to venture-backed competitors at bootstrap-
  pace (F2.1). When the asker is F1-anchored (mentions venture
  fundraising, board structure, dilution math, venture-scale
  targets), surface F1.1 (pre-PMF capital problem) and F1.4
  (venture-market cyclicality). When the asker is F2-anchored
  (mentions MRR transparency, ramen-profitability, Indie Hackers
  ethos, lifestyle-business outcomes), surface F2.1 (network-
  effects categories) and F2.4 (under-investment in growth at
  ramen-profitable).

- **F9 (PLG) ↔ F10 (SLG) on D9 / D10.** F9's "build the funnel and
  customers convert" misses F10's recognition that mid-market /
  enterprise sales fundamentally requires sales-overlay (F9.1);
  F10's "build the AE-CSM-SE team" misses F9's recognition that
  PLG-only motions cap at SMB segment but pure-SLG also misses
  the bottom-of-funnel volume. When the asker is F9-anchored
  (mentions freemium / self-serve / activation / NRR-from-
  expansion / PLG-canon), surface F9.1 (PLG caps at SMB) and F9.5
  (activation-rate masking product-fundamentals). When the asker is
  F10-anchored (mentions enterprise / SOC 2 / MEDDIC / quota / AE-
  OTE / CAC-payback), surface F10.1 (Series A required for SLG) and
  F10.4 (metrics encode bad assumptions). Hybrid PLG-with-sales-
  overlay motions are increasingly common and the framings can
  co-exist rather than purely conflict.

- **F11 (founder-mode) ↔ F12 (manager-mode) on D10 / D11.** F11's
  "stay in the details" misses F12's recognition that founder-mode
  caps at ~200 people without org-design support (F11.2); F12's
  "build the executive layer" misses F11's recognition that over-
  hiring executive layer pre-PMF accelerates burn without
  accelerating revenue (F12.1). When the asker is F11-anchored
  (mentions PG *Founder Mode* / Brian Chesky / Steve Jobs / skip-
  level), surface F11.1 (founder-mode pre-PMF rationalization) and
  F11.4 (board expectations diverge at growth-stage). When the
  asker is F12-anchored (mentions scalable-org / OKR / VP-of-X /
  professional-management / hire-from-Google), surface F12.1 (over-
  hiring pre-PMF) and F12.4 (founder constitutional capacity-to-
  delegate). Both framings are partially-correct at different
  company-stages.

- **F13 (optionality-preservation) ↔ F14 (conviction-commitment) on
  D2 / D3 / D5.** F13's "preserve options" can rationalize failure
  to commit (F13.1); F14's "burn the boats" can destroy household
  financial stability for family-obligation founders (F14.1). When
  the asker is F13-anchored (mentions runway / fallback / preserve-
  options / two-way-door / Patio11 anti-platitude), surface F13.1
  (permanent optionality is inaction) and F13.3 (option-value-
  decay-over-time). When the asker is F14-anchored (mentions ten-
  year-horizon / no-Plan-B / founder-all-in / burn-the-boats /
  Sam-Altman-conviction), surface F14.1 (burn-the-boats destroys
  family-context founders) and F14.4 (sunk-cost rationalization
  disguised as conviction-discipline). The conflict often resolves
  on the asker's household-context rather than on principle —
  cross-domain edge to `personal-finance` D2 (household-runway
  sizing) and `health-insurance` D5 (COBRA-to-Marketplace transition).

- **F5 (QSBS / tax-tail-event) ↔ F2 (bootstrap / default-alive) on
  D5.** F5 argues for early C-corp conversion and priced-round
  timing to start the QSBS clock (F5.5: SAFE-stacking silently
  delays QSBS clock by 18-24 months); F2 argues for LLC simplicity
  and delayed-formation, treating entity question as second-order
  to revenue-and-customer validation. Same founder pre-formation,
  opposite recommendation. The conflict resolves on whether the
  founder-and-business is plausibly venture-scale (F5 dominates,
  QSBS-clock-start is load-bearing tail value) or lifestyle / niche
  (F2 dominates, QSBS practically irrelevant). When the asker is
  F5-anchored, surface F5.5 (SAFE-stacking delays QSBS) and F5.3
  (LLC-to-C-corp conversion §351 mechanics); when the asker is
  F2-anchored but exit-trajectory looks venture-scale, surface F5.4
  (state-conformity divergence) as the corrective.

- **F4 (SE-tax-and-entity-arbitrage) ↔ F5 (QSBS / tax-tail-event) on
  D4.** F4 says S-corp election saves 15.3% × distribution-portion
  of FICA arbitrage starting at the ~$80-100k crossover (F4.1).
  F5 says S-corp is INCOMPATIBLE with QSBS — QSBS requires C-corp
  throughout substantially-all of the 5-year-hold-period (F5.5
  mental model), so S-corp election eliminates QSBS eligibility.
  For potentially-venture-scale founders, F5 dominates the arbitrage
  entirely: locking in 15.3% × $100k = $15k/yr of SE-tax savings is
  a poor trade for eliminating a potential $10M+ QSBS exclusion.
  For non-venture-scale consulting / service businesses, F4
  dominates because QSBS is practically irrelevant. The conflict
  resolves on plausible-exit-trajectory; founders straddling the
  boundary should explicitly model both paths with a startup-
  experienced CPA. **D4 + D5 + D8 high-stakes pocket** — consult a
  startup-experienced CPA AND startup attorney; the joint
  optimization is not a generic-CPA-solvable problem. Boundary
  `personal-finance` F4 / F8 / F10 on QSBS-and-S-corp coordination.

- **F8 (day-job-fallback) ↔ F14 (conviction-commitment) on D3.**
  F8 says wait until the next vest cliff, carve out the side-
  project IP in writing, maintain the day-job as the safe baseline.
  F14 says the day-job-as-baseline is itself a hedge that signals
  lack of conviction. Same household-context, same MRR-level,
  opposite leap-recommendation. When the asker is F8-anchored
  (mentions vesting cliff / RSU schedule / household-runway /
  health-insurance / spouse-income), surface F8.1 (W-2-stability-
  overstated) and F8.3 (Roth-conversion window on low-income year).
  When the asker is F14-anchored (mentions conviction / commitment /
  ten-year-horizon / no-Plan-B), surface F14.1 (burn-the-boats
  destroys family-context founders) and F14.2 (no-salary
  destroys retirement-trajectory). The conflict often resolves on
  the asker's personal-finance situation (dependents, household-
  income-diversification) rather than on principle.

- **F3 (founder-fairness-and-vesting) ↔ F7 (ABC-test / worker-
  classification) on D1 / D10.** F3 focuses on co-founder equity-
  vesting-and-IP-assignment mechanics with the assumption co-
  founders are W-2 employees of the C-corp issued founder restricted
  stock; F7 focuses on the ABC-test classification of every worker
  including post-incorporation co-founders. The hybrid case
  (post-incorporation co-founder joining as 1099 with equity grant
  in lieu of salary, common in early-stage) sits in tension between
  the framings — F3 wants founder-restricted-stock + 83(b) +
  CIIAA; F7 wants W-2-vs-1099 ABC-test analysis. When the asker
  is in this hybrid, surface BOTH F3.3 (post-incorporation co-
  founder addition mechanics) and F7.4 (contractor-side asymmetric
  exposure on post-separation misclassification claims). **D1 + D7
  high-stakes pocket** — consult both startup attorney AND
  employment-law attorney for hybrid co-founder cases.

- **F6 (liability-shield) ↔ F4 (SE-tax-and-entity-arbitrage) on D6.**
  F6 says form an LLC for liability-shield benefit; F4 says elect
  S-corp on the LLC for SE-tax arbitrage; both framings interact
  on the entity-form-and-tax-classification choice. The hybrid
  case (LLC with S-corp election) has its own complexity: F6.4
  (LLC-vs-C-corp shield equivalence false; investor-expectations
  differ) and F4.4 (single-member LLC-to-S-corp framing misses
  multi-member partnership complexity) jointly capture the
  practical analysis. When the asker is choosing entity form for
  a venture-trajectory company, F5's QSBS-requires-C-corp
  consideration dominates both F6 and F4 — surface F5.5 (SAFE-
  stacking-delays-QSBS) and F6.4 (LLC-vs-C-corp shield equivalence).
  **D4 + D6 high-stakes pocket** — consult an entity-formation-
  experienced startup attorney AND CPA before committing to entity
  form when venture-trajectory is plausible.

- **F11 (founder-mode) ↔ F12 (manager-mode) at growth-stage
  transition.** The same founder, having succeeded in founder-mode
  pre-Series-A, faces the question of whether to *continue*
  founder-mode at 100+ employees or transition to manager-mode.
  F11.2 (skip-level practices don't scale beyond ~200 people) and
  F12.4 (founder's constitutional capacity-to-delegate often the
  bottleneck) are the synthesis blindspots that both framings need
  surfaced together. Many founders mis-time the transition in
  either direction (transitioning too early loses founder-DNA
  advantage; transitioning too late caps growth). When the asker
  mentions employee-count > 50, post-Series-A scaling questions,
  executive-team-design, or VP-hire decisions, surface BOTH F11
  and F12 blindspots; the resolution depends on founder-personality,
  company-stage, and board composition. Boundary `tech-career` on
  engineering-management scaling.

---

## Maturity / source-anchor note

This file is `planned` maturity per
[`_meta_ontology.md` §6](../_meta_ontology.md). Source-evidence
lines above currently anchor to:

- `framings.md` Excludes lines (load-bearing — the framing-level
  Excludes were authored specifically to seed Layer 3, per the
  "Notes for downstream layers" section of `framings.md` and the
  Coverage map's explicit "Sweep all 14 framings × ~4 bullets each
  = ~56 blindspot candidates; promote ≥5 per framing").
- `decisions.md` §Notes high-stakes pocket enumeration (D1 / D4 /
  D5 / D7 / D8 / D11) for Recovery-move professional-channel
  routing.
- Conceptual references to community-voice classes named in
  `framings.md` voice anchors (Indie Hackers, r/Entrepreneur,
  r/SmallBusiness, Hacker News startup voices, Patio11 / Patrick
  McKenzie, YC playbooks, SaaStr / Jason Lemkin, Tomasz Tunguz /
  Redpoint, Lenny Newsletter, First Round Review, a16z growth
  essays, Founder Collective, The Finance Buff, Clerky, Stripe
  Atlas, IRS-publication-authority, state-bar lawyer-referral-
  service, SEC EDGAR / FINRA BrokerCheck).

When `domain_knowledge/entrepreneurship/sources.yaml` is authored
and `domain_knowledge/entrepreneurship/communities/*.md` community
profiles land, source-evidence lines above should be tightened to
specific source-view ids.

**High-stakes posture per Mechanism E partial-gating**: entrepreneurship
is `high_stakes: false`, so Recovery moves are NOT uniformly routed
to professional counsel. Recovery moves above flag professional
referral inline only where the decision's six-figure-tail-risk
justifies it, per [`decisions.md` §Notes](./decisions.md):

- **Startup attorney with founder-side experience** (Cooley /
  Gunderson / WSGR / Orrick / Fenwick high-end; Clerky / Stripe
  Atlas / Atomic / Mintz accessible): D1 (F3.1 LLC vs C-corp
  conversion 83(b) mechanics; F3.2 50/50 split decisions; F3.3
  post-incorporation co-founder addition; F3.4 for-cause definition
  drafting; F3.5 double-trigger-acceleration negotiation; F5.2
  family-stacking via non-grantor trusts; F5.3 LLC-to-C-corp
  conversion §351 mechanics; F5.4 state-conformity residency-
  planning; F6.4 LLC-vs-C-corp at formation; F6.5 personal-guarantee
  negotiation; F13.2 founder-agreement documentation; F13.5
  reversal-mechanism enumeration); D5 (F1.3 cumulative protective-
  provision lock-in; F1.5 term-sheet comparison; F5.5 SAFE-vs-
  priced-round QSBS-clock-start); D11 (F6.2 veil-piercing
  litigation; F11.3 founder-CEO transition mechanics; F11.4 board
  protective-provision analysis).

- **S-corp-experienced CPA (NOT generic 1040-prep CPA)**: D4 (F4.1
  state-and-SSTB-adjusted break-even modeling; F4.3 reasonable-
  salary written determination; F4.4 multi-member LLC partnership
  tax mechanics; F4.5 multi-state nexus from remote-W-2 hire;
  F5.3 LLC-to-C-corp §351 conversion); D8 (F4.2 S-corp +
  retirement-vehicle joint optimization; The Finance Buff voice as
  the procedural-floor on Mega-Backdoor-Roth eligibility analysis).

- **Employment-law attorney** in the worker's state of residence /
  employment: D7 (F7.1 borderline-engagement ABC analysis; F7.2
  contractor-LLC-doesn't-immunize; F7.3 FTC non-compete rule
  current-status; F7.4 sustained-senior-contractor classification;
  F7.5 retroactive-misclassification remediation; F8.2 anticipated-
  business carve-out negotiation); D11 (F7.3 non-compete /
  non-solicit enforcement; F6.3 IRS Trust Fund Recovery Penalty
  defense).

- **Tax attorney with §1202 QSBS + §351 entity-conversion
  experience**: D1 (F5.2 family-stacking; F5.3 §351 conversion;
  F5.4 state-conformity); D5 (F5.5 SAFE-to-priced-round QSBS
  acceleration; F5.1 redemption-tests); cross-domain edge to
  `personal-finance` D6 / D7.

- **Estate-planning attorney** (for family-stacking of QSBS / equity
  pre-issuance): F5.2 (non-grantor trust formation at company-
  formation, NOT at exit); cross-domain edge to `family-planning`
  and `personal-finance` D10.

State Bar / FINRA BrokerCheck / state-bar-grievance lookup on any
individual professional recommended is the $0-friction procedural
floor named on every individual-professional referral.

For lower-stakes framings (F2 bootstrap, F8 day-job-fallback on
non-IP-carveout questions, F9 PLG, F10 SLG, F11 founder-mode, F12
manager-mode on non-board-conflict, F13 optionality-preservation on
non-equity-decisions, F14 conviction-commitment on non-cap-table
decisions), Recovery moves above are **self-directed** with named-
resource pointers (Indie Hackers community, r/Entrepreneur top-voted
threads, r/SmallBusiness operator-experience threads, Patio11 /
Kalzumeus / patio11.substack.com essays, YC Library at
ycombinator.com/library, SaaStr / Jason Lemkin playbooks at
saastr.com, Tomasz Tunguz quarterly venture-market analysis at
tomtunguz.com, Lenny Newsletter at lennysnewsletter.com, First Round
Review at firstround.com/review, Founder Collective at
foundercollective.com, The Finance Buff at thefinancebuff.com,
Clerky handbook at clerky.com, Stripe Atlas at stripe.com/atlas,
IRS Pub 535 / 583 / 587 / 463 / 15 / 560).

**Date-stamp risk**: anchor numbers above carry date-stamp risk
inherited from the underlying tax-code / regulatory corpus. Entries
to re-check before relying on for an active decision:

- F4.1 — Social Security wage base ($168,600 in 2025; updates
  annually); SSTB phase-out thresholds ($241,950 single / $483,900
  MFJ 2024; verify 2025); QBI §199A 20% deduction (subject to
  potential TCJA-sunset legislation).
- F4.3 — Watson v US 2012 reasonable-salary precedent (stable but
  post-Watson IRS audit-and-litigation patterns continue to
  develop).
- F5.1 — IRC §1202 QSBS eligibility ($50M aggregate gross assets
  threshold; TCJA-era proposals to raise to $75M have not passed
  as of 2025).
- F5.4 — State QSBS conformity (CA non-conform, NY partial, NJ
  partial — verify state legislative changes).
- F7.3 — FTC 2024 non-compete rule (status in litigation; *Ryan
  LLC v FTC* Northern District of Texas; check current federal-
  rule status with employment-law counsel).
- F7.2, F7.4 — CA AB-5 + AB-2257 + Prop 22 status (Prop 22 in
  litigation; check current state-of-play); PAGA penalty amounts
  ($100/$200 per pay period; check for legislative changes).
- F8.5 — COBRA / Marketplace / ACA subsidy-cliff arithmetic (annual
  ACA enrollment-rule changes; verify current cycle).
- F11.4 — Board governance / protective-provision norms (NVCA
  template evolves; verify current practice).

**Mechanism E posture summary**: entrepreneurship's per-framing
inline referral pattern is the partial-gating shape
`_meta_ontology.md` flagged when it noted entrepreneurship is
"high_stakes: false because failure is the modal outcome and is
generally survivable; not Mechanism-E-gated despite large dollar
swings." The `domain_pack.md` (later sub-item) will encode this
pattern as selective referrals rather than the blanket-defer
language `immigration` / `health-insurance` / `personal-finance` /
`family-planning` / `legal-disputes` require. The selective-referral
posture is the calibration that distinguishes `entrepreneurship`
from the uniformly-Mechanism-E-gated domains.
