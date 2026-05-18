# housing — framings.md (Layer 2)

Framing library for `housing`. Each entry names one lens — the way a
specific community / tradition argues about a decision — and lists the
decisions from [`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

The `housing` domain is **high_stakes: false** per
[`_meta_ontology.md` §3](../_meta_ontology.md) — most outcomes are
recoverable (sell, refinance, sublet, break the lease with a fee). But
several decisions below have six-figure tail risks where professional
counsel (buyer's agent, mortgage broker, real-estate attorney, CPA,
structural / pest / sewer inspector) is the correct deferral. The
Editor layer should flag the appropriate referral inline rather than
blanket-mandating one on every answer. The framings below name *axes
and trade-offs the buyer / renter / owner must reason about* — they
are decision-support pointers, not transaction advice.

Voice anchors (conceptual, not source URLs — those live in
`sources.yaml` once authored): **r/RealEstate / r/FirstTimeHomeBuyer
voice** (transactional, agent-mediated, vocabulary of "comps,"
"appraisal gap," "escalation clause"); **BiggerPockets voice**
(investor-pilled, cap-rate / cash-on-cash arithmetic, leverage as
amplifier, "house-hacking" as wedge); **Bogleheads-housing voice**
(opportunity-cost-pilled, rent-vs-buy as portfolio-allocation question,
"the New York Times calculator" as canonical artifact);
**personal-finance-blogger voice** (Mr. Money Mustache, Ramit Sethi
style — rent-vs-buy as lifestyle and total-cost-of-ownership math);
**Calculated Risk / housing-economist voice** (macro view — housing
starts, months-of-supply, price-to-rent national series, MBS spreads,
cycle-aware); **NAR / NAHB / agent-establishment voice** (institutional
optimism — "real estate always goes up," "marry the house date the
rate"); **local-market-subreddit voice** (r/Seattle, r/Austin,
r/RealEstateAustin, r/AskNYC — neighborhood granularity, school-
attendance-zone obsession, gentrification narrative); **fee-only-CFP /
CPA voice** (tax-cap and amortization math, SALT-cap, 1031, §121
exclusion, depreciation recapture); **architect / climate-resilience
voice** (Insurance Institute for Business & Home Safety, IBHS-FORTIFIED,
First Street Foundation — physical-risk-anchored); **insurance-adjuster
/ broker voice** (peril-specific deductibles, master policy gaps,
loss-assessment exposure, Florida / California non-renewal trauma);
**legal-services / tenant-union voice** (landlord-tenant statute,
rent-stabilization mechanics, eviction-process timeline by state);
**mortgage-broker / loan-officer voice** (rate-sheet weekly, ARM
margin / cap structure, conforming vs jumbo cliff, lender-credit
arithmetic).

Cross-domain edges: D1, D4, D7 boundary `tech-career` (employer
stability and relocation probability shape buy-vs-rent and rate
structure); D3, D4, D7, D8, D9, D10 boundary `personal-finance`
(opportunity-cost-of-cash, mortgage-as-leveraged-position, §121
exclusion, SALT cap, depreciation recapture); D1 boundary
`immigration` (status-driven exit within break-even horizon makes
buying worse-than-default); D6, D10 boundary `family-planning`
(school-district premium, eldercare-ADU alternative to assisted
living); D2, D9 boundary `legal-disputes` (security-deposit recovery,
tenant-friendly eviction regimes). Routing across edges is V2-Triage's
job; these edges help framings name adjacent domains rather than
absorb their content.

---

## 1. Financial-return framing

- **Decisions it applies to**: D1 (Rent vs buy), D3 (Down-payment
  size), D8 (Refinance trigger), D9 (Investment property vs index).
- **Mental model summary**: A primary residence is a leveraged asset
  with an embedded short call on rent (you avoid future rent
  increases) and an embedded long call on property appreciation. The
  framing reasons in IRR, after-tax cash-on-cash, and risk-adjusted
  total return: down-payment is a partial cash purchase of a
  leveraged real-asset position; the mortgage is the leverage; the
  alternative is the equivalent capital in a diversified market
  portfolio with the equity-risk-premium attached. The decision is
  always "what's the after-tax, after-cost return on the capital I'd
  deploy in housing vs the next-best deployment, accounting for
  leverage, transaction friction, and the option value of the
  refinance / sell-and-move events." Characteristic move: build a
  spreadsheet that includes all the boring line items (PITI,
  maintenance at 1–2% of value/yr, capex reserve, vacancy if rental,
  property management, opportunity-cost-of-down-payment compounded
  at expected market return) and let the IRR fall out — usually the
  rent-vs-buy answer is *not* "buying wins" once the boring items
  are honest. Anchor numbers: 6–10% round-trip transaction cost
  (agent commissions + closing + moving), 1–2%/yr maintenance,
  ~50bps/yr CapEx reserve on top of maintenance, 8–10% expected
  equity-portfolio return for the alternative.
- **Characteristic vocabulary**: "rent-vs-buy break-even", "the NYT
  calculator", "price-to-rent ratio", "5% rule (Felix Salmon /
  Khan)", "IRR on housing", "opportunity cost of down payment",
  "after-tax cap rate", "cash-on-cash return", "leverage cuts both
  ways", "mortgage interest as deductible leverage", "Sharpe ratio
  of housing as asset class."
- **Excludes**:
  - Frames housing purely as an asset; misses that *consumption*
    value (security of tenure, ability to renovate, freedom from
    landlord intrusion) is real and not captured in IRR. The
    framing's "renting is mathematically superior at price-to-rent
    > 20" advice is structurally correct but routes users toward
    decisions that under-weight their own preferences. Opposes F2,
    F4.
  - Treats the maintenance reserve as a deterministic line item;
    misses that maintenance is *lumpy* — the roof replacement, HVAC,
    sewer line, foundation work are 5-figure surprises every 7–15
    years that the 1–2%/yr average smooths over in a way that
    decouples cash-flow planning from reality. The honest framing
    is "average 1.5%/yr, but with $25k punches every ~8 years."
  - Opportunity-cost-of-down-payment-invested presumes the
    counterfactual user actually invests the difference. In
    revealed-preference data (housing-counsel papers, FRED household
    saving rate), renters who don't buy don't tend to invest the
    delta in equities; the cash sits at <2% in checking. The
    framing's "buy with 5% down, invest the difference" arithmetic
    overstates the realistic counterfactual return.
  - Ignores the forced-savings function of mortgage principal
    payment for households without disciplined investment habits.
    The Mr. Money Mustache / Bogleheads counter-argument that
    "amortization is just savings" is technically correct but
    discounts the behavioral wedge for the modal buyer who would
    otherwise not save the principal.
  - Doesn't price *psychological* drag of being underwater (an
    upside-down mortgage creates immobility — can't relocate for
    a 30% raise, can't accept job in different metro). The
    leverage-amplifies-returns story has a leverage-amplifies-
    immobility shadow.

## 2. Lifestyle-flexibility framing

- **Decisions it applies to**: D1 (Rent vs buy), D2 (Lease length),
  D5 (Property type), D7 (Sell-and-buy sequencing).
- **Mental model summary**: Housing is the *physical environment of
  daily life* — the constraint on where you sleep, eat, work, and
  raise children for the next N years. Reasoning is in optionality-
  preservation and life-trajectory-uncertainty terms: at 25 with an
  unclear career, the value of being able to move cities on 30 days'
  notice is high; at 40 with a 7-year-old in school, the value of
  not being able to move (commitment to school district, neighbor
  network) is high. The framing's reflex on every decision: how
  *fungible* is the housing choice with the rest of life — can I
  re-optimize without a 6-month, $50k transaction event? Buying
  trades flexibility for stability; renting trades stability for
  flexibility. Shorter leases trade rent-rate-premium for option to
  move; longer leases trade option for rate. Characteristic move:
  honest base-rate on "how likely am I to want to move in the next
  3 / 5 / 10 years" using the asker's own history (number of moves
  in last decade is a better predictor than the asker's stated
  intent), the partner's career trajectory, and the macro mobility
  of the asker's industry / role.
- **Characteristic vocabulary**: "optionality", "5-year rule",
  "break-even horizon", "lock-in cost", "exit liquidity", "renting
  is freedom", "selling on short notice eats the equity",
  "underwater immobility", "you can't refinance into a new life",
  "the marginal year of holding pays for the round-trip cost."
- **Excludes**:
  - Treats flexibility as monotonically valuable; misses that for
    some households the *constraint* of a 30-year mortgage produces
    long-horizon commitment effects (neighborhood roots, social-
    capital accumulation, kids' school continuity) that the
    flexibility framing under-prices.
  - "5-year rule" is a transaction-cost heuristic, not a flexibility
    heuristic. Selling at year 4 costs 6–10% of value in round-trip
    friction — the financial cost is the binding constraint, not
    "you didn't get enough flexibility value." Conflating the two
    leads to "I should buy because I'm staying 5+ years," which
    skips the price-to-rent check.
  - Under-weights that *renting itself has lock-in events* — the
    annual lease renewal, the security-deposit pull-forward, the
    14-day notice clock to vacate, the rent-hike timing the
    landlord chooses. The framing's "I'm free as a renter" is
    structurally true but operationally over-stated. Opposes F12.
  - "I might move for a job" assumes the move is the asker's
    initiative. Layoffs, family illness, and partner career events
    are externally-imposed move triggers the flexibility-framing
    handles correctly but the asker's stated horizon under-weights
    relative to base rates. Cross-routes `tech-career`.
  - The framing treats the buy-vs-rent decision as bidirectional
    optionality; in practice transitioning from owning to renting
    requires selling first, which is itself a 60–120 day operation
    in a normal market and 6–12 months in a slow one. Optionality
    on the way *out* of homeownership is asymmetric.

## 3. Household-stability framing

- **Decisions it applies to**: D1 (Rent vs buy), D2 (Lease length),
  D6 (Location within metro), D10 (House-hacking / ADU).
- **Mental model summary**: Housing is the *container for the
  household* — a partner, children, aging parents, pets, the texture
  of nightly dinner and weekend routine. The framing reasons in
  household-cohesion-and-rootedness terms: the value of *not* moving
  is the value of children continuing in the same school, the
  partner not re-commuting, the dog knowing the block, the
  neighbor-network calling 911 if something looks wrong. Buying
  signals — to landlord, to neighbors, to oneself — that this
  household is staying; renting (especially short leases) signals
  the opposite. The framing's reflex on every decision: what does
  this do to household-cohesion and to the long-arc obligations the
  household has implicitly made (school, eldercare, partner career).
  Characteristic move: weight the qualitative-stability factors as
  if they had a 6-figure dollar number attached, because they
  empirically do in life-satisfaction research and child-outcomes
  literature.
- **Characteristic vocabulary**: "putting down roots", "the kids'
  school", "the neighborhood", "block social capital", "we want a
  place that's *ours*", "aging in place", "the dog needs a yard",
  "I want to stop counting the months on the lease", "stability for
  the kids", "this is home."
- **Excludes**:
  - Conflates the *consumption* value of stability with the *
    investment* commitment of ownership. Stability can be purchased
    with a long lease (24–36 months) in many markets without the
    leverage exposure of a mortgage; the framing's reflex jumps to
    "buy to stop renting" when a long-term lease in a non-rent-
    controlled market is often the cheaper purchase of the same
    stability good. Opposes F1.
  - Stability is *durable only if the underlying environment
    doesn't change*. Buying into a fast-gentrifying neighborhood
    locks in the *house* but the schools, commute, and neighbor
    set change anyway; buying into a declining neighborhood locks
    in both the house and a slow erosion of the household-stability
    good the framing was buying. The framing rarely names that
    "rootedness" is partly an environmental, not legal-contractual,
    good.
  - Under-weights divorce / separation / partner-death scenarios in
    the household-stability arithmetic. Joint ownership creates
    legal partition-of-asset friction that joint tenancy on a lease
    does not; the framing's "we're building a life together"
    presumes the life-together continues, and the legal exit costs
    are higher than the framing names.
  - "Aging in place" presumes the house remains physically suited
    to aging (single-floor or elevator, ADA-friendly bathrooms,
    walkable to medical). Most US single-family stock fails these
    criteria; the framing routes asker into a stability-good that
    becomes a mobility-trap at 75. Cross-routes `family-planning`.
  - Doesn't engage with that the *household* is a moving target —
    children leave home, partners' careers diverge, aging parents
    join (cross-routes F10 on ADU). The "stable forever home" the
    framing builds toward is a snapshot of a 15-year window, not a
    30-year mortgage horizon.

## 4. Total-cost-of-ownership framing

- **Decisions it applies to**: D1 (Rent vs buy), D3 (Down-payment
  size), D5 (Property type), D6 (Location within metro).
- **Mental model summary**: The mortgage payment (P&I) is the
  *visible* cost; the *invisible* costs — property tax, insurance,
  HOA, maintenance, CapEx reserve, utilities (higher in SFR than
  apartment), commute cost, time cost of yard / repair labor — add
  up to a multiplier on the visible cost. The framing reasons in
  fully-loaded monthly cost-per-square-foot and per-year-of-tenure
  terms: the comparable to a $3,500/mo rent is *not* the $3,500/mo
  P&I, it's $3,500 P&I + $700 tax + $200 insurance + $400 HOA + $400
  maintenance + $300 CapEx = ~$5,500/mo, plus the down-payment
  opportunity cost. The framing's reflex on every decision: what
  are the line items the seller / agent / mortgage broker is
  *not* showing me. Characteristic move: build a 12-row monthly
  cost table that includes every recurring line item, including
  the ones that fire every 5–10 years amortized to monthly
  ($500/mo CapEx for the $40k roof at year 10), and compare
  against rent at the same square-footage / commute / school
  zone. Anchor numbers: maintenance 1–2%/yr of value, CapEx 0.5%/
  yr on top, property tax 0.5–2.5%/yr depending on state, HOA $0
  (SFR) to $1k+/mo (full-service condo).
- **Characteristic vocabulary**: "PITI" (principal-interest-tax-
  insurance), "PITIA" (with HOA), "fully loaded monthly", "the
  hidden cost is the cost", "maintenance ate the appreciation",
  "deferred maintenance is debt", "the boring line items",
  "lifetime cost per sqft", "operating expense ratio", "the
  agent's payment-calculator lies."
- **Excludes**:
  - Computes the cost honestly but doesn't engage with the *
    benefit* side beyond market rent — for owner-occupiers the
    consumption value (renovation freedom, no landlord, garden,
    pet rules) is real and not captured in rent-comp. The
    framing's "your $5,500 fully-loaded vs $3,500 rent → don't
    buy" routes asker out of valid decisions. Opposes F3.
  - Maintenance averaging hides the variance. A buyer who computes
    1.5%/yr × $700k = $10,500/yr ÷ 12 = $875/mo is correct in
    expectation and wrong in cashflow planning — the actual
    pattern is $1,500 in year 1, $0 in year 2, $25,000 in year 8,
    etc. The framing's monthly-amortization view obscures the
    liquidity reserve required to survive the lumpy reality.
  - Property-tax projection assumes current-millage; misses that
    in CA (Prop 13) the basis resets on transfer and your tax bill
    is dramatically higher than the seller's — the listing's
    "property tax: $4,000/yr" is the seller's basis, not yours;
    in TX / FL post-purchase reassessment can be 50%+ higher than
    the listing shows.
  - HOA cost is a *current* number; doesn't engage with
    special-assessment trajectory (post-Surfside FL condo
    reserves, CO HB 23-1233 reform). The framing's "$400/mo HOA"
    can be "$400/mo + $15k special assessment in year 3" and the
    static cost view doesn't catch this. Cross-routes F8.
  - "Compare against rent at same sqft" presumes a 1-to-1 rental
    comparable exists. In SFR-dominated markets (Austin, Phoenix,
    much of suburban Atlanta), there's no equivalent 3BR/2BA SFR
    rental within 30% of the buy's square footage; the framing's
    apples-to-apples comparison breaks down and the analyst either
    inflates the rent (to make buying look better) or accepts the
    apartment as comp (to make renting look better).

## 5. Rate-trajectory framing

- **Decisions it applies to**: D1 (Rent vs buy), D4 (Fixed vs ARM),
  D8 (Refinance trigger).
- **Mental model summary**: Mortgage rates move with the 10-year
  Treasury plus an MBS spread; in a falling-rate environment, the
  refi option is valuable (free embedded put — you keep your rate
  if rates rise, refinance if they fall); in a rising-rate
  environment, locking the 30-year fixed is locking in cheap
  capital before it disappears. The framing reasons in macro-rate-
  forecast terms: where is the Fed, what's priced into Fed Funds
  futures, what's the MBS-Treasury spread relative to history, what
  did the last 12 months of Treasury yields do. The framing's reflex
  on every decision: what does the rate path imply for the choice —
  ARM only if you expect rates to fall or to move before reset; refi
  only if rates have fallen enough to clear closing-cost break-even;
  rent only if the locked rate is so high that current PITI exceeds
  rent by > X%. Characteristic move: refuse to buy in the top of a
  rate cycle when the rent-vs-buy math depends on a refinance
  within 18 months — that's pricing in a Fed pivot the futures
  curve may not deliver. Anchor: 30-year fixed has averaged ~6.5%
  over the last 50 years; sub-3% rates of 2020–21 were a generational
  outlier, not a baseline.
- **Characteristic vocabulary**: "rate cycle", "10-year Treasury",
  "MBS spread", "Fed pivot", "duration risk", "marry the house,
  date the rate", "refi option value", "lock-vs-float", "discount
  points break-even", "yield-curve inversion as recession signal."
- **Excludes**:
  - "Marry the house, date the rate" is structurally optimistic
    about refi availability. In 1980, the 30-year fixed hit ~18%;
    rates fell back below 10% only in 1986 — six years of "dating
    the rate" with no exit. The framing's reflex assumes a refi
    window opens within the holding period; in long-duration
    high-rate regimes that's wrong. Opposes F1's break-even math.
  - Rate forecasts are weakly accurate beyond 6 months. The
    framing's "we expect rates to fall" depends on forecasts that
    professional rate strategists explicitly disclaim. The honest
    framing is "we don't know — buy the house if the math works
    at *today's* rate and the refi is upside."
  - ARM-vs-fixed decision depends on *index-and-margin-and-cap-
    structure* (most have 2/2/5 caps), which is not the same as
    "ARM is X% lower." A 5/1 ARM at 5.875% with a 2/2/5 cap can
    reset to 7.875% / 9.875% / 10.875% — the framing's "ARM is
    cheaper for 5 years" is honest only if the buyer can afford
    the cap. Cross-routes F12.
  - Discount-point arithmetic ("pay 1 point to buy down 25bps")
    breaks even in 4–6 years at typical rates; the framing's "buy
    points to lower the rate" presumes hold-to-break-even, which
    contradicts the framing's other reflex (refi when rates fall).
    A buyer who pays points and refis in 18 months has paid for a
    rate they didn't use. Opposes F8 (refinance).
  - Treats rate as the only mortgage variable; doesn't engage with
    lender credit (the inverse of discount points), pricing exception
    on relationship (some banks shave 12.5–25bp for AUM-tied
    customers), or builder-finance buy-downs (2-1 buy-downs are
    builder-funded rate-temporaries that the framing rarely names).

## 6. Household-cashflow framing

- **Decisions it applies to**: D2 (Lease length), D3 (Down-payment
  size), D4 (Fixed vs ARM), D7 (Sell-and-buy sequencing).
- **Mental model summary**: Housing cost is the largest line item
  in most household budgets; the binding constraint on every
  housing decision is "what can the household *cashflow* without
  forcing other compromises (savings rate, vacation, kids'
  activities, eating out, retirement contributions)." The framing
  reasons in front-end DTI (housing ÷ gross income), back-end DTI
  (total debt ÷ gross income), and the *real* household budget
  the lender doesn't see (daycare, parent care, debt-payoff
  contributions, savings targets). The framing's reflex on every
  decision: what does this do to the monthly free cashflow
  *after* every other obligation. Characteristic move: refuse
  to buy at the lender's maximum approval (which can be 45% DTI);
  cap housing at 28–30% of gross income (or 25% of net) so the
  household retains shock-absorption capacity. Anchor: lender's
  "you qualify for $900k" is *not* the same as "you can afford
  $900k"; the lender prices default risk, not life-quality risk.
- **Characteristic vocabulary**: "front-end DTI", "back-end DTI",
  "28/36 rule", "house poor", "the lender will let you, but you
  shouldn't", "the *real* budget", "shock-absorber savings",
  "emergency fund post-close", "payment-shock tolerance",
  "household runway."
- **Excludes**:
  - 28/36 rule was calibrated for 1970s-era housing-to-income
    ratios; in HCOL metros (SF, NYC, Seattle, Boston) modal tech-
    worker buyers carry 35–45% front-end DTI without obvious
    distress because compensation is heavily skewed toward equity /
    bonus the rule doesn't model. The framing's "house poor at >
    28%" is calibrated to a different income structure than the
    modal asker. Opposes F1 in HCOL contexts.
  - Treats household cashflow as if base-salary is the binding
    constraint; for tech-worker askers a meaningful chunk of comp
    is RSU / bonus that may or may not vest. The framing's
    "compute DTI on base only" is conservative, but the framing's
    "compute DTI on total comp" is over-aggressive — both because
    RSUs are price-sensitive (down 60% from 2021 peaks across many
    public-tech) and because variable comp can be cut. Cross-
    routes `tech-career`.
  - Under-weights childcare / eldercare line items that scale
    with house location. A "we can afford this house" calculation
    that ignores the $30k/yr daycare in the school-district premium
    neighborhood is structurally wrong; the framing names the
    cashflow constraint but rarely names the location-dependent
    line items that go *with* the housing choice.
  - "Cap at 28% to preserve flexibility" presumes the alternative
    use of the cash is value-creating (savings, debt payoff,
    retirement). For households without disciplined savings
    behavior, the 12% of income the framing protects often
    dissipates into lifestyle inflation rather than the financial-
    security goal. The framing's "trust the household to deploy
    the freed cashflow" is empirically optimistic.
  - ARM-vs-fixed-vs-15yr decision is partly a *forced savings*
    question that this framing under-weights — the 15-year
    mortgage compels principal accumulation; the 30-year preserves
    cashflow flexibility. The framing's reflex toward "more
    cashflow flexibility = better" trades against the F1 reflex
    toward forced-savings discipline.

## 7. Duration-of-stay framing

- **Decisions it applies to**: D1 (Rent vs buy), D2 (Lease length),
  D4 (Fixed vs ARM), D7 (Sell-and-buy sequencing).
- **Mental model summary**: The right housing choice is a function of
  *expected holding period*. ARMs are correct when the holding
  period is bounded below the reset (5/1 ARM if expected sale or
  refi by year 5; 7/1 if by year 7); 15-year fixed makes sense if
  holding to payoff; rent-vs-buy depends on break-even-horizon (the
  point where cumulative ownership costs minus cumulative rent
  savings cross zero, typically 4–7 years depending on price-to-
  rent and rate environment). The framing reasons in expected-
  holding-distribution terms: not a point estimate but a
  distribution — base rate of actual moves vs intended moves
  diverges sharply (median first-home tenure ~13 years per NAR,
  but mean is shorter due to long right-tail; cluster of moves
  at year 3–5 driven by job change, family change, dissatisfaction).
  The framing's reflex on every decision: what's the expected hold,
  what's the 25th-percentile hold (move sooner than expected), and
  does the choice survive both. Characteristic move: stress-test
  every decision against a 3-year hold (would I be OK if I had to
  sell in 3 years) — if no, the choice is fragile to externally-
  imposed move triggers (layoff, family illness, partner career).
- **Characteristic vocabulary**: "expected holding period", "break-
  even horizon", "the 5-year rule", "stress-test the hold", "ARM
  reset horizon", "duration risk on transaction costs",
  "median-vs-mean tenure", "the move you didn't plan for", "exit-
  in-three-years test."
- **Excludes**:
  - Treats expected-hold as a planning input; misses that the
    *actual* hold is a function of life-shocks (layoff, divorce,
    illness, family event) that the buyer can't predict and the
    base-rate distribution under-weights for a specific asker.
    The framing's "I'm staying 10 years" is a stated intent that
    revealed-preference data flatly contradicts for 25–35% of
    first-time buyers (NAR data: ~25% sell within 5 years).
  - "Stress-test against 3-year hold" produces a conservative
    answer but doesn't engage with the asker's *reasons* — a
    35-year-old single-income tech worker has a different
    transaction-cost-amortization than a 50-year-old dual-income
    family. The framing's uniform stress-test under-personalizes.
  - Under-weights the option-value of *not* moving when life-events
    permit. A 7/1 ARM at 5.875% saved over 30-year fixed at 6.75%
    has positive value at year 5 *if* the buyer can refi or sell;
    if neither (rates higher, market frozen, life events block
    sale), the buyer takes the full reset. The framing prices the
    expected case but under-prices the joint failure of "rates up
    AND family event keeps you stuck."
  - The framing's break-even arithmetic depends on transaction
    cost (6–10% round-trip); doesn't engage with the *softer*
    costs — the move itself is 2–4 weeks of household time, the
    new-home settling-in is 6–12 months of friction, the kids'
    school transition is its own multi-year cost. These don't
    fit the break-even table but bind the move-or-stay decision
    in practice.
  - "Duration of stay" presumes a binary stay-or-leave; the
    actual pattern includes *partial* moves (the partner takes a
    job in another city, the household maintains two residences
    for 18 months, then consolidates). The framing's stay-vs-leave
    binary doesn't handle this hybrid mode.

## 8. Climate-and-insurance-risk framing

- **Decisions it applies to**: D5 (Property type), D6 (Location
  within metro), D9 (Investment property), D10 (House-hacking /
  ADU).
- **Mental model summary**: Physical-risk exposure (wildfire,
  hurricane, storm surge, inland flood, hail, freeze, sea-level rise,
  extreme heat) is being repriced into the insurance market faster
  than into property prices. The framing reasons in
  peril-and-trajectory terms: what perils does this property face
  (FEMA flood zone, IBHS-FORTIFIED roof eligibility, First Street
  Foundation risk score, state-fire-marshal wildfire designation),
  what is the trajectory of insurance availability (FL, CA, LA
  non-renewals; State Farm CA exit 2023; Citizens FL as last-resort
  insurer), and what is the trajectory of climate exposure (10-year,
  30-year mortgage horizon — risk pricing today reflects 2020s
  climate, not 2050s). The framing's reflex on every decision: get
  the multi-year insurance-quote trajectory before buying (request
  current premium and prior-3-year history), check the FEMA flood
  map AND the First Street Foundation private risk score (FEMA
  under-prices outside designated zones), price the special-
  assessment risk on condos in coastal / older-construction stock.
  Characteristic move: subtract the present value of a 5-year
  insurance-premium-doubling from the offer price; refuse to buy in
  insurance-non-renewing markets without a 5-year written premium
  commitment from the broker. Anchor: FL average homeowner premium
  rose ~3× 2018–2024; some CA wildfire zones saw 5× over the same
  window; uninsurable properties trade at 20–40% discounts and have
  effectively no exit liquidity.
- **Characteristic vocabulary**: "FEMA flood zone (X, AE, VE)",
  "First Street risk score", "FORTIFIED roof", "wildfire urban
  interface", "WUI", "insurance non-renewal", "Citizens (FL)",
  "FAIR Plan (CA)", "loss-assessment master policy gap",
  "special assessment trajectory", "climate alpha vs beta", "the
  insurance market is the canary."
- **Excludes**:
  - Frames insurance as the right price signal; misses that the
    insurance market is *itself* mis-priced — state-mandated
    insurer-of-last-resort programs (Citizens FL, FAIR CA) cap
    premiums below true risk, and the catastrophic tail risk is
    being absorbed by taxpayers via state-bailout mechanisms. The
    framing's "let the insurance market tell you the risk" works
    until it doesn't.
  - Climate-risk trajectory is over 30 years; insurance pricing is
    typically annual. The framing's "premium trajectory" signal
    lags the underlying risk by 5–15 years — a property that's
    safely insurable today may be uninsurable by 2035, and the
    current premium doesn't carry that information. The framing's
    "watch the premium" is reactive, not anticipatory.
  - Under-weights *property-level* risk mitigation (defensible
    space, IBHS-FORTIFIED retrofit, basement-pump and french-drain
    flood mitigation, hurricane-shutter installation). The framing
    routes asker out of high-risk zones rather than naming that
    a $30k IBHS-FORTIFIED retrofit can preserve insurability and
    sometimes secure premium discounts. Cross-routes F4.
  - First Street Foundation and similar private risk scores are
    *modeled* (not measured) and have their own bias structure
    (over-weighting riverine flood, under-weighting urban-stormwater
    flood in some metros). The framing presents the score as
    ground truth when it's a model output the buyer should
    triangulate against FEMA, state hazard maps, and local
    historical data.
  - The framing protects against catastrophic loss but doesn't
    engage with the *liquidity* dimension — an uninsurable
    property in a non-renewing market has no buyer pool, and the
    discount to clear is much larger than the present value of
    avoided premium increases. The framing prices the wrong
    variable; the binding constraint is "can I exit this property
    in 3 years if I need to."

## 9. School-district-and-neighborhood-premium framing

- **Decisions it applies to**: D6 (Location within metro), D1
  (Rent vs buy), D7 (Sell-and-buy sequencing).
- **Mental model summary**: Within a metro, school-district quality
  (proxy: GreatSchools rating, test scores, college-matriculation
  pattern) attaches a 15–30% price premium to comparable houses on
  the school-zone boundary. The framing reasons in
  zone-arbitrage and child-outcome terms: pay the premium for the
  schooling outcome, OR pay private-school tuition ($30–60k/yr) and
  buy in a lower-zoned area, OR opt out (homeschool, magnet, charter)
  and capture the price arbitrage. The framing's reflex on every
  decision: which school zone is this property in, what's the
  premium relative to the boundary, what's the zone-change risk
  (school-board redistricting events). Characteristic move: walk
  the school-zone boundaries on the GIS map before touring houses;
  pay for a buyer's agent who knows which streets are in which zone
  (boundary properties can be on either side of an arbitrary
  street, and listings sometimes mis-report); price the zone change
  risk (school board votes are 5–10-year recurring events).
- **Characteristic vocabulary**: "GreatSchools rating",
  "elementary feeder pattern", "high school zone", "boundary
  street", "redistricting risk", "magnet lottery", "charter
  proximity", "school zone premium", "private school vs zone
  arbitrage", "test-score-vs-peer-effect."
- **Excludes**:
  - GreatSchools and similar ratings are dominated by test scores;
    test scores correlate with neighborhood demographics more than
    with school value-add. The empirical research on "school
    effects" controlling for peer composition is much weaker than
    the rating implies — the framing routes asker into the
    premium price for a signal that's partly demographic sorting,
    not differential education quality.
  - "Pay private tuition and buy in cheaper zone" arithmetic looks
    appealing for K-12 ($30–60k/yr × 13 years = $390–780k of
    tuition) but the framing under-weights that private-school
    families also pay for the high-zoned house (peer effects on
    *adult* networks, neighbor-set, parent social capital). The
    arbitrage is real but smaller than the headline math suggests.
  - Boundary-street redistricting risk is named but rarely
    quantified — the framing flags it without giving the asker a
    process for assessment (read the past 3 school board meeting
    minutes; check enrollment-projection reports; assess the
    political-coalition stability around the current zone lines).
  - The framing presumes the asker's kid will attend public school
    in this zone for the full duration. Doesn't engage with
    school-mismatch (the kid hates the school, the school's
    pedagogy is wrong for the kid, the kid develops special-ed
    needs the zone school can't serve well) that converts the
    "we bought for the school" thesis into a property-and-tuition
    double-pay. Cross-routes `family-planning`.
  - Under-weights the *commute* delta. A top-zoned house 40min
    from work trades the school premium against 80min/day of
    commute (= ~6 hours/wk of life). The framing's "the schools
    are worth it" gets weighted against the F2 (lifestyle-
    flexibility) reflex; the asker needs both axes priced.

## 10. Investor-leverage / cap-rate framing

- **Decisions it applies to**: D3 (Down-payment size), D9
  (Investment property vs index), D10 (House-hacking / ADU).
- **Mental model summary**: An investment property is a leveraged
  bet on cap rate, rent growth, appreciation, and the financing
  spread. The framing reasons in cap-rate (NOI ÷ price), cash-on-
  cash (after-financing cashflow ÷ cash invested), debt service
  coverage ratio, internal rate of return, and 1031-exchange
  optionality. The framing's reflex on every decision: what's the
  cap rate (5–7% in most US metros for SFR rentals; lower in
  coastal HCOL), what's the cost of leverage (6–8% mortgage rate
  for investor loans + 50–100bp premium over owner-occupied), and
  is leverage *positive* (cap rate > debt service rate, you earn
  the spread) or *negative* (debt cost > cap rate, you pay to
  hold). Characteristic move: refuse to buy negative-leverage
  rentals on the appreciation thesis alone; require positive
  cash-on-cash of 6–8% post-vacancy / -CapEx / -management as the
  hurdle rate; pair every property with a 1031-exchange exit plan
  (sell-and-trade-up rather than realize gain) to defer tax. Anchor
  numbers: 10% of rent for property management, 5% vacancy, 5–10%
  combined for CapEx + maintenance reserves, $250k Section 121
  exclusion (primary) vs no exclusion (investment).
- **Characteristic vocabulary**: "cap rate", "NOI", "cash-on-cash",
  "DSCR (debt service coverage)", "positive leverage / negative
  leverage", "1031 exchange", "depreciation schedule
  (27.5 yr residential)", "real estate professional status",
  "passive activity loss limit ($25k MAGI < $100k)", "BRRRR
  (buy-rehab-rent-refi-repeat)", "house hack as wedge."
- **Excludes**:
  - Cap-rate arithmetic uses *current* rent and *current* expenses;
    misses that rent-growth projections vary 5× by metro and that
    rent-stabilization regimes (NYC, SF, LA, Oregon statewide,
    parts of NJ) cap upside. The framing's "5% cap rate plus
    rent growth" assumes a free rent-growth model that doesn't
    hold in regulated jurisdictions. Cross-routes `legal-disputes`.
  - Depreciation deduction lowers current taxable income; the
    framing prices the *current* benefit but under-prices the
    depreciation-recapture obligation at sale (25% recapture
    rate vs 0–20% capital gains). For a hold-to-death scenario
    the step-up-in-basis erases the recapture; for active trade-
    up scenarios the recapture is a real drag the framing rarely
    surfaces honestly. Cross-routes `personal-finance`.
  - "Real estate professional status" unlocks active-loss treatment
    against W-2 income but requires 750+ hours/yr of qualifying
    real-estate activity and >50% of total work time. For
    full-time-employed tech workers this status is generally
    unavailable; the framing's "depreciation offsets your W-2" is
    correct only for spouses or after-tech-exit.
  - Under-weights *operational drag* — tenant selection, eviction
    process (3–18 months by state), repairs at 2am, property-
    management-vs-self-management decision. The framing's cap-rate
    math assumes operations are frictionless; in practice the
    self-managing landlord loses ~10% of cap rate to time-cost the
    spreadsheet doesn't model.
  - The framing prices the asset in isolation; doesn't engage with
    *concentration risk* — a single $700k rental is 3–10× a
    typical investor's portfolio asset, undiversified across
    geography and tenant. The framing's "leverage amplifies
    return" is true and the "concentration amplifies tail risk"
    is the inverse the framing rarely names.

## 11. Transaction-cost-amortization framing

- **Decisions it applies to**: D1 (Rent vs buy), D7 (Sell-and-buy
  sequencing), D8 (Refinance trigger).
- **Mental model summary**: Real-estate transactions are *expensive
  one-way doors*: 5–6% seller agent commission, 1–3% closing costs
  (title, escrow, transfer tax, recording fees by state), 1–2%
  buyer-side closing, 0.5–1.5% moving and rehab — total round-
  trip cost 8–12% of the property value. The framing reasons in
  amortization-horizon terms: every transaction needs a holding
  period long enough for appreciation + amortization principal +
  rent-equivalent savings to clear the 8–12% drag; otherwise the
  buyer locks in a loss the first day of ownership. The framing's
  reflex on every decision: how many years of holding does this
  decision require to clear the round-trip cost, and what's the
  base-rate probability the asker actually holds that long.
  Characteristic move: refuse to buy on a < 5-year horizon
  regardless of how "good the deal looks"; treat refinance closing
  costs ($5–12k typical) the same way — refinance only when the
  monthly savings × expected hold-to-refi exceeds the closing
  cost by 50%+; treat home-improvement renovations as transaction
  costs (you usually don't recover them at sale, contrary to
  HGTV-fueled assumptions). Anchor: NAR data shows ~7% of buyer
  cost is agent commission; in some states (NY, NJ, MA, parts of
  the South) add a real-estate-attorney fee ($1–3k).
- **Characteristic vocabulary**: "round-trip cost", "closing
  costs", "title and escrow", "transfer tax", "5-year rule",
  "break-even months", "the round-trip eats your appreciation",
  "renovation cost-recoupment ratio (Cost vs Value report)",
  "the agent's commission is real", "FSBO arithmetic".
- **Excludes**:
  - The 8–12% round-trip is an average; for some property types
    (luxury condos, specialty homes, climate-stressed markets)
    selling friction is 15–25% (longer days-on-market, larger
    price concessions, multiple price drops). The framing's
    flat number under-prices illiquid niches.
  - "5-year rule" is necessary but not sufficient. Buying for 5
    years at the top of a rate cycle into a falling-price
    environment can still clear the round-trip on appreciation
    arithmetic but leave the buyer with no exit liquidity. The
    framing's break-even math assumes a continuous-pricing market
    and ignores days-on-market expansion in turning markets.
  - Refinance arithmetic ("save $300/mo, pay $9k closing, break
    even in 30 months") doesn't account for amortization-clock
    reset — refinancing from year 7 of 30 to a new 30 re-extends
    payoff by 7 years. The framing's monthly-savings view ignores
    the lifetime-interest-paid increase. Cross-routes F1.
  - Renovation cost-recoupment ratios from Remodeling Magazine's
    Cost vs Value report are *median* numbers; outliers (over-
    improving for the neighborhood, kitchen renovations into a
    declining market, owner-installed work that depreciates resale)
    can recoup < 50%. The framing names the recoupment ratio but
    rarely names the variance.
  - The framing treats commission as an unavoidable line item;
    doesn't engage with the buyer-agent commission post-2024 NAR
    settlement (commissions are now explicitly negotiable;
    listings cannot publish buyer-side commission; buyers
    increasingly sign written buyer-agency agreements that fix
    fee). The framing's "5–6% is the cost" is calibrated to a
    regime that just changed.

## 12. Tenant-rights / landlord-tenant-statute framing

- **Decisions it applies to**: D2 (Lease length), D9 (Investment
  property), D10 (House-hacking / ADU).
- **Mental model summary**: Landlord-tenant relationships are
  governed by state and city statute that varies widely — security-
  deposit caps and return-window (CA: 21 days, NY: 14 days, TX: 30
  days), notice-to-vacate periods (30 / 60 / 90 days varying by
  tenancy length), rent-control / rent-stabilization (NYC 1947+
  stabilization, SF, LA RSO, Oregon statewide 10%+CPI cap,
  Minneapolis 3% cap pending), eviction process timelines
  (3–6 months in tenant-friendly states; 30–60 days in landlord-
  friendly), warranty-of-habitability standards, retaliation
  prohibitions, and just-cause-eviction requirements. The framing
  reasons in jurisdictional-statute terms: what does the local law
  permit, what's the landlord's recourse, what's the tenant's
  recourse, and how do these shape the lease decision (tenant
  side) and the investment decision (landlord side). The framing's
  reflex on every decision: read the state statute and the local
  ordinance before signing; never assume landlord-side or tenant-
  side facts portable across jurisdictions. Characteristic move:
  for tenants — check rent-stabilization status of the building,
  document move-in condition obsessively, know the security-
  deposit-return clock; for landlords — model the eviction-process
  cost (lost rent + legal fees + property damage) into the cap-
  rate calculation; price the rent-stabilization regime as a
  permanent rent-ceiling, not a temporary inconvenience.
- **Characteristic vocabulary**: "warranty of habitability",
  "security deposit return clock", "just-cause eviction",
  "rent stabilization vs rent control", "Costa-Hawkins (CA)",
  "Ellis Act (CA)", "loft law (NYC)", "right of first refusal
  (DC TOPA, MA condo conversion)", "constructive eviction",
  "retaliatory eviction", "tenancy at sufferance",
  "holdover proceedings."
- **Excludes**:
  - Treats statute as the operative reality; misses that
    *enforcement* varies — a tenant-favorable statute in a
    jurisdiction without legal aid funding means the tenant's
    nominal rights aren't operational without $5–15k in attorney
    fees. The framing's "you have the right to X" is structurally
    true and practically often dead-letter.
  - The framing prices the security-deposit and just-cause angles
    correctly but under-weights the *informal* economics — most
    landlord-tenant relationships are resolved without invoking
    statute (landlord absorbs $200 of damage rather than fight,
    tenant breaks the lease and forfeits one month's rent). The
    statutory framing over-models the formal pathway.
  - Rent-stabilization regimes have *complex* exit conditions —
    vacancy decontrol (NYC pre-2019), preferential rent
    expirations, individual-apartment-improvement increases,
    luxury decontrol thresholds. The framing's "this unit is
    stabilized" is a snapshot that can erode through landlord-
    initiated actions the tenant rarely sees coming. Opposes F10.
  - For investor-landlords the framing names the eviction-cost
    line item but rarely the *time* line item — even a 30-day
    eviction is 30 days of zero rent plus prep cost; a 6-month
    California eviction with a holdover proceeding is 6 months
    of zero rent plus $10–20k in legal fees plus property damage
    during the contested period. The framing names eviction as
    risk; the IRR math rarely models the variance.
  - The framing's tenant-side and landlord-side perspectives are
    *opposing* — the same statute is protective to one and
    constraining to the other. The framing rarely flags that
    the asker's role (tenant / landlord / both via house-hacking)
    flips the polarity of every statutory provision. House-
    hackers in particular straddle both sides on the same
    property and need to read the statute from both perspectives.

## 13. Pro-buyer / consumer-advocate framing

- **Decisions it applies to**: D1 (Rent vs buy), D3 (Down-payment
  size), D5 (Property type), D6 (Location within metro), D7
  (Sell-and-buy sequencing), D11 (refi — D8).
- **Mental model summary**: Every other party in a real-estate
  transaction has a financial interest aligned *against* the buyer
  — the seller wants the highest price; the seller's agent earns
  commission on the price (typically 2.5–3% of sale); the buyer's
  agent earns commission on the *purchase* price (post-2024 NAR
  settlement, this is explicit, not bundled); the mortgage broker
  earns on loan size and rate (yield-spread premium incentive); the
  title / escrow company is selling lender-protective insurance the
  buyer pays for; the inspector may be agent-referred and reliant
  on agent referrals. The framing reasons in interest-alignment
  terms: who is on the buyer's side, who is on the other side, what
  do their compensation incentives reveal about the advice they
  give. The framing's reflex on every decision: independent-source
  every recommendation. Get independent inspector (not the agent's
  referral). Get independent attorney in states where attorneys
  close (NY, NJ, MA, GA). Shop the mortgage among 3+ lenders;
  request the LE (loan estimate) at the same time-of-day for
  apples-to-apples comparison. Characteristic move: act as if
  every counterparty is on the other side of the trade, because
  most are. Anchor: a $5–10k inspection + attorney spend at
  purchase typically pays for itself in negotiated repair credits
  or in surfaced defects the buyer would have eaten silently.
- **Characteristic vocabulary**: "fiduciary vs transactional",
  "agent's commission is real", "yield-spread premium", "title
  insurance vs owner's policy", "shop the mortgage", "loan
  estimate (LE) comparison", "independent inspection", "sewer
  scope", "pest letter (WDO)", "buyer's agency agreement (post-
  2024 NAR)", "dual agency conflict."
- **Excludes**:
  - Treats counterparty-adversarial as the dominant frame; misses
    that real-estate transactions are *repeat* games for the
    professionals — agents in a metro see the same buyers /
    sellers / agents over years, and reputational concerns
    discipline behavior beyond what the static-game framing
    predicts. The framing's "treat agent as adversary" routes
    the buyer into needless friction with counterparts who
    actually need referrals and reviews.
  - "Shop the mortgage" assumes the buyer has the bandwidth to
    submit 3+ applications, each generating a credit pull and a
    week of broker conversations. For the modal asker (working
    full-time, in a 30-day close window), 3-broker shopping is
    aspirational; 2-broker quote-shopping is realistic. The
    framing under-weights the operational cost of the consumer-
    advocate process.
  - The framing emphasizes adversarial-mode in a way that under-
    uses *cooperative* moves — the seller's agent often has
    information the buyer's agent doesn't (off-market comps,
    seller motivation, contingency-removal flexibility) and a
    cordial repeat-game relationship surfaces these. The buyer's
    "we're adversaries" reflex closes information channels.
  - Inspector selection is named but the framing rarely
    distinguishes inspection *tiers* — general inspector ($400–
    800), sewer scope ($150–300, often skipped, frequently the
    most important inspection), structural engineer ($500–1500
    when red flags appear), industrial-hygienist (mold, asbestos,
    lead — $300–800 each). The framing's "get an inspection" is
    correct in direction but under-specified.
  - Post-2024 NAR settlement changed buyer-side commission
    mechanics (now explicitly negotiable, written buyer-agency
    agreements required, listings can't publish buyer-side comp).
    The framing's "agent commissions are 5–6%" is calibrated to
    the prior regime; the new regime opens negotiating room the
    framing rarely names.

## 14. Macro-housing-cycle framing

- **Decisions it applies to**: D1 (Rent vs buy), D7 (Sell-and-buy
  sequencing), D8 (Refinance trigger), D9 (Investment property).
- **Mental model summary**: US housing moves in cycles driven by
  inventory (months-of-supply), affordability (price-to-income,
  price-to-rent, mortgage-payment-to-rent ratio), credit conditions
  (mortgage standards, MBS spreads), and rate cycle. The framing
  reasons in cycle-position terms: where are we — early expansion
  (rising prices, falling rates, expanding credit), late expansion
  (peak prices, tight inventory, FOMO buyers paying over ask), early
  contraction (price flat-to-declining, inventory rising, days-on-
  market expanding), late contraction (price decline, foreclosure
  uptick, distressed-seller market) — and what does the cycle
  position imply for the current decision. The framing's reflex
  on every decision: buy more aggressively in late contraction;
  rent and wait in late expansion; refinance in early expansion;
  liquidate investment-portfolio housing in late expansion.
  Characteristic move: track months-of-supply (4–6 months is
  balanced, < 3 is sellers' market, > 7 is buyers' market) and
  price-to-rent (national average ~16; > 20 is unfavorable for
  buyers; < 12 is favorable) for the specific metro, not the
  national series. Anchor: the 2006–2012 housing decline saw
  national price decline ~30% peak-to-trough but with metro
  variance from -10% (TX, much of the Midwest) to -50% (Las Vegas,
  Phoenix, parts of FL). National framing under-models metro-
  level variance.
- **Characteristic vocabulary**: "months of supply",
  "price-to-rent ratio", "price-to-income ratio", "Case-Shiller",
  "FHFA index", "mortgage-payment-to-rent",
  "Calculated Risk new home sales", "MBA mortgage application
  index", "MLS days on market", "buyers' market vs sellers'
  market", "the cycle is the macro", "above-trend vs trend".
- **Excludes**:
  - "Buy in a buyers' market" is structurally correct and
    operationally hard — buyers' markets coincide with credit
    tightening (lender standards rise, fewer loans approved) and
    distressed-seller markets are also distressed-buyer
    environments (job loss, recession). The framing's reflex
    routes the asker into a market they may not be able to
    transact in. Opposes F6 (cashflow) in those scenarios.
  - National-cycle framing under-models metro variance. In 2022,
    Austin and Phoenix saw 15–20% price declines while NYC and
    DC were flat-to-positive; the "we're in a downturn" framing
    obscures the metro-level reality. The framing's reflex
    "the cycle says wait" can be wrong by 18 months for the
    asker's specific metro.
  - Cycle timing is harder than the framing acknowledges. "Late
    expansion" is a label assigned in retrospect; in real-time
    the signal is noisy — Calculated Risk's housing-starts call
    in 2021 was directionally correct but 6+ months early, and
    the asker who acted on the call in mid-2021 was waiting
    through a peak that didn't break until late 2022. The
    framing presents cycle calls with more confidence than the
    underlying signal supports.
  - Under-weights the *secular* shifts the cycle framing
    treats as cyclical noise — work-from-home permanently lowered
    commute-density demand for some metros (SF urban core),
    permanently raised density demand for others (Boise,
    Asheville); the framing's "cycle reverts" misses durable
    relocation. Opposes F2.
  - The framing's "rent and wait" advice for late-expansion
    requires the asker to be a disciplined renter for 18–36
    months — most aren't. The behavioral cost (continued rent
    payments, capitulation-buy at the wrong time, frustration-
    purchase) often exceeds the cycle-arbitrage value. The
    framing under-weights the asker's emotional bandwidth for
    cycle-disciplined inaction.

---

## Coverage map

Per `_schema.md`, every decision needs ≥ 3 framings.

| Decision | Framings that cover it | Count |
|---|---|---|
| D1 Rent vs buy on 5–7yr horizon | F1, F2, F3, F4, F5, F7, F9, F11, F13, F14 | 10 |
| D2 Lease length and renewal | F2, F3, F6, F7, F12 | 5 |
| D3 Down-payment size | F1, F4, F6, F10, F13 | 5 |
| D4 Fixed-rate vs ARM vs IO | F5, F6, F7 | 3 |
| D5 Property type (SFR / condo / co-op) | F2, F4, F8, F13 | 4 |
| D6 Location within metro | F3, F4, F8, F9, F13 | 5 |
| D7 Sell-and-buy sequencing | F2, F6, F7, F11, F13, F14 | 6 |
| D8 Refinance trigger | F1, F5, F11, F14 | 4 |
| D9 Investment property vs index | F1, F8, F10, F12, F14 | 5 |
| D10 House-hacking / ADU | F3, F8, F10, F12 | 4 |

All 10 decisions satisfy the ≥ 3 framings minimum. D1 (rent vs buy)
is the densest coverage because nearly every framing lens has an
opinion on the foundational decision; D4 (fixed vs ARM) and D8
(refinance) sit closer to the floor because they are narrower
mortgage-mechanics decisions that fewer general frames argue about.

## Opposing-framing pairs

These are the direct axiom-level oppositions to surface in Layer 3
and for Triage / Risk Officer routing when the asker's prompt
vocabulary lands on one side:

- **F1 (financial-return) ↔ F2 (lifestyle-flexibility)** on D1.
  F1 says: at price-to-rent > 20, the rent-vs-buy math favors
  renting; the opportunity cost of the down payment compounded at
  market return beats the homeowner's leveraged appreciation +
  forced savings. F2 says: even if the IRR favors renting, the
  consumption value of being able to settle in / settle out
  matters; the asker's life-trajectory uncertainty is the
  binding variable, not the IRR. Same asker, same metro, same
  numbers gets opposite answers; Triage should surface F2 when
  the asker's prompt reads as F1-anchored ("the math says rent")
  and vice versa.

- **F1 (financial-return) ↔ F3 (household-stability)** on D1 / D2.
  F1's "buy when the IRR clears" misses that household-stability
  has dollar-equivalent value the IRR doesn't model; F3's "buy
  to put down roots" misses that a long-term lease purchases
  the same stability good more cheaply. The framings argue past
  each other unless both axes are priced.

- **F5 (rate-trajectory) ↔ F6 (household-cashflow)** on D4. F5
  says: at the top of a rate cycle, take the ARM and refi when
  rates fall; the locked-in 30-year fixed at 7%+ is overpaying
  for duration. F6 says: take the fixed regardless of rate cycle
  because payment-shock risk on ARM reset can exceed the
  household's shock-absorption capacity; the option value of
  refinance is a luxury, not a necessity. Same buyer, same
  numbers, opposite advice — F5 reasons from macro forecast, F6
  reasons from household budget; the right answer depends on the
  household's cashflow margin and the buyer's risk tolerance.

- **F5 (rate-trajectory) ↔ F7 (duration-of-stay)** on D4. F5's
  "ARMs are cheaper when rates will fall" presumes a refi window
  opens before reset; F7's "ARMs are cheaper if you sell before
  reset" presumes the buyer actually sells. The framings agree
  on ARM-preference under different mechanisms; they diverge
  when neither refi nor sale materializes — F5's path leaves the
  buyer holding a reset, F7's path leaves the buyer holding a
  reset, and both framings under-price the joint failure.

- **F6 (household-cashflow) ↔ F10 (investor-leverage)** on D3.
  F6 says: cap front-end DTI at 28%, keep a 3–6 month PITI
  reserve, don't deploy all liquid capital into the down payment.
  F10 says: maximize leverage to maximize ROE; minimize the down
  payment to preserve capital for the next acquisition. The
  framings carry opposite reflexes on the same numerical question
  (how much down) because they price different risks — F6 prices
  household-financial-fragility, F10 prices opportunity-cost-of-
  trapped-equity.

- **F8 (climate-and-insurance-risk) ↔ F9 (school-and-neighborhood
  premium)** on D6. F8 routes buyers *out* of climate-stressed
  zones; F9 routes buyers *into* school-zoned areas regardless
  of climate exposure (many top US school districts are in
  hurricane / wildfire / flood-exposed metros — Houston ISD,
  San Diego Unified, parts of FL). When the top school zone is
  in the climate-risk zone, the framings produce direct
  opposition; the asker needs both priced.

- **F11 (transaction-cost-amortization) ↔ F14 (macro-housing-
  cycle)** on D1 / D7. F11 says: buy when you can hold 5+ years
  regardless of macro; transaction cost dominates short-hold
  math. F14 says: don't buy in late-expansion regardless of
  intended hold; the cycle decline can erase 5 years of
  amortization gain. The framings can be reconciled (buy on
  5-year horizon AND in early-to-mid cycle) but in
  late-expansion-with-long-hold scenarios they conflict, and
  the right answer depends on whether macro signal is strong
  enough to override the holding-period heuristic.

- **F12 (tenant-rights) ↔ F10 (investor-leverage)** on D9 / D10.
  Same statute (rent-stabilization, just-cause eviction,
  warranty of habitability) is protective from F12's vantage
  and constraining from F10's. House-hackers (live in one unit,
  rent the other) straddle both framings on the same property
  and need to read every statutory provision twice. The
  opposing-framing surface is the literal same paragraph of
  statute argued from opposite sides.

- **F13 (consumer-advocate) ↔ F10 (investor-leverage)** on D9.
  F13's "every counterparty is adversarial" applies to owner-
  occupied transactions; for investor-acquisitions the same
  agent / broker / inspector relationships are *repeat* games
  with multi-transaction value, and F13's reflex toward
  adversarial-mode burns relationships F10 wants intact. The
  framings handle the *same* transaction-counterparty correctly
  in different roles (single-purchase buyer vs portfolio-
  builder).

## Voice anchors for Layer 3 (blindspots)

Layer 3 (`blindspots.md`) will draw from these conceptual
communities — each carries a recognizable voice, vocabulary, and
characteristic blind spots OF its own framing. These are voice-
anchors, not source URLs; `sources.yaml` (a later sub-item) will
attach concrete sources to each.

- **r/RealEstate / r/FirstTimeHomeBuyer** — transactional voice,
  agent-mediated, vocabulary of "comps," "appraisal gap,"
  "escalation clause." Blind spot of *this* community: under-
  weights opportunity cost (F1) and macro cycle (F14); over-
  weights the immediate transaction. Primary source for D1, D3,
  D5, D7 framings.
- **r/Bogleheads / Bogleheads forum housing threads** —
  opportunity-cost-pilled, rent-vs-buy as portfolio-allocation
  question, the NYT calculator as canonical artifact. Blind
  spot: under-weights consumption value (F2, F3) and
  household-stability premium. Primary source for F1.
- **BiggerPockets / r/realestateinvesting** — investor-pilled,
  cap-rate / cash-on-cash arithmetic, leverage as amplifier,
  "house-hacking" as wedge. Blind spot: under-weights tenant-
  rights (F12) and operational drag of self-management. Primary
  source for F10.
- **Mr. Money Mustache / r/financialindependence** — total-
  cost-of-ownership obsession, FIRE-driven, lifestyle-inflation
  resistance. Primary source for F4. Blind spot: routes
  everything into FI-arithmetic; under-prices household
  consumption value.
- **Ramit Sethi / I Will Teach You To Be Rich (housing
  chapter)** — "renting is not throwing money away," anti-
  conventional-wisdom, calculator-driven. Primary source for F1
  / F2. Blind spot: under-prices F3 stability for households
  with children.
- **Calculated Risk blog / Bill McBride** — macro housing
  cycle, months-of-supply, MBA mortgage application index,
  housing starts. Primary source for F14. Blind spot: macro
  forecast confidence is well-calibrated but the framing
  itself can route asker into market-timing failures on
  individual decisions.
- **NAR / NAHB / National Realtor data publications** —
  institutional optimism, "real estate always goes up," "marry
  the house, date the rate." Primary source for F11 commission
  baseline; primary anti-source for F13 (consumer-advocate
  reflex builds against this voice).
- **Marketplace housing / NPR Planet Money housing episodes** —
  generalist-economic voice, accessible-explainer. Useful for
  cross-validating F1 and F14 against single-issue communities;
  rarely the primary source.
- **r/Seattle / r/Austin / r/AskNYC / r/Boston / r/RealEstate
  TX / metro-specific subreddits** — neighborhood granularity,
  school-attendance-zone obsession, gentrification narrative.
  Primary source for F9 zone-premium signals and for F14 metro-
  variance calibration. Blind spot: under-weight national-cycle
  context; metro-internal framing can be 18 months out of phase
  with national.
- **Fee-only CFP / r/personalfinance (housing threads) / Bogleheads
  CPA-adjacent voices** — tax-cap and amortization math, SALT-cap,
  1031, §121 exclusion, depreciation recapture. Primary source
  for F1, F10, F11 tax mechanics. Blind spot: routes everything
  through tax-optimization at the cost of non-financial values.
- **First Street Foundation / IBHS / climate-risk research
  publications** — physical-risk-anchored, model-output framing.
  Primary source for F8. Blind spot: model-output uncertainty
  rarely surfaced; can be over-confident on perils that lack
  ground-truth calibration.
- **State insurance commissioner publications / r/Insurance /
  insurance-adjuster blogs** — peril-specific deductibles,
  master policy gaps, loss-assessment exposure, FL / CA non-
  renewal trauma. Primary source for F8 insurance-trajectory
  signals.
- **Tenant union publications / Bay Area / NYC tenant
  associations / Legal Aid landlord-tenant publications** —
  statute-and-enforcement voice, eviction-process timelines.
  Primary source for F12 tenant side.
- **r/Landlord / mom-and-pop landlord forums / BiggerPockets
  landlord threads** — operational-landlord voice, eviction-
  cost reality, tenant-selection heuristics. Primary source for
  F12 landlord side; complements (opposes) F12 tenant side.
- **Mortgage-broker blogs / r/Mortgages / loan-officer
  publications** — rate-sheet weekly, ARM margin / cap
  structure, conforming vs jumbo cliff, lender-credit
  arithmetic. Primary source for F5, F6 rate mechanics.
- **Buyer's-agent and real-estate-attorney publications / post-
  2024 NAR settlement coverage / state-bar real-estate
  sections** — fiduciary-vs-transactional, attorney-mandatory
  state mechanics. Primary source for F13.

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  every `Excludes` bullet above is a Layer 3 candidate. Highest-
  density candidates are F1 (financial-return — counterfactual-
  investment-assumption trap; maintenance-lumpiness trap; lender's-
  max-vs-buyer's-comfort delta), F5 (rate-trajectory — "marry the
  house date the rate" optimism on refi timing; ARM cap-structure
  reset math), F8 (climate-and-insurance — insurance-market lag
  vs underlying risk; FEMA-flood-map under-pricing of urban-
  stormwater; insurance-market is the canary but lags 5–15
  years), F9 (school-and-neighborhood — GreatSchools-rating-as-
  demographic-sorting; redistricting risk on boundary streets;
  K-12 mismatch converting school-thesis into double-pay), F10
  (investor-leverage — depreciation-recapture-deferred-vs-
  realized; real-estate-professional-status unavailability for
  most W-2 askers; concentration risk on single-property
  exposure), and F11 (transaction-cost — renovation cost-
  recoupment variance hidden under median numbers; post-2024
  NAR settlement changing commission mechanics; refinance
  amortization-clock-reset hidden in monthly-savings view).
  Sweep all 14 framings × ~4–5 bullets each = ~60+ blindspot
  candidates; promote ≥ 5 per framing into `blindspots.md` per
  the [`_schema.md`](../_schema.md) minimum.

- **High-stakes posture (Mechanism E partial)**: `housing` is
  `high_stakes: false` per `_meta_ontology.md` §3 (most outcomes
  reversible at modest cost), but selected decisions carry
  six-figure tail risks where professional referral is the
  correct framing exit: D7 (capital-gains-exclusion timing near
  caps; depreciation recapture from prior rental conversion —
  CPA), D8 (cash-out interest deductibility post-TCJA — CPA),
  D9 (real-estate-professional status and passive-loss
  limitations — CPA), and any transaction in
  attorney-mandatory states (NY, NJ, MA, GA, parts of the South —
  real-estate-attorney). Inspection-side: any decision where
  structural / sewer / pest finding would change the offer
  (independent inspector + buyer's agent; F13's reflex).
  domain_pack.md (later sub-item) should encode these as
  selective referrals, not blanket-defer language.

- **Triage routing notes**: framings 1 (financial-return), 6
  (household-cashflow), 8 (climate-and-insurance), 10
  (investor-leverage), and 11 (transaction-cost) carry the most
  distinctive vocabulary signatures and should be high-confidence
  routing matches (price-to-rent, DTI, FEMA flood zone, cap rate,
  closing costs). Framings 2 (lifestyle-flexibility) and 3
  (household-stability) share vocabulary that overlaps with
  general life-decisions outside housing — disambiguation against
  `family-planning` and `tech-career` adjacency is needed once
  V2 two-pass Triage is wired. Framing 13 (consumer-advocate)
  has vocabulary distinctive enough to route but applies broadly
  across nearly every housing decision — it's a posture-framing
  rather than a decision-framing.

- **Cross-domain edges from `decisions.md`**: F1 (financial-
  return) carries cross-domain edges into `personal-finance`
  (opportunity-cost-of-down-payment, mortgage-as-tax-leveraged-
  position, SALT-cap interactions); F10 (investor-leverage)
  cross-routes `personal-finance` (depreciation, 1031, passive-
  loss); F12 (tenant-rights / landlord-tenant) cross-routes
  `legal-disputes`; F2 (lifestyle-flexibility) cross-routes
  `tech-career` (relocation probability) and `immigration`
  (status-driven-exit horizon); F3 (household-stability) and F9
  (school-premium) cross-route `family-planning`; F8 (climate-
  and-insurance) is partially cross-domain into `personal-
  finance` via the insurance-premium-trajectory framing. Triage
  should surface these adjacencies when the user's situation
  spans both domains.

- **Voice-anchor → sources.yaml hand-off**: the voice anchors
  named above are the input list for the later `sources.yaml`
  sub-item. Each anchor should produce 1–3 source-views with
  distinct `community_tag` values, hitting the ≥ 8 source-views
  / ≥ 4 distinct community tags minimum from
  [`_schema.md`](../_schema.md) and the V2 §4 per-domain
  checklist. The current framings file flags voice anchors at
  the conceptual community level; concrete URLs and reliability
  ratings are sources.yaml's job.
