# housing — blindspots.md (Layer 3)

Blindspot catalogue for `housing`. Each entry names what a real
practitioner in the relevant framing would say is missed — anchored to
either an `Excludes` line in [`framings.md`](./framings.md) or to a
"Known blind spots OF this community" bullet in a V1 community profile
(`domain_knowledge/tech-career/communities/*.md`) where that profile
discusses housing-adjacent topics (geographic comp tiers, relocation,
HCOL-vs-LCOL trade-offs). Per [`_schema.md`](../_schema.md), every
entry is relative to a framing and ships with a trigger pattern and a
concrete recovery move.

The `housing` domain is **high_stakes: false** per
[`_meta_ontology.md` §3](../_meta_ontology.md) — most outcomes are
recoverable (sell, refinance, sublet, break the lease with a fee).
Unlike `immigration` (where every Recovery move ends in "consult a
licensed immigration attorney"), housing's Recovery moves are
**selectively** routed to professional counsel — buyer's agent,
mortgage broker, real-estate attorney, CPA, structural / pest / sewer
inspector, insurance broker, IBHS / climate-resilience inspector — only
where the decision carries six-figure tail risk that an informed
self-directed move cannot manage. Refinance trigger math and §121
exclusion / 1031 exchange / depreciation recapture sit on the CPA side;
title / easement / boundary-line / TOPA-right-of-first-refusal issues
sit on the real-estate-attorney side; flood / wind / wildfire / hail
exposure sit on the insurance-broker plus climate-resilience-inspector
side. Lower-stakes framings (lease renewal vs move, neighborhood
selection, basic refinance arithmetic at the high break-even-clearance
end) get self-directed Recovery moves. This per-framing inline routing
is the [V2 §4 Mechanism E partial-gating posture](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)
the housing `domain_pack.md` will encode (later sub-item).

Each blindspot lists:
- **Statement** — one sentence naming what is missed
- **Source evidence** — the framing-Excludes anchor or community-profile
  audit line this blindspot was extracted from (not invented)
- **Trigger** — the situation pattern the Triage / Risk Officer should
  match against
- **Failure mode** — the specific bad outcome if the blindspot stays
  unsurfaced
- **Recovery move** — the concrete action that resolves it, with
  professional-counsel referral named inline only where the decision's
  tail risk justifies it

The framing names below match [`framings.md`](./framings.md) exactly;
all 14 are covered with ≥ 5 entries each (≥ 70 total). Voice anchors
are conceptual — the source-views in
`domain_knowledge/housing/sources.yaml` are not yet authored, so
attribution is to the *class* of community (r/RealEstate, BiggerPockets,
Bogleheads-housing, Calculated Risk / housing-economist voice, NAR /
NAHB, local-market subreddits, fee-only CFP / CPA voice, climate-
resilience research, tenant-union / Legal Aid landlord-tenant
publications, mortgage-broker / loan-officer blogs, buyer's-agent and
real-estate-attorney publications). When `sources.yaml` lands,
source-evidence lines below should be tightened to specific
source-view ids.

---

## 1. Financial-return framing

### 1.1 IRR-superiority over rent ignores consumption value of tenure security

- **Statement**: The framing's "renting is mathematically superior at
  price-to-rent > 20" advice is structurally correct but routes the
  asker away from the consumption goods of housing that don't appear in
  the IRR — security of tenure, renovation freedom, freedom from
  landlord intrusion, the right to install a 240V outlet or paint a
  wall purple. An asker who treats housing purely as an asset class
  ends up renting through a decade where the consumption value of a
  stable wall set would have dominated the foregone equity-premium.
- **Source evidence**: `framings.md` §1 first Excludes bullet — "Frames
  housing purely as an asset; misses that *consumption* value... is real
  and not captured in IRR"; Bogleheads-housing voice's known blind spot
  ("under-weights consumption value F2/F3").
- **Trigger**: Asker presents the NYT rent-vs-buy calculator output as
  the dispositive answer, OR uses phrases like "the math says rent" /
  "renting is always cheaper at price-to-rent > 20" / "I shouldn't pay
  for an emotion."
- **Failure mode**: Asker stays renting through years of landlord turn-
  over, lease non-renewal, can't-paint-the-walls constraint, and
  mid-lease pet-policy reversals; the IRR was correct but the
  consumption foregone was the binding variable for this household.
- **Recovery move**: Before locking in the IRR conclusion, run a paired
  willingness-to-pay exercise — what would the asker pay annually for
  renovation freedom, for a 5-year guaranteed wall set, for the ability
  to install solar without landlord approval? If that number is large
  relative to the IRR delta, the consumption-value frame is binding and
  the math-only conclusion is wrong.

### 1.2 Maintenance averaging hides the lumpy-cash-shock distribution

- **Statement**: A 1.5%/yr maintenance reserve on a $700k house averages
  to $875/mo, which is honest in expectation and dishonest in cashflow.
  The real cost pattern is $0 in year 1, $2k in year 2, $30k in year 8
  (full roof + HVAC + sewer-line), $0 in year 9 — the 1.5%-amortized
  view obscures the liquidity reserve required to survive the lumpy
  reality and routes asker into a budget that breaks the first time the
  variance fires.
- **Source evidence**: `framings.md` §1 second Excludes bullet — "Treats
  the maintenance reserve as a deterministic line item; misses that
  maintenance is *lumpy* — the roof replacement, HVAC, sewer line,
  foundation work are 5-figure surprises every 7–15 years"; reinforced
  in §4 second Excludes bullet on monthly-amortization view obscuring
  the actual variance.
- **Trigger**: Asker computes a fully-loaded monthly cost using 1.5%/yr
  maintenance as the line item AND has < 6 months of PITI in liquid
  reserves post-close.
- **Failure mode**: Year 5 roof leak forces a $25k replacement; asker
  pulls from 401k (10% penalty + ordinary income) or runs a $25k credit-
  card balance at 24% APR; the maintenance-averaged budget was correct
  in expectation and disastrous in execution.
- **Recovery move**: Budget the average AND hold a separate $20–40k
  "lumpy reserve" untouched outside the operating budget — sized to the
  worst single 7-year-pattern repair (roof + HVAC simultaneous failure
  is the canonical worst case). Do NOT commingle with the emergency
  fund.

### 1.3 Opportunity-cost arithmetic assumes a counterfactual that doesn't exist

- **Statement**: "Buy with 5% down, invest the difference" arithmetic
  presumes the counterfactual asker actually invests the saved capital
  at the equity-risk-premium-bearing return. Empirical revealed-
  preference data (FRED household saving rate, housing-counsel papers)
  shows non-buyers who don't deploy the down-payment difference into
  equities — the cash sits at < 2% in checking. The "invest the
  difference" framing overstates the realistic counterfactual return by
  4–6 percentage points.
- **Source evidence**: `framings.md` §1 third Excludes bullet —
  "Opportunity-cost-of-down-payment-invested presumes the counterfactual
  user actually invests the difference."
- **Trigger**: Asker is reasoning from a calculator that compares
  buying-with-low-down vs renting-and-investing-the-saved-cash at 7–10%
  return AND does not have a 5-year track record of automated index-
  fund DCA contributions OR a written investment policy statement.
- **Failure mode**: Asker rents on the "invest the difference" thesis;
  spends the saved capital on lifestyle inflation; ends year 5 with
  neither the home equity nor the equity portfolio the framing
  predicted.
- **Recovery move**: Either commit in writing to an automatic monthly
  investment equal to the down-payment-difference / 60 BEFORE deciding
  on rent, OR adjust the comparison calculator to use a 2% checking-
  account return for the saved cash (which usually flips the conclusion
  back to "buying is closer than the framing claims").

### 1.4 Forced-savings function of amortization is dismissed too cleanly

- **Statement**: The framing's reflex that "amortization is just
  savings, you could save the same amount in a brokerage account" is
  technically correct but ignores the behavioral wedge: principal
  payment is forced and automated; brokerage contributions are
  discretionary and reversible. For the modal household without a
  hard-coded investment policy, the forced-savings function of the
  mortgage is real economic value the framing systematically writes
  off.
- **Source evidence**: `framings.md` §1 fourth Excludes bullet —
  "Ignores the forced-savings function of mortgage principal payment
  for households without disciplined investment habits."
- **Trigger**: Asker is being told by a Bogleheads-voice source that
  amortization is just savings AND the asker's reported brokerage
  contribution rate is < 10% of income with no automatic-deduction
  setup.
- **Failure mode**: Asker rents on the "I'll just invest more"
  argument; investment contributions never materialize at the level the
  calculator assumed; the household ends year 10 with neither
  amortization-built equity nor invested savings.
- **Recovery move**: If the household has no automated investment
  policy in place, model the rent-vs-buy decision with a realistic
  rather than aspirational savings rate; or set up the automated
  brokerage contribution FIRST (and run it for 6+ months), then
  reconsider rent-vs-buy with the demonstrated savings rate as input.

### 1.5 Leverage-amplifies-immobility is the shadow of leverage-amplifies-returns

- **Statement**: The framing celebrates leverage on the upside (5x on
  20% down) and prices the downside as "you can lose more than you put
  in" — but rarely names the *immobility* tail: an underwater mortgage
  (negative equity) prevents the asker from selling at market price to
  accept a 30% raise in another metro, or to follow a partner's job
  move, or to downsize after divorce. The leverage that amplifies
  returns also amplifies geographic and life lock-in.
- **Source evidence**: `framings.md` §1 fifth Excludes bullet — "Doesn't
  price *psychological* drag of being underwater (an upside-down
  mortgage creates immobility — can't relocate for a 30% raise, can't
  accept job in different metro)"; reinforced by `domain_knowledge/
  tech-career/communities/carta-and-platform-data.md` audit lines on
  geographic comp tiers and relocation-as-comp-arbitrage.
- **Trigger**: Asker is in a tech / consulting / academic career with
  recurring relocation pressure AND is buying at the top of a rate
  cycle with < 15% down in a metro showing flat-to-negative price
  momentum.
- **Failure mode**: Year 2 a 40% TC raise offer in another metro
  arrives; selling the house clears 3% net after commission against an
  8% LTV erosion; asker either declines the raise (long-term comp loss
  of $500k+ NPV) or takes a short-sale credit hit and writes a check
  to close.
- **Recovery move**: Stress-test the buy decision against a "must
  relocate at year 3" scenario at base-rate probability (NAR data:
  ~25% of first-time buyers sell within 5 years, tech-worker subset
  is higher). If the down-payment buffer can't absorb a 10% price
  decline plus 8% round-trip cost without writing a check at close,
  the buy is fragile to mobility shocks; either delay or buy at a
  cheaper price point.

---

## 2. Lifestyle-flexibility framing

### 2.1 Flexibility-is-monotonically-valuable misses commitment-effect goods

- **Statement**: The framing treats optionality as a one-way good — more
  is better. For households with children, aging parents, or rooted
  community ties, the *constraint* of a 30-year mortgage and a school-
  zone commitment produces social-capital, neighbor-network, and
  child-stability goods that the optionality framing systematically
  under-prices. Flexibility maximization can be its own trap when the
  asker's binding variable is "we keep moving and never put down roots."
- **Source evidence**: `framings.md` §2 first Excludes bullet — "Treats
  flexibility as monotonically valuable; misses that for some households
  the *constraint* of a 30-year mortgage produces long-horizon
  commitment effects."
- **Trigger**: Asker is 35+ with school-age children AND has moved
  3+ times in the last 7 years AND reports dissatisfaction with the
  "we never feel settled" pattern.
- **Failure mode**: Asker takes the 12-month lease again on
  optionality grounds; the kids' school continuity is broken for a
  fourth time; the household-stability good the asker actually wanted
  is sacrificed to an optionality reflex that the household has not
  exercised in 7 years.
- **Recovery move**: Look at the asker's revealed-preference data
  (number of moves in the last 7 years, reasons for each) vs stated
  intent. If the asker hasn't exercised the flexibility option in
  multiple years and reports stability-want, weight the F3 (household
  stability) framing against this F2 reflex.

### 2.2 The 5-year rule is a transaction-cost heuristic, not a flexibility heuristic

- **Statement**: "I should buy because I'm staying 5+ years" is a
  conflation. The 5-year rule is a *break-even-amortization* heuristic
  derived from the 6–10% round-trip cost; selling at year 4 costs
  the financial round-trip, not "you didn't get enough flexibility
  value." Treating it as a flexibility threshold leads askers to skip
  the price-to-rent and rate-environment checks the rule was never
  intended to absorb.
- **Source evidence**: `framings.md` §2 second Excludes bullet — "5-year
  rule is a transaction-cost heuristic, not a flexibility heuristic.
  Selling at year 4 costs 6–10% of value in round-trip friction — the
  financial cost is the binding constraint, not 'you didn't get enough
  flexibility value.'"
- **Trigger**: Asker uses "I'll be there 5+ years so buying makes
  sense" as the dispositive argument AND has not computed price-to-rent
  or rate-cycle position.
- **Failure mode**: Asker buys on the 5-year-horizon argument at a
  20+ price-to-rent ratio at top of rate cycle; appreciation over
  the 5-year hold is 0–3%/yr nominal; round-trip cost consumes the
  appreciation; asker exits with break-even-or-slightly-negative net.
- **Recovery move**: Treat the 5-year horizon as necessary, not
  sufficient. Pair it with the price-to-rent check (< 18 favorable;
  18–22 borderline; > 22 hostile) and the rate-cycle check (early-
  expansion / late-expansion / contraction). Buy only when all three
  align, not when one alone is satisfied.

### 2.3 Renting itself has lock-in events the framing under-states

- **Statement**: The framing's "I'm free as a renter" narrative is
  structurally true on the 30-year mortgage axis but operationally
  over-stated. The renter is locked into the lease term, the security-
  deposit pull-forward (often 1.5–2 months of rent), the 14-day or
  30-day notice clock at vacate, the rent-hike timing the landlord
  chooses, the annual lease-renewal window. "Renting is freedom" is a
  yearly choice, not a daily choice.
- **Source evidence**: `framings.md` §2 third Excludes bullet — "Under-
  weights that *renting itself has lock-in events* — the annual lease
  renewal, the security-deposit pull-forward, the 14-day notice clock
  to vacate, the rent-hike timing the landlord chooses. Opposes F12."
- **Trigger**: Asker reports the lease-renewal window or a mid-lease
  rent increase as feeling like a constraint, while still framing the
  rent-vs-buy choice as "I want to stay flexible."
- **Failure mode**: Asker signs a 12-month lease believing it preserves
  optionality; 7 months in, life-event triggers a desired move; asker
  faces 5 months of double-rent or lease-buyout fees (typically 2
  months) — the optionality cost is real and unpriced.
- **Recovery move**: Quantify the renter-side lock-in: lease-buyout
  fee, advance-notice requirement, sublease rights, mid-lease rent-
  increase protections. Compare against the homeowner-side lock-in
  (commission cost, days-on-market). The choice is between two
  asymmetric lock-in profiles, not between lock-in and freedom.

### 2.4 Externally-imposed moves are the base-rate trigger, not asker-initiated ones

- **Statement**: The framing's "I might move for a job" implicitly
  assumes the move is the asker's initiative. Empirically, the modal
  unplanned move comes from layoff, partner career event, family
  illness, or eldercare crisis — externally-imposed triggers the
  asker doesn't model when computing a stated holding horizon. The
  flexibility framing handles these correctly *if priced*; askers
  routinely fail to price them and predict their own horizon too
  confidently.
- **Source evidence**: `framings.md` §2 fourth Excludes bullet — "'I
  might move for a job' assumes the move is the asker's initiative.
  Layoffs, family illness, and partner career events are externally-
  imposed move triggers the flexibility-framing handles correctly but
  the asker's stated horizon under-weights relative to base rates.
  Cross-routes `tech-career`."
- **Trigger**: Asker states a confident 10+ year holding horizon AND
  works in an industry with > 10% annual layoff rate (tech, finance,
  media, biotech post-2022) OR has a partner with a mobile career
  trajectory (consulting, academic-track, federal-rotation).
- **Failure mode**: Asker buys on stated 10-year horizon; year 3
  layoff or partner-relocation forces the sale; the round-trip cost
  and timing-of-market both go against the asker.
- **Recovery move**: Compute the move at base-rate probability rather
  than stated intent — for tech workers, assume 30–40% probability of
  involuntary move within 5 years; for dual-career households with one
  mobile partner, assume 25%+. Stress-test the buy decision against the
  base rate, not the stated intent.

### 2.5 Optionality on the way *out* of homeownership is asymmetric

- **Statement**: The framing treats buy-vs-rent as bidirectional
  optionality. In practice, transitioning from owning to renting
  requires selling first — a 60–120 day operation in normal markets
  and 6–12 months in slow ones. The "I'll just sell if I need to"
  reflex is calibrated to a fast-market assumption that doesn't hold
  in contraction. Optionality is real on the way *in* (buy or rent on
  any month); it is *time-asymmetric* on the way out.
- **Source evidence**: `framings.md` §2 fifth Excludes bullet — "The
  framing treats the buy-vs-rent decision as bidirectional optionality;
  in practice transitioning from owning to renting requires selling
  first, which is itself a 60–120 day operation in a normal market and
  6–12 months in a slow one. Optionality on the way *out* of
  homeownership is asymmetric."
- **Trigger**: Asker frames the buy decision as "I can always sell
  later if I need to" AND has not assessed the local market's
  days-on-market trend OR the macro cycle position.
- **Failure mode**: Asker buys; mid-year-3 needs to exit; local market
  is in early contraction with 90+ days-on-market; the "sell later"
  optionality requires either a 12% price concession or 6+ months of
  carrying cost while the listing sits.
- **Recovery move**: Before buying, look up the local market's current
  days-on-market and 12-month trend (Redfin / Zillow market reports,
  local MLS). Add 50% to the worst recent reading as the planning
  horizon for an exit. If that exit window is incompatible with the
  asker's possible relocation timeline, the optionality on exit isn't
  what the framing implies.

---

## 3. Household-stability framing

### 3.1 Stability can be purchased with a long lease, not only with ownership

- **Statement**: The framing's reflex jumps from "we want stability"
  to "buy" without engaging the long-lease alternative. In many markets
  (non-rent-controlled but landlord-stable), a 24–36 month lease
  delivers the same school-continuity, neighbor-network, and
  "we-live-here" stability good as ownership, without the leverage
  exposure or transaction friction. The framing rarely names this as
  a substitute.
- **Source evidence**: `framings.md` §3 first Excludes bullet —
  "Conflates the *consumption* value of stability with the *investment*
  commitment of ownership. Stability can be purchased with a long lease
  (24–36 months) in many markets without the leverage exposure of a
  mortgage; the framing's reflex jumps to 'buy to stop renting' when a
  long-term lease in a non-rent-controlled market is often the cheaper
  purchase of the same stability good. Opposes F1."
- **Trigger**: Asker reports wanting stability ("the kids need
  continuity," "we want to stop counting the months") and immediately
  jumps to buy-vs-rent calculator math, skipping the explicit long-
  lease negotiation as an option.
- **Failure mode**: Asker buys at the top of a rate cycle for stability
  reasons; carries 30 years of leverage and maintenance risk to
  purchase a consumption good that a 36-month negotiated lease (often
  at a 10–15% discount in soft markets) would have delivered with
  10× less capital deployed.
- **Recovery move**: Before triggering the buy process, write a 24–36
  month lease offer to the current landlord (or to comparable units)
  with rent locked at current market. Many landlords accept long
  leases at slight discounts; if the asker's stability-want is
  satisfied by the lease offer, the buy decision was over-routed.

### 3.2 Environmental change can erode stability the framing locks in physically

- **Statement**: Stability is durable only if the underlying environment
  doesn't change. Buying into a fast-gentrifying neighborhood locks in
  the *house* but the schools, commute, neighbor-set, and street
  character change anyway; buying into a declining neighborhood locks
  in both the house and a slow erosion of the household-stability
  good the framing was buying. The asker's stability purchase is
  partly an environmental, not a legal-contractual, good.
- **Source evidence**: `framings.md` §3 second Excludes bullet —
  "Stability is *durable only if the underlying environment doesn't
  change*. Buying into a fast-gentrifying neighborhood locks in the
  *house* but the schools, commute, and neighbor set change anyway."
- **Trigger**: Asker is buying in a neighborhood currently undergoing
  visible transition (new construction starts visible on the block,
  new restaurants on the commercial strip, school-zone-boundary
  redistricting in active discussion, multiple "for-sale" signs going
  up within a 3-block radius).
- **Failure mode**: Year 5 the neighborhood the asker bought for is
  gone — gentrified, schools redrawn, commercial-strip displaced;
  the house remains, the stability good doesn't; the asker is
  geographically rooted in an environment they would not have chosen
  freshly.
- **Recovery move**: Walk the neighborhood at three different times
  (weekday morning, weekend evening, school-pickup hour); talk to 5+
  current residents about how the neighborhood has changed over the
  prior 5 years; look at the school-board meeting minutes for
  zone-boundary discussions; price stability as a *current* good with
  decay risk rather than a permanent good.

### 3.3 Divorce / separation / partner death is unmodeled legal-partition friction

- **Statement**: Joint ownership creates legal partition-of-asset
  friction (forced sale, partition action, refinance-to-sole-owner
  math) that joint tenancy on a lease does not. The framing's "we're
  building a life together" presumes the life-together continues; the
  legal exit costs at separation or partner-death are 2–5× higher than
  the framing names.
- **Source evidence**: `framings.md` §3 third Excludes bullet — "Under-
  weights divorce / separation / partner-death scenarios in the
  household-stability arithmetic. Joint ownership creates legal
  partition-of-asset friction that joint tenancy on a lease does not."
- **Trigger**: Asker is buying jointly with an unmarried partner OR
  with a partner without a prenup OR within the first 24 months of
  cohabitation AND the household stability assumption is "we're going
  to be together long-term."
- **Failure mode**: Year 3 separation; one partner wants to keep the
  house; the refinance-to-sole-owner requires a new full income-
  qualification at current rates (often 200+ bps higher than the
  original lock); the partner can't qualify alone; forced sale at a
  bad time; both partners take a $30–60k hit relative to a planned
  exit.
- **Recovery move**: For unmarried co-buyers, paper the partnership
  with a co-ownership agreement before close — including buy-out
  formula, dispute-resolution mechanism, and refinance-trigger
  provisions; consult a real-estate attorney in the jurisdiction
  (this is the kind of decision where the attorney spend is the
  cheapest part of the deal). For married co-buyers in a community-
  property state, model the partition mechanics at separation as part
  of the buy decision.

### 3.4 "Aging in place" presumes physical compatibility most US stock lacks

- **Statement**: The framing's stability-arc presumes the house remains
  physically suited to aging — single-floor or elevator, ADA-compatible
  bathrooms, walkable to medical / grocery / pharmacy. Most US single-
  family stock fails these criteria; the framing routes asker into a
  stability-good that becomes a *mobility-trap* at age 75 when stairs
  become impossible and the house can't be retrofitted economically.
- **Source evidence**: `framings.md` §3 fourth Excludes bullet —
  "'Aging in place' presumes the house remains physically suited to
  aging (single-floor or elevator, ADA-friendly bathrooms, walkable to
  medical). Most US single-family stock fails these criteria; the
  framing routes asker into a stability-good that becomes a mobility-
  trap at 75. Cross-routes `family-planning`."
- **Trigger**: Asker is 45+ buying a multi-story house with
  bedrooms/laundry/main bath on upper floor AND is framing the
  decision in "forever home" terms.
- **Failure mode**: Age 70–75 the stairs become an obstacle; ADA
  retrofit cost is $40–150k (chair lift, first-floor full-bath
  conversion, exterior ramp); house is in a car-dependent
  neighborhood the asker can no longer drive in; forced move into
  assisted living at 78 at the absolute worst time emotionally and
  market-timing-wise.
- **Recovery move**: For "forever home" buyers over 45, run an
  aging-compatibility audit: count steps from car to bedroom, identify
  first-floor full-bath options (or absence), walk distance to nearest
  pharmacy / grocery / urgent-care, neighborhood drive-or-die
  classification. If the house fails 2+ of these, the "forever" frame
  is wrong and either select an aging-compatible house now or treat
  this house as a 15-year not 30-year horizon.

### 3.5 The household is a moving target the 30-year frame doesn't model

- **Statement**: The framing's "stable forever home" presumes a static
  household composition over a 30-year mortgage. The actual household
  changes — children launch and stop using bedrooms (and start using
  visits-only-mode bedrooms); partners' careers diverge; aging parents
  move in (cross-routing F10 on ADU); some members exit via death or
  separation. The 30-year frame absorbs a 15-year household snapshot
  and projects it forward.
- **Source evidence**: `framings.md` §3 fifth Excludes bullet —
  "Doesn't engage with that the *household* is a moving target —
  children leave home, partners' careers diverge, aging parents join.
  The 'stable forever home' the framing builds toward is a snapshot
  of a 15-year window, not a 30-year mortgage horizon."
- **Trigger**: Asker (typically 35–45 with young children) is buying
  a 4BR+ family house framed as the forever home AND has not modeled
  the empty-nest phase OR the elderly-parent-moves-in phase.
- **Failure mode**: Year 18 kids have launched; couple is rattling
  around in 4 unused bedrooms, paying property tax and maintenance on
  underused space; downsizing requires another round-trip transaction
  the original "forever" frame ruled out.
- **Recovery move**: Buy for the next 10–15 years, not the next 30.
  Plan the second-half-of-life downsize as part of the original buy
  thesis (which type of property, which neighborhood, expected price
  point), not as a surprise life event two decades later. If the
  current house lets you anticipate that next move comfortably, the
  decision is robust; if not, smaller-now-with-room-to-grow may be
  the better frame.

---

## 4. Total-cost-of-ownership framing

### 4.1 TCO honesty without consumption-side scoring routes asker out of valid buys

- **Statement**: The framing computes the cost side honestly (PITI +
  HOA + maintenance + CapEx + opportunity cost) and compares against
  market rent without engaging the *benefit* side beyond rent —
  renovation freedom, garden, no-landlord pets, ADU optionality.
  Asker sees "fully-loaded $5,500 vs $3,500 rent" and routes to rent;
  the consumption goods of ownership are worth real money that the
  rent-only comp doesn't capture.
- **Source evidence**: `framings.md` §4 first Excludes bullet —
  "Computes the cost honestly but doesn't engage with the *benefit*
  side beyond market rent — for owner-occupiers the consumption value
  (renovation freedom, no landlord, garden, pet rules) is real and
  not captured in rent-comp. The framing's '$5,500 fully-loaded vs
  $3,500 rent → don't buy' routes asker out of valid decisions.
  Opposes F3."
- **Trigger**: Asker has run the fully-loaded monthly TCO table and is
  routing to rent because the gap is > 30% AND the asker has named
  specific consumption goods (garden, multi-pet, home-office build-out,
  ADA modifications, renovation projects) that are constrained in the
  rental alternative.
- **Failure mode**: Asker rents on the TCO math; spends 5 years
  unable to install the dedicated home office, the dog run, the
  garage workshop the asker would have built; the $24k/yr "TCO
  delta" was the price of consumption goods the asker would have
  paid for and the math under-priced.
- **Recovery move**: Estimate the consumption-side dollar value
  explicitly — what would the asker pay annually to install solar,
  to renovate the kitchen, to have a garden, to install a 240V outlet
  for an EV charger? If that aggregate exceeds 50%+ of the monthly
  TCO delta, the buy is closer than the cost-only view shows.

### 4.2 Monthly-amortized maintenance hides the cashflow-pattern reality

- **Statement**: $875/mo amortized maintenance is honest in expectation
  and wrong in cashflow. Year 1: $0–1500. Year 8: $25k. Year 15:
  $40k. The monthly view obscures the liquidity-reserve requirement
  and routes the buyer into a budget that can't survive the variance.
- **Source evidence**: `framings.md` §4 second Excludes bullet —
  "Maintenance averaging hides the variance. A buyer who computes
  1.5%/yr × $700k = $10,500/yr ÷ 12 = $875/mo is correct in
  expectation and wrong in cashflow planning — the actual pattern is
  $1,500 in year 1, $0 in year 2, $25,000 in year 8, etc."; reinforced
  by §1.2 above on lumpy-cash-shock distribution.
- **Trigger**: Asker presents a fully-loaded TCO table with
  maintenance as a flat monthly line item AND post-close liquid
  reserves below 12 months PITI + 1 worst-case-repair.
- **Failure mode**: Year 7 a $25k roof bill arrives; asker carries it
  on a HELOC at 9% APR for 18 months; the monthly TCO blueprint never
  modeled this and the real cost is 20%+ higher than the table showed.
- **Recovery move**: Pair the monthly amortization (for income-vs-
  payment qualification) with a separate "lumpy reserve" line that
  holds 1× worst-case-7-year-repair in liquid savings, untouched and
  separate from emergency fund.

### 4.3 Property-tax projection on listing data is the seller's basis, not yours

- **Statement**: The MLS / Zillow listing's "property tax: $X/yr"
  reflects the *current owner's* assessment. In CA (Prop 13) the
  basis resets on transfer and the new owner's tax is often 2–4×
  higher than the listing shows. In FL / TX / GA (post-purchase
  reassessment regimes) the basis resets to market value and the
  listing-time tax under-states the buyer's actual obligation by 30–70%.
- **Source evidence**: `framings.md` §4 third Excludes bullet —
  "Property-tax projection assumes current-millage; misses that in
  CA (Prop 13) the basis resets on transfer and your tax bill is
  dramatically higher than the seller's — the listing's 'property
  tax: $4,000/yr' is the seller's basis, not yours; in TX / FL post-
  purchase reassessment can be 50%+ higher than the listing shows."
- **Trigger**: Asker is in CA / FL / TX / GA / NV / SC and is using
  the MLS listing's property-tax line as the budget input for TCO.
- **Failure mode**: Closing year property-tax bill arrives at 2.5× the
  listing number; asker is $400+/mo over budget on a recurring basis;
  household savings rate drops by half to absorb the gap.
- **Recovery move**: For any purchase in a re-assessment-on-transfer
  state, compute property tax as the *market* assessed value × the
  current millage rate, NOT as the seller's prior bill. For CA
  specifically: use the contract price as the new basis × the
  property's prior millage. If the math is large enough to matter,
  validate with the local county assessor (most have a buyer-side
  estimator on the county website).

### 4.4 HOA "$X/mo" is a snapshot that hides special-assessment trajectory

- **Statement**: The framing prices HOA as a static monthly line —
  $400/mo, $800/mo, $1200/mo. Post-Surfside (FL condo collapse 2021)
  and post-CO HB 23-1233 reform, condo and HOA reserve requirements
  are tightening; under-reserved buildings are issuing $10–50k+
  special assessments to fund overdue structural work. "$400/mo HOA"
  can be "$400/mo + $15k special assessment in year 3" — the static
  view doesn't carry this signal.
- **Source evidence**: `framings.md` §4 fourth Excludes bullet —
  "HOA cost is a *current* number; doesn't engage with special-
  assessment trajectory (post-Surfside FL condo reserves, CO HB
  23-1233 reform). The framing's '$400/mo HOA' can be '$400/mo +
  $15k special assessment in year 3' and the static cost view doesn't
  catch this. Cross-routes F8."
- **Trigger**: Asker is buying a condo / townhome with HOA in a
  building > 30 years old OR in a coastal / hurricane / wildfire
  zone OR in a state with recent reserve-study legislation (FL post-
  Surfside, CO post-HB 23-1233, CA pending).
- **Failure mode**: Year 2 the HOA board issues a $35k special
  assessment for a roof + façade + balcony retrofit the reserve
  study identified; asker either pays cash, takes on personal debt,
  or sells at a discount (the special-assessment overhang spooks
  buyers and lowers the next sale price).
- **Recovery move**: Demand the HOA reserve study (often 3–10
  years old; should be ≤ 5 years for buildings > 30 years old) and
  the financial-statement audits for the last 3 years BEFORE
  removing inspection contingency. For older buildings or coastal
  exposure, this is the decision where the buyer's-agent referral
  to a condo-specialized real-estate attorney pays for itself —
  this is the highest tail-risk inspection a condo buyer can buy.

### 4.5 Rent-comp at the same square footage often doesn't exist

- **Statement**: The framing's "compare against rent at same sqft"
  presumes an apples-to-apples rental comparable exists. In SFR-
  dominated markets (Austin, Phoenix, suburban Atlanta, much of TX
  and FL), there is no equivalent 3BR/2BA SFR rental within 30% of
  the buy's square footage; the analyst either inflates the rent
  comp (making buying look better) or accepts an apartment as comp
  (making renting look better). The TCO math breaks down without an
  honest comparable.
- **Source evidence**: `framings.md` §4 fifth Excludes bullet —
  "'Compare against rent at same sqft' presumes a 1-to-1 rental
  comparable exists. In SFR-dominated markets (Austin, Phoenix, much
  of suburban Atlanta), there's no equivalent 3BR/2BA SFR rental
  within 30% of the buy's square footage; the framing's apples-to-
  apples comparison breaks down."
- **Trigger**: Asker is computing a TCO comparison in an SFR-
  dominated suburban market AND is using an apartment rent or a
  cross-metro rent as the comp.
- **Failure mode**: Asker buys on the inflated-rent-comp version of
  the math; the actual rent comparable in the same market is 30%
  lower (because the SFR-rental market is thin); the buy decision
  was made against a comparable that doesn't exist.
- **Recovery move**: When the rental market is thin, do NOT force a
  same-sqft comp — instead, run two scenarios: (a) buy this house vs
  rent the realistically-available apartment at smaller-sqft (engages
  the consumption-value question of "do we need this much space"),
  and (b) buy this house vs rent a similar-sqft house in an adjacent
  metro (engages the metro-choice question). Pick whichever framing
  matches the actual decision being made.

---

## 5. Rate-trajectory framing

### 5.1 "Marry the house, date the rate" assumes a refi window that may not open

- **Statement**: The famous "marry the house, date the rate" reflex
  is structurally optimistic. In 1980, the 30-year fixed hit ~18%;
  rates fell below 10% only in 1986 — six years of "dating" with no
  exit. The framing presumes a refi opens within the holding period;
  in long-duration high-rate regimes, that's wrong and the buyer is
  married to both the house and the rate.
- **Source evidence**: `framings.md` §5 first Excludes bullet — "'Marry
  the house, date the rate' is structurally optimistic about refi
  availability. In 1980, the 30-year fixed hit ~18%; rates fell back
  below 10% only in 1986 — six years of 'dating the rate' with no
  exit."
- **Trigger**: Asker is being told (by NAR / mortgage-broker / agent)
  to buy at top-of-cycle rates with refinance-within-2-years as the
  thesis AND the rent-vs-buy math doesn't clear at the current rate.
- **Failure mode**: Rates do not fall fast enough; asker carries
  the higher PITI for 4+ years; the refi-thesis was the load-bearing
  assumption of the buy decision and it didn't deliver.
- **Recovery move**: Refuse to buy at top-of-cycle on a refi thesis.
  Buy only when the math works at *today's* rate; treat refi as
  upside, not as the load-bearing assumption. If the math doesn't
  clear at today's rate, the decision is wrong regardless of the
  rate-trajectory thesis.

### 5.2 Rate forecasts are weakly accurate beyond 6 months

- **Statement**: Professional rate strategists routinely produce 12-
  month forecasts that miss by 100–200bps; the asker's "rates will
  fall next year" is borrowed confidence the underlying analysts
  explicitly disclaim. Acting on a confident rate forecast at the 12-
  month horizon is acting on noise.
- **Source evidence**: `framings.md` §5 second Excludes bullet — "Rate
  forecasts are weakly accurate beyond 6 months. The framing's 'we
  expect rates to fall' depends on forecasts that professional rate
  strategists explicitly disclaim."
- **Trigger**: Asker uses "we expect rates to fall" as a load-bearing
  input to the buy decision OR to the ARM-vs-fixed choice, citing a
  popular-press forecast or a single research-note headline.
- **Failure mode**: Decision was made on a forecast that didn't
  materialize; the asker has 30 years to absorb the consequence of a
  12-month-horizon noise bet.
- **Recovery move**: Treat any rate-trajectory assumption beyond
  6 months as noise. Make the decision robust to "rates stay flat or
  rise" as the modal scenario; refi-when-rates-fall is the upside
  case, not the planning case.

### 5.3 ARM cap structure is the load-bearing variable, not the headline rate

- **Statement**: A 5/1 ARM at 5.875% with a 2/2/5 cap can reset to
  7.875% / 9.875% / 10.875% over years 6–8 — a 5-percentage-point
  swing. The framing's "ARM is X% lower than fixed" is honest only
  if the buyer can afford the cap. Most ARM disclosures bury the cap
  structure; the headline-rate-only comparison misses the binding
  variable.
- **Source evidence**: `framings.md` §5 third Excludes bullet — "ARM-
  vs-fixed decision depends on *index-and-margin-and-cap-structure*
  (most have 2/2/5 caps), which is not the same as 'ARM is X% lower.'
  A 5/1 ARM at 5.875% with a 2/2/5 cap can reset to 7.875% / 9.875%
  / 10.875%."
- **Trigger**: Asker is choosing between 30-year fixed and 5/1 or 7/1
  ARM AND is reasoning from the headline rate delta alone, without
  having extracted the index / margin / cap structure from the
  closing disclosure.
- **Failure mode**: Asker takes the ARM; life-event prevents refi or
  sale before reset; year-6 payment jumps by 35% of current PITI;
  household budget is broken by a number the headline-rate comparison
  did not surface.
- **Recovery move**: Before any ARM decision, ask the loan officer to
  show the *maximum* monthly payment at the lifetime cap, the
  reset-year payment at the first cap, and the index-and-margin
  formula explicitly. If the buyer can't afford the lifetime-cap
  payment at current income, the ARM is a bet on refi or sale; price
  it that way. Mortgage-broker referral is the right move here — a
  fee-only mortgage broker (paid by the buyer, not the lender) is the
  fastest way to see the cap structure across multiple ARM products.

### 5.4 Discount-point arithmetic contradicts the refi-soon thesis

- **Statement**: Paying 1 point to buy down 25 bps breaks even in
  4–6 years at typical rates. The framing's reflex toward buying
  points presumes hold-to-break-even, which directly contradicts the
  framing's other reflex toward refi-when-rates-fall. A buyer who
  pays points and refis in 18 months has paid for a rate they didn't
  use.
- **Source evidence**: `framings.md` §5 fourth Excludes bullet —
  "Discount-point arithmetic ('pay 1 point to buy down 25bps') breaks
  even in 4–6 years at typical rates; the framing's 'buy points to
  lower the rate' presumes hold-to-break-even, which contradicts the
  framing's other reflex (refi when rates fall). Opposes F8 (refinance)."
- **Trigger**: Asker is being offered discount points at close AND is
  simultaneously planning to refi within 2 years if rates fall.
- **Failure mode**: Asker pays $8k in discount points; refis 14
  months later at a lower rate; never recoups the point cost; the
  $8k was a transfer to the lender at close on the basis of a hold
  thesis the buyer contradicted within 14 months.
- **Recovery move**: Only buy points if the hold-to-refi-OR-sale
  horizon is robustly > 5 years AND the rate-fall thesis is
  explicitly NOT load-bearing in the buy decision. Otherwise take
  the par rate (no points, no credit) and preserve the refi
  optionality unburdened by a sunk point-cost.

### 5.5 Lender-credit and relationship-pricing are unnamed levers

- **Statement**: The framing treats rate as the only mortgage variable
  and the headline rate as the buyer's only output. In practice,
  lender credit (the inverse of discount points — lender pays buyer
  closing costs in exchange for slightly higher rate), relationship-
  pricing (banks shaving 12.5–25bp for high-AUM-tied customers), and
  builder-finance buy-downs (2-1 temporary rate reductions, builder-
  funded) are real levers the framing rarely names. The buyer who
  shops on rate alone leaves money on the table.
- **Source evidence**: `framings.md` §5 fifth Excludes bullet —
  "Treats rate as the only mortgage variable; doesn't engage with
  lender credit (the inverse of discount points), pricing exception
  on relationship (some banks shave 12.5–25bp for AUM-tied customers),
  or builder-finance buy-downs (2-1 buy-downs are builder-funded
  rate-temporaries that the framing rarely names)."
- **Trigger**: Asker is shopping rate alone (calling 3 lenders for
  "best 30-year fixed rate") AND has > $250k of brokerage / banking
  assets at any single institution OR is buying new construction
  with a builder-affiliated lender.
- **Failure mode**: Asker takes a 7.0% rate from a discount lender
  with $9k closing; could have taken 7.125% from primary banking
  relationship with $0 closing and a 12.5bp relationship discount
  bringing the rate to 7.0% on lender-credit terms — same net rate,
  $9k more in pocket.
- **Recovery move**: Ask each lender explicitly: (a) what's the par
  rate at 0 points, 0 credit; (b) what's the lender-credit table at
  +12.5, +25, +37.5 bps; (c) is there a relationship-pricing
  exception for high-AUM-tied customers; (d) for new construction,
  what's the builder's rate-buy-down offer separately from the
  lender's. A fee-only mortgage broker can shop across 3+ lenders
  and surface levers a single-lender call would not.

---

## 6. Household-cashflow framing

### 6.1 28/36 rule was calibrated to a different income structure than the modal HCOL tech worker

- **Statement**: The 28/36 rule was calibrated to 1970s-era housing-
  to-income ratios. In HCOL metros (SF, NYC, Seattle, Boston) modal
  tech-worker buyers carry 35–45% front-end DTI without obvious
  distress because compensation is heavily skewed toward equity and
  bonus the rule doesn't model. The framing's "house poor at > 28%"
  is calibrated to a different income structure than the modal asker
  faces.
- **Source evidence**: `framings.md` §6 first Excludes bullet — "28/36
  rule was calibrated for 1970s-era housing-to-income ratios; in HCOL
  metros (SF, NYC, Seattle, Boston) modal tech-worker buyers carry
  35–45% front-end DTI without obvious distress because compensation
  is heavily skewed toward equity / bonus the rule doesn't model.
  Opposes F1 in HCOL contexts."
- **Trigger**: Asker is a tech worker in a top-tier HCOL metro AND
  is being routed out of a buy decision purely on the 28% front-end
  rule AND the asker's base salary is < 50% of their total comp.
- **Failure mode**: Asker stays renting on the 28% rule; over 5
  years foregoes 200k+ of equity-build in a market where base salary
  alone would have flagged unaffordability but total comp clears
  comfortably; the rule's calibration was wrong for this household.
- **Recovery move**: Compute DTI three ways — on base only
  (conservative), on base + reliable cash bonus (mid), on base +
  bonus + 25% of RSU at current valuation (aggressive, models
  expected vest under current employer). The right cap is somewhere
  between mid and aggressive, not at the conservative single-income
  baseline.

### 6.2 RSU comp is volatile and the framing under-weights the downside path

- **Statement**: For tech-worker askers a meaningful chunk of comp is
  RSU / bonus that may or may not vest. The framing's two reflexes
  ("compute DTI on base only" = over-conservative; "compute DTI on
  total comp" = over-aggressive) both miss the volatility. RSUs are
  price-sensitive (down 60% from 2021 peaks across many public-tech),
  and variable comp can be cut at layoff or perf-cycle reset.
- **Source evidence**: `framings.md` §6 second Excludes bullet —
  "Treats household cashflow as if base-salary is the binding
  constraint; for tech-worker askers a meaningful chunk of comp is
  RSU / bonus that may or may not vest. The framing's 'compute DTI
  on base only' is conservative, but the framing's 'compute DTI on
  total comp' is over-aggressive — both because RSUs are price-
  sensitive (down 60% from 2021 peaks across many public-tech) and
  because variable comp can be cut. Cross-routes `tech-career`."
- **Trigger**: Asker has > 30% of TC in unvested RSU AND is computing
  affordability against total comp AND has not stress-tested against a
  50% stock decline or a layoff scenario.
- **Failure mode**: Year 2 a sector-wide pullback halves the asker's
  RSU value AND the company does a 10% workforce reduction; asker
  survives the layoff but loses 30% of total comp; PITI is now 45% of
  base, household savings rate goes to 0, the buy is fragile.
- **Recovery move**: Cap PITI at 28–32% of base + previously-vested-
  and-sold RSU income (i.e., income that has already been crystallized
  to cash). Treat unvested RSU as upside, NOT as the load-bearing
  income for affordability. Maintain a 12-month base-salary-only PITI
  reserve for layoff coverage.

### 6.3 Childcare and eldercare line items scale with house location and are not in the formula

- **Statement**: "We can afford this house" calculations that ignore
  the $30–60k/yr daycare cost in the school-district-premium
  neighborhood are structurally wrong. The framing names cashflow but
  rarely names the location-dependent line items that go with the
  housing choice — daycare cost differential, eldercare proximity,
  household-help availability and price.
- **Source evidence**: `framings.md` §6 third Excludes bullet —
  "Under-weights childcare / eldercare line items that scale with
  house location. A 'we can afford this house' calculation that
  ignores the $30k/yr daycare in the school-district premium
  neighborhood is structurally wrong; the framing names the cashflow
  constraint but rarely names the location-dependent line items that
  go *with* the housing choice."
- **Trigger**: Asker is buying in a school-district-premium
  neighborhood AND has children under 5 AND has not budgeted
  location-specific daycare cost OR has aging parents within 50
  miles AND has not budgeted location-specific eldercare cost.
- **Failure mode**: Asker buys; year-1 daycare for two kids in
  premium-zone market is $5,500/mo (vs $3,000/mo in adjacent lower-
  zoned neighborhood); the housing decision and the daycare decision
  are coupled and the cashflow math missed it; household savings rate
  drops by half.
- **Recovery move**: Build the location-dependent line items into the
  housing-affordability math before locking the house decision —
  daycare cost in this specific zone; commute cost vs alternatives;
  household-help market rate; eldercare-distance premium. The right
  comparison is "can we afford this house WITH the location-coupled
  costs," not "can we afford this PITI."

### 6.4 The "freed cashflow" from a 28% cap often dissipates without discipline

- **Statement**: The framing's "cap at 28% to preserve flexibility"
  presumes the freed 7–17% of income flows to savings, debt payoff,
  or retirement. For households without a written investment policy
  or automatic-deduction setup, the freed cashflow empirically
  dissipates into lifestyle inflation rather than the financial-
  security goal the framing imagined.
- **Source evidence**: `framings.md` §6 fourth Excludes bullet —
  "'Cap at 28% to preserve flexibility' presumes the alternative use
  of the cash is value-creating (savings, debt payoff, retirement).
  For households without disciplined savings behavior, the 12% of
  income the framing protects often dissipates into lifestyle
  inflation rather than the financial-security goal."
- **Trigger**: Asker is choosing between a 28%-PITI house and a
  35%-PITI house AND does not have an automated savings rate of
  > 15% running for the last 12+ months.
- **Failure mode**: Asker takes the 28% house; the freed 7% flows to
  restaurant meals and weekend travel rather than to savings; the
  framing's "flexibility" benefit was theoretical and the asker
  ended year 5 with the same savings rate as a hypothetical
  35%-PITI counterfactual.
- **Recovery move**: Either install the automated-savings policy
  BEFORE the buy decision (and run it 6+ months to verify execution),
  OR accept that the framing's flexibility benefit won't materialize
  for this household and adjust the comparison accordingly.

### 6.5 15-year-vs-30-year is partly forced-savings, which this framing under-weights

- **Statement**: ARM-vs-fixed-vs-15yr decision is partly a *forced
  savings* question. The 15-year mortgage compels principal
  accumulation at a faster rate; the 30-year preserves cashflow
  flexibility. The framing's reflex toward "more cashflow flexibility
  = better" trades against the F1 reflex toward forced-savings
  discipline. For households where discretionary savings are not
  reliable, the 15-year is a forced-discipline product the cashflow
  framing systematically undersells.
- **Source evidence**: `framings.md` §6 fifth Excludes bullet — "ARM-
  vs-fixed-vs-15yr decision is partly a *forced savings* question that
  this framing under-weights — the 15-year mortgage compels principal
  accumulation; the 30-year preserves cashflow flexibility."
- **Trigger**: Asker is choosing between 15-year-fixed and 30-year-
  fixed AND is being routed to 30-year purely on cashflow-flexibility
  grounds AND has variable savings discipline.
- **Failure mode**: Asker takes the 30-year on flexibility grounds;
  the freed cashflow goes to consumption not savings; ends 15 years
  in with half the equity the 15-year would have produced and no
  meaningful brokerage offset; the flexibility was unused.
- **Recovery move**: For households with weak savings discipline,
  treat the 15-year as forced-savings infrastructure even at the cost
  of cashflow flexibility. For households with strong discipline, the
  30-year-and-invest-the-difference is correct on math — but verify
  the discipline first rather than assume it.

---

## 7. Duration-of-stay framing

### 7.1 Actual hold is a function of life-shocks the asker can't predict

- **Statement**: The framing treats expected-hold as a planning input
  derived from intent. The actual hold is a function of life-shocks
  (layoff, divorce, illness, family event) that the buyer can't
  predict and base-rate data routinely contradicts stated intent —
  NAR reports ~25% of first-time buyers sell within 5 years despite
  longer stated intentions.
- **Source evidence**: `framings.md` §7 first Excludes bullet —
  "Treats expected-hold as a planning input; misses that the *actual*
  hold is a function of life-shocks (layoff, divorce, illness, family
  event) that the buyer can't predict and the base-rate distribution
  under-weights for a specific asker. The framing's 'I'm staying 10
  years' is a stated intent that revealed-preference data flatly
  contradicts for 25–35% of first-time buyers."
- **Trigger**: Asker states a confident 10+ year horizon AND is a
  first-time buyer (NAR data: median first-time-buyer tenure is well
  below stated intent).
- **Failure mode**: Asker plans for 10-year hold; life-shock at
  year 4 forces exit; the 5-year-rule margin of safety was thin;
  asker exits at break-even-or-loss.
- **Recovery move**: Use the base rate, not the intent. For first-
  time buyers, assume 30–35% probability of selling within 5 years;
  ensure the buy clears the round-trip cost even at the 25th-
  percentile hold horizon (not just the modal hold).

### 7.2 The uniform stress-test under-personalizes by life-stage

- **Statement**: The "stress-test against 3-year hold" produces a
  conservative answer but doesn't engage with the asker's specific
  reasons. A 35-year-old single-income tech worker has a different
  transaction-cost-amortization profile than a 50-year-old dual-
  income family; the uniform stress-test under-personalizes.
- **Source evidence**: `framings.md` §7 second Excludes bullet —
  "'Stress-test against 3-year hold' produces a conservative answer
  but doesn't engage with the asker's *reasons* — a 35-year-old
  single-income tech worker has a different transaction-cost-
  amortization than a 50-year-old dual-income family. The framing's
  uniform stress-test under-personalizes."
- **Trigger**: Asker is at either end of the life-stage range
  (early-career single OR late-career stable-family) AND is being
  routed against a generic 3-year-hold test.
- **Failure mode**: Generic stress-test mis-routes the decision —
  early-career single takes too conservative a horizon (loses
  optionality value); late-career stable-family takes too aggressive
  a horizon (under-prices the still-possible illness or eldercare
  shock).
- **Recovery move**: Personalize the stress-test horizon to the
  asker's specific life-stage and shock distribution: early-career
  high-mobility = 2-year-hold stress test (very aggressive); mid-
  career rooted = 4-year (default); late-career stable = 6-year
  (still account for downsize-or-eldercare). The test is a calibrated
  base rate, not a one-size-fits-all number.

### 7.3 ARM-reset joint-failure with frozen-market is under-priced

- **Statement**: A 7/1 ARM at 5.875% saved over 30-year fixed at
  6.75% has positive value at year 5 *if* the buyer can refi or
  sell. If neither (rates higher, market frozen, life events block
  sale), the buyer takes the full reset. The framing prices the
  expected case but under-prices the *joint failure* of "rates up
  AND family event keeps you stuck."
- **Source evidence**: `framings.md` §7 third Excludes bullet —
  "Under-weights the option-value of *not* moving when life-events
  permit. A 7/1 ARM at 5.875% saved over 30-year fixed at 6.75% has
  positive value at year 5 *if* the buyer can refi or sell; if
  neither (rates higher, market frozen, life events block sale), the
  buyer takes the full reset. The framing prices the expected case
  but under-prices the joint failure."
- **Trigger**: Asker is choosing an ARM purely on the basis of "I'll
  sell or refi before reset" AND has not modeled the joint failure
  of (a) rates up at reset AND (b) market frozen / life event
  preventing sale.
- **Failure mode**: Year 7 reset arrives; rates are 200bps higher
  than at origination; local market in early contraction with 6-
  month days-on-market; asker is mid-divorce and can't easily exit;
  the cap-rate jump consumes 1/3 of monthly free cashflow.
- **Recovery move**: Stress-test the ARM against the joint failure
  scenario (rates +200bps AND can't sell). If the household can't
  carry the cap-rate payment under that scenario, the ARM is fragile
  — either price the joint failure correctly or take the fixed.

### 7.4 Soft transaction costs aren't on the break-even table

- **Statement**: The framing's break-even arithmetic depends on
  transaction cost (6–10% round-trip) and doesn't engage with the
  *softer* costs — the move itself is 2–4 weeks of household time,
  new-home settling-in is 6–12 months of friction, the kids' school
  transition is its own multi-year cost. These don't fit the break-
  even table but bind the move-or-stay decision in practice.
- **Source evidence**: `framings.md` §7 fourth Excludes bullet — "The
  framing's break-even arithmetic depends on transaction cost (6–10%
  round-trip); doesn't engage with the *softer* costs — the move
  itself is 2–4 weeks of household time, the new-home settling-in
  is 6–12 months of friction, the kids' school transition is its
  own multi-year cost."
- **Trigger**: Asker is computing break-even purely on financial
  round-trip cost AND has school-age children OR a working partner
  with a brittle commute OR a community-rooted social network.
- **Failure mode**: Break-even math says year 4 exit is OK; actual
  exit at year 4 incurs school-transition cost (a year of academic
  disruption for two kids), partner-career disruption, and 9 months
  of household-disorientation that the financial table didn't model.
- **Recovery move**: Estimate the soft transaction costs in dollar
  terms (school transition = 1 year of after-school tutoring
  budget; partner career disruption = 3–6 months income gap;
  household disorientation = lost productivity). Add to the financial
  round-trip when computing break-even. The honest break-even
  horizon is usually 1–2 years longer than the financial-only table
  shows.

### 7.5 Partial moves break the stay-vs-leave binary

- **Statement**: "Duration of stay" presumes a binary stay-or-leave.
  The actual pattern often includes *partial* moves — partner takes a
  job in another city, household maintains two residences for 18
  months, then consolidates. The framing's binary doesn't handle this
  hybrid mode and routes the asker into an all-or-nothing decision
  that doesn't match the actual constraint.
- **Source evidence**: `framings.md` §7 fifth Excludes bullet —
  "'Duration of stay' presumes a binary stay-or-leave; the actual
  pattern includes *partial* moves (the partner takes a job in
  another city, the household maintains two residences for 18 months,
  then consolidates). The framing's stay-vs-leave binary doesn't
  handle this hybrid mode."
- **Trigger**: Asker is in a dual-career household where one
  partner has a known relocation event in the 2–5 year horizon AND
  is computing the buy decision as a single-residence single-horizon
  problem.
- **Failure mode**: Partner takes the other-city job year 2; the
  household runs two residences for 14 months while transitioning;
  the original house is rented under-market by an inexperienced
  landlord; eventual sale clears at a discount; the binary frame
  missed the partial-move pattern entirely.
- **Recovery move**: For households facing likely partial-move
  pattern, plan the housing decision as a two-stage problem: stage 1
  buy something rentable (or rent something rentable-out), stage 2
  consolidate. The decision is "which of stage 1 minimizes the
  total cost across stages," not "where do we live forever."

---

## 8. Climate-and-insurance-risk framing

### 8.1 Insurance market is itself mis-priced via insurer-of-last-resort programs

- **Statement**: The framing treats insurance pricing as the
  authoritative risk signal. In FL (Citizens), CA (FAIR Plan), LA
  (Louisiana Citizens), state-mandated insurer-of-last-resort programs
  cap premiums below true risk and the catastrophic tail is absorbed
  by taxpayers via state-bailout mechanisms. The "let the insurance
  market tell you the risk" reflex works until the legislature
  decides it doesn't.
- **Source evidence**: `framings.md` §8 first Excludes bullet —
  "Frames insurance as the right price signal; misses that the
  insurance market is *itself* mis-priced — state-mandated insurer-of-
  last-resort programs (Citizens FL, FAIR CA) cap premiums below
  true risk, and the catastrophic tail risk is being absorbed by
  taxpayers via state-bailout mechanisms."
- **Trigger**: Asker is buying in FL / CA / LA AND the property is
  insured through a state-run last-resort plan OR the asker's quoted
  premium is dramatically lower than First Street Foundation /
  IBHS-modeled expected loss for the parcel.
- **Failure mode**: Year 3 the state legislature reforms the last-
  resort program (premiums rise 3–5×, coverage tightens, deductibles
  jump); asker's mortgage requires policy maintenance and the new
  reality consumes 1.5× the prior PITI; or the property becomes
  effectively uninsurable on the open market.
- **Recovery move**: For last-resort-insured properties in FL / CA /
  LA, treat the current premium as a regulatory snapshot, not a
  risk signal. Engage an insurance broker who can quote private-
  market coverage for the same parcel (often refused, which is
  itself the signal). For properties with > $500k climate exposure
  and uncertain insurance trajectory, the right referral is a
  climate-resilience-aware insurance broker AND an IBHS-certified
  inspector to surface mitigation options.

### 8.2 Insurance pricing lags underlying climate risk by 5–15 years

- **Statement**: Climate-risk trajectory is over 30 years; insurance
  pricing is typically annual and lags the underlying risk by 5–15
  years. A property that's safely insurable today may be uninsurable
  by 2035, and the current premium doesn't carry that information.
  The framing's "watch the premium" is reactive, not anticipatory.
- **Source evidence**: `framings.md` §8 second Excludes bullet —
  "Climate-risk trajectory is over 30 years; insurance pricing is
  typically annual. The framing's 'premium trajectory' signal lags
  the underlying risk by 5–15 years — a property that's safely
  insurable today may be uninsurable by 2035."
- **Trigger**: Asker is buying in a coastal / wildfire-WUI / inland-
  flood / hurricane-corridor zone for a 30-year horizon AND is using
  the current insurance premium as the trajectory anchor.
- **Failure mode**: Year 10 the property's peril category sees a
  multi-event-year (3 hurricanes, 2 wildfires); private insurers
  exit; property is uninsurable on terms acceptable to the mortgage;
  asker either sells at a 30%+ distressed discount or carries an
  uninsured asset against mortgage requirement.
- **Recovery move**: Triangulate three signals — current insurance
  premium (regulatory snapshot), First Street Foundation modeled
  30-year risk score (model output, calibrate with caveats), state-
  fire-marshal / FEMA / NWS historical event frequency for the
  parcel-vicinity. If the three signals diverge sharply, the
  framing's "watch the premium" is wrong; bias toward the higher-
  risk signal and price the long-horizon trajectory.

### 8.3 Property-level mitigation can preserve insurability that geographic-routing rejects

- **Statement**: The framing routes asker *out* of high-risk zones
  rather than naming that property-level mitigation — defensible
  space, IBHS-FORTIFIED roof retrofit, basement pump + french drain
  flood mitigation, hurricane shutters — can preserve insurability
  and sometimes secure premium discounts. The mitigation pathway is
  systematically underrepresented in geographic-screening framings.
- **Source evidence**: `framings.md` §8 third Excludes bullet — "Under-
  weights *property-level* risk mitigation (defensible space, IBHS-
  FORTIFIED retrofit, basement-pump and french-drain flood mitigation,
  hurricane-shutter installation). The framing routes asker out of
  high-risk zones rather than naming that a $30k IBHS-FORTIFIED
  retrofit can preserve insurability and sometimes secure premium
  discounts. Cross-routes F4."
- **Trigger**: Asker has identified a target property in a moderate-
  risk zone AND the insurance quote is high but available AND the
  framing is routing the asker away purely on zone designation.
- **Failure mode**: Asker over-broadens the rejection zone; passes on
  a property where a $20–40k mitigation retrofit would have brought
  insurance into the affordable range; foregoes the school zone /
  community / commute the property offered.
- **Recovery move**: For moderate-risk zones, get an IBHS-certified
  inspector or a climate-resilience consultant to scope mitigation
  options BEFORE rejecting the property. If a tractable mitigation
  package reduces the modeled risk meaningfully, the buy is in
  scope; if not, the geographic-routing rejection is correct. This
  is the decision where the climate-resilience inspector referral
  is the cost-effective pre-offer move.

### 8.4 First Street and similar private risk scores are modeled outputs, not measurements

- **Statement**: First Street Foundation and similar private risk
  scores are *modeled* outputs (not measurements) with their own
  bias structure — over-weighting riverine flood, under-weighting
  urban-stormwater flood in some metros, calibration sensitive to
  unstable forward-projection assumptions. The framing presents the
  score as ground truth when it's a model output the buyer should
  triangulate against FEMA, state hazard maps, and local historical
  data.
- **Source evidence**: `framings.md` §8 fourth Excludes bullet — "First
  Street Foundation and similar private risk scores are *modeled*
  (not measured) and have their own bias structure (over-weighting
  riverine flood, under-weighting urban-stormwater flood in some
  metros). The framing presents the score as ground truth when it's
  a model output the buyer should triangulate against FEMA, state
  hazard maps, and local historical data."
- **Trigger**: Asker is making a buy-or-reject decision based on a
  single risk score (First Street, ClimateCheck, RiskFactor) without
  cross-validation against FEMA flood maps, state hazard maps, or
  local historical data.
- **Failure mode**: Asker rejects a property on a single high First
  Street score that turns out to be model-driven (catchment-area
  over-weighting); passes on a livable property; OR accepts a
  property on a low First Street score that misses urban-stormwater
  risk visible in city historical data — basement floods year 2,
  uninsured.
- **Recovery move**: Triangulate any single risk score against
  (a) FEMA flood map (regulatory baseline, under-prices outside
  designated zones), (b) state-level hazard map (state geological
  / fire-marshal / coastal-management agency), (c) local historical
  event data (city stormwater reports, county fire history, NWS
  storm reports). A 30-year buy decision deserves 3 sources, not 1.

### 8.5 Uninsurable property has no liquidity, regardless of present-value premium math

- **Statement**: The framing protects against catastrophic loss but
  doesn't engage with the *liquidity* dimension. An uninsurable
  property in a non-renewing market has no buyer pool, and the
  discount to clear is much larger than the present value of avoided
  premium increases. The binding constraint isn't "what's my
  expected insurance cost" — it's "can I exit this property in 3
  years if I need to."
- **Source evidence**: `framings.md` §8 fifth Excludes bullet — "The
  framing protects against catastrophic loss but doesn't engage with
  the *liquidity* dimension — an uninsurable property in a non-
  renewing market has no buyer pool, and the discount to clear is
  much larger than the present value of avoided premium increases.
  The framing prices the wrong variable; the binding constraint is
  'can I exit this property in 3 years if I need to.'"
- **Trigger**: Asker is buying in a market with active insurer non-
  renewal (FL coastal, CA WUI, parts of LA / TX / NC) AND has any
  meaningful probability of needing to exit within 5 years.
- **Failure mode**: Year 3 asker needs to exit (job, family, life-
  event); private buyers can't get conventional insurance for the
  property; cash-buyer pool is small and demands 25–40% discount; the
  framing's "buy and absorb the premium" math never priced exit
  liquidity.
- **Recovery move**: For non-renewing markets, treat exit liquidity
  as the binding constraint. Request a 5-year written premium
  trajectory from the broker AND a comparable-recent-sale price list
  for properties listed > 90 days. If the discount-to-clear is > 15%
  and the asker's exit probability is > 20% in 5 years, the buy is
  fragile to exit and the framing's premium-only math is the wrong
  decision frame.

---

## 9. School-district-and-neighborhood-premium framing

### 9.1 GreatSchools rating is partly demographic sorting, not school value-add

- **Statement**: GreatSchools and similar ratings are dominated by
  test scores; test scores correlate with neighborhood demographics
  more than with school value-add. The empirical research on "school
  effects" controlling for peer composition is much weaker than the
  rating implies — the framing routes asker into the premium price
  for a signal that's partly demographic sorting, not differential
  education quality.
- **Source evidence**: `framings.md` §9 first Excludes bullet —
  "GreatSchools and similar ratings are dominated by test scores;
  test scores correlate with neighborhood demographics more than with
  school value-add. The empirical research on 'school effects'
  controlling for peer composition is much weaker than the rating
  implies."
- **Trigger**: Asker is paying a 15–30% price premium for a top-rated
  school zone AND is reasoning purely from GreatSchools / Niche /
  similar test-score-dominated ratings.
- **Failure mode**: Asker pays the school-zone premium; the
  differential education outcome turns out to be smaller than the
  rating implied (largely peer effects, replicable elsewhere); the
  premium was paid for a noisy signal.
- **Recovery move**: Look beyond test-score-dominated ratings:
  matriculation-pattern data (where do graduates go), teacher-
  retention rate, district per-pupil spending net of demographics-
  driven federal supplements, and value-added measures where the
  state publishes them. If the differential persists across those
  measures, the premium is real; if it collapses, the framing was
  measuring demographic sorting.

### 9.2 Private-tuition arbitrage under-weights adult-network and parent-social-capital

- **Statement**: "Pay private tuition and buy in cheaper zone"
  arithmetic looks appealing for K-12 ($30–60k/yr × 13 years =
  $390–780k of tuition) but under-weights that private-school
  families also pay for the high-zoned house — peer effects on
  *adult* networks, neighbor-set, parent-social-capital. The
  arbitrage is real but smaller than the headline math suggests.
- **Source evidence**: `framings.md` §9 second Excludes bullet —
  "'Pay private tuition and buy in cheaper zone' arithmetic looks
  appealing for K-12 ($30–60k/yr × 13 years = $390–780k of tuition)
  but the framing under-weights that private-school families also
  pay for the high-zoned house (peer effects on *adult* networks,
  neighbor-set, parent social capital). The arbitrage is real but
  smaller than the headline math suggests."
- **Trigger**: Asker is computing the private-tuition-vs-school-zone
  arbitrage purely on direct-cost terms and routing to private-
  tuition based on the cost delta.
- **Failure mode**: Asker buys in a lower-zoned neighborhood with
  private school; experiences the "we don't fit in the neighborhood
  socially" friction; the parent-network the asker would have built
  in the higher-zoned neighborhood would have been load-bearing for
  career / business / civic connections; the arbitrage was unpriced.
- **Recovery move**: When computing the arbitrage, name the parent-
  network / adult-social-capital good explicitly and price it at
  $5–15k/yr of equivalent membership-network expense. The arbitrage
  is real but not as large as the tuition-vs-premium math implies;
  decision depends on whether the asker actually values the parent-
  network good.

### 9.3 Boundary-street redistricting risk is named but rarely quantified

- **Statement**: Boundary-street redistricting risk is flagged in
  the framing but rarely quantified. School-board zone-line votes
  are 5–10 year recurring events, and a house bought for school
  zone X can be re-zoned to school zone Y mid-tenure — the buyer
  paid the premium for a zone the buyer no longer has access to.
- **Source evidence**: `framings.md` §9 third Excludes bullet —
  "Boundary-street redistricting risk is named but rarely quantified
  — the framing flags it without giving the asker a process for
  assessment (read the past 3 school board meeting minutes; check
  enrollment-projection reports; assess the political-coalition
  stability around the current zone lines)."
- **Trigger**: Asker is buying a house on or within 3 blocks of a
  school-zone-boundary street AND is paying the premium for the
  currently-zoned school.
- **Failure mode**: Year 4 the district redraws boundaries; the
  house is now zoned to a lower-rated school; the resale price drops
  10–15% reflecting the new zoning; the school-zone premium evaporates.
- **Recovery move**: Before buying, read the past 3 years of school
  board meeting minutes for boundary-line discussions; check
  enrollment-projection reports (most districts publish these);
  attend at least one board meeting to assess political-coalition
  stability around current zone lines. If the lines are under active
  discussion, the premium is fragile.

### 9.4 K-12 mismatch converts the school-thesis into double-pay

- **Statement**: The framing presumes the asker's kid will attend
  public school in this zone for the full duration. Doesn't engage
  with school-mismatch (kid hates the school, school pedagogy is
  wrong for the kid, kid develops special-ed needs the zone school
  can't serve well) that converts "we bought for the school" thesis
  into a property-and-tuition double-pay.
- **Source evidence**: `framings.md` §9 fourth Excludes bullet — "The
  framing presumes the asker's kid will attend public school in this
  zone for the full duration. Doesn't engage with school-mismatch
  (the kid hates the school, the school's pedagogy is wrong for the
  kid, the kid develops special-ed needs the zone school can't
  serve well) that converts the 'we bought for the school' thesis
  into a property-and-tuition double-pay. Cross-routes `family-
  planning`."
- **Trigger**: Asker is paying a 20%+ school-zone premium for a kid
  not yet in the K-12 system OR with characteristics (gifted /
  special-ed / strong specific pedagogical needs) where the zone
  school is not pre-validated as fit.
- **Failure mode**: Year 3 the kid hates the school OR the school
  can't serve a discovered special-ed need; family pays K-12 tuition
  on top of the zone premium; the "we bought for the school" thesis
  doubles the cost.
- **Recovery move**: Before paying the zone premium for an unborn
  or pre-K kid, model the probability of school-mismatch (10–20%
  base rate for K-12 fit; higher for special-needs or gifted) and
  the cost of the alternative private/charter/magnet path; ensure
  the buy clears even under the 20%-mismatch scenario.

### 9.5 Commute delta against school premium is rarely priced

- **Statement**: A top-zoned house 40 minutes from work trades the
  school premium against 80 minutes/day of commute (~6 hours/week
  of life). The framing's "the schools are worth it" gets weighted
  against the F2 (lifestyle-flexibility) reflex; the asker needs
  both axes priced.
- **Source evidence**: `framings.md` §9 fifth Excludes bullet —
  "Under-weights the *commute* delta. A top-zoned house 40min from
  work trades the school premium against 80min/day of commute
  (= ~6 hours/wk of life). The framing's 'the schools are worth
  it' gets weighted against the F2 (lifestyle-flexibility) reflex;
  the asker needs both axes priced."
- **Trigger**: Asker is comparing two houses — one in a top school
  zone with a long commute, one in a moderate zone with a short
  commute — and is routing purely on school rating.
- **Failure mode**: Asker buys the top-zoned house; the daily 80-
  minute commute consumes the gains over the next 10 years (lost
  family time, lost sleep, lost personal time, gas/wear cost,
  commute-attributable stress); the school benefit was real but
  the commute cost was higher and unpriced.
- **Recovery move**: Price the commute delta in dollars and hours
  before locking the school decision: 6 hours/week × 50 weeks ×
  $50/hour shadow rate = $15k/yr; add gas / vehicle wear at
  ~$3k/yr; add commute-stress / sleep-quality cost (estimated
  at 5% of base salary, conservatively). Compare against the
  annualized school premium; if commute cost > school premium,
  the moderate-zone-short-commute house wins.

---

## 10. Investor-leverage / cap-rate framing

### 10.1 Cap-rate uses current rent but ignores rent-stabilization upside-cap

- **Statement**: Cap-rate arithmetic uses *current* rent and *current*
  expenses; misses that rent-growth projections vary 5× by metro and
  that rent-stabilization regimes (NYC, SF, LA, Oregon statewide,
  parts of NJ, pending in Minneapolis) cap upside. The framing's "5%
  cap rate plus rent growth" assumes a free rent-growth model that
  doesn't hold in regulated jurisdictions.
- **Source evidence**: `framings.md` §10 first Excludes bullet — "Cap-
  rate arithmetic uses *current* rent and *current* expenses; misses
  that rent-growth projections vary 5× by metro and that rent-
  stabilization regimes (NYC, SF, LA, Oregon statewide, parts of NJ)
  cap upside. The framing's '5% cap rate plus rent growth' assumes a
  free rent-growth model that doesn't hold in regulated jurisdictions.
  Cross-routes `legal-disputes`."
- **Trigger**: Asker is buying a rental property in a rent-stabilized
  or rent-controlled jurisdiction AND is using a free-market rent-
  growth projection in the underwriting.
- **Failure mode**: Asker buys assuming 4%/yr rent growth; the unit
  is stabilized at CPI-only or CPI-plus-2% growth; the rent-growth
  thesis collapses; cap rate over 10 years is half what was
  modeled.
- **Recovery move**: Before underwriting, confirm the regulatory
  status of every unit in the property (some buildings are partially
  stabilized, partially market-rate). For stabilized units, use the
  regulatory cap as the rent-growth ceiling, not the free-market
  projection. Cross-validate with local tenant-union or rent-board
  data on actual realized growth.

### 10.2 Depreciation recapture is deferred, not avoided, for active trade-ups

- **Statement**: Depreciation deduction lowers current taxable income;
  the framing prices the *current* benefit but under-prices the
  depreciation-recapture obligation at sale (25% recapture rate vs
  0–20% capital gains). For hold-to-death (step-up-in-basis erases
  recapture), the deduction is permanent. For active trade-up
  scenarios, recapture is a real drag the framing rarely surfaces
  honestly.
- **Source evidence**: `framings.md` §10 second Excludes bullet —
  "Depreciation deduction lowers current taxable income; the framing
  prices the *current* benefit but under-prices the depreciation-
  recapture obligation at sale (25% recapture rate vs 0–20% capital
  gains). For hold-to-death the step-up-in-basis erases the recapture;
  for active trade-up scenarios the recapture is a real drag. Cross-
  routes `personal-finance`."
- **Trigger**: Asker is buying an investment property AND is being
  shown a 10-year hold IRR that uses depreciation deduction as
  benefit AND has not modeled the recapture at sale.
- **Failure mode**: Year 10 asker sells; depreciation recapture +
  capital gains + state tax + NIIT consume 25–35% of the gain; the
  IRR is meaningfully lower than the depreciation-benefit-only
  underwriting showed.
- **Recovery move**: For any investment property with an expected
  hold < 15 years, model depreciation as a tax *deferral* not a
  tax *elimination*; compute the recapture explicitly at expected
  sale. Pair every investment-property analysis with a CPA review
  before close — recapture interacts with the asker's full tax
  situation (other passive losses, real-estate-professional status,
  Section 121 if converted to primary) and is exactly the kind of
  six-figure tail risk the CPA referral exists to surface.

### 10.3 Real-estate-professional status is unavailable for most W-2 tech askers

- **Statement**: "Real estate professional status" unlocks active-
  loss treatment against W-2 income but requires 750+ hours/yr of
  qualifying real-estate activity AND > 50% of total work time. For
  full-time-employed tech workers, this status is generally
  unavailable; the framing's "depreciation offsets your W-2" is
  correct only for spouses or after-tech-exit askers.
- **Source evidence**: `framings.md` §10 third Excludes bullet — "'Real
  estate professional status' unlocks active-loss treatment against
  W-2 income but requires 750+ hours/yr of qualifying real-estate
  activity and >50% of total work time. For full-time-employed tech
  workers this status is generally unavailable; the framing's
  'depreciation offsets your W-2' is correct only for spouses or
  after-tech-exit."
- **Trigger**: Asker is full-time W-2 employed in tech AND is being
  routed to investment property on the thesis that depreciation will
  offset W-2 income.
- **Failure mode**: Asker buys; files taxes year 1 expecting passive-
  loss offset against W-2; IRS limits the offset to $25k (and only
  if MAGI < $100k, phasing out by $150k — which the tech worker is
  almost certainly above); the depreciation-benefit thesis was wrong
  for this asker.
- **Recovery move**: For W-2-employed tech-worker askers, do NOT
  underwrite investment property assuming RE professional status;
  use the passive-loss-limit math (suspended losses carry forward
  but provide no current-year W-2 offset). The CPA referral here
  is the right move — RE-professional-status optimization is a
  joint-filer (spouse can qualify) or post-tech-exit play, not a
  shortcut for the modal tech-worker.

### 10.4 Operational drag eats ~10% of cap rate the spreadsheet doesn't model

- **Statement**: The framing's cap-rate math assumes operations are
  frictionless; in practice the self-managing landlord loses ~10%
  of cap rate to time-cost the spreadsheet doesn't model — tenant
  selection, eviction process (3–18 months by state), repairs at 2am,
  property-management-vs-self-management decision. The headline cap
  rate over-states realized return.
- **Source evidence**: `framings.md` §10 fourth Excludes bullet —
  "Under-weights *operational drag* — tenant selection, eviction
  process (3–18 months by state), repairs at 2am, property-management-
  vs-self-management decision. The framing's cap-rate math assumes
  operations are frictionless; in practice the self-managing landlord
  loses ~10% of cap rate to time-cost the spreadsheet doesn't model."
- **Trigger**: First-time investor asker is self-managing AND is
  underwriting at a 6–7% cap rate assuming pass-through operations.
- **Failure mode**: Year 1 the asker fields a 2am water leak, spends
  weekends screening tenants, and absorbs a 3-month vacancy on a bad
  tenant; the realized cap rate is 4.5% not 6.5%; the headline math
  over-stated by 30%.
- **Recovery move**: Either pre-budget property management at 8–10%
  of rent (and accept the lower cap rate explicitly), OR pre-budget
  the asker's own time at a market shadow rate (~$50–100/hr) and
  back it out of NOI. The honest cap rate is one of these two
  numbers, not the property-management-free headline.

### 10.5 Single-property concentration risk is the inverse of leverage

- **Statement**: The framing prices the asset in isolation but
  doesn't engage with *concentration risk* — a single $700k rental
  is 3–10× a typical investor's portfolio asset, undiversified
  across geography and tenant. "Leverage amplifies return" is the
  framing's load-bearing line; "concentration amplifies tail risk"
  is the inverse the framing rarely names.
- **Source evidence**: `framings.md` §10 fifth Excludes bullet — "The
  framing prices the asset in isolation; doesn't engage with
  *concentration risk* — a single $700k rental is 3–10× a typical
  investor's portfolio asset, undiversified across geography and
  tenant. The framing's 'leverage amplifies return' is true and the
  'concentration amplifies tail risk' is the inverse the framing
  rarely names."
- **Trigger**: Asker is buying first investment property AND it
  represents > 30% of total household net worth AND is geographically
  concentrated with the asker's primary residence.
- **Failure mode**: Local employer (Boeing in Seattle, oil in
  Houston, casinos in Vegas) shedding workforce; same metro that
  houses asker's W-2 job and rental property; correlated tenant-
  default and primary-job-risk shock simultaneously.
- **Recovery move**: For first investment property representing > 25%
  of net worth, prefer geographic diversification from primary
  residence (different metro / state / employer concentration); OR
  ensure REIT / index-fund offset in the household portfolio brings
  the housing-real-estate concentration below 40%; OR explicitly
  treat the single-property bet as a concentrated bet and limit
  total real-estate exposure accordingly.

---

## 11. Transaction-cost-amortization framing

### 11.1 The 8–12% round-trip cost is an average; some niches are 15–25%

- **Statement**: The framing's flat "8–12% round-trip" is an average
  number. For luxury condos, specialty homes, climate-stressed
  markets, the realized selling friction is 15–25% — longer days-on-
  market, larger price concessions, multiple price drops. The flat
  number under-prices illiquid niches.
- **Source evidence**: `framings.md` §11 first Excludes bullet — "The
  8–12% round-trip is an average; for some property types (luxury
  condos, specialty homes, climate-stressed markets) selling friction
  is 15–25%. The framing's flat number under-prices illiquid niches."
- **Trigger**: Asker is buying in an illiquid niche — luxury (top 5%
  of metro price distribution), specialty (large lot, unique
  architecture, age-restricted community), or climate-stressed
  market — AND is using a generic 8–10% round-trip cost in
  break-even math.
- **Failure mode**: Asker exits a luxury condo at year 5; days-on-
  market is 240+; final clearing price is 18% below ask; round-trip
  cost ends at 22% all-in; the break-even math was wrong.
- **Recovery move**: For illiquid niches, look up the recent
  comparable-sale data — median days-on-market for the property's
  segment, price-cut frequency, ask-vs-close-price spread. Use
  these to compute a niche-specific round-trip cost, often 15–22%,
  not the generic 8–10%.

### 11.2 5-year rule fails in turning-market contractions

- **Statement**: "5-year rule" is necessary but not sufficient.
  Buying for 5 years at the top of a rate cycle into a falling-
  price environment can clear the round-trip on amortization
  arithmetic but leave the buyer with no exit liquidity; the
  framing's break-even math assumes a continuous-pricing market and
  ignores days-on-market expansion in turning markets.
- **Source evidence**: `framings.md` §11 second Excludes bullet —
  "'5-year rule' is necessary but not sufficient. Buying for 5 years
  at the top of a rate cycle into a falling-price environment can
  still clear the round-trip on appreciation arithmetic but leave
  the buyer with no exit liquidity. The framing's break-even math
  assumes a continuous-pricing market and ignores days-on-market
  expansion in turning markets."
- **Trigger**: Asker is buying at late-expansion or peak in a market
  that's beginning to show months-of-supply expansion AND is
  reasoning purely from "I'll hold 5 years and break even on round-
  trip."
- **Failure mode**: Year 5 exit; the local market is in early
  contraction with 6-month-plus days-on-market; the listing sits
  for 9 months at sequentially-lower prices; the round-trip cost
  ends at 15%+ on the realized clearing price; break-even math
  was off.
- **Recovery move**: In late-expansion markets, demand a longer
  margin-of-safety hold horizon than the 5-year rule — 7-year is
  conservative — and budget for the worst-case days-on-market
  expansion the local market has shown in any 5-year window.

### 11.3 Refinance "monthly savings" view hides the amortization-clock reset

- **Statement**: Refinance arithmetic ("save $300/mo, pay $9k
  closing, break even in 30 months") doesn't account for
  amortization-clock reset — refinancing from year 7 of 30 to a new
  30 re-extends payoff by 7 years. The framing's monthly-savings
  view ignores the lifetime-interest-paid increase.
- **Source evidence**: `framings.md` §11 third Excludes bullet —
  "Refinance arithmetic ('save $300/mo, pay $9k closing, break even
  in 30 months') doesn't account for amortization-clock reset —
  refinancing from year 7 of 30 to a new 30 re-extends payoff by 7
  years. The framing's monthly-savings view ignores the lifetime-
  interest-paid increase. Cross-routes F1."
- **Trigger**: Asker is considering a refinance from year 5+ of an
  existing 30-year mortgage to a new 30-year AND is computing
  break-even purely on monthly-savings vs closing cost.
- **Failure mode**: Asker refinances year 7 to new 30; saves
  $300/mo for 22 years (vs 23 years remaining on original); the
  monthly-savings break-even arithmetic showed a win, but the
  lifetime-interest-paid increase ($40–80k extra over the new full
  30-year term) was unpriced.
- **Recovery move**: For any refinance from year 5+ of a 30-year
  mortgage, compute lifetime-interest-paid under both the
  status-quo and the refi-to-new-30 scenarios; consider refi-to-
  shorter-term (15-year, 20-year) or apply the monthly savings as
  principal-acceleration to neutralize the clock-reset; engage a
  fee-only mortgage broker to model the alternatives. For larger
  loan amounts (> $500k) where the lifetime-interest delta is
  meaningful, this is also the kind of decision a CPA review can
  improve by accounting for the mortgage-interest-deduction shift
  under current TCJA cap.

### 11.4 Renovation cost-recoupment is median data hiding wide variance

- **Statement**: Renovation cost-recoupment ratios from Remodeling
  Magazine's Cost vs Value report are *median* numbers; outliers
  (over-improving for the neighborhood, kitchen renovations into a
  declining market, owner-installed work that depreciates resale)
  can recoup < 50%. The framing names the ratio but rarely names
  the variance.
- **Source evidence**: `framings.md` §11 fourth Excludes bullet —
  "Renovation cost-recoupment ratios from Remodeling Magazine's
  Cost vs Value report are *median* numbers; outliers (over-
  improving for the neighborhood, kitchen renovations into a
  declining market, owner-installed work that depreciates resale)
  can recoup < 50%. The framing names the recoupment ratio but
  rarely names the variance."
- **Trigger**: Asker is planning a $50k+ renovation budget on a
  property in an over-improved range relative to neighborhood
  median OR in a declining market OR with DIY substantial work.
- **Failure mode**: Asker spends $80k on a kitchen renovation;
  neighborhood ceiling is 30% below the renovated comp; buyer pool
  at exit doesn't pay the recoupment; asker eats 60%+ of the
  renovation cost.
- **Recovery move**: For any renovation > 15% of property value,
  validate the neighborhood-ceiling comp before starting the
  renovation. Cap the renovation budget at neighborhood-ceiling-
  minus-buy-price. If the gap is small, the over-improvement risk
  is high; either scope down or rebudget against the consumption-
  value benefit (you enjoy the renovation, you don't recover at
  sale).

### 11.5 Post-2024 NAR settlement changed buyer-side commission mechanics

- **Statement**: The framing treats commission as an unavoidable
  5–6% line item. Post-2024 NAR settlement: commissions are now
  explicitly negotiable; listings cannot publish buyer-side
  commission; buyers increasingly sign written buyer-agency
  agreements that fix the buyer's-agent fee. The "5–6% is the cost"
  calibration is for a regime that just changed.
- **Source evidence**: `framings.md` §11 fifth Excludes bullet — "The
  framing treats commission as an unavoidable line item; doesn't
  engage with the buyer-agent commission post-2024 NAR settlement
  (commissions are now explicitly negotiable; listings cannot
  publish buyer-side commission; buyers increasingly sign written
  buyer-agency agreements that fix fee)."
- **Trigger**: Asker is closing a buy transaction AFTER the
  post-2024 NAR settlement effective date AND is being told the
  buyer's-side commission is "what it's always been."
- **Failure mode**: Asker signs a buyer-agency agreement at 2.5% on
  reflex; doesn't negotiate; pays $20–30k on a $1M house for
  agent services where a 1.5–2% negotiated fee or a flat-fee
  ($5–10k) buyer's-agent model would have been available.
- **Recovery move**: Before signing a buyer-agency agreement,
  interview 2–3 buyer's-agents on fee structure: flat fee, 1–1.5%,
  hourly. The post-settlement market is fluid; flat-fee buyer's-
  agents are increasingly viable on transactions where the buyer is
  pre-pre-qualified and the agent's main job is showings and
  paperwork rather than discovery and negotiation. For high-
  consequence transactions (> $1M, complex contingency stack,
  attorney-mandatory state), a real-estate-attorney engagement
  often substitutes for a chunk of buyer's-agent work at lower
  total cost.

---

## 12. Tenant-rights / landlord-tenant-statute framing

### 12.1 Tenant-rights statutes are dead-letter without legal-aid funding

- **Statement**: A tenant-favorable statute in a jurisdiction without
  funded legal aid means the tenant's nominal rights aren't
  operational without $5–15k in attorney fees. The framing's "you
  have the right to X" is structurally true and practically often
  dead-letter — the right that requires private counsel to enforce
  is functionally a right only for the high-income tenant.
- **Source evidence**: `framings.md` §12 first Excludes bullet —
  "Treats statute as the operative reality; misses that *enforcement*
  varies — a tenant-favorable statute in a jurisdiction without
  legal aid funding means the tenant's nominal rights aren't
  operational without $5–15k in attorney fees."
- **Trigger**: Tenant-asker is considering enforcing a statutory
  right (security-deposit return, repair obligation, retaliation
  defense) AND the jurisdiction has known under-funded legal aid
  (most non-coastal small-city jurisdictions, much of the South
  and Mountain West).
- **Failure mode**: Tenant pays $3,000 in attorney consultation
  fees to recover a $1,800 security deposit; the legal-cost-to-
  recovery ratio is upside-down; the statute that "guaranteed" the
  return was dead-letter in practice.
- **Recovery move**: Before relying on a statutory right, check
  whether the jurisdiction has funded legal aid for landlord-tenant
  matters (Legal Services Corporation, state bar pro-bono programs,
  tenant union legal clinics). If yes, the right may be operational.
  If no, treat the right as nominal and pursue informal resolution
  (small claims for amounts under the limit, mediation, paying-not-
  enforcing as the rational individual response). For amounts > 10k
  or for retaliation-eviction defense where the stakes are housing
  itself, a real-estate-attorney consultation is the right move.

### 12.2 Informal economics resolve most landlord-tenant matters; the formal framing over-models

- **Statement**: The framing prices the security-deposit and just-
  cause angles correctly but under-weights the *informal*
  economics — most landlord-tenant relationships are resolved
  without invoking statute (landlord absorbs $200 of damage rather
  than fight, tenant breaks the lease and forfeits one month's rent
  rather than litigate). The statutory framing over-models the
  formal pathway.
- **Source evidence**: `framings.md` §12 second Excludes bullet —
  "The framing prices the security-deposit and just-cause angles
  correctly but under-weights the *informal* economics — most
  landlord-tenant relationships are resolved without invoking
  statute (landlord absorbs $200 of damage rather than fight, tenant
  breaks the lease and forfeits one month's rent). The statutory
  framing over-models the formal pathway."
- **Trigger**: Tenant or landlord-asker is escalating to statute
  on a dispute < $2,000 in expected outcome AND the relationship
  is not otherwise broken.
- **Failure mode**: Either party invokes statute on a small-dollar
  dispute; consumes attorney time and counterparty goodwill; the
  formal resolution costs more than the dispute amount on both
  sides; relationship becomes adversarial unnecessarily.
- **Recovery move**: For disputes < $2,000, attempt informal
  resolution first — direct conversation, a written demand with
  reasonable settlement, mediation through a community housing
  organization. Reserve statutory invocation for disputes > $5,000
  or for clear pattern-of-bad-faith counterparty behavior. Sometimes
  the right answer is "pay the small loss and move on" rather than
  enforce a right that costs more to vindicate than the right is
  worth.

### 12.3 Rent-stabilization has complex exit conditions that erode protection

- **Statement**: Rent-stabilization regimes have *complex* exit
  conditions — vacancy decontrol (NYC pre-2019), preferential rent
  expirations, individual-apartment-improvement (IAI) increases,
  luxury decontrol thresholds. The framing's "this unit is
  stabilized" is a snapshot that can erode through landlord-
  initiated actions the tenant rarely sees coming.
- **Source evidence**: `framings.md` §12 third Excludes bullet —
  "Rent-stabilization regimes have *complex* exit conditions —
  vacancy decontrol (NYC pre-2019), preferential rent expirations,
  individual-apartment-improvement increases, luxury decontrol
  thresholds. The framing's 'this unit is stabilized' is a snapshot
  that can erode through landlord-initiated actions. Opposes F10."
- **Trigger**: Tenant-asker is renting a stabilized unit AND is
  treating the rent ceiling as a permanent fact OR landlord-asker is
  buying a stabilized building expecting the cap to persist.
- **Failure mode**: For tenant — landlord triggers IAI capital
  improvement; the apartment's regulated rent ceiling jumps by 20%;
  the stability the tenant counted on erodes. For landlord — the
  state legislature tightens the regime (NYC 2019 HSTPA); the
  expected vacancy-decontrol upside disappears retroactively.
- **Recovery move**: For tenants — read the local rent-stabilization
  rulebook on IAI, MCI (major capital improvement), and individual
  apartment improvement thresholds; document the apartment's
  pre-IAI condition obsessively; know the appeal/challenge process.
  For landlords — model rent stabilization as a regulatory floor on
  the upside, not a frictional inconvenience to be worked around;
  consult a real-estate attorney in the jurisdiction on the actual
  regulatory trajectory before underwriting on the basis of
  expected loopholes.

### 12.4 Eviction-time-cost is rarely modeled in cap-rate math

- **Statement**: For investor-landlords the framing names the
  eviction-cost line item but rarely the *time* line item — even a
  30-day eviction is 30 days of zero rent plus prep cost; a 6-month
  California eviction with a holdover proceeding is 6 months of
  zero rent plus $10–20k in legal fees plus property damage during
  the contested period. The framing names eviction as risk; the IRR
  math rarely models the variance.
- **Source evidence**: `framings.md` §12 fourth Excludes bullet —
  "For investor-landlords the framing names the eviction-cost line
  item but rarely the *time* line item — even a 30-day eviction is
  30 days of zero rent plus prep cost; a 6-month California eviction
  with a holdover proceeding is 6 months of zero rent plus $10–20k
  in legal fees plus property damage during the contested period."
- **Trigger**: Landlord-asker is underwriting a rental property in
  a tenant-friendly jurisdiction (CA, NY, NJ, OR, WA) AND has
  modeled eviction as a one-time cost rather than a multi-month
  zero-rent-plus-damage line item.
- **Failure mode**: Year 2 a non-paying tenant; eviction takes 4
  months; lost rent ($12k) + legal fees ($8k) + property damage
  during holdover ($5k) + post-eviction turnover ($3k) = $28k
  realized loss; the cap-rate underwriting modeled $5k.
- **Recovery move**: For investments in tenant-friendly jurisdictions,
  model an eviction event with a 3-year probability (typically
  5–15% for SFR rentals, higher for multifamily in high-turnover
  markets) and the jurisdiction-specific median timeline and cost.
  Build a reserve for the modeled eviction event into the
  underwriting; rent-screen aggressively at lease-signing to lower
  the probability.

### 12.5 House-hackers straddle both sides; framing rarely names the polarity flip

- **Statement**: The framing's tenant-side and landlord-side
  perspectives are *opposing* — the same statute is protective to
  one and constraining to the other. The framing rarely flags that
  the asker's role (tenant / landlord / both via house-hacking)
  flips the polarity of every statutory provision. House-hackers in
  particular straddle both sides on the same property and need to
  read the statute from both perspectives.
- **Source evidence**: `framings.md` §12 fifth Excludes bullet — "The
  framing's tenant-side and landlord-side perspectives are *opposing*
  — the same statute is protective to one and constraining to the
  other. The framing rarely flags that the asker's role (tenant /
  landlord / both via house-hacking) flips the polarity of every
  statutory provision. House-hackers in particular straddle both
  sides on the same property and need to read the statute from both
  perspectives."
- **Trigger**: Asker is house-hacking (owner-occupied multifamily,
  ADU rental, primary-with-roommate) AND is reading the local
  statute from only one side (typically the landlord side, ignoring
  the warranty-of-habitability obligations owed to the tenant in the
  other unit).
- **Failure mode**: Asker as landlord under-serves the warranty-of-
  habitability standard for the rented unit; tenant escalates with
  a 4-hour-notice-to-repair letter (or whatever the state requires);
  landlord-asker is caught flat-footed because the asker has been
  reading the statute only as the owner.
- **Recovery move**: For house-hackers, read the statute twice — once
  from the landlord's perspective (rights and obligations as
  landlord) and once from the tenant's perspective (the duties the
  asker owes to the tenant unit). Engage a local real-estate attorney
  for a one-hour pre-occupancy review of the statutory obligations
  on both sides; the cost is < $500 and the surfaced obligations
  prevent the modal house-hacker compliance failures.

---

## 13. Pro-buyer / consumer-advocate framing

### 13.1 Counterparties are repeat-game players, not single-shot adversaries

- **Statement**: The framing treats counterparty-adversarial as the
  dominant frame; misses that real-estate transactions are *repeat*
  games for the professionals — agents in a metro see the same
  buyers, sellers, and agents over years, and reputational concerns
  discipline behavior beyond what the static-game framing predicts.
  Treating every agent as an adversary routes the buyer into needless
  friction with counterparts who need referrals and reviews.
- **Source evidence**: `framings.md` §13 first Excludes bullet —
  "Treats counterparty-adversarial as the dominant frame; misses
  that real-estate transactions are *repeat* games for the
  professionals — agents in a metro see the same buyers / sellers /
  agents over years, and reputational concerns discipline behavior
  beyond what the static-game framing predicts."
- **Trigger**: Asker is being routed into maximum-adversarial mode
  with their own buyer's-agent (refusing to share decision criteria,
  treating every recommendation as conflicted) when the agent's
  long-term reputational stake disciplines behavior more than the
  single-transaction commission incentive.
- **Failure mode**: Asker treats own buyer's-agent as adversary;
  buyer's-agent reduces effort and information-sharing; the
  reciprocal cooperation the asker would have gained from a normal
  client relationship doesn't materialize; the asker pays the
  same commission for worse service.
- **Recovery move**: Distinguish between buyer's-agent (your
  fiduciary; build cooperative relationship) and other counterparties
  (seller's agent, mortgage broker without buyer relationship, agent-
  referred inspector — apply more skepticism). Treat repeat-game
  reputation as a real disciplining mechanism for your own buyer's-
  agent; the consumer-advocate reflex applies harder to single-
  transaction counterparts than to repeat ones.

### 13.2 3-broker mortgage shopping is aspirational for the modal time-constrained asker

- **Statement**: "Shop the mortgage" assumes the buyer has the
  bandwidth to submit 3+ applications, each generating a credit
  pull and a week of broker conversations. For the modal asker
  (working full-time, in a 30-day close window), 3-broker shopping
  is aspirational; 2-broker quote-shopping is realistic. The framing
  under-weights the operational cost of the consumer-advocate
  process.
- **Source evidence**: `framings.md` §13 second Excludes bullet —
  "'Shop the mortgage' assumes the buyer has the bandwidth to submit
  3+ applications, each generating a credit pull and a week of broker
  conversations. For the modal asker (working full-time, in a 30-day
  close window), 3-broker shopping is aspirational; 2-broker quote-
  shopping is realistic. The framing under-weights the operational
  cost of the consumer advocate process."
- **Trigger**: Asker is being told to shop 3+ mortgage quotes AND has
  a 30-day-or-shorter close window AND a full-time job AND no prior
  experience with multi-lender shopping.
- **Failure mode**: Asker tries to shop 3+ and burns out at lender 2;
  takes a sub-optimal rate at lender 2 because the close clock is
  ticking; the broker-shopping benefit was less than the time-cost
  expended.
- **Recovery move**: 2-broker shopping is the modal realistic target.
  One should be a low-cost direct lender (credit union, online
  lender), one should be a broker who can shop across 5–15 wholesale
  lenders simultaneously. This pair covers most of the rate-shopping
  benefit at half the operational cost.

### 13.3 Adversarial mode closes information channels with the seller's agent

- **Statement**: The framing emphasizes adversarial-mode in a way
  that under-uses *cooperative* moves — the seller's agent often
  has information the buyer's agent doesn't (off-market comps,
  seller motivation, contingency-removal flexibility) and a cordial
  repeat-game relationship surfaces these. The "we're adversaries"
  reflex closes information channels.
- **Source evidence**: `framings.md` §13 third Excludes bullet —
  "The framing emphasizes adversarial-mode in a way that under-uses
  *cooperative* moves — the seller's agent often has information
  the buyer's agent doesn't (off-market comps, seller motivation,
  contingency-removal flexibility) and a cordial repeat-game
  relationship surfaces these. The buyer's 'we're adversaries'
  reflex closes information channels."
- **Trigger**: Asker is in active negotiation on a specific
  property AND refuses any direct interaction with the listing
  agent AND has not asked the buyer's-agent to surface seller
  motivation / timing / contingency flexibility.
- **Failure mode**: Asker submits an offer that misses the seller's
  actual constraint (the seller needs a 60-day post-close possession
  to find next-house; asker's 30-day close doesn't work; the offer
  is rejected for a reason the buyer's-agent could have surfaced
  with a 10-minute conversation with listing agent).
- **Recovery move**: Permit your buyer's-agent to have professional
  conversation with the listing agent — seller motivation, timing
  preferences, what the seller cares about beyond price. Sharing
  decision criteria does not equal weakness; it equals
  better-matched offers. Adversarial-on-price; cooperative-on-fit.

### 13.4 Inspection tiers are under-specified by the generic "get an inspection"

- **Statement**: The framing's "get an inspection" is correct in
  direction but under-specified. Tiers: general inspector ($400–800),
  sewer scope ($150–300, often skipped, frequently the most
  important single inspection), structural engineer ($500–1500 when
  red flags appear), industrial-hygienist for mold / asbestos / lead
  ($300–800 each), foundation specialist ($500–1500), termite/WDO
  inspection ($75–150), radon test ($150).
- **Source evidence**: `framings.md` §13 fourth Excludes bullet —
  "Inspector selection is named but the framing rarely distinguishes
  inspection *tiers* — general inspector ($400–800), sewer scope
  ($150–300, often skipped, frequently the most important
  inspection), structural engineer ($500–1500 when red flags
  appear), industrial-hygienist (mold, asbestos, lead — $300–800
  each). The framing's 'get an inspection' is correct in direction
  but under-specified."
- **Trigger**: Asker is closing on a property > 30 years old OR with
  any visible distress flags (stains on ceiling / foundation cracks
  / odor signals) AND is planning only a general inspection.
- **Failure mode**: General inspection misses a $25k sewer-line
  replacement (sewer scope was skipped); year 2 the line backs up
  during a heavy rain event; the asker eats the replacement on top
  of full mortgage; would have been a $15k buyer-credit at closing
  if surfaced during inspection.
- **Recovery move**: For any property > 30 years old, always add the
  sewer scope ($150–300) and a foundation walkaround ($150–300)
  to the general inspection. For coastal / wildfire / high-radon
  / pre-1978 (lead) / pre-1980 (asbestos) properties, add the
  specialist inspections that apply. The general inspector should
  flag when an upgrade-tier specialist is needed; don't take "looks
  ok to me" from a generalist on a structurally-suspect property.

### 13.5 Post-2024 NAR settlement opens negotiating room the framing doesn't yet model

- **Statement**: Post-2024 NAR settlement changed buyer-side
  commission mechanics — commissions are now explicitly negotiable,
  written buyer-agency agreements are required, listings can't
  publish buyer-side comp. The framing's "agent commissions are
  5–6%" is calibrated to the prior regime; the new regime opens
  negotiating room the framing rarely names.
- **Source evidence**: `framings.md` §13 fifth Excludes bullet —
  "Post-2024 NAR settlement changed buyer-side commission mechanics
  (now explicitly negotiable, written buyer-agency agreements
  required, listings can't publish buyer-side comp). The framing's
  'agent commissions are 5–6%' is calibrated to the prior regime;
  the new regime opens negotiating room the framing rarely names."
- **Trigger**: Asker is closing post-2024 NAR-settlement AND is
  treating buyer-agent commission as a fixed 2.5–3% cost.
- **Failure mode**: Asker signs a buyer-agency agreement at 2.5%
  reflexively; doesn't negotiate or shop; pays $25k on a $1M
  transaction for services that a 1.5% negotiated rate or a flat
  fee would have covered.
- **Recovery move**: Before signing any buyer-agency agreement
  post-settlement, interview at least 2 agents on fee structure
  options — flat fee, hourly, lower percentage. The fluid market
  rewards askers who name the options; the rigid market punished
  askers who didn't. For high-value transactions in attorney-
  mandatory states (NY, NJ, MA, GA), substituting a real-estate-
  attorney engagement for some of the buyer's-agent scope often
  reduces total cost.

---

## 14. Macro-housing-cycle framing

### 14.1 "Buy in a buyers' market" coincides with credit tightening that excludes the asker

- **Statement**: "Buy in a buyers' market" is structurally correct
  and operationally hard — buyers' markets coincide with credit
  tightening (lender standards rise, fewer loans approved) and
  distressed-seller markets are also distressed-buyer environments
  (job loss, recession). The framing's reflex can route the asker
  into a market they may not be able to transact in.
- **Source evidence**: `framings.md` §14 first Excludes bullet —
  "'Buy in a buyers' market' is structurally correct and
  operationally hard — buyers' markets coincide with credit
  tightening (lender standards rise, fewer loans approved) and
  distressed-seller markets are also distressed-buyer environments
  (job loss, recession). The framing's reflex routes the asker
  into a market they may not be able to transact in. Opposes F6
  (cashflow) in those scenarios."
- **Trigger**: Asker is "waiting for a downturn" to buy AND has not
  pre-qualified at current rates AND is in an industry with
  recession-sensitive employment (tech, finance, media, biotech).
- **Failure mode**: Downturn arrives; mortgage lenders tighten
  standards; asker no longer qualifies at the lower price; asker's
  own job becomes uncertain (the same downturn); the planned
  arbitrage was foreclosed by the very conditions that produced
  the buying opportunity.
- **Recovery move**: Pre-qualify at current rates today; lock in
  the qualification (good for 90–120 days, can be re-pulled).
  Build a cash reserve sized to 12 months of carrying cost so the
  asker's own employment shock doesn't foreclose the buy
  capability. Treat "buy in a downturn" as a thesis robust to
  asker-side shocks, not a free lunch.

### 14.2 National-cycle framing under-models metro variance

- **Statement**: In 2022, Austin and Phoenix saw 15–20% price
  declines while NYC and DC were flat-to-positive; the "we're in a
  downturn" framing obscures the metro-level reality. The framing's
  "the cycle says wait" can be wrong by 18 months for the asker's
  specific metro.
- **Source evidence**: `framings.md` §14 second Excludes bullet —
  "National-cycle framing under-models metro variance. In 2022,
  Austin and Phoenix saw 15–20% price declines while NYC and DC
  were flat-to-positive; the 'we're in a downturn' framing obscures
  the metro-level reality. The framing's reflex 'the cycle says
  wait' can be wrong by 18 months for the asker's specific metro."
- **Trigger**: Asker is using a national-cycle thesis (Calculated
  Risk-style read of national housing-starts / months-of-supply)
  to drive a metro-specific buy-or-wait decision.
- **Failure mode**: Asker waits because "national cycle is rolling
  over"; the asker's specific metro (NYC, DC, parts of New England,
  Midwest small cities) doesn't follow the national cycle and
  prices keep rising; asker pays 18 months of additional rent and
  buys 8% higher.
- **Recovery move**: Look at the metro-specific data, not the
  national series. Local months-of-supply, local price-to-rent,
  local days-on-market trend; cross-reference with metro-specific
  subreddits (r/Seattle, r/Austin, r/RealEstateNYC) for ground-
  truth signal. Metros decouple from the national cycle by 12–24
  months in either direction.

### 14.3 Cycle timing is harder than the framing acknowledges

- **Statement**: Cycle timing is harder than the framing claims.
  "Late expansion" is a label assigned in retrospect; in real-time
  the signal is noisy — Calculated Risk's housing-starts call in
  2021 was directionally correct but 6+ months early, and the
  asker who acted on the call in mid-2021 was waiting through a
  peak that didn't break until late 2022.
- **Source evidence**: `framings.md` §14 third Excludes bullet —
  "Cycle timing is harder than the framing acknowledges. 'Late
  expansion' is a label assigned in retrospect; in real-time the
  signal is noisy — Calculated Risk's housing-starts call in 2021
  was directionally correct but 6+ months early. The framing
  presents cycle calls with more confidence than the underlying
  signal supports."
- **Trigger**: Asker is making a buy-or-wait decision on the basis
  of a single cycle-position call (housing-starts down, months-of-
  supply expanding, MBA mortgage applications declining) without
  modeling timing uncertainty.
- **Failure mode**: Asker waits for the called cycle bottom; the
  bottom is 12+ months later than called; opportunity cost of
  continued rent compounds; asker capitulates and buys at the
  worst time emotionally (frustration-purchase).
- **Recovery move**: Treat cycle calls as Bayesian inputs with
  wide error bars, not point estimates. The right framing is "the
  cycle is unfavorable to buying with X probability over the next
  12 months"; bias toward acting when math works at today's
  fundamentals, not waiting for the perfectly-called bottom.

### 14.4 Secular shifts the cycle framing treats as cyclical noise

- **Statement**: The framing under-weights *secular* shifts the
  cycle framing treats as cyclical noise — work-from-home
  permanently lowered commute-density demand for some metros (SF
  urban core); permanently raised density demand for others (Boise,
  Asheville, Bend); the framing's "cycle reverts" misses durable
  relocation patterns.
- **Source evidence**: `framings.md` §14 fourth Excludes bullet —
  "Under-weights the *secular* shifts the cycle framing treats as
  cyclical noise — work-from-home permanently lowered commute-
  density demand for some metros (SF urban core), permanently
  raised density demand for others (Boise, Asheville); the framing's
  'cycle reverts' misses durable relocation. Opposes F2."
- **Trigger**: Asker is reasoning from a "the cycle will revert
  and SF urban will come back" thesis OR "Boise / Asheville
  prices are a bubble that will break" thesis — both assume
  cyclical reversion of a structural change.
- **Failure mode**: Asker buys SF urban on the cyclical-reversion
  thesis; prices stay 30% below 2019 peak for the full holding
  period; the "wait for revert" never arrived. OR asker passes on
  Boise / Asheville on the bubble thesis; prices stay 50%+ above
  2019 levels through the cycle; the "bubble" was a structural
  reset.
- **Recovery move**: Distinguish between cyclical and structural
  signals. Work-from-home, climate-driven migration, school-
  district-driven migration are structural — they don't revert on
  the cycle clock. Look at the durability evidence (employer
  permanence of remote-work policies, climate-migration sustained
  inflows, school-quality trajectory) before assuming a price
  pattern is cyclical.

### 14.5 Behavioral discipline for "rent and wait" is rarely available

- **Statement**: The framing's "rent and wait" advice for late-
  expansion requires the asker to be a disciplined renter for 18–36
  months — most aren't. The behavioral cost (continued rent
  payments, capitulation-buy at the wrong time, frustration-
  purchase, partner-pressure-to-settle) often exceeds the cycle-
  arbitrage value.
- **Source evidence**: `framings.md` §14 fifth Excludes bullet —
  "The framing's 'rent and wait' advice for late-expansion requires
  the asker to be a disciplined renter for 18–36 months — most
  aren't. The behavioral cost (continued rent payments, capitulation-
  buy at the wrong time, frustration-purchase) often exceeds the
  cycle-arbitrage value. The framing under-weights the asker's
  emotional bandwidth for cycle-disciplined inaction."
- **Trigger**: Asker is committing to "rent and wait for the cycle"
  on an 18+ month horizon AND has a partner with different
  patience or strong stability preferences AND has not seriously
  modeled the capitulation-purchase scenario.
- **Failure mode**: Month 14 of waiting; partner is exhausted;
  asker capitulates at a worse rate / price than the original
  pre-wait market would have offered; the cycle-arbitrage was
  consumed by the behavioral pattern.
- **Recovery move**: Be honest about the asker's behavioral
  bandwidth for cycle-disciplined waiting. If the wait exceeds
  12 months and the household has stability-preferring members,
  the "rent and wait" advice is fragile to the household's actual
  patience. Either commit upfront with explicit milestones (re-
  evaluate at month 12, month 18, month 24) AND a "we buy at
  current math" fallback, OR don't take the rent-and-wait advice
  in the first place.

---

## Cross-framing tensions

These call out where blindspots in one framing are the *recovery move*
of another, mirroring the structure in
[`framings.md` "Opposing-framing pairs"](./framings.md). The pairings
are useful for the Triage / Risk Officer when the asker is clearly
inside one framing — the contrarian framing's blindspot list is often
the right intervention.

- **§1 Financial-return ↔ §2 Lifestyle-flexibility on D1**. F1's
  reflex "the math says rent at price-to-rent > 20" misses F2's
  optionality-asymmetry on exit (§2.5: optionality on the way *out*
  of homeownership is asymmetric); F2's reflex "I might move" misses
  F1's lender's-max-vs-buyer's-comfort delta and the leverage-
  amplifies-immobility shadow (§1.5). When the asker is F1-anchored
  ("the math says rent"), surface §2.1 (commitment-effect goods)
  and §2.4 (externally-imposed moves are the base-rate trigger). When
  the asker is F2-anchored ("I want to stay flexible"), surface §1.1
  (IRR-superiority ignores consumption value of tenure security) and
  §1.5 (leverage-amplifies-immobility is the shadow).

- **§1 Financial-return ↔ §3 Household-stability on D1 / D2**. F1's
  "buy when IRR clears" misses §3.1 (stability can be purchased with
  a long lease, not only with ownership) which is exactly the
  alternative F1 doesn't model. F3's "buy to put down roots" misses
  §1.4 (forced-savings function of amortization is dismissed too
  cleanly) when the household's revealed savings rate is high — the
  forced-savings function isn't binding for that household. Both
  framings need to price both the consumption-value good and the
  IRR cost honestly.

- **§5 Rate-trajectory ↔ §6 Household-cashflow on D4**. F5's "take
  the ARM, refi when rates fall" presumes a refi window opens before
  reset (§5.1: "marry the house, date the rate" assumes a refi
  window that may not open); F6's "take the fixed regardless" misses
  the rate-cycle context entirely. When asker is F5-anchored (ARM
  enthusiast), surface §5.3 (ARM cap structure is the load-bearing
  variable) — most ARM askers haven't extracted the lifetime-cap
  payment. When asker is F6-anchored (fixed-only on cashflow grounds),
  surface §6.5 (15-year-vs-30-year is partly forced-savings) — the
  household-cashflow framing may be over-weighting the wrong axis.

- **§5 Rate-trajectory ↔ §7 Duration-of-stay on D4**. F5 and F7 both
  recommend ARM under different mechanisms (F5: refi before reset;
  F7: sell before reset); both under-price the joint failure when
  neither refi nor sale materializes. §7.3 (ARM-reset joint-failure
  with frozen-market is under-priced) is the synthesis blindspot that
  both framings need surfaced together.

- **§6 Household-cashflow ↔ §10 Investor-leverage on D3**. F6 caps
  front-end DTI at 28% and keeps a 3–6 month PITI reserve; F10
  maximizes leverage to maximize ROE on the down-payment. Same
  numerical question (how much down), opposite reflexes. Surface
  §6.2 (RSU comp is volatile) when the asker is F10-anchored on a
  tech-worker cap-rate underwriting; surface §10.5 (single-property
  concentration risk) when the asker is F6-anchored on cashflow and
  underestimating the cost of trapped equity.

- **§8 Climate-and-insurance ↔ §9 School-and-neighborhood-premium on
  D6**. F8 routes buyers *out* of climate-stressed zones; F9 routes
  buyers *into* school-zoned areas regardless of climate exposure.
  Many top US school districts are in hurricane / wildfire / flood-
  exposed metros — Houston ISD, San Diego Unified, parts of FL.
  When the top school zone is in the climate-risk zone, surface
  §8.3 (property-level mitigation can preserve insurability) — the
  framings can be reconciled if mitigation is in scope. Surface §8.5
  (uninsurable property has no liquidity) when the asker is F9-
  anchored and not pricing exit liquidity in the climate zone.

- **§10 Investor-leverage ↔ §12 Tenant-rights on D9 / D10**. Same
  statute (rent-stabilization, just-cause eviction, warranty of
  habitability) is protective from F12's vantage and constraining
  from F10's. §10.1 (cap-rate ignores rent-stabilization upside-cap)
  and §12.3 (rent-stabilization has complex exit conditions) are the
  cross-framing tensions: the F10 investor needs §12's statutory
  trajectory priced into the cap-rate underwriting; the F12 tenant
  needs §10's investor-perspective understanding to anticipate IAI
  / MCI / decontrol-escalation patterns coming from the landlord
  side. §12.5 (house-hackers straddle both sides) is the explicit
  hybrid case.

- **§11 Transaction-cost-amortization ↔ §14 Macro-housing-cycle on
  D1 / D7**. F11 says buy when you can hold 5+ years regardless of
  macro; F14 says don't buy in late-expansion regardless of intended
  hold. §11.2 (5-year rule fails in turning-market contractions)
  is the synthesis blindspot — the F11 5-year rule isn't sufficient
  in late-expansion-into-contraction scenarios; surface §14.1 (buyers'
  market coincides with credit tightening) when the asker is F14-
  anchored and waiting for a downturn without modeling whether they
  can transact in it.

- **§13 Consumer-advocate ↔ §10 Investor-leverage on D9**. F13's
  "every counterparty is adversarial" applies to owner-occupied
  transactions; for investor-acquisitions the same agent / broker /
  inspector relationships are *repeat* games with multi-transaction
  value, and F13's adversarial-mode reflex burns relationships F10
  wants intact. The framings handle the *same* transaction-counterparty
  correctly in different roles (single-purchase buyer vs portfolio-
  builder).

- **§13 Consumer-advocate ↔ §11 Transaction-cost on D1 / D7**. F11's
  "5–6% commission is the cost" is calibrated to the pre-2024 NAR-
  settlement regime; F13's §13.5 (post-2024 NAR settlement opens
  negotiating room) is the corrective. When asker is F11-anchored
  on round-trip math, surface §13.5 — the regime change reduces the
  round-trip cost meaningfully for askers who negotiate.

---

## Maturity / source-anchor note

This file is `planned` maturity per
[`_meta_ontology.md` §3](../_meta_ontology.md). Source-evidence
lines above currently anchor to:

- `framings.md` Excludes lines (load-bearing — the framing-level
  Excludes were authored specifically to seed Layer 3, per the
  "Notes for downstream layers" section of `framings.md`).
- V1 community-profile bullets that touched housing-adjacent
  topics from `tech-career` adjacency (most relevant:
  `domain_knowledge/tech-career/communities/carta-and-platform-
  data.md` on geographic comp tiers and HCOL-vs-LCOL trade-offs
  that bound F1 / F6 / F14 reasoning). Other V1 community
  profiles touched housing only tangentially (the V1 tech-career
  corpus's housing-adjacency is thinner than its immigration-
  adjacency was for `immigration/blindspots.md`); most source-
  anchors here therefore route to framings.md Excludes lines.
- Conceptual references to the housing-specific community classes
  named in `framings.md` voice anchors (r/RealEstate /
  r/FirstTimeHomeBuyer, BiggerPockets, Bogleheads-housing,
  Mr. Money Mustache / r/financialindependence, Ramit Sethi,
  Calculated Risk / Bill McBride, NAR / NAHB publications, local-
  market subreddits, fee-only CFP / r/personalfinance, First Street
  Foundation / IBHS, state insurance commissioner publications,
  tenant union / Legal Aid landlord-tenant publications, mortgage-
  broker / loan-officer publications, buyer's-agent / real-estate-
  attorney publications including post-2024 NAR settlement coverage).

When `domain_knowledge/housing/sources.yaml` is authored and
`domain_knowledge/housing/communities/*.md` community profiles
land, source-evidence lines above should be tightened to specific
source-view ids. Until then, this file's grounding is the framings-
Excludes seed plus the housing-adjacent V1 community-profile content.

**High-stakes posture per Mechanism E partial-gating**: housing is
`high_stakes: false`, so Recovery moves are NOT uniformly routed to
professional counsel. Recovery moves above flag professional referral
inline only where the decision's tail risk justifies it:

- **Real-estate attorney**: §3.3 (joint-ownership partition / co-
  ownership agreement at unmarried co-buy); §4.4 (HOA reserve study
  in older condo / coastal exposure); §11.3 (refinance with TCJA
  mortgage-interest-deduction implications); §11.5 (buyer-agency
  agreement post-NAR-settlement in attorney-mandatory states);
  §12.1 (tenant-rights enforcement above small-claims threshold or
  retaliation-eviction defense); §12.3 (rent-stabilization regime
  trajectory before underwriting); §12.5 (house-hacker statutory
  obligation review). Title / easement / boundary-line / TOPA-right-
  of-first-refusal issues fall here generally.
- **CPA**: §10.2 (depreciation recapture at sale); §10.3 (real-
  estate-professional status math); §11.3 (lifetime-interest-paid
  delta and TCJA cap interactions on large mortgage refinances).
  §121 exclusion eligibility, 1031 exchange structuring, and
  depreciation-recapture optimization fall here generally.
- **Mortgage broker (fee-only preferred)**: §5.3 (ARM cap-structure
  extraction); §5.5 (lender-credit / relationship / builder-buy-down
  levers); §11.3 (refinance trigger math with amortization-clock-
  reset awareness).
- **Insurance broker + climate-resilience / IBHS-certified
  inspector**: §8.1 (last-resort-insured property in FL / CA / LA);
  §8.3 (property-level mitigation scoping before reject); §8.5
  (non-renewing-market exit-liquidity assessment).
- **Inspector (general + sewer-scope + structural + specialist
  tier)**: §13.4 (inspection-tier specification for property age /
  zone / distress flags); also §4.4 (older condo).

For lower-stakes framings (lease renewal vs move under §2 / §3,
neighborhood selection under §9 absent zone-boundary fragility,
basic refinance arithmetic with clear break-even clearance under §5
/ §11), Recovery moves above are self-directed — no professional-
counsel deferral needed.

**Date-stamp risk**: anchor numbers below carry date-stamp risk
inherited from the underlying market and regulatory corpus. Entries
to re-check before relying on for an active decision:

- §4.3 — Property tax post-purchase reassessment rules (state-level;
  CA Prop 13, FL save-our-homes cap variation, TX uniform-and-equal
  appraisal; check current state-of-play for the specific county).
- §4.4 — HOA reserve-study legislation (FL post-Surfside SB 4-D /
  HB 1021 effective dates; CO HB 23-1233; CA SB 326 balcony
  inspections; check current state-of-play for the specific state).
- §6.1 — DTI conventional-conforming limits (FHFA annual updates,
  jumbo thresholds; check current cycle).
- §8.1 — State insurer-of-last-resort regime details (Citizens FL
  reform trajectory post-2023; CA FAIR Plan exposure-cap reform;
  LA Citizens premium-formula; check current premium tables).
- §10.2 — Depreciation recapture rate and capital-gains brackets
  (federal tax-code stable but state additions vary; check current
  federal rates).
- §10.3 — Real-estate-professional status time tests (IRS guidance
  on 750-hours / >50% tests; passive-loss-limit MAGI phaseout
  thresholds; check current annual update).
- §11.5 / §13.5 — Post-2024 NAR settlement effective date and
  implementation patterns (rolled out late 2024; state-by-state
  implementation variance; check current MLS-level commission-
  publishing rules).

**Mechanism E posture summary**: housing's per-framing inline
referral pattern is the partial-gating shape `_meta_ontology.md`
flagged when it noted housing is "borderline; flagged false because
the user typically also engages an agent and lender." The
`domain_pack.md` (later sub-item) will encode this pattern as
selective referrals rather than the blanket-defer language
`immigration` requires.
