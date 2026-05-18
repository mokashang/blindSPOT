# entrepreneurship — decisions.md (Layer 1)

Decision ontology for `entrepreneurship`. Scope inherits from
[`_meta_ontology.md` §6](../_meta_ontology.md): US-resident knowledge-
worker entrepreneurship decisions — founding, co-founder selection and
equity structuring, fundraising vs bootstrapping, side-business vs
full-time leap, freelance / consulting structure (sole-prop / LLC /
S-corp / C-corp), early-employee-vs-contractor classification, pricing-
model selection, and founder-departure / dispute resolution. Excludes
deep entity-tax optimization (overlaps `personal-finance` on QBI
Section-199A, QSBS Section-1202, retirement-vehicle selection for
self-employed), domain-specific legal litigation procedure (overlaps
`legal-disputes` on founder lawsuits, IP-assignment disputes, equity
disputes), and visa-tied entrepreneurship constraints (overlaps
`immigration` on E-2 / O-1 / EB-5 / founder-on-H-1B mechanics).

The `entrepreneurship` domain is **high_stakes: false** per
`_meta_ontology.md` §6 — failure is the modal outcome (75-90% of
startups fail per the standard CB Insights / Statistic Brain
distributions) and is generally survivable for a knowledge-worker
founder who retained a credible day-job-return path. The dollar swings
are large but the irreversibility profile is fundamentally different
from `health-insurance` (12-month plan lock-ins, Medicare late-
enrollment permanent penalties) or `immigration` (out-of-status
multi-year bans, missed filing windows) — most entrepreneurship-domain
errors compress to "lost 12-36 months of opportunity cost plus
moderate-to-large dollar loss", which is recoverable on a typical
30-year career horizon. Therefore the Editor posture is
**decision-support framing rather than uniform Mechanism E deferral**:
the user is treated as a decision-capable adult navigating an
inherently uncertain domain, and the system surfaces the framings the
founder community would name. The exceptions where six-figure tail
risk justifies professional referral are enumerated below — they are
**selective, not blanket**.

Selective referral categories (keyed by decision, not blanket-applied):

- **Startup / corporate attorney with founder-side experience** (NOT
  generic small-business lawyer; the distinction matters because
  founder-side attorneys have seen the recurring patterns in vesting,
  IP-assignment, SAFE-to-priced-seed conversions, drag-along /
  tag-along provisions, and Delaware-C-corp formation; firms like
  Cooley / Gunderson / WSGR / Orrick / Fenwick at the high end,
  Clerky / Stripe Atlas / Atomic / Mintz at the more accessible end).
  Warranted for decision 1 (co-founder equity + vesting structure),
  decision 5 (SAFE post-money vs priced seed), decision 11 (co-
  founder departure / cap-table buyback), and any decision involving
  IP-assignment carve-outs from a prior W-2 employer.
- **Tax attorney or CPA with S-corp / multi-entity / startup
  experience** (NOT a generic 1040-prep CPA — the relevant
  qualifications are S-corp election history, multi-state nexus
  experience, QBI Section-199A planning, accountable-plan setup,
  reasonable-salary analysis with industry-comp data). Warranted for
  decision 4 (LLC pass-through vs S-corp election), decision 8
  (solo-401(k) vs SEP-IRA vs SIMPLE retirement vehicle), decision 7
  (first-employee vs contractor — payroll-tax mechanics and ABC-test
  state-by-state risk), and any decision crossing the multi-state
  income-tax nexus boundary.
- **Employment-law attorney** for decision 7 (first W-2 employee
  hiring, especially in CA / MA / NJ / IL where ABC-test
  misclassification penalties are severe — backpay, payroll-tax
  liability, statutory penalties, and in CA private-attorneys-general-
  act exposure that can exceed the unpaid wages many-fold), decision
  11 (co-founder departure with non-compete / non-solicit / IP-
  assignment disputes), and any wrongful-termination or
  discrimination-claim posture in the early hiring rounds.
- **Insurance broker familiar with startup E&O / D&O / cyber** for
  any decision where the company is taking on customer contracts with
  indemnification obligations, raising priced equity (D&O becomes
  effectively mandatory once outside directors are seated), or
  handling regulated data (PHI / PII / PCI cardholder data —
  cross-cutting `legal-disputes` and the relevant compliance regime).
  Note: not enumerated as a per-decision referral below because it
  cuts across decisions rather than mapping to one.
- **State Bar / FINRA BrokerCheck / NJ-NY-CA Bar-grievance lookup**
  as a $0-friction procedural floor on any individual attorney /
  CPA / broker recommended — verify license and disciplinary history
  before engagement. Cross-references `personal-finance` decisions.md
  on this same procedural floor.

Framing-axes named below are pointers — full framings will live in
`framings.md` (later artifact). `entrepreneurship` is **cross-cutting**
in a different way than `personal-finance`: rather than tax-and-cash-
flow cascading out, entrepreneurship decisions cascade *into* the
founder's `personal-finance` (retirement-vehicle selection, QBI,
QSBS), `health-insurance` (loss of employer coverage, ACA / spousal
fall-back), `legal-disputes` (founder disputes, IP assignment,
employment claims), `housing` (HELOC-or-cash-out-refi as bridge
capital, mortgage-qualification with 1099 income), and `tech-career`
(employer-IP-assignment carve-outs, W-2-to-1099 transition). Cross-
domain edges flagged inline below: `personal-finance` overlaps on
solo-401(k) / SEP-IRA / SIMPLE selection (decisions 4, 8),
QBI Section-199A deduction sizing (decisions 4, 8), QSBS Section-1202
5-year-hold (decisions 5, 10), S-corp-reasonable-salary minimization
(decision 4), and retirement-account-creditor-protection for founder
personal assets (decision 11). `tech-career` overlaps on
W-2-to-1099 transition timing relative to RSU vest schedule
(decisions 2, 3), employer-IP-assignment carve-out for moonlight
work (decisions 2, 3), and golden-handcuffs-vs-leap framing (decision
3). `legal-disputes` overlaps on founder-lawsuit posture (decision
11), IP-assignment carve-outs and Defend-Trade-Secrets-Act exposure
(decisions 2, 11), and worker-misclassification PAGA / wage-and-hour
claims (decision 7). `health-insurance` overlaps on solo health
insurance via ACA marketplace vs spousal coverage vs COBRA bridge
(decision 3), small-group plans once first W-2 employee is hired
(decision 7), and HSA-eligibility-via-HDHP for the founder personally
(decision 8). `housing` overlaps on HELOC / cash-out-refi as bridge
financing alternative (decision 3), and mortgage-qualification with
1099 / S-corp-distribution income that lenders treat with sharply
higher scrutiny (decision 4 specifically — 2 years of tax returns
typically required, with self-employment income averaged and
discounted). `immigration` overlaps for foreign founders on E-2 / O-1
/ EB-5 / founder-on-H-1B mechanics (not enumerated per-decision below
because the carve-out is the bigger framing — visa-status founders
face structurally different constraints across nearly every decision
and the routing belongs in `immigration/decisions.md`, not duplicated
here). Routing across edges is V2-Triage's job; the edge annotations
here help future `framings.md` authors name the adjacent domains.

---

## 1. Co-founder selection and equity structuring (split + vesting + IP-assignment)

