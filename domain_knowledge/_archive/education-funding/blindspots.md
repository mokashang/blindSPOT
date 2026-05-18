# education-funding — blindspots.md (Layer 3)

Blindspot catalogue for `education-funding`. Each entry names what a
real practitioner in the relevant framing would say is missed — anchored
to either an `Excludes` line in [`framings.md`](./framings.md) or to a
cross-decision edge in [`decisions.md`](./decisions.md). Per
[`_schema.md`](../_schema.md), every entry is relative to a framing and
ships with a trigger pattern and a concrete recovery move.

The `education-funding` domain is **high_stakes: false** per
[`_meta_ontology.md` §7](../_meta_ontology.md) — most decisions are
slow-clocked and reversible on multi-year horizons (refinance back to
a better rate, switch IDR plans, transfer 529 beneficiary, defer
enrollment, take a leave of absence, file appeals, redo FAFSA in a
subsequent year). The two genuine irreversibility traps inside the
domain are (a) **federal-to-private refi**, which permanently erases
IDR / PSLF / SAVE / death-and-disability discharge under HEA §437(a) /
Borrower Defense under HEA §455(h) / in-school deferment — there is no
re-federalization path; and (b) the §529(c)(2)(B) **5-year-forward
election** on front-loaded 529 contributions, where Form 709 filing
errors propagate forward and a death within the 5-year window claws
back the unspent portion into the donor's estate. Outside those
pockets and the analogous six-figure tail-risk pockets enumerated in
[`decisions.md` §Notes](./decisions.md) — D4 IDR + tax-bomb sinking-
fund design, D7 Parent PLUS / private cosigner mechanics, D10 PSLF
qualifying-employment + employment-certification + Buyback — the
Editor posture is decision-support framing rather than uniform
Mechanism E deferral.

This mirrors the [V2 §4 Mechanism E partial-gating posture](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)
already encoded by [`housing/blindspots.md`](../housing/blindspots.md)
(PR #64) and [`entrepreneurship/blindspots.md`](../entrepreneurship/blindspots.md)
(PR #83). Recovery moves below route to a **named professional channel
only on the six-figure tail-risk pockets D1 / D3 / D4 / D7 / D10** —
student-loan attorney, Student Loan Borrower Assistance Project
(SLBA) / National Consumer Law Center, FSA Ombudsman Group,
retirement-experienced CPA with §25A / §127 / §529 / SECURE 2.0 §126
history, fee-only fiduciary CFP (NAPFA-affiliated, AUM-free), NACAC-
member counselor / high-school college-counseling office. For routine
decisions (D2 graduate-school ROI, D5 school-choice with merit aid,
D6 vehicle-mix outside the leftover-529 / parental-retirement-
priority tail, D8 FAFSA / CSS positioning outside the divorced-parent
or business-asset reporting tail, D9 employer §127) Recovery moves
are self-directed and educational — the user is treated as a
decision-capable adult navigating slow-clocked financial choices.
Over-referral degrades signal; under-referral on the irreversible
or large-tail-risk decisions creates harm.

Each blindspot lists:
- **Statement** — one sentence naming what the asker believes or will
  default to
- **Source-evidence** — the framing-Excludes anchor or decision cross-
  edge this blindspot was extracted from (not invented); statutory
  anchors where applicable
- **Trigger** — the situation pattern the Triage / Risk Officer should
  match against
- **Failure-mode** — the specific bad outcome with dollar / time /
  status implications
- **Recovery-move** — the concrete action that resolves it, with
  named professional-channel referral inline only where the decision's
  tail risk justifies it

The framing names below match [`framings.md`](./framings.md) exactly;
all 14 are covered with ≥ 5 entries each (≥ 70 total). Voice anchors
are conceptual — the source-views in
`domain_knowledge/education-funding/sources.yaml` are not yet
authored, so attribution is to the *class* of community
(r/PSLF / r/StudentLoans / r/StudentLoansHelp, Heather Jarvis Student
Loan Expert / SLBA / NCLC, SavingForCollege / Mark Kantrowitz / The
College Investor, Mike Piper / Bogleheads-college, Mr. Money
Mustache / r/financialindependence / ChooseFI, NACAC / NASFAA / high-
school college-counseling offices, r/financialaid /
r/ApplyingToCollege, NAPFA-affiliated fee-only CFPs, MBA-admissions /
Poets&Quants / Wall Street Oasis, Levels.fyi / Blind /
r/cscareerquestions, CFPB / SLBA / state-AG consumer-protection,
NACBA bankruptcy attorneys / post-2022 DOJ-USDOE-attestation-
guidance voice, HELOC-as-college-funding voice cross-routing
`housing`). When `sources.yaml` lands, source-evidence lines below
should be tightened to specific source-view ids.

Cross-domain edges flagged inline per entry where relevant —
`personal-finance` (529-vs-Roth ordering, asset location across
529 / Roth / taxable / UGMA-UTMA / Coverdell, kiddie-tax §1(g),
SECURE 2.0 §126 529-to-Roth rollover, retirement-account-exclusion
from FAFSA / CSS, Roth-conversion-in-low-income-year as tax-bomb-
bracket-management), `tech-career` (full-time-MBA-ROI on engineering
tracks, MS-CS at top-10 as H-1B-cap-exempt-master's-cap route, §127
employer tuition reimbursement retention-clawback as golden-
handcuffs), `entrepreneurship` (1099-vs-W-2 PSLF asymmetry — only
W-2 employment at a qualifying employer counts, self-employed
contractor at a 501(c)(3) does NOT, this is one of the most-missed
PSLF mechanics for former-contractor founders; S-corp salary-vs-
distribution affecting AGI / FAFSA EFC; LLC-as-parent for 529-
front-loading estate-planning), `family-planning` (529 inter-
generational gifting, grandparent-529-FAFSA-post-simplification
removed trap, UGMA/UTMA basis transfer, divorced-parent-of-record
under FAFSA Simplification Act, custodial-account drag), `housing`
(HELOC-as-college-funding-alternative, cash-out-refi-vs-Parent-PLUS,
primary-residence non-reportable on FAFSA but reportable on CSS
Profile at many schools), `immigration` (international-student MS-CS
calculus, F-1 / J-1 status interactions with 529 / federal-aid
eligibility, F-1 ineligible for federal-Direct-aid). Routing across
edges is V2-Triage's job; the edge annotations here help future
`sources.yaml` and `communities/*.md` authors name the adjacent
domains.

---

## F1 — Federal-optionality-as-embedded-put-option framing

### 1.1 "Never refi federal" treated as universal heuristic even when option-value is genuinely zero

- **Statement**: The asker believes the PSLF / IDR / death-and-
  disability / Borrower-Defense optionality bundled with federal
  loans is always worth more than any private-refi rate spread, so
  refinancing is always wrong.
- **Source-evidence**: [`framings.md` F1 first Excludes bullet](./framings.md) —
  "Frames every federal borrower as having latent option value even
  when the realistic option-exercise probability is near zero
  (high-income tech worker with stable career, no public-service or
  grad-school plausibility, no household-disability risk)." Opposes
  F4 (rate-spread-arithmetic). Decisions.md D1 cross-edge — "rough
  community heuristic is 'do not refi federal if there is any
  plausible PSLF path or any household member with elevated
  disability risk'".
- **Trigger**: Asker holds federal loans, top-quartile professional
  comp at a for-profit employer (FAANG-tier comp, BigLaw associate,
  IB / MBB / Big 4 consulting), no public-service or graduate-school
  plausibility, no household-member-disability indicator, no
  expressed openness to nonprofit pivot — AND quotes the "never refi
  federal" reflex without an explicit option-value calculation.
- **Failure-mode**: Borrower stays on federal at 7.5% weighted-avg
  while SoFi offers 5.25% fixed for a 760+ FICO / $280k AGI tech
  worker; $4–5k/year of interest expense / ~$25–35k over typical
  5-7 year accelerated pay-off horizon is left on the table to
  hedge optionality whose probability-weighted value is < $1k/year
  for this profile.
- **Recovery-move**: Surface F4 (rate-spread-arithmetic) explicitly
  and walk through the option-exercise probability calculation for
  this specific borrower (PSLF path probability × 10-year forgiveness
  value + disability path probability × discharge value + grad-school
  path probability × in-school-deferment value + IDR-forgiveness
  path probability × tax-adjusted forgiveness value). For borrowers
  in this profile with a $150k+ balance considering refi to a
  private lender — D1 is the federal-to-private one-way door —
  **route to a student-loan attorney or SLBA** for the option-value
  audit before the refi closes. Re-federalization is not available.

### 1.2 SAVE current-status treated as a permanent IDR feature when it is in administrative forbearance

- **Statement**: The asker references SAVE's 5%-discretionary-income
  cap on undergrad and interest-non-accrual subsidy as the operative
  IDR baseline for refi-vs-stay-federal comparison or for long-
  horizon IDR-forgiveness planning.
- **Source-evidence**: [`framings.md` F1 second Excludes bullet](./framings.md) —
  "Treats SAVE-current-status as if it were a permanent feature when
  it's currently in administrative forbearance under the 8th Circuit
  injunction, with months counting for PSLF but NOT for IDR-
  forgiveness." Reinforced in F12 Excludes (SAVE-administrative-
  forbearance). Statutory anchor: HEA §455(d), 8th Circuit SAVE
  injunction (2024).
- **Trigger**: Asker mentions SAVE by name as the IDR plan they are
  on or planning around, OR references the 5% undergrad
  discretionary-income cap and interest-subsidy without
  acknowledging the litigation-induced forbearance status.
- **Failure-mode**: Borrower plans a 20-year IDR-forgiveness path
  assuming SAVE-mechanics continue; the SAVE plan is rolled back or
  materially altered before the borrower reaches forgiveness; the
  borrower discovers years of forbearance months counted for PSLF
  but NOT for IDR-forgiveness — payment-count timeline slips from
  year 20 to year 22–23 once accounts re-baseline, and the interest-
  subsidy retroactively reverses (5-figure balance growth).
- **Recovery-move**: Re-anchor on a non-SAVE IDR plan (IBR for
  post-2014 borrowers, PAYE for those with PAYE-grandfathering, or
  the post-injunction IDR baseline once finalized). Pull a current
  payment-count from StudentAid.gov "PSLF & TEPSLF Certification &
  Application" via the PSLF Help Tool. Document expected
  forgiveness-year arithmetic under at least two IDR scenarios
  (current-administration + alternative-rulemaking) before the refi
  decision. For PSLF-path borrowers, the SAVE-forbearance months
  count for PSLF — confirm via Employment Certification Form (ECF)
  refresh. Cross-edge to D10.

### 1.3 Political-risk on federal-loan-program features treated as systemic when historical change has been net-positive for low/mid-income borrowers

- **Statement**: The asker uses "the federal-loan-program rules can
  change" as a generic reason to refinance OUT of federal — but
  doesn't distinguish *changes that cut against* the borrower from
  *changes that cut in favor of* the borrower (the 2022 one-time
  forgiveness wave, the 2022-2024 account-adjustment that captured
  millions of qualifying payments, SAVE's 5%/225%-poverty
  mechanics when it was active, Borrower Defense relief cohort
  expansion).
- **Source-evidence**: [`framings.md` F1 third Excludes bullet](./framings.md) —
  "Under-weights the political-risk dimension: federal-loan-program
  features ... are subject to administrative-rule changes and
  statutory amendments." Tension with F12 first Excludes bullet —
  political-risk has been net-positive for low-and-middle-income
  borrowers historically. Decisions.md D1 cross-edge.
- **Trigger**: Asker cites "political risk" or "the rules can change"
  as the primary reason to refinance federal-to-private, WITHOUT
  modeling specific change-scenarios on either side of the ledger.
- **Failure-mode**: Borrower refis out of federal at a $200bp spread
  to hedge generic political risk, then misses a $20k+ payment-
  count adjustment in their cohort that would have made PSLF or
  IDR-forgiveness arithmetic land more favorably; the political risk
  cut *in their favor* but they had already burned the federal
  bundle and cannot re-federalize.
- **Recovery-move**: Build an explicit two-sided political-risk
  table (favorable rule changes 2018-2024: payment-count adjustment,
  one-time forgiveness, SAVE mechanics when active, Borrower Defense
  expansion, ARPA tax-bomb exclusion; unfavorable rule changes:
  SAVE injunction, ARPA cliff at end-2025 absent extension, IDR
  payment recertification timing under rulemaking churn). Decide on
  the net direction *for this borrower's profile* before the refi.
  For borrowers with documented forbearance-steering history (2010-
  2018 Navient / FedLoan era), surface the **FSA Ombudsman Group**
  as a $0-cost escalation channel to claim the account-adjustment
  before refi closes the channel; cross-edge to D10 and to F9
  (consumer-protection).

### 1.4 Behavioral cost of holding non-amortizing IDR balance for 20+ years under-priced

- **Statement**: The asker computes "stay on IDR for 20 years to
  forgiveness" as a pure arithmetic comparison vs the 10-year
  standard payment, without pricing the psychological drag of
  watching the balance grow on every servicer statement.
- **Source-evidence**: [`framings.md` F1 fourth Excludes bullet](./framings.md) —
  "Doesn't price the *behavioral* cost of holding a federal balance
  for 20+ years at non-amortizing IDR — the balance grows on paper,
  servicer statements show the running interest accrual, and
  borrowers report psychological drag from 'the balance going up
  every month even though I'm paying.'" Opposes F4. Reinforced by
  r/StudentLoans community voice — recurring "I can't sleep with
  this balance" posts.
- **Trigger**: Asker on IDR for 3+ years with balance higher than
  origination amount due to interest accrual, AGI in the $80-150k
  range where 10-year-standard would be uncomfortable but possible,
  AND expresses anxiety or shame about the balance trajectory
  ("I've been paying for years and it's gone UP", "I feel like I'll
  never get out from under this").
- **Failure-mode**: Borrower stays on IDR planning to forgive at
  year 20, but at year 5-7 abandons the plan in a moment of
  psychological exhaustion, refis to private at whatever rate
  available, loses federal optionality, and ends up paying *more*
  total than either the original IDR plan OR a hybrid IDR-with-
  accelerated-principal strategy would have cost.
- **Recovery-move**: Name the behavioral cost as a real input, not
  a weakness — F1 framing acknowledges it as a load-bearing
  consideration. For borrowers in this psychological-distress
  pattern, model a *hybrid* strategy (stay on IDR for PSLF /
  forgiveness protection, but make additional principal payments
  when budget allows to keep the balance from growing — the IDR
  payment-count clock continues since IDR is the qualifying plan).
  For borrowers genuinely past the behavioral-tolerance threshold,
  surface that refi removes the optionality permanently and recommend
  a 6-month "decision-pause" before pulling the trigger. If the
  borrower has a $150k+ balance and is in active distress, **route
  to a fee-only fiduciary CFP** (NAPFA-affiliated, no AUM fee
  structure) for a comprehensive financial-plan review before
  refinancing.

### 1.5 Death-and-disability discharge under §437(a) over-counted as protection for family-member disability

- **Statement**: The asker treats §437(a) discharge as if any
  household-member disability triggers loan forgiveness, when in
  fact §437(a) requires the *borrower's own* total and permanent
  disability (TPD) certified by a physician, the VA, or 3+ years
  SSDI — and applies a 3-year post-discharge monitoring period.
- **Source-evidence**: [`framings.md` F1 fifth Excludes bullet](./framings.md) —
  "Frames death-and-disability discharge under §437(a) as if every
  family-member-disability triggers discharge; it actually requires
  the *borrower's own* total and permanent disability (TPD)
  certified by a physician, the VA, or 3+ years SSDI — not a spouse /
  child / parent disability." Reinforced in F13 Excludes (3-year
  monitoring period). Statutory anchor: HEA §437(a) and 34 CFR §685.213.
- **Trigger**: Asker cites "I have a spouse with [chronic illness] /
  parent in dementia care / child with autism, so I'm staying
  federal for the disability protection" as primary refi-vs-stay-
  federal reasoning.
- **Failure-mode**: Borrower over-weights the protection in the
  refi calculation, foregoes $3-5k/yr of rate-spread savings for
  protection that won't actually trigger on the family-member-
  disability they're worried about; if their own disability later
  occurs they would qualify, but the protection has been
  systematically miscounted for *years* in the meantime.
- **Recovery-move**: Re-state the §437(a) eligibility criteria
  explicitly — *borrower's* own TPD, certified by physician + VA +
  3-year SSDI, with 3-year post-discharge monitoring. Help the
  borrower re-do the refi calculation with the *correct* protection
  scope. Note that some private lenders (SoFi, Earnest) offer
  voluntary disability-discharge as a benefit but with much weaker
  terms; this is not equivalent. For borrowers in an actual
  disability-eligibility scenario, **route to a student-loan
  attorney or SLBA** for the TPD application process — improperly
  documented TPD claims are often denied on first review.

---

## F2 — 529-state-deduction-and-tax-deferral framing

### 2.1 State-deduction value over-weighted in states where the deduction is small or absent

- **Statement**: The asker defaults to "stay in-state for the
  deduction" without computing whether the marginal state-deduction
  value actually exceeds expense-ratio drag, investment-option
  quality, and beneficiary-flexibility considerations.
- **Source-evidence**: [`framings.md` F2 first Excludes bullet](./framings.md) —
  "Treats the 529 state-deduction as if it were the dominant
  consideration when for households in deduction-less states (CA,
  NJ, MA, several others) or with state-deduction caps below
  realistic contribution levels (IL $20k/MFJ, AZ $4k/MFJ), the
  deduction-arbitrage is small enough that expense-ratio drag and
  investment-option quality dominate." Statutory anchor: state
  529-deduction statutes (e.g. NY Tax Law §612(c)(32), IL 35 ILCS
  5/203(a)(2)(Y)).
- **Trigger**: Asker is in a no-deduction state (CA, NJ, MA, DE,
  HI, KY, ME, NC) OR a small-deduction state (AZ $4k MFJ, IL $20k
  MFJ, OH $4k single) AND defaults to "I'm using [in-state plan
  name]" without naming the deduction value or comparing expense
  ratios to Utah my529, Nevada Vanguard, or NY 529 Direct.
- **Failure-mode**: Family in California (zero state deduction)
  uses ScholarShare with 0.18% all-in expense ratio when Utah my529
  is 0.12% — over 18 years on a $200k portfolio, the 6bp drag
  compounds to ~$3-4k of foregone returns for zero deduction-arbitrage
  benefit. Alternatively, IL family caps the $20k MFJ deduction
  but contributes $40k/yr; the marginal $20k receives no deduction
  and is locked into Bright Start when Utah/Nevada have better
  investment options and lower fees.
- **Recovery-move**: Compute the explicit state-deduction value (deduction
  × marginal state bracket × annual contribution) and compare
  against the expense-ratio differential vs Utah my529 / Nevada
  Vanguard 529 / NY 529 Direct over the funding horizon. For
  no-deduction states, default to Utah my529 unless there's a
  specific investment-option reason. For small-deduction states,
  contribute up to the deduction cap in-state and route the
  marginal contribution to a better out-of-state plan if expense
  ratios warrant. Cross-edge to `personal-finance` (asset-location
  decision).

### 2.2 §529(c)(2)(B) 5-year-forward election treated as set-and-forget when Form 709 filing is the load-bearing mechanic

- **Statement**: The asker plans to use the §529(c)(2)(B) 5-year-
  forward election (lump-sum $95k single / $190k MFJ in 2026) but
  doesn't know Form 709 must be filed in the election year even
  though no gift tax is owed; failure to file means the contribution
  isn't formally elected and any death within the 5-year window
  causes the unspent portion to claw back into the donor's estate.
- **Source-evidence**: [`framings.md` F2 second Excludes bullet](./framings.md) —
  "Doesn't see that the §529(c)(2)(B) 5-year-forward election
  requires Form 709 filing in the election year *even though no gift
  tax is owed* — this is the most-missed mechanic of the strategy;
  failure to file means the contribution isn't formally elected and
  death within the 5-year window causes the unspent portion to claw
  back into the donor's estate." Decisions.md D3 cross-edge.
  Statutory anchor: IRC §529(c)(2)(B), Form 709 instructions.
- **Trigger**: Asker (parent or grandparent) plans a 5-year-forward
  election contribution > annual gift-tax exclusion ($19k for 2026)
  in a single year AND does not mention Form 709 filing OR uses
  language like "I'll just write the check, the bank handles the
  paperwork" / "my CPA does my regular 1040, this should be fine".
- **Failure-mode**: Grandparent contributes $190k MFJ as 5-year-
  forward election; CPA doing standard 1040 prep doesn't know to
  file Form 709 (Form 709 is a separate gift-tax return outside the
  standard 1040 scope for most CPAs); grandparent dies in year 3 of
  the 5-year window; $76k unspent portion (years 4-5 of the ratable
  election) claws back into the estate at probate, with no charitable
  / education exclusion — the anti-purpose of the original strategy.
- **Recovery-move**: Confirm Form 709 filing is on the CPA's task
  list for the election year explicitly. Form 709 is due by the
  donor's regular 1040 deadline (April 15 with extension to
  October 15). Verify the CPA has §529 / §529(c)(2)(B) experience.
  For 5-year-forward elections > $100k single / $200k MFJ, or for
  grandparents using the 5-year election in conjunction with
  lifetime-estate-exemption planning (especially before the 2026
  TCJA sunset), **route to a retirement-experienced CPA with §25A /
  §127 / §529 history** specifically — NOT a generic 1040-prep CPA.
  Cross-edge D3, D6.

