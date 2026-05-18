# housing — decisions.md (Layer 1)

Decision ontology for `housing`. Scope inherits from
[`_meta_ontology.md` §3](../_meta_ontology.md): US-resident knowledge-
worker housing decisions — rent vs buy, lease terms, mortgage selection
(rate type, term, down-payment trade-offs), location choice within a
metro (commute, schools, climate risk), primary-residence vs investment-
property framing. Excludes commercial real estate, multifamily syndicate
investing (deferred to V3+ if a careful source-view set emerges), and
jurisdiction-specific landlord-tenant litigation specifics (overlaps
`legal-disputes`).

The `housing` domain is **high_stakes: false** per `_meta_ontology.md` §3
— large dollar magnitudes but most outcomes are reversible (sell,
refinance, sublet, break the lease with a fee). However, several
decisions below have six-figure tail risks where professional counsel
(buyer's agent, mortgage broker, real-estate attorney, CPA, structural
inspector) should be deferred-to in the framing. The Editor layer should
flag the appropriate referral inline rather than blanket-mandating one
on every decision — over-referral degrades signal. Framing-axes named
below are pointers — full framings will live in `framings.md` (later
artifact).

Cross-domain edges are flagged inline. `personal-finance` overlaps
heavily (down-payment vs invested-difference, mortgage-as-leveraged-
position, property-tax / SALT-cap interactions). `immigration` overlaps
on buy-vs-rent under uncertain status (any decision below where a
status-driven exit is plausible within the break-even horizon).
`family-planning` overlaps on school-district premium and multi-
generational housing for eldercare. `tech-career` overlaps via
employer-stability inputs to mortgage choice (decision 4) and via
relocation-driven sell-and-buy decisions (decision 7). Routing across
edges is V2-Triage's job; the edge annotations here help future
`framings.md` authors name the adjacent domains.

---

## 1. Rent vs buy in current metro on a 5–7 year horizon

- **Scope**: User is currently renting (or relocating into a new metro)
  and is evaluating whether to purchase a primary residence within
  their existing or new location. Decision is the binary buy-vs-rent
  *plus* the implied time horizon — break-even arithmetic depends
  sensitively on holding period. Distinct from decision 7 (sell-and-
  buy when already an owner) and decision 9 (investment property).
- **Framing-axes-covered**: total-cost-of-ownership-vs-rent (PITI +
  HOA + maintenance + opportunity-cost-of-down-payment vs market
  rent), break-even-horizon-and-transaction-cost-amortization (typical
  6–10% round-trip in commission + closing), local-rent-to-price-ratio
  (price-to-rent above ~20 favors renting absent strong appreciation
  thesis), employment-stability-and-relocation-probability (boundary
  `tech-career`), mortgage-interest-and-SALT-deduction-after-2017-cap
  (boundary `personal-finance`).
- **Sample situations**:
  - "Renting a $4,200/mo 2BR in Seattle; could buy a comparable
    townhome at $850k with 20% down at 6.75%. Stay renting or buy?"
  - "Relocating to Austin for a 4-year role; tempted to buy given
    'throwing money away on rent' framing — does the math actually
    work at this horizon?"

## 2. Lease length and renewal-vs-move decision

- **Scope**: Existing renter at a lease boundary (typically 30–60 days
  before expiry) facing a renewal offer with a rent change, OR a
  prospective renter choosing between 6/12/18/24-month lease terms at
  initial signing. Includes the related sub-decision of whether to
  negotiate the renewal, accept, or move. Distinct from decision 1 —
  here the user is staying in the rental market.
- **Framing-axes-covered**: rent-trajectory-and-renewal-anchor-vs-
  market-comp, moving-cost-amortization-vs-rent-savings (typical
  $2–5k all-in moving + deposit shuffle), lease-length-vs-flexibility-
  premium (longer leases price lower in soft markets, higher in tight
  ones), rent-control / stabilization-rules-by-jurisdiction (NYC,
  SF, LA, Oregon statewide cap, etc.), early-termination-clause-and-
  buy-out-options, security-deposit-recoverability-and-state-law
  (boundary `legal-disputes`).
- **Sample situations**:
  - "Current $2,800 rent; landlord offers renewal at $3,150 (+12.5%);
    similar units listed at $2,950 — negotiate, accept, or move?"
  - "First lease in a new city; landlord offering 12 or 18 months at
    same rate; job is uncertain past month 9 — which term?"

## 3. Down-payment size — 20% vs 5/10/15% vs all-cash

- **Scope**: Buyer with sufficient liquid net worth to choose among
  multiple down-payment levels (typically 5%, 10%, 15%, 20%, 25%+, and
  all-cash on the high end). Decision spans PMI mechanics, the
  opportunity-cost of the difference invested elsewhere, and the
  signal value of a larger down to win competitive offers. Distinct
  from decision 4 (rate-type choice) and decision 11 (refi later).