- **Scope**: One or more founders are forming a new company together
  and must decide the equity split, the vesting schedule (cliff +
  vesting period + acceleration triggers), and the IP-assignment
  posture (what each founder is bringing in, what's been carved out
  from a prior employer). Decision spans the split (50/50 vs
  asymmetric vs solo-with-advisors), the vesting structure (4-year
  with 1-year cliff is market-standard; reverse-cliff and "earnout"
  variants exist for asymmetric-contribution cases), the double-
  trigger acceleration on change-of-control (single-trigger is rare
  and acquirer-hostile; double-trigger is standard), and the
  Confidential-Information-and-Invention-Assignment-Agreement (CIIAA)
  scope and carve-outs. Distinct from decision 11 (departure /
  dispute resolution after the structure is in place) — here the
  question is the up-front structure. Cross-routes `tech-career`
  (employer-IP-assignment from prior W-2 employer can void or
  encumber the founder's contribution to the new company if not
  carved out — CA Labor Code §2870 limits employer-IP claims but
  doesn't eliminate them; other states are more aggressive),
  `legal-disputes` (CIIAA scope disputes are the most-litigated
  founder-disagreement category; vesting cliff disputes are the
  second-most), `personal-finance` (the 83(b) election on founder
  restricted stock is a 30-day filing window from grant; missing it
  causes ordinary-income tax on each vest tranche at FMV, which
  approaches a tax-poison-pill at exit — boundary
  `personal-finance` decision 1, decision 6).
- **Framing-axes-covered**: 50/50-equal-split-vs-vesting-asymmetric-
  vs-cap-table-precision-to-1% (the 50/50 equal split is the
  founder-community default and signals shared-fate, but Noam
  Wasserman's "Founder's Dilemmas" data shows 50/50 splits correlate
  with higher post-Series-A founder-conflict; vesting-asymmetric
  with the same end-state but different cliffs / acceleration is the
  more honest framing when contributions are genuinely asymmetric;
  cap-table-precision-to-1% is a YC-influenced framing that says
  small fractional differences matter less than getting the vesting
  right), four-year-vesting-with-one-year-cliff-vs-reverse-cliff-
  vs-front-loaded (4/1 is market-standard for both founders and
  employees; reverse-cliff — founder vests faster early and slower
  late — is rare but appropriate when one founder is bringing
  in disproportionate initial IP / brand / customer base; front-
  loaded vesting can be appropriate for the late-joining
  "technical-co-founder" who joined post-incorporation but pre-
  funding), double-trigger-acceleration-on-change-of-control
  (single-trigger acceleration vests on M&A regardless of
  continued employment — acquirers hate it because it incents the
  founder to leave post-close; double-trigger requires both M&A
  AND involuntary termination — vests only if acquirer fires the
  founder; double-trigger is the standard ask in modern term
  sheets; 100% double-trigger acceleration is the founder ask,
  acquirer counter is typically 25-50%; the unfunded-pre-priced-
  round case sometimes uses single-trigger and gets renegotiated
  at first priced round), confidential-information-and-invention-
  assignment-CIIAA-scope-and-prior-art-carve-out (the CIIAA each
  founder signs must list prior inventions / prior art carved out
  of assignment; failure to list means the new company owns
  everything the founder ever did, which causes downstream disputes
  when the founder wants to use a prior side-project; California
  Labor Code §2870 prevents employer-IP claims on work done outside
  scope on personal time without employer resources, but other
  states — Delaware, NY, MA — are more aggressive and the carve-out
  document is the load-bearing protection), 83(b)-election-30-day-
  window (founder restricted stock granted with vesting requires
  an 83(b) election within 30 days of grant to elect to pay
  ordinary-income tax NOW at FMV ($0.001/share or fractions of a
  cent at incorporation, so tax owed is near-zero) rather than at
  each vest tranche; missing the 30-day window causes ordinary-
  income tax on each vest tranche at then-current FMV, which can
  approach 50%+ of the equity value at a high-growth exit — this is
  a tax-poison-pill that has killed founder net-worth on otherwise-
  successful exits; the 30-day window starts at grant, not at
  incorporation, and there is NO extension or recovery mechanism;
  IRS Form to file is direct attachment to the founder's 1040 plus
  certified-mail copy to IRS service center; boundary
  `personal-finance`), advisor-equity-vs-founder-equity-vs-employee-
  pool (advisors get 0.1-1.0% typically, vest over 1-2 years, FAST
  agreement is the Founder-Institute standard template; advisor
  equity should not be confused with founder equity in cap-table
  arithmetic — early-stage founders sometimes give "co-founder
  title" to advisors and over-dilute, which becomes a dispute when
  the priced round forces a clean-up).
- **Sample situations**:
  - "Two co-founders forming a SaaS; I have the idea + 6 months of
    MVP code, they have 12 years of deep-tech engineering experience
    we need. They're proposing 50/50 with 4/1 vesting. Should I
    counter with 60/40 given the IP head-start, or accept and focus
    on getting the vesting + CIIAA right?"
  - "Solo founder, brought on a 'technical co-founder' 4 months
    post-incorporation. They want 30% with vesting starting at their
    join date. I have 70% already vested 4/12 of a 4-year schedule.
    How do I structure this without giving them a tax-poison-pill
    grant?"
  - "Three founders, equal 33% split, joined together at
    incorporation. We forgot to file 83(b) elections. Stock is at
    par value ($0.0001/share × 4M shares = $400 FMV at grant).
    Discovered the miss at month 4. Is there ANY recovery, or do
    we eat ordinary-income tax at each vest going forward?"

## 2. Bootstrap to revenue vs raise pre-seed / seed (timing + dilution + time-to-PMF compression)

- **Scope**: Founder(s) with an early-stage company (pre-revenue or
  early-revenue) deciding whether to seek outside capital (angels,
  pre-seed funds, seed funds) or self-fund / bootstrap to a revenue
  milestone before raising (if ever). Decision is the joint
  consideration of (a) the dilution accepted to compress time-to-
  product-market-fit, (b) the strategic-and-control consequences of
  taking institutional capital (board seats, information rights,
  protective provisions, pro-rata rights for follow-ons), (c) the
  founder's personal-financial runway and risk tolerance, and (d)
  the realistic market-size case for the company. Distinct from
  decision 5 (the SAFE-vs-priced-seed instrument choice once the
  decision to raise is made) and decision 3 (the quit-day-job leap
  itself). Cross-routes `personal-finance` (the bootstrap path
  amplifies founder personal-cash-flow constraint; the raise path
  can fund founder modest salary which changes the retirement-
  account-contribution math — boundary decision 1 / decision 8 in
  this file, decision 1 in personal-finance), `tech-career` (the
  founder's day-job-fallback option-value scales with how recent
  their last comp benchmark is; pausing for 18 months on bootstrap
  vs raising-and-paying-themselves is partly a job-market hedge).
- **Framing-axes-covered**: dilution-arithmetic-and-compounding-
  across-rounds (pre-seed $500k on 5M post = 10% dilution; seed
  $2M on 12M post = ~17% additional; Series A $10M on 40M post =
  ~25% additional; founders who do all three rounds with no
  unusual amounts retain ~50-55% combined pre-Series-B; bootstrap
  to revenue + skip pre-seed/seed can preserve full founder
  ownership but typically caps growth speed), time-to-product-
  market-fit-compression-via-capital (capital lets you parallelize
  experiments — hire engineers to run multiple builds, hire growth
  marketers to test channels, buy data and tools; bootstrap forces
  serial experimentation which extends calendar-time-to-PMF but
  forces ruthless prioritization that often produces tighter early
  product), board-seats-and-information-rights-and-protective-
  provisions (institutional investors take board seats at seed
  typically; information rights require monthly or quarterly
  reporting; protective provisions require investor approval for
  major decisions — issuing new equity, taking on debt above $X,
  changing the business materially, selling the company; founders
  often underestimate the time-cost of board management and the
  decision-velocity loss from protective provisions — both
  compound across rounds), pro-rata-rights-and-the-stack-of-
  obligations-to-existing-investors (early investors typically
  negotiate pro-rata participation rights for future rounds; this
  reserves cap-table space for them and constrains follow-on round
  composition; the founder optimizing for ownership has to budget
  for pro-rata at every subsequent round), revenue-bar-as-leverage-
  in-raise-negotiation (raising at $0 revenue is purely team /
  vision / market; raising at $50k MRR is on a 10-20x ARR
  multiple basis with comparable-company valuation anchors;
  raising at $1M ARR is mid-Series-A territory with real
  negotiating leverage on valuation and term-sheet structure; the
  bootstrap-to-revenue path trades calendar-time for raise-leverage),
  cash-flow-business-vs-venture-scale-business-self-honesty (most
  SaaS / service businesses can sustain founder + small team on
  $200k-$1M ARR; the VC math requires $100M+ ARR exit potential to
  justify the dilution, which means roughly 1-in-100 of seed-funded
  companies returns the fund; founders running cash-flow-positive
  businesses who take VC money are signing up for a swing-for-the-
  fences trajectory that destroys $5M-ARR-comfortable-business
  outcomes — this is the "venture trap" framing), founder-personal-
  runway-as-implicit-cost (bootstrap with 18 months of personal
  savings is functionally a $X/year personal-salary forgone
  investment; raising at modest founder salary + dilution is the
  alternative; the implicit-personal-runway-cost is rarely surfaced
  in raise/bootstrap math but is often the load-bearing constraint).
- **Sample situations**:
  - "B2B SaaS at $40k MRR, 4 paying customers, 2 founders no
    employees. Pre-seed fund offers $1.5M at $7.5M post (~17%
    dilution). We could probably hit $80k MRR in 6-9 months on
    cash flow. Take the round or wait and raise at $80k MRR?"
  - "Solo founder, dev-tools open-source-with-paid-cloud, no
    revenue yet, 8 months runway from savings. Angel investor
    offers $250k on a $5M post SAFE. Take it, or stay solo and
    push for revenue first?"
  - "Two-founder consulting firm, $400k revenue, profitable.
    Considering productizing a SaaS spinout. Bootstrap from
    consulting cash flow or raise a seed to dedicate full-time to
    the SaaS? Consulting-as-implicit-financing vs venture-scale."

## 3. Quit day job vs nights-and-weekends (signal threshold and risk-bearing capacity)

- **Scope**: Aspiring or current founder with a paying day-job
  evaluating when (or whether) to quit and work on their startup
  full-time. Decision is the joint consideration of (a) the
  signal-threshold metric that would justify the leap (typically
  MRR, but can be customer-LOI count, hire-able team commitments,
  closed funding round, validated pricing), (b) the founder's
  personal-financial runway and burn rate, (c) the day-job-IP-
  assignment exposure on continued moonlight work, (d) the
  household risk-bearing capacity (single vs dual-income, kids,
  health-insurance dependence on employer plan), and (e) the time-
  efficiency loss of context-switching between day job and startup.
  Distinct from decision 2 (the raise-vs-bootstrap choice, which
  is downstream of being full-time) and decision 1 (forming the
  company itself). Cross-routes `personal-finance` (emergency-fund
  sizing and asset-allocation shifts when household income drops;
  Roth-conversion-window opens in a low-income year — boundary
  decision 7 in personal-finance), `tech-career` (the day-job-
  fallback option-value erodes with time-away-from-market; deep-
  tech roles in particular have a 12-24-month freshness window;
  golden-handcuffs from RSU vesting cliffs create implicit per-
  month opportunity cost — boundary decision 4 / decision 5 in
  tech-career), `health-insurance` (loss of employer coverage
  forces ACA-marketplace / spousal-plan / COBRA decision — COBRA
  is 18 months at full-cost-plus-2%, ACA may have subsidy at low
  income, spousal coverage typically cheapest if available —
  boundary decision 1 / decision 3 in health-insurance), `housing`
  (HELOC or cash-out-refi as bridge capital must be originated
  BEFORE the income drop because lenders qualify on W-2 income
  not yet-unproven self-employment income — boundary decision 8
  in housing).
- **Framing-axes-covered**: MRR-or-revenue-threshold-as-signal
  (common heuristics: "quit when MRR covers 50% of expenses",
  "quit at $10k MRR with growth", "quit at $30k MRR with
  retention", "quit when full-time would clearly accelerate
  growth more than 2x"; the right threshold depends on (a) burn
  rate, (b) growth slope, (c) personal runway — there is no
  universal number, and the heuristics-treated-as-rules cause
  founders to either leap too early or stay too long; the
  framing axis is "what's the growth-slope-change a full-time
  commitment would produce, and is that worth the personal-
  income-loss"), six-to-eighteen-months-runway-and-burn-rate-
  honesty (the typical advice is 12+ months personal runway
  before quitting; the load-bearing variable is honest burn-rate
  forecasting including healthcare, taxes on prior-year W-2
  income, and a buffer for founder-mental-health spending
  (therapy, gym, occasional travel reset — running out of
  buffer-for-self compresses founder time-horizon decision-
  making); single-founder-with-kids runway is materially longer
  than single-founder-no-dependents — 24+ months not 12; partner-
  income-as-runway-extender is real but creates relationship-
  capital cost that compounds across the runway), day-job-IP-
  assignment-on-moonlight-work (most employer IP-assignment
  clauses claim ownership of inventions created "during
  employment" or "using employer resources" or "related to the
  employer's business"; California Labor Code §2870 carves out
  inventions created (a) on the employee's own time, (b) without
  employer equipment or facilities, (c) not related to the
  employer's actual or anticipated business; other states are
  less protective and the carve-out lives in the offer letter
  and employee handbook; "anticipated business" is the load-
  bearing fuzzy term — a sufficiently-broad employer-mission
  statement can swallow most adjacent founder ideas; the
  recovery move is (i) carve out the side-project in writing
  with the employer, (ii) avoid using any employer equipment /
  network / time, (iii) be ready to walk if the employer
  refuses to carve out — the alternative is an IP-assignment
  lawsuit at the moment of liquidity, which has destroyed
  founder net-worth at exit), context-switching-cost-and-decision-
  velocity (running a startup nights-and-weekends caps decision-
  velocity at the founder's available cycles; 10-15 hours/week
  of focused-startup-time often translates to ~30 hours of
  calendar week including context-switch and energy-recovery;
  many decisions that move the company forward require sustained
  blocks (3-5 hours minimum) which are hard to find in fragments
  — this is why the "side project to full-time" transition
  often produces a 3-5x productivity jump that surprises the
  founder), household-risk-bearing-capacity-and-dependent-effects
  (single-income-household with kids and mortgage carries
  fundamentally different decision-weights than dual-income-no-
  kids; the household's collective risk tolerance constrains the
  decision more than the founder's individual risk tolerance;
  the spouse-as-implicit-investor framing — the spouse is taking
  uncompensated risk by accepting income variance — is rarely
  surfaced explicitly), Roth-conversion-window-on-low-income-year
  (a year of reduced or zero W-2 income from the leap creates a
  Roth-conversion window: traditional-401(k) or traditional-IRA
  balances can be converted to Roth at the founder's low marginal
  rate, locking in the rate forever; this is the highest-leverage
  personal-finance move available to a quitting founder and is
  almost universally missed — boundary `personal-finance`
  decision 7).
- **Sample situations**:
  - "Single, 31, $230k base + $180k RSU at MAANG, $80k saved. SaaS
    side project at $4k MRR growing 25%/mo. Day job is consuming
    60+hrs/wk, can't move the startup faster. Quit now, quit at
    $10k MRR, or quit at $30k MRR? Cliff is 8 months out at
    next vest."
  - "Married, 38, two kids 4 and 7, $180k household income (mine
    $160k, spouse $20k part-time), $300k home equity, $250k
    retirement. Have a B2B idea with 3 LOIs. When can I leap?"
  - "Just got laid off with 4 months severance + 6 months COBRA
    eligibility. Was going to start company in 18 months anyway.
    Use severance as runway and start now, or job-search and
    start later? How does the severance change the IP carve-
    out math vs starting while employed?"

## 4. LLC pass-through vs S-corp election (the ~$80k crossover and self-employment-tax mechanics)

- **Scope**: Self-employed individual or LLC member with net
  business income high enough that the self-employment-tax math
  may favor electing S-corporation tax treatment via IRS Form 2553.
  Decision is whether to (a) operate as sole-proprietor or default
  LLC pass-through (entire net income subject to 15.3% SE tax up
  to the Social Security wage base then 2.9% Medicare above, plus
  ordinary income tax), (b) elect S-corp tax treatment (split net
  income into reasonable salary subject to FICA and remainder as
  distributions exempt from FICA), or (c) elect C-corp tax treatment
  (separate entity, 21% federal corporate rate, then dividend tax
  on distributions — double taxation; only relevant for retained-
  earnings or specific QSBS positioning). The "crossover" point
  where S-corp savings exceed S-corp compliance costs (payroll
  service, separate corp-tax-return, additional bookkeeping,
  reasonable-salary documentation) is typically cited as $80-100k
  in net income but the right answer depends sharply on (a) state
  S-corp recognition (CA imposes a 1.5% S-corp tax, NY-NYC and TN
  have additional layers; some states don't recognize S-corp at
  all and tax as C-corp), (b) reasonable-salary defensibility for
  the founder's role (a $200k-net-income consultant cannot pay
  themselves $30k salary; the IRS Watson v US precedent and the
  ongoing audit-scrutiny pattern on under-salary S-corps make this
  load-bearing), (c) QBI Section-199A interaction (the §199A
  pass-through deduction is reduced for SSTBs — Specified Service
  Trades or Businesses, including law, accounting, consulting,
  health — above income thresholds; S-corp reasonable-salary
  reduces QBI but also reduces SE tax). Distinct from decision 6
  (sole-prop vs LLC formation) — here the question is the TAX
  election within an already-formed entity. Cross-routes
  `personal-finance` (S-corp election interacts with solo-401(k)
  contribution math because employee-deferral is based on W-2
  salary not net income; SEP-IRA contribution is based on net SE
  earnings; this is a load-bearing interaction with decision 8 in
  this file and decision 1 in personal-finance; QBI Section-199A
  pass-through deduction is sized off the QBI amount which is
  reduced by S-corp reasonable salary — boundary `personal-finance`
  decision 1 / decision 7), `housing` (mortgage-qualification with
  S-corp-distribution income vs W-2 salary income — lenders treat
  the W-2 portion at face value but discount the distribution
  portion 75% with 2 years of returns required; election timing
  matters if a mortgage application is in flight — boundary
  decision 8 in housing).