### 2.3 Leftover-529 problem under-priced when SECURE 2.0 §126 is treated as adequate flexibility hedge

- **Statement**: The asker treats SECURE 2.0 §126 (529-to-Roth
  rollover) as solving the "what if kid doesn't go to college"
  problem, when the $35k lifetime cap, 15-year clock, 5-year
  recent-contribution lockout, and beneficiary-earned-income
  requirement make it a narrow partial hedge rather than a general
  flexibility solution.
- **Source-evidence**: [`framings.md` F2 third Excludes bullet](./framings.md) —
  "Under-weights the leftover-529 problem: if the kid skips college,
  goes to a cheaper school, gets full-ride scholarships, or finishes
  early, the unspent 529 balance faces 10% penalty + ordinary-income
  tax on earnings unless rolled to a sibling beneficiary, used for
  K-12 ($10k/year cap), used for graduate-school later, or rolled to
  a Roth (SECURE 2.0 §126, capped at $35k lifetime with 15-year-
  clock)." Reinforced in F6 first Excludes (financial press oversold
  §126). Statutory anchor: SECURE 2.0 §126, IRC §529(c)(6) penalty
  on non-qualified distribution.
- **Trigger**: Asker plans heavy 529 contribution ($150k+ projected
  funding) and references SECURE 2.0 §126 as the "escape valve" for
  the leftover problem, OR is contributing late (kid is 10+ and
  funding is back-loaded) such that the 15-year-clock doesn't reach
  rollover-eligibility before realistic college-distribution timing.
- **Failure-mode**: Parent over-funds 529 to $240k by the time kid
  is 14; kid gets significant merit / need-aid and only $60k is
  needed for college; $180k of unspent 529 funds face 10% penalty +
  ordinary-income on earnings (typical 50%+ of balance for old
  529s) — call it $30k earnings × ~35% combined federal + state +
  10% penalty = ~$13.5k tax cost; the $35k rollover-to-Roth only
  partially solves the problem AND requires 5+ years of beneficiary
  earned-income to fully convert AND requires waiting until 5 years
  after the last contribution was made.
- **Recovery-move**: Right-size 529 funding to the realistic college
  cost (use College Scorecard net price calculators for likely
  schools, not sticker price) plus a 15-20% buffer; route additional
  savings to flexible vehicles (Roth IRA up to limit, taxable
  brokerage) rather than over-funding the 529. For families already
  over-funded, plan beneficiary-change to a sibling, plan for K-12
  $10k/year distributions if private-school is in play, and start
  the 5-year-no-contribution clock NOW so 529-to-Roth rollover is
  available at the 15-year anniversary. Cross-edge to F10 (FIRE-
  retirement-priority): for households already retirement-stressed,
  this is one of the highest-regret patterns.

### 2.4 State-deduction recapture rules on out-of-state rollover treated as edge case when they're common

- **Statement**: The asker assumes a 529 rollover from one state's
  plan to another's is tax-neutral, when most states with a 529
  deduction recapture the deduction on out-of-state rollover (NY,
  IL, NC, AR, IN, others); some allow tax-free in-state-to-in-
  state transfers but recapture on out-of-state.
- **Source-evidence**: [`framings.md` F2 fourth Excludes bullet](./framings.md) —
  "Glosses over state-deduction recapture rules on out-of-state
  rollover: most states with a 529 deduction recapture the deduction
  if you roll out to another state's plan." Statutory anchor:
  state-specific 529 recapture statutes (e.g. NY Tax Law
  §612(b)(40), IL 35 ILCS 5/203(a)(2)(Y)).
- **Trigger**: Asker took state-deduction in a recapture-state (NY,
  IL, NC, AR, IN, GA, MD, OK, OR, RI, UT, VT, WI) AND is
  considering rollover to Utah / Nevada / out-of-state plan for
  better expense ratio OR is planning to move to a new state and
  wants to consolidate.
- **Failure-mode**: NY family took $10k/yr MFJ deduction over 10
  years = $100k of deductions × ~6.85% NY marginal = ~$6,850 of
  cumulative state tax benefit. Rolls $200k from NY 529 to Utah
  my529 for the expense-ratio savings; NY recaptures the $6,850
  in the rollover year as additional NY taxable income — wipes out
  the entire expense-ratio savings for the next decade-plus.
- **Recovery-move**: Before any out-of-state rollover, compute the
  cumulative deduction-recapture liability (sum of all years'
  deductions × current marginal state rate) against the expense-
  ratio and feature savings. For most families in NY / IL / IN / GA
  / NC, the recapture liability exceeds the rollover benefit. For
  state-moves (changing residency), the recapture rules generally
  STILL apply — moving doesn't reset the recapture clock. Check
  the specific state's 529 statute for "qualified distribution"
  carve-outs (some allow rollover-to-new-state-of-residence
  without recapture). Cross-edge to `personal-finance` (asset
  relocation on state moves).

### 2.5 Grandparent-529 post-Simplification treated as universally superior when CSS Profile treatment is school-by-school

- **Statement**: The asker treats grandparent-529 as the dominant
  funding vehicle post-FAFSA-Simplification because grandparent
  distributions no longer count as student income — without
  checking that CSS Profile schools (~200 mostly-private institutions)
  often still count grandparent-529 distributions or balances.
- **Source-evidence**: [`framings.md` F2 fifth Excludes bullet](./framings.md) —
  "Frames grandparent-529 as if it were superior to parent-529
  post-FAFSA-Simplification across the board; in fact, grandparent-
  529 distributions are NOT reported as student income on the new
  FAFSA, but on the CSS Profile they often still are (depends on
  the school's CSS treatment)." Decisions.md D3 / D8 cross-edge.
  Statutory anchor: FAFSA Simplification Act of 2020 (effective
  2024-25 award year).
- **Trigger**: Asker references "grandparent 529 trap is gone" or
  "we shifted the 529 to the grandparent" AND the kid is applying
  to schools that include CSS Profile institutions (most highly-
  selective privates — Ivies, T20 LACs, Stanford, Duke, Vanderbilt,
  USC, etc.).
- **Failure-mode**: Family shifts $150k 529 from parent to grandparent
  expecting the post-Simplification benefit; kid is admitted to a
  CSS Profile school that still counts grandparent-529 distributions
  as student income at 50% drag — kid loses $25-30k of need-aid
  over 4 years because of the CSS treatment, wiping out the FAFSA-
  benefit assumption.
- **Recovery-move**: Before any parent-to-grandparent 529 transfer,
  build the target-school list and check each school's CSS Profile
  treatment of grandparent-owned 529 (some schools, like Princeton,
  explicitly exclude; others count distributions; others count
  balance). For mixed FAFSA-only-and-CSS school lists, keep the 529
  in parent's name OR plan grandparent distributions for the senior
  year only (CSS reports prior-prior-year for early years but the
  senior-year FAFSA is the last filed, so a grandparent distribution
  in the last year is past the CSS reporting window for most schools).
  Cross-edge to F5 (FAFSA-base-year), D8.

---

## F3 — ROI-by-major / program-not-school framing

### 3.1 Median earnings treated as the relevant statistic when distribution is highly skewed for the target program

- **Statement**: The asker uses published median earnings (College
  Scorecard, Burning Glass) as the dispositive ROI input for a
  CS / finance / consulting program — but the outcome distribution
  for these programs is bimodal (top-tier vs everyone-else), and
  the median understates the dispersion that determines actual ROI.
- **Source-evidence**: [`framings.md` F3 first Excludes bullet](./framings.md) —
  "Treats published median earnings as the relevant statistic when
  the distribution is highly skewed for many programs (CS, finance,
  consulting outcomes are bimodal — top-tier vs everyone-else)."
  Opposes F9 (consumer-protection-anti-debt). Decisions.md D2 cross-
  edge.
- **Trigger**: Asker references "MBA median comp is $X" or "CS
  median starting salary is $Y" as the ROI benchmark for a specific
  program decision, without distinguishing top-quintile / median /
  bottom-quintile outcomes or naming the specific recruiting funnel
  the program does or doesn't access.
- **Failure-mode**: Asker enrolls in a non-target MBA program
  expecting the "MBA pays $150k base + bonus" median that's actually
  a statement about top-10 programs feeding into MBB / BB-finance /
  FAANG-PM funnels; for non-target outcomes (typical $90-110k base,
  often regional), the program net-NPV is negative even before
  considering the 2-year opportunity cost.
- **Recovery-move**: Pull program-specific outcomes from College
  Scorecard (federally funded earnings data), the program's own
  employment report (especially MBA programs publish detailed CMO
  reports with sector / firm / comp breakdowns), and target-firm
  campus-recruiting lists (most BBs and MBBs publish their core
  recruiting school lists). Distinguish median / 25th-percentile /
  75th-percentile. For high-debt / bimodal-outcome programs (most
  MBA, CS at mid-tier, JD outside T14), model the realistic
  individual outcome distribution rather than the program median.
  Cross-edge to `tech-career` decision 1 (TC framing) and to F9
  (consumer-protection on for-profit / mid-tier privates with high
  CDR).

### 3.2 Non-vocational degrees treated as low-ROI when 20-year option-value via professional school is the right window

- **Statement**: The asker treats a humanities / social-science /
  liberal-arts undergrad as a low-ROI choice based on 4-year-post-
  graduation earnings — without considering the subset who pivot to
  law / medicine / consulting / business school where the lifetime
  earnings curve significantly out-performs the 4-year window's
  prediction.
- **Source-evidence**: [`framings.md` F3 second Excludes bullet](./framings.md) —
  "Doesn't surface the *option value* of a non-vocational degree —
  philosophy / English / history majors who go into law, consulting,
  or graduate school have outcomes that don't show up in 4-year
  post-graduation earnings data." Tension with `tech-career`
  framing on vocational specialization.
- **Trigger**: Asker (or parent of a high-school-senior asker) is
  pressuring a humanities-inclined student toward a vocational
  major (CS, engineering, business) using ROI arguments, or
  considering an in-state-flagship for a humanities major against
  a stronger liberal-arts program with the assumption that "the
  state school is fine for that major anyway".
- **Failure-mode**: Student is forced into a CS major they're not
  suited for, performs poorly, doesn't enter the high-ROI software-
  engineering track anyway, AND doesn't develop the writing /
  analytical skills that would have positioned them for law school
  / consulting / academic-research pivots. The opportunity cost of
  the forced major exceeds the assumed ROI savings.
- **Recovery-move**: Distinguish the *4-year-post-graduation*
  earnings window (where vocational majors dominate) from the
  *20-year* lifetime-earnings window (where the law / consulting /
  business-school pivot subset of humanities majors closes most of
  the gap and often surpasses it for top-program graduates). For
  humanities-inclined students, model the realistic professional-
  school pivot rate from their target undergraduate program — top
  liberal-arts colleges and Ivies have JD-bound pipelines at 25-40%
  of graduates; flagship publics have 5-10%. The program's
  professional-school pipeline often matters more than the major.

### 3.3 Conditional-on-completion medians ignored when 4-year-graduation-rate variance is the load-bearing risk

- **Statement**: The asker compares "engineering at flagship public
  out-earns liberal-arts at ranked-private" on median earnings,
  without noting that the flagship-public engineering 4-year
  graduation rate is often 50-65% vs 85-95% at ranked-privates —
  and the failure-to-complete cost (1-2 years of debt with no
  degree) is the highest-regret pattern in the lower-completion
  tail.
- **Source-evidence**: [`framings.md` F3 third Excludes bullet](./framings.md) —
  "Under-weights the *negative* selection in non-completion rates:
  the framing's 'engineering at flagship public out-earns liberal-
  arts-at-ranked-private' is true *conditional on completion*."
  Reinforced by College Scorecard published completion-rate data.
- **Trigger**: Asker is comparing a flagship-public engineering /
  CS / business program (especially at large publics with weeder-
  course attrition — Berkeley EECS, UIUC CS, UMich Engineering,
  Purdue, Texas A&M) against a ranked-private with higher
  completion AND is using median-earnings of completers as the
  relevant comparison.
- **Failure-mode**: Student enters flagship-public engineering with
  the median-earnings expectation; gets weeded out of the major in
  year 2; transfers to a non-target major at the same school;
  graduates in 5-6 years with debt sized to the original
  expectation and earnings closer to the new major's median (often
  $30-50k below the engineering-completer median). The conditional-
  on-completion assumption was load-bearing.
- **Recovery-move**: Pull both the program's median earnings AND
  the 4-year / 6-year completion rate, AND the within-major-
  retention rate (often available in institutional research /
  common-data-set publications). For high-attrition-major scenarios,
  model the *realistic* outcome as a weighted average of complete /
  switch / drop. For students with marginal preparation for the
  flagship-public major (especially out-of-state who didn't
  graduate from the strongest local feeder high schools), the
  ranked-private with higher completion may be the better expected-
  outcome despite the higher sticker. Cross-edge to D5.

### 3.4 Program choice treated as free when admissions-side constraints gate internal transfer

- **Statement**: The asker assumes "pick the high-ROI program" once
  admitted to the school, when capacity-constrained majors at
  flagship publics (CS at UW, engineering at UT-Austin, business
  at UMich, McCombs at UT, Haas at Berkeley) gate internal transfer
  via GPA cuts and waitlists.
- **Source-evidence**: [`framings.md` F3 fourth Excludes bullet](./framings.md) —
  "Frames 'ROI by program' as if program-of-study were a free
  choice; many applicants are admitted to a specific college on
  the basis of an intended major, and changing majors after
  enrollment is not always free."
- **Trigger**: Asker is admitted to a flagship public but NOT
  directly to the high-ROI major they want (CS, engineering,
  business) — admitted to "pre-CS" / "L&S undeclared" /
  "engineering-undeclared" / "intended-business-no-direct-admit".
- **Failure-mode**: Student enrolls expecting to transfer into CS /
  business / engineering after first-year; doesn't make the GPA
  cut (CS at UW requires 3.7+ in prereqs; Haas at Berkeley
  requires top ~20% of applicant pool); is locked into a non-
  target major with the higher-tuition out-of-state cost of the
  flagship; the ROI calculation was based on access to the high-
  ROI major they couldn't enter.
- **Recovery-move**: Verify direct-admit status into the target
  major BEFORE accepting the offer. For flagship publics with
  capacity-constrained majors, prefer direct-admit at a slightly-
  less-prestigious school over indirect-admit at the flagship.
  Check each school's internal-transfer policy and historical
  acceptance rate into the constrained major. For pre-CS / pre-
  business indirect-admit cases, model the realistic transfer
  probability and the cost of the non-target outcome. Cross-edge
  to D5.

### 3.5 International-student visa-pathway value omitted from program-ROI for international applicants

- **Statement**: The asker (or family) is computing program ROI on
  earnings-only data for an international applicant, missing that
  MS-CS at a top-10 US program unlocks H-1B-cap-exempt-master's-cap
  routes and 3-year STEM-OPT extension — visa-pathway value that
  domestic-framing earnings data understates materially.
- **Source-evidence**: [`framings.md` F3 fifth Excludes bullet](./framings.md) —
  "Doesn't see that for international students, the program-level
  ROI calculation has to include visa-pathway value." Cross-routes
  `immigration`. Statutory anchor: INA §214(g)(5)(C) H-1B master's-
  cap, 8 CFR §214.2(f)(10)(ii)(C) STEM-OPT extension.
- **Trigger**: International student (or family) considering US
  MS-CS / MS-engineering programs AND comparing programs on
  earnings-only data, AND not explicitly weighting the visa-pathway
  difference between top-10 (H-1B cap-exempt master's cap access,
  strong STEM-OPT-to-H-1B pipeline) and non-top STEM programs
  (still STEM-OPT but weaker downstream H-1B sponsorship rates).
- **Failure-mode**: International student chooses a lower-cost
  non-top MS-CS at a state university over a top-10 program based
  on earnings-only comparison; STEM-OPT works for 3 years, but
  H-1B cap-exempt master's-cap is harder to access without the
  top-program signal, and the regular H-1B lottery odds (~25-30%
  per year, three tries via STEM-OPT) mean a meaningful chance
  of forced US-exit at year 6 with no H-1B. Visa-pathway value of
  the top-program tier is on the order of "US-career-possibility-
  multiplier × lifetime US comp differential", easily $500k-2M
  NPV.
- **Recovery-move**: For international students, build a program-
  ROI calculation that includes (a) earnings differential, (b)
  H-1B master's-cap access probability differential, (c) downstream
  employer-sponsorship reputation (FAANG / large tech routinely
  sponsor; mid-tier and startups less so), (d) STEM-OPT-to-H-1B
  conversion probability. For students with strong intent to stay
  in the US long-term, top-10 STEM is often justified by visa-
  pathway value alone even when the earnings differential is
  modest. Cross-route to `immigration` for the H-1B / OPT / O-1 /
  EB-2-NIW pathway analysis; cross-route to `tech-career` for the
  FAANG vs mid-tier sponsorship reality.

---

## F4 — Rate-spread-arithmetic framing

### 4.1 Probability of option-exercise systematically under-estimated by the borrower

- **Statement**: The asker computes the rate-spread refi math
  assuming they can accurately model their own probability of
  layoff / disability / nonprofit-pivot / graduate-school over a
  20-year horizon, when revealed-preference data shows personal
  probability-estimation is systematically optimistic on these
  dimensions.
- **Source-evidence**: [`framings.md` F4 first Excludes bullet](./framings.md) —
  "Doesn't see that the rate-spread framing presumes the borrower
  can accurately model their probability of option-exercise — most
  borrowers under-estimate layoff probability, disability-onset
  probability, career-pivot-to-nonprofit probability, and family-
  emergency probability over 20-year horizons." Opposes F1's
  Excludes #1 (over-counting option value).
- **Trigger**: Asker presents a refi-vs-stay-federal decision as
  "I'm in stable comp, I'll never need PSLF, the math is the math"
  AND has not modeled adverse-scenario probabilities (BLS layoff
  base rate by industry, SSA disability-onset by age, the actual
  population rate of mid-career nonprofit / public-service pivots
  among professionals).
- **Failure-mode**: Borrower refis $200k federal-to-private at
  200bp spread saving $4k/yr; year 4 of repayment, gets laid off
  in a tech contraction; private lender has no IDR equivalent,
  no income-based hardship lever beyond 12-month forbearance with
  interest accrual; borrower has $200k private balance and no
  income; the federal IDR cap that would have been ~$0/mo at
  poverty-line income is unavailable; default risk is now
  meaningfully elevated.
- **Recovery-move**: Before any refi-vs-federal decision, walk
  through specific adverse scenarios with base-rate probabilities
  attached: tech-layoff rate ~10-15% per year in recession years
  for senior engineers; SSA disability-onset by 50 is ~5-8%;
  mid-career pivot to nonprofit is ~5-10% among professionals over
  20 years; PSLF-eligible-employment probability is ~10-15% among
  professionals depending on field. Multiply each by the option's
  value to the borrower in that scenario. If the *probability-
  weighted option value* exceeds the rate-spread savings, federal
  optionality wins. For borrowers with $150k+ balance and any
  ambiguity on these probabilities, **route to a fee-only fiduciary
  CFP or student-loan attorney** for the option-value audit.
  Cross-edge to F1, D1.

### 4.2 Private-refi rate quotes treated as permanently available when re-rate on income change is the actual exposure

- **Statement**: The asker assumes "I can always refi again if
  rates fall" — but private lenders re-rate hard on income change
  at refi-cycle, so the same SoFi 800+ FICO borrower at $400k AGI
  gets rejected at $80k AGI post-layoff. The refi-optionality is
  path-dependent on income stability.
- **Source-evidence**: [`framings.md` F4 second Excludes bullet](./framings.md) —
  "Treats private-refi rate quotes as if they were permanently
  available; private lenders re-rate hard on income change at
  refi-cycle so the 'I'll just refi again if rates fall'
  assumption is fragile."
- **Trigger**: Asker accepts a private refi at a higher rate today
  with the explicit plan "I'll refi again when rates drop" OR
  "I'll refi to variable later if the rate environment shifts."
- **Failure-mode**: Borrower refis to SoFi 7% fixed in 2025 with
  $300k AGI; rates fall to 5% in 2027; borrower had a $180k bonus
  reduction and now AGI is $150k; SoFi declines the re-refi based
  on the lower income; borrower stays at 7% with no ability to
  capture the rate drop, AND the option to refi back-to-federal
  doesn't exist.
- **Recovery-move**: Treat the *initial* private-refi rate as the
  rate the borrower will be carrying for the loan term, NOT as a
  starting point that can be refi'd lower later. Verify any "I'll
  refi later" plans against current lender re-rate underwriting
  criteria (most require ≥$X AGI and clean credit at re-refi;
  SoFi typically requires same-or-higher income vs original
  underwriting). For borrowers in income-volatile fields
  (commission-based comp, startup equity, freelance / 1099),
  build the refi decision around the *current* rate as permanent
  AND model the no-future-refi scenario.