- **Framing-axes-covered**: PMI-cost-and-cancellation-mechanics-at-
  80%-LTV (auto-cancel at 78%, can request at 80%), conventional-vs-
  FHA-vs-VA-vs-jumbo-thresholds, opportunity-cost-of-down-payment-
  invested-at-market-return (boundary `personal-finance` — equity-
  risk-premium vs mortgage rate), competitive-offer-strength-and-
  appraisal-gap-coverage, liquidity-reserve-post-close (3–6 months
  PITI is a typical floor), QSBS / brokerage-margin-as-alternate-
  liquidity-sources before depleting cash.
- **Sample situations**:
  - "Approved for $900k; have $400k liquid; should I put 20% down
    ($180k), 30% down, or all-cash and refi out?"
  - "Hot market with 8 competing offers; agent suggests bumping from
    10% to 25% down to win — is that signal worth the lost liquidity?"

## 4. Fixed-rate vs ARM (5/1, 7/1, 10/1) vs interest-only

- **Scope**: Buyer who has committed to financing and is choosing among
  rate structures: 30-year fixed, 15-year fixed, ARMs of various
  initial-fixed periods, and (for jumbo borrowers) interest-only loans.
  Decision is anchored by expected holding period, rate-direction
  outlook, and tolerance for payment variance after the initial period.
  Distinct from decision 3 (down-payment sizing) and decision 11
  (refi-trigger logic).
- **Framing-axes-covered**: expected-holding-period-vs-ARM-reset-
  horizon (5/1 makes sense if expected to sell or refi by year 5),
  rate-spread-between-30yr-fixed-and-ARM-initial (typically 50–100bp
  but compresses in flat curves), index-and-margin-and-cap-structure-
  on-ARM (most have 2/2/5 caps; verify), refi-as-implicit-put-option-
  on-fixed (free embedded option if rates fall, you keep your rate if
  they rise), payment-shock-tolerance-and-household-cashflow-buffer,
  prepayment-penalty-by-state-and-loan-type, 15-year-vs-30-year-as-
  forced-savings-vs-opportunity-cost (boundary `personal-finance`).
- **Sample situations**:
  - "30-year fixed at 6.75% vs 7/1 ARM at 5.875%; we expect to move in
    5–6 years for kids' schools. Which?"
  - "Jumbo loan; bank pitched interest-only for 10 years to maximize
    cashflow — what's the catch?"

## 5. Property type — SFR vs condo vs townhouse vs co-op

- **Scope**: Buyer deciding among property-type categories within a
  metro at a given budget. The decision is rarely "all four on the
  table"; usually it's SFR-vs-condo (suburban metros) or condo-vs-
  co-op (NYC, parts of DC). Distinct from decision 6 (location within
  metro) — here the question is *what kind of structure*, not *where*.
- **Framing-axes-covered**: HOA-cost-and-reserve-study-quality (well-
  funded reserves vs special-assessment risk; recent CO/FL condo
  reforms post-Surfside drive special assessments), shared-wall-and-
  insurance-master-policy-mechanics, co-op-board-approval-and-
  financial-disclosure (NYC: board interview, 20–50% post-close
  liquidity asks), warrantability-of-condo-for-conforming-loans
  (Fannie/Freddie warrantability blocks affect financeability and
  resale), land-vs-improvement-value-and-appreciation-asymmetry (SFR
  land tends to appreciate; structure depreciates), insurance-and-
  climate-risk-by-type (condos in older buildings carry
  loss-assessment risk).
- **Sample situations**:
  - "Same price point: $700k 1,400sqft condo with $850/mo HOA, or
    $700k SFR 1,600sqft 30min further out with no HOA. Long-term?"
  - "NYC co-op asking 25% down + 2 years post-close liquidity vs
    condo at 10% down — co-op is $300k cheaper but harder to resell."

## 6. Location choice within metro — commute / schools / climate-risk

- **Scope**: Buyer (or renter committing to a longer lease) selecting
  between neighborhoods or sub-markets within their chosen metro.
  Decision compresses commute-time, school-district premium, climate-
  risk trajectory, walkability/transit access, and gentrification or
  neighborhood-trajectory bets. Cross-routes `family-planning`
  (school district premium can be 15–30% of price) and on the climate
  axis, increasingly `personal-finance` (insurance availability and
  premium trajectory).
- **Framing-axes-covered**: school-district-premium-and-test-score-
  vs-actual-outcomes-research (much of premium is sorting; effects
  attenuate after controlling for peer composition), commute-time-
  and-utility-vs-time-budget (research: long commute is the strongest
  inverse-correlate of life satisfaction), climate-risk-trajectory-
  by-peril-and-region (wildfire-urban-interface in CA / OR / CO;
  hurricane storm-surge along Gulf and SE coast; inland-flood
  reassessment after Helene-style events; insurance-market-pullback
  in FL/CA), walkability-and-transit-vs-car-dependency-cost,
  gentrification-trajectory-and-displacement-ethics (the framing axis,
  not the moral verdict), boundary-effects-of-school-attendance-
  zones-being-redrawn (low-likelihood high-impact).