- **Framing-axes-covered**: self-employment-tax-arithmetic-on-net-
  income (sole-prop or single-member-LLC: 15.3% SE tax on first
  $168,600 of net SE earnings in 2025 (Social Security wage base),
  then 2.9% Medicare above, plus 0.9% additional Medicare for high-
  earners above $200k single / $250k MFJ; for $200k net SE earnings
  the SE tax is roughly $25k — and this is BEFORE ordinary income
  tax; the S-corp election splits this into reasonable salary
  (subject to FICA = 15.3% combined) and distributions (exempt
  from FICA) — the saving is 15.3% × distribution-portion), the-
  80k-crossover-and-why-it's-actually-fuzzy (the $80-100k crossover
  comes from rough math: at $80k net, splitting $50k salary / $30k
  distribution saves ~$4.5k in FICA; S-corp compliance costs
  (Gusto-or-similar payroll $50/month × 12 = $600, S-corp tax
  return at $800-1500, additional CPA time, state S-corp tax in
  CA $800-minimum or 1.5% of net) typically run $2-4k/year — the
  break-even is income-AND-state-dependent; in CA-with-1.5%-tax
  the crossover is closer to $100-120k; in TX-with-no-state-income-
  tax it's closer to $60-80k), reasonable-salary-defensibility-and-
  IRS-audit-risk (the IRS focuses S-corp audit attention on
  S-corps paying obviously-low salaries relative to industry
  comparables; Watson v US (8th Cir 2012) established the
  reasonable-salary standard — a CPA paid himself $24k salary on
  $200k+ S-corp net income, IRS reclassified $67k as additional
  salary subject to FICA, the court upheld; tools like RCReports
  generate defensible salary benchmarks against BLS / industry
  comp; the safer posture for an audit-defensible salary is 40-60%
  of net income at lower income levels, decreasing to 25-40% at
  much higher net income; a salary below ~$30k regardless of net
  income is a high-audit-risk pattern), state-S-corp-recognition-
  variation (CA: 1.5% S-corp tax on net income, $800 minimum;
  NY: S-corp recognized federally but NY-NYC adds NYC unincorporated
  business tax then NYS personal income tax; TN: franchise tax;
  some states (Louisiana, DC) don't recognize S-corp election —
  taxes as C-corp at state level; multi-state nexus from out-of-
  state customers complicates further; CPA-with-multi-state-
  experience referral is warranted when net income > $150k and any
  cross-state nexus exists), QBI-Section-199A-interaction-and-SSTB-
  phaseout (the §199A pass-through deduction is 20% of QBI for
  pass-through-entity owners; for Specified Service Trades or
  Businesses — law, accounting, consulting, finance, health,
  performing arts, athletics — the deduction phases out between
  $191,950-$241,950 single / $383,900-$483,900 MFJ in 2024 income
  thresholds (verify 2025 numbers); S-corp reasonable salary is
  NOT part of QBI, so a high-salary-low-distribution split reduces
  both SE tax AND QBI deduction — the optimization is non-trivial
  and CPA-supported; for SSTB founders near the phaseout, a year
  of higher salary can preserve QBI by keeping taxable income
  below the threshold), C-corp-as-rare-third-option (C-corp
  election makes sense only for (a) startups raising venture
  capital — investors require Delaware C-corp for series-rounds,
  (b) QSBS Section-1202 positioning — only C-corps qualify for
  QSBS 5-year-hold gain exclusion up to $10M or 10x basis,
  (c) businesses planning significant retained earnings reinvested
  at 21% corporate rate; for typical consulting / single-product
  software the C-corp creates double-taxation pain that exceeds the
  savings; boundary `personal-finance` decision 6 on QSBS).