### 4.3 Cosigner-asymmetry on private undergrad refi missed when comparing to Parent PLUS

- **Statement**: The asker compares "private undergrad refi at 5%
  vs Parent PLUS at 9.08%" on rate-spread alone, missing that
  Parent PLUS discharges on parent death under HEA §437(a) while
  private cosigner debt typically does not — and that private
  cosigner-release after 12-48 months requires re-underwrite that
  can fail.
- **Source-evidence**: [`framings.md` F4 third Excludes bullet](./framings.md) —
  "Under-weights the cosigner-asymmetry on private undergrad refi:
  most private refis allow cosigner-release after 12-48 months of
  on-time payments but require a re-underwrite that can fail if
  income has dropped — material for borrowers whose parent
  cosigned and wants release. The rate-spread framing's 'private
  beats PLUS by 200bp' misses that the parent-cosigner-trap on
  private is structurally different from Parent-PLUS-in-parent's-
  name." Decisions.md D7 cross-edge. Statutory anchor: HEA §437(a)
  death-and-disability discharge.
- **Trigger**: Family is considering "private with parent cosigner"
  vs "Parent PLUS in parent's name" purely on rate, AND the parent
  is 55+ (mortality-table-relevant for the §437(a) discharge
  consideration) OR the parent's income is variable / approaching
  retirement (cosigner-release re-underwrite at risk).
- **Failure-mode**: Family takes private undergrad loan with parent
  cosigner at 6%; parent dies during the loan term; the loan
  remains on the student's balance with the *deceased parent's
  estate* still a co-obligor through probate, AND the loan
  servicer typically does not stop collection during the probate
  process; this is materially worse than the Parent-PLUS-in-
  parent's-name case where §437(a) discharges the entire balance
  on parent death.
- **Recovery-move**: For families with parents 55+ or
  health-uncertainty, prefer Parent PLUS (despite rate premium)
  for the §437(a) protection. For families pursuing private with
  cosigner, verify the cosigner-release re-underwrite criteria
  explicitly (SoFi requires 12 months on-time + income test;
  Earnest requires 36; Sallie Mae 12-48 depending on product) and
  understand that re-underwrite failure leaves the cosigner on
  the loan for the full term. Plan the cosigner-release
  application timing around the expected income-stability window
  for the primary borrower. For Parent PLUS, also surface that
  the parent borrower can use Direct Consolidation + IDR (via
  ICR specifically — only IDR option for Parent PLUS after
  consolidation) for hardship — option not available on private.
  Cross-edge to D7, F9.

### 4.4 ARPA §9675 tax-bomb-exclusion cliff (end-2025) missed when comparing refi vs IDR-forgiveness

- **Statement**: The asker compares refi rates against IDR-
  forgiveness arithmetic that assumes the ARPA §9675 federal-tax-
  exclusion of forgiven balances continues, when the exclusion
  sunsets end-of-2025 absent extension and IDR borrowers reaching
  forgiveness in 2026+ face full ordinary-income inclusion.
- **Source-evidence**: [`framings.md` F4 fourth Excludes bullet](./framings.md) —
  "Misses ARPA §9675's tax-bomb-exclusion-sunset (end-of-2025) for
  IDR borrowers: a borrower currently on IDR planning the rate-
  spread refi comparison 'in case the IDR-forgiveness math
  improves' is comparing against an IDR-forgiveness scenario that
  may include $50k+ of unplanned tax liability post-2025 absent
  ARPA extension." Decisions.md D4 cross-edge. Statutory anchor:
  ARPA §9675 (P.L. 117-2), sunset end-of-2025.
- **Trigger**: Asker is on IDR with balance > 1× AGI, considering
  whether to refi to private vs continue on IDR for the long-haul
  forgiveness, AND projected forgiveness year is 2026 or later,
  AND the borrower has not modeled the post-cliff scenario
  explicitly.
- **Failure-mode**: Borrower stays on IDR planning to forgive
  $180k at year 20 (2031); ARPA exclusion is not extended;
  forgiveness-year tax liability at 35% marginal = $63k due in
  cash that year; borrower has no sinking fund because the
  comparison was done assuming ARPA exclusion holds; the $63k
  must come from retirement-account distributions (10% penalty
  + ordinary income on 401k pre-59.5) or short-term debt at 8-12%
  APR.
- **Recovery-move**: Re-do the refi vs IDR-forgiveness math under
  *two* tax-bomb scenarios: ARPA-extended (federal tax-free) and
  ARPA-cliff (federal tax at marginal rate + state per
  conformity). If post-cliff scenario flips the conclusion to
  "refi captures more value", surface this explicitly. For
  borrowers staying on IDR despite cliff exposure, **route to a
  retirement-experienced CPA** for tax-bomb sinking-fund design
  and Roth-conversion-ladder coordination. Cross-edge to F8
  (tax-bomb sinking-fund), F12 (ARPA-cliff-aware), D4.

### 4.5 SAVE-administrative-forbearance treatment of payment counts missed in refi-vs-IDR math

- **Statement**: The asker compares refi-savings against "stay on
  SAVE and forgive in year 20" without recognizing that SAVE-
  forbearance months count for PSLF but NOT for IDR-forgiveness
  counting — the year-20 baseline may slip to year 22-23 once
  the SAVE litigation resolves and counts are re-baselined.
- **Source-evidence**: [`framings.md` F4 fifth Excludes bullet](./framings.md) —
  "Glosses over SAVE-administrative-forbearance treatment of months
  for IDR-forgiveness (those months count for PSLF but NOT for
  IDR-forgiveness counting purposes); a borrower comparing rate-
  refi against 'stay on SAVE and forgive in year 20' is comparing
  against a year-20 that may slip to year 22-23 once the SAVE
  litigation resolves and counts are re-baselined." Statutory
  anchor: 8th Circuit SAVE injunction (2024-25).
- **Trigger**: Asker is currently on SAVE (or claims to be — many
  borrowers don't realize they were auto-enrolled or that SAVE
  is now in forbearance), AND is doing refi-vs-IDR math against
  a year-20 IDR-forgiveness baseline, AND has not pulled their
  current "qualifying payment count for IDR-forgiveness" from
  StudentAid.gov (distinct from the PSLF count).
- **Failure-mode**: Borrower stays on what they call SAVE plan
  expecting forgiveness at month 240 from their original loan
  origination; learns at year 18 that 24 months of SAVE-
  forbearance didn't count toward IDR-forgiveness (only toward
  PSLF, which the borrower wasn't pursuing); forgiveness slips
  to month 264 (year 22); tax-bomb at 35% marginal hits 22 years
  out instead of 20, and the additional 2 years of interest
  accrual adds ~$15-25k to the forgiven balance and tax bill.
- **Recovery-move**: Pull current "qualifying payment count for
  IDR forgiveness" (distinct from PSLF count) from StudentAid.gov
  PSLF Help Tool / IDR-forgiveness-tracker (where available).
  Plan IDR-forgiveness math around the *re-baselined* count, not
  the original loan-month count. For borrowers on SAVE in active
  forbearance, consider switching to IBR or PAYE (post-injunction
  IDR option) to get the months counting again — though this
  itself can reset some clocks; verify before switching. Cross-
  edge to F1 (SAVE-as-permanent), D4.

---

## F5 — FAFSA-base-year-and-asset-positioning framing

### 5.1 CSS Profile schools treated as sharing FAFSA reporting rules

- **Statement**: The asker plans FAFSA-optimization (max retirement
  contributions in pre-base-year, shift assets out of student name,
  shelter business assets) thinking it applies to all aid sources,
  missing that CSS Profile schools count home equity, count small-
  business assets (FAFSA stopped counting these in 2024 but CSS
  still asks), ask divorced non-custodial-parent income separately,
  and may add 401k contributions in the base year back into
  available income.
- **Source-evidence**: [`framings.md` F5 first Excludes bullet](./framings.md) —
  "Treats CSS Profile schools as if they shared FAFSA reporting
  rules; in fact CSS counts home equity (often capped at 1.2-2.4×
  income at some schools, uncapped at others), counts small-
  business assets that FAFSA doesn't since 2024, asks divorced
  non-custodial-parent income separately." Decisions.md D8 cross-
  edge. Statutory anchor: FAFSA Simplification Act of 2020; CSS
  Profile is private College Board product, not statutory.
- **Trigger**: Family applying to a school list that includes CSS
  Profile institutions (most highly-selective privates — all Ivies,
  T20 LACs, Stanford, Duke, Vanderbilt, USC, Northwestern,
  Georgetown, etc.) AND is doing FAFSA-only optimization without
  modeling CSS treatment.
- **Failure-mode**: Family in NJ owns $1.2M primary residence with
  $700k equity; FAFSA excludes home equity entirely; CSS Profile
  at Princeton / Duke / Stanford counts the $700k home equity at
  5.64% drag = ~$40k/yr add to expected contribution; family
  optimized FAFSA-only and is shocked by CSS aid offer $35-40k/yr
  below what FAFSA-only schools offered for the same family.
- **Recovery-move**: Build the target-school list FIRST, identify
  which schools require CSS Profile (use College Board's CSS-
  Profile Participating Schools list), and pull each school's CSS
  asset treatment (some schools have home-equity caps at 1.2-2.4×
  income, others count uncapped; Princeton excludes primary
  residence entirely; many T20s cap at 1.2× income). For mixed
  FAFSA/CSS lists, model both aid scenarios separately. Use each
  school's Net Price Calculator with realistic asset disclosure
  for first-pass aid estimates. For families with significant home
  equity or small-business assets AND CSS-school applications,
  **route to a NACAC-member college counselor** for CSS-specific
  positioning — this is one of the highest-leverage advisory
  interventions in the college process. Cross-edge to D8, F7.

### 5.2 Base-year-of-prior-prior applied only to first year, not to each subsequent FAFSA cycle

- **Statement**: The asker plans pre-base-year AGI management for
  the freshman-year FAFSA (avoid Roth conversions, capital-gains
  harvests, business sales 2 years before college start) but
  doesn't realize each subsequent year's FAFSA also uses prior-
  prior, so AGI-inflating events in sophomore-year tax-year affect
  senior-year award.
- **Source-evidence**: [`framings.md` F5 second Excludes bullet](./framings.md) —
  "Under-weights the *base-year-of-prior-prior-year* on the *back
  end* of college: the FAFSA submitted for the senior-year award
  uses tax-year sophomore-year as the base year, which means an
  AGI-inflating event in the sophomore-year tax-year matters for
  the senior-year award. The framing's 'pre-base-year planning'
  applies to the front-of-college decisions but the same logic
  applies to each subsequent year's award."
- **Trigger**: Family did careful pre-base-year planning for
  freshman-year FAFSA, AND has a planned AGI-inflating event in
  the sophomore-year tax-year (planned business sale, executive
  comp vest, retirement-account-conversion strategy, real-estate
  sale), AND is not planning around the senior-year FAFSA cycle
  recurrence.
- **Failure-mode**: Family takes $200k Roth conversion in
  sophomore-year tax-year for long-term tax-bracket-management;
  senior-year FAFSA AGI shows the conversion as ordinary income;
  need-based aid for senior year drops by $15-20k vs prior years
  the family had planned for; the conversion benefit was real but
  the aid hit was unplanned.
- **Recovery-move**: For families with kids in college, map the
  FAFSA-base-year-window for *every* college year — freshman uses
  prior-prior, sophomore uses prior-prior, etc. Plan AGI-inflating
  events for the *student's-final-college-year + 1 tax-year* or
  later, when no further FAFSA cycle is affected. For multi-kid
  families with overlapping enrollment, the window may span 5-7
  years total. Cross-edge to `personal-finance` (Roth-conversion-
  ladder timing).

### 5.3 FAFSA Simplification removal of small-business assets read as universal — CSS reporting unchanged

- **Statement**: The asker (often a small-business owner / S-corp
  parent) hears "FAFSA doesn't count small-business assets anymore"
  and relaxes CSS asset disclosure thinking the same change applies,
  when CSS Profile still asks about all business assets in detail.
- **Source-evidence**: [`framings.md` F5 third Excludes bullet](./framings.md) —
  "Doesn't see that the FAFSA Simplification Act's removal of
  small-business assets from FAFSA reporting created a *deceptive*
  optimization — many CSS schools still ask, and self-employed-
  parent (S-corp distribution-vs-salary, schedule-C net income)
  reporting on CSS is unchanged from pre-Simplification." Cross-
  routes `entrepreneurship`. Statutory anchor: FAFSA Simplification
  Act of 2020.
- **Trigger**: Self-employed / S-corp / LLC parent with kid applying
  to CSS Profile schools AND referencing "FAFSA Simplification
  helped us" / "business assets aren't on FAFSA anymore" without
  acknowledging CSS still asks.
- **Failure-mode**: S-corp owner-parent with $800k in business
  retained-earnings + AR + equipment reports $0 business assets on
  FAFSA (correct under Simplification) but also relaxes CSS
  disclosure thinking the same; CSS Profile audit catches the
  discrepancy; aid offer is rescinded or reduced and the family
  loses trust with the FA office for future years; or the family
  discloses CSS accurately and is surprised when CSS-school aid is
  $20-30k/yr below FAFSA-school aid because of the business-asset
  add.
- **Recovery-move**: For self-employed / S-corp parents,
  proactively prepare both FAFSA and CSS disclosures separately —
  FAFSA excludes business assets, CSS asks. Be accurate on each.
  For CSS-school applications, model the business-asset impact on
  expected contribution and adjust the school list if CSS schools
  become unaffordable. For S-corp distribution-vs-salary
  questions, the salary affects AGI on both FAFSA and CSS (cross-
  edge to `entrepreneurship` on S-corp reasonable-comp under §1366);
  the distribution shows up on CSS as business income / owner-draw.
  For families with significant business complexity, **route to a
  retirement-experienced CPA with §529 / §25A history AND a NACAC-
  member college counselor** for joint CSS positioning. Cross-edge
  to D8, F7.

### 5.4 Retirement-account-contribution add-back on CSS missed when "max retirement IN base year" is treated as universal FAFSA tactic

- **Statement**: The asker maxes out 401k / 403b / IRA / Roth
  contributions IN the base year (not just pre-base-year) thinking
  it lowers reportable income, missing that many CSS Profile
  schools add base-year retirement contributions back into
  available income.
- **Source-evidence**: [`framings.md` F5 fourth Excludes bullet](./framings.md) —
  "Glosses over the *retirement-account-contribution add-back* on
  CSS Profile: many CSS schools add 401k / IRA / Roth contributions
  in the base year back into available income — the FAFSA strategy
  of 'max retirement contributions in pre-base-year' can still
  reduce CSS reported income but the strategy of 'make a large
  401k contribution IN the base year to lower reported AGI'
  doesn't work at most CSS schools." Decisions.md D8 cross-edge.
- **Trigger**: Family doing tactical 401k contribution sizing in
  the base year specifically for FAFSA-AGI reduction AND applying
  to CSS Profile schools (~200 institutions).
- **Failure-mode**: Parent makes a $23k 401k contribution in the
  base year specifically to lower reported AGI by $23k (saves
  ~$1,300-1,800 on FAFSA EFC at 5.64% drag); CSS school adds the
  $23k back into available income; CSS aid offer is unaffected by
  the contribution; the tactic only worked at FAFSA-only schools
  but was applied across-the-board.
- **Recovery-move**: For CSS-school families, max retirement
  contributions in *pre-base-year* tax-years (when the funds
  permanently exit reportable assets and income) rather than IN
  the base year (when CSS adds them back). The pre-base-year
  strategy still works at FAFSA-only schools too. For families
  late to the planning window with only base-year as the active
  cycle, the contribution still has long-term retirement value
  but should not be counted as CSS-aid-tactic. Cross-edge to F10,
  `personal-finance` decision 1 (retirement-priority).

### 5.5 Professional-judgment-appeal under §479A treated as universally-granted reset button

- **Statement**: The asker treats the financial-aid appeal under
  HEA §479A as if it's a guaranteed adjustment for any hardship,
  when in fact §479A authority is *discretionary* per office,
  appeal-success rates vary significantly by institutional-aid
  budget, and documentation quality materially affects the outcome.
- **Source-evidence**: [`framings.md` F5 fifth Excludes bullet](./framings.md) —
  "Frames professional-judgment appeals as if they were universally
  available; in fact §479A authority is discretionary per
  financial-aid office, and the appeal-success rate varies
  significantly by school's institutional-aid budget and the
  specific change-in-circumstance documented." Reinforced by F7
  first Excludes (appeal-success-rate variance). Statutory anchor:
  HEA §479A.
- **Trigger**: Family planning to "just appeal if the aid offer is
  bad" without naming the specific change-in-circumstance that
  would trigger §479A authority (job loss, divorce mid-process,
  medical expense, business loss, death-in-family) and without
  documenting evidence.
- **Failure-mode**: Family receives FAFSA-determined SAI of $48k/yr
  based on prior-prior-year income; parent has since taken a $60k
  income reduction (voluntary pivot to lower-paying nonprofit, not
  a layoff); files §479A appeal without specific change-in-
  circumstance documentation; appeal denied; family is locked into
  the $48k/yr expected contribution for the award year; the asker
  blames the system when the issue was an inappropriate appeal
  basis.
- **Recovery-move**: §479A appeals require *documented change-in-
  circumstance* — job loss with severance letter, divorce decree,
  medical bills, business-failure financials, death certificate.
  Voluntary income reduction generally doesn't qualify. For
  families with genuine change-in-circumstance, prepare appeal
  packet with: cover letter naming the specific §479A basis,
  before/after income documentation, supporting third-party
  documents (medical, legal, employment), updated budget showing
  hardship. Appeal calendars vary by school (often 30-60 day
  windows post-award letter); file early. For high-stakes
  appeals (significant aid at risk), **route to a NACAC-member
  college counselor or NASFAA-affiliated financial-aid
  consultant** for appeal-letter drafting — letter quality
  matters. Cross-edge to F7, D8.

---

## F6 — 529-to-Roth-flexibility-hedge / SECURE 2.0 §126 framing

### 6.1 SECURE 2.0 §126 oversold as near-term flexibility when 15-year clock is the binding constraint

- **Statement**: The asker hears "529 now has Roth flexibility" and
  treats SECURE 2.0 §126 as a general solution to the "kid doesn't
  go" problem, when the 15-year-clock means a 529 funded in 2025
  cannot roll until 2040 at the earliest.
- **Source-evidence**: [`framings.md` F6 first Excludes bullet](./framings.md) —
  "Oversells the SECURE 2.0 §126 rollover's near-term value;
  financial press routinely treats it as '529 now has Roth
  flexibility' when the 15-year-clock means a 529 funded in 2025
  cannot roll until 2040 at the earliest, the $35k cap is small
  relative to typical college-funding shortfalls, the annual-Roth-
  limit constraint means even fully-converting $35k takes 5+ years,
  and the beneficiary-earned-income requirement excludes
  beneficiaries who are full-time students with no earned income."
  Decisions.md D3, D6 cross-edge. Statutory anchor: SECURE 2.0
  §126 (P.L. 117-328), effective 2024.
- **Trigger**: Asker references "SECURE 2.0 changed everything" /
  "529-to-Roth solves the leftover problem" / "we can always roll
  to Roth now" AND is starting 529 funding for an older child
  (10+) where 15-year-clock can't reach pre-college, OR is using
  §126 as justification for over-contribution.
- **Failure-mode**: Parent of 12-year-old aggressively funds 529
  to $200k by year-of-enrollment (age 18); kid gets full-ride
  scholarship + parent retains $180k unspent; SECURE 2.0 §126 15-
  year clock means rollover-eligible 2040 (kid will be 27);
  rollover capped at $35k lifetime AND subject to annual Roth
  contribution limit (~$7k/yr in 2026, indexed); even at $7k/yr
  takes 5 years to roll the full $35k; remaining $145k still
  faces 10% penalty + ordinary income on earnings for non-qualified
  distribution.
- **Recovery-move**: Treat SECURE 2.0 §126 as a narrow partial
  hedge worth ~$35k lifetime, not a general "529 flexibility"
  feature. For families starting 529 funding for children 10+,
  consider Roth IRA (if AGI qualifies) or taxable as alternative
  vehicles for the marginal contribution beyond projected college
  need. For over-funded existing 529s, plan beneficiary-change to
  siblings / nieces / nephews / self as the primary flexibility
  lever; SECURE 2.0 is secondary. Cross-edge to F2 third Excludes
  (leftover-529 problem), F10 (retirement-priority).

### 6.2 5-year recent-contribution lockout on §126 rollover under-appreciated

- **Statement**: The asker plans "fund 529 now, roll to Roth in 15
  years" without knowing that contributions made in the 5 years
  *before* rollover are locked out — so a parent contributing
  through years 11-15 of the seasoning window finds that
  contributions can't be rolled.
- **Source-evidence**: [`framings.md` F6 second Excludes bullet](./framings.md) —
  "Doesn't see the *5-year recent-contribution lockout*:
  contributions made within the past 5 years cannot be rolled — so
  a parent who funded $50k into a 529 in years 1-3 of beneficiary's
  life and then waits 15 years and tries to roll the leftover finds
  that any contributions made in years 11-15 of seasoning (within
  5 years of the rollover) are locked out." Statutory anchor:
  SECURE 2.0 §126 5-year contribution lookback.
