# tech-career — decisions.md (Layer 1)

Decision ontology for `tech-career`. Scope inherits from
[`_meta_ontology.md` §1](../_meta_ontology.md): US knowledge-worker comp,
equity, offer negotiation, perf reviews, layoff response, intra-industry
job changes. Cross-industry pivots belong to `career-pivots`; status-
dependent moves to `immigration`; tax-filing mechanics to
`personal-finance`. Framing-axes named below are pointers — full
framings will live in `framings.md` (later artifact).

---

## 1. Compare structurally-different offers across stages

- **Scope**: User holds ≥ 2 offers whose packages differ in composition
  (base-heavy vs RSU-heavy vs ISO-heavy), risk class (public vs late-
  private vs early), or vesting curve. Distinct from decision 8
  (refresher negotiation at an existing employer).
- **Framing-axes-covered**: expected-value-vs-risk-adjusted-EV,
  liquidity-horizon, dilution-and-strike-trajectory, team-and-learning
  optionality, tax-treatment-asymmetry (RSU at vest vs ISO at exercise).
- **Sample situations**:
  - "Public co offered $250k base + $400k RSUs / 4yr; current employer
    countered $310k base + smaller RSU grant." (fixture
    `late-stage-rsu-vs-base`)
  - "Offers from a FAANG, a Series C, and a Series A — packages
    structured very differently." (fixture `comparing-offers-3-companies`)

## 2. Accept early-stage offer where below-market cash is paid for in equity

- **Scope**: Single-offer decision at seed-to-Series-B where the equity
  component is the load-bearing argument for accepting and the user
  must price both dilution and survival probability. Distinct from
  decision 1 — here the counterfactual is "take it or pass," not "rank."
- **Framing-axes-covered**: expected-value-under-survival-curve,
  strike-vs-FMV-and-cliff-risk, team-quality-as-an-asymmetric-bet,
  opportunity-cost-of-the-next-12-months.
- **Sample situations**:
  - "Series B offer with 0.1% in ISOs over 4yr / 1yr cliff; comp below
    market but team is exceptional." (fixture `series-b-iso-cliff`)
  - "First offer out of school: $180k base + 0.05% equity at seed —
    I don't understand the equity part." (fixture
    `first-job-equity-confusion`)

## 3. ISO exercise timing pre-IPO under AMT exposure

- **Scope**: User holds vested ISOs with FMV materially above strike at
  a still-private company. Decision is *when* (and how much) to
  exercise — exercise-on-leave and exercise-during-tender are sub-cases.
  Excludes RSUs (no exercise step) and fully-public scenarios.
- **Framing-axes-covered**: AMT-exposure-in-exercise-year,
  cash-outlay-and-liquidity-reserve, ordinary-income-clock-and-LTCG,
  company-survival-and-strike-recovery, the 90-day-PTE-window if
  leaving.
- **Sample situations**:
  - "ISOs deeply ITM — FMV is 10x strike. No IPO planned for ≥ 2yr.
    Exercise now?" (fixture `amt-exercise-decision`)
  - "Joined 5 weeks ago; they mentioned an 83(b) election; the
    deadline is 30 days from grant — did I miss it?" (fixture
    `83b-deadline-missed`)

## 4. Stay-through-cliff vs leave-with-partial-vest

- **Scope**: User is partway through a vesting cliff (typically the
  first 12 months) and is weighing the value of vested equity at the
  cliff against the cost (in dollars, optionality, and burnout) of
  staying that long. Distinct from decision 6 (full-cliff golden-
  handcuffs at refresher boundary) — here no equity is yet vested.
- **Framing-axes-covered**: vesting-value-vs-time-cost,
  competing-offer-clock-and-rescindability, employer-counter-and-
  retention-grant-mechanics, signal-to-future-employers.
- **Sample situations**:
  - "10 months in at Series A; want to leave for a competing Series B
    offer — wait 2 months for the cliff?" (fixture `pre-cliff-quit-dilemma`)

## 5. Severance + release negotiation post-layoff

- **Scope**: User has been laid off with a severance offer bundling
  non-compete, waiver of unvested equity, confidentiality, and release-
  of-claims clauses. Decision spans whether to sign, what to push back
  on, and what the signing deadline hides. Excludes unemployment-
  insurance filing mechanics.
- **Framing-axes-covered**: non-compete-enforceability-by-state,
  release-waiver-and-known-claims, unvested-equity-as-bargaining-chip,
  signing-deadline-as-pressure-tactic, reference-and-rehire-eligibility.
- **Sample situations**:
  - "Laid off after 3yr at Series D; 8 weeks severance, 12-month
    non-compete, waiver of ~$180k unvested RSUs, 7 days to sign — can
    I push back?" (fixture `layoff-severance-negotiation`)

## 6. Stay-vs-leave when unvested equity is high (golden handcuffs)

- **Scope**: Employed at a public or late-private company with material
  unvested grant remaining; recruited externally with arguably better
  role or comp. Decision compares forfeited unvested equity (and any
  trailing vest) against the new opportunity, with retention-grant
  counters as a side branch. Distinct from decision 4 (pre-first-cliff).
- **Framing-axes-covered**: unvested-forfeiture-vs-sign-on-replacement,
  retention-grant-mechanics-and-counter-strategy, growth-and-learning-
  delta, concentration-risk-in-employer-stock, post-vest-cliff-of-the-
  new-grant.