- **Sample situations**:
  - "Solo software consultant, $180k net income year 2 of LLC.
    Currently default LLC pass-through. CPA suggesting S-corp
    election starting January. I'm in CA. Worth it? What
    reasonable salary?"
  - "Two-partner LLC in TX, $400k net income split 60/40.
    Considering S-corp election. How does the split affect
    each partner's election decision — can one elect and the
    other not?"
  - "Just hit $300k 1099 income as freelance dev. Want to
    maximize retirement contributions. S-corp election lets
    me do solo-401(k) employee deferral on salary AND profit-
    sharing on net SE — does the S-corp election help or hurt
    the retirement-cap math? Boundary with decision 8."

## 5. SAFE post-money cap vs priced seed (valuation cap + MFN + pro-rata + dilution prediction)

- **Scope**: Founder raising the first institutional or angel round
  is choosing between (a) issuing SAFEs (Simple Agreements for
  Future Equity, YC standard) with valuation caps and optional
  discount rates, (b) issuing convertible notes (similar to SAFE
  but with interest and maturity date), or (c) doing a priced
  equity round (typically preferred-stock Series Seed) with
  defined valuation and term-sheet provisions. Decision spans the
  instrument choice, the valuation cap (post-money SAFE caps are
  now standard post-2018; pre-money caps were the older norm and
  caused unpleasant founder surprises on dilution), the discount
  rate (typically 0-25% — many modern SAFEs have no discount,
  just the cap), MFN clause (Most-Favored-Nation — if a later
  SAFE has better terms, this SAFE auto-upgrades), pro-rata side-
  letter rights (typically only for $250k+ check sizes), and the
  conversion mechanics at the next priced round. Distinct from
  decision 2 (the choice TO raise) — here the question is the
  instrument and terms. Cross-routes `personal-finance` (QSBS
  Section-1202 5-year-hold starts at C-corp stock issuance, not at
  SAFE issuance; SAFEs don't start the QSBS clock — only the
  conversion to priced equity does, which delays the 5-year-hold
  by however long the SAFE sits unconverted; this is a load-
  bearing tax timing consideration for founders and key early
  employees with significant equity — boundary `personal-finance`
  decision 1 / decision 6).
- **Framing-axes-covered**: post-money-cap-vs-pre-money-cap-and-
  founder-dilution-arithmetic (post-money SAFE: the cap IS the
  post-money valuation including the SAFE itself; if a founder
  takes $1M on $10M post-money cap, the SAFE holders own 10%
  on conversion regardless of how many other SAFEs are issued
  before the priced round; pre-money SAFE: the cap is pre-money,
  meaning each subsequent SAFE dilutes the founder MORE than
  expected because the post-money valuation grows with stacked
  SAFEs; YC switched to post-money in 2018 because pre-money
  caps were surprising founders with 30-50% dilution at priced
  round when expected was 15-20%), valuation-cap-as-binding-or-
  irrelevant-depending-on-priced-round-valuation (the cap binds
  if the priced round valuation > cap; binding cap converts SAFEs
  at the lower cap valuation, so SAFE holders get more equity per
  dollar than priced-round investors; non-binding cap (priced
  round at or below cap) converts SAFEs at priced-round valuation
  with the discount applied; the binding-cap scenario is the
  founder-dilutive surprise — a $5M cap SAFE at a $30M Series A
  converts as if Series A were at $5M, which means SAFE-holders
  get 6x the equity per dollar of priced-round investors — this
  arithmetic is regularly mis-modeled in founder cap-table
  projections), MFN-most-favored-nation-clause-and-stacking-risk
  (MFN clauses auto-upgrade an early SAFE if a later SAFE has
  better terms (lower cap, higher discount, more rights); innocent
  on its face, but if the founder stacks 5+ SAFEs at various
  terms while trying different price points to attract investors,
  MFN causes all earlier SAFEs to auto-upgrade to the best terms
  issued — which can quietly multiply early-SAFE dilution; the
  recovery is to issue ONLY at one set of terms within a given
  SAFE-stack, and re-paper when terms change), pro-rata-side-
  letter-rights-and-investor-stack (lead pre-seed / seed investors
  with check sizes above $250k typically negotiate pro-rata side
  letters granting the right to participate in subsequent rounds
  at the new price; founders accept this routinely without
  modeling the cumulative effect on later rounds — at Series A
  the pro-rata holders may demand $X of the round, constraining
  the round size or pushing the founder to increase the round at
  the cost of additional dilution), QSBS-Section-1202-clock-
  doesn't-start-on-SAFE (the 5-year-hold-period for QSBS gain
  exclusion starts at C-corp stock issuance; SAFEs are not stock,
  they're convertible instruments; the clock starts when SAFE
  converts to preferred at the priced round, not when SAFE was
  issued; founders sitting on SAFEs for 18-24 months pre-priced-
  round are losing 18-24 months of QSBS clock; if a priced round
  is foreseeable within 6 months, accelerating conversion via a
  formal priced round (vs continuing to SAFE) can preserve QSBS
  clock — boundary `personal-finance` decision 1 / decision 6;
  this is among the highest-leverage tax considerations for
  founder eventual-exit-net-worth and is almost universally
  missed by non-startup-CPAs), priced-seed-as-alternative-when-
  terms-matter (priced equity Series Seed with defined preferred-
  stock terms is the right choice when (a) the round is large
  enough to justify the legal cost ($15-30k vs $1-3k for SAFEs),
  (b) the investors require liquidation preference / participation
  rights / anti-dilution provisions that SAFEs don't carry, (c)
  the founder values certainty over future SAFE-conversion-
  modeling, (d) starting the QSBS clock is valuable; the trade-
  off is the legal cost and the founder time-commitment to
  negotiate the term sheet vs the SAFE simplicity).
- **Sample situations**:
  - "First check, $500k from a known angel, offering YC standard
    post-money SAFE at $8M cap, no discount, no MFN, no pro-
    rata. We expect to raise priced seed at $20M+ in 12 months.
    Take it as-is, or negotiate down the cap, or push for
    priced round directly?"
  - "Stacked 6 SAFEs over 14 months: $50k at $4M cap, $200k at
    $5M, $150k at $6M, $300k at $7M, $200k at $7M with MFN,
    $250k at $8M with MFN. Now raising $5M priced Series A.
    What's our actual cap-table going to look like?"
  - "Considering between $2M priced seed at $10M post-money
    (with full Series Seed term sheet, board observer rights,
    pro-rata) vs $2M post-money SAFE at same $10M cap with no
    other terms. What are we giving up by going priced, and
    what are we giving up by staying SAFE?"

## 6. Sole-prop vs LLC formation timing (liability shield, audit risk, state-fee variation)

