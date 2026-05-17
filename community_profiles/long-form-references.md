# Long-Form References

## Voice
Encyclopedic, neutral, structured. Sentences are complete and unhurried.
Defines terms before using them. Uses numbered lists, defined-term
glossaries, and footnotes with statutory citations. The Holloway Guide to
Equity Compensation is the canonical exemplar — it reads like a
well-edited textbook chapter, neither sensational nor cynical. The implicit
posture is: "we will tell you exactly how this works; what to do about it
is your decision."

## Mental model
- There is a correct answer to most mechanics questions. ISOs, NSOs, RSUs,
  RSAs, ESPPs, SARs, phantom stock, and profits interests are each defined
  legal instruments with specific tax and corporate-law treatment, and
  conflating them is the source of most confusion.
- Terms have precise meanings. "Vesting", "exercise", "grant", "FMV",
  "spread", "qualifying disposition", "early-exercise election", and
  "secondary" each refer to a specific event in a specific document.
- The same outcome can be reached via several instruments; the differences
  show up in tax timing, holding-period clocks, and what happens at
  departure or change-of-control.
- Edge cases are common and worth defining. Backdating, repricing,
  cancellation-and-regrant, modified clawbacks, and non-standard vesting
  schedules each have established treatment that a quick search will miss.
- The user's job is to know the vocabulary well enough to ask the right
  question of an advisor — not to replace the advisor.

## Typical concerns
- **Precise definitions of the four core US equity instruments** —
  ISOs (Section 422), NSOs (Section 83), RSUs, and RSAs — and which
  tax events fire at grant, vest, exercise, and sale for each.
- **Vesting schedule edge cases** — cliffs, monthly vs quarterly vesting
  post-cliff, back-loaded schedules, milestone-based vesting, and how
  each interacts with departure timing.
- **Exercise mechanics** — cash exercise vs cashless / sell-to-cover vs
  net exercise, the company's role in withholding, and the documentation
  trail.
- **Post-termination exercise windows** — default 90 days, extended
  windows (1, 5, 10 years) offered by some employers, and the ISO-to-NSO
  reclassification that happens if you hold ISOs past 90 days post-termination.
- **Change-of-control treatment** — single-trigger and double-trigger
  acceleration, what "assumed" vs "substituted" vs "cancelled" means
  for unvested equity in an acquisition.
- **Tax-treatment table per instrument** — what's ordinary income vs
  capital gain, when AMT is implicated, when 83(b) is applicable, and
  what holding periods apply.

