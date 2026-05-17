# tech-career — framings.md (Layer 2)

Framing library for `tech-career`. Each entry names one lens — the way
a specific community / tradition argues about a decision — and lists the
decisions from [`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

Voice references: `community_profiles/tax-and-finance-professionals.md`
(AMT, clocks), `community_profiles/carta-and-platform-data.md`
(market-comp), `community_profiles/founder-engineer-bloggers.md`
(negotiation, retention, cliff), `community_profiles/matt-levine-school.md`
(insider signal, preference stack), `community_profiles/vc-blogosphere.md`
(dilution, pool refresh), `community_profiles/hn-collective.md`
(forfeiture stories, headline-vs-payout), `community_profiles/long-form-references.md`
(non-compete enforceability), `community_profiles/tax-and-finance-professionals.md`
again for clock arbitrage and QSBS.

---

## 1. AMT-minimization framing

- **Decisions it applies to**: D3 (ISO exercise timing pre-IPO),
  D9 (Pre-IPO tender / secondary).
- **Mental model summary**: The bargain element on ISO exercise —
  (FMV − strike) × shares — is an AMT preference item that doesn't
  appear on regular taxable income. The April-15 cash bill is the
  binding constraint, not the option's nominal value. Reasons in
  exercise-year dollar terms: "what is the largest exercise I can do
  in 2026 that absorbs the AMT exemption + the 26%/28% bracket without
  triggering the phase-out cliff?" Anchor numbers: 2026 AMT exemption
  ($88,100 single / $137,000 MFJ), 28% bracket break ~$232,600 AMTI,
  ~$1.2M phase-out completion. Frames a tender as a *deliberate AMT
  event* with a calculable bill, not a liquidity windfall. The
  characteristic move is "tranche the exercise across calendar years."
- **Characteristic vocabulary**: "bargain element", "AMTI",
  "exemption phase-out", "26/28 crossover", "AMT credit carryforward",
  "tentative minimum tax", "disqualifying disposition", "Section 422",
  "ISO basis bifurcation", "tranched exercise."
- **Excludes**:
  - The modal pre-IPO outcome is flat-or-down: tranching assumes
    monotone FMV growth and the framing has no place for "exercise
    early, AMT-bill, stock goes to zero, AMT credit is uncollectable
    because regular tax never catches up."
  - State-level AMT divergence (CA carries no refundable credit;
    NY claws back option income on grant-to-exercise allocation for
    partial-year residents) is treated as a footnote even when the
    state delta dominates the federal optimization.
  - Cash-bind reality: the framing's modeled reader has 6 figures
    liquid; for a grantee with $40k savings, "tranche optimally"
    collapses to "don't exercise," missing net-exercise-at-tender,
    sell-to-cover, or 83(b)-on-early-exercise paths.
  - The 409A FMV used in the AMTI calc is itself a negotiation
    between the company and its valuation firm; treating it as
    exogenous misses that a refresh timed against a tender can
    move the bargain element by 30%+.

## 2. Tax-clock-arbitrage framing

- **Decisions it applies to**: D3, D9.
- **Mental model summary**: Equity tax outcomes are dominated by a
  handful of clocks that start on specific events and pay off if you
  hold long enough. ISOs: ≥ 2 years from grant AND ≥ 1 year from
  exercise for qualifying disposition. QSBS (Section 1202): 5 years
  of original-issuance C-corp stock holding for up to $10M (or 10×
  basis) of federally-excluded gain. LTCG: 1 year from acquisition.
  AMT credit: recoverable in any future year where regular tax > AMT.
  The framing optimizes by starting clocks as early as cash and AMT
  permit, then aligning sales to land after the latest binding clock.
  Distinct from AMT-minimization in that the binding constraint is
  *time*, not exercise-year cash. Characteristic move: early-exercise
  unvested ISOs with an 83(b) to start the ISO holding-period and the
  QSBS clock from day one of grant.
- **Characteristic vocabulary**: "QSBS clock", "5-year holding",
  "1202 stack", "original issuance", "qualifying disposition",
  "83(b) within 30 days", "holding-period bifurcation",
  "AMT credit recovery", "LTCG crossover", "step-up at death."
- **Excludes**:
  - QSBS and 1061 (carried interest) are politically volatile — the
    framing's confidence in 422 (ISO mechanics, stable since 1981)
    bleeds across to 1202, where the per-issuer cap and holding
    period have been targeted by multiple legislative proposals
    since 2021.
  - "Start the clock early" advice ignores that early-exercise on
    unvested stock requires the company to permit it (often gated to
    employees 1-50 or the founder cohort); the rank-and-file reader
    can't act on the framing's preferred move.
  - The AMT credit dies at death without step-up — the framing
    promotes accumulating credit as a long-run asset but never
    names this asymmetry for older grantees or estate planners.
  - On a year-4 disqualifying redemption (acquihire forced
    short-window sale), the 5-year QSBS clock resets across the
    successor entity in ways the framing's "just hold for 5 years"
    summary doesn't capture.

## 3. Liquidity-preservation framing

- **Decisions it applies to**: D1 (Compare offers), D2 (Early-stage
  offer), D3, D9.
- **Mental model summary**: Paper wealth is not real wealth until it's
  cash in your account. The framing reasons from the personal balance
  sheet: cash-on-hand, runway in months, fixed obligations (rent,
  childcare, debt service). Every grant is also a *liability* — the
  cost to exercise, the AMT cash bill, the opportunity cost of capital
  locked in an illiquid ticker. Anchor numbers: 6-12 months expenses
  in cash, exercise cost as a fraction of liquid net worth, ratio of
  vested-but-unexercised value to cash available to exercise it.
  Characteristic move: walk away from an option whose AMT bill would
  consume the emergency fund, regardless of EV upside.
- **Characteristic vocabulary**: "cash runway", "exercise cost",
  "after-tax liquid", "concentration of net worth", "forced sale",
  "AMT cash bind", "emergency fund", "personal balance sheet",
  "sell-to-cover", "net exercise."
- **Excludes**:
  - Treats grants symmetrically as "illiquid asset / known cost" and
    misses non-recourse loan structures (ESO Fund, secondary lenders)
    that decouple exercise cost from personal cash for grantees who
    can clear due diligence.
  - "Build 12 months runway before exercising" is itself an
    opportunity-cost choice — cash held for safety is cash not
    compounding, and the framing doesn't name the trade.
  - For high-income earners ($400k+ TC), the "personal balance sheet"
    constraint becomes loose and the framing's vocabulary is
    unhelpful — they should be reasoning about marginal tax brackets
    and concentration, not cash on hand.
  - The framing's prudence-bias systematically under-recommends
    exercise at the moment when an early-employee should exercise
    (low strike, low FMV-strike spread, low AMT) — the cheap-window
    is exactly when the asker has the least cash.

## 4. Concentration-risk framing

- **Decisions it applies to**: D1, D3, D6 (Golden handcuffs),
  D9 (Tender).
- **Mental model summary**: Single-stock concentration in employer
  equity is uncompensated risk. Once vested holdings exceed ~20% of
  net worth, the marginal next dollar of comp should be cash, not
  more of the same ticker. Reasons in portfolio terms: idiosyncratic
  risk premium is zero in efficient markets; concentration is paid
  for by the holder, not rewarded. Characteristic move: participate
  fully in any tender that brings concentration below the threshold,
  even at a 20%+ discount to the last-round price. Anchor numbers:
  Markowitz mean-variance bounds, the empirical 50% probability that
  any individual stock underperforms cash over 10 years (Bessembinder
  2018), the post-tax cost of holding vs diversifying given a 1y vs
  20% LTCG bracket gap.
- **Characteristic vocabulary**: "idiosyncratic risk", "concentration",
  "diversify out", "single-ticker exposure", "10b5-1 plan",
  "Bessembinder", "uncompensated volatility", "mean-variance",
  "tax-aware rebalance", "vest-and-sell."
- **Excludes**:
  - Treats the employer-stock as identically distributed with other
    public equities for risk purposes, missing that an
    employee-shareholder has private information about company
    trajectory that flat-portfolio theory assumes away.
  - At early-stage private companies, "diversify out" is impossible —
    there is no exit market — and the framing has no vocabulary for
    "concentration is your only option, manage on the qualitative
    side instead."
  - The Bessembinder result is about *random* single-stock picks;
    employees aren't random pickers — they're inside the cap table.
    Whether that inside view shifts the base rate is exactly what
    this framing refuses to engage.
  - Tax-aware rebalancing advice glides past wash-sale interaction
    with ongoing RSU vests at the same ticker: selling vested shares
    while new RSUs vest can trigger §1091 disallowance the framing
    rarely catches.

## 5. Dilution-math framing

- **Decisions it applies to**: D1, D2, D6, D8 (Refresher),
  D10 (Acquihire), D11 (Cofounder split).
- **Mental model summary**: Equity value is a function of (your %
  ownership) × (exit valuation) × (1 − preference stack) ×
  (1 − dilution from now to exit). Each priced round dilutes existing
  shareholders 15–25%; option pool refreshes pre-money dilute existing
  shareholders without diluting the incoming investor. A grant at
  seed is worth ~half by Series C purely from dilution, before
  considering pool refreshes. Reasons on the cap table: post-money
  ownership, fully-diluted ownership, ownership at exit assuming
  N more rounds. Characteristic move: model the exit-time stake at
  +1, +2, +3 future rounds before signing, then negotiate to the
  delta. Anchor numbers: 0.5-1.5% for early seed engineers,
  declining by stage; typical 10-20% pool refresh per round; 1×
  non-participating preferred as baseline preference stack.
- **Characteristic vocabulary**: "fully diluted", "pre-money pool",
  "option pool top-up", "post-money cap table", "1× non-participating",
  "participating preferred with cap", "pay-to-play", "anti-dilution
  ratchet", "stacked preferences", "common-stock waterfall."
- **Excludes**:
  - Assumes a priced-round trajectory; reasons poorly about
    SAFE-only seed companies where post-conversion dilution is
    deferred and ambiguous until the next priced round resolves.
  - Headline "1× non-participating" gets stated but per-series
    participation caps, pay-to-play, side-letter MFNs, and
    multi-round anti-dilution adjustments stack into 50%+ of exit
    value at a soft sale — the framing's preference-stack vocabulary
    is correct but routinely under-applied.
  - Treats the exit valuation as the analytical input but most
    employee outcomes are governed by acqui-hire scenarios where
    the *headline* and the *common-stock* numbers diverge by 80%+.
  - Doesn't model refresher-or-die dynamics: a non-refreshed
    employee at Series C is on a 4-year glide path to <0.05%, a
    discontinuity the per-round dilution arithmetic obscures.

## 6. Cliff-arithmetic framing

- **Decisions it applies to**: D2, D4 (Pre-cliff quit), D6, D7 (PIP),
  D10, D11.
- **Mental model summary**: Vesting cliffs and re-vest schedules
  create discontinuities in the payoff function. The week before a
  1-year cliff is worth ~0 in vested equity; the week after, ~25% of
  the grant. Acquihire re-vests reset the clock; PIPs are often
  timed to a vesting event the employer wants to avoid paying out.
  Reasons in calendar terms: time to next vest, time to cliff,
  acceleration triggers, post-termination forfeiture rules.
  Characteristic move: never quit, switch, or accept a PIP within
  ~90 days of a vest; either bridge the calendar or use the vest as
  leverage. Anchor numbers: 4-year/1-year-cliff baseline; monthly vs
  quarterly post-cliff vest cadence; 90-day PTE window; double-
  trigger acceleration ≈ 25-50% of unvested on qualifying termination.
- **Characteristic vocabulary**: "cliff", "monthly vest", "quarterly
  vest", "PTE window", "single-trigger acceleration", "double-trigger
  acceleration", "re-vest", "back-loaded vest" (Amazon 5/15/40/40),
  "vest acceleration on involuntary termination", "trailing vest."
- **Excludes**:
  - Treats vesting events as exogenous calendar facts; misses that
    the employer can re-time perf cycles, layoff dates, and PIP
    starts to land on the cheap side of a vest (the framing's own
    Decision 7 reasoning, oddly under-applied to its own scenarios).
  - Parental leave inside a cliff: most plans don't extend the
    cliff for protected leave, and the framing's "wait for the
    cliff" advice can route a new parent into months of unpaid
    cliff-stretch they didn't price in.
  - For golden-handcuffs at FAANG with quarterly vest cadence and
    refresher stacking, the "next vest" question is misleading —
    the binding decision is the *trailing* unvested portfolio
    across multiple grants, not the next ~$30k tranche.
  - 90-day PTE assumption is anchored to ISO statutory requirements;
    extended PTE windows (Quora, Pinterest, Coinbase pre-IPO) and
    early-exercise-with-83(b) regimes invalidate the calendar
    arithmetic without changing the framing's vocabulary.

## 7. Retention-leverage framing

- **Decisions it applies to**: D1, D4, D5 (Severance), D6, D8, D10,
  D11.
- **Mental model summary**: Compensation outcomes are determined by
  relative leverage at the moment of the conversation, not by abstract
  fairness or market rate. Leverage = (cost to employer of you
  walking) − (cost to you of walking). At a new-hire negotiation,
  leverage comes from a competing offer; mid-tenure, from being
  load-bearing on a shipping project; in severance, from threat of
  litigation or knowledge of unpaid OT/equity claims. The asymmetry
  default is that the employer has done this hundreds of times and
  you have not. Characteristic move: never volunteer information that
  collapses the leverage gradient (current salary, eagerness, willingness
  to accept). Always make the employer name the number first; always
  let silence work. Anchor numbers: 10-25% lift from a competing-offer
  counter at top employers; refresher requests succeed 60-80% when
  framed with market data and a credible alt; severance negotiable
  ~50% in the dollars and ~80% on the non-cash terms (release scope,
  rehire eligibility, reference letter).
- **Characteristic vocabulary**: "BATNA", "leverage", "competing offer",
  "anchoring", "first number wins", "walking warm", "load-bearing",
  "retention grant", "counter-offer", "the company has done this a
  thousand times."
- **Excludes**:
  - Assumes the asker can credibly walk; for an H-1B holder 3 years
    into a green-card process whose I-140 hasn't crossed the AC21
    portability threshold, the "always negotiate, worst they can
    say is no" advice is structurally wrong and the framing has no
    vocabulary for status-bounded leverage.
  - Empirical evidence that women and Black IC candidates who
    counter at the same rate as white men are perceived as more
    aggressive by hiring committees (Bowles HBR 2007 line; replicated
    at FAANG) — the framing assumes symmetric reception of the same
    tactic, which the data contradicts.
  - For senior managers in re-org-prone product areas, the implicit
    "load-bearing on a project" leverage source evaporates when the
    project is killed in an exec swap — the framing reasons about
    individual leverage but not organizational fragility.
  - Companies pattern-match aggressive negotiation as a sign of
    likely retention problems; the framing's tactic that maximizes
    signing-bonus dollar can degrade post-signing promotion velocity
    and OKR-bandwidth allocation — a multi-year cost the single-
    transaction framing doesn't price.

## 8. Severance-leverage framing

- **Decisions it applies to**: D5, D7.
- **Mental model summary**: A severance offer is a settlement, not a
  gift. The signing deadline (typically 7-21 days under OWBPA for
  age-40+; uncodified shorter for under-40) is a negotiation pressure
  tactic, not a hard expiry. The bundled clauses — release of all
  claims, non-disparagement, non-compete, confidentiality, return-of-
  property — are individually negotiable and trade against the cash
  number. Reasons clause-by-clause: what claim is being waived, what
  the employer's litigation exposure looks like if you don't sign,
  what the cost is to them of an extended dispute. Characteristic
  move: never sign on the original deadline; always counter on
  non-cash terms (rehire eligibility, reference letter, accelerated
  vesting, extended healthcare, removal of non-compete) before
  countering on cash. The waiver of unvested equity is often the
  largest negotiable item that goes uncountered.
- **Characteristic vocabulary**: "release of claims", "OWBPA 21-day
  consideration", "EEOC carve-out", "non-disparagement",
  "garden leave", "trailing vest", "rehire eligibility",
  "no-rehire policy", "settlement on stale claims", "tolling letter."
- **Excludes**:
  - Assumes the asker has the emotional bandwidth to negotiate
    during a layoff — post-termination decision quality is empirically
    poor (financial-decision research on stress-induced narrowing),
    and the framing's "take your time, push back" advice can be
    actively harmful for a sole-income earner with mortgage stress.
  - At-will employment baseline makes most "settlement value of
    claim" math a bluff; for retaliation / discrimination claims
    with concrete documentation, the framing under-prices the
    counter-leverage available (a Title VII charge filed pro se is
    free to the asker and expensive to the employer).
  - "Trailing vest" and "accelerated vest" requests get treated as
    standard negotiation items; in practice most ISO plans
    explicitly prohibit post-termination vesting and the request
    forces a non-standard board action the employer often refuses
    on principle.
  - The framing's clause-by-clause discipline gets short-circuited
    by the bundled-binary signing UX of platforms like Carta /
    Sequoia One — the asker is presented with "Accept" or "Decline"
    and the framing's negotiation move has no surface to land on
    until they get a partner-attorney on the phone.

## 9. Non-compete-enforceability framing

- **Decisions it applies to**: D5.
- **Mental model summary**: Non-compete clauses vary in enforceability
  by state from "categorically void" (California, North Dakota,
  Oklahoma) to "void with narrow exception" (Minnesota, Colorado for
  most workers since 2022) to "enforceable with reasonableness test"
  (most other states). The 2024 FTC rule banning most non-competes
  was vacated by the Northern District of Texas (Aug 2024) and the
  pre-FTC patchwork is back in force. Reasons in jurisdiction + duty
  + duration + scope: where the work is performed, whether the
  signer is exempt/non-exempt, whether the clause covers competitors
  or all employers, how long, with or without garden leave.
  Characteristic move: identify governing-law clause, check the
  state's current enforceability stance, then evaluate whether the
  cost of enforcement (litigation by ex-employer, injunction risk)
  exceeds the value of the constraint to them. Anchor: CA non-compete
  is a Business & Professions Code §16600 nullity; MA Garden Leave
  Act requires 50% pay during enforcement; FL is the strictest
  full-enforcement state.
- **Characteristic vocabulary**: "Business and Professions Code §16600",
  "garden leave", "tortious interference", "blue pencil doctrine",
  "reasonableness test", "consideration for the restraint",
  "geographic scope", "duration scope", "tolling on breach",
  "FTC non-compete rule (vacated)."
- **Excludes**:
  - State-of-residence vs state-of-incorporation vs state-of-work
    creates a choice-of-law puzzle the "check your state" shorthand
    skips — a CA-resident remote employee of a NY-incorporated
    employer working with TX customers has three plausible laws to
    apply, and the contract often picks DE governing law to muddy
    further.
  - The cost of *defending* an unenforceable non-compete
    (attorney fees pre-12-day TRO hearing, lost income while
    employer "evaluates whether to sue") can dwarf the value of
    the new job — the framing's correct-on-the-law conclusion
    can route the asker into an expensive practical loss.
  - Trade secret and inevitable disclosure doctrines route around
    voided non-competes via DTSA / state UTSA claims, which the
    framing's enforceability map doesn't capture.
  - The framing covers leave-employer non-competes well but
    under-addresses customer non-solicit and employee non-solicit
    (which survive in CA where non-competes don't, under §16600
    case-law splits) — these are the more enforceable cousins.

## 10. Contribution-asymmetry framing

- **Decisions it applies to**: D11 (Cofounder split).
- **Mental model summary**: Equity at cofounder formation is paying
  for *future* work, not past contribution. The "I had the idea"
  argument is worth ~5-10% premium at most; the next 4-7 years of
  execution is the asymmetric work being compensated. Reasons in
  forward-work units: who is full-time vs part-time, who has primary
  family responsibility, who took the salary cut, who has the
  domain network, who can fundraise. Characteristic move: structure
  splits to incentivize the people doing the work being done, with
  vesting + acceleration as the trust mechanism rather than ownership
  % as a status assignment. Anchor: 50/50 with vesting is more
  durable than 60/40 without; idea premium of 5-10% is the literature
  bound (Slicing Pie, Founder Institute templates); the cliff +
  4-year vest is the trust-mechanism equivalent of marriage's
  no-fault divorce protocol.
- **Characteristic vocabulary**: "sweat equity", "idea premium",
  "forward work", "reverse vesting", "founder vesting cliff",
  "Slicing Pie", "dynamic equity split", "founders' breakup
  agreement", "acceleration on involuntary removal",
  "for-cause vs not-for-cause termination of a founder."
- **Excludes**:
  - The framing assumes ongoing collaboration and that the trust
    mechanism (vesting) is sufficient; misses the case where the
    relationship sours pre-product-market-fit and the cap table
    becomes a divorce — at which point the IP, the company name,
    and the existing investor relationships are all contested
    in ways the equity-split framing doesn't address.
  - Capital contribution (one founder funds the company's first
    18 months from savings) doesn't fit cleanly into "forward
    work" arithmetic; the framing routes this through "convertible
    note from a founder" and loses the human dynamic.
  - International cofounder pairs face country-specific issues
    (UK BSPCE-equivalent rules, Indian FEMA restrictions on
    foreign-resident shareholders) the US-default framing
    silently glides over.
  - The "idea premium of 5-10%" anchor is from successful-company
    retrospectives — survivorship bias. The premium the *failed*
    cofounder relationships had when they were forming is unknown
    and presumed higher (because the breakup is what produces the
    data the literature samples).

## 11. Asymmetric-bet-on-team framing

- **Decisions it applies to**: D2 (Early-stage offer).
- **Mental model summary**: At seed-to-Series-A, expected-value
  calculations on the equity component are noise — the variance is
  multiple orders of magnitude wider than the point estimate. The
  load-bearing question is whether the team is in the top decile of
  founders the asker can plausibly work with, because outcomes are
  log-normal and "the right team at the right moment" is the only
  empirically replicable predictor of an outlier outcome. Reasons in
  team-quality terms: who else are they hiring, who has invested,
  what is the founder's prior shipping track record, what is the
  asker's learning rate inside this team vs the next best opportunity.
  Characteristic move: take the comp-below-market offer if (and only
  if) the team would be a top-3 career bet over the next 4-7 years;
  walk if the team is merely "good." Anchor numbers: power-law
  outcome distribution (top 1% of seed-stage companies generate
  ~95% of total value, per First Round / YC retrospectives); team-
  quality as the only stage-one input that correlates with the
  outlier outcome.
- **Characteristic vocabulary**: "power law", "outlier outcome",
  "asymmetric bet", "top-decile team", "founder-market fit",
  "expected value is noise at this stage", "learning rate",
  "category-defining", "if it works, it works",
  "the team is the asset."
- **Excludes**:
  - The framing's "if the team is exceptional, take it" advice is
    indistinguishable from confirmation bias when the asker is
    already inclined to join — provides no falsifiable rejection
    criterion for "exceptional."
  - Power-law outcomes are real at the *fund* level (the VC bet);
    the employee's payoff is bounded by their grant size, vesting,
    and dilution path, which compresses the upside in ways the
    fund-level math doesn't.
  - The opportunity-cost framing — what the asker is *not* doing
    during the 4-7 years — is named in passing but rarely modeled.
    A foregone FAANG offer at $500k TC × 4 years = $2M of
    after-tax cash + retirement contributions + diversified
    portfolio compounding, which is the benchmark the "team is the
    asset" bet has to clear.
  - Survivorship voice — the people writing the "join the great
    team" essays are the ones whose great teams worked. The
    cohort of equally-thoughtful asker-bettors whose great teams
    quietly hit the wall at Series B doesn't produce the same
    volume of post-hoc rationalization content.

## 12. Market-comp-anchoring framing

- **Decisions it applies to**: D1, D2, D8 (Refresher).
- **Mental model summary**: Compensation is a distribution, not a
  point estimate. The question is "what's the 50th / 75th / 90th
  percentile for my stage, role, location, and level?", and the
  asker's offer should be evaluated against that benchmark. Stage
  drives equity more than any other variable: median engineer grant
  at Series A is 5-10× that at Series D. Geographic tiers (SF/NY
  top; Seattle/LA second; remote varies) have flattened since 2022
  but not converged. Refreshers cluster at year 2 and year 4 in the
  Carta dataset at 25-50% of original grant; employees who don't
  get refreshed are at a benchmarkable disadvantage. Characteristic
  move: cite a specific percentile band ("75th-percentile L5 base at
  Series C is $235-265k per levels.fyi") as the negotiation anchor,
  then negotiate against it. Anchor numbers: percentile bands by
  stage × level × geo as the primary unit of analysis.
- **Characteristic vocabulary**: "p50 / p75 / p90", "levels.fyi
  band", "Carta State of Comp", "stage-adjusted", "level mapping",
  "TC at signing", "median refresher", "geo tier",
  "benchmark distribution", "Equity Almanac."
- **Excludes**:
  - The data publisher (Carta) is also the cap-table vendor selling
    to the issuer; findings that would embarrass the customer
    (year-4 zero-refresher rates, pre-409A repricings that wiped
    underwater grants) don't get surfaced. The framing's "median
    Series C refresher is 25-50%" is computed over the cohort that
    *received* one; the denominator of "got zero" is invisible.
  - Stage coverage tilts toward funded Delaware C-corps with priced
    rounds; SAFE-only seed, bootstrapped, revenue-funded, and
    PE-backed companies are silently dropped from the benchmark.
    A "Series A senior-eng median grant is 0.25-0.75%" anchor
    misroutes for a bootstrapped reader whose right comparator is
    profit-share or phantom equity.
  - Self-reported data (levels.fyi) over-weights successful
    negotiators; the median reported TC is higher than the median
    actual TC by a self-selection band the framing rarely names.
  - The framing's percentile-talk over-anchors the asker on a
    distributional outcome that doesn't account for their personal
    leverage — being p75 with a credible competing offer should
    yield p90+, but the framing's "we benchmark against p75"
    suggests p75 as the ceiling.

## 13. Insider-signal-reading framing

- **Decisions it applies to**: D9 (Tender), D10 (Acquihire).
- **Mental model summary**: Every deal is structured by people who
  are getting paid to structure it. Tenders, secondaries, and
  acquisitions route money among founders, VCs, banks, and employees
  in different proportions, and the proportions are the story. The
  question to ask about a tender isn't "is the price fair?" but
  "who is selling, at what price, in what size?" — founder sales at
  the employee tender price are a *forward-looking signal* that
  liquidity-now beats expected value, even though the framing's
  Matt-Levine voice presents them as "this is the mechanism."
  Characteristic move: read the S-1 (when available), the tender
  pro-rata structure, the founder-secondary participation rate, and
  the lockup terms; treat the deal price as one input alongside
  the disclosed insider behavior. Anchor: the gap between the
  public-narrative price and the implied insider opinion is the
  decision-relevant variable.
- **Characteristic vocabulary**: "S-1 archeology", "founder secondary",
  "pro-rata participation", "lockup extension", "the basic story is",
  "follow the incentives", "stacked preferences", "common-stock
  waterfall", "underwriter allocation", "PIPE pricing."
- **Excludes**:
  - Treats employee tax as a downstream footnote (the unit of
    analysis is the deal, not the asker's 1040). Frames a tender
    as "founders sell $80M, VCs take preference, lockup extends"
    without flagging the NSO ordinary-income or ISO-spread AMT
    coming due that April — the asker reads a correct deal
    description and walks into a six-figure surprise tax bill.
  - Over-applies public-company / Delaware framings (appraisal
    rights, Dell, Aruba) to private-company situations where the
    binding constraint is the drag-along plus the founder re-vest,
    not governance-style protection.
  - Big-deal-centric: $500M+ M&A and IPO mechanics get covered;
    the Series B acquihire of a 30-person company and EU-equity
    instruments (BSPCE, EMI, Dutch STAK) are out of corpus.
  - Reads "insiders sell" as mechanism for the deal-narrative voice
    while forgetting it's also private information for the
    rank-and-file — the framing's "this is fine, this is how it
    works" rhetorical move under-weights the base-rate finding
    that tender-then-down-round sequences are common.

## 14. Reputation-signal framing

- **Decisions it applies to**: D4 (Pre-cliff quit), D5, D7 (PIP).
- **Mental model summary**: Career outcomes over a 10-20 year arc
  are dominated by reputation and reference network, not by any
  single comp negotiation. Decisions that look locally rational
  (quit two weeks before the cliff to take the better offer;
  accept the PIP and fight to preserve the resume narrative;
  litigate the severance dispute) can be globally costly because
  the reference call, the LinkedIn-overlap network, and the
  industry-Slack channels persist beyond any single employer. The
  framing reasons in reputational-asset units: who will speak well
  of you, what story your departure tells, how the next 3 hiring
  managers in your stack will hear about this. Characteristic move:
  optimize the *story* you can tell about a departure (and that the
  ex-employer's managers can tell on your reference call), even at
  modest dollar cost. Anchor: a strong reference from a former
  manager is worth $50-200k in next-job comp via faster offer
  velocity and higher signing leverage.
- **Characteristic vocabulary**: "burning a bridge", "reference call",
  "managed departure", "narrative around the gap", "rehire-eligible",
  "your story", "the industry is small", "warm intro from a former
  manager", "leave on good terms", "managed exit."
- **Excludes**:
  - "Industry is small" reasoning over-generalizes from the
    framing's SF/NY tech-network sample; for engineers outside
    those metros, in less network-dense subfields (govtech,
    biotech, climate hardware), the reputation-graph is sparser
    and the framing's "everyone will know" pressure is overstated.
  - Treats reputational damage as a uniform cost; in practice the
    *type* of departure that's reputationally costly varies by
    role (engineers can leave abruptly with little stigma;
    GTM/sales leaders cannot) and the framing doesn't differentiate.
  - The framing's "always leave on good terms" advice can route
    the asker into accepting genuinely-bad treatment (uncountered
    severance, unfair PIP, retaliation after protected activity)
    because confrontation is presented as universally
    reputation-destroying.
  - Generational shift: Gen-Z and younger Millennial engineers
    report on layoff / PIP / departure stories on social media
    in ways the prior cohort treated as confidential; the
    framing's "don't burn the bridge" model is based on a more
    discreet labor-market era that's eroding.

---

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`): every
  `Excludes` bullet above is a Layer 3 candidate. Highest-density
  candidates are framings 1 (AMT — modal-down-outcome, state divergence,
  cash-bind reality), 4 (concentration — early-stage impossibility,
  wash-sale interaction), 7 (retention-leverage — H-1B, demographic
  reception, org fragility), 9 (non-compete — choice-of-law,
  defense-cost gap), and 11 (asymmetric-bet — survivorship voice,
  opportunity-cost-not-modeled). Sweep all 14 framings × ~4 bullets
  each = ~56 blindspot candidates; promote ≥ 5 per framing into
  `blindspots.md` per the [`_schema.md`](../_schema.md) minimum.
- **Cross-framing tensions worth flagging in Layer 3**: framings 3
  (liquidity-preservation) vs 11 (asymmetric-bet) are direct opposites
  on early-stage offer acceptance — the user inside one is exactly
  the person the other should be challenging. Framings 4
  (concentration-risk) vs 13 (insider-signal-reading) push opposite
  directions on tender participation: the first says "sell to
  diversify"; the second says "read what insiders are doing and price
  accordingly." Triage / Risk Officer should surface the contrarian
  framing when the asker's prompt vocabulary lands on one of these
  pairs.
- **Triage routing notes**: framings 7, 8, 9, 12 carry the most
  distinctive vocabulary signatures and should be the highest-
  confidence routing matches; framings 3 and 6 share vocabulary with
  general personal-finance (cash runway, vesting) and need disambiguation
  against the `personal-finance` and other domain packs once V2 two-pass
  Triage is wired.