- **Scope**: Aspiring or current self-employed individual deciding
  whether to operate as a sole-proprietor (no formal entity, all
  income reported on personal Schedule C), to form a single-member
  LLC (state-level entity providing limited-liability shield, taxed
  as sole-prop by default unless S-corp or C-corp election under
  decision 4), or to form a multi-member LLC or partnership.
  Decision spans timing (form now vs revenue-trigger vs liability-
  trigger), state of formation (home state typically; Delaware-LLC
  for software-and-IP-businesses is a sometimes-overrated default),
  and the relationship between LLC formation and the tax-election
  decision in decision 4. Distinct from decision 4 (tax election
  on an already-formed entity) — here the question is whether to
  form the entity at all and when. Cross-routes `legal-disputes`
  (the limited-liability shield is the primary functional benefit
  of an LLC, but the shield is eroded by undercapitalization,
  commingling of funds, failure to follow corporate formalities,
  and direct-tort-by-the-member; "piercing the corporate veil" is
  a real risk and the shield is not absolute — boundary
  `legal-disputes` on liability disputes), `personal-finance`
  (LLC formation costs and annual state fees are non-trivial in
  some states — CA $800/year minimum franchise tax even at zero
  income, NY publication requirement adds $1k-2k one-time fees,
  DE annual report $300; for a sub-$50k-revenue side-business
  these fees can exceed the LLC's tax-and-liability benefits).
- **Framing-axes-covered**: liability-shield-as-primary-benefit-
  and-where-it-fails (the LLC's primary functional benefit is
  the limited-liability shield: members are not personally liable
  for LLC debts and judgments (with exceptions); the shield is
  load-bearing for any business with (a) physical premises and
  customer foot traffic (slip-and-fall risk), (b) products that
  could cause injury, (c) contracts with significant indemnity
  exposure, (d) employees (employment-related claims); the shield
  is much LESS valuable for (a) solo software consulting where
  the work product is the only liability surface and a contract
  E&O clause does most of the work, (b) pure online content /
  newsletter businesses, (c) any business where the founder is
  personally licensed (lawyer, doctor, architect — professional
  liability isn't shielded by an entity); piercing-the-corporate-
  veil happens via undercapitalization, commingling personal and
  business funds, failure to file annual reports, signing
  contracts in personal name not entity name, and direct-tort by
  the member — the LLC can be "ignored" by courts when these
  formalities aren't kept), state-fee-variation-and-the-CA-$800-
  minimum (CA franchise tax is $800/year minimum regardless of
  income (waived first year for new entities since 2021, but
  collected from year 2); NY has a publication requirement
  costing $1,000-$2,000 one-time depending on county (Manhattan
  county is expensive); TX has no franchise tax until $1.23M
  revenue (2024) but requires annual public-information report;
  DE has $300 annual report + registered-agent service if
  founder is not resident; the right state of formation is
  typically the founder's home state — Delaware-LLC for non-
  Delaware-resident founders adds foreign-qualification cost in
  home state, doesn't escape home-state taxes, and provides no
  benefit for sub-Series-A entities), formation-timing-vs-revenue-
  trigger-vs-liability-trigger (revenue-trigger: form once revenue
  exceeds a threshold where the tax-or-fee math favors entity;
  liability-trigger: form before signing the first customer
  contract with material indemnity exposure or hiring the first
  contractor or employee; defensive-trigger: form before
  approaching investors or partners who will not deal with a
  sole-prop; the right trigger depends on which liability surface
  matters most — revenue alone is the wrong trigger if no
  liability exposure exists, liability alone is the wrong trigger
  if no real exposure exists), single-member-LLC-vs-multi-member-
  LLC-tax-treatment (single-member LLC is taxed as disregarded
  entity = sole-proprietor on Schedule C; multi-member LLC is
  taxed as partnership on Form 1065 with K-1s to members; an
  S-corp election (decision 4) converts either to S-corp
  treatment; the multi-member partnership treatment is its own
  return-filing complexity and the K-1 must reach members by
  March 15 — a major upgrade in compliance burden over sole-
  prop), DBA-as-lighter-alternative-when-LLC-isn't-justified
  (a Doing-Business-As filing in the founder's county registers
  a business name without forming an entity; allows opening a
  business bank account and signing contracts under a business
  name; provides ZERO liability shield; appropriate for sub-
  $30k-revenue side-businesses with no liability exposure where
  the founder just wants a brand identity and a separate bank
  account; cost is typically $20-50 + advertisement requirement
  in some counties), bank-account-and-EIN-as-prerequisite-step
  (regardless of entity choice, separate business bank account
  + EIN (IRS Form SS-4, free, instant online) is the minimum
  hygiene; commingling personal and business funds is the
  fastest way to lose corporate-veil protection even if an LLC
  exists, and is the fastest way to make a Schedule C audit
  unwinnable for sole-props; EIN is also required to hire even
  one W-2 employee — see decision 7).
- **Sample situations**:
  - "Just started freelancing while in W-2 job, $15k revenue
    expected year 1. Worth forming an LLC, or DBA + business
    bank account is enough?"
  - "$90k year-2 software consulting revenue in CA. Currently
    sole-prop. CA's $800 franchise tax annoys me — but I'm
    considering the S-corp election (decision 4). Form LLC
    now or skip LLC and incorporate directly?"
  - "Two-person partnership operating informally, $200k
    revenue, no entity. We're about to sign a $50k contract
    with a Fortune 500 customer with indemnity language we
    don't fully understand. Form LLC + multi-member, or push
    for S-corp election immediately, or get the contract
    redlined first?"

## 7. First W-2 employee vs 1099 contractor (ABC test, misclassification penalties, payroll mechanics)

- **Scope**: Founder hiring the first person to work for the
  company is deciding whether to engage them as a W-2 employee
  (with payroll, withholding, employer-paid FICA, unemployment
  insurance, workers comp, benefits eligibility, and the full
  employment-law exposure) or as a 1099 independent contractor
  (paid gross, no withholding, no employer-FICA, no benefits,
  no unemployment insurance, no workers comp, but with the
  classification at risk if the worker doesn't meet the IRS or
  state-law independent-contractor tests). Decision spans the
  classification choice, the payroll-system selection (Gusto /
  Justworks / Rippling / Deel for global), the benefits-package
  decision (health insurance becomes a major cost driver — see
  cross-route to health-insurance), and the equity-grant decision
  for early employees (typically option pool 10-20%, 4/1 vesting,
  early-exercise + 83(b) option). Distinct from decision 1 (co-
  founder equity) — here the worker is an employee/contractor not
  a co-founder. Cross-routes `legal-disputes` (worker
  misclassification is among the most-litigated employment-law
  categories; CA's PAGA Private Attorneys General Act allows
  employees to sue on behalf of the state for civil penalties on
  misclassification, and CA's AB-5 codified the ABC test broadly
  — the financial exposure for misclassification in CA can
  exceed unpaid wages many-fold including statutory penalties,
  attorney fees, and interest; this is a load-bearing referral
  trigger to employment-law attorney — boundary `legal-disputes`),
  `personal-finance` (payroll-tax mechanics impact the founder's
  own salary decision under decision 4; benefits costs change
  the contribution math under decision 8; equity grants to
  employees trigger 409A valuation requirement — boundary
  `personal-finance`), `health-insurance` (first W-2 employee
  may trigger eligibility for small-group health insurance plans
  which are often more affordable than ACA-individual; SHOP
  marketplace for 1-50 employees; reimbursement-only options like
  QSEHRA and ICHRA — boundary `health-insurance` decision 1).
- **Framing-axes-covered**: IRS-common-law-control-test-and-state-
  ABC-test-divergence (IRS uses the common-law-control test: 20+
  factors covering behavioral control (how work is done),
  financial control (who provides tools, expense reimbursement,
  opportunity for profit/loss), and relationship-type
  (permanency, written contracts, benefits, services-integral-to-
  business); state ABC tests are typically more restrictive —
  a worker is an employee unless ALL of (A) free from control,
  (B) work outside usual course of business, (C) customarily
  engaged in independent trade; CA, MA, NJ, IL, NV use ABC or
  ABC-equivalent strict tests; the "(B) outside usual course of
  business" prong is the load-bearing one — a software company
  cannot classify a software engineer as 1099 in CA because
  software is the usual course of business; the worker can be
  legitimately 1099 if they're an external consultant for a
  bounded engagement with their own tools and clients), CA-PAGA-
  and-state-misclassification-penalty-stack (CA AB-5 (2019)
  codified ABC test broadly; PAGA Private Attorneys General Act
  allows employee to sue on behalf of state for civil penalties
  ($100/pay-period/employee for initial violation, $200 for
  subsequent; can apply to all misclassified workers in the
  lookback period); plus unpaid overtime, waiting-time penalties
  under CA Labor Code §203 (up to 30 days of additional wages),
  attorney fees and interest; a CA-misclassified-software-engineer
  case can exceed $100k+ in total exposure even at modest 1099
  rates; out-of-state founders hiring CA workers as 1099 are
  routinely caught here; the recovery is to (a) get state-of-
  worker right, (b) apply the strictest applicable state's test,
  (c) when in doubt, classify as W-2), W-2-employer-cost-loading-
  beyond-salary (employer-side FICA 7.65% on first $168,600
  Social Security wage base + 1.45% Medicare above, federal
  unemployment ~0.6% on first $7,000, state unemployment varies
  ($300-$2,000/year typical at standard rate), workers compensation
  insurance varies sharply by state and class code ($0.50-$5/$100
  of payroll typical for office work), health insurance employer
  share ($500-$1,500/employee/month typical for small-group
  plans), 401(k) match if offered, payroll-service fees ($40-$80/
  month base plus per-employee); the typical loading is 15-30%
  on top of base salary for a W-2 employee, which materially
  changes the budget for first hire), early-employee-equity-grant-
  and-409A-valuation (early employees get option grants from the
  10-20% option pool (set aside at first priced round; granted
  per-hire); option-grant strike price must equal fair market
  value per 409A; before priced round, FMV is often nominal but
  needs documented support (Carta / Shareworks / Pulley provide
  409A valuations at $1-2k); after priced round, 409A is updated
  per Section 409A regulation typically every 12 months or
  material event; mis-pricing an option grant below FMV creates
  income at vest plus 20% penalty — major founder error pattern;
  early-exercise + 83(b) lets employee buy shares immediately
  to start LTCG and QSBS clocks — useful for high-conviction
  early employees), QSEHRA-vs-ICHRA-vs-group-plan-vs-stipend-for-
  health-benefits (Qualified Small Employer Health Reimbursement
  Arrangement (QSEHRA) — for <50 employees, tax-free
  reimbursement of employee individual-market premiums up to
  ~$6,150 self / $12,450 family in 2025; Individual Coverage
  HRA (ICHRA) — same idea but no cap, employees can be classified
  into HRA classes; small-group plan via SHOP or broker; cash
  stipend taxed as wages; the right choice depends on number of
  employees, geographic dispersion, and benefits-philosophy;
  founders forget that first-employee triggers eligibility for
  small-group plans which can be more affordable than ACA-
  individual for both founder and employee — boundary
  `health-insurance` decision 1), contractor-as-stepping-stone-
  to-W-2 (legitimate use of 1099: project-based external work,
  short-term specialized expertise, parallel-clients-with-own-
  tools structure; legitimate transition: hire as 1099 for a
  bounded 3-6 month engagement with clear deliverables, convert
  to W-2 if relationship continues; not legitimate: hire someone
  to be "an employee but called a contractor for tax reasons" —
  this is the misclassification pattern courts and agencies
  target).
- **Sample situations**:
  - "Bootstrap SaaS, $30k MRR, need a backend engineer 30
    hours/week ongoing. Want to hire them 1099 to avoid
    payroll complexity. They're in CA. Safe to do 1099, or
    classify as W-2?"
  - "Need a designer for a 3-month rebrand engagement, will
    work on their own time, parallel-clients, own tools.
    Definitely 1099. But they want to bill through their LLC
    — does that change anything for us as payer?"
  - "Hiring first full-time engineer, $130k base, equity TBD.
    Need to decide health benefits before posting the job.
    QSEHRA reimbursement up to $6k, small-group plan at $1k/
    month employer share, or cash stipend?"

## 8. Solo-401(k) vs SEP-IRA vs SIMPLE-IRA retirement-savings vehicle (self-employed founder)

- **Scope**: Self-employed founder (sole-prop / LLC / S-corp;
  no W-2 employees, or only spouse as W-2) selecting the
  retirement-savings vehicle for the business. Decision spans
  (a) solo-401(k) — employee deferral up to $23,500 (2025) +
  age-50 catch-up $7,500 + employer profit-sharing up to 25% of
  W-2 salary or 20% of net SE earnings, combined up to $70,000
  (§415(c) cap, 2025); (b) SEP-IRA — employer-only contribution
  up to 25% of W-2 compensation or 20% of net SE earnings, max
  $70,000; (c) SIMPLE-IRA — employee deferral $16,500 + 3%
  employer match or 2% non-elective, max much lower; (d) defined-
  benefit / cash-balance plans for very high-earners ($300k+ net
  income, founder near retirement age) allowing $100k-$300k+
  annual contribution. Decision is keyed to (i) the founder's
  net SE income, (ii) the W-2 vs net-SE-income mix (which depends
  on the S-corp election decision from decision 4), (iii) whether
  the founder has access to a backdoor-Roth (SEP-IRA balance
  creates pro-rata problem; solo-401(k) does not), (iv) whether
  any non-spouse employees exist (changes the solo-401(k) and
  SEP eligibility). Distinct from decision 4 (S-corp election)
  but tightly coupled — the S-corp election affects this
  decision's math via the W-2-salary-vs-net-SE-distribution
  split. Cross-routes `personal-finance` heavily (decision 1's
  retirement-account ordering is fundamentally modified for self-
  employed users; backdoor-Roth pro-rata trap from SEP-IRA
  balance is a major design consideration — boundary
  `personal-finance` decision 1).
- **Framing-axes-covered**: solo-401k-as-default-when-eligible
  (solo-401(k) is generally the highest-contribution and most-
  flexible option for solo founders: employee deferral
  ($23,500 + age catch-ups) PLUS employer profit-sharing up to
  the §415(c) cap, plus the contribution split can be all-
  traditional, all-Roth (solo-Roth-401(k) widely available since
  2023), or any mix; the only exclusion is if any non-spouse
  employee works 1000+ hours/year — at which point solo-401(k)
  becomes a regular 401(k) with non-discrimination testing and
  the founder must offer the plan to employees), SEP-IRA-as-
  simpler-but-pro-rata-poison (SEP-IRA is simpler to set up
  (no annual Form 5500 filing required until $250k+ balance,
  most providers charge $0) and contribution is 100% employer-
  side; downside is the SEP-IRA balance counts as a pre-tax IRA
  for backdoor-Roth pro-rata purposes — any backdoor-Roth done
  while a SEP-IRA balance exists is partially taxable on Form
  8606; founders who plan to do backdoor-Roth should AVOID SEP-
  IRA, OR roll the SEP into a solo-401(k) before Dec 31 of the
  backdoor year if the solo-401(k) plan-document accepts
  incoming-rollovers; this is the load-bearing reason to choose
  solo-401(k) over SEP-IRA — boundary `personal-finance`
  decision 1), SIMPLE-IRA-as-rarely-right-for-solo-founder
  (SIMPLE-IRA caps are lower and the employer match structure
  doesn't help solo founders; SIMPLE makes sense for small
  businesses with 2-10 employees where the simpler structure
  outweighs the lower caps; rarely the right answer for solo
  founders), W-2-salary-vs-net-SE-income-base-arithmetic (for
  sole-prop and default-LLC pass-through, contribution base is
  net SE earnings minus 1/2 SE tax = roughly net-business-income
  × 0.9235; for S-corp election, contribution base is W-2 salary
  for employee deferral and W-2 salary for the 25% profit-
  sharing match; the S-corp founder paying themselves $60k
  salary on $200k net income can defer $23,500 employee + $15k
  profit-sharing = $38.5k total vs the sole-prop with same
  $200k net income can do $23,500 employee + ~$36k profit-
  sharing = $59.5k total; the S-corp election (decision 4)
  SAVES SE tax but COSTS retirement-contribution capacity —
  the optimization is non-trivial and CPA-supported, particularly
  for founders trying to maximize tax-advantaged retirement
  while keeping reasonable salary defensible), Mega-Backdoor-Roth-
  in-solo-401k-rare-availability (some solo-401(k) plan-documents
  (E*Trade pre-2024 was the famous example; My Solo 401k Financial
  custom plans) allow after-tax 401(k) contributions plus in-plan-
  Roth conversion, unlocking the Mega-Backdoor Roth strategy at
  the §415(c) cap; most solo-401(k) providers (Vanguard, Fidelity,
  Schwab) do NOT offer this; founders who want Mega-Backdoor
  Roth in a solo-401(k) must use a custom plan-document with
  $500-1500 setup cost and ~$100/year annual fees, justifiable
  only at very-high contribution levels — boundary
  `personal-finance` decision 1), defined-benefit-or-cash-balance-
  plan-for-high-earner-late-career (founder with $300k+ net
  income age 45+ can contribute $100k-$300k+ to a defined-benefit
  / cash-balance plan, far above any DC plan cap; the actuarial
  setup costs $2-5k/year and the contribution-commitment is
  multi-year (mandatory minimum contributions), so this works
  for stable high-earners not for volatile founders; CPA-and-
  actuary-supported — boundary `personal-finance`), spousal-
  employment-as-contribution-multiplier (a spouse working in the
  business as W-2 employee can have their own solo-401(k)
  participation under the same plan, doubling household
  contribution capacity; common pattern in solo-consulting where
  spouse does back-office work; the spouse salary must be
  defensible — actual hours, market-rate-compensation; CPA
  caution warranted on aggressive deployment of this pattern).
- **Sample situations**:
  - "Solo consultant, default-LLC pass-through, $200k net income
    year 3. Want to max retirement contributions. Solo-401(k)
    vs SEP-IRA — and how does this interact with the S-corp
    election decision I'm making in parallel (decision 4)?"
  - "S-corp elected, $300k net, paying myself $80k W-2 salary +
    $220k distributions. What's my retirement contribution
    capacity? Solo-401(k) deferral + match on the $80k?"
  - "I do backdoor-Roth every year via personal IRA. Just
    became self-employed and a CPA is suggesting SEP-IRA. Won't
    that break my backdoor-Roth via pro-rata? What's the right
    sequencing?"

## 9. Pricing model selection (per-seat vs usage vs flat vs freemium with PLG funnel)

- **Scope**: Founder of a software / SaaS / API / API-plus-
  service business is deciding the pricing model — the structure
  by which revenue is collected from customers. Decision spans
  (a) per-seat / per-user pricing (Slack, Linear, Notion-team),
  (b) usage-based / consumption pricing (AWS, Twilio, OpenAI,
  Stripe percentage), (c) flat / tiered pricing (Basecamp,
  WordPress.com plans), (d) freemium with paid-tier upsell
  (Notion, Linear, Asana), (e) hybrid models (per-seat with
  usage-based add-ons; flat-tier with overage). Decision is
  upstream of nearly every revenue-and-growth metric: pricing
  model determines CAC payback, expansion revenue mechanics,
  customer-segment fit, sales-motion (PLG vs sales-led), and
  the metrics the company will optimize for. Cross-routes
  `tech-career` (founders coming from product / engineering
  backgrounds often default to per-seat without questioning;
  founders from finance / consulting backgrounds tend toward
  usage-based without questioning; the discipline is to choose
  based on customer-value-correlation not founder-default).
- **Framing-axes-covered**: pricing-aligned-to-value-metric (the
  central design principle: the unit of pricing should be the
  unit the customer experiences as value; for a CRM, value
  scales with sales-team-size → per-seat; for cloud storage,
  value scales with GB-stored → usage; for payments, value
  scales with $-processed → take-rate; mis-aligning pricing
  with value causes either undermonetization at scale (charging
  per-seat for a system that scales to 1000 users naturally)
  or customer-churn when value-perceived doesn't match invoice;
  Patrick Campbell / ProfitWell research repeatedly shows
  value-metric-alignment is the single largest pricing-design
  lever), per-seat-pricing-and-its-limits (per-seat is the most
  predictable for both customer (knows their monthly cost) and
  vendor (knows their MRR); works well for products with clear
  user-identity (CRM, design tool, project management); breaks
  down for products with high-non-named-user usage (an API
  consumed programmatically has no "user" to charge per-seat;
  a multi-tenant analytics tool used by 1 person to query
  100M records is underpriced per-seat); per-seat caps
  expansion revenue at user-count growth which may lag value-
  growth), usage-pricing-and-customer-budget-friction (usage-
  based aligns vendor revenue with customer value at scale but
  introduces budget-uncertainty for customers — most enterprise
  procurement processes require known annual spend, which
  usage-based prices fight; the recovery is committed-spend
  contracts (AWS Reserved, Twilio committed-use) that give
  budget certainty in exchange for discounts; usage-based also
  creates a customer-success cost — small-customer overages
  can be a 30-50% churn cause without proactive monitoring),
  flat-tiered-pricing-and-simplicity-premium (flat tiers
  (Basic / Pro / Enterprise) are simplest for the customer to
  understand and the lowest-friction to purchase; but the
  tiering must map to clear customer-segments — if all
  customers want roughly the same features, tiers cause
  decision-paralysis rather than segmentation; the right number
  of tiers is 3 (canonical), occasionally 4; 5+ tiers signal
  the company hasn't decided who they're for), freemium-vs-
  free-trial-PLG-funnel-tradeoffs (freemium = forever-free
  tier with paid upgrade path; free-trial = time-limited
  full access; freemium acquires more users but converts at
  1-5% to paid; free-trial converts at 10-30% but acquires
  fewer; freemium is right when (a) free-tier creates network
  effects or distribution (Slack, Dropbox), (b) the paid
  features are clearly differentiated for power users; freemium
  is wrong when (a) the support cost of free users exceeds the
  paid-conversion value (Atlassian famously moved off freemium
  for low-tier products), (b) the free tier cannibalizes paid
  rather than acquiring; PLG = Product-Led-Growth motion
  where the product itself drives acquisition and conversion;
  PLG demands extreme product polish on the free experience
  and instrumented activation metrics, which is a build-cost
  most early-stage products underestimate), price-anchor-and-
  raising-prices-as-load-bearing-move (founders systematically
  underprice early — partly from imposter syndrome, partly from
  fear-of-losing-deals, partly because the first customers
  optimize on price-not-value; the typical recovery pattern is
  10-30% price increases every 12-18 months as the product
  matures, with grandfathering for early customers; founders
  who never raise prices leave significant revenue on the
  table, which compounds because pricing-as-anchor sets all
  subsequent customer expectations), enterprise-pricing-and-
  list-price-vs-actual-discount (B2B enterprise customers
  expect to negotiate; list price is the anchor, actual price
  is typically 20-40% off list with multi-year commits, plus
  procurement adds standard requirements (SOC 2, security
  questionnaires, payment terms, MSA negotiation); founders
  moving from PLG-self-serve to enterprise are surprised by
  the 3-6-month sales cycle and the discounting expectation;
  the recovery is to bake discount expectation into list-price-
  setting from the start — quote list at 1.3-1.5x desired-
  realized-price).
- **Sample situations**:
  - "B2B SaaS for sales teams, $40k MRR, currently per-seat
    at $30/user/month. Customers asking for usage-based
    options because they have many infrequent users.
    Re-price, add usage tier, or stay per-seat?"
  - "Developer-tools API, charging per-API-call at $0.001.
    Customers complaining about budget unpredictability.
    Add committed-spend tier with discount, flat-tier
    pricing, or per-developer-seat model?"
  - "Pre-launch B2C consumer SaaS. Considering freemium
    forever-free with $10/mo Pro vs 14-day-free-trial then
    $10/mo. What changes the choice — current marketing
    channel, expected viral mechanics, paid-feature
    differentiation?"

## 10. Bring on first employee vs contractor vs offshore (cost, equity-pool, cultural-foundation)

- **Scope**: Founder hiring beyond the founding team is deciding
  the structure of the second-or-third hire (after decision 7
  established W-2 vs 1099 frameworks for the first). Decision
  spans (a) US-W-2 employee at full loaded cost ($150-200k+
  effective for $130k base in a typical metro), (b) US-1099
  contractor for bounded engagements (limited by decision 7's
  ABC test), (c) offshore contractor via direct hire or via
  EOR/Employer-of-Record service (Deel, Remote, Velocity Global),
  (d) offshore W-2-equivalent via EOR for compliance, (e) part-
  time / fractional (commonly used for first marketing /
  finance hires), (f) interns / co-op students for time-bound
  project work. Decision spans cost arithmetic, equity-pool
  consumption rate (every US hire dilutes founders 0.1-2.0%
  from the option pool), cultural-foundation effects (early
  hires shape company culture in load-bearing ways), and
  liability exposure (offshore EOR shifts liability to EOR;
  direct offshore exposes the company to local labor law).
  Distinct from decision 7 (first hire's W-2-vs-1099
  classification) and decision 11 (departure of any of these
  hires). Cross-routes `personal-finance` (equity grants
  consume the option pool and dilute founders progressively;
  each grant requires 409A valuation update), `legal-disputes`
  (offshore-direct-contractor without EOR creates labor-law
  exposure in worker's country — Brazil, India, EU member
  states have aggressive worker-protection regimes), `health-
  insurance` (each US W-2 hire may trigger small-group plan
  eligibility transitions — boundary `health-insurance`
  decision 1).
- **Framing-axes-covered**: equity-pool-burn-rate-and-cap-table-
  projection (option pool typically set at 10-20% at first
  priced round; engineer hires typically get 0.1-1.5% (senior
  vs mid vs junior, and pre-seed vs Series A); each hire eats
  pool, and pool is refreshed at each round but at the cost
  of additional dilution to existing holders; founders need
  to model 3-year pool-burn against hiring plan, and recognize
  that under-granting early hires creates retention risk that
  costs more than the equity saved), offshore-direct-vs-EOR-
  vs-staffing-agency (offshore direct = pay contractor in
  USD via Wise / Payoneer / similar, expose company to local-
  jurisdiction labor law if relationship looks employee-like;
  EOR = third-party employs the worker locally and bills the
  company, EOR handles local taxes / benefits / labor-law
  compliance, typical EOR cost $300-700/employee/month on top
  of salary; staffing-agency = managed service with team-of-
  contractors, higher markup but lower management burden;
  the EOR option (Deel, Remote, Velocity Global, Globalization
  Partners) is the right answer for most non-trivial offshore
  hires — direct without EOR works for true short-term
  bounded engagements but breaks for long-term hires in
  worker-protection-strong jurisdictions), cultural-foundation-
  effects-of-first-5-hires (early hires set baselines for
  performance expectations, communication style, decision-
  making norms, and "what good looks like" that persist for
  years; hiring early for cultural-foundation considerations
  beyond skill-match is load-bearing — a brilliant
  technically-strong-but-culturally-toxic hire in the first 5
  can durably damage the company; the recovery is slower than
  expected because early-employees have founder-adjacent
  authority by association), part-time-or-fractional-as-
  bridge-to-full-time (fractional CFO / CMO / Head-of-
  Engineering at 5-20 hours/week is increasingly common for
  early-stage companies that need senior expertise but can't
  afford full-time at FAANG-level comp; fractional has higher
  hourly rate but bounded total cost and faster onboarding;
  the trade-off is that fractional executives have other
  clients and limited bandwidth for crisis-time scaling;
  appropriate for first finance/marketing/HR hires, less
  appropriate for engineering or product where deep-product-
  context is critical), loaded-cost-of-US-W2-vs-offshore-EOR
  (typical US W-2 senior engineer in HCOL: $180k base +
  $30k equity-grant amortized + $25k benefits-and-employer-
  tax loading = $235k+ effective; same role offshore via EOR
  in Eastern Europe / Latin America: $80-130k base + EOR
  $500/mo = $90-140k all-in; the savings are 30-60% and the
  talent pool is large for software engineering specifically;
  the cost in collaboration is real (timezone, language-
  precision, async-by-default workflow requirements) but
  often overstated for well-run remote teams), 409A-valuation-
  update-cost-and-frequency (each material event (priced
  round, significant new revenue contract, hire of senior
  exec) can trigger a 409A re-valuation requirement;
  routine annual update at $1-2k via Carta / Shareworks /
  Pulley is standard; pricing options below FMV creates
  income at vest plus 20% penalty as in decision 7; the
  founder hiring 3+ employees per year should bake annual
  409A into operating cost), reference-check-and-back-channel-
  diligence-as-asymmetric-leverage (back-channel reference
  checking (calling people not on the reference list but
  who worked with the candidate) is the highest-leverage
  hiring tool and is almost universally skipped at early
  stage due to discomfort; pattern-matching on subtle
  reference signals (hedge language, what isn't said,
  reluctance to take the call) catches the cultural-toxicity
  cases that formal interviewing misses; founders sourcing
  through their network have a structural advantage on this
  axis vs founders sourcing through cold inbound).
- **Sample situations**:
  - "Just closed seed round, $2M raised, 18 months runway,
    hiring plan calls for 5 engineers in next 12 months. Mix
    of US-W2 senior + offshore-EOR mid-level for cost-savings,
    or all US-W2 for culture-and-collaboration?"
  - "Need a fractional CFO for board-reporting and financial
    modeling before Series A. Fractional at $400/hr for
    10 hrs/month, or hire junior FP&A full-time at $90k?"
  - "First three engineering hires went well but slow. Fourth
    hire has stronger technical resume but two back-channel
    references mentioned 'difficult to work with' and 'opinionated
    in unproductive ways'. Hire anyway, pass, or push for trial
    period?"

## 11. Co-founder departure / cap-table-buyback / dispute resolution (the structural breakup decision)

- **Scope**: A founder is leaving the company — voluntarily
  (resignation, personal reasons, opportunity elsewhere),
  involuntarily (fired by the board or remaining co-founders),
  or via dispute that escalates to a forced separation. Decision
  spans (a) the vesting calculation at departure (what's vested
  per the agreement, what's unvested and returned to the
  company), (b) the buyback of any vested equity (company has
  right of first refusal under most standard agreements; price
  is fair-market-value per 409A or per term-sheet formula),
  (c) the IP-assignment and non-compete posture (IP must be
  fully assigned and confirmed; non-compete enforceability
  varies sharply by state — CA does not enforce non-competes
  for employees, recent FTC rule attempted broader ban, status
  of FTC rule changing — verify current status), (d) severance
  / settlement structure (departing founder may negotiate
  acceleration, severance pay, or cash buyback of vested
  shares; the company may demand release of claims), (e) board
  / advisor transition (if departing founder was a board
  member, their seat must be transitioned per the certificate
  of incorporation / bylaws). Distinct from decision 1 (the
  up-front structuring of co-founder relationship) — here the
  structure is being unwound. This is among the highest-stakes
  decisions in entrepreneurship not because dollars are large
  (sometimes they are, often they aren't) but because
  procedural-and-emotional missteps create cascade failures
  — angry departing founders can damage company through
  customer-poaching, employee-poaching, IP-disputes, social-
  media airing, and litigation; well-structured departures
  preserve relationship and minimize ongoing risk. Cross-
  routes `legal-disputes` heavily (any departure with disputed
  facts (was it for-cause, was the trigger met, is the
  acceleration earned) raises litigation risk; non-compete
  enforcement varies sharply by state — boundary
  `legal-disputes`), `personal-finance` (departing founder
  needs to manage retirement-account rollover from any
  company plan, COBRA vs ACA decision for health insurance,
  Roth-conversion-window in the post-departure low-income year
  — boundary `personal-finance` decision 7 and decision 3 in
  this file).
- **Framing-axes-covered**: vested-vs-unvested-at-departure-
  arithmetic (per standard 4/1 vesting: at month 12 cliff,
  25% vests instantly; thereafter monthly vesting of 1/48 per
  month; departing founder at month 18 has vested 18/48 =
  37.5%; remaining 62.5% unvested returns to the company;
  acceleration provisions may add up to additional vesting
  based on (a) double-trigger acceleration on M&A + involuntary
  termination, (b) for-cause vs without-cause distinction in
  the agreement, (c) "good reason" trigger if departing founder
  was constructively terminated; the vesting calc is
  load-bearing and a fertile dispute ground), company-buyback-
  rights-and-fair-market-value-determination (most founder
  agreements give the company right of first refusal to
  buy back vested shares at departure at fair-market-value
  (defined per 409A or by formula); the FMV determination is
  contestable — recent 409A may be stale, recent priced round
  changes math, departing founder may dispute the formula; if
  company exercises ROFR the departing founder gets cash for
  shares; if company waives, departing founder retains shares
  subject to standard transfer restrictions in the
  certificate of incorporation), for-cause-vs-without-cause-
  termination-and-vesting-impact (most agreements distinguish:
  for-cause termination (fraud, willful misconduct, material
  breach of agreement, conviction of felony) may forfeit
  unvested AND vested shares per agreement; without-cause
  termination preserves vested per schedule; "good reason"
  resignation (material reduction in role, geographic
  relocation forced, material reduction in comp) may trigger
  same protections as without-cause termination; the "for
  cause" definition is the load-bearing legal text and is
  often left vague in early-stage agreements, creating
  dispute ground later), non-compete-enforceability-by-state-
  and-FTC-rule-status (CA Business and Professions Code
  §16600 voids non-competes against employees with narrow
  exceptions (sale-of-business, dissolution of partnership);
  NY, MA, IL, WA have varying restrictions (income thresholds,
  notice requirements, garden-leave requirements); TX, FL, GA
  enforce non-competes more liberally with reasonable-
  geographic-and-time-scope requirements; the FTC issued a
  rule in 2024 broadly banning non-competes nationally;
  status of rule is in litigation and the operative state at
  any given moment requires verification; founders entering
  separation should NOT rely on non-compete enforceability
  without state-specific employment-law-attorney review),
  IP-assignment-confirmation-and-trailing-IP (the CIIAA from
  decision 1 governs ongoing IP assignment; departure does not
  unwind prior assignments but creates risk if departing
  founder developed IP near departure that wasn't formally
  assigned, or claims pre-existing prior-art that wasn't
  carved out at start; the recovery is a separation
  agreement with explicit IP-confirmation and warranty of
  no-trailing-IP claims, with consideration (typically the
  buyback payment or severance) acting as consideration for
  the warranty), severance-and-release-of-claims-as-mutual-
  insurance (severance pay (a few months of comp typically)
  in exchange for general release of claims is standard
  mutual-insurance: departing founder gets cash bridge,
  company gets release from wrongful-termination /
  discrimination / wage-claim exposure; release should be
  bilateral where possible; ADEA-protected employees (age
  40+) have 21-day-consider / 7-day-revoke statutory rights
  on release that can't be waived), customer-and-employee-
  poaching-restrictions (non-solicit covenants for customers
  and employees are more broadly enforceable than non-
  competes — even CA enforces narrow non-solicit; reasonable
  scope is 12-24 months and named-customer-list rather than
  broad-market; the departing-founder-poaches-customers
  scenario is among the most common company-killing post-
  departure events; well-structured separation includes
  reasonable non-solicit with consideration to make it
  enforceable), board-seat-transition-and-shareholder-
  voting (if departing founder held a board seat, the seat
  must transition per the certificate of incorporation —
  may be remaining-founder-elected, board-elected, or
  vacant; if departing founder held majority-voting-shares,
  the buyback or restructure can shift control to remaining
  founders — major strategic event that may trigger
  investor-consent provisions; this is among the most
  procedurally complex separation scenarios), professional-
  referral-trigger (any departure involving (i) > 10%
  equity changing hands, (ii) disputed facts about for-
  cause / good-reason, (iii) prior-IP or trailing-IP
  claims, (iv) non-compete enforcement question, (v)
  customer-or-employee-poaching risk warrants startup /
  employment-law attorney engagement on both sides; the
  cost ($5-25k typical for a clean separation, $50k+ if
  contested) is small relative to the company-impact of a
  badly-handled departure).
- **Sample situations**:
  - "Co-founder is leaving at month 22 of a 4-year vest.
    They're vested 22/48 = 46%. They want to walk with
    their shares. Standard agreement gives company ROFR
    at FMV per most-recent 409A ($1.20/share). They argue
    recent customer contract should bump FMV. Buy them out
    at $1.20, negotiate higher, or let them keep shares?"
  - "Co-founder is being asked to leave by remaining founders
    + board for performance reasons. Agreement doesn't
    define 'for cause' clearly — it lists fraud and felony
    but not performance issues. They're refusing to sign
    separation without acceleration. Engage employment
    counsel both sides, structure mutual release with
    partial acceleration, or push through unilaterally?"
  - "Co-founder quit 4 months ago. Now we discover they're
    pitching investors on a directly-competing company
    using insights they got from our customer interviews.
    Their non-compete is unenforceable in CA. What's our
    actual recovery — trade-secret claim under DTSA,
    customer non-solicit if it's in the agreement,
    something else?"

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the
  axes above cluster into ~10-12 reusable framings —
  vesting-as-retention-and-fairness-mechanism, dilution-
  arithmetic-across-rounds, day-job-fallback-option-value-
  decay, self-employment-tax-vs-S-corp-payroll-arbitrage,
  SAFE-vs-priced-equity-instrument-design, liability-shield-
  and-corporate-veil, ABC-test-and-misclassification-exposure,
  retirement-vehicle-and-backdoor-Roth-interaction, pricing-
  as-value-metric-alignment, hiring-equity-pool-burn-and-
  cultural-foundation, departure-and-non-compete-and-IP-
  preservation. These framings will become Layer 2 entries
  with mental-model summaries, characteristic vocabulary,
  and explicit "excludes" lists that seed Layer 3 blindspots.
- **Blindspot anchors** (forward-pointer to `blindspots.md`):
  decisions 1, 3, 5, 7, 11 are highest-density — 83(b)-
  election-window-miss (1), day-job-IP-assignment-on-
  moonlight (3), post-money-cap-arithmetic-surprise and
  QSBS-clock-doesn't-start-on-SAFE (5), CA-AB-5-PAGA-
  misclassification-stack (7), non-compete-enforcement-by-
  state-with-changing-FTC-rule and IP-trailing-claim-on-
  departure (11) are frequently miscalibrated even among
  technically-competent founders. Decision 5's QSBS-clock-
  on-SAFE has the highest single-dollar tail risk per
  mis-step at a successful exit.
- **Cross-domain edges**: 1, 2, 3, 4, 5, 8 boundary
  `personal-finance` (83(b) election timing on founder
  stock; retirement-vehicle selection cascading from S-corp
  election; QBI Section-199A pass-through; QSBS Section-
  1202 5-year-hold timing; backdoor-Roth pro-rata complication
  with SEP-IRA balance); 1, 3 boundary `tech-career`
  (CIIAA carve-out from prior W-2 employer; day-job-IP-
  assignment on moonlight work; golden-handcuffs RSU
  cliff cost of leap); 1, 7, 11 boundary `legal-disputes`
  (founder dispute litigation; worker-misclassification
  PAGA exposure; IP-assignment / non-compete / non-solicit
  enforcement); 3, 7 boundary `health-insurance` (loss of
  employer coverage on leap, ACA vs spousal vs COBRA;
  small-group plan eligibility on first W-2 hire); 3
  boundary `housing` (HELOC / cash-out-refi as bridge
  capital must be originated pre-leap; mortgage-
  qualification with 1099 / S-corp distribution income).
  Edges are documentation; routing across edges is V2-
  Triage's job.
- **High-stakes posture** (selective rather than uniform):
  `entrepreneurship` is `high_stakes: false` per
  `_meta_ontology.md` §6 — failure is the modal outcome and
  generally survivable; Mechanism E uniform deferral is
  NOT applied. The Editor layer should NOT blanket-defer
  every decision to a professional. Selective referral is
  warranted for: decision 1 (founder-IP-and-equity-disputes
  — startup attorney with founder-side experience), decision
  4 (S-corp election with multi-state nexus or SSTB
  phaseout positioning — CPA experienced with S-corp
  reasonable-salary and §199A), decision 5 (SAFE-to-priced-
  seed conversion or any priced round — startup attorney),
  decision 7 (first W-2 employee in ABC-test-strict state
  or any misclassification dispute — employment-law
  attorney), decision 8 (high-leverage retirement-vehicle
  selection coupled with S-corp election — CPA with
  retirement-plan experience), decision 11 (any disputed
  departure with > 10% equity at stake or non-compete /
  non-solicit / IP-trailing claim — both startup and
  employment-law counsel; consider engaging counsel on
  BOTH sides for clean separation). The posture remains
  "decision-support framing rather than professional advice";
  the Editor surfaces the appropriate specific category
  inline rather than blanket-mandating one on every
  decision. Over-referral degrades signal; under-referral
  on the high-tail-risk decisions creates harm. State Bar
  / FINRA / disciplinary-record verification on any
  individual professional recommended is the $0-friction
  procedural floor — surfaced on every individual-
  professional referral. This selective-referral posture is
  the calibration that distinguishes `entrepreneurship` from
  the uniformly-Mechanism-E-gated `personal-finance` /
  `health-insurance` / `immigration` / `family-planning` /
  `legal-disputes` domains.