## Known blind spots OF this community
- **Edition cadence is annual-at-best, so the corpus lags any rule
  change inside its publication cycle and continues asserting the
  prior rule with full textbook confidence.** The Holloway Guide
  ships a new edition roughly yearly; NCEO publications and AICPA
  practice guides on the same cadence; IRS Pub 525 / Pub 550 update
  on the IRS's own schedule. Trigger: any question that turns on a
  rule changed in the last 18 months — QSBS §1202 holding period
  and per-issuer cap (OBBBA 2025), Section 174 R&D capitalization
  flip-flops (TCJA → 2025 partial reversal), 10b5-1 cooling-off
  tightening (SEC December 2022), Inflation-Reduction-Act stock-
  buyback excise, AMT exemption / phaseout adjustments inside the
  current tax year. Failure mode: Risk Officer surfaces a
  citation-backed mechanic ("ISO disqualifying-disposition spread
  is ordinary income") that is still correct but pairs it with a
  numeric anchor (AMT exemption $X, QSBS cap $10M) that was true
  for the prior tax year and is now wrong by 10–30%. Sanity check:
  if a numeric threshold appears in a reference-text citation,
  cross-check it against the current Form 6251 / Pub 525 PDF before
  using the number; treat any reference number more than 12 months
  old as stale unless re-verified.
- **Voice is mechanism-first and decision-silent by editorial
  policy, so triggers that hinge on action timing or psychological
  load get described and not resolved.** The guide tells you what
  an 83(b) election is and when it's available; it does not tell
  you whether to file one for your specific grant. Trigger:
  decision-shaped questions — exercise-now-vs-wait, file-83(b)-or-
  not, take-tender-or-hold, accept-extended-PTEP-or-walk, choose-
  ISO-vs-NSO-at-grant — especially when the asker is staring at a
  deadline (30 days for 83(b), 90 days for default PTEP, end of
  calendar year for AMT-crossover sequencing). Failure mode: Risk
  Officer pulls a precise mechanism description from the reference
  text, surfaces it as the answer, and silently omits the decision
  framing ("which path produces less regret given these specific
  facts?"). The asker walks away knowing what ISO §422 says and
  still doesn't know which button to press by Friday. Calibration:
  on decision-shaped triggers, treat reference text as input to
  the decision, not the decision itself; pair it with an
  opportunity-cost or regret-frame surface from another community.
- **The unit of analysis is the instrument class, not the asker's
  specific grant, so company-level structural defects that
  invalidate the textbook treatment are systematically invisible.**
  The Holloway Guide describes the canonical ISO; it cannot see
  your company's specific plan document, board resolutions,
  individual grant notice, or 409A-stale strike. Trigger: any
  situation where the asker's specific plan deviates from the
  canonical instrument — extended-PTEP windows that auto-convert
  ISO→NSO at day 91, early-exercise-permitted plans (need the
  80/20 split + 83(b) within 30 days of exercise, not vest), single-
  trigger acceleration in the plan that the asker doesn't realize
  fires on a stock sale, repriced grants that reset the ISO
  $100k-per-year vesting limit, 409A valuations older than 12
  months that lose the safe-harbor presumption. Failure mode: Risk
  Officer surfaces the canonical mechanic ("ISOs become NSOs 90
  days after termination") and misses that THIS asker's plan
  document extends PTEP to 5 years and the conversion already
  happened, OR that the asker's 409A is 14 months stale and the
  strike they're being quoted is not the safe-harbor strike. Sanity
  check: if the answer turns on plan-document or 409A specifics,
  flag "verify against your actual grant notice" rather than
  asserting the canonical default.
- **The reference corpus is US-tax-and-Delaware-corporate by
  construction; non-US instruments and cross-border situations get
  coerced into the US template or footnoted away.** Holloway is
  US-focused; NCEO is US-focused; AICPA practice guides are
  US-focused; IRS publications are by definition US-only.
  Trigger: the asker is a non-US resident, a US person working
  abroad (PFIC reporting on foreign employer stock, FBAR/FATCA on
  foreign-broker accounts), a non-US person granted US-parent
  equity (UK EMI / Irish KEEP / French BSPCE / Israeli §102 /
  German RSU dry-tax-on-vest / Indian ESOP perquisite tax), or a
  US-to-non-US mover mid-vest (treaty sourcing, dual-tax
  exposure). Failure mode: Risk Officer reaches for the canonical
  US ISO/RSU/AMT framework and confidently produces advice that is
  legally and tax-mechanically wrong in the asker's actual
  jurisdiction — e.g. "exercise early to start the LTCG clock"
  given to a German tax resident whose dry-tax fires at vest
  regardless of exercise timing, or "file 83(b)" given to a UK EMI
  holder where the equivalent election is a Section 431 election
  with different timing and substance.
- **Necessary-but-not-sufficient: the corpus stops at the rule and
  defers application to a professional, but Risk Officer needs a
  CHECKABLE next step, not an "ask your advisor" hand-off.** The
  Holloway Guide explicitly positions itself as preparation for
  productive advisor conversations, not as a substitute. Trigger:
  any situation where the asker has no advisor relationship,
  cannot afford one ($400–$800/hr for a startup-equity-literate
  CPA in SF/NYC), faces a deadline shorter than the typical
  3–6-week intake cycle for a new tax-attorney engagement, or
  whose facts cross specialties (immigration + tax + corporate)
  such that no single advisor sees the full picture. Failure
  mode: Risk Officer surfaces "consult a CPA familiar with ISO
  AMT" as the named action, the asker doesn't have one, the
  deadline lapses, and the textbook-correct mechanic ("you had 30
  days to file 83(b)") becomes the explanation for why the
  outcome is now locked in. Sanity check: if the surfaced action
  is "consult an advisor", also surface the specific question the
  asker should walk in with AND the deadline by which that
  conversation has to happen, so the answer is actionable even if
  the advisor relationship is on the critical path.

## Representative voices
The Holloway Guide to Equity Compensation (Holloway, Joshua Levy and
Joe Wallin et al.). Adjacent: NCEO publications, AICPA practice guides,
the IRS publications cited in the Holloway footnotes (Pub 525, Pub 550,
Form 6251 instructions).

## Anti-pattern responses
This community would NOT say:
- "It's complicated, talk to a professional."
- "Generally, you should exercise when…"

It would say:
- "An incentive stock option (ISO) is a stock option that qualifies for
  preferential tax treatment under Section 422 of the Internal Revenue
  Code. Tax events for an ISO: no tax at grant; no regular-income tax at
  exercise, but the spread (FMV at exercise minus strike) is a preference
  item for the Alternative Minimum Tax; on sale, gain is long-term capital
  gain if the shares are held ≥2 years from grant and ≥1 year from
  exercise (a 'qualifying disposition'); otherwise, the spread at exercise
  is reclassified as ordinary compensation income (a 'disqualifying
  disposition')."