- **Trigger**: Asker is planning 529-to-Roth rollover as a
  multi-year strategy AND continues making contributions during
  the rollover-execution years OR is steady-state contributing on
  the same schedule throughout the funding horizon.
- **Failure-mode**: Parent contributes $5k/yr to 529 for 18 years;
  by year 15 the kid has graduated with $80k unspent; parent tries
  to roll $35k to Roth IRA; contributions from years 11-15 (last
  5 years = $25k of contributions + earnings) are locked out and
  cannot be rolled; only the older $35k or so of contributions
  qualifies for rollover; the rollover-flexibility plan was sized
  to $35k but operationally only ~$10-15k is available given the
  contribution-cadence.
- **Recovery-move**: For families planning §126 rollover, stop
  contributing 5 years before the planned rollover date. Build
  this gap into the funding cadence proactively. For families
  late to the planning, plan the rollover for 5+ years after the
  *last* contribution, not 15 years after the *first*. Combine
  with beneficiary-change to extend the rollover availability
  across siblings (each new beneficiary resets the 15-year clock
  unless the IRS treats it as a continuation — this is an open
  question per current guidance; verify before relying).

### 6.3 Roth IRA earnings-withdrawal pre-59.5 treated as costless under §72(t) education-exception

- **Statement**: The asker treats Roth IRA as "fully flexible for
  college" because §72(t) waives the 10% early-withdrawal penalty
  for qualified education expenses — missing that the income tax
  on *earnings* withdrawn pre-59.5 still applies (only the
  contribution basis is tax-and-penalty-free).
- **Source-evidence**: [`framings.md` F6 third Excludes bullet](./framings.md) —
  "Treats Roth-IRA-as-college-funding-substitute as if Roth-
  contribution-withdrawal were costless; withdrawing Roth *earnings*
  before 59.5 (even for qualified education expenses) incurs 10%
  penalty on earnings absent the §72(t) education-expense
  exception (which waives the penalty but NOT the income tax on
  earnings)." Statutory anchor: IRC §72(t)(2)(E) education-expense
  exception; IRC §408A(d) Roth ordering rules.
- **Trigger**: Parent considering "use Roth IRA for college" as a
  flexibility-preserving alternative to 529, AND plans to access
  more than the contribution basis (Roth IRAs of 15+ years
  typically have basis < 30-40% of balance), AND parent is
  under 59.5.
- **Failure-mode**: Parent ages 48 has Roth IRA $120k ($45k basis +
  $75k earnings), uses $60k for kid's college; first $45k is tax-
  and-penalty-free (basis), next $15k is earnings — §72(t) waives
  10% penalty but NOT ordinary income tax; at 32% marginal = $4.8k
  of unexpected federal tax + state tax + reduced retirement
  balance vs the assumption of "Roth is fully flexible".
- **Recovery-move**: Distinguish *Roth contributions* (basis,
  always tax-and-penalty-free at any age) from *Roth earnings*
  (taxable as ordinary income pre-59.5 even for qualified
  education with §72(t)). For Roth-as-college-funding-substitute,
  plan to use only the basis portion pre-59.5. For larger college
  funding needs, the 529 (state-deduction + tax-free growth + tax-
  free qualified distribution) typically dominates Roth despite
  Roth's nominal flexibility advantage. Roth IRA as college-
  funding makes most sense for the small portion of contributions
  that may not be needed for retirement; the bulk of college
  funding belongs in 529.

### 6.4 AOTC/LLC §25A interaction with 529 distributions causes retroactive credit denial

- **Statement**: The asker doesn't realize the same dollar of
  qualified-education-expense cannot be used both to claim the
  AOTC under §25A and to justify a tax-free 529 distribution; the
  family must coordinate which expense dollars get attributed to
  the credit and which to the 529.
- **Source-evidence**: [`framings.md` F6 fourth Excludes bullet](./framings.md) —
  "Under-weights the IRC §25A AOTC/LLC interaction with 529 and
  Roth distributions: the same dollar of qualified-education-
  expense cannot be used both to claim the AOTC and to justify a
  tax-free 529 distribution — the family must coordinate which
  expense dollars get attributed to the credit and which to the
  529. Many families discover the coordination requirement
  retroactively at tax-filing time when the §25A claim is denied."
  Statutory anchor: IRC §25A AOTC/LLC, IRC §529(c)(3)(B)(v) no-
  double-dip coordination rule.
- **Trigger**: Family claims AOTC ($2,500/yr first 4 years
  undergrad) AND takes 529 distributions to cover qualified
  expenses AND total 529-paid expenses + AOTC-claimed expenses
  > total qualified expenses incurred.
- **Failure-mode**: Family pays $25k tuition (qualified expense);
  529 distributes $25k tax-free; family also claims AOTC ($2,500
  credit) on the same $4k of tuition; IRS audit catches the
  double-dip; AOTC credit is denied + 20% accuracy-related
  penalty under §6662 + interest = ~$3,000 tax bill in audit-year.
- **Recovery-move**: For AOTC-eligible years, plan to pay the
  first $4k of qualified expenses from non-529 sources (cash flow,
  Roth basis withdrawal, taxable brokerage) and use 529 for the
  remainder above $4k; this preserves AOTC eligibility cleanly.
  Document the source of each dollar of expense payment in
  contemporaneous records (1098-T, 529 distribution records, bank
  records). For families with both 529 and other funding sources,
  **route to a retirement-experienced CPA with §25A / §529
  history** for the year-of-distribution tax planning — this is a
  recurring annual coordination, not one-time. Cross-edge to D3,
  D6, F2.

### 6.5 State-tax recapture on 529-to-Roth rollover missed when treating SECURE 2.0 §126 as fully federal-tax-neutral

- **Statement**: The asker treats the SECURE 2.0 §126 529-to-Roth
  rollover as fully tax-free, missing that several states (NY,
  IL, NC, AR) explicitly recapture the original 529-contribution
  state-deduction when the rollover happens, treating it as a
  non-qualified distribution.
- **Source-evidence**: [`framings.md` F6 fifth Excludes bullet](./framings.md) —
  "Glosses over the state-tax treatment of the 529-to-Roth
  rollover: several states (NY, IL, NC, AR) explicitly recapture
  the original 529-contribution state-deduction when the rollover
  happens treating it as a non-qualified distribution; the
  federal-tax-free rollover does not protect against state-level
  recapture."
- **Trigger**: Family in state with 529-deduction recapture rules
  (NY, IL, NC, AR, others — check state) planning a §126 rollover
  AND assuming federal tax-free status applies at state level too.
- **Failure-mode**: NY family rolled $35k from NY 529 to Roth IRA
  under §126; NY recaptures the proportional deduction taken on
  the original contributions = ~$2,400 of NY tax owed in rollover
  year (35k × 6.85% NY marginal); family had not budgeted for the
  state-tax hit on what they thought was a federal-tax-free
  rollover.
- **Recovery-move**: Before executing §126 rollover, check state
  529-deduction recapture rules explicitly. For families in
  recapture states with significant deduction history, the §126
  rollover may not be worth the state-tax cost vs leaving funds
  in 529 for sibling beneficiary or accepting the 10% penalty +
  ordinary income on non-qualified distribution. Cross-edge to F2
  fourth Excludes (general state-recapture rules).

---

## F7 — NACAC-counselor / financial-aid-negotiation framing

### 7.1 Appeal-success treated as universal when school's institutional-aid budget is the binding constraint

- **Statement**: The asker treats "appeal the aid offer and you'll
  get more" as universal advice, missing that §479A success rates
  vary sharply by school's institutional-aid budget — Princeton /
  Harvard / Yale / Stanford with large endowments and need-blind-
  meets-full-need policies have different appeal-economics than
  mid-tier privates and tuition-dependent regionals.
- **Source-evidence**: [`framings.md` F7 first Excludes bullet](./framings.md) —
  "Treats appeal-success as universal; in fact §479A authority is
  discretionary per office, success rates vary significantly by
  school's institutional-aid budget." Opposes F3 (ROI-by-major).
- **Trigger**: Asker plans to appeal across all schools using same
  template / same documentation without segmenting by school's
  endowment / aid policy / sticker-vs-net-price patterns.
- **Failure-mode**: Family submits identical appeal letter to 6
  schools; high-endowment need-blind-meets-full-need schools
  (Princeton, Harvard) approve substantial adjustment; mid-tier
  tuition-dependent privates (regional Catholic / liberal-arts)
  deny because their institutional-aid budget is committed earlier
  in the cycle and they can't afford broad post-admit adjustments;
  family interprets all denials as personal-judgment when only the
  high-budget schools were realistically going to flex.
- **Recovery-move**: Segment the appeal strategy by school's
  institutional-aid context. For high-endowment / need-blind-
  meets-full-need schools, robust appeals with cross-admit
  leverage often succeed. For mid-tier privates, focus appeal on
  *demonstrated need-change* (job loss, medical) rather than
  cross-admit-leverage. For regional state-systems with formula-
  driven aid, appeal is typically procedural and limited to
  data-correction. **Route to a NACAC-member college counselor**
  for school-by-school appeal-strategy when the aid stack is
  high-stakes ($30k+ delta across offers).

### 7.2 Yield-protection and demonstrated-interest as negative factors missed in cross-admit-leverage strategy

- **Statement**: The asker uses cross-admit leverage to pressure
  mid-tier schools without realizing those schools may "yield-
  protect" — withhold merit aid from strong applicants assumed to
  be using the school as a safety, given less merit than weaker
  applicants likely to enroll.
- **Source-evidence**: [`framings.md` F7 second Excludes bullet](./framings.md) —
  "Doesn't see *yield-protection* and *demonstrated-interest* as
  factors that can work against the strong-applicant appeal: top-
  cross-admit applicants are sometimes 'yield-protected' by mid-
  tier schools (assumed to be using the school as a safety, given
  less merit aid than weaker applicants who are likely to enroll)."
- **Trigger**: Student admitted to a high-tier school AND a mid-
  tier school (where the student is in the top decile of admits);
  family plans to leverage the high-tier offer at the mid-tier for
  merit-aid increase.
- **Failure-mode**: Family writes appeal letter to mid-tier
  citing the higher-tier offer as benchmark; mid-tier interprets
  this as confirmation the student won't enroll there regardless;
  mid-tier doesn't budge on merit aid; family loses the leverage
  attempt; if family was actually interested in the mid-tier, the
  appeal may have damaged the relationship.
- **Recovery-move**: For yield-protection-prone schools (mid-tier
  privates where the student is in top decile, some flagship
  publics for in-state high-achievers), demonstrate genuine
  interest BEFORE appealing — campus visit, named-program-
  application-essay, named-faculty-correspondence. Frame the
  appeal as "I'm trying to make X work, here's the gap" rather
  than "School-Y offered me more, can you match?". For schools
  where genuine interest hasn't been signaled, the appeal may
  back-fire. Cross-edge to F3 (ROI-by-program) when ROI argument
  is stronger than emotional fit.

### 7.3 Appeal-cycle calendar awareness missing — late appeals deprioritized

- **Statement**: The asker plans to appeal after the May 1
  commitment deadline thinking the appeal works year-round,
  missing that most schools have internal deadlines for §479A
  appeals (often within 30 days of award letter, sometimes by
  May 1).
- **Source-evidence**: [`framings.md` F7 third Excludes bullet](./framings.md) —
  "Glosses over the *timing* of the appeal: most schools have an
  internal deadline for professional-judgment appeals (often
  within 30 days of the award letter, sometimes by May 1 commitment
  deadline), and late appeals are de-prioritized or denied outright."
- **Trigger**: Family received aid offer in March, plans to commit
  by May 1, and figures they can appeal "any time during the
  award year if circumstances change" without checking the school's
  appeal-deadline policy.
- **Failure-mode**: Parent has a job-loss in mid-summer (post-May 1
  commitment); family tries to file §479A appeal in July; school's
  institutional-aid budget is already committed for the year;
  appeal is denied or deferred to spring-semester-only adjustment;
  family is locked into the original aid offer for fall-semester
  at minimum.
- **Recovery-move**: For each school in the application list,
  identify the §479A appeal cycle and deadlines explicitly (most
  publish on financial-aid office website or in the award packet).
  File appeals as early as possible after triggering event; for
  pre-commitment appeals, file before May 1. For mid-year
  hardships, appeals can be filed but may apply only to
  subsequent semesters. Document the triggering event with date-
  stamped supporting materials. Cross-edge to D8, F5 fifth
  Excludes (appeal-basis).

### 7.4 FAFSA-appeal vs CSS-Profile-appeal conflated when procedural paths differ

- **Statement**: The asker treats "appeal" as a single process,
  missing that FAFSA appeals (need-based, driven by AGI / asset
  changes) and CSS Profile appeals (institutional-aid-budget-
  driven, more discretionary) follow different procedural paths.
- **Source-evidence**: [`framings.md` F7 fourth Excludes bullet](./framings.md) —
  "Under-weights the difference between FAFSA appeals (need-based,
  driven by AGI / asset changes) and CSS-Profile appeals
  (institutional-aid-budget driven, more discretionary), which
  follow different procedural paths at most schools."
- **Trigger**: Family at a CSS-Profile school appeals via the FAFSA
  process (or vice versa) without realizing the school treats them
  separately, AND the change-in-circumstance affects only one
  reporting source.
- **Failure-mode**: Family has a primary residence with significant
  equity (not reported on FAFSA, reported on CSS at 5.64% drag);
  family appeals "we have less liquid resources than the EFC
  suggests"; FAFSA appeal denied because FAFSA-reported assets
  don't include the home equity in question; CSS appeal not filed
  because family didn't realize the institutional-aid track was
  separate; aid offer unchanged when CSS-specific appeal might
  have succeeded.
- **Recovery-move**: For mixed FAFSA/CSS school applications,
  clarify which aid source is driving the gap (FAFSA need-based vs
  CSS institutional vs merit) and file appeals through the
  correct channel. Most schools have separate appeal forms or
  contacts for FAFSA-need-based vs CSS-institutional. For families
  unclear on the source-of-gap, the financial-aid office can
  explain — ask. Cross-edge to F5, D8.

### 7.5 Merit-aid framed as fully negotiable when formula-driven merit programs are mechanical

- **Statement**: The asker treats all merit aid as discretionary
  / negotiable, missing that some schools (flagship publics'
  automatic scholarships based on GPA / test-score cutoffs, large-
  state-system merit programs) do NOT negotiate because awards
  are formula-mechanical.
- **Source-evidence**: [`framings.md` F7 fifth Excludes bullet](./framings.md) —
  "Frames merit-aid as fully negotiable when in fact some schools
  (especially those with formula-driven merit-aid awards based on
  GPA / test-score cutoffs — many flagship publics' automatic
  scholarships, large-state-system merit programs) do NOT
  negotiate on merit because the awards are formula-mechanical."
- **Trigger**: Family asks "can we negotiate the merit aid?" at a
  formula-driven scholarship program (Bama / Alabama-flagship
  automatic National Merit scholarships, Texas A&M President's
  Endowed Scholarship, Florida Bright Futures, GA HOPE, NC
  Carolina Covenant).
- **Failure-mode**: Family invests time in negotiation efforts at
  formula-merit schools; aid office responds with "we cannot
  adjust formula scholarships"; family interprets as adversarial
  / personal when it's structural; misses the timing window for
  other-school appeals where negotiation actually works.
- **Recovery-move**: Identify formula-merit vs discretionary-merit
  at each school in the application list. For formula-merit (Bama
  / Florida / GA / TX-A&M etc.), the path is to meet a higher
  formula threshold via additional test-prep or transcript-
  improvement rather than negotiation. For discretionary-merit
  (most ranked-privates, some publics' Honors Colleges), cross-
  admit leverage is the standard tool. Cross-edge to F3 (ROI-by-
  program for formula-merit schools).

---

## F8 — Tax-bomb-arithmetic-and-sinking-fund framing

### 8.1 ARPA §9675 sunset treated as certain when extension is plausible

- **Statement**: The asker is building a tax-bomb sinking fund
  for IDR-forgiveness assuming ARPA §9675 (federal tax-exclusion
  of student-loan forgiveness through 2025) definitely sunsets —
  without acknowledging that extension is plausible given
  political dynamics, in which case the sinking fund earmarks
  funds for a non-event.
- **Source-evidence**: [`framings.md` F8 first Excludes bullet](./framings.md) —
  "Treats the tax-bomb-sinking-fund as if the ARPA §9675 exclusion
  will definitely sunset; in fact further extension is plausible
  given political dynamics, and a sinking fund that grows for 20
  years against a tax liability that gets excluded leaves the
  borrower with $30-40k of taxable brokerage that did NOT need to
  be earmarked for taxes." Opposes F12 (ARPA-cliff-aware).
  Statutory anchor: ARPA §9675 (P.L. 117-2).
- **Trigger**: Asker on IDR with projected forgiveness year 2026+
  is building tax-bomb sinking fund AND treating ARPA-cliff as
  certain (no scenario-modeling for extension).
- **Failure-mode**: Borrower sets aside $30-40k for tax-bomb over
  20 years; ARPA extension passes 2027; forgiveness in 2030 is
  federal-tax-free; the $30-40k of taxable brokerage was earmarked
  for an unneeded tax bill — funds were not deployed to higher-
  growth-rate retirement-account contributions during accumulation
  phase, $30-40k present-value × ~15-20 years × growth-differential
  = $30-50k of foregone retirement-account growth.
- **Recovery-move**: Build the sinking fund but treat it as
  *flexible* taxable brokerage that defaults to retirement /
  general savings if ARPA extends. Don't lock the funds into an
  earmarked-only account. Re-evaluate the sinking-fund need
  annually as the ARPA-cliff approaches and after each cycle's
  legislative action. For high-balance IDR borrowers ($150k+
  projected forgiveness), **route to a fee-only fiduciary CFP and
  retirement-experienced CPA** for joint planning that hedges both
  ARPA-sunset and ARPA-extension scenarios. Cross-edge to F12,
  D4.

### 8.2 §108(a)(1)(B) insolvency exclusion overstated when retirement balances disqualify the path

- **Statement**: The asker treats §108(a)(1)(B) insolvency
  exclusion as a reliable backstop, missing that retirement-
  account balances count as *assets* for insolvency-determination
  purposes (even though they're excluded from FAFSA), so borrowers
  with significant 401k / IRA / Roth balances are usually NOT
  insolvent at moment-of-forgiveness.
- **Source-evidence**: [`framings.md` F8 second Excludes bullet](./framings.md) —
  "Doesn't see the *insolvency-exclusion-§108(a)(1)(B)* path
  clearly: insolvency at the moment of forgiveness can fully
  exclude the forgiven amount from federal income, but it
  requires documenting that liabilities exceeded assets
  *immediately before the discharge* — a fact-specific calculation
  that requires CPA analysis and Form 982 filing. For borrowers
  with significant retirement-account balances (which count as
  assets for insolvency purposes despite being excluded from
  FAFSA), the insolvency path is often unavailable." Statutory
  anchor: IRC §108(a)(1)(B), Form 982.
- **Trigger**: Asker considering "I'll just use insolvency
  exclusion at forgiveness" as the tax-bomb-management strategy,
  AND has $200k+ of retirement-account balances accumulated by
  forgiveness year (likely for any borrower with 20+ years of
  401k participation).
- **Failure-mode**: Borrower reaches IDR-forgiveness year with
  $180k forgiven balance + $400k of 401k / Roth assets + $30k of
  non-retirement equity; insolvency test requires liabilities >
  assets *immediately before discharge*; retirement balances count
  as assets; borrower is NOT insolvent; §108(a)(1)(B) exclusion
  unavailable; full $180k forgiven balance is ordinary income at
  35% marginal = $63k tax bill the borrower had planned to
  exclude.
- **Recovery-move**: Don't plan around §108(a)(1)(B) insolvency
  exclusion unless current asset trajectory genuinely projects
  insolvency at forgiveness year (which usually requires
  borrower has not been retirement-saving, which is itself a bad
  outcome). For borrowers actively saving for retirement,
  **route to a retirement-experienced CPA** for tax-bomb
  sinking-fund design that does NOT rely on insolvency exclusion
  as primary plan. Insolvency is a fallback for genuine
  catastrophic-financial-situation borrowers, not a primary tax-
  planning tool. Cross-edge to D4, F1 (federal-optionality death-
  and-disability).

### 8.3 State-level tax-bomb on forgiven amount missed even when federal ARPA excludes

- **Statement**: The asker plans tax-bomb math based on federal
  ARPA §9675 exclusion, missing that state conformity to ARPA is
  uneven — CA, MS, IN, NC, WI did NOT conform to the 2022 one-time
  exclusion, and similar non-conformity may apply to IDR-
  forgiveness post-2026.
- **Source-evidence**: [`framings.md` F8 third Excludes bullet](./framings.md) —
  "Glosses over the state-level tax-bomb on the forgiven amount:
  even when ARPA §9675 excludes federally, state conformity is
  uneven — CA, MS, IN, NC, WI did NOT conform to the 2022 one-time
  exclusion. A borrower in a non-conforming state faces state tax
  on the forgiven balance even when federal tax is excluded."
- **Trigger**: Borrower in non-conforming state (CA, MS, IN, NC,
  WI, others to check current-year) projecting IDR-forgiveness AND
  doing tax-bomb math at federal-only level.
- **Failure-mode**: California borrower forgives $200k IDR balance
  in 2027; federal ARPA exclusion (if extended) makes federal tax
  $0; CA does not conform — $200k counts as CA ordinary income at
  9.3% marginal = $18,600 of CA tax owed in forgiveness year;
  borrower had planned for $0 tax under federal-only analysis;
  $18k cash shortfall in forgiveness year.
- **Recovery-move**: Do the tax-bomb math at both federal AND
  state level separately. Check current-year state conformity to
  the relevant federal exclusion (state-tax-conformity-statements
  published annually by state revenue departments). For borrowers
  in non-conforming high-tax states (CA, NY, NJ, OR, MN), size the
  sinking fund to the state-tax-portion even if federal exclusion
  holds. Cross-edge to F12 (state-conformity dimension), D4.

### 8.4 Roth-conversion-ladder in low-income years as bracket-management complement missed

- **Statement**: The asker treats the tax-bomb as a year-of-
  forgiveness lump-sum tax event, missing that Roth conversions
  in *prior* low-income years (sabbatical, leave-of-absence,
  between jobs) can use up bracket headroom and partially pre-pay
  the future tax liability at a lower effective rate.
- **Source-evidence**: [`framings.md` F8 fourth Excludes bullet](./framings.md) —
  "Under-weights the *Roth-conversion-ladder in low-income years*
  as a complementary strategy: in years where the borrower has
  structurally low income (sabbatical, leave-of-absence, between
  jobs), accelerating Roth conversions to use up bracket headroom
  is a partial pre-payment of the future tax-bomb liability."
  Cross-routes `personal-finance` decision 4 (Roth-conversion-
  ladder).
- **Trigger**: Borrower on long-horizon IDR-forgiveness path AND
  has periods of low-income (sabbatical, parental leave, job
  transition, career pivot to grad school) AND has traditional
  IRA / 401k balances eligible for Roth conversion AND is not
  using the low-income windows for bracket arbitrage.
- **Failure-mode**: Borrower has $100k of pre-tax 401k that will
  eventually need RMD-conversion in retirement at 25%+ marginal;
  forgiveness year hits at 35% marginal due to forgiveness-
  income spike; borrower paid 35% rate on $100k of conversion
  (or $100k of forgiveness-included income) when low-income years
  could have converted at 12-22%. Lost arbitrage value: ~$10-20k
  on $100k converted at the right time.
- **Recovery-move**: For IDR-forgiveness-track borrowers, build a
  multi-year tax plan that uses low-income years for Roth
  conversions up to bracket-fill (target 12% bracket fill, or 22%
  fill if longer-horizon retirement). This pre-pays effective tax
  on the eventual forgiveness income at a lower rate. Coordinate
  with sinking-fund cadence. For borrowers with $150k+ IDR
  forgiveness projected, **route to a retirement-experienced CPA
  and fee-only fiduciary CFP** for joint multi-year tax planning.
  Cross-edge to `personal-finance` decision 4, F4 fourth Excludes
  (ARPA-cliff awareness).

### 8.5 Taxable brokerage growth on sinking fund treated as pre-tax when LTCG drag is real

- **Statement**: The asker sizes the sinking fund at "expected
  market return" (7-8% nominal) without netting out LTCG / dividend
  drag on the taxable account; the actual after-tax accumulation
  rate is meaningfully lower.
- **Source-evidence**: [`framings.md` F8 fifth Excludes bullet](./framings.md) —
  "Frames the sinking-fund-in-taxable-brokerage as if taxable
  growth were free; taxable LTCG on the sinking fund itself is
  taxed, and dividends are ordinary or qualified depending on the
  fund — the net-of-tax growth rate on the sinking fund is below
  market rate." Statutory anchor: IRC §1(h) LTCG rates.
- **Trigger**: Borrower computing tax-bomb sinking-fund target
  using gross market return ~7-8% / yr without distinguishing
  pre-tax vs after-tax growth rate.
- **Failure-mode**: Borrower needs $70k future-value at year 20
  to cover tax bomb; sizes contribution at $30k present-value
  assuming 7% growth × 20 years = ~$116k future-value (covers
  with margin); actual after-tax accumulation (with ~1% LTCG
  drag and ~2% qualified-dividend tax) is ~6% / yr × 20 years =
  ~$96k future-value; combined with conservative scenario where
  market underperforms expectation, borrower is $15-25k short of
  tax-bomb need in forgiveness year.
- **Recovery-move**: Use after-tax expected return (subtract ~1-1.5
  percentage points from gross for typical taxable-brokerage drag)
  for sinking-fund sizing. Prefer tax-efficient ETFs (low-turnover,
  qualified-dividend-heavy) to minimize drag. Consider holding
  sinking fund in a state-tax-free vehicle (muni-bond ETF for
  high-state-tax borrowers) if liquidity needs are met. For
  borrowers with retirement-account room, use tax-advantaged
  vehicles for the sinking fund where possible (Roth IRA for
  contribution-basis-flexibility — sinking fund in Roth gives
  tax-free growth, basis available without penalty at any age).
  Cross-edge to `personal-finance` asset-location.

---

## F9 — Consumer-protection / anti-predatory-lending framing

### 9.1 All private-refi solicitations treated as adversarial when many are appropriate

- **Statement**: The asker (often coached by SLBA / NCLC voice)
  treats every private-lender refinance solicitation as
  adversarial / predatory, missing that for high-credit-tier
  professionals with no plausible PSLF or disability path, the
  rate-savings are real and the federal protections are out-of-
  the-money.
- **Source-evidence**: [`framings.md` F9 first Excludes bullet](./framings.md) —
  "Treats every private-lender refinance solicitation as
  adversarial when many private refinance products are
  *appropriate* for the borrower's situation (high-credit-tier
  professional with no plausible PSLF path); the framing's anti-
  private-refi reflex costs borrowers who would benefit from
  refinancing the rate savings." Opposes F4 (rate-spread-
  arithmetic).