- **Sample situations**:
  - "Two houses, same price: $1.1M in a top-10 school district 40min
    commute, or $1.1M in a so-so district 12min commute. Family of 4
    with a 2yr-old."
  - "Boulder vs Longmont: $1.4M in Boulder near wildfire-urban-
    interface, insurance non-renewals starting; $950k in Longmont
    with no insurance pressure. How to price the climate delta?"

## 7. Sell current home before buying next vs bridge vs contingent offer

- **Scope**: Current homeowner who wants to move (job relocation,
  family change, upgrade). Decision is the sequencing of sell and buy:
  (a) sell first, rent temporarily, then buy; (b) buy first with a
  bridge loan or HELOC against current equity; (c) make a contingent
  offer on the new home subject to selling the current one. Each
  has distinct timing risk, cost, and offer-strength implications.
  Cross-routes `tech-career` when triggered by relocation; cross-
  routes `personal-finance` when bridge loans interact with
  cash-flow management.
- **Framing-axes-covered**: market-direction-and-sell-first-vs-buy-
  first-risk-asymmetry (rising market: sell-first risks pricing
  yourself out; falling market: buy-first risks double carry),
  bridge-loan-cost-and-eligibility (typically 8–12% APR, 6–12 month
  term, equity-secured), HELOC-as-bridge-alternative (cheaper but
  requires originating before listing), contingent-offer-strength-
  by-market (often non-competitive in hot markets), double-mortgage-
  carrying-cost-tolerance-and-reserves, capital-gains-exclusion-
  timing ($250k single / $500k MFJ, ownership-and-use-test 2-of-5;
  boundary `personal-finance` — CPA referral warranted if approaching
  the exclusion cap or factoring in depreciation recapture from
  prior rental conversion).
- **Sample situations**:
  - "Current home worth $950k, mortgage $400k; buying $1.4M next.
    Market is balanced; can carry both mortgages for 4 months. Sell
    first or buy first with bridge?"
  - "Relocation for work; company offers a guaranteed-buyout program
    at appraised value − 3%. Take it, or list and try to beat it?"

## 8. Refinance trigger — rate-and-cost vs cash-out vs no-cost refi

- **Scope**: Current homeowner with an existing mortgage evaluating
  whether (and how) to refinance. Three sub-decisions: (a) rate-and-
  term refi to lower the rate, (b) cash-out refi to extract equity
  for other purposes, (c) no-cost refi where lender credits
  offset closing costs in exchange for a rate bump. The break-even
  calculus differs across all three. Distinct from decision 4 (initial
  rate-type choice).