- **Sample situations**:
  - "Vested half my FAANG grant; competitor recruiting; unvested
    ~$400k. Stay or go?" (fixture `golden-handcuffs-eval`)

## 7. PIP-accept-vs-managed-exit

- **Scope**: User just received a PIP (or is about to). Decision is
  whether to accept and fight through, or negotiate a managed exit now.
  Often time-coupled to an upcoming vesting event. Distinct from
  decision 5 — here the user has agency on the front side.
- **Framing-axes-covered**: vesting-forfeiture-if-terminated-vs-
  preserved-if-exited, success-rate-of-PIPs-empirically, reference-and-
  future-employer-signal, severance-leverage-while-still-employed,
  burnout-and-time-cost-of-fighting.
- **Sample situations**:
  - "60-day PIP yesterday; RSU cliff in 4 months (~$220k); HR hinted
    at 'negotiate a transition' — accept PIP and fight, or take
    managed exit?" (fixture `pip-accept-vs-exit`)

## 8. Refresher-grant negotiation mid-tenure

- **Scope**: Employed user with most of their initial grant vested or
  near-vested; the question is how (and when) to surface a refresher
  request without weakening their position. Excludes new-hire
  negotiation (decisions 1 and 2) and severance contexts (decision 5).
- **Framing-axes-covered**: timing-relative-to-perf-cycle, market-comp-
  data-as-anchor, internal-vs-external-leverage-and-the-cost-of-
  walking-warm, refresher-shape (one-time-vs-multi-year-stacking).
- **Sample situations**:
  - "2.5 years in; initial grant mostly vested — how do I bring up a
    refresher without sounding ungrateful?" (fixture
    `refresher-grant-negotiation`)

## 9. Pre-IPO secondary / tender-offer participation

- **Scope**: User holds vested shares in a late-stage private company
  that is offering a structured tender for a fixed % of vested holdings
  at a discount to the last round. Decision is whether (and how much)
  to participate. Distinct from decision 3 (exercise timing on
  unexercised ISOs) — here the shares are already exercised/vested
  RSU-equivalents.
- **Framing-axes-covered**: concentration-risk-vs-IPO-upside, discount-
  to-last-round-and-tax-treatment, IPO-timeline-credibility, signal-
  to-future-acquirer-and-internal-perception, LTCG-clock-and-QSBS-eligibility.
- **Sample situations**:
  - "Pre-IPO at ~$4B last round; ~80% of net worth in vested shares;
    tender lets me sell up to 25% at 10% discount; IPO '1–2 years
    out.' Sell the full 25% or hold?" (fixture `pre-ipo-tender-offer`)
  - "IPO filing in 3 months; secondary available at the last private
    valuation — worth taking some liquidity?" (fixture
    `ipo-secondary-decision`)

## 10. Acquihire / acquisition equity terms

- **Scope**: Employer is being acquired and the buyer proposes new-grant
  terms (re-vest schedule, acceleration triggers, retention bonuses)
  alongside or replacing remaining unvested equity. Decision spans
  accepting the package, negotiating individual clauses, and evaluating
  leave-with-payout alternatives. Excludes founder-side acqui-hire
  negotiation from the cap-table seat (overlaps `entrepreneurship`).
- **Framing-axes-covered**: single-trigger-vs-double-trigger-
  acceleration, re-vest-schedule-and-credit-for-prior-tenure,
  retention-bonus-vs-equity-conversion, change-of-control-cliff-on-
  unvested, buyer-employer-fit-and-non-comparable-role.
- **Sample situations**:
  - "Startup acquired; buyer wants me to re-vest over 4yr with
    double-trigger acceleration. Is this normal?" (fixture
    `acquihire-double-trigger`)

## 11. Founder / co-founder equity split with vesting structure

- **Scope**: Pre-incorporation or just-incorporated co-founder pair
  setting initial equity allocation and vesting schedule. Distinct
  from the rest of this domain (which is employee-side) because the
  user is on the cap-table seat. Co-located here rather than under
  `entrepreneurship` because the framings overlap heavily with
  employee-side equity decisions (4, 6).
- **Framing-axes-covered**: contribution-asymmetry-and-time-zero-vs-
  forward-work, vesting-and-acceleration-as-trust-mechanism, dilution-
  math-across-future-rounds, exit-and-removal-clauses, idea-vs-
  execution-weighting.
- **Sample situations**:
  - "Co-founder wants 50/50; I had the idea, am doing most of the
    early work, brought in the first investor — how should I think?"
    (fixture `founder-equity-cofounder`)

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the axes
  above cluster into ~6–8 reusable framings — AMT-minimization,
  liquidity-preservation, concentration-risk, retention-leverage,
  severance-leverage, dilution-math, cliff-arithmetic, contribution-
  asymmetry.
- **Blindspot anchors** (forward-pointer to `blindspots.md`): decisions
  3, 5, 7, 9 are highest-density — AMT mechanics, non-compete
  enforceability, PIP success rates, and tender-offer tax treatment are
  all frequently miscalibrated even among insiders.
- **Cross-domain edges**: 3 and 9 boundary `personal-finance` (tax-
  account-ordering, LTCG); 5 and 7 boundary `legal-disputes` (release-
  waivers, retaliation claims); 11 boundaries `entrepreneurship` (cap-
  table modeling). Edges are documentation; routing is V2-Triage's job.