- **Trigger**: Asker with high comp (top-quartile professional),
  stable industry, no plausible PSLF / disability path, AND
  reflexively quoting "the servicer is not your friend" / "don't
  trust SoFi" / consumer-protection language as the dispositive
  argument against refi.
- **Failure-mode**: Tech worker with $300k income, $200k federal
  balance at 7%, no PSLF or disability path; refuses SoFi refi at
  5% based on "private lenders are predatory"; pays $4k/yr extra
  in interest for federal protections worth ~$200/yr in expected-
  value to this profile; over 5-year accelerated payoff, ~$20k of
  foregone savings for protection that won't fire.
- **Recovery-move**: Distinguish predatory-pattern lending (high-
  fee, variable-rate-with-aggressive-reset, cosigner-trap
  marketed to vulnerable populations) from rate-arbitrage refi
  (transparent fixed-rate, regulated lender, top-tier pricing for
  top-credit borrowers). The first is the F9 target; the second
  is the F4 target. For borrowers in the high-credit / stable-
  career profile, capture the rate spread. For ambiguous cases,
  consult CFPB student-loan complaint database for the specific
  lender and product. Cross-edge to F4, D1.

### 9.2 Bankruptcy-discharge post-2022 DOJ guidance oversold even when softening is real

- **Statement**: The asker hears "you can discharge student loans
  in bankruptcy now under the 2022 DOJ-USDOE guidance" and
  treats discharge as a reliable path; the bar has softened but
  realistic discharge rate is still well under 50% in most
  districts even when borrowers actually file.
- **Source-evidence**: [`framings.md` F9 second Excludes bullet](./framings.md) —
  "Doesn't see that the post-2022 DOJ-USDOE bankruptcy-discharge
  attestation guidance has softened the *Brunner* / *Frost* bar
  but the discharge bar remains highly fact-specific — the
  framing's 'discharge is now possible' oversells the realistic
  rate of successful discharges." Statutory anchor: 11 U.S.C.
  §523(a)(8), 2022 DOJ-USDOE Joint Attestation Guidance.
- **Trigger**: Borrower in severe financial distress mentions
  "bankruptcy discharge" as a planned strategy AND has heard
  about 2022 DOJ guidance AND treats the softening as if it makes
  discharge routine.
- **Failure-mode**: Borrower files Chapter 7 + adversary proceeding
  for student-loan discharge expecting 50%+ success; case is
  denied on *Brunner* prongs that DOJ guidance didn't override
  (good-faith effort prong is often the sticking point for
  borrowers who haven't been on IDR); borrower has Chapter 7 on
  credit report for 10 years AND still owes the student-loan
  balance.
- **Recovery-move**: For borrowers considering bankruptcy
  discharge of student loans, **route to a NACBA-affiliated
  bankruptcy attorney** for case-specific evaluation — discharge
  rates vary widely by district, by judge, by borrower's history
  on IDR plans, and by the strength of the undue-hardship narrative.
  Before discharge, exhaust default-rehabilitation (9 on-time
  payments restores federal protections), IDR-forgiveness
  trajectory, and PSLF-buyback options. Bankruptcy is appropriate
  for narrow set of cases (long-term inability to pay despite
  good-faith IDR participation); not appropriate as a tactical
  first-move. Cross-edge to F13, D1.

### 9.3 FSA Ombudsman / escalation ladder operational cost under-weighted

- **Statement**: The asker is pointed to the FSA Ombudsman Group →
  SLBA / NCLC → state AG → district-court litigation escalation
  ladder as the path for servicer disputes, without acknowledging
  the time-to-resolution at each step is months to years.
- **Source-evidence**: [`framings.md` F9 third Excludes bullet](./framings.md) —
  "Under-weights the *operational* path through the FSA Ombudsman
  Group → SLBA / NCLC referral → state-AG complaint → district-
  court litigation — the framing names the escalation ladder but
  the time-to-resolution at each step is months to years and the
  framing's 'use the escalation channel' understates the lived
  cost of navigating it. Borrowers in active servicer disputes
  often pay down the disputed balance rather than wait on the
  escalation outcome."
- **Trigger**: Borrower in active servicer dispute (PSLF count
  discrepancy, IDR recertification error, forbearance-steering
  remediation request) considering escalation but not aware of
  realistic time-to-resolution.
- **Failure-mode**: Borrower files PSLF qualifying-payment dispute
  with MOHELA, denied; files with FSA Ombudsman, 6-9 month
  resolution timeline; escalates to SLBA, 3-6 months for
  consultation; potentially state-AG, months more; total elapsed
  time 1-3 years; in the meantime borrower is making payments on
  loans they believe will be forgiven, accruing interest on
  disputed balance, and paying out-of-pocket for what may
  retroactively be reclassified as qualifying payments.
- **Recovery-move**: Set realistic time-to-resolution expectations
  upfront (12-36 months for full escalation ladder is typical).
  Document everything in date-stamped records during the wait.
  For borrowers with PSLF approaching year 10, file escalation
  early (year 7-8) so resolution is in hand by forgiveness window.
  **Route to FSA Ombudsman Group ($0-cost escalation, file
  directly via StudentAid.gov) as first escalation step** before
  retaining paid counsel. For unresolved cases at year 9+ approaching
  forgiveness, **route to a student-loan attorney or SLBA /
  NCLC** for direct litigation prep. Cross-edge to D10, F12.

### 9.4 Parent-borrower informed-consent gap on Parent PLUS missed when refi-out is the proposed fix

- **Statement**: The asker recognizes Parent PLUS is debt in
  parent's name (not student's), and the proposed fix is to "re-
  paper the loan into the student's name via private refi" — but
  this triggers federal-protection-erasure that the framing's own
  anti-private-refi reflex should object to.
