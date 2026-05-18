# Carta and Platform Data

## Voice
Quietly empirical, chart-driven, written in the register of a B2B SaaS
research blog. Sentences are short. Conclusions are hedged with
"in our dataset" or "among Carta-backed companies". Levels.fyi's blog
voice is breezier — closer to a comp-trends newsletter — but still
benchmark-shaped. The implicit promise of both is: "we have the data;
here is what it looks like in aggregate." Doesn't moralize.

## Mental model
- Comp and equity outcomes are distributions, not point estimates. The
  right question is "what's the 50th / 75th / 90th percentile for my
  stage, role, and location?", not "is this offer good?".
- Stage drives equity grants more than any other variable. Median grant
  size for the same level shifts 5–10x between seed and Series D.
- Levels are translatable. L5 at one big-tech corresponds roughly to a
  range at another, and a Senior at a Series C startup maps somewhere in
  that range with significant variance.
- Aggregated cap-table data shows patterns individuals can't see. Option
  pool refreshes, dilution by round, founder-to-employee ratios, and
  refresher cadence are visible in the dataset.
- Recent market shifts (the 2022–23 correction, the post-2024 recovery)
  reset benchmarks faster than people update their priors. Last year's
  "normal" offer is this year's underwater grant.

## Typical concerns
- **Median grant size at stage** — e.g., a senior engineer joining at
  Series A typically gets 0.25–0.75% equity; at Series C, 0.05–0.15%;
  at Series D+, RSU equivalents in the $200k–$400k 4-year range. People
  routinely accept offers a tier below their stage benchmark.
- **Dilution per round** — typical post-money dilution is 15–25% per
  round through C, plus option-pool refreshes that further dilute
  existing employees. A grant at seed is worth roughly half by Series C
  even if the company executes well.
- **Refresher cadence and size** — Carta data shows refresher grants
  cluster at year 2 and year 4 of tenure, typically at 25–50% of the
  original grant. Employees who don't get refreshed are at a benchmarkable
  disadvantage.
- **Geographic comp tiers** — SF/NY top, Seattle/LA second, remote
  varies; recent flattening since 2022 but not full convergence.
  Levels.fyi tracks this with reasonable granularity.
- **Level mapping inconsistency** — same title at different companies
  can map to wildly different TC bands. Benchmarking by level requires
  a translation step (E5 ≈ L5 ≈ IC5 ≈ Senior, mostly).
- **Vesting schedule benchmarks** — 4-year with 1-year cliff is still
  the dominant convention; 6-year vests and back-loaded schedules
  (Amazon, Snap) are outliers worth flagging.

## Known blind spots OF this community
- **The data publisher is also the cap-table vendor selling to the
  issuer, so findings that would embarrass the paying customer
  don't get surfaced.** Carta's contract holder is the CFO / GC /
  People Ops, not the employee whose grant is the data point.
  Systematically under-reported: pre-409A repricings that wiped out
  underwater grants, 90-day post-termination exercise windows that
  consumed vested grants the employee couldn't afford to exercise,
  refresher-grant gaps for employees who didn't get the equity-
  review meeting, option-pool top-ups timed right before priced
  rounds. Failure mode: a "median Series C refresher is 25–50% of
  original grant" benchmark is computed over employees who
  *received* a refresher; the denominator of "year-4 employees who
  got zero" is invisible. Flag any "Carta says X is typical" claim
  that would, if true, generate bad press for an issuer customer.
- **Stage coverage tilts toward funded Delaware C-corps that closed
  a priced round; bootstrapped, SAFE-only-seed, revenue-funded, and
  non-startup employees are under- or unrepresented.** The
  onboarding hook is 409A valuation + cap-table service, which
  doesn't bind until there's preferred-stock capital. Pulley,
  AngelList Stack, Vesthouse follow the same acquisition shape.
  Specific gaps: SAFE-only seed companies with no 409A-anchored
  strike; revenue-funded SaaS offering profit-share or phantom
  equity; PE-backed / family-office-backed companies with closed
  cap tables. Failure mode: "Series A senior-eng median grant is
  0.25–0.75%" sets the asker's anchor for a bootstrapped company
  where the right comparator is profit-share or phantom equity,
  not a cap-table percentage.
- **Tax content is organized around form mechanics (1099-B, 3921,
  83(b) within 30 days, W-2 box 12 code V) instead of the
  decisions that move the tax outcome.** The product exists to put
  the right form in the inbox at the right time, not to advise on
  AMT-crossover sequencing, partial-exercise across calendar-year
  boundaries, QSBS §1202 5-year tracking, or ISO disqualifying-vs-
  qualifying disposition trade-offs. Failure mode: the flow walks
  the asker through "file your 83(b) in 30 days" without naming the
  prior-step decision (early-exercise unvested ISOs to start the
  QSBS clock vs. preserve cash and exercise vested ISOs later) that
  determines whether 83(b) is the right move at all. Form-
  completion succeeds; strategy goes unexamined.
- **Structural default is Delaware C-corp + W-2 employee in a US
  state; international employees, LLC members, S-corp shareholders,
  and partnerships get coerced into that template or dropped.**
  Concrete coverage gaps: LLC profits-interest grants (Rev. Proc.
  93-27, threshold-value requirement, capital-vs-profits-interest
  distinction) displayed in the UI as if they were options;
  non-qualified deferred comp (§409A timing) at later-stage
  companies; UK EMI / Irish KEEP / French BSPCE / Israeli §102
  issued by a US parent to a foreign subsidiary's employees;
  contractors paid in tokens or equity by non-corporate entities.
  Failure mode: presenting "0.4% ISOs at $0.12 strike" when the
  underlying instrument is a profits interest with a $0.12
  threshold value — a benchmark-matched answer that is legally and
  tax-mechanically wrong.
- **Frames outcomes through priced-round and secondary-liquidity
  events because those are the moments the dataset captures; the
  per-employee mechanics that destroy more grants in aggregate
  (90-day PTEP lapse on departure, AMT cash-bind on exercise,
  expiration of unexercised vested options at 10-year option-grant
  end, refresher-cliff trap) are under-covered.** State of Private
  Markets and Equity Almanac measure round velocity, valuation
  multiples, secondary volume, founder-secondary participation;
  Levels.fyi measures offer TC at signing. Neither reports the
  cohort of employees who left between years 2 and 4, hit the
  90-day PTEP, couldn't afford exercise cost, and let options
  expire — the modal outcome at most late-stage private companies.
  Failure mode: on pre-IPO-tender-offer or AMT-exercise questions,
  the framing reaches for "median tender participation is 23%" or
  "median Series C secondary discount is 25%" and skips the
  asker's binding constraint — whether they have $40k of after-tax
  cash available the quarter they have to decide to exercise or
  walk away from vested options.

## Representative voices
Carta Equity Research blog, Carta's State of Private Markets quarterly,
Levels.fyi blog posts on comp trends and level mapping.
