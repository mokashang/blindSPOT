# tech-career — blindspots.md (Layer 3)

Blindspot catalogue for `tech-career`. Each entry names what a real
practitioner in the relevant framing would say is missed — sourced from
audited community profiles (`community_profiles/*.md`) and source-views
in [`data/source_registry.yaml`](../../data/source_registry.yaml), not
LLM extrapolation. Per [`_schema.md`](../_schema.md), every entry is
relative to a framing in [`framings.md`](./framings.md) and ships with
a trigger pattern and a concrete recovery move.

Each blindspot lists:
- **Statement** — one sentence naming what is missed
- **Source evidence** — the community-profile audit or source-view that
  this blindspot was extracted from (not invented)
- **Trigger** — the situation pattern the Triage / Risk Officer should
  match against
- **Failure mode** — the specific bad outcome if the blindspot stays
  unsurfaced
- **Recovery move** — the concrete action that resolves it

The framing names below match [`framings.md`](./framings.md) exactly;
all 14 are covered with ≥ 5 entries each.

---

## 1. AMT-minimization framing

### 1.1 The modal pre-IPO outcome is flat-or-down, but the framing only models monotone-up

- **Statement**: Tranched ISO exercise advice assumes FMV will keep
  rising long enough for the AMT credit to recover; in the real base
  rate (acquihire-zero, 7-year flat secondary, 10-year stall) the
  $200k AMT bill is paid on stock that ends at $0 and the credit is
  uncollectable.