- **Source-evidence**: [`framings.md` F9 fourth Excludes bullet](./framings.md) —
  "Glosses over the *parent-borrower* informed-consent gap on
  Parent PLUS: many parents don't realize Parent PLUS is debt in
  *their* name (not the student's) until the first credit-report
  pull or co-signed apartment lease. The framing's 'Parent PLUS
  disclosure is inadequate' is correct but the operational fix
  (re-papering the loan into the student's name via private refi)
  has the federal-protection-erasure cost the framing's own anti-
  private-refi reflex should object to — internal tension within
  the framing." Decisions.md D7 cross-edge.
- **Trigger**: Parent realizes Parent PLUS is parental debt, wants
  to transfer to adult child via private refi, AND has not been
  walked through the federal-protection-loss (§437(a) discharge
  on parent death, IDR-via-ICR-after-consolidation, in-school
  deferment for grad school) the transfer eliminates.
- **Failure-mode**: Parent in late-50s transfers $80k Parent PLUS
  to adult-child SoFi refi at 6% (vs Parent PLUS 9.08%); child
  has no federal protections on the new debt; parent dies year 7
  of the loan term; under Parent PLUS the balance would have
  discharged under §437(a); under private refi the child owes the
  $80k balance; saved ~$20k in interest over 7 years but lost
  $80k of discharge protection.
- **Recovery-move**: For Parent PLUS transfers to student name,
  surface §437(a) discharge value explicitly. For parents 55+
  with health uncertainty, the discharge protection often exceeds
  the rate-spread savings. For families committed to the
  refi-to-student-name path, consider term-life insurance on the
  parent equal to outstanding balance (cheap for healthy 50s) as
  a partial hedge. **Route to a fee-only fiduciary CFP** for the
  joint refi + insurance analysis. Cross-edge to D7, F4 third
  Excludes (cosigner-asymmetry), `housing` (HELOC-as-college-
  funding-alternative).

### 9.5 For-profit-college-targeting treated as historical when surviving-borrower population is still exposed

- **Statement**: The asker treats the for-profit-college predatory-
  targeting era as resolved by Borrower Defense and post-2015
  enforcement, missing that the underlying population of
  borrowers who attended Corinthian / ITT / Argosy / DeVry / similar
  still face ongoing credit-damage and balance-without-degree even
  after Borrower Defense relief.
- **Source-evidence**: [`framings.md` F9 fifth Excludes bullet](./framings.md) —
  "Frames for-profit-college-targeting as if it had been resolved
  by Borrower Defense and the 2015-and-after enforcement actions;
  the underlying population of borrowers who attended Corinthian
  / ITT / Argosy / DeVry / similar still face credit-damage,
  spousal-credit-pull complications, and ongoing loan-balance-
  with-no-degree even after Borrower Defense relief."
- **Trigger**: Borrower attended a closed-or-discredited for-profit
  school (Corinthian, ITT Tech, Argosy, Westwood, Education
  Management Corporation chains, others) AND has not filed
  Borrower Defense to Repayment claim OR has had claim denied OR
  has lingering credit-damage from pre-discharge collection
  activity.
- **Failure-mode**: Former Corinthian student has $40k of federal
  balance, didn't complete degree, hasn't filed Borrower Defense;
  loan is in collection; credit score sub-600; can't qualify for
  apartment lease without high security deposit; refused mortgage;
  spouse's credit affected via joint accounts. The school-closure
  + cohort-default-rate relief and the Borrower Defense
  expansion would apply but the borrower doesn't know.
- **Recovery-move**: For borrowers who attended any closed-or-
  discredited for-profit school, file Borrower Defense to
  Repayment claim via StudentAid.gov (free, no attorney required
  for application). Document attendance dates, marketing
  materials, job-placement claims made by the school. For
  rejected claims or complex cases, **route to SLBA / NCLC** for
  attorney-assisted appeal. For surviving credit-damage, file
  TransUnion / Experian / Equifax disputes citing the school-
  closure / fraud finding; some disputes succeed in removing
  derogatory tradelines. Cross-edge to D1, F13.

---

## F10 — FIRE-aware-college-funding / retirement-priority framing

### 10.1 Parental-retirement-readiness treated as binary cutoff when household-level optimization is continuous

- **Statement**: The asker treats "are parents on track for
  retirement?" as a binary on/off gate to college funding,
  missing that the actual optimization is continuous — the
  marginal 529 dollar trades against the marginal 401k dollar at
  a household-specific rate-of-return.
- **Source-evidence**: [`framings.md` F10 first Excludes bullet](./framings.md) —
  "Treats parental-retirement-readiness as binary (on-track vs not)
  when in reality the distribution is continuous and the marginal
  529 dollar trades against the marginal 401k dollar at a household-
  specific rate of return. The framing's 'fund retirement to 15-25%
  THEN start the 529' creates a discrete cutoff that doesn't match
  the actual optimization." Opposes F2 (529-state-deduction).
- **Trigger**: Asker uses Fidelity-style targets (1× by 30, 3× by
  40, 6× by 50, 8× by 60) as gate and either (a) stops all 529
  funding until retirement is "caught up" or (b) ignores
  retirement-priority entirely because the targets feel
  unattainable.
- **Failure-mode**: Family at age 42 with 2× income retirement
  balance (below 3× target); stops all 529 funding pending
  retirement-catchup; child entering college at parent age 50
  with $0 in 529; family takes Parent PLUS at 9.08% for the full
  cost; net household NPV worse than partial 529 + partial
  retirement funding because Parent PLUS-rate dominates the
  marginal-return trade-off.
- **Recovery-move**: Build a continuous-allocation model: for each
  marginal dollar, model the after-tax return in retirement
  account vs 529 vs Parent-PLUS-avoided. Most households benefit
  from concurrent funding (e.g. 70% retirement / 30% 529 of
  surplus) rather than sequential funding. State-deduction value
  on 529 contribution + tax-free growth at long horizon often
  competes with retirement-account growth for the marginal dollar.
  For high-income households where retirement-account limits are
  binding, the 529 receives more of the surplus by default. For
  households late to retirement saving AND with kids approaching
  college, **route to a fee-only fiduciary CFP** for the multi-
  goal allocation analysis.

### 10.2 Parent-401k vs kid-529 framing assumes unified household decision-making

- **Statement**: The asker (often a personal-finance-advice
  generator) frames "parents fund retirement first" as if it
  were a single decision-maker's choice, missing that in many
  two-income households the employed-parent's 401k is one
  decision channel and the household-budget-decision-maker funds
  the 529 from after-tax income as a separate channel.
- **Source-evidence**: [`framings.md` F10 second Excludes bullet](./framings.md) —
  "Doesn't see that the *parent-401k-contribution* and *kid-529-
  contribution* may live in different decision-makers' control
  (e.g. employed-parent's 401k, household-budget-decision-maker
  funds the 529 from after-tax income); the framing's 'parents
  fund retirement first' assumes unified household optimization
  that doesn't always exist in two-income households with
  different account-decision-rights."
- **Trigger**: Two-income household where one parent's 401k
  contribution rate is set by their employer-default + occasional
  manual adjustment, the other parent's 401k is similarly
  separate, AND the 529 is funded from joint checking via the
  parent who manages the household budget.
- **Failure-mode**: Household budget-manager allocates $1k/mo to
  529 from after-tax cash flow without realizing the other
  spouse's 401k contribution rate is below their employer match
  threshold (e.g. spouse contributes 3% to 401k where employer
  matches 6%); household is leaving $4-6k/yr of free 401k match
  on the table while funding 529 at full rate; the framing's
  "fund retirement first" never reaches the household-allocation
  layer because the 401k decision isn't on the budget-meeting
  agenda.
- **Recovery-move**: For two-income households with separate 401k
  decision rights, the FIRST step is "both spouses' 401k
  contribution rate covers full employer match" — this is the
  household-level retirement-priority step. After that, the 529
  allocation can be debated on its merits. Surface this
  explicitly in any college-funding conversation by asking "what's
  each spouse's 401k contribution rate and employer match?" before
  discussing 529 cadence. Cross-edge to `tech-career` (employer
  match in tech) and `personal-finance` (retirement-priority).

### 10.3 Grandparent-funding path orthogonal to parental-retirement trade-off — under-priced

- **Statement**: The asker applies the "parents fund retirement
  first" reflex to all college funding, missing that grandparent-
  529 contributions (especially post-Simplification, where
  grandparent distributions don't count as student income) are a
  funding source orthogonal to parental retirement — the framing's
  trade-off doesn't apply.
- **Source-evidence**: [`framings.md` F10 third Excludes bullet](./framings.md) —
  "Under-weights the *grandparent-funding* path that doesn't trade
  off against parental retirement at all — grandparent-529
  (especially post-Simplification with grandparent-distributions
  removed from student-income) is a funding source independent of
  the parental-retirement question; the framing's 'retirement
  priority' applies to the parent-as-funder but the same household
  may have grandparent-funding-availability the framing under-
  prices." Cross-routes `family-planning`. Statutory anchor:
  FAFSA Simplification Act.
- **Trigger**: Family has grandparents with discretionary capital
  AND parents are below retirement-target, AND family is debating
  parental 529 contribution sizing as if grandparent funding
  weren't available.
- **Failure-mode**: Family applies retirement-priority reflex
  rigorously, postpones kid's 529 funding until parents catch up;
  grandparents would have happily 5-year-elected $190k into kid's
  529 but weren't asked; kid arrives at college with parent-funded
  $40k and ends up Parent-PLUS-borrowing $80k+ for the gap; family
  could have had the same outcome with grandparent funding +
  parental-retirement focus.
- **Recovery-move**: For families with retired or retiring
  grandparents (especially those using lifetime estate-tax
  exemption before 2026 TCJA sunset), explicitly surface
  grandparent-529 as a funding source separate from parental
  retirement-vs-college trade-off. For grandparents with
  significant estate, 5-year-forward election ($95k single / $190k
  MFJ per donor per beneficiary) under §529(c)(2)(B) is the
  highest-leverage estate-planning + college-funding move. **Route
  to a retirement-experienced CPA with §529 history** for the
  Form 709 filing and estate-tax-exemption coordination. Cross-
  edge to F2 (529-state-deduction), F5 (FAFSA-base-year), `family-
  planning` decision on inter-generational gifting.

### 10.4 Positional / status component of college-funding under-priced when peer-group norms diverge from FIRE ethos

- **Statement**: The asker (often steeped in r/financialindependence
  / MMM voice) treats retirement-priority as universally applicable,
  missing that for households embedded in peer-groups where
  private-school funding is treated as table-stakes (legacy /
  prep-school / Ivy-family contexts), the FIRE ethos bumps
  against social-context for many families.
- **Source-evidence**: [`framings.md` F10 fourth Excludes bullet](./framings.md) —
  "Glosses over the *positional* / status component of college-
  funding decisions: many parents whose retirement is genuinely
  on-track still under-fund kids' college relative to peer-group
  norms (the framing's 'retirement-first ethos' is alien to
  households where neighbors / extended family treat private-
  school funding as table-stakes)."
- **Trigger**: Household in high-income tech / finance / medicine
  professional bracket, embedded in social context where private-
  K-12 / Ivy-target / full-pay-college is the norm, applies FIRE
  reflex to college-funding without acknowledging the social-
  context cost.
- **Failure-mode**: Family pushes kid toward in-state flagship for
  FIRE-aligned reasons; kid feels socially marked relative to
  peers heading to private colleges; family-dynamics suffer;
  extended family / grandparents intervene with funding offers
  that come with strings; the FIRE win on retirement was real
  but the household-relationship cost was unbudgeted.
- **Recovery-move**: Name the positional / status dimension
  explicitly as a real input to the decision, not a weakness to
  be overcome. For families embedded in private-school /
  Ivy-target peer groups, the marginal value of "kid attends
  private vs flagship-public" includes the social-context
  component, which is legitimately variable across households.
  The FIRE prescription applies cleanly for households whose
  social context tolerates flagship-public outcomes; for others,
  the framework needs the social-context input. Cross-edge to F3
  (ROI-by-major-and-program — for many social-context-driven
  decisions, the ROI-by-program argument is still load-bearing).

### 10.5 Parent PLUS treated as uniformly worse than 401k contribution when §221 deduction lowers after-tax rate

- **Statement**: The asker compares Parent PLUS at nominal 9.08%
  against 401k-match expected return as if the Parent PLUS rate
  were pre-tax, missing that PLUS interest is deductible under IRC
  §221 (student-loan-interest deduction up to $2,500/year, AGI
  phase-out at $200k MFJ / $100k single).
- **Source-evidence**: [`framings.md` F10 fifth Excludes bullet](./framings.md) —
  "Frames Parent PLUS as uniformly worse than 401k-contribution on
  rate-of-return grounds when in fact Parent PLUS interest is
  deductible under IRC §221 (student-loan-interest deduction up to
  $2,500/year, AGI phase-out), so the after-tax effective rate is
  lower than the nominal 9.08% — the framing's rate comparison
  needs to be net-of-deduction for the parents in the AGI phase-
  in range." Statutory anchor: IRC §221.
- **Trigger**: Family with AGI in the §221 deduction-eligible range
  ($170k-$200k MFJ / $80k-$100k single 2026 phaseouts, indexed)
  considering Parent PLUS vs reducing 401k contribution to fund
  college, AND comparing pre-tax PLUS rate to 401k-match return.
- **Failure-mode**: MFJ family at $180k AGI with Parent PLUS
  balance $30k at 9.08%; interest paid year 1 ~$2,500; §221
  deduction available; saves ~$550 federal tax (22% marginal) +
  ~$170 state (NJ); after-tax effective rate is ~7.7%; family
  decided to take PLUS over reducing 401k contribution comparing
  9.08% vs 8% match-included expected return, but at 7.7%
  effective rate the comparison flips. Or alternatively, family
  refused PLUS and reduced 401k contribution to fund college,
  losing match — wrong direction.
- **Recovery-move**: For families in §221 deduction-eligible range,
  compute the after-tax effective rate on Parent PLUS (interest
  paid × applicable federal + state marginal × ratio of $2,500-cap
  to interest-paid) and use that for the cross-comparison vs 401k-
  contribution-foregone. For families above $200k MFJ AGI (phased
  out of §221), use the nominal rate. For Parent PLUS held
  through retirement-saving years, the §221 deduction is an annual
  benefit, not one-time. Cross-edge to D7, `personal-finance`
  asset-location.

---

## F11 — Employer-tuition / §127-retention-clawback framing

### 11.1 Generic clawback-structure assumed when employer-specific terms vary widely

- **Statement**: The asker treats all employer-tuition programs as
  having a "2-year prorated clawback" without reading the
  employer's specific plan document — clawback windows, proration
  formulas, pre-approval requirements, and approved-program-lists
  vary widely.
- **Source-evidence**: [`framings.md` F11 first Excludes bullet](./framings.md) —
  "Treats every employer-tuition program as having the same
  clawback structure when in fact the clawback windows, proration
  formulas, pre-approval requirements, and approved-program-lists
  vary widely by employer; the framing's 'tuition reimbursement is
  comp with a retention lock' is structurally correct but the
  specific terms at any given employer often deviate from the
  typical 2-year prorated-clawback — borrowers need to read their
  employer's tuition-reimbursement plan document, not the
  framing's generic terms."
- **Trigger**: Asker mentions employer-tuition reimbursement as
  funding strategy but hasn't named the specific clawback terms
  (length, proration, trigger events, repayment cap).
- **Failure-mode**: Engineer enrolls in part-time MBA assuming
  "typical 2-year clawback"; actually employer's plan is 4-year
  full clawback (no proration) AND triggers on competitor
  employment within 5 years; engineer gets recruited by competitor
  in year 3; owes full $40k tuition reimbursement back to old
  employer + transitions to new employer with cash-flow shock;
  framing's generic-terms assumption left this unbudgeted.
- **Recovery-move**: Before enrollment, obtain and read the
  employer's specific tuition-reimbursement plan document.
  Specifically identify: (a) clawback length, (b) proration
  schedule, (c) trigger events (voluntary departure, layoff,
  competitor employment, geographic relocation), (d) repayment cap
  vs full amount, (e) pre-enrollment approval requirements, (f)
  approved-program-list and prior-approval procedure. For
  programs with long clawback / no proration / competitor-
  exclusion, the program is significantly less valuable than the
  generic "2-year clawback" framing suggests. Model the
  realistic stay-at-employer probability over the clawback
  window. Cross-edge to `tech-career` (job-hopping rate in field).

### 11.2 §127 cap timing on 1-year intensive programs leaves half the capacity unused

- **Statement**: The asker doesn't realize §127 is an annual cap
  ($5,250 per calendar year), so a 1-year intensive program loses
  half the §127 capacity that a 2-year part-time program can use;
  the framing optimizes for 2-3 year part-time programs.
- **Source-evidence**: [`framings.md` F11 second Excludes bullet](./framings.md) —
  "Doesn't see the *§127 cap timing* mechanic: §127 is an annual
  cap ($5,250/calendar year), so a 2-year part-time program can
  use $10,500 total of §127 exclusion across 2 tax years; a 1-year
  intensive program loses half the §127 capacity." Statutory
  anchor: IRC §127.
- **Trigger**: Asker considers a 1-year intensive program
  (Sloan Fellows, 1-year master's, accelerated MBA) with employer
  reimbursement up to §127 cap, treating the cap as a per-program
  rather than per-calendar-year limit.
- **Failure-mode**: Engineer enrolls in 1-year intensive MS-Eng
  program with $10k tuition; employer reimburses up to $5,250
  §127 cap in calendar year 1; the remaining $4,750 is paid in
  calendar year 1 too and counts as imputed taxable income at
  marginal rate. If the program had been 2-year part-time, each
  year would have used $5,000 of the $5,250 cap with no imputed
  income, saving ~$1,500 in federal+state tax over the 2-year
  span.
- **Recovery-move**: For employer-funded programs with tuition
  near or above $5,250/yr, prefer the multi-year part-time
  structure to maximize §127 cap usage across tax years. For
  intensive programs where multi-year structure isn't an option,
  time tuition payments across calendar-year boundaries when
  possible (Dec / Jan payments split a fall semester across tax
  years). Cross-edge to D2 (full-time vs part-time MBA).

### 11.3 Scholarship-displacement assumed when timing-optimization can preserve partial stack

- **Statement**: The asker treats institutional scholarships as
  non-stackable with employer reimbursement, missing that the
  *order of application* matters — submitting the scholarship
  application before the employer-reimbursement enrollment can
  sometimes preserve the scholarship and stack with employer
  reimbursement at the §127-cap-only level.
- **Source-evidence**: [`framings.md` F11 third Excludes bullet](./framings.md) —
  "Under-weights the *scholarship-displacement* mechanic in
  detail: the school adjusts the scholarship downward if the
  employer pays first, but the *order of application* matters —
  submitting the scholarship application before the employer-
  reimbursement enrollment can sometimes preserve the scholarship
  and stack with employer reimbursement at the §127-cap-only
  level." Opposes F7 (NACAC-counselor).
- **Trigger**: Applicant eligible for institutional merit
  scholarship at part-time program AND has employer tuition-
  reimbursement available, AND is sequencing the applications
  without strategic timing.
- **Failure-mode**: Applicant accepts employer-reimbursement
  enrollment first (HR makes this easy and fast); applies for
  scholarship subsequently; school sees employer is paying first
  $5,250 of cost, reduces scholarship by the same amount; effective
  combined funding is $5,250 + ($scholarship - $5,250) = same as
  scholarship alone; applicant could have stacked $5,250 + full
  scholarship if scholarship had been applied for first.
- **Recovery-move**: Apply for institutional scholarships BEFORE
  accepting employer-reimbursement enrollment; ensure scholarship
  award letter is dated before employer-reimbursement starts. For
  some programs, this requires year-ahead planning (scholarships
  often have December / January deadlines for fall enrollment).
  Combined with §117(a) qualified-scholarship exclusion (tuition
  + required fees portion is tax-free) and §127 employer-
  reimbursement exclusion ($5,250 cap), the optimization can
  preserve significant tax-free funding above what either source
  alone provides.

### 11.4 Career-pivot-during-program creates embedded employee-call missed by framing

- **Statement**: The asker treats employer-reimbursement as pure
  comp without pricing the embedded call-on-the-employee: a
  layoff or competing-offer during years 1-2 of a multi-year
  program creates a forced choice between completing the program
  (potentially without employer support if laid off) and
  pursuing the new opportunity.
- **Source-evidence**: [`framings.md` F11 fourth Excludes bullet](./framings.md) —
  "Glosses over the *career-pivot-during-program* problem:
  enrolling in a 3-year part-time MBA with employer reimbursement
  creates a career-lock during the program (you can't quit mid-
  program without triggering clawback), so a layoff or a
  competing job offer during years 1-2 creates a forced choice
  between completing the program (potentially without employer
  support if laid off) and pursuing the new opportunity. The
  framing's 'tuition reimbursement is comp' doesn't price the
  *embedded call-on-the-employee* during the program window."
- **Trigger**: Applicant in volatile industry (tech with active
  layoff cycle, finance with bonus-cycle hiring waves, consulting
  with up-or-out culture) considers 3-4 year part-time program
  with employer reimbursement AND clawback.
- **Failure-mode**: Tech engineer enrolls in 3-year part-time MBA;
  laid off in year 2; employer still triggers clawback on the
  $30k already reimbursed (most plans treat involuntary
  separation the same as voluntary for clawback purposes —
  layoff doesn't waive); engineer owes $30k back to former
  employer AND has no employer reimbursement for years 3-4 (full
  cost ~$60k); forced choice between completing at out-of-pocket
  cost or abandoning the program mid-stream and writing the
  clawback check.
- **Recovery-move**: Before enrolling in multi-year employer-
  reimbursed program, verify clawback treatment of involuntary
  separation (some plans waive clawback on layoff; many don't).
  Build a "layoff during program" scenario into the decision —
  what's the realistic layoff probability over the program
  window? Volatile industries should weight this heavily. For
  high-layoff-risk profiles, prefer shorter programs or self-pay
  with portability over locked-in employer-reimbursement.
  Consider applying to programs with hybrid online-cohort
  flexibility that allow program-completion through job
  transitions. Cross-edge to D2 (full-time vs part-time) and
  `tech-career` (layoff-rate by industry).

### 11.5 §132(d) Working-Condition-Fringe path framed as available when most HR doesn't run it

- **Statement**: The asker treats above-§127-cap reimbursement as
  potentially excludable under §132(d) Working-Condition-Fringe
  for job-related courses, missing that most HR / payroll
  departments don't have the systems to distinguish §127 from
  §132(d) tracking — they default to §127 reporting for everything.
- **Source-evidence**: [`framings.md` F11 fifth Excludes bullet](./framings.md) —
  "Frames the §127 exclusion as if Working-Condition-Fringe
  §132(d) were practically available; in practice most HR /
  payroll departments don't have the systems to distinguish §127
  from §132(d) tracking and they default to §127 reporting for
  everything, which means above-cap reimbursement gets imputed
  even when the course is job-related enough to qualify for
  §132(d)." Statutory anchor: IRC §132(d), Treas. Reg. §1.132-5.
- **Trigger**: Asker mentions "I'll use §132(d) for the above-cap
  portion since my MS-CS is clearly job-related to my software-
  engineering role", AND has not verified employer payroll
  treatment of §132(d) for tuition reimbursement.
- **Failure-mode**: Engineer enrolls in $10k/yr MS-CS program at
  employer with $5,250 §127 cap; expects §132(d) treatment for
  the $4,750 over-cap portion (clearly job-related); employer
  payroll department defaults to §127 reporting only, treats the
  $4,750 as W-2 wages imputed at year-end; engineer owes
  marginal-rate federal + state + FICA on $4,750 = ~$1,800
  unbudgeted tax bill.
- **Recovery-move**: Before enrollment, verify employer payroll
  treatment of above-§127-cap reimbursement explicitly with HR.
  For employers that do NOT run §132(d), budget the marginal-tax
  cost on the above-cap portion as part of program-cost analysis.
  For employers that DO run §132(d) (rare at large companies,
  more common at small employers and educational institutions),
  document job-relatedness with a written letter from manager
  citing the course-to-role connection. Cross-edge to D9.

---

## F12 — ARPA-cliff-aware / political-risk framing

### 12.1 Political-risk anchored on loss when historical changes have been net-positive for low/mid-income borrowers

- **Statement**: The asker uses generic "political risk on
  federal-loan-program" as a reason to refi out of federal,
  anchoring on loss-scenarios — when the historical population of
  recent rule-changes is net-positive for low-and-middle-income
  borrowers (2022 one-time forgiveness, account-adjustment, SAVE
  when active, Borrower Defense expansion).
- **Source-evidence**: [`framings.md` F12 first Excludes bullet](./framings.md) —
  "Treats political-risk as if it cuts uniformly against the
  borrower; in fact some political risks cut *in favor of* the
  borrower (the 2022 Biden one-time forgiveness, the SAVE plan's
  5%/225%-poverty mechanics when it was active, the 2022-2024
  account-adjustment that captured millions of qualifying
  payments). The framing's 'the rules can get worse' anchors on
  loss but the population of recent rule-changes is net-positive
  for low-and-middle-income borrowers." Opposes F8 (tax-bomb-
  arithmetic).
- **Trigger**: Asker references "political risk" / "the rules can
  change" as primary reason to refi federal-to-private, AND
  doesn't distinguish loss-scenarios from gain-scenarios in the
  political-risk landscape.
- **Failure-mode**: Borrower refis federal-to-private to hedge
  generic political risk in 2024; subsequent administrative-rule
  expansion (Borrower Defense relief cohort, account-adjustment
  windows for additional categories of borrowers) provides
  forgiveness or count-correction to borrower's original federal-
  loan profile; borrower had already refi'd out and cannot benefit.
- **Recovery-move**: Build a balanced political-risk inventory:
  (a) loss-scenarios — ARPA cliff at end-2025, IDR-payment-
  recertification timing tightening, hypothetical PSLF reform; (b)
  gain-scenarios — periodic one-time forgiveness waves, ongoing
  account-adjustment expansion, Borrower Defense cohort expansion,
  IDR plan introduction (post-SAVE rulemaking). For borrowers
  with PSLF / disability / lower-income trajectory, gain-scenarios
  outweigh loss-scenarios historically. For high-income borrowers
  on standard repayment, the asymmetry is smaller. Cross-edge to
  F1 third Excludes (political-risk net direction).

### 12.2 Account-adjustment one-time-window urgency under-stated for forbearance-steered borrowers

- **Statement**: The asker names the 2022-2024 account-adjustment
  but doesn't communicate the closing window's urgency; borrowers
  who haven't filed by the deadline lose the corrective for prior
  forbearance / non-IDR periods.
- **Source-evidence**: [`framings.md` F12 second Excludes bullet](./framings.md) —
  "Doesn't see that the *account-adjustment* is a one-time
  opportunity with a closing window; borrowers who haven't filed
  by the deadline lose the corrective for prior forbearance /
  non-IDR periods. The framing names the window but understates
  the urgency for borrowers whose servicer-history includes
  documented forbearance-steering."
- **Trigger**: Borrower with pre-2018 federal-loan history
  (Navient / FedLoan era) AND documented or suspected
  forbearance-steering AND has not filed for account-adjustment
  review.
- **Failure-mode**: Borrower has 24 months of pre-2018
  administrative forbearance that under account-adjustment rules
  would convert to qualifying payments for PSLF / IDR-forgiveness;
  borrower hasn't filed by the closing deadline; loses 2 years of
  qualifying payment credit ~$30k+ of present-value loan
  forgiveness; PSLF trajectory pushed back 2 years.
- **Recovery-move**: For any borrower with pre-2018 federal-loan
  history, file for account-adjustment review via StudentAid.gov
  IMMEDIATELY (the original deadlines have been extended several
  times but the window remains closing). The process is free, no
  attorney required for initial filing. Document any
  forbearance-steering instances with date-stamped records of
  servicer communications. For complex cases or after denial,
  **route to SLBA / NCLC or FSA Ombudsman Group** for assisted
  appeal. Cross-edge to F9, D10.

### 12.3 Borrower Defense as political-risk *opportunity* (not threat) under-surfaced

- **Statement**: The asker frames Borrower Defense to Repayment
  under HEA §455(h) as a narrow remedy when it's actually a
  political-risk *opportunity* — relief expansion under the
  2022-2024 cohorts can fully discharge federal balances and
  includes tax-free treatment under §108(f)(1)-analog mechanics.
- **Source-evidence**: [`framings.md` F12 third Excludes bullet](./framings.md) —
  "Under-weights the *Borrower Defense to Repayment* path under
  HEA §455(h) for borrowers attending schools later found to have
  engaged in misrepresentation — Borrower Defense relief can
  fully discharge federal balances and includes tax-free treatment
  under §108(f)(1)-analog mechanics. The framing's 'political
  risk on the federal bundle' doesn't surface Borrower Defense as
  a political-risk *opportunity* (relief expansion under the 2022-
  2024 cohorts) vs threat." Statutory anchor: HEA §455(h),
  34 CFR §685.222.
- **Trigger**: Borrower attended any school that has been subject
  to USDOE enforcement action, state-AG action, FTC action, or
  has been included in a Borrower Defense relief cohort (any
  Corinthian, ITT, Argosy, DeVry, ITT Tech, EDMC, ECMC, Walden,
  University of Phoenix, Westwood, others — list expands
  periodically).
- **Failure-mode**: Borrower has $80k federal balance from a
  school later included in BDR cohort; borrower has been paying
  on the loans for years thinking no recourse available; loses
  $80k+ of potential forgiveness because they didn't know to file
  BDR.
- **Recovery-move**: Maintain awareness of the BDR cohort list
  (USDOE publishes; SLBA and NCLC also track) and check for any
  school the borrower attended. File BDR via StudentAid.gov
  (free, no attorney required for cohort-eligible applications).
  For ambiguous cases (school not in cohort but pattern of
  misrepresentation), **route to SLBA / NCLC** for case-specific
  evaluation before filing. Cross-edge to F9 fifth Excludes
  (for-profit-college-targeting).

### 12.4 State-conformity dimension to political risk not extended to state legislatures

- **Statement**: The asker tracks federal political-risk (ARPA
  cliff, PSLF eligibility rules) but doesn't extend the
  political-risk lens to state-conformity decisions made
  independently by each state legislature.
- **Source-evidence**: [`framings.md` F12 fourth Excludes bullet](./framings.md) —
  "Glosses over the *state-conformity* dimension to political-
  risk: even when federal ARPA §9675 excludes the forgiven
  amount, state conformity is uneven and changes year-to-year —
  CA, MS, IN, NC, WI didn't conform to the 2022 one-time
  exclusion. The framing's 'political risk on the federal bundle'
  needs to extend to state-conformity decisions made
  independently by each state legislature."
- **Trigger**: Borrower in non-conforming state (CA, MS, IN, NC,
  WI, others) tracking federal political-risk but treating state-
  conformity as automatic following federal action.
- **Failure-mode**: California borrower assumes if ARPA-cliff
  extends federally, no state tax on forgiveness; CA may continue
  to not conform; $200k forgiveness at 9.3% CA marginal = $18,600
  CA tax unbudgeted; the political-risk lens caught the federal
  dimension but missed the state.
- **Recovery-move**: For borrowers in non-conforming states,
  track BOTH federal and state political-risk separately. Monitor
  state revenue department guidance on conformity to federal
  student-loan exclusions (typically issued in late spring of
  each year for the prior tax year). Size sinking-fund to the
  combined federal+state exposure. For borrowers approaching
  forgiveness, consider state-residency timing as a planning
  lever (changing residency to a conforming state in the
  forgiveness year may be legitimate planning, fact-specific).
  Cross-edge to F8 (state-tax-bomb).

### 12.5 Federal-loan-program systemic risk overstated relative to documented stability

- **Statement**: The asker treats "the rules can change" as
  evidence the federal-loan-program is unstable, when in fact
  the program's *core* features (Direct loans, IDR plans, PSLF,
  federal interest-rate-set-annually-by-statute) have been
  remarkably stable across administrations even through
  rulemaking churn on specific IDR terms.
- **Source-evidence**: [`framings.md` F12 fifth Excludes bullet](./framings.md) —
  "Frames the federal-loan-program as if its future were
  unpredictable; in fact the program's *core* features (Direct
  loans, IDR plans, PSLF, the federal interest-rate-set-annually-
  by-statute) have been remarkably stable across administrations
  even through rulemaking churn on the specific IDR terms. The
  framing's 'the rules can change' over-states the systemic risk
  relative to the documented pace of meaningful change."
- **Trigger**: Asker treats political-risk as reason to abandon
  long-horizon federal strategy (PSLF, IDR-forgiveness) entirely,
  treating any program-rule-change-rumor as cause to refi out.
- **Failure-mode**: Borrower at PSLF year 6 abandons the path and
  refis out citing "the program could change", losing $80k+ of
  near-term tax-free forgiveness; the program's core PSLF
  forgiveness mechanic doesn't change; borrower writes off the
  forgiveness benefit for protection against a non-event.
- **Recovery-move**: Distinguish core-program-features (very
  stable across administrations) from specific-IDR-plan-terms
  (subject to rulemaking churn). PSLF qualifying-payment-count +
  qualifying-employer mechanics have been stable; specific IDR
  payment formulas have been variable. For borrowers deep into
  PSLF (year 5+), the core mechanic is highly likely to fire.
  For borrowers on IDR-forgiveness-only paths, the
  variability is real but bounded. File annual ECF to lock in
  qualifying-employment-and-payment counts on the *current*
  rule set, which provides protection against retroactive rule
  changes. Cross-edge to D10, F1.

---

## F13 — Bankruptcy-discharge-and-default-recovery framing

### 13.1 Post-2022 *Brunner*-softening oversold relative to operational discharge rate

- **Statement**: The asker treats the 2022 DOJ-USDOE attestation
  guidance as making bankruptcy discharge of student loans
  routine, missing that operational discharge rate is still well
  under 50% in most districts even when borrowers actually file.
- **Source-evidence**: [`framings.md` F13 first Excludes bullet](./framings.md) —
  "Oversells the post-2022 DOJ guidance softening of *Brunner*;
  while discharge rates have risen, the realistic rate is still
  well under 50% in most districts even when borrowers actually
  file. Many borrowers learn about the discharge path but don't
  file because the bankruptcy-itself cost (credit damage,
  attorney fees, chapter-7-or-13 procedural complexity)
  dominates."
- **Trigger**: Borrower considering bankruptcy discharge as
  tactical move (not as last-resort), citing DOJ guidance as
  evidence of high success probability.
- **Failure-mode**: Borrower files Chapter 7 + adversary
  proceeding for $80k student loan discharge expecting 50%+
  success; bankruptcy court denies discharge on *Brunner* good-
  faith-effort prong (borrower hadn't been on IDR for sufficient
  duration); borrower has Chapter 7 on credit report 10 years +
  attorney fees $5-10k + still owes $80k student loan; net
  position significantly worse than pre-filing.
- **Recovery-move**: Bankruptcy discharge of student loans is
  appropriate for narrow set of cases (long-term inability to pay
  despite good-faith IDR participation); not appropriate as
  tactical first-move. **Route to NACBA-affiliated bankruptcy
  attorney** for case-specific evaluation including district-
  specific discharge-rate research. Before filing, exhaust
  default-rehabilitation (D1 cross-edge), IDR-forgiveness
  trajectory (D4), and PSLF-Buyback (D10). For borrowers in
  severe distress without these options exhausted, work the
  alternatives first; bankruptcy as last resort. Cross-edge to
  F9.

### 13.2 Default-rehabilitation lifetime-limit missed when treating as repeatable strategy

- **Statement**: The asker treats "rehabilitate then choose IDR"
  as a repeatable strategy, missing that default-rehabilitation
  has a one-time-per-loan limit; a borrower who rehabilitates
  and then defaults again has used the rehabilitation card.
- **Source-evidence**: [`framings.md` F13 second Excludes bullet](./framings.md) —
  "Doesn't see that the *default-rehabilitation* path has a
  one-time-per-loan limit; a borrower who rehabilitates and then
  defaults again has used the rehabilitation card. The framing's
  'rehabilitate then choose IDR' is the right starting move but
  the lifetime-limit means it's not a repeatable strategy."
  Statutory anchor: HEA §428F (rehabilitation), 34 CFR §685.211.
- **Trigger**: Borrower has previously rehabilitated a defaulted
  federal loan AND is in default again, considering second
  rehabilitation.
- **Failure-mode**: Borrower rehabilitated 2018 default; defaulted
  again 2024 due to job loss; tries to file second rehabilitation;
  servicer denies (one-time-per-loan limit); borrower's only
  options are consolidation-to-cure (which DOES still work for
  second defaults), wage-garnishment-cure, settlement
  negotiation, or bankruptcy discharge consideration; the
  rehabilitation card has been used and isn't available again.
- **Recovery-move**: For borrowers approaching second default,
  treat rehabilitation as a one-time tool — exhaust hardship
  forbearance, IDR-recertification (income-based payment may be
  $0 at low income), unemployment deferment, military deferment
  before defaulting. For borrowers in second default, consolidate
  the defaulted loans (consolidation-to-cure works for second
  defaults) rather than rehabilitate; the consolidation resets
  IDR-eligibility without using the rehabilitation card. **Route
  to SLBA / NCLC** for default-recovery case management when the
  rehabilitation card is gone. Cross-edge to D1, F9.

### 13.3 Post-discharge tax-treatment under §108(a)(1)(A) bankruptcy exclusion under-surfaced

- **Statement**: The asker compares bankruptcy discharge against
  IDR-forgiveness math without seeing that bankruptcy discharge
  of student-loan debt is excluded from income under IRC
  §108(a)(1)(A) — discharge is *tax-free* even when ARPA cliffs
  out and IDR-forgiveness becomes taxable.
- **Source-evidence**: [`framings.md` F13 third Excludes bullet](./framings.md) —
  "Under-weights the *post-discharge* tax-treatment: bankruptcy
  discharge of student-loan debt is excluded from income under
  IRC §108(a)(1)(A), so there's no tax-bomb on discharged
  balances. The framing names this in passing but many borrowers
  comparing discharge against IDR-forgiveness don't see that
  discharge is *tax-free* even when ARPA cliffs out and IDR-
  forgiveness becomes taxable." Statutory anchor: IRC
  §108(a)(1)(A) bankruptcy exclusion.
- **Trigger**: Borrower comparing IDR-forgiveness (taxable post-
  ARPA-cliff) vs bankruptcy discharge (tax-free) as alternative
  exit paths for high-balance distress, AND treating both as
  equivalent on tax-treatment.
- **Failure-mode**: Borrower reaches IDR-forgiveness year with
  $200k forgiven balance + ARPA cliff active = $70k federal tax
  liability + state tax; same borrower could potentially have
  pursued bankruptcy discharge in earlier year with $200k
  discharged tax-free under §108(a)(1)(A); $70k tax-treatment
  delta wasn't part of the IDR-vs-bankruptcy comparison.
- **Recovery-move**: For borrowers in severe distress evaluating
  discharge-vs-IDR-forgiveness, the post-tax-treatment is a
  significant variable favoring bankruptcy discharge IF the
  discharge is granted. Build the comparison with after-tax
  values on both sides. Combined with credit-damage and
  procedural cost of bankruptcy, the analysis is fact-specific.
  For high-balance borrowers ($150k+) with realistic discharge
  prospects, **route to NACBA-affiliated bankruptcy attorney**
  for joint evaluation. Cross-edge to F8 (tax-bomb), D4.

### 13.4 Spousal-credit-pull implications of bankruptcy under-stated in community-property states

- **Statement**: The asker treats bankruptcy as a single-borrower
  decision, missing that in community-property states a spouse's
  bankruptcy can affect the non-filing spouse's credit, and joint
  accounts get discharged-or-not based on filing structure
  (Chapter 7 vs Chapter 13).
- **Source-evidence**: [`framings.md` F13 fourth Excludes bullet](./framings.md) —
  "Glosses over the *spousal-credit-pull* implications of
  bankruptcy: in community-property states, a spouse's
  bankruptcy can affect the non-filing spouse's credit, and
  joint accounts get discharged-or-not based on the filing
  structure (Chapter 7 vs Chapter 13). The framing's 'discharge
  frees the borrower' understates the household-credit knock-on
  for married filers."
- **Trigger**: Married borrower in community-property state (AZ,
  CA, ID, LA, NV, NM, TX, WA, WI, AK opt-in) considering
  bankruptcy discharge of student loans AND has not modeled the
  spousal-credit impact.
- **Failure-mode**: Borrower in TX (community-property) files
  Chapter 7 for student-loan discharge; spouse's credit report
  shows joint-account history affected by the filing; spouse's
  small-business loan application is denied; spouse can't qualify
  for new mortgage; household credit takes 2-borrower hit instead
  of 1-borrower hit; the framing's "discharge frees the borrower"
  didn't price the household-level credit damage.
- **Recovery-move**: For married borrowers in community-property
  states considering bankruptcy, model the spousal-credit impact
  explicitly. Joint accounts may or may not be affected depending
  on Chapter 7 vs Chapter 13 + community-property treatment by
  the bankruptcy court. **Route to NACBA-affiliated bankruptcy
  attorney with community-property experience** for case-specific
  evaluation. In some cases, separating joint accounts pre-
  filing or filing in a different state (if move is legitimate)
  can mitigate spousal-credit damage.

### 13.5 §437(a) death-and-disability discharge 3-year monitoring trap missed

- **Statement**: The asker treats §437(a) total-and-permanent-
  disability (TPD) discharge as cleanly available, missing that
  TPD certification requires physician attestation, VA disability
  rating of 100%, or 3+ years SSDI — AND a 3-year monitoring
  period applies post-discharge during which earned income above
  the poverty-line threshold reverses the discharge.
- **Source-evidence**: [`framings.md` F13 fifth Excludes bullet](./framings.md) —
  "Frames *death-and-disability discharge* under HEA §437(a) as
  cleanly available; in fact total-and-permanent-disability (TPD)
  certification requires physician attestation, VA disability
  rating of 100%, or 3+ years of SSDI — and a 3-year monitoring
  period applies post-discharge during which earned income above
  the poverty-line threshold reverses the discharge." Statutory
  anchor: HEA §437(a), 34 CFR §685.213.
- **Trigger**: Borrower or family is exploring TPD discharge for
  borrower with disability AND is planning income-generating
  activity (part-time work, gradual return-to-work) during the
  3-year post-discharge monitoring period.
- **Failure-mode**: Borrower receives TPD discharge in year 1;
  starts part-time freelance work year 2 earning $25k (above
  poverty-line for single individual ~$15k); USDOE conducts
  routine income-monitoring (3-year post-discharge); discharge
  is reversed, full loan balance reinstated; borrower now owes
  $80k+ they thought was discharged AND has interest accrued
  during monitoring period.
- **Recovery-move**: For TPD discharge applicants, plan the
  3-year monitoring period explicitly — earned income must
  remain below the poverty-line threshold (currently ~$15k for
  single, ~$31k for family of 4 in 2026, indexed). For borrowers
  expecting to return to work, time the TPD application around
  realistic work-return — there's no benefit to filing TPD if
  expected to return to work within 3 years. **Route to a
  student-loan attorney experienced with TPD applications** —
  improperly documented TPD claims are often denied on first
  review, and the post-discharge monitoring is enforced. Cross-
  edge to F1 (death-and-disability discharge for family-member-
  disability under-counts the protection scope).

---

## F14 — 1099-vs-W-2-PSLF-asymmetry / contractor-trap framing

### 14.1 W-2 vs 1099 classification treated as clean line when reclassification path exists

- **Statement**: The asker treats W-2-vs-1099 as a clean
  classification, missing that the classification is contested in
  many gig-economy / consulting / fractional-roles — a worker
  classified as 1099 may be a W-2 employee under the IRS common-
  law-employee test or under state-law AB-5-style ABC tests.
- **Source-evidence**: [`framings.md` F14 first Excludes bullet](./framings.md) —
  "Treats W-2-vs-1099 as a clean line when in fact the
  classification is contested in many gig-economy / consulting /
  fractional-roles — a worker classified as 1099 may be a W-2
  employee under the IRS common-law-employee test or under state-
  law AB-5-style ABC tests, and reclassification (forced or
  voluntary) can retroactively change PSLF qualifying-payment
  status. The framing's '1099 doesn't qualify' misses the
  reclassification path that some borrowers pursue." Cross-routes
  `entrepreneurship`. Statutory anchor: IRS Rev. Rul. 87-41
  common-law-employee test; CA AB-5 (codified Lab. Code §2750.3).
- **Trigger**: Borrower at qualifying-employer organization (501(c)(3),
  government) classified as 1099 contractor performing work
  identical to W-2 employees, AND wants PSLF qualifying status.
- **Failure-mode**: Borrower is "consultant" at 501(c)(3) for 5
  years on 1099; the 5 years don't count for PSLF; borrower
  realizes at year 10 they have 0 qualifying payments despite
  working at qualifying employer the whole time; PSLF clock
  hasn't started.
- **Recovery-move**: For 1099-at-qualifying-employer scenarios,
  evaluate whether the worker meets the IRS common-law-employee
  test (employer controls means and methods of work, sets
  schedule, provides tools, is exclusive employer, etc.). If yes,
  consider requesting W-2 reclassification with the employer
  (some 501(c)(3)s will agree given DOL / IRS audit risk on
  misclassification). For workers in AB-5-style states (CA, NJ,
  MA), the ABC test may force reclassification regardless of
  preference. Document work-pattern in case of retroactive
  reclassification claim. **Route to an employment-classification
  attorney** for high-value cases (5+ years at qualifying
  employer that would have been ~$80k+ of PSLF forgiveness if
  W-2). Cross-edge to D10, `entrepreneurship`.

### 14.2 Part-time aggregation across two qualifying employers requires both to certify on separate ECFs

- **Statement**: The asker assumes part-time work at two 501(c)(3)
  employers automatically aggregates to PSLF full-time-equivalence,
  missing that both employers must certify on separate ECFs and
  the borrower must track full-time-equivalence calculation
  proactively.
- **Source-evidence**: [`framings.md` F14 second Excludes bullet](./framings.md) —
  "Doesn't see that *part-time aggregation* across two qualifying
  employers requires both to certify on separate ECFs and the
  borrower to track full-time-equivalence calculation
  proactively — many borrowers in part-time roles at two
  501(c)(3)s assume they qualify without doing the ECF paperwork
  for both; the year-9 surprise pattern (MOHELA finds only one
  employer's certification, zeroes the other employer's months)
  is documented."
- **Trigger**: Borrower working part-time at two qualifying
  employers totaling ≥30 hours/week aggregated AND has not filed
  ECF for both employers separately.
- **Failure-mode**: Borrower works 20 hours/week at hospital
  501(c)(3) + 15 hours/week at university 501(c)(3) = 35 hours
  aggregated full-time; files ECF only for hospital (the
  "primary" job); at year 9, MOHELA reviews and finds the
  hospital-alone hours were below full-time-equivalence (since
  ECF only covers hospital); 9 years zeroed for PSLF; if borrower
  had filed both ECFs, the aggregated full-time-equivalence would
  have qualified.
- **Recovery-move**: For part-time-at-multiple-employers
  borrowers, file separate ECFs for each qualifying employer
  every year. Track aggregated full-time-equivalence (sum of
  hours / employer's full-time definition or 30 hours / whichever
  is lower per HEA). For borrowers with PSLF history but missing
  ECF for second employer, file the second-employer ECF
  retroactively (employers can certify past employment via ECF;
  many will accept past-date attestations). **Route to FSA
  Ombudsman Group** if MOHELA denies retroactive certification.
  Cross-edge to D10, F12.

### 14.3 S-corp formation at 501(c)(3) client converts borrower OUT of PSLF qualification

- **Statement**: The asker incorporates as S-corp to serve a
  501(c)(3) client (consulting structure), missing that they
  become the W-2 employee of their own S-corp (for-profit), NOT
  of the 501(c)(3) — the S-corp is for-profit, so the borrower's
  W-2 employment is at a for-profit and does not qualify for
  PSLF.
- **Source-evidence**: [`framings.md` F14 third Excludes bullet](./framings.md) —
  "Under-weights the *S-corp-formation-at-501(c)(3)* trap: a
  borrower who incorporates as an S-corp to serve a 501(c)(3)
  client (consulting structure) typically becomes the W-2
  employee of their OWN S-corp, NOT the 501(c)(3) — and the
  S-corp is for-profit, so the borrower's W-2 employment is at a
  for-profit and does not qualify for PSLF even when the
  underlying work is for a 501(c)(3). The framing's '501(c)(3)
  employer' test is more restrictive than the work-content test
  many borrowers assume." Cross-routes `entrepreneurship`.
- **Trigger**: Borrower on PSLF track is offered or considering
  S-corp / LLC formation to consult for 501(c)(3) clients (often
  driven by tax-advisor advice on the QBI §199A deduction or
  S-corp distribution-vs-salary planning).
- **Failure-mode**: Borrower at PSLF year 6 forms S-corp to
  consult for the same 501(c)(3) employer (now as contractor);
  W-2 status switches to the S-corp; PSLF clock stops; borrower
  thinks "I'm still serving the nonprofit"; at year 10 discovers
  the 4 post-S-corp years didn't count for PSLF; 4 years pushed
  back, $80k+ of forgiveness delayed by 4 years.
- **Recovery-move**: Before forming S-corp / LLC while on PSLF
  track, evaluate whether the entity-of-record on W-2 will be
  the qualifying employer or the for-profit pass-through. For
  PSLF preservation, remain as W-2 employee of the qualifying
  employer directly. For tax-optimization reasons that drive
  S-corp consideration, the PSLF cost is typically larger than
  the QBI / distribution-vs-salary benefit unless balance is
  very small. **Route to a CPA AND student-loan attorney** for
  joint evaluation when both entity-formation and PSLF
  preservation are in play. Cross-edge to D10, `entrepreneurship`
  (S-corp reasonable-comp), `tech-career` (1099 vs W-2 in
  consulting roles).

### 14.4 §501(c)(4) advocacy nonprofits excluded from PSLF — surprise for think-tank and policy-org employees

- **Statement**: The asker assumes any tax-exempt nonprofit
  qualifies for PSLF, missing that advocacy nonprofits organized
  under §501(c)(4) (issue-advocacy, lobbying, political-action)
  do NOT qualify even though they are tax-exempt.
- **Source-evidence**: [`framings.md` F14 fourth Excludes bullet](./framings.md) —
  "Glosses over the *501(c)(4) exclusion*: advocacy nonprofits
  organized under §501(c)(4) (issue-advocacy, lobbying, political-
  action) do NOT qualify for PSLF even though they are tax-exempt
  nonprofits — a frequent surprise for borrowers at think-tanks
  and policy-advocacy organizations that operate as §501(c)(4)
  for lobbying-flexibility reasons. The framing names 'NOT
  501(c)(4)' but borrowers don't always know their employer's
  tax-exempt classification." Statutory anchor: HEA §455(m)
  qualifying employer (limits to §501(c)(3) among tax-exempt).
- **Trigger**: Borrower works at a think-tank, policy organization,
  advocacy group, or lobbying-adjacent nonprofit AND assumes
  PSLF eligibility based on "we're a nonprofit".
- **Failure-mode**: Borrower at advocacy think-tank classified as
  §501(c)(4) works 7 years on PSLF assumption; files first ECF
  at year 7; MOHELA rejects because employer is §501(c)(4) not
  §501(c)(3); 7 years zeroed; if borrower had checked
  classification at year 0 they could have prioritized §501(c)(3)
  employer search instead.
- **Recovery-move**: For any borrower at a tax-exempt nonprofit,
  verify the employer's specific §501(c) classification by
  checking IRS Exempt Organizations Select Check (EOSC) or
  asking HR / general counsel directly. §501(c)(3) qualifies for
  PSLF; §501(c)(4), §501(c)(6) (trade association), §501(c)(7)
  (social club), §527 (political organization) do NOT. For
  borrowers at organizations with both §501(c)(3) and §501(c)(4)
  arms (common at policy organizations), confirm which entity
  is the employer-of-record on W-2. **File ECF in year 1** to
  catch classification issues early, not at year 7. Cross-edge
  to D10.

### 14.5 Partisan / political employment entity-of-record subtlety missed at think-tanks with mixed structure

- **Statement**: The asker assumes partisan-political employment
  is cleanly excluded from PSLF, missing that some borrowers at
  nonprofit-research arms of partisan organizations face
  complicated classification — parent organization may be
  §501(c)(4) or §527 but the research-and-policy arm is
  §501(c)(3); ECF certification follows the employer-of-record
  on W-2.
- **Source-evidence**: [`framings.md` F14 fifth Excludes bullet](./framings.md) —
  "Frames *partisan political* employment as cleanly excluded;
  in fact some borrowers at nonprofit-research arms of partisan
  organizations face complicated classification — the parent
  organization is §501(c)(4) or §527 (political organization),
  but the research-and-policy arm is §501(c)(3); ECF
  certification follows the employer-of-record on the W-2, which
  can be either entity depending on the org's structure. The
  framing's 'no partisan' doesn't surface the entity-of-record
  subtlety."
- **Trigger**: Borrower at an organization with both a §501(c)(3)
  research arm and a §501(c)(4) advocacy arm (common at policy
  organizations across the political spectrum — think-tanks,
  advocacy umbrellas) AND uncertain about W-2 entity-of-record.
- **Failure-mode**: Borrower at policy organization's research
  arm assumes they're at the §501(c)(3) (which is true) but
  W-2 is actually issued by the parent §501(c)(4) for
  administrative simplicity; ECF certification reflects §501(c)(4)
  parent; PSLF rejected at first ECF; borrower had assumed
  qualifying status based on the work-content (research) rather
  than the W-2 entity-of-record.
- **Recovery-move**: Check the W-2 entity-of-record (not just
  the org's marketing name) before assuming PSLF qualification.
  For mixed-structure organizations, request HR clarification
  on which entity issues the W-2. If W-2 is from the §501(c)(4)
  parent, explore whether the §501(c)(3) research arm can issue
  W-2 directly (some orgs will do this for PSLF-eligible
  employees as employee benefit). For borrowers already at
  organizations with §501(c)(4)-W-2, evaluate whether moving to
  a purely-§501(c)(3) employer is worth the PSLF preservation.
  **File ECF in year 1** to catch entity-of-record issues early.
  Cross-edge to D10.

---

## Cross-framing tensions (opposing-framing pairs)

These are the direct axiom-level oppositions the responder must
surface in answers and the Triage / Risk Officer should route on
when the asker's prompt vocabulary lands on one side. Mirroring
[`framings.md` §Cross-framing tensions](./framings.md), expanded
with the per-blindspot anchor.

- **F1 (federal-optionality-as-put-option) ↔ F4 (rate-spread-
  arithmetic)** on D1 / D4 / D7. F1 §1.1 ("never refi federal
  universal heuristic") and §1.2 (SAVE-treated-as-permanent) are
  the dimensions F4 attacks; F4 §4.1 (probability-of-option-
  exercise under-estimated) and §4.4 (ARPA-cliff missed) are the
  dimensions F1 attacks. Triage should surface F4 entries when
  asker is F1-anchored ("never refi federal") on borrowers with
  genuinely near-zero option-exercise probability, and surface
  F1 entries when asker is F4-anchored ("the math is the math")
  on borrowers with plausible PSLF / disability / grad-school
  trajectory.

- **F2 (529-state-deduction-and-tax-deferral) ↔ F6 (529-to-Roth-
  flexibility-hedge)** on D3 / D6. F2 §2.3 (leftover-529 problem)
  and F6 §6.1 (SECURE 2.0 §126 oversold) are the dual-direction
  tension: F2 reflexes toward maximizing tax-deferred growth via
  front-loading; F6 reflexes toward flexibility-preservation via
  Roth-substitute or SECURE 2.0 §126 hedge. Both framings agree
  529 is dominant when kid will go to college; they disagree on
  how much flexibility-cost to pay for the kid-doesn't-go
  scenario.

- **F2 (529-state-deduction) ↔ F10 (FIRE-retirement-priority)** on
  D3 / D6 / D7. F2 §2.1 (state-deduction-over-weighted) and F10
  §10.1 (parental-retirement-readiness binary-vs-continuous) are
  the cross-framing tension: F2 reasons from per-vehicle tax-
  arbitrage; F10 reasons from household-allocation-priority.
  Triage should surface F10 entries when asker is 529-focused on
  households with retirement-savings rate below target; F2 when
  asker is retirement-priority-anchored but living in a high-
  state-deduction state where 529 arbitrage is significant.

- **F3 (ROI-by-major) ↔ F7 (NACAC-counselor-aid-negotiation)** on
  D5. F3 §3.1 (median-earnings-treated-as-relevant when
  distribution is skewed) and F7 §7.1 (appeal-success treated as
  universal) are the dual tension: both frame net-price-not-
  sticker-price; F3 treats the initial net-price as the
  comparison input; F7 treats the initial net-price as the
  *initial* input that an appeal will move. The right answer
  depends on the family's willingness to invest in appeal-process
  and the school's institutional-aid-budget context.

- **F5 (FAFSA-base-year-and-asset-positioning) ↔ F10 (FIRE-
  retirement-priority)** on D8. F5 §5.4 (retirement-contribution-
  in-base-year add-back on CSS) and F10 §10.1 (continuous
  allocation) agree on the action (max retirement contributions)
  but disagree on the framing — F5 treats retirement-shelter as
  FAFSA-optimization strategy; F10 treats it as household-priority
  that happens to also yield FAFSA benefits. Tension matters when
  household retirement-contribution capacity is below maximum
  and family must trade off retirement-funding against college-
  funding cadence.

- **F8 (tax-bomb-arithmetic-and-sinking-fund) ↔ F12 (ARPA-cliff-
  aware-political-risk)** on D4 / D10. F8 §8.1 (ARPA-sunset-
  treated-as-certain) and F12 §12.1 (political-risk-anchored-on-
  loss-when-net-positive-historically) are the dual cliff/extension
  tension: F8 builds sinking fund NOW for IDR-forgiveness 20+
  years out; F12 says ARPA may extend and the sinking fund grows
  against tax liability that gets excluded. Both framings agree
  political-risk exists and disagree on which direction it cuts.
  The synthesis is "build sinking fund as flexible taxable
  brokerage that defaults to retirement / general savings if
  ARPA extends" — neither pure F8 nor pure F12.

- **F9 (consumer-protection-anti-predatory) ↔ F4 (rate-spread-
  arithmetic)** on D1. F9 §9.1 (all-private-refi-treated-as-
  adversarial) and F4 §4.1 (probability-of-option-exercise) are
  the cross-framing tension on the same borrower population
  framed differently. Triage should surface F9 entries when
  asker is in active servicer-dispute or near a PSLF / disability
  threshold, and F4 entries when neither holds.

- **F11 (§127-retention-clawback) ↔ F3 (ROI-by-major)** on D2 /
  D9. F11 §11.4 (career-pivot-during-program embedded employee-
  call) is in tension with F3 §3.4 (program-choice-treated-as-
  free with admissions-side constraints): F11 says the part-time-
  with-employer-funding path dominates for engineers / consultants
  / finance pros pursuing MBA / MS-CS / JD-part-time *when
  program quality is acceptable*; F3 says program quality and
  ROI-by-program drive the choice — and a top program may not
  accept the part-time-employer-funded path or may lack the
  recruiting-funnel access that justifies the program in F3's
  framing. The cross-tension is most acute for engineering-to-
  finance / consulting / PM pivot via MBA where F3 strongly
  prefers a top full-time program and F11 strongly prefers
  employer-funded part-time.

- **F13 (bankruptcy-discharge-and-default-recovery) ↔ F12 (ARPA-
  cliff-aware)** on D4. F13 §13.3 (post-discharge §108(a)(1)(A)
  bankruptcy exclusion is tax-free) is the dimension F12 ignores
  — bankruptcy discharge of student-loan debt is tax-free even
  when ARPA cliffs out, materially changing the bankruptcy-vs-
  IDR-forgiveness comparison post-2026. F13 says: for high-balance
  borrowers facing IDR-forgiveness tax-bomb cliff, bankruptcy may
  actually be the more favorable exit; F12 anchors on federal-
  bundle preservation rather than discharge-as-alternative.

- **F14 (1099-vs-W-2-PSLF-asymmetry) ↔ F1 (federal-optionality)**
  on D10 / D2. F14 §14.3 (S-corp formation at 501(c)(3) client
  converts OUT of PSLF) is the entity-formation cost that F1's
  "preserve federal optionality" framing doesn't surface — a
  borrower preserving federal optionality on the loan side while
  forming an S-corp on the work side may inadvertently zero
  their PSLF qualifying employment. Cross-routes `entrepreneurship`.

- **F6 (529-to-Roth-flexibility-hedge) ↔ F10 (FIRE-retirement-
  priority)** on D6. F6 §6.3 (Roth IRA earnings-withdrawal pre-
  59.5 treated as costless) is in tension with F10's
  reflex toward using Roth IRA as flexibility-preserving college
  vehicle — F6 surfaces that the Roth IRA's earnings portion is
  tax-disadvantaged for pre-59.5 college use, so the Roth-as-
  college-funding-substitute strategy is more limited than F10
  implies. Both framings agree retirement-priority is load-bearing;
  they disagree on whether Roth IRA is a good "both" vehicle.

- **F8 (tax-bomb-sinking-fund) ↔ F10 (FIRE-retirement-priority)** on
  D4. F8 §8.4 (Roth-conversion-ladder in low-income years) and
  F8 §8.5 (taxable brokerage growth net-of-tax) point toward
  using retirement-account-room for the sinking fund where
  possible; F10's retirement-priority reflex aligns with this but
  may resist earmarking retirement-account-room for what F10
  sees as a debt-management need. The synthesis is "use Roth IRA
  contribution-basis for tax-bomb sinking-fund — preserves
  retirement growth, gives basis-flexibility, eliminates LTCG
  drag."

- **F9 (consumer-protection) ↔ F13 (bankruptcy-discharge)** on D1
  / D4. F9 §9.2 (bankruptcy-discharge-oversold) and F13 §13.1
  (post-2022 Brunner-softening-oversold) are the same insight
  from different framing-perspectives — both surface that
  bankruptcy is not a tactical first-move despite DOJ guidance
  softening. The cross-framing convergence here is mutually
  reinforcing: consumer-protection and bankruptcy framings both
  caution against treating discharge as routine.

---

## Maturity / source-anchor / date-stamp note

This file is `planned` maturity per
[`_meta_ontology.md` §3](../_meta_ontology.md). Source-evidence
lines above currently anchor to:

- [`framings.md`](./framings.md) Excludes lines (load-bearing —
  the framing-level Excludes were authored specifically to seed
  Layer 3, per the "Notes for downstream layers" section of
  framings.md).
- [`decisions.md`](./decisions.md) decision-scope and framing-
  axes-covered fields (for cross-edge anchors).
- V1 community-profile bullets are NOT a source here — V1
  community-profiles cover `tech-career` and `personal-finance`
  adjacencies primarily; education-funding-specific communities
  are not yet authored (they'll land in
  `domain_knowledge/education-funding/communities/*.md` in a
  later sub-item once `sources.yaml` is in place). Most source-
  anchors here therefore route to framings.md Excludes lines.
- Conceptual references to the education-funding-specific
  community classes named in `framings.md` voice anchors
  (PSLF-preservation / student-loan-attorney voice, r/PSLF /
  r/StudentLoans / r/StudentLoansHelp, ROI-by-major / Georgetown
  CEW / Burning Glass, Bogleheads-college / Mike Piper,
  SavingForCollege / Mark Kantrowitz / The College Investor,
  FIRE-aware-college-funding / Mr. Money Mustache "MMM
  University" / ChooseFI, NACAC-counselor / NASFAA / r/financialaid /
  r/ApplyingToCollege, fee-only-CFP / NAPFA, retirement-
  experienced-CPA with §25A / §127 / §529 history, MBA-admissions /
  Poets&Quants / r/MBA / Wall Street Oasis, engineering-pivot /
  Levels.fyi / Blind / r/cscareerquestions, consumer-protection /
  CFPB / NCLC / SLBA / state AGs, employer-tuition voice /
  corporate HR / Glassdoor, bankruptcy-discharge / NACBA / post-
  2022 DOJ-USDOE attestation voice, HELOC-as-college-funding voice
  cross-routing `housing`, SECURE-2.0-§126 voice).

When `domain_knowledge/education-funding/sources.yaml` is
authored and `domain_knowledge/education-funding/communities/*.md`
community profiles land, source-evidence lines above should be
tightened to specific source-view ids. Until then, this file's
grounding is the framings-Excludes seed plus the cross-domain V1
community-profile content where relevant (`tech-career` /
`personal-finance` communities touch education-funding adjacencies
through MBA-ROI on engineering tracks, 529-vs-Roth ordering,
retirement-priority vs college-funding cadence — those are the
overlap zones).

### High-stakes posture summary

`education-funding` is `high_stakes: false` per
[`_meta_ontology.md` §7](../_meta_ontology.md). Recovery moves
above route to professional channels **only on the six-figure
tail-risk pockets**, mirroring the
[V2 §4 Mechanism E partial-gating posture](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)
established by [`housing/blindspots.md`](../housing/blindspots.md)
(PR #64) and [`entrepreneurship/blindspots.md`](../entrepreneurship/blindspots.md)
(PR #83):

- **Student-loan attorney / SLBA / NCLC**: §1.1 (refi vs federal-
  optionality option-value audit), §1.5 (TPD application), §9.2
  (bankruptcy-discharge case evaluation — also NACBA), §9.3
  (escalation after FSA Ombudsman exhausted), §9.5 (BDR rejected-
  claim appeal), §13.1 (bankruptcy as last-resort), §13.2 (default-
  recovery case management when rehabilitation card gone), §14.1
  (W-2 reclassification — also employment-classification
  attorney), §14.3 (S-corp + PSLF joint evaluation — also CPA).
- **FSA Ombudsman Group** ($0-cost escalation, file directly via
  StudentAid.gov): §1.3 (forbearance-steering account-adjustment),
  §9.3 (first escalation step), §12.2 (account-adjustment one-
  time-window appeal), §14.2 (retroactive ECF certification denied).
- **Retirement-experienced CPA with §25A / §127 / §529 / SECURE
  2.0 §126 history**: §2.2 (5-year-forward Form 709 + estate-tax-
  exemption coordination), §4.4 (ARPA-cliff tax-bomb sinking-
  fund + Roth-conversion-coordination), §5.3 (S-corp CSS-Profile
  reporting + 529 coordination), §6.4 (AOTC §25A / 529 year-of-
  distribution coordination), §8.2 (tax-bomb sinking-fund design),
  §8.4 (multi-year low-income Roth-conversion-ladder), §10.3
  (grandparent-529 5-year-elect + estate-tax-exemption),
  §14.3 (S-corp + PSLF tax planning — joint with student-loan
  attorney).
- **Fee-only fiduciary CFP (NAPFA-affiliated, AUM-free)**: §1.4
  (high-balance IDR distress comprehensive plan review), §4.1
  (option-value audit for high-balance refi), §8.1 (high-balance
  IDR forgiveness flexible sinking-fund planning), §8.4 (joint
  with CPA on multi-year tax planning), §9.4 (Parent PLUS refi +
  term-life insurance hedge), §10.1 (continuous parental-
  retirement vs college-funding allocation).
- **NACAC-member college counselor / NASFAA-affiliated financial-
  aid consultant**: §5.1 (CSS-specific positioning), §5.3 (S-corp
  CSS positioning — joint with CPA), §5.5 (§479A appeal letter
  drafting), §7.1 (school-by-school appeal-strategy).
- **NACBA-affiliated bankruptcy attorney**: §9.2 (bankruptcy-
  discharge case evaluation), §13.1 (bankruptcy as last-resort),
  §13.4 (community-property-state spousal-credit impact).
- **Employment-classification attorney**: §14.1 (W-2
  reclassification for 1099-at-qualifying-employer with 5+ years
  history).

For lower-stakes framings (D2 graduate-school ROI for routine
career stage, D5 school-choice with merit aid outside the
six-figure tail, D6 vehicle-mix outside the leftover-529 /
parental-retirement tail, D8 FAFSA positioning outside the
divorced-parent / business-asset / CSS-Profile tail, D9 employer
§127 outside above-cap or multi-year-clawback scenarios), Recovery
moves above are self-directed — no professional-counsel deferral
needed. The user is treated as a decision-capable adult navigating
slow-clocked financial choices.

### Date-stamp risk

Anchor numbers and rules above carry date-stamp risk inherited
from the underlying tax and regulatory corpus. Entries to re-check
before relying on for an active decision:

- §1.2 / §1.3 / §4.5 / §12.5 — SAVE plan post-injunction status
  (8th Circuit injunction 2024; rulemaking-rollback in progress;
  check current status of administrative forbearance, IDR-
  forgiveness counting treatment for SAVE-forbearance months, and
  any new IDR plan introduced post-rulemaking).
- §2.2 / §10.3 — TCJA estate-tax-exemption sunset (currently
  scheduled end-2025; potential legislative action; check current
  lifetime exemption for 5-year-forward 529 election planning).
- §2.4 / §6.5 — State-level 529-deduction recapture rules (check
  current state statute for NY / IL / NC / AR / IN / GA / MD / OK /
  OR / RI / UT / VT / WI and any newly-added or removed states).
- §4.4 / §8.1 / §8.3 / §12.2 / §12.4 — ARPA §9675 federal tax-
  exclusion of student-loan forgiveness sunset (end-2025 absent
  extension); state conformity uneven and changes year-to-year;
  check current federal extension status and state-by-state
  conformity for CA / MS / IN / NC / WI / NY / NJ / OR / MN.
- §5.1 / §5.3 — FAFSA Simplification Act implementation continuing
  to settle (effective 2024-25 award year; 2025-26 cycle had
  major rollout delays); check current FAFSA / CSS treatment of
  base-year, small-business-assets, grandparent-529, divorced-
  parent-of-record rule.
- §6.1 / §6.2 / §6.5 — SECURE 2.0 §126 529-to-Roth rollover
  guidance still developing (Treasury / IRS guidance on
  beneficiary-change-resets-15-year-clock question is an open
  area).
- §10.5 — IRC §221 student-loan-interest deduction AGI phaseouts
  (annually indexed; check current MFJ / single phase-in
  thresholds).
- §11.1 / §11.2 / §11.5 — IRC §127 $5,250 cap (statutory; not
  indexed historically but periodically updated; check current
  cap before relying).
- §12.2 — Account-adjustment review closing deadlines (extended
  multiple times; check current deadline before relying on
  retroactive filing).
- §13.1 — Post-2022 DOJ-USDOE attestation guidance evolution
  (district-level discharge rates continue to evolve; check
  current district-specific case-law before bankruptcy filing).
- §14.4 — IRS Exempt Organizations classification database (EOSC)
  for §501(c) determination — verify employer classification
  rather than rely on org's marketing-name.

### Mechanism E posture summary

`education-funding`'s per-framing inline referral pattern is the
partial-gating shape described in
[`_meta_ontology.md` §7](../_meta_ontology.md) — selective
professional referral on the six-figure tail-risk pockets D1, D3,
D4, D7, D10, with self-directed Recovery moves for routine
decisions D2, D5, D6, D8, D9. The `domain_pack.md` (later sub-item
in V2 §4) will encode this pattern explicitly. This is the SAME
posture as `housing` (PR #64) and `entrepreneurship` (PR #83), and
DIFFERENT from the uniform Mechanism E gating in `immigration`
(PR #48), `health-insurance` (PR #75), and `personal-finance`
(PR #79) which all carry `high_stakes: true`.

The six-figure tail-risk pockets that warrant inline professional
referral, mirroring the structure in
[`decisions.md` §Notes](./decisions.md):

- **D1 federal-to-private refi** — one-way door, no
  re-federalization path; option-value erasure is permanent.
- **D3 §529(c)(2)(B) 5-year-forward + Form 709** — election-year
  filing required, Form 709 omission propagates forward to
  estate-clawback.
- **D4 IDR + tax-bomb sinking-fund** — multi-year tax planning
  with bracket-management coordination; ARPA-cliff exposure.
- **D7 Parent PLUS** — parental debt with §437(a) discharge
  asymmetry vs private cosigner, and HELOC alternative cross-
  edge to housing.
- **D10 PSLF qualifying-employment + Buyback** — entity-of-record
  / W-2-vs-1099 / §501(c)(3)-vs-§501(c)(4) classification traps
  with year-9-surprise pattern; FSA Ombudsman as $0-cost first
  escalation.

For routine decisions outside these pockets, Recovery moves above
are educational and self-directed. Over-referral degrades signal;
under-referral on the irreversible (D1) and large-tail-risk (D3,
D4, D7, D10) decisions creates harm.