- **Framing-axes-covered**: rate-delta-and-break-even-months
  (closing-cost / monthly-savings rule of thumb; valid only when
  remaining term ≥ break-even), reset-of-amortization-clock-on-
  30-year-refi (refinancing from year 7 of 30 back to a new 30
  re-extends the loan; recasting or 23-year custom term preserves
  payoff date), cash-out-LTV-cap-and-rate-premium (typically capped
  at 80% LTV with 25–50bp rate add), no-cost-refi-as-implicit-
  hedge (worth the rate bump if rates likely to fall again; not if
  you'll hold the loan to term), tax-treatment-of-cash-out-use
  (interest deductible only for home-improvement use after TCJA;
  boundary `personal-finance`), prepayment-penalty-and-PMI-recapture-
  on-current-loan.
- **Sample situations**:
  - "Mortgage at 7.25% from 2024; rates now 5.875%; loan balance
    $620k, closing costs would be $9k. Break-even? Do it now or
    wait?"
  - "Have $200k equity I want to extract for a kitchen reno —
    cash-out refi or HELOC?"

## 9. Buy investment property vs invest in market index

- **Scope**: User with sufficient capital to make a 20–30% down
  payment on a rental property is evaluating that purchase against
  putting the equivalent capital in a broad-market index fund. This
  is the framing-comparison decision, not the property-selection
  decision once committed. Cross-routes `personal-finance` heavily
  (leverage, tax treatment, time-cost-of-management).
- **Framing-axes-covered**: cap-rate-vs-cost-of-leverage-and-positive-
  vs-negative-leverage, cash-on-cash-return-with-and-without-
  appreciation, depreciation-and-passive-loss-rules-and-real-estate-
  professional-status (boundary `personal-finance` — CPA warranted
  before committing), 1031-exchange-mechanics-for-future-trade-up,
  property-management-cost-vs-self-management-time (10% of rent typical),
  vacancy-and-CapEx-reserves (5–10% combined floor), single-asset-
  concentration-risk-vs-REIT-or-syndication-diversification, local-
  rent-regulation-and-eviction-process-by-state (boundary `legal-
  disputes` — pro-tenant jurisdictions can cap returns).
- **Sample situations**:
  - "$200k available to invest: down-payment on a $700k rental
    expected to clear $200/mo positive cashflow, or VTSAX. Long-term?"
  - "Inherited $300k; partner wants to buy a duplex and house-hack
    one side; I want to put it in the market. How to compare?"

## 10. House-hacking and accessory-dwelling-unit (ADU) decisions

- **Scope**: Buyer or current owner evaluating multifamily-as-primary-
  residence strategies: (a) buy a 2–4 unit property and live in one
  unit (FHA / conventional owner-occupied financing); (b) add an
  ADU to an existing SFR for rental income or eldercare housing;
  (c) rent out rooms in a primary residence. Each combines tax,
  zoning, and lifestyle considerations. Distinct from decision 9 —
  here the property is *primary residence* with rental upside.
  Cross-routes `family-planning` for the eldercare-ADU sub-case.
- **Framing-axes-covered**: FHA-3.5%-down-on-2-to-4-unit-owner-
  occupied-rules-and-self-sufficiency-test, ADU-zoning-and-permit-
  process-by-jurisdiction (CA-statewide-by-right since SB-9; many
  metros still highly restrictive), construction-cost-vs-rent-
  recovery-payback-period (15–25 year typical), conversion-of-
  primary-to-rental-and-§121-exclusion-clock-implications (boundary
  `personal-finance`), insurance-and-liability-as-landlord-while-
  living-on-site, eldercare-ADU-vs-assisted-living-tradeoff (boundary
  `family-planning`), neighborhood-relations-and-short-term-rental-
  restrictions (HOA, city ordinances).
- **Sample situations**:
  - "Looking at a $1.1M duplex; live in one unit, rent the other at
    $2,400/mo. FHA owner-occupied gets us in at 3.5% down. Worth the
    landlord overhead?"
  - "SFR with a 600sqft detached garage; convert to ADU for $180k all-
    in to rent at $2,200/mo OR house aging parent. Different
    calculus?"

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the axes
  above cluster into ~8–10 reusable framings — break-even-and-holding-
  period, total-cost-of-ownership-vs-rent, opportunity-cost-of-down-
  payment, rate-structure-as-embedded-options, leverage-and-cap-rate-
  arithmetic, climate-and-insurance-risk-trajectory, school-district-
  premium-vs-realized-outcome, transaction-cost-amortization, capital-
  gains-exclusion-clock, owner-occupied-vs-investor-tax-treatment.
- **Blindspot anchors** (forward-pointer to `blindspots.md`): decisions
  1, 3, 6, 8, 9 are highest-density — break-even horizons under
  transaction costs (1), opportunity cost of large down payments (3),
  climate-risk pricing and insurance-market pullback (6), refi
  break-even with amortization-clock-reset hidden cost (8), and
  cap-rate-with-leverage-vs-index-fund false equivalence (9) are
  frequently miscalibrated even among financially literate buyers.
  Decision 7's capital-gains-exclusion clock has the highest single-
  dollar tail risk per mis-step.
- **Cross-domain edges**: 1, 4, 7 boundary `tech-career` (employer
  stability and relocation probability shape mortgage structure and
  sell-buy sequencing); 3, 4, 7, 8, 9, 10 boundary `personal-finance`
  (opportunity-cost-of-cash, mortgage-as-tax-leveraged-position,
  capital-gains-exclusion, depreciation recapture, SALT cap);
  1 boundary `immigration` (status-driven exit within break-even
  horizon makes buying worse-than-default); 6, 10 boundary
  `family-planning` (school-district premium framing, eldercare-ADU
  alternative to assisted living); 2, 9 boundary `legal-disputes`
  (security-deposit recovery, tenant-friendly eviction regimes).
  Edges are documentation; routing is V2-Triage's job.
- **High-stakes posture** (selective): `housing` as a whole is
  `high_stakes: false` per `_meta_ontology.md` §3 — most outcomes are
  reversible. The Editor layer should NOT blanket-defer every decision
  to a professional. Selective referral is warranted for: decision 7
  (capital-gains-exclusion math near caps, or depreciation recapture
  from prior rental conversion — CPA), decision 8 (cash-out interest
  deductibility — CPA), decision 9 (real-estate-professional status
  and passive-loss limitations — CPA), any decision involving a real-
  estate-attorney-mandatory state (NY, NJ, MA, parts of the South),
  and any decision where a structural / pest / sewer inspection
  finding would change the offer (inspector + buyer's agent). When in
  doubt, name the professional category in the framing rather than
  the binding decision.