- **Source evidence**: `community_profiles/tax-and-finance-professionals.md`
  Known-blindspot 1 ("Optimizes tax on equity that may never clear
  strike + AMT … $1.2M-FMV employee to a $200k AMT check on stock
  worth $0 three years later").
- **Trigger**: Asker is being advised to exercise ISOs early "for the
  QSBS clock" or to "tranche across calendar years" at a private
  company with no near-term liquidity event named.
- **Failure mode**: Asker writes the AMT check, company stalls or
  recaps, AMT credit dies unrecoverable because regular tax never
  exceeds AMT in their bracket.
- **Recovery move**: Run the calculation in worst-case ($0 exit)
  dollars before exercising; size the exercise to a tranche the
  asker would tolerate losing entirely. If the asker can't tolerate
  the worst case, don't exercise — even if the EV-positive case is
  larger.

### 1.2 State AMT divergence dominates the federal optimization on multi-state moves

- **Statement**: California has no refundable AMT credit and pulls
  CA-employer RSU vests into CA tax post-move; NY's statutory
  allocation claws back option income across grant-to-exercise for
  partial-year residents. The state delta is routinely larger than
  the federal tranche optimization the framing focuses on.
- **Source evidence**: `community_profiles/tax-and-finance-professionals.md`
  Known-blindspot 2 ("State divergence underweighted even when it
  dominates"); reinforced by
  `community_profiles/reddit-tech-collective.md` typical-concern on
  state-tax residency (California claws back RSU income earned-while-
  resident even after you move).
- **Trigger**: Asker mentions a multi-state move (CA→TX/WA/FL, or
  NY→remote) alongside any ISO exercise or RSU vest decision.
- **Failure mode**: Asker optimizes the federal AMT tranche, moves
  to TX/WA/FL expecting the state delta as gravy, and discovers post-
  move CA still taxes the trailing vest under the statutory allocation
  rule for grants earned in-state.
- **Recovery move**: Compute state liability under both states' rules
  for the year of move BEFORE the federal tranche decision; many
  exercise-timing choices invert when the state component is included.

### 1.3 The framing's "tranche optimally" advice collapses to "don't exercise" for cash-constrained grantees

- **Statement**: The AMT-minimization model assumes the reader has
  six figures of liquid net worth; for a grantee with $40k cost +
  $90k AMT + $30k savings, "tranche optimally" produces "don't
  exercise" and obscures the realistic paths (net-exercise-at-tender,
  sell-to-cover, 83(b)-on-early-exercise, secondary lender, ESO Fund
  non-recourse loan).
- **Source evidence**: `community_profiles/tax-and-finance-professionals.md`
  Known-blindspot 5 ("'Can't afford to exercise' collapses to 'don't
  exercise'"); reinforced by `framings.md` §1 Excludes line on
  cash-bind reality.
- **Trigger**: Asker names a personal-balance-sheet number (savings,
  emergency fund, mortgage runway) alongside an exercise question.
- **Failure mode**: Asker reads the advice as "you can't afford this,
  don't do it" and forfeits at the 90-day PTE without learning about
  the alternative exercise paths that exist precisely for cash-constrained
  grantees.
- **Recovery move**: Surface the four cash-light paths explicitly:
  (1) early-exercise + 83(b) pre-runup if the plan permits;
  (2) net-exercise or sell-to-cover at the next tender;
  (3) ESO Fund / Quid / secondary lender non-recourse loan (assess
  due-diligence eligibility); (4) partial exercise sized to the cash
  available, accepting the forfeiture of the rest.

### 1.4 The 409A FMV input to the AMTI calc is endogenous, not exogenous

- **Statement**: The framing treats 409A FMV as a given input to the
  bargain-element calculation; in practice 409A is a negotiated number
  between the company and its valuation firm, and a refresh timed
  against a tender can shift the bargain element by 30%+. Pre-tender
  exercisers who don't ask about pending 409A refreshes pay AMT on the
  post-tender bump.
- **Source evidence**: `framings.md` §1 Excludes line on 409A as
  negotiation;
  `community_profiles/carta-and-platform-data.md` Known-blindspot 1
  on under-reported pre-409A repricings.
- **Trigger**: Asker is timing an exercise in the same calendar window
  as a tender, secondary, or priced round announcement.
- **Failure mode**: Asker exercises on Monday at the stale 409A,
  company refreshes 409A on Friday at +30%, asker's AMTI is calculated
  at the old strike but their next exercise sits at the new spread —
  losing the cheap window entirely without realizing it was about to
  vanish.
- **Recovery move**: Ask the company directly about the 409A refresh
  schedule before exercising; in tender windows, the answer often
  shifts the calendar-year exercise plan by a quarter.

### 1.5 The AMT-credit-as-asset frame ignores asymmetric death and disposition risk

- **Statement**: The framing models the AMT credit as an asset
  recoverable in any future year where regular tax > AMT; it ignores
  that the credit dies at death without step-up, that it doesn't
  transfer in divorce in many state regimes, and that a year-4
  disqualifying disposition (acquihire forced short-window sale)
  triggers ordinary income that *eats* the AMT-credit position
  asymmetrically.
- **Source evidence**: `community_profiles/tax-and-finance-professionals.md`
  Known-blindspot 3 ("AMT credit dying at death (no step-up)");
  `framings.md` §1 Excludes on cash-bind, and §2 Excludes on
  year-4 disqualifying redemption resetting the QSBS clock.
- **Trigger**: Asker is older (50+), in a high-divorce-risk situation,
  or holding equity at a company likely to be acquihired (declining
  burn, single-customer dependency, distressed last round).
- **Failure mode**: Asker accumulates years of AMT credit as a planned
  retirement asset; estate or acquihire event extinguishes it
  unrecovered.
- **Recovery move**: For grantees over 50 or in high-risk relationship
  / company situations, treat AMT credit as a wasting asset with a
  finite life rather than a long-run equity-equivalent. Plan to crystallize
  it in years where regular tax > AMT can be forced.

---

## 2. Tax-clock-arbitrage framing

### 2.1 QSBS and §1061 are politically volatile; the framing's confidence in stable §422 bleeds across

- **Statement**: §422 (ISO mechanics) has been stable since 1981 and
  the framing's "start the clock and hold" confidence is calibrated
  there; §1202 (QSBS) per-issuer cap and 5-year period have been
  targeted in multiple legislative proposals since 2021 (and modified
  by OBBBA 2025), and §1061 has already moved 1y → 3y with further
  proposals pending. A 5-year plan that assumes today's rules hold at
  sale is bearing material policy risk the framing's voice doesn't
  signal.
- **Source evidence**: `community_profiles/tax-and-finance-professionals.md`
  Known-blindspot 4 ("Overconfident on stable IRC sections,
  underweighted on volatile ones"); `framings.md` §2 Excludes on QSBS
  political volatility.
- **Trigger**: Asker is being told to "early-exercise with 83(b) to
  start the QSBS clock" or to structure exit timing for §1202 treatment
  with > 18 months to go.
- **Failure mode**: Asker locks in cash outflow and concentration risk
  for a 5-year QSBS plan; Congress modifies §1202 in year 3 and the
  expected federal exclusion is recalculated downward 30-70%, no
  longer justifying the cash outlay.
- **Recovery move**: Run the same plan under three policy scenarios
  (status quo, modest tightening, repeal); proceed only if the modest-
  tightening case still clears a return threshold the asker would
  accept without the §1202 benefit.

### 2.2 Early-exercise advice requires plan-document permission the modal grantee doesn't have

- **Statement**: "Start the QSBS clock at grant via 83(b) on
  early-exercised unvested ISOs" assumes the company's plan permits
  early exercise — typically gated to employees 1-50 or the founder
  cohort. Rank-and-file readers at Series B+ companies usually cannot
  execute the framing's preferred move at all.
- **Source evidence**: `framings.md` §2 Excludes on early-exercise
  permission gating;
  `community_profiles/long-form-references.md` Known-blindspot 3 on
  company-level structural defects that invalidate textbook treatment
  (specifically early-exercise-permitted plans).
- **Trigger**: Asker is at headcount > ~50 or has joined post-Series B
  and is reading early-exercise + 83(b) advice from a founder-bloggers
  source.
- **Failure mode**: Asker spends weeks researching 83(b) mechanics,
  then discovers their plan document doesn't permit early exercise; by
  the time they pivot, the cheap-window opportunity is gone.
- **Recovery move**: Check the plan document FIRST (specifically: is
  early exercise permitted, what is the share-class structure, does
  the 80/20 split apply); if early exercise is not permitted, drop
  the QSBS-clock branch entirely and reason about the vested-only
  paths.

### 2.3 Acquihire scenarios force disqualifying dispositions that reset clocks across successor entities

- **Statement**: The "just hold for 5 years" summary doesn't capture
  that an acquihire in year 4 forces a short-window sale that's
  disqualifying for ISO purposes AND resets the QSBS clock across
  the successor entity (the acquirer is rarely a fresh-issuance
  C-corp under $50M gross assets). Holding-period plans built on the
  framing fail without warning at the most common bad outcome for
  early-stage equity.
- **Source evidence**: `framings.md` §2 Excludes on year-4
  disqualifying redemption;
  `community_profiles/hn-collective.md` typical-concern on acquihire
  reality (most "acquisitions" of struggling startups yield offer
  letter + retention grant, original equity worth zero).
- **Trigger**: Asker holds equity at a struggling startup (declining
  burn, single-customer dependency, missed-fundraise rumors) AND is
  reasoning in QSBS-clock terms about future exit timing.
- **Failure mode**: Acquihire announced at year 4.5, asker forced to
  accept new-grant-with-clawback-of-original; QSBS clock resets to
  zero on the new instrument, original AMT paid on now-worthless
  common.
- **Recovery move**: Discount the QSBS-eligible outcome by the base
  rate of acquihire-vs-IPO at the asker's stage (Carta data publishes
  this); decide whether the discounted-EV justifies the cash outlay,
  not the headline-EV.

### 2.4 The "start clocks early" frame ignores cash and AMT carrying cost

- **Statement**: Every clock the framing wants to start (LTCG-1y,
  ISO-2y-1y, QSBS-5y) has an opportunity cost equal to the cash
  outflow × the asker's risk-adjusted return on that cash for the
  holding period, plus the AMT carrying cost. The framing presents
  clocks as costless to start; the cost is the foregone diversified
  return on locked-up cash.
- **Source evidence**: `community_profiles/founder-engineer-bloggers.md`
  typical-concern on AMT exposure ("many people exercise without
  modeling the AMT hit and get a six-figure surprise tax bill");
  `framings.md` §3 Excludes on opportunity-cost-of-cash-held.
- **Trigger**: Asker's cash position is constrained, OR asker's
  alternative use of the cash (mortgage, S&P index, emergency fund)
  has a defined return.
- **Failure mode**: Asker exercises for the clock, foregoes 5 years
  of compounding on the $90k cash outlay (≈ $40-60k in opportunity
  cost at 8% real), and the equity ends below the after-tax breakeven
  on the diversified alternative.
- **Recovery move**: Compute the breakeven exit price that justifies
  exercising-now-vs-holding-cash; if the company is not likely to
  clear that exit price within the holding period, defer the exercise.

### 2.5 Step-up at death is the highest-leverage clock the framing rarely names

- **Statement**: Equity held to death receives a basis step-up that
  zeroes out all unrealized gain; the framing's clock-arbitrage logic
  treats this as a footnote when for grantees over 60 with no liquidity
  need it is often the dominant strategy (hold-to-death beats
  every-clock-optimized-sale by the income-tax savings on the basis
  reset).
- **Source evidence**: `framings.md` §2 Mental model line on
  "step-up at death" appearing only in vocabulary;
  `community_profiles/tax-and-finance-professionals.md` Known-blindspot
  3 (asymmetric death treatment under-named).
- **Trigger**: Asker is over 55, financially comfortable, has heirs,
  and is reasoning about LTCG vs §1202 vs exercise-timing for a
  concentrated position.
- **Failure mode**: Asker pays large clock-optimized capital-gains
  bills in the last decade of life to "harvest" gains that would have
  stepped up to zero on inheritance.
- **Recovery move**: For asker > 55 with non-binding liquidity needs,
  surface hold-to-death + Section 1014 step-up as the comparator
  baseline; clock-arbitrage strategies must beat it after estate-tax
  treatment to be worth executing.

---

## 3. Liquidity-preservation framing

### 3.1 Non-recourse exercise lending decouples exercise cost from personal cash

- **Statement**: The framing treats exercise cost as a personal-balance-
  sheet item against cash on hand; it ignores ESO Fund, Quid, EquityZen
  loans, and other non-recourse structures that fund exercise + AMT
  against the stock itself, with the lender taking the downside risk.
  For grantees who can pass diligence, the exercise-cash-is-personal-
  cash equation is false.
- **Source evidence**: `framings.md` §3 Excludes on non-recourse loan
  structures;
  `community_profiles/tax-and-finance-professionals.md` Known-blindspot
  5 on the "can't afford to exercise" trap.
- **Trigger**: Asker is being told to forfeit unexercised ISOs at the
  90-day PTE because the exercise + AMT exceeds their savings, AND
  the company is at Series C+ with credible exit timeline.
- **Failure mode**: Asker forfeits $50k-$500k of vested equity at the
  90-day window when a non-recourse loan would have financed the
  exercise with the lender taking the binary downside.
- **Recovery move**: At Series C+ with a credible exit window, evaluate
  non-recourse exercise lenders before forfeiting. Diligence cost is
  weeks, not days — start before the PTE clock starts.

### 3.2 "Build 12 months runway before exercising" is itself an opportunity-cost trade

- **Statement**: The framing's prudence rule treats cash-as-safety-
  buffer as costless; cash held for safety is cash not compounding,
  and at multi-year horizons the foregone diversified return often
  exceeds the downside of the exercise the runway-rule blocked.
- **Source evidence**: `framings.md` §3 Excludes on "build 12 months
  runway" as itself an opportunity-cost choice.
- **Trigger**: Asker is comparing exercise-now vs build-runway-first
  with a multi-year time horizon and a definable next-best use of
  the cash.
- **Failure mode**: Asker spends 18 months building runway, in which
  time FMV moves 3-5x, AMT bill triples, and the originally-attractive
  exercise window closes.
- **Recovery move**: Frame the choice in three-asset terms (equity
  exercise / cash buffer / diversified index) and pick the allocation
  that beats both extremes; rarely is all-cash or all-exercise the
  right answer.

### 3.3 The framing inverts at high-income brackets where cash on hand isn't the binding constraint

- **Statement**: For $400k+ TC earners, "personal balance sheet" is
  loose and "cash runway" is a slack constraint; the binding decisions
  are marginal-tax-bracket sequencing and concentration ratio, not
  liquidity. The framing's vocabulary actively misroutes high-earners
  toward decisions that solve a constraint they don't have.
- **Source evidence**: `framings.md` §3 Excludes on high-income earners
  outgrowing the framing;
  `community_profiles/founder-engineer-bloggers.md` typical-concern
  on AMT modeling at scale.
- **Trigger**: Asker reports TC > $400k, dual-income > $500k, or
  liquid net worth > $1M alongside an exercise / equity decision.
- **Failure mode**: High-earner spends mental cycles managing
  emergency-fund ratios while the actual decision (which RSU tranche
  to defer into a higher-bracket vest year) goes unattended.
- **Recovery move**: Above the $400k TC threshold, route to the
  concentration-risk and tax-clock-arbitrage framings instead;
  liquidity-preservation has decreasing marginal advice quality.

### 3.4 The prudence bias systematically misses the early-employee cheap window

- **Statement**: The cheapest window to exercise (early-employee, low
  strike, low FMV-strike spread, low AMT) is exactly when the asker
  has the least cash; the framing's prudence-default of "wait until
  you can afford it" passes through that window without flagging
  that the cost grows nonlinearly over time.
- **Source evidence**: `framings.md` §3 Excludes on prudence-bias
  under-recommending exercise at the cheap window;
  `community_profiles/founder-engineer-bloggers.md` typical-concern
  on 90-day PTE forfeiture mechanics.
- **Trigger**: Asker is in years 1-2 at an early-stage company with
  modest strike and modest FMV-strike spread, and is reasoning in
  "wait until I have more savings" terms.
- **Failure mode**: Asker waits 3 years; FMV moves 10x; the now-large
  spread makes the exercise + AMT 30x what it would have been;
  asker forfeits at PTE rather than write a $300k check.
- **Recovery move**: For year-1-2 employees at early-stage companies,
  evaluate early exercise + 83(b) explicitly — cash-light at this
  point and dominantly cheaper than any future exercise window.

### 3.5 Personal balance sheet ignores non-cash personal liabilities (dependents, mortgage, visa)

- **Statement**: The framing's "personal balance sheet" focuses on
  cash and obligations; it underweights non-cash personal-life
  liabilities — visa dependence (one-job risk), single-income family
  with kids, caregiver responsibilities — that make any forced
  illiquidity event from exercise structurally worse than the cash
  arithmetic suggests.
- **Source evidence**: `community_profiles/founder-engineer-bloggers.md`
  Known-blindspot 1 (visa-status mechanics) and 4 (demographic
  context — caregiver, dual-income, first-generation-professional
  cost).
- **Trigger**: Asker mentions H-1B status, dependents, sole income,
  or non-portable mortgage alongside a cash-intensive equity decision.
- **Failure mode**: Asker uses cash buffer for exercise, then loses
  job 4 months later; H-1B 60-day grace clock starts AND the buffer
  is gone, forcing acceptance of a worse next-offer at a discount
  to leverage.
- **Recovery move**: Stack the non-cash liabilities as additional
  required-runway months on top of the cash framework; the right
  buffer for a visa-dependent sole-earner with kids is 3-4x what the
  framing's generic answer produces.

---

## 4. Concentration-risk framing

### 4.1 Employee-shareholders have private information that flat-portfolio theory assumes away

- **Statement**: Treating employer stock as identically distributed
  with other public equities is the Markowitz default; an
  employee-shareholder sees roadmap, customer concentration, exec
  turnover, deal pipeline that change the risk distribution. The
  framing's "diversify out" advice ignores the information asymmetry
  that may justify either greater or lesser concentration than the
  generic answer.
- **Source evidence**: `framings.md` §4 Excludes on private-information
  asymmetry;
  `community_profiles/hn-collective.md` Known-blindspot 5 on anecdotes
  cited as if market structure is static (the inside view is real
  data the textbook framing discards).
- **Trigger**: Asker is an L5+ at a company with disclosable internal
  signals (declining new ARR, slipped product launches, exec
  resignations) reasoning purely from public-market portfolio theory.
- **Failure mode**: Asker reads "diversify" and waits to sell at LTCG,
  during which insiders sell on a 10b5-1 plan that asker would have
  reproduced if surfacing the inside view explicitly.
- **Recovery move**: Surface the "what do you know that the public
  market doesn't" question separately from the portfolio-math
  question; allow the inside-view adjustment to shift the
  concentration target up or down before applying the textbook bound.

### 4.2 At pre-IPO companies, "diversify out" is structurally impossible

- **Statement**: The framing's recommended action (sell to diversify)
  requires a liquidity market that doesn't exist at most private
  companies; the framing has no vocabulary for "concentration is your
  only option, manage on the qualitative side instead." Applying the
  diversification frame to a Series B holding produces guilt without
  action.
- **Source evidence**: `framings.md` §4 Excludes on early-stage
  impossibility;
  `community_profiles/carta-and-platform-data.md` Known-blindspot 5
  on per-employee mechanics where the "diversify" framing has no
  surface to land on.
- **Trigger**: Asker holds private-company equity below Series C with
  no tender or secondary market available, and is reasoning in
  Bessembinder / Markowitz terms.
- **Failure mode**: Asker accumulates anxiety about a concentration
  position they cannot exit, defers the actual decisions available
  (exercise timing, 83(b), insurance, role decision) because the
  active recommendation (sell) is impossible.
- **Recovery move**: Reframe to "what can I do given concentration is
  forced": evaluate disability / life insurance to hedge dependency
  risk, model exit scenarios at the position size (not as a sale
  target), make role decisions assuming the position stays concentrated.

### 4.3 The Bessembinder result samples random pickers, not inside cap-table residents

- **Statement**: Bessembinder's "50% of stocks underperform cash over
  10 years" is computed over random single-stock picks; employees
  aren't random pickers — they're inside the cap table. Whether the
  inside-cap-table base rate matches the all-cap-table base rate is
  the exact question the framing refuses to engage.
- **Source evidence**: `framings.md` §4 Excludes on Bessembinder's
  random-picker assumption.
- **Trigger**: Asker is being shown the Bessembinder statistic as a
  reason to sell employer equity, without the comparable inside-
  employee-cohort base rate.
- **Failure mode**: Asker sells based on a statistic that doesn't
  apply to their selection process; misses upside that inside
  employees at strong cohorts realize.
- **Recovery move**: Source an inside-employee outcome base rate
  (Carta exit statistics, YC outcome distributions) rather than
  using the all-stock base rate as the comparator; the inside-cohort
  number is the relevant prior.

### 4.4 Tax-aware rebalancing collides with §1091 wash-sale on ongoing RSU vests

- **Statement**: The framing's "tax-aware rebalance" assumes the sale
  isn't matched by a substantially-identical-security purchase within
  ±30 days; for FAANG employees with quarterly RSU vests at the same
  ticker, selling vested shares while new RSUs vest in the wash-sale
  window triggers §1091 disallowance the framing rarely names.
- **Source evidence**: `framings.md` §4 Excludes on wash-sale
  interaction with ongoing RSU vests;
  `community_profiles/carta-and-platform-data.md` Known-blindspot 3
  on tax content organized around forms rather than decisions.
- **Trigger**: Asker is at a public-co with quarterly RSU vest cadence,
  planning to sell concentrated employer position for diversification.
- **Failure mode**: Asker sells losses to harvest, RSUs vest within
  30 days, §1091 disallows the loss and shifts basis; the planned
  tax benefit evaporates without warning.
- **Recovery move**: Time sales to avoid the ±30-day RSU vest window;
  if vests are quarterly, the rebalancing windows are constrained to
  ~30-day stretches mid-quarter. Plan ahead.

### 4.5 The "20% concentration threshold" rule misses correlation-with-income risk

- **Statement**: The framing's 20%-of-net-worth concentration bound
  treats employer equity as a standalone asset; in fact employer
  equity correlates highly with the asker's wage income (both go to
  zero at company failure). The right concentration cap is far lower
  than 20% once correlated-income-risk is added.
- **Source evidence**: `community_profiles/reddit-tech-collective.md`
  typical-concern on RSU concentration and "got managed out … lost
  unvested cliff" narrative; `framings.md` §4 Mental model line on
  20% as the rule of thumb.
- **Trigger**: Asker holds > 15% of net worth in employer stock AND
  derives > 60% of income from that employer.
- **Failure mode**: Company has a bad quarter, asker is laid off AND
  the stock drops 40% simultaneously; both halves of the personal
  balance sheet decline together as one correlated event.
- **Recovery move**: For correlated wage + equity exposure, target
  concentration < 10% of net worth, not 20%; or buy explicit hedges
  (put options on the employer ticker for the wage-replacement
  amount) if the position is forced.

---

## 5. Dilution-math framing

### 5.1 SAFE-only seed companies break the priced-round dilution model

- **Statement**: The framing reasons about post-money ownership across
  priced rounds; for SAFE-only seed companies, post-conversion
  dilution is deferred and ambiguous until the next priced round
  resolves. The "model dilution per round" advice produces a number
  that doesn't apply to the asker's actual cap-table dynamics.
- **Source evidence**: `framings.md` §5 Excludes on SAFE-only
  ambiguity;
  `community_profiles/carta-and-platform-data.md` Known-blindspot 2
  on SAFE-only seed companies under-represented in benchmarks.
- **Trigger**: Asker joins a seed-stage company that has raised only
  SAFEs (no priced round yet) and is asking about effective ownership
  or dilution.
- **Failure mode**: Asker computes "0.5% of $20M = $100k" thinking
  in priced-round arithmetic; SAFEs convert at lower valuation caps
  on the next priced round and the asker's actual stake on conversion
  is 0.25-0.35%.
- **Recovery move**: Ask for the SAFE terms (valuation caps,
  discounts, MFNs) and model conversion at multiple next-priced-round
  scenarios; treat the headline 0.5% as a ceiling, not a number.

### 5.2 Stacked preference structures dwarf the headline "1× non-participating"

- **Statement**: The framing's vocabulary for preference stacks
  (participation caps, pay-to-play, side-letter MFNs, multi-round
  anti-dilution) is correct but under-applied; in soft-sale scenarios
  these stack into 50%+ of exit value going to preferred ahead of
  common. Asking "is it 1× non-participating?" without asking about
  the full stack misses the dominant variable.
- **Source evidence**: `community_profiles/matt-levine-school.md`
  Known-blindspot 4 ("Stops at the headline preference and skips the
  stacked legal stack"; "$200M sale with $180M of stacked preference
  can leave common with $20M, not the $40M the headline suggests");
  `framings.md` §5 Excludes on per-series participation caps.
- **Trigger**: Asker is evaluating an offer at a multi-round private
  company (Series C+) and asks about preference treatment.
- **Failure mode**: Asker accepts an offer reading "1× non-participating
  baseline" and discovers at exit that pay-to-play participation,
  anti-dilution ratchets across 3 rounds, and MFNs gave preferred
  ~80% of the headline.
- **Recovery move**: Request the COI (Certificate of Incorporation)
  and any side-letter MFNs in due diligence; pay an attorney $500-1000
  for a one-hour preference-stack model before signing.

### 5.3 Most employee outcomes are acquihire-driven; the framing optimizes for the priced-exit case

- **Statement**: The framing treats exit valuation as the analytical
  input; in the actual outcome distribution at venture-backed
  startups, acquihire is far more common than IPO, and at acquihire
  the headline number and the common-stock number diverge by 80%+.
  Optimizing dilution math against an assumed priced-exit is
  optimizing for the rare case.
- **Source evidence**: `community_profiles/hn-collective.md`
  typical-concern on acquihire reality (original equity worth zero);
  `community_profiles/vc-blogosphere.md` Known-blindspot 3 on
  survivorship bias toward winning portfolios;
  `framings.md` §5 Excludes on acquihire-vs-headline divergence.
- **Trigger**: Asker is at a Series A-C company, reasoning about
  expected equity value at a $500M+ exit, without acknowledging the
  acquihire-vs-priced-exit distribution.
- **Failure mode**: Asker accepts the offer based on the "if it works"
  EV; company acquihires, asker gets new-grant at acquirer, original
  equity zeros out, the headline math becomes a footnote.
- **Recovery move**: Discount the priced-exit EV by the published
  base rate of acquihire-vs-IPO at the asker's stage; the
  base-rate-weighted EV is the right comparator.

### 5.4 Refresher-or-die dynamics produce a discontinuity per-round arithmetic obscures

- **Statement**: Per-round dilution arithmetic gives a smooth curve;
  in practice non-refreshed employees at Series C drift to < 0.05%
  on a path that suddenly forks at refresh-or-not. The framing
  doesn't model the refresher event as the dominant variable in
  late-stage employee outcomes.
- **Source evidence**: `framings.md` §5 Excludes on refresher-or-die
  dynamics;
  `community_profiles/vc-blogosphere.md` typical-concern on
  refreshers ("early employees who don't get refreshed get diluted
  to insignificance by Series C; VCs know this and budget for it;
  employees don't ask");
  `community_profiles/carta-and-platform-data.md` Known-blindspot 1
  on under-reported refresher-gap rates.
- **Trigger**: Asker is at year 2-3 of a late-stage private company
  and is reasoning about projected ownership at exit purely by
  dilution arithmetic.
- **Failure mode**: Asker plans on 0.4% effective stake; doesn't ask
  for refresher; gets 25% the refresher their peer who asked got;
  ends at 0.15% over the next 2 years.
- **Recovery move**: Treat the refresher conversation as the dominant
  cap-table event for the asker between now and exit; schedule it,
  prepare for it (market data, BATNA), don't wait to be offered.

### 5.5 Pool top-ups timed pre-priced-round dilute existing employees, not the incoming investor

- **Statement**: The framing names "pool refresh" but doesn't make
  vivid that pre-money pool top-ups dilute existing shareholders
  (founders + employees) while leaving the incoming investor
  un-diluted — this is the VC's negotiation lever and the asker's
  hidden 5-15% dilution per round.
- **Source evidence**: `community_profiles/vc-blogosphere.md`
  typical-concern on option-pool sizing pre-money ("VCs negotiate to
  expand the pool pre-money, which dilutes existing shareholders
  but not the incoming investor");
  `framings.md` §5 Mental model line on pool refreshes.
- **Trigger**: Asker is at a company about to close a priced round
  and is reasoning about expected ownership change.
- **Failure mode**: Asker models 20% round dilution; actual dilution
  is 30% because the new investor required a 10% pool refresh
  pre-money; asker's stake drops 50% more than expected.
- **Recovery move**: When asking about an upcoming round, ask
  separately about the pool refresh size and whether it's pre-money
  or post-money; the pre-money pool is the asymmetric dilution
  vector.

---

## 6. Cliff-arithmetic framing

### 6.1 The employer can re-time perf cycles, layoff dates, and PIPs around cheap-side-of-vest

- **Statement**: The framing treats vesting events as exogenous
  calendar facts; in practice the employer can re-time perf cycles,
  layoff dates, and PIP starts to land on the cheap side of a vest.
  The framing's own Decision 7 reasoning (PIP-as-managed-exit) is
  oddly under-applied to its own scenarios.
- **Source evidence**: `framings.md` §6 Excludes on employer re-timing;
  `community_profiles/reddit-tech-collective.md` typical-concern on
  cliff timing around layoff rumors and PIP as soft termination.
- **Trigger**: Asker is approaching a vesting event AND there are
  rumors of perf-review changes, org reshuffles, layoffs, or PIP
  initiations.
- **Failure mode**: Asker plans for the upcoming vest, employer
  re-times the perf cycle to land PIP placement two weeks before
  vest, asker exits with zero from the next tranche.
- **Recovery move**: Read the perf-cycle calendar alongside the vest
  calendar; if they're suspiciously aligned, accelerate the
  conversation with manager (or accelerate the job search) rather
  than passively waiting.

### 6.2 Parental and medical leave inside a cliff don't extend the cliff in most plans

- **Statement**: Most equity plans do not extend the cliff for
  protected leave; the framing's "wait for the cliff" advice can
  route a new parent or medical-leave employee into months of unpaid
  cliff-stretch that didn't exist in the modeled timeline. The
  framing's symmetry assumption (calendar advances independent of
  life events) is plan-document false.
- **Source evidence**: `framings.md` §6 Excludes on parental leave
  inside a cliff;
  `community_profiles/founder-engineer-bloggers.md` Known-blindspot 4
  on caregiving-leave-during-cliff trap.
- **Trigger**: Asker is taking or planning protected leave (parental,
  medical, FMLA) within ±6 months of a vesting cliff.
- **Failure mode**: Asker assumes "I'm still vesting"; plan document
  pauses vesting on unpaid leave OR cliff doesn't extend, asker
  loses a quarter of expected equity AND returns from leave to
  unfamiliar comp.
- **Recovery move**: Pull the plan document's leave provisions
  BEFORE leave starts; if vesting pauses, time the leave to maximize
  vested-on-departure value (e.g., return briefly after leave to vest
  the next tranche before quitting).

### 6.3 At FAANG with quarterly + stacked refreshers, "next vest" misframes the decision

- **Statement**: For golden-handcuffs FAANG holders with quarterly
  cadence and refresher stacking, the next-vest tranche is small
  (~$30k); the binding decision is the *trailing* unvested portfolio
  across multiple grants. The framing's vocabulary points at the next
  $30k while the decision sits on the $400k unvested stack.
- **Source evidence**: `framings.md` §6 Excludes on FAANG quarterly
  vest cadence;
  `community_profiles/reddit-tech-collective.md` mental-model line on
  TC as `base + bonus + equity/vest_years`.
- **Trigger**: Asker has been at a FAANG 3+ years with refresher
  stacking and is reasoning about quitting in terms of "next vest".
- **Failure mode**: Asker waits for next $30k tranche, gets it,
  re-anchors on the next $30k tranche, never decides; the trailing
  unvested decays as new opportunity windows close.
- **Recovery move**: Compute total unvested value across all grants
  and the implied months-to-zero-unvested glide path; that is the
  decision horizon, not the next tranche.

### 6.4 Extended PTE windows invalidate the 90-day arithmetic without changing the vocabulary

- **Statement**: The framing's 90-day PTE arithmetic is anchored to
  ISO statutory limits; extended PTE windows (Quora, Pinterest,
  Coinbase, many post-2018 unicorns offer 7-10 year windows) and
  early-exercise-with-83(b) regimes invalidate the calendar
  arithmetic without changing the vocabulary. The framing's
  "exercise within 90 days" advice is wrong by years at companies
  that revised their plans.
- **Source evidence**: `framings.md` §6 Excludes on extended PTE
  windows;
  `community_profiles/hn-collective.md` Known-blindspot 5 on
  anecdotes cited as if market structure is static
  (90-day-PTE assumption applied to plans revised in 2023);
  `community_profiles/long-form-references.md` Known-blindspot 3 on
  company-level plan-document specifics.
- **Trigger**: Asker is being told "exercise within 90 days of
  leaving" without anyone checking the plan document for extended
  PTE.
- **Failure mode**: Asker scrambles to write the AMT check in 90
  days when their plan actually gives them 5 years; cash-bind
  forces forfeiture or non-recourse loan that wasn't necessary.
- **Recovery move**: Pull the plan document and the individual grant
  notice BEFORE acting on the 90-day default; extended PTE shifts
  the entire exercise calendar.

### 6.5 Single-trigger acceleration is rare but its assumed presence skews advice

- **Statement**: The community confuses single-trigger and
  double-trigger acceleration; single-trigger (acceleration on
  acquisition alone) is rare in 2026 plans, double-trigger
  (acquisition + involuntary termination within X months) is the
  norm. Advice that assumes single-trigger ("at acquisition my
  unvested vests") leaves asker exposed to the involuntary-
  termination condition.
- **Source evidence**: `community_profiles/reddit-tech-collective.md`
  typical-concern on cliff timing ("Single-trigger acceleration is
  rare; people miss this");
  `community_profiles/founder-engineer-bloggers.md` typical-concern
  on acceleration clauses being negotiable.
- **Trigger**: Asker is reasoning about acquisition outcomes assuming
  unvested equity will accelerate at deal close.
- **Failure mode**: Acquisition closes, asker is retained, expects
  acceleration, doesn't get it; then is laid off 13 months later
  AFTER the double-trigger window expired.
- **Recovery move**: Confirm whether the grant has single- or
  double-trigger language AND the post-close termination window
  (typically 12-18 months); if double-trigger, the acquisition
  doesn't accelerate anything unless the second trigger fires.

---

## 7. Retention-leverage framing

### 7.1 H-1B and green-card status collapse the "always negotiate" advice

- **Statement**: The framing assumes the asker can credibly walk away
  from the negotiation; for an H-1B holder 3 years into a green-card
  process whose I-140 hasn't crossed the AC21 portability threshold,
  "always negotiate, worst they can say is no" is structurally wrong
  and the framing has no vocabulary for status-bounded leverage.
- **Source evidence**: `community_profiles/founder-engineer-bloggers.md`
  Known-blindspot 1 (visa-status mechanics treated as someone else's
  problem); `framings.md` §7 Excludes on H-1B/AC21.
- **Trigger**: Asker mentions visa status (H-1B, O-1, EAD, GC pending)
  alongside a negotiation question.
- **Failure mode**: Asker counters aggressively; employer rescinds;
  asker has < 60 days to find another H-1B-sponsoring employer or
  fall out of status; accepts the next offer at a discount because
  the cap-subject re-filing risk is binding.
- **Recovery move**: For visa-dependent askers, treat the existing
  offer as the BATNA and negotiate from below it (smaller asks: signon,
  start date, level-mid vs level-high) rather than risking
  rescission; reserve aggressive counters for post-GC stage when
  walking is actually possible.

### 7.2 Symmetric-reception assumption contradicts the empirical reception data

- **Statement**: The framing assumes the same counter-offer produces
  the same hiring-committee reception regardless of asker
  demographics; the empirical evidence (Bowles HBR 2007 lineage,
  replicated at FAANG) shows women and Black IC candidates who
  counter at the same rate as white men are perceived as more
  aggressive. The framing's "always counter" advice has a
  demographic-dependent cost the framing doesn't price.
- **Source evidence**: `community_profiles/founder-engineer-bloggers.md`
  Known-blindspot 4 (demographic context affecting bargaining
  outcomes);
  `framings.md` §7 Excludes on Bowles 2007 line.
- **Trigger**: Asker is from a demographic shown to face asymmetric
  reception, is being advised to apply maximum-leverage tactics.
- **Failure mode**: Asker counters per the playbook, gets the dollar
  lift but is perceived as "aggressive" by the hiring committee,
  loses internal promotion velocity AND/OR project-allocation
  preference in year 1.
- **Recovery move**: Pair leverage tactics with relationship framing
  ("I want to make sure this is a long-term fit at a level we both
  feel is right"); the dollar outcome can be preserved while
  reducing the perception cost.

### 7.3 Org-design fragility evaporates "load-bearing" leverage

- **Statement**: The framing names "load-bearing on a shipping
  project" as a leverage source; for senior managers in re-org-prone
  product areas, this leverage evaporates when the project is killed
  in an exec swap. The framing reasons about individual leverage
  without modeling organizational fragility.
- **Source evidence**: `framings.md` §7 Excludes on org fragility;
  `community_profiles/founder-engineer-bloggers.md` Known-blindspot 3
  on EM/director gaps ("org-design risk — your direct reports get
  reorged out from under you").
- **Trigger**: Asker is a manager / director planning leverage-based
  comp negotiation at a company with recent exec changes, missed
  fundraise, or product-portfolio reshuffles.
- **Failure mode**: Asker negotiates from "I'm load-bearing on
  $project"; new VP joins 3 months later; $project killed; leverage
  source disappears mid-cycle.
- **Recovery move**: Diversify leverage sources before negotiating
  (multiple-project criticality, market BATNA, retention precedent
  in adjacent skip-levels) when org fragility is high.

### 7.4 Aggressive-negotiation tactics carry multi-year promotion-velocity costs

- **Statement**: Companies pattern-match aggressive signing-bonus
  negotiation as a sign of likely retention problems; the framing's
  tactic that maximizes signing-bonus dollar can degrade
  post-signing promotion velocity and OKR-bandwidth allocation, a
  multi-year cost the single-transaction framing doesn't price.
- **Source evidence**: `framings.md` §7 Excludes on multi-year
  pattern-match cost; reinforced by
  `community_profiles/founder-engineer-bloggers.md` mental model
  on counterparty optimization.
- **Trigger**: Asker is being coached to push hard for an extra
  $20-50k signon at a company they expect to stay 3+ years.
- **Failure mode**: Asker gets the $30k; first perf cycle they're
  in the "ROI watch" cohort because the recruiter flagged them as
  high-cost-hire; promotion deferred 6 months; cumulative TC delta
  is negative over the 3-year horizon.
- **Recovery move**: At long-tenure-intent companies, prioritize
  level + equity refresh negotiation (recurring) over signon
  (one-shot); single-shot maximization at signing is the wrong
  optimization target.

### 7.5 First-time negotiators and non-tenured ICs lack the symmetric counterparty knowledge

- **Statement**: The framing's "the company has done this a thousand
  times" asymmetry default acknowledges the gap but doesn't help an
  asker close it; what the recruiter is actually incentivized for
  (signed offers per quarter, not TC) and the hiring-manager's level
  budget remain opaque to the asker. The framing names the asymmetry
  but offers no information-acquisition path.
- **Source evidence**: `community_profiles/reddit-tech-collective.md`
  Known-blindspot 5 (employer-side optimization treated as
  adversarial rather than modeled).
- **Trigger**: Asker is in first 1-2 industry negotiations OR is
  negotiating with no recruiter / TC anchor data.
- **Failure mode**: Asker negotiates blind, anchors low, accepts
  the first counter, leaves $30-80k on the table because the
  recruiter's quarterly quota incentive (which the asker could have
  exploited by waiting one extra week) was invisible.
- **Recovery move**: For first-time negotiators, surface what the
  counterparty wants ("the recruiter needs the signed offer this
  quarter, so the closer the calendar comes to quarter-end the
  faster their concession curve") as actionable intel, not abstract
  asymmetry.

---

## 8. Severance-leverage framing

### 8.1 Post-termination decision quality is empirically poor

- **Statement**: The framing's "take your time, push back" advice
  assumes the asker has the emotional bandwidth to negotiate
  during a layoff; financial-decision research on stress-induced
  narrowing shows post-termination decision quality is empirically
  poor. The advice is actively harmful for a sole-income earner
  with mortgage stress.
- **Source evidence**: `framings.md` §8 Excludes on emotional-
  bandwidth assumption;
  `community_profiles/founder-engineer-bloggers.md` Known-blindspot
  4 on demographic context (sole-earner, first-generation-
  professional cost).
- **Trigger**: Asker is in active layoff response, with
  high-stress life conditions (sole earner, dependents, recent
  illness, mortgage > 40% of TC).
- **Failure mode**: Asker tries to negotiate under stress, makes a
  worse decision than the original (signs on principle without
  reading clauses, OR refuses to sign and loses both severance and
  pursued claim).
- **Recovery move**: Surface a structural alternative: ask for a
  one-week extension on the consideration window, hire an
  employment attorney for a fixed-fee one-hour consult ($300-600),
  delegate the negotiation rather than running it personally under
  stress.

### 8.2 Settlement-value-of-claim math is mostly a bluff under at-will employment

- **Statement**: At-will employment baseline makes most "settlement
  value of claim" calculations a bluff; conversely, for retaliation
  / discrimination claims with concrete documentation, the framing
  under-prices the counter-leverage (a pro se Title VII charge is
  free to file and expensive for the employer to defend). The
  framing's symmetric treatment misses both directions.
- **Source evidence**: `framings.md` §8 Excludes on at-will
  vs claims-leverage asymmetry.
- **Trigger**: Asker is weighing severance package terms with no
  documented protected-activity claim, OR with strong concrete
  evidence of one.
- **Failure mode**: At-will asker over-leverages a non-existent
  claim and gets rescinded offer; claim-strong asker under-
  leverages and accepts standard package when EEOC charge would
  have produced 2-3x.
- **Recovery move**: Triage the situation: at-will + no documented
  claim → accept standard package terms, negotiate non-cash; at-will
  + concrete documented claim → consult employment attorney about
  filing-before-signing leverage.

### 8.3 Trailing-vest requests often require non-standard board action that gets refused on principle

- **Statement**: The framing treats trailing-vest and accelerated-
  vest as standard negotiation items; in practice most ISO plans
  prohibit post-termination vesting and the request forces a
  non-standard board action the employer often refuses on principle
  (precedent-setting cost). The framing's "ask for it" advice has a
  meaningful refusal probability the framing doesn't name.
- **Source evidence**: `framings.md` §8 Excludes on plan-document
  prohibitions on post-termination vesting;
  `community_profiles/long-form-references.md` Known-blindspot 3 on
  plan-document specifics that invalidate textbook treatment.
- **Trigger**: Asker is being advised to ask for accelerated or
  trailing vest as a severance term.
- **Failure mode**: Asker leads with the trailing-vest ask;
  employer refuses on principle; mood turns adversarial; cash
  severance comes in lower than the no-ask baseline.
- **Recovery move**: Read the plan document first; if
  post-termination vesting is plan-prohibited, do not lead with this
  ask. Reserve it for situations where the plan permits but the
  default offer doesn't include.

### 8.4 Carta / Sequoia One bundled-binary signing UX collapses clause-by-clause negotiation

- **Statement**: The framing's clause-by-clause discipline assumes
  the asker can mark up the document; platforms like Carta and
  Sequoia One present "Accept" or "Decline" as the only options
  in the UX, and the framing's negotiation move has no surface
  to land on until the asker gets a partner-attorney on the phone.
- **Source evidence**: `framings.md` §8 Excludes on bundled-binary
  signing UX.
- **Trigger**: Asker receives the severance package via Carta,
  Sequoia One, or similar platform with binary accept-or-decline UI.
- **Failure mode**: Asker accepts the binary UX prompt without
  realizing the underlying document is negotiable; signs as
  presented.
- **Recovery move**: Treat the platform UX as a friction-not-a-rule;
  email the HR contact or company counsel directly with
  redlines/asks; the platform exists to streamline the standard
  path, not to enforce it.

### 8.5 The waiver of unvested equity is the largest negotiable item that goes uncountered

- **Statement**: The framing names the bundled clauses but rarely
  flags that the waiver of unvested equity is often the largest
  dollar item in the package; askers counter on cash and miss the
  larger waiver line.
- **Source evidence**: `framings.md` §8 Mental model line ("waiver
  of unvested equity is often the largest negotiable item that
  goes uncountered").
- **Trigger**: Asker is reviewing severance package terms that
  include any forfeiture-of-unvested clause.
- **Failure mode**: Asker counters on the cash severance ($30k →
  $45k), accepts the unvested waiver, loses $200k+ of unvested
  RSUs that could have been partially preserved or sold to acquirer
  at fair value.
- **Recovery move**: Always evaluate the unvested-equity waiver as
  the first dollar item to counter; even a 25% partial preservation
  often dwarfs the cash-severance counter.

---

## 9. Non-compete-enforceability framing

### 9.1 Choice-of-law puzzles defeat the "check your state" shorthand

- **Statement**: A CA-resident remote employee of a NY-incorporated
  employer working with TX customers has three plausible laws to
  apply, and the contract often picks DE governing law to muddy
  further. The "check your state" shorthand collapses the multi-
  jurisdiction reality the framing's own complexity warning should
  surface.
- **Source evidence**: `framings.md` §9 Excludes on choice-of-law
  puzzle.
- **Trigger**: Asker is a remote employee whose state of residence,
  state of work, employer state of incorporation, and customer
  states differ.
- **Failure mode**: Asker assumes CA §16600 voids the non-compete;
  employer files for injunction in NY or DE invoking
  choice-of-law clause; the asker's CA-resident shorthand was
  wrong and they're now in litigation in the wrong forum.
- **Recovery move**: Read the contract's governing-law and forum-
  selection clauses; identify the worst-case forum for enforcement
  and check that state's rule, not the residence state's; consider
  declaratory action in the friendly forum if leaving.

### 9.2 Defense cost of an unenforceable non-compete can dwarf its value

- **Statement**: The cost of defending an unenforceable non-compete
  (attorney fees pre-12-day TRO hearing, lost income during
  "evaluation whether to sue") can dwarf the value of the new job;
  the framing's correct-on-the-law conclusion can route the asker
  into an expensive practical loss.
- **Source evidence**: `framings.md` §9 Excludes on defense cost gap;
  `community_profiles/long-form-references.md` Known-blindspot 2 on
  decision-shaped questions where the mechanics are correct but the
  asker walks away without knowing which button to press.
- **Trigger**: Asker has a void-or-overbroad non-compete and is
  joining a competitor; ex-employer has a litigious history or
  named the asker specifically in a cease-and-desist.
- **Failure mode**: Asker takes the new job confident the non-compete
  is unenforceable; ex-employer files anyway; asker pays $20-60k
  in defense + lost income during weeks of legal uncertainty,
  even though they eventually win.
- **Recovery move**: When the ex-employer has named the asker, get
  a declaratory-judgment action filed first in the friendly forum,
  OR settle for non-cash carveouts (tolling letter, customer carve-
  out) that remove the threat before joining.

### 9.3 Trade-secret and inevitable-disclosure doctrines route around voided non-competes

- **Statement**: The framing's "check enforceability map" doesn't
  catch DTSA / state UTSA claims that survive in CA where
  non-competes don't; "inevitable disclosure" doctrines can produce
  injunctive relief even in §16600 states. The voided non-compete
  is not the end of the story.
- **Source evidence**: `framings.md` §9 Excludes on trade-secret
  routing.
- **Trigger**: Asker is moving to a direct competitor and holds
  sensitive proprietary information (customer lists, roadmaps,
  source code, training-data, model weights).
- **Failure mode**: Asker assumes CA-resident protection is
  sufficient; ex-employer files DTSA / inevitable-disclosure suit;
  injunction blocks asker from working in the role they were hired
  for, regardless of the non-compete being void.
- **Recovery move**: Audit what the asker took / would
  "inevitably disclose" (clean room departure, attorney-supervised
  laptop wipe); negotiate a non-objection letter from the
  ex-employer before joining; refuse roles that put asker
  competitively-adjacent to specific projects they recently led.

### 9.4 Customer non-solicit and employee non-solicit survive where non-competes don't

- **Statement**: The framing covers leave-employer non-competes well
  but under-addresses customer non-solicit and employee non-solicit
  clauses, which survive in CA where non-competes don't (under
  §16600 case-law splits). These are the more enforceable cousins
  the framing skips.
- **Source evidence**: `framings.md` §9 Excludes on customer /
  employee non-solicit survival.
- **Trigger**: Asker's contract has solicitation restrictions even
  if the non-compete is void; asker is moving to a competitor with
  overlapping customer or talent pool.
- **Failure mode**: Asker assumes CA voids "all that stuff"; takes
  the new role; recruits ex-colleagues or contacts former customers;
  faces a §17200 unfair-competition claim that survives §16600
  scrutiny.
- **Recovery move**: Read non-solicit clauses separately from
  non-compete; map them to the new-role activities; redline or
  carve out specific known customers / hires before signing.

### 9.5 FTC non-compete rule status is a moving target the framing's voice doesn't track

- **Statement**: The framing's vocabulary names the FTC rule and
  its vacatur but the underlying landscape is moving — appeal in the
  5th Circuit, state-level FTC-style bans (MN 2023, MA Garden Leave
  changes, CO 2022, WA 2020). The framing's "FTC rule vacated, pre-
  FTC patchwork is back in force" anchor is increasingly incomplete.
- **Source evidence**: `framings.md` §9 Mental model on FTC rule
  vacated; `community_profiles/long-form-references.md`
  Known-blindspot 1 on edition cadence lagging rule changes
  inside the publication cycle.
- **Trigger**: Asker's situation depends on rule status as of
  this quarter (not the publication date of the source-view notes).
- **Failure mode**: Asker reads a 2024 analysis that assumes FTC
  vacatur stands; intermediate ruling shifts; advice is stale
  within months.
- **Recovery move**: Date-stamp the source consulted and require a
  current-quarter check on FTC and state-level non-compete law
  before relying on the framing's conclusions for an active
  decision.

---

## 10. Contribution-asymmetry framing

### 10.1 Pre-PMF cofounder breakups produce IP / company-name / investor-relationship fights the framing skips

- **Statement**: The framing assumes ongoing collaboration plus
  vesting as the trust mechanism; misses the case where the
  relationship sours pre-product-market-fit and the cap table
  becomes a divorce — at which point IP ownership, the company
  name, and existing investor relationships are all contested in
  ways the equity-split framing doesn't address.
- **Source evidence**: `framings.md` §10 Excludes on pre-PMF
  cofounder divorce.
- **Trigger**: Asker is in a cofounder relationship pre-PMF where
  trust signals are degrading (founder-A working unilaterally,
  founder-B questioning core decisions, equity-split debates
  becoming recurrent).
- **Failure mode**: Cofounders split, both claim founder status,
  IP assignment unclear, investors uncertain who to back; company
  effectively dies during the dispute.
- **Recovery move**: Sign a founders' breakup agreement at
  formation that names IP ownership, name rights, investor primary-
  contact, and a buyout formula triggered by cofounder departure;
  this is the framework version of vesting that the equity-split
  alone doesn't supply.

### 10.2 Capital contribution doesn't fit cleanly into "forward work" arithmetic

- **Statement**: When one cofounder funds the company's first 18
  months from savings, the contribution is structurally different
  from "forward work" units; the framing routes this through
  "convertible note from a founder" and loses the human dynamic of
  the funder having taken real personal risk that the equal-split
  template doesn't reward.
- **Source evidence**: `framings.md` §10 Excludes on capital
  contribution mis-routing.
- **Trigger**: One cofounder is bankrolling the venture from
  personal savings while the other(s) trade salary for equity.
- **Failure mode**: 50/50 split executed; funder feels increasingly
  resentful as runway burns; resentment surfaces at fundraise,
  damaging investor confidence.
- **Recovery move**: Separate the capital contribution into a
  convertible note (with market interest and cap) AND give the
  funder a forward-work-equivalent equity slice; this is two
  instruments, not one negotiation about percentage.

### 10.3 International cofounder pairs face country-specific issues the US default skips

- **Statement**: UK BSPCE-equivalent rules, Indian FEMA restrictions
  on foreign-resident shareholders, French BSPCE eligibility cliffs,
  Israeli §102 trustee track — these all matter for cofounder pairs
  with non-US members and the US-default framing silently glides
  over them.
- **Source evidence**: `framings.md` §10 Excludes on international
  cofounder pairs;
  `community_profiles/founder-engineer-bloggers.md` Known-blindspot
  2 on non-US comp structure (UK EMI, German dry-tax, BSPCE,
  Israeli §102) being gestured at, not modeled;
  `community_profiles/long-form-references.md` Known-blindspot 4 on
  the corpus being US-Delaware by construction.
- **Trigger**: Cofounder pair includes a non-US resident, OR plans
  to operate primarily outside the US, OR holds dual citizenship
  affecting tax treaty treatment.
- **Failure mode**: Standard US equity split executed via DE
  C-corp; non-US cofounder hits tax treatment that wipes out their
  effective stake (dry-tax on vest in DE; §102 trustee-track
  ineligibility in IL; FEMA reporting failure in IN).
- **Recovery move**: Engage a tax attorney in EACH cofounder's
  residence jurisdiction before signing the equity split; the
  effective economic outcome can be radically different from the
  on-paper percentage.

### 10.4 The "idea premium" anchor is from survivorship retrospectives

- **Statement**: The 5-10% idea-premium anchor comes from
  successful-company retrospectives — survivorship bias. The
  premium that *failed* cofounder relationships had at formation
  is unknown and presumed higher (the breakup is what produced the
  data the literature samples). The framing's "5-10% is the cap"
  number is the post-success number, not the at-formation prior.
- **Source evidence**: `framings.md` §10 Excludes on survivorship-
  biased idea-premium anchor;
  `community_profiles/vc-blogosphere.md` Known-blindspot 3 on
  survivorship bias toward winning portfolios.
- **Trigger**: Asker is forming a cofounder pair where one party
  is asserting an "I had the idea" premium > 10%.
- **Failure mode**: The 5-10% literature cap is cited as gospel;
  the higher-premium-asker walks because they believe the equal-
  split data is from companies-like-theirs (when in fact those are
  companies that survived their higher-premium starting position).
- **Recovery move**: Acknowledge the literature is biased toward
  outcomes-we-can-observe; negotiate the cofounder split on
  forward-work-fit grounds (not historical-norm grounds) and let
  the team's own conviction drive the number.

### 10.5 Reverse-vesting acceleration on involuntary removal is the most-skipped trust mechanism

- **Statement**: Founder vesting cliffs and acceleration on
  involuntary removal (the "for-cause vs not-for-cause termination
  of a founder" line) are named in vocabulary but routinely skipped
  in actual implementation. The framing's "marriage's no-fault
  divorce protocol" analogy is correct but cofounders rarely
  execute the protocol fully.
- **Source evidence**: `framings.md` §10 Mental model line on
  reverse-vesting + acceleration; reinforced by
  `community_profiles/vc-blogosphere.md` typical-concern on
  founder vesting + reverse-vesting as company-stability signal.
- **Trigger**: Cofounder pair is incorporating without legal counsel
  AND debating equity percentage in isolation from vesting / removal
  terms.
- **Failure mode**: 50/50 split with no vesting executed; one
  founder leaves at month 9; departing founder retains 50% of
  cap table with no recourse from remaining founder.
- **Recovery move**: Pair the equity-split decision with a
  reverse-vesting schedule with acceleration-on-not-for-cause-
  removal; the equity number without the vesting structure is
  half a decision.

---

## 11. Asymmetric-bet-on-team framing

### 11.1 "Exceptional team" is unfalsifiable when the asker is already leaning in

- **Statement**: The framing's "if the team is exceptional, take it"
  advice is indistinguishable from confirmation bias when the asker
  is already inclined to join. It provides no falsifiable rejection
  criterion for "exceptional."
- **Source evidence**: `framings.md` §11 Excludes on unfalsifiability;
  `community_profiles/vc-blogosphere.md` Known-blindspot 3 on
  survivorship-biased public VC writing.
- **Trigger**: Asker is already enthusiastic about a team and is
  seeking external validation for accepting a below-market offer.
- **Failure mode**: Asker reads "if exceptional, take it"; treats
  their own enthusiasm as evidence of exceptional-ness; accepts
  a comp cut for a team that is good-not-exceptional.
- **Recovery move**: Force the asker to write down a
  pre-registered rejection criterion: "I would walk if the team
  failed test X, Y, Z." If they can't name a credible failure mode,
  the assessment is biased — ask a skeptical second opinion before
  signing.

### 11.2 Employee payoff is bounded by grant + dilution; the fund-level power law doesn't transfer

- **Statement**: Power-law outcomes are real at the fund level (the
  VC bet); the employee's payoff is bounded by grant size, vesting,
  dilution path. The fund-level math (1 in 100 → 100x) doesn't
  transfer to the employee whose grant is 0.1% of the company.
- **Source evidence**: `framings.md` §11 Excludes on fund-vs-employee
  power-law gap;
  `community_profiles/vc-blogosphere.md` Known-blindspot 1
  (underweights employee-level tax timing because partnership tax
  model doesn't apply to W-2 grantees).
- **Trigger**: Asker is being shown power-law statistics ("top 1%
  generate 95% of returns") as a reason to join a high-variance
  early-stage company.
- **Failure mode**: Asker accepts the framing's bet; even in the
  outlier-outcome scenario, their 0.1% × $2B exit × (1 - preference
  stack) × (1 - dilution) is $400k pre-tax — material but not
  fund-level upside.
- **Recovery move**: Translate the fund-level statistic into
  employee terms: what does the asker's 4-year economic outcome
  look like in the top 5% scenario, not the fund's? Compare against
  the no-bet alternative on the same horizon.

### 11.3 Opportunity cost (the foregone FAANG path) is named but rarely modeled

- **Statement**: The framing names opportunity cost in passing but
  rarely models it. A foregone $500k TC × 4 years = $2M of after-tax
  cash + retirement contributions + diversified portfolio
  compounding. The "team is the asset" bet has to clear this
  benchmark to be EV-positive.
- **Source evidence**: `framings.md` §11 Excludes on
  opportunity-cost-not-modeled.
- **Trigger**: Asker is choosing between a top-tier FAANG offer and
  a Series A startup, with the startup pitched as "asymmetric bet on
  the team."
- **Failure mode**: Asker takes the startup; 4 years later it's
  acquihired at $0 common payout; opportunity cost over the period
  is $2-3M (pre-tax) plus career-velocity differential.
- **Recovery move**: Build the opportunity-cost number explicitly:
  4-year after-tax cash, RSU vesting at the foregone employer,
  401k/IRA compounding, diversified portfolio gains. The startup
  bet must clear this floor in expected outcome, not in
  best-case outcome.

### 11.4 Survivor voice dominates the public corpus

- **Statement**: The people writing the "join the great team" essays
  are the ones whose great teams worked. The cohort of equally-
  thoughtful asker-bettors whose great teams quietly hit the wall
  at Series B don't produce the same volume of post-hoc
  rationalization content. The framing's voice is structurally
  biased.
- **Source evidence**: `framings.md` §11 Excludes on survivorship
  voice;
  `community_profiles/hn-collective.md` Known-blindspot 1
  (top-comment selection bias mistaken for community consensus);
  `community_profiles/vc-blogosphere.md` Known-blindspot 3
  (survivorship toward winning portfolios).
- **Trigger**: Asker is reading exclusively from successful-founder
  essays, "I joined Stripe in 2014" stories, retrospective YC
  alumni interviews.
- **Failure mode**: Asker calibrates probability of outlier
  outcome upward based on the publishable-stories sample, not the
  full population.
- **Recovery move**: Seek out the failed-team retrospectives where
  available (post-mortems, "lessons from killing my startup"
  posts); calibrate the prior against both sides of the
  distribution.

### 11.5 The "learning rate" claim isn't separable from career velocity

- **Statement**: The framing claims a high "learning rate" inside a
  great early-stage team as a non-monetary return; in practice
  learning rate is bundled with career-progression visibility (no
  promotions at 8-person companies, no level-mapping to next
  employer, harder to leverage for next negotiation). The framing
  treats learning as cleanly extractable.
- **Source evidence**: `community_profiles/vc-blogosphere.md`
  Known-blindspot 4 on grant-size differences between employee #5
  and #50 (level mapping unclear at small companies);
  `community_profiles/reddit-tech-collective.md` typical-concern on
  TC as the comparable unit.
- **Trigger**: Asker is taking a 30%+ comp cut for "the learning
  opportunity" at a small early-stage company.
- **Failure mode**: 4 years later, asker has rich experience but
  no titled progression; next-employer comp negotiation anchors on
  the small-company TC rather than the foregone large-company
  trajectory.
- **Recovery move**: Pre-negotiate level + title alignment with the
  next-employer benchmark; document accomplishments and scope
  recurrently for next negotiation; separate "learning value" from
  "career legibility value" — both matter.

---

## 12. Market-comp-anchoring framing

### 12.1 Carta benchmarks suppress data that would embarrass paying issuers

- **Statement**: The data publisher (Carta) is also the cap-table
  vendor selling to the issuer; findings that would embarrass the
  customer (year-4 zero-refresher rates, pre-409A repricings that
  wiped underwater grants) don't get surfaced. The "median refresher
  is 25-50%" benchmark is computed over the cohort that *received*
  one; the denominator of "got zero" is invisible.
- **Source evidence**: `community_profiles/carta-and-platform-data.md`
  Known-blindspot 1 (publisher-as-vendor conflict);
  `framings.md` §12 Excludes on the same.
- **Trigger**: Asker is anchoring on Carta-published percentile data
  for an outcome where the issuer would have commercial reason to
  suppress contrary data.
- **Failure mode**: Asker calibrates expected refresher at 25-50%
  of original grant; the actual cohort-wide refresher rate (including
  zeros) is half that; asker's negotiation anchor is off by 2x.
- **Recovery move**: When a Carta number would embarrass the
  paying customer if surfaced, treat it as a ceiling not a median;
  cross-reference against war-story sources (HN, r/ExperiencedDevs)
  for the denominator-including data.

### 12.2 Stage coverage tilts toward funded DE C-corps, dropping bootstrapped + SAFE-only + PE-backed

- **Statement**: Stage coverage tilts toward funded Delaware C-corps
  with priced rounds; SAFE-only seed, bootstrapped, revenue-funded,
  and PE-backed companies are silently dropped from the benchmark.
  A "Series A senior-eng median grant is 0.25-0.75%" anchor
  misroutes for a bootstrapped reader whose right comparator is
  profit-share or phantom equity.
- **Source evidence**: `community_profiles/carta-and-platform-data.md`
  Known-blindspot 2 (stage coverage tilt);
  `framings.md` §12 Excludes on same.
- **Trigger**: Asker is comparing offers from companies of materially
  different structure (bootstrapped + funded, or PE-backed + venture)
  and applying the same Carta-derived benchmark to both.
- **Failure mode**: Asker rejects the bootstrapped offer because
  the "0.5% Series A median" anchor makes 0.05% profit-share look
  like a lowball; the correct comparator (profit-share, dividends,
  buyout multiple) was different all along.
- **Recovery move**: Match the benchmark to the structure: equity
  benchmarks for funded DE C-corps, EBITDA-multiple / dividend-
  yield benchmarks for revenue-funded, MOIC and waterfall for
  PE-backed.

### 12.3 levels.fyi over-weights successful negotiators

- **Statement**: Self-reported data (levels.fyi) over-weights
  successful negotiators — people who got the comp they wanted are
  more likely to post. The median reported TC is higher than the
  median actual TC by a self-selection band the framing rarely
  names.
- **Source evidence**: `framings.md` §12 Excludes on self-selection
  bias.
- **Trigger**: Asker is anchoring on levels.fyi median for level X
  at company Y as the negotiation target.
- **Failure mode**: Asker uses p50 levels.fyi as the floor; recruiter
  comes back with "that's actually closer to our p75 internal";
  asker either over-anchors and gets rejected, or under-anchors
  the counter and accepts lower than rumored.
- **Recovery move**: Treat levels.fyi p50 as approximately the
  true-cohort p60-p70; calibrate negotiation accordingly. Use
  multiple sources (Glassdoor, internal contacts, recruiter
  direct ask) for triangulation.

### 12.4 Percentile-talk under-prices personal leverage

- **Statement**: Percentile-talk over-anchors the asker on a
  distributional outcome that doesn't account for their personal
  leverage; being p75 with a credible competing offer should yield
  p90+, but the framing's "we benchmark against p75" suggests p75
  as the ceiling.
- **Source evidence**: `framings.md` §12 Excludes on percentile-as-
  ceiling;
  `community_profiles/founder-engineer-bloggers.md` mental model on
  negotiation as information leverage.
- **Trigger**: Asker has personal leverage (competing offer, scarce
  skill, time-sensitive employer need) but is anchoring on
  benchmark p-bands.
- **Failure mode**: Asker negotiates to p75, gets there, stops;
  leverage-adjusted target was p90+; leaves $40-80k on the table.
- **Recovery move**: Treat benchmarks as the unleveraged baseline;
  add an explicit leverage adjustment (10-25% above benchmark for
  strong competing offer, 5-10% for moderate); negotiate the
  benchmark + leverage number, not the benchmark alone.

### 12.5 Geographic tier flattening is overstated post-2024

- **Statement**: The framing's "remote varies but tiers persist"
  is calibrated to the 2022-2023 remote-arbitrage moment; post-2024
  RTO mandates have re-tiered geography by where you must be
  physically present. Pure-remote comp benchmarks are increasingly
  rare at top employers.
- **Source evidence**: `community_profiles/carta-and-platform-data.md`
  typical-concern on geographic comp tiers (recent flattening since
  2022 but not full convergence — written assuming 2022-23 baseline);
  `community_profiles/hn-collective.md` Known-blindspot 5 on
  anecdotes cited as if market structure is static.
- **Trigger**: Asker is reasoning about remote vs SF/NY comp using
  pre-RTO-mandate benchmark data.
- **Failure mode**: Asker assumes remote-comp parity has held;
  negotiation anchors high; employer rebalances to lower remote-comp
  band that the asker's data didn't reflect.
- **Recovery move**: Date-stamp the benchmark source; for post-2024
  data, distinguish "fully remote OK at full comp", "fully remote
  OK at -10-20%", "hybrid required at SF/NY band"; the policy is
  the variable, not the role.

---

## 13. Insider-signal-reading framing

### 13.1 Employee tax is a downstream footnote, not a primary signal

- **Statement**: The framing treats employee tax as a downstream
  footnote (the unit of analysis is the deal, not the asker's
  1040). Frames a tender as "founders sell $80M, VCs take
  preference" without flagging the NSO ordinary-income or
  ISO-spread AMT coming due that April. Asker reads a correct
  deal description and walks into a six-figure surprise tax bill.
- **Source evidence**: `community_profiles/matt-levine-school.md`
  Known-blindspot 2 (treats employee tax as a downstream footnote
  because the unit of analysis is the deal); `framings.md` §13
  Excludes on same.
- **Trigger**: Asker is participating in a tender / secondary
  presented as a "good outcome" by a deal-mechanics-voice source.
- **Failure mode**: Asker participates; tender treated as
  disqualifying ISO disposition triggers ordinary-income tax on
  the bargain element plus short-term cap gain on appreciation;
  withholding inadequate, $80-150k surprise tax bill at April.
- **Recovery move**: Before participating in any tender, run the
  AMT + ordinary-income calculation explicitly; the tender price
  net of all tax is the right comparator, not the headline price.

### 13.2 Public-company / Delaware framings over-applied to private-company situations

- **Statement**: Over-applies public-company / Delaware framings
  (appraisal rights, Dell, Aruba) to private-company situations
  where the binding constraint is the drag-along plus the founder
  re-vest, not governance-style protection.
- **Source evidence**: `community_profiles/matt-levine-school.md`
  Known-blindspot 1 (over-applies public-company / Delaware framings
  to private-company situations); `framings.md` §13 Excludes on
  same.
- **Trigger**: Asker is evaluating an acquihire / sub-$50M sale and
  hearing analysis citing Delaware appraisal-rights case law as
  protection.
- **Failure mode**: Asker expects appraisal protection that doesn't
  apply to private common; drag-along forces the sale at common
  $0; appraisal-rights advice was theoretical from the start.
- **Recovery move**: For private-company exits, the binding
  documents are the drag-along, the COI preference stack, and the
  founder re-vest terms — not Delaware case law. Read those
  documents.

### 13.3 Big-deal-centric corpus, EU / Israeli / small-deal blind

- **Statement**: $500M+ M&A and IPO mechanics get covered; the
  Series B acquihire of a 30-person company and EU-equity
  instruments (BSPCE, EMI, Dutch STAK, Israeli §102) are out of
  corpus.
- **Source evidence**: `community_profiles/matt-levine-school.md`
  Known-blindspot 5 (big-deal-centric and US-centric by corpus
  selection);
  `community_profiles/founder-engineer-bloggers.md` Known-blindspot
  2 (non-US comp structure gestured at, not modeled);
  `framings.md` §13 Excludes on same.
- **Trigger**: Asker's situation is small (sub-$50M deal) OR
  non-US-instrument; framing is reaching for big-deal Delaware
  vocabulary.
- **Failure mode**: Asker gets confidently-wrong advice based on
  big-deal Delaware framework; binding law is country-specific
  (UK EMI, German vest-tax, Israeli §102 trustee track) or
  small-deal-specific (drag-along, no-fairness-opinion).
- **Recovery move**: Confirm scope match before applying the
  framing: if deal < $50M or non-US instrument, defer to local
  specialist; the deal-mechanics framing's reach exceeds its
  corpus here.

### 13.4 Insider-sell is treated as mechanism, missed as base-rate signal

- **Statement**: Reads "insiders sell" as mechanism for the
  deal-narrative voice while forgetting it's also private
  information for the rank-and-file — the framing's "this is fine,
  this is how it works" rhetorical move under-weights the base-rate
  finding that tender-then-down-round sequences are common.
- **Source evidence**: `community_profiles/matt-levine-school.md`
  Known-blindspot 3 (reads "insiders sell" as mechanism and forgets
  it's also signal); `framings.md` §13 Excludes on same.
- **Trigger**: Asker is participating in a tender where founders or
  early VCs are selling material amounts; framing analysis
  presents this as routine.
- **Failure mode**: Asker holds, treating founder-sells as
  procedural; next round comes in at a lower valuation; founders
  who sold are the only winners.
- **Recovery move**: When founders / VCs sell at the tender price,
  weight that as inside-information signal; the base-rate of
  tender-then-down-round is meaningful at most late-stage
  privates. Diversify against this signal.

### 13.5 S-1 archaeology requires the S-1; private-company decisions lack the document

- **Statement**: "S-1 archaeology" is the framing's
  characteristic move — but it requires the S-1 to exist; for
  private-company decisions there is no S-1, only the cap-table
  summary the company chooses to share. The framing's
  document-reading discipline has no document to read.
- **Source evidence**: `framings.md` §13 Mental model line on S-1
  archaeology; `community_profiles/hn-collective.md` Known-blindspot
  3 on anecdote-weight asymmetry (in absence of public docs, all
  anecdotes weight equally regardless of poster proximity).
- **Trigger**: Asker is making a tender / acquihire / private-company
  exercise decision and the framing-voice advice is "read the S-1".
- **Failure mode**: Asker has no S-1; defaults to company-provided
  summary; misses the preference-stack and retention-package
  details that would normally show up in S-1 exhibits.
- **Recovery move**: For private companies, request specific
  documents (COI, plan document, individual grant notice,
  recent 409A appraisal summary); these are the closest analog to
  S-1 disclosure and are often shareable on request.

---

## 14. Reputation-signal framing

### 14.1 "Industry is small" over-generalizes from SF/NY tech-network density

- **Statement**: "Industry is small" reasoning over-generalizes from
  the framing's SF/NY tech-network sample; for engineers outside
  those metros, in less network-dense subfields (govtech, biotech,
  climate hardware), the reputation-graph is sparser and the
  framing's "everyone will know" pressure is overstated.
- **Source evidence**: `framings.md` §14 Excludes on SF/NY-network
  sample.
- **Trigger**: Asker is outside the SF/NY tech corridor (regional
  city, EU, non-tech-adjacent subfield) and is being told
  "industry is small, don't burn the bridge".
- **Failure mode**: Asker accepts a worse outcome (worse severance,
  unfair PIP, lower counter) under a reputational pressure that
  doesn't actually exist in their network density.
- **Recovery move**: Calibrate network density to the asker's actual
  subfield + metro; for low-density situations, the reputational
  weight on a single departure is much lower than the framing
  suggests.

### 14.2 Reputational cost varies by role; the framing treats it as uniform

- **Statement**: The framing treats reputational damage as a uniform
  cost; in practice the type of departure that's reputationally
  costly varies by role (engineers can leave abruptly with little
  stigma; GTM/sales leaders cannot, customer accounts move with
  them) and the framing doesn't differentiate.
- **Source evidence**: `framings.md` §14 Excludes on role-specific
  reputational cost;
  `community_profiles/founder-engineer-bloggers.md` Known-blindspot
  3 (EM/director-specific gaps).
- **Trigger**: Asker is in a customer-facing or relationship-based
  role (sales, customer success, founder) AND applying the
  engineering-default reputation framework.
- **Failure mode**: Asker quits per the framing's "always leave on
  good terms" without realizing that for their role-class the
  damaging element is customer-poaching perception, not
  resignation-style; the bridge burns despite procedural caution.
- **Recovery move**: Match reputation framework to role: ICs can
  resign per the textbook; customer-facing roles need explicit
  hand-off scripts and a customer-non-solicit understanding to
  preserve relationships.

### 14.3 "Always leave on good terms" can route the asker into accepting bad treatment

- **Statement**: The framing's "always leave on good terms" advice
  can route the asker into accepting genuinely-bad treatment
  (uncountered severance, unfair PIP, retaliation after protected
  activity) because confrontation is presented as universally
  reputation-destroying.
- **Source evidence**: `framings.md` §14 Excludes on bad-treatment
  acceptance;
  `community_profiles/reddit-tech-collective.md` typical-concern on
  PIP-as-soft-termination and severance vs UI eligibility tradeoff.
- **Trigger**: Asker faces concrete bad treatment (documented
  retaliation, PIP after protected activity, uncountered standard
  severance) AND framework-voice is counseling "manage the
  departure smoothly".
- **Failure mode**: Asker accepts the bad treatment to preserve
  the relationship; relationship was already adversarial; gives
  up legally-leveraged settlement value AND the relationship
  benefits don't materialize.
- **Recovery move**: Triage relationship-status BEFORE applying
  the framework: if the employer's behavior is already adversarial
  (documented PIP-after-protected-activity, retaliation), the
  bridge is already burning and the framing inverts — push back
  on substantive terms because the reputation hit is already
  accepted by the counterparty.

### 14.4 Generational social-media disclosure norms have shifted

- **Statement**: Gen-Z and younger Millennial engineers report on
  layoff / PIP / departure stories on social media in ways the
  prior cohort treated as confidential; the framing's
  "don't burn the bridge" model is based on a more discreet
  labor-market era that's eroding.
- **Source evidence**: `framings.md` §14 Excludes on generational
  shift;
  `community_profiles/hn-collective.md` Known-blindspot 5 on
  anecdotes cited as if market structure is static.
- **Trigger**: Asker is a Gen-Z / younger Millennial AND framework
  is being applied as if disclosure norms match the 2010-era
  baseline.
- **Failure mode**: Asker holds to silence as the framework
  prescribes; peer cohort uses transparency as a recruiting /
  hiring-manager-credibility signal; asker's silence is itself
  perceived as the suspicious behavior.
- **Recovery move**: For younger-cohort askers, recognize that
  selective transparency (LinkedIn open-to-work post, blog post
  about layoff with no employer-bashing) has become a positive
  signal; the framework's silence-is-default rule is now
  context-dependent.

### 14.5 Reference-call leverage assumes a manager who will pick up the phone

- **Statement**: The framing values a strong manager reference at
  $50-200k of next-job comp via faster offer velocity; this assumes
  the manager will pick up the phone in 2-3 years. For managers
  who have themselves been laid off, moved on, or who follow
  no-reference HR policies, the reference asset has near-zero value.
- **Source evidence**: `community_profiles/founder-engineer-bloggers.md`
  Known-blindspot 3 (EM/director-specific gaps); reinforced by
  `community_profiles/reddit-tech-collective.md` Known-blindspot 3
  (FAANG-washout PIP threads).
- **Trigger**: Asker is investing significant career-decision weight
  in preserving relationship with a specific manager, in a
  high-attrition environment.
- **Failure mode**: Asker holds back from a needed counter / a
  needed exit to preserve "the reference"; manager leaves company
  before reference is needed; preservation gave up value for
  nothing.
- **Recovery move**: Distinguish between a network reference (3-5
  people who know your work) and a single-manager reference; the
  former is durable, the latter is fragile. Invest in network
  breadth, not single-relationship preservation.

---

## Cross-framing notes

These call out where blindspots in one framing are the *recovery move*
of another. The pairings are useful for the Triage / Risk Officer when
the asker is clearly inside one framing — the contrarian framing's
blindspot list is often the right intervention.

- **§3 Liquidity-preservation ↔ §11 Asymmetric-bet-on-team**: opposites
  on early-stage offer acceptance. The asker inside one is exactly the
  person the other should be challenging. §3.4 (prudence misses the
  cheap window) and §11.3 (opportunity cost not modeled) are the
  cross-framing tensions.
- **§4 Concentration-risk ↔ §13 Insider-signal-reading**: opposite
  directions on tender participation. §4.1 (employee inside view) and
  §13.4 (insider-sells-as-signal) are the same insight from different
  voices — surface both when the asker is anchored on one.
- **§1 AMT-minimization ↔ §3 Liquidity-preservation**: AMT pushes
  toward earlier / larger exercise; liquidity pushes toward smaller /
  later. The synthesis (§1.3 cash-constrained paths, §3.4 cheap
  window) requires holding both framings.
- **§7 Retention-leverage ↔ §14 Reputation-signal**: short-term
  leverage extraction vs long-term relationship preservation. §7.4
  (multi-year promotion-velocity cost) and §14.3 (bad-treatment
  acceptance) bound the tradeoff from both directions.

## Maturity note

This file is `in-migration` maturity per
[`_schema.md`](../_schema.md). Blindspots are written from
audited community profiles and source-views; numeric anchors carry
the date-stamp risk inherited from the underlying corpus
(see `long-form-references.md` Known-blindspot 1 on edition cadence).
When OBBBA 2025, the FTC non-compete rule status, or AMT exemption
thresholds shift, the affected entries (§1.1, §1.2, §2.1, §9.5) need
re-check before being relied on for an active decision.
