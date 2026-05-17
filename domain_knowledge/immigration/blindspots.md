# immigration — blindspots.md (Layer 3)

Blindspot catalogue for `immigration`. Each entry names what a real
practitioner in the relevant framing would say is missed — anchored to
either an `Excludes` line in [`framings.md`](./framings.md) or to a
"Known blind spots OF this community" bullet in a V1 community profile
(`domain_knowledge/tech-career/communities/*.md`) where that profile
discusses immigration-adjacent topics. Per [`_schema.md`](../_schema.md),
every entry is relative to a framing and ships with a trigger pattern
and a concrete recovery move.

The `immigration` domain is **high_stakes: true** per
[`_meta_ontology.md` §2](../_meta_ontology.md). Per
[ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating),
**every Recovery move below ends in (or explicitly contains) the
phrase "consult a licensed immigration attorney" or an equivalent
professional-counsel deferral.** The wrong call here is not recoverable
on a multi-year horizon the way a bad ISO exercise is: missed filing
windows trigger out-of-status accrual; visa-stamp surprises at re-entry
trigger 214(b) refusals; unlawful-presence accrual past 180 / 365 days
triggers the §212(a)(9)(B) 3-year and 10-year bars; an erroneous
public-charge or marriage-fraud finding compounds across every future
adjudication of any benefit. This file is decision-support pointing
at where the analysis happens — the binding determination is the
attorney's, applied to the asker's full filing history, current USCIS /
DOS policy, and case-specific facts.

Each blindspot lists:
- **Statement** — one sentence naming what is missed
- **Source evidence** — the framing-Excludes anchor or community-profile
  audit line this blindspot was extracted from (not invented)
- **Trigger** — the situation pattern the Triage / Risk Officer should
  match against
- **Failure mode** — the specific bad outcome if the blindspot stays
  unsurfaced
- **Recovery move** — the concrete action that resolves it, ending in
  the Mechanism E professional-counsel deferral

The framing names below match [`framings.md`](./framings.md) exactly;
all 14 are covered with ≥ 5 entries each (≥ 70 total). Voice anchors
are conceptual — the source-views in
`domain_knowledge/immigration/sources.yaml` are not yet authored, so
attribution is to the *class* of community (immigration-attorney
blogs, AILA practitioner forums, MurthyDotCom-style consumer-rights
voice, USCIS Ombudsman annual reports, r/immigration / r/USCIS / r/h1b
subreddit threads, Boundless / Cyrus D. Mehta blog network, trackitt
priority-date forums). When `sources.yaml` lands, source-evidence
lines below should be tightened to the specific source-view ids.

---

## 1. Status-continuity framing

### 1.1 Out-of-status and unlawful presence are different inadmissibility regimes

- **Statement**: The framing's "never let status lapse" collapses two
  distinct USCIS / IJ regimes: *out-of-status* (failure to maintain
  conditions, e.g. unauthorized work) and *unlawful presence* (the
  §212(a)(9)(B) 3-year / 10-year bar clock, which under the 2018 F/J/M
  memo runs from a formal USCIS or IJ determination, not from I-94
  expiry). An asker who hears "you're out of status" and assumes the
  bar clock is already running can be steered into rash departure-and-
  CP gambles that themselves trigger the bar they were trying to avoid.
- **Source evidence**: `framings.md` §1 Excludes line on out-of-status
  vs unlawful presence being distinct regimes; reinforced by AILA-
  practitioner voice on the 2018 USCIS F/J/M memo's revised unlawful-
  presence-start-date rule (subsequently partially vacated by Guilford
  College v. Wolf, the operational policy oscillates).
- **Trigger**: Asker reports an I-94 expiry, denied COS / extension,
  or terminated H-1B and uses the phrase "I'm illegal now" or "the
  3-year-bar clock is running."
- **Failure mode**: Asker books a same-week flight to avoid the bar
  clock they believe is running; departure itself triggers a §222(g)
  visa voidance and forecloses CP, when the unlawful-presence clock had
  not yet started under the operative USCIS memo.
- **Recovery move**: Before any departure, get a written assessment of
  whether unlawful presence has started accruing under current USCIS
  policy — this is exactly the §212(a)(9)(B) calculation that turns
  on memo-vintage and case-specific facts; consult a licensed
  immigration attorney with the full I-94 / status history before
  acting on a bar-clock assumption.

### 1.2 The "automatic" 540-day EAD extension is procedurally fragile

- **Statement**: The framing presents the 540-day automatic EAD
  extension (and the H-1B 240-day work-auth extension on timely-filed
  extensions, and the F-1 cap-gap extension) as automatic. Each
  requires *timely* filing of the underlying renewal AND that the
  employer / DSO / asker met their own procedural deadlines — a
  receipt-notice delay, a payroll-system code-mismatch (USCIS class
  code C19 vs C09), or an HR-misfiled I-983 invalidates the automatic
  extension silently.
- **Source evidence**: `framings.md` §1 Excludes line on cap-gap and
  540-day extensions being presented as automatic when both require
  timely filing and procedural cooperation; reinforced by USCIS
  Ombudsman annual report patterns on EAD-renewal lag and class-code
  mismatch in employer E-Verify entries.
- **Trigger**: Asker reports an EAD expiry within the 540-day window
  and is being told "you're covered, keep working" by HR or by
  community-forum consensus.
- **Failure mode**: Employer's E-Verify or I-9 reverification system
  refuses the automatic-extension representation; asker is suspended
  without pay during the gap and accrues §245(c) unauthorized-employment
  exposure that surfaces years later at I-485 adjudication.
- **Recovery move**: Confirm the receipt notice's USCIS class code
  matches an automatic-extension-eligible category AND that the
  employer's I-9 reverification team accepts the receipt notice as
  evidence; if either is unclear, suspend work until a licensed
  immigration attorney has reviewed both the receipt and the I-9
  acceptance pathway.

### 1.3 245(k) is an under-used recovery path for short out-of-status gaps

- **Statement**: For employment-based AOS applicants, INA §245(k)
  forgives up to 180 aggregate days of out-of-status / unauthorized
  employment since last lawful admission; the framing's "any lapse is
  fatal" reflex misses 245(k) as a viable recovery path for an
  applicant who fell out briefly mid-pendency.
- **Source evidence**: `framings.md` §1 implicit gap on 245(k);
  `framings.md` §4 Excludes line on 245(k) under-use for dual-intent
  applicants; AILA-practitioner voice frequently emphasizes 245(k) as
  the most-missed forgiveness clause in employment-based AOS practice.
- **Trigger**: Asker reports a past out-of-status episode (gap between
  H-1B extensions, unauthorized work week, employer payroll lapse)
  AND is being told their EB-2 / EB-3 AOS is now foreclosed.
- **Failure mode**: Asker abandons employment-based AOS and routes to
  CP in a country with a hostile consulate, accumulating travel risk
  and re-entry exposure they didn't need to take on.
- **Recovery move**: Compute the aggregate out-of-status days since
  last lawful admission; if under 180, surface §245(k) as the operative
  forgiveness pathway and confirm applicability with a licensed
  immigration attorney before pivoting away from AOS.

### 1.4 Family-based AOS doesn't get 245(k); the framing collapses categories

- **Statement**: §245(k) applies *only* to employment-based AOS
  applicants. Family-based AOS applicants (marriage to USC, immediate-
  relative I-130 + I-485) get §245(i) (sunset, requires pre-2001 or
  pre-2000 grandfathering) or §245(c) exceptions, NOT §245(k). The
  framing's blanket "245(k) gives you 180 days of forgiveness" reflex
  is wrong for the modal marriage-based asker.
- **Source evidence**: `framings.md` §1 Excludes on out-of-status vs
  unlawful-presence regime confusion; AILA-practitioner voice on the
  §245(i) sunset (April 30, 2001) being the load-bearing date for
  family-based applicants with prior status gaps.
- **Trigger**: Asker is a marriage-based applicant (USC or LPR spouse)
  with prior out-of-status episodes AND is being assured "245(k) will
  forgive that."
- **Failure mode**: Asker files I-485 expecting 245(k) forgiveness on
  the marriage-based petition; USCIS denies for §245(c) ineligibility
  because the wrong subsection was relied on.
- **Recovery move**: Verify category-specific §245 subsection
  eligibility with a licensed immigration attorney before filing —
  §245(a) baseline, §245(c) bars (including the 245(c)(2) bar on
  unauthorized employment that disqualifies many employment-based
  filers when 245(k) does not apply), §245(i) grandfathering, and
  §245(k) employment-based forgiveness are four different regimes.

### 1.5 Strategic short out-of-status is rarely the right call but is sometimes the only call

- **Statement**: The framing has no native vocabulary for cases where
  the asker's correct move is to *allow* a short out-of-status interval
  while a different status matures — DACA recipients considering AOS
  through marriage, TPS holders considering CP, asylum-pending
  applicants whose underlying application changes status. These cases
  are rare but real, and the framing's reflex misroutes them.
- **Source evidence**: `framings.md` §1 Excludes line on the framing
  having no native vocabulary for strategic accrual of unlawful
  presence; AILA-practitioner voice on TPS / DACA / asylum-pending
  edge cases that don't fit a status-continuity-first heuristic.
- **Trigger**: Asker is DACA / TPS / asylum-pending AND is being
  pushed toward emergency status-preservation moves (rush COS, accept
  any H-1B sponsorship offer, marry-for-status timing forced).
- **Failure mode**: Asker rushes a status-preserving move that itself
  forecloses the longer-term path their actual category supports;
  e.g. DACA-to-H-1B-to-AOS sequence triggers preconceived-intent
  scrutiny that DACA-to-marriage-AOS would have avoided.
- **Recovery move**: For DACA / TPS / asylum-pending / VAWA-eligible
  askers, treat status-continuity as one variable among many rather
  than the dominant variable; route to a licensed immigration attorney
  with deep experience in the specific underlying category (DACA-
  specific or TPS-specific counsel, not generalist), as the pathways
  diverge sharply from the modal H-1B-to-EB-2 trajectory the framing
  defaults to.

---

## 2. Route-optimality framing

### 2.1 The route-velocity headline buries family-cost during transition

- **Statement**: The framing's "10 years faster" route advice (file
  EB-1A while H-1B max-out approaches; downgrade EB-2 → EB-3; pivot to
  CP) omits that during the transition the asker's H-4 spouse may face
  EAD lapse, H-4 children face derivative-status re-establishment, and
  the family faces health-insurance gaps on any status flip — costs
  the route-velocity arithmetic doesn't price.
- **Source evidence**: `framings.md` §2 Excludes line on under-
  weighting H-4 EAD lapses, school continuity, and health-insurance
  gaps during route transitions.
- **Trigger**: Asker has H-4 dependents (spouse with EAD, children
  enrolled in US schools) AND is being shown a route-velocity argument
  for switching categories or pivoting to CP.
- **Failure mode**: Asker pivots; H-4 spouse's EAD lapses for 6–12
  months during the new category's pendency; family income is halved
  and health-insurance becomes COBRA or marketplace at full premium;
  the "10 years faster" gain is consumed by 2 years of family
  disruption.
- **Recovery move**: Before any route pivot, model the dependent-side
  consequences on the same timeline as the principal's route gain —
  H-4 EAD validity, child CSPA-age clock, school visa renewals;
  consult a licensed immigration attorney whose practice includes
  derivative-status management, not only principal-petition optimization.

### 2.2 Visa Bulletin forecasting is over-confident relative to DOS's own internal forecast

- **Statement**: The framing's "EB-3 India will be faster this year"
  type confidence exceeds what DOS analyst Charlie Oppenheim retains
  in his public briefings — EB-3 India 2020–22 famously reversed
  within 6 months. The framing's category-arbitrage moves often back
  themselves into the slower category by the time the move executes.
- **Source evidence**: `framings.md` §2 Excludes line on Visa Bulletin
  forecasting overconfidence; trackitt / r/EB1 / r/EB2 priority-date
  forum threads documenting the 2020–22 EB-3 India reversal as the
  paradigm case; AILA-practitioner voice on the difference between
  DOS public projections and actual monthly bulletin movement.
- **Trigger**: Asker is being advised to downgrade EB-2 → EB-3 (or
  vice versa) on the basis of a single recent Visa Bulletin movement
  or a projection more than 3 months forward.
- **Failure mode**: Asker downgrades, the bulletin reverses inside 6
  months, the new category retrogresses, and the asker has paid a
  second I-140 fee plus interfiling delay for negative route value.
- **Recovery move**: Treat single-bulletin trends as noise; require
  3+ consecutive months of consistent movement plus DOS / AILA
  consensus before pivoting; even then, confirm the trade-off with a
  licensed immigration attorney who tracks bulletin-projection
  reliability per category.

### 2.3 USCIS adjudication quality varies by service center and administration

- **Statement**: The framing assumes USCIS adjudication is constant
  across service centers and administrations; EB-1A and NIW RFE rates
  have varied 2–3× between 2017 and 2023 by service center, and
  identical petitions receive materially different scrutiny under
  different policy administrations. "The case is strong, file it" is
  calibrated to a steady-state adjudicator that doesn't exist.
- **Source evidence**: `framings.md` §2 Excludes line on USCIS
  adjudication quality variation; `framings.md` §9 Excludes line on
  political-administration calibration for EB-1A / NIW;
  AILA-practitioner forum threads on Texas vs Nebraska service
  center RFE-rate divergence.
- **Trigger**: Asker is considering an EB-1A / NIW self-petition AND
  the framing advice is calibrated to a service-center / administration
  pair different from the one that will adjudicate the actual filing.
- **Failure mode**: Asker spends $10k+ on attorney fees and 100+ hours
  on evidence curation for a petition calibrated to the prior RFE
  regime; receives a denial whose pattern matches the current regime's
  scrutiny on a criterion the prior regime would have accepted.
- **Recovery move**: Before filing, ask the attorney for service-
  center-specific and administration-specific RFE-rate data on the
  exact petition type (EB-1A vs NIW vs O-1A) and the exact criterion
  set being argued; if the attorney can't provide that calibration,
  consult a licensed immigration attorney who tracks USCIS service-
  center variance as part of practice management.

### 2.4 The EB-1A / NIW per-hour-wage math often loses to the day-job alternative

- **Statement**: A sophisticated EB-1A petition is $8–15k in attorney
  fees plus 100–200 hours of the applicant's own evidence-curation
  time; if the incremental green-card-velocity is 2 years on an
  8-year wait, the per-hour wage on the time invested often runs less
  than the asker's day-job opportunity cost.
- **Source evidence**: `framings.md` §2 Excludes line on not pricing
  attorney time + applicant evidence-curation time against
  opportunity cost; founder-engineer-blogger voice on time-value
  framing common to engineering audiences.
- **Trigger**: Asker is high-TC (>$300k), in an EB-2/3 backlog where
  EB-1A would shave 1–3 years, AND is being told "go for the EB-1A,
  you have the profile."
- **Failure mode**: Asker invests 200 hours on evidence assembly +
  $12k cash; receives EB-1A denial after RFE; the 2-year-velocity-gain
  was hypothetical and the underlying EB-2/3 PERM is now stale because
  the asker was distracted from sponsor-management during the EB-1A
  push.
- **Recovery move**: Run the per-hour wage calc explicitly (TC ÷ 2080
  × hours invested vs incremental velocity × discount rate); if the
  EB-1A path doesn't clear that bar with a meaningful margin of
  safety, route to the lower-effort options first (EB-2 NIW, priority-
  date portability moves), and consult a licensed immigration attorney
  to size the realistic RFE-and-denial probability rather than the
  headline approval-rate.

### 2.5 Self-petition independence presumes the petition succeeds

- **Statement**: The framing presents EB-1A / NIW as a route to
  visa-independent leverage; the headline assumes the petition
  succeeds. RFE-then-denial restarts the dependency cycle while
  consuming the cash and applicant time already spent, and a denied
  EB-1A creates a record adjudicators in future filings can consult.
- **Source evidence**: `framings.md` §10 Excludes line on self-
  petition fees + time as one-time costs that USCIS rejection /
  RFE-denial restarts.
- **Trigger**: Asker is being sold EB-1A as a definitive exit from
  employer-sponsorship dependency, without a denial-probability bound.
- **Failure mode**: Asker self-petitions, denial issues, the asker
  is back in employer-sponsored dependency with reduced cash buffer
  AND a denied-EB-1A-in-file that complicates a later attempt; the
  "independence" narrative collapses.
- **Recovery move**: Before filing, build the contingency plan for
  RFE and for denial (continue parallel employer-sponsored petition;
  preserve cash reserve sized to one additional attorney engagement);
  size the petition as a 2-attempt strategy not a 1-attempt strategy,
  and consult a licensed immigration attorney about the record-
  consequence of a denied petition for future filings.

---

## 3. Filing-window-arbitrage framing

### 3.1 Dates-for-Filing is DOS's table; AOS-acceptance is USCIS's call

- **Statement**: "DFF is current so I can file I-485" assumes USCIS
  will accept I-485s based on DFF — USCIS posts this acceptance
  determination monthly and the answer is sometimes no. DFF is
  *DOS's* table; AOS-filing eligibility is *USCIS's* call, and they
  can diverge for the same bulletin month.
- **Source evidence**: `framings.md` §3 Excludes line on USCIS's own
  monthly determination of whether to accept DFF-based I-485 filings;
  MurthyDotCom-style consumer-rights voice on the DFF-vs-USCIS-
  acceptance distinction as the most-frequently-misread bulletin
  element.
- **Trigger**: Asker sees DFF go current and is about to assemble the
  I-485 package without checking USCIS's monthly DFF-acceptance
  announcement.
- **Failure mode**: Asker pays $1500+ in filing fees, gathers medical
  exam and biometric photos and affidavits; USCIS rejects the I-485
  for filing-eligibility-not-supported because the asker relied on
  DFF when USCIS announced FAD-only acceptance for that month.
- **Recovery move**: For every DFF-current month, check the USCIS
  "Adjustment of Status Filing Charts from the Visa Bulletin"
  announcement (separate URL from the DOS bulletin) before assembling
  the I-485; confirm filing-eligibility with a licensed immigration
  attorney if USCIS's announcement is ambiguous.

### 3.2 The I-693 validity window changed in late 2024

- **Statement**: The framing's "pre-stage your I-693 medical exam"
  advice from older sources reflects the prior 60-day-validity (from
  signing) rule. USCIS extended I-693 validity to "indefinite if
  signed by civil surgeon, no expiration" in late 2024; pre-staging
  logic from earlier sources is now over-cautious in one direction
  (medical re-do not needed) and under-cautious in another (sealed
  envelope handling matters more, not less, when the document is
  multi-year valid).
- **Source evidence**: `framings.md` §3 Excludes line on the late-2024
  I-693 validity-rule change; AILA-practitioner voice on the
  significance of the indefinite-validity update for cross-priority-
  date-cycle filings.
- **Trigger**: Asker is following pre-2024 pre-staging guidance OR is
  re-doing a medical exam they had done within the prior year because
  "the 60-day window expired."
- **Failure mode**: Asker pays $300–500 for an unnecessary repeat
  medical exam AND delays I-485 filing waiting for the new exam
  slot; the original I-693 was still valid under current rules.
- **Recovery move**: Confirm current I-693 validity rules at USCIS's
  Policy Manual Vol 8 Part B before re-doing a medical exam; if the
  asker holds a properly-sealed I-693 from any post-late-2024
  signing date, consult a licensed immigration attorney about
  filing with that I-693 rather than re-doing.

### 3.3 Concurrent I-485 filing locks the asker out of certain status moves

- **Statement**: Filing I-485 concurrent with I-140 unlocks EAD/AP
  benefits but locks the asker out of certain non-immigrant moves —
  the pending I-485 abandons certain nonimmigrant-intent statuses on
  travel without AP, complicates COS to a non-dual-intent status,
  and changes the calculus on a layoff response (the asker is now
  reasoning from "I have a pending AOS" rather than "I have H-1B
  optionality").
- **Source evidence**: `framings.md` §3 Excludes line on filing-window-
  as-not-costless; `framings.md` §4 Excludes line on the dual-intent
  mechanics that turn on concurrent-AOS status.
- **Trigger**: Asker is about to file concurrent I-485 AND has not
  modeled the post-filing status flexibility (travel, COS, layoff
  response, H-4 EAD downstream).
- **Failure mode**: Asker files concurrent; receives a great offer at
  a non-dual-intent employer 4 months later; cannot COS to the new
  status without abandoning the pending I-485; declines the offer or
  abandons the AOS, either of which destroys value the concurrent-
  filing was supposed to create.
- **Recovery move**: Before filing concurrent, enumerate the next-12-
  months status moves the asker may want to make (travel, employer
  change, COS, H-4 dependent moves) and model each against the
  pending-I-485 status; consult a licensed immigration attorney on
  which of those moves remain feasible post-filing.

### 3.4 H-4 dependents must also file or risk derivative-eligibility loss on age-out

- **Statement**: Concurrent I-485 filing for the principal must be
  matched by I-485 filings for each H-4 dependent if the principal
  wants derivative AOS coverage; for H-4 children near age 21, the
  CSPA-age lock-in is determined by their *own* I-485 filing date
  (or sought-to-acquire action), not the principal's, and missing
  the derivative filing can age-out a child whose CSPA age was
  otherwise protected.
- **Source evidence**: `framings.md` §3 Excludes line on H-4 dependents
  also needing to file to preserve derivative eligibility on age-out;
  `framings.md` §6 Mental model on the CSPA formula's PD-current
  trigger and the per-child filing requirement.
- **Trigger**: Asker has an H-4 child age 17–21 AND is filing
  concurrent I-485 for the principal without parallel derivative
  filings.
- **Failure mode**: Principal's I-485 is filed; child turns 21 before
  derivative I-485 is filed; CSPA age determination is destabilized;
  child must re-file under F2B with a fresh priority-date and a
  multi-year wait; family is split in green-card timing.
- **Recovery move**: File all dependent I-485s on the same day as
  the principal's; for any H-4 child in the 17–22 age range, treat
  the derivative-filing timing as a critical-path item and consult a
  licensed immigration attorney specifically on CSPA-age preservation
  for that child before any concurrent filing.

### 3.5 The asker without an attorney on retainer can't reliably do monthly Visa Bulletin watch

- **Statement**: The framing's "monitor continuously" advice presumes
  the asker has bandwidth to read a monthly DOS document and
  translate it into action; for an asker without an attorney on
  retainer the practical question "do I need to do anything this
  month" is opaque, and a missed bulletin can mean a missed window
  that doesn't re-open for years.
- **Source evidence**: `framings.md` §3 Excludes line on bulletin-watch
  being over-asked for askers without ongoing legal support;
  r/immigration / trackitt forum threads on missed-bulletin-window
  regret as a recurring pattern.
- **Trigger**: Asker has approved I-140 and is in retrogression but
  has no attorney on retainer AND is not on any AILA-attorney-curated
  bulletin-alert distribution list.
- **Failure mode**: Asker misses the one bulletin cycle where their
  PD became current under DFF; window closes the following month; the
  asker's I-485 filing slips 12+ months until DFF re-opens.
- **Recovery move**: Subscribe to at least two attorney-curated
  bulletin-alert services (Murthy Dot Com, Boundless, Cyrus D. Mehta
  newsletter, AILA bulletin commentary) AND retain a licensed
  immigration attorney on at least a low-touch consultation basis so
  that bulletin-driven action items have a confirmed escalation path.

---

## 4. Dual-intent-and-abandonment framing

### 4.1 H-1B is dual-intent but the visa stamp can have expired

- **Statement**: "H-1B is dual-intent so I can travel" is correct on
  AOS-abandonment grounds; the framing skips that the visa stamp
  itself (the consulate stamp permitting entry, distinct from the
  I-94) may have expired during AOS pendency. The asker travels on a
  valid I-94 with pending I-485, and discovers at re-entry that they
  need to renew the visa stamp at a consulate before returning.
- **Source evidence**: `framings.md` §4 Excludes line on visa-stamp
  expiry during AOS pendency; AILA-practitioner voice on the
  CBP-vs-DOS coordination gap as a recurring trap.
- **Trigger**: Asker has pending I-485 AND valid H-1B I-94 AND visa
  stamp from prior issuance, and is planning international travel
  without checking the stamp validity.
- **Failure mode**: Asker travels; at return, CBP defers re-entry
  pending fresh visa stamping; asker is stuck abroad for the
  consulate's appointment slot (weeks to months) and the AOS
  pendency continues without the asker present for any in-US
  biometrics, interview, or RFE response.
- **Recovery move**: Before any international travel during pending
  AOS, verify (1) AP validity AND (2) underlying visa-stamp validity
  for the return; if the stamp is expired, pre-schedule a consular
  appointment before departure AND consult a licensed immigration
  attorney on whether to defer the trip.

### 4.2 245(k) under-use on AOS abandonment recoveries

- **Statement**: For employment-based AOS applicants who fell out of
  status briefly (up to 180 aggregate days since last admission),
  §245(k) is a recovery pathway the framing's "any abandonment is
  fatal" posture under-promotes. The framing's reflex on travel-
  without-AP is the same — to treat the AOS as definitively
  abandoned, when 245(k) plus a refiled I-485 may be available.
- **Source evidence**: `framings.md` §4 Excludes line on 245(k) being
  mentioned in passing but under-promoted as a recovery path.
- **Trigger**: Asker traveled without AP, or otherwise interrupted
  AOS pendency, and is being told the AOS is dead.
- **Failure mode**: Asker abandons the employment-based AOS and
  routes to CP with consulate-discretion risk; the §245(k) path
  through a refiled I-485 was open the whole time.
- **Recovery move**: For employment-based applicants with any
  interrupted-AOS history, evaluate §245(k) recovery before pivoting
  to CP; consult a licensed immigration attorney to compute the
  aggregate out-of-status days and confirm the refiled-I-485 pathway
  is viable.

### 4.3 Advance Parole travel has residual H-1B-status risk under older case law

- **Statement**: The framing presents AP as the permission slip to
  travel during AOS; older case law treated AP-departure-and-return
  as breaking H-1B status, requiring fresh H-1B stamping abroad
  before any later extension. Newer USCIS guidance softened this but
  circuit splits remain in fringe cases — and the asker who relies
  on the "AP cures everything" headline can find their H-1B
  extension foreclosed at the next renewal.
- **Source evidence**: `framings.md` §4 Excludes line on AP travel
  carrying procedural risk under older case law and remaining circuit
  splits.
- **Trigger**: Asker is traveling on AP with concurrent H-1B I-94
  AND is planning to extend H-1B post-return (e.g. as a fallback if
  AOS is denied or to preserve cap-exempt extension eligibility).
- **Failure mode**: AP-departure is recorded; asker returns as
  parolee not as H-1B admittee; subsequent H-1B extension is denied
  on "no current H-1B status to extend"; asker must do fresh
  consular H-1B stamping abroad before any further extension is
  possible.
- **Recovery move**: For askers who want to preserve H-1B status as
  a fallback, the conservative path is to re-enter on the H-1B
  stamp (not on AP) when the underlying H-1B visa is still valid;
  consult a licensed immigration attorney on the AP-vs-H-1B re-entry
  choice given current circuit law and the asker's specific service
  center's recent practice.

### 4.4 CBP secondary inspection can detain even an AP-approved returning applicant

- **Statement**: The framing protects against AOS abandonment but not
  against CBP secondary inspection on return. A returning AP holder
  with an inconsistent I-94 history, prior 214(b) refusal, evidence
  of unauthorized employment, or any social-media flag can be paroled
  in but referred for further questioning, and in extreme cases
  detained and placed in removal proceedings.
- **Source evidence**: `framings.md` §4 Excludes line on CBP secondary
  inspection risk despite AP; AILA-practitioner voice on CBP
  practices at JFK / LAX / ATL secondary inspection patterns.
- **Trigger**: Asker has any of: prior visa refusal, gap in I-94 history,
  documented unauthorized work, contested past employment, AND is
  traveling on AP during AOS.
- **Failure mode**: Asker is paroled into the US with a Notice to
  Appear; AOS is now adjudicated in removal proceedings before an
  immigration judge, not by USCIS, with vastly different procedural
  rules and burdens of proof.
- **Recovery move**: For any asker with a complicated past-status
  record, do not travel on AP without first consulting a licensed
  immigration attorney on the CBP-secondary-inspection probability;
  if travel is necessary, prepare a portfolio of supporting documents
  (status history, employer-attestation letters, AOS pendency proof)
  to carry on the return flight.

### 4.5 Preconceived intent applies beyond the 90-day rule when other facts support it

- **Statement**: The 90-day preconceived-intent rule on B-visa entrants
  is a Foreign Affairs Manual guideline, not a hard line; a §214(b)
  refusal can apply *outside* the 90-day window when other facts
  support preconceived intent (e.g. apartment lease signed before
  entry, job offer letter dated before visa issuance, school
  enrollment paperwork pre-arrival). The framing's "wait until day
  91" advice is structurally weak.
- **Source evidence**: `framings.md` §13 Excludes line on the 90-day
  rule being a FAM guideline rather than a hard line; AILA-
  practitioner voice on §214(b) findings outside the 90-day window.
- **Trigger**: Asker entered as B-1/B-2 and is being advised to file
  COS on day 91 of presence to "clear the preconceived-intent rule."
- **Failure mode**: Asker files COS on day 91; USCIS / consular review
  surfaces evidence of pre-entry intent (LinkedIn job-offer
  announcement, lease signed pre-arrival); 214(b) refusal applies
  despite the day-count clearing; the COS denial creates a refusal
  record that complicates every future visa application.
- **Recovery move**: For any COS after a B-visa entry, audit the
  asker's documentary record for pre-entry-intent evidence (email
  archives, social-media posts, lease / school / employment paperwork
  dates); if any evidence exists, the day-91 heuristic is insufficient
  and the asker should consult a licensed immigration attorney on
  whether COS or CP is the lower-risk path.

---

## 5. AC21-portability framing

### 5.1 SOC-code literalism on promotions can trigger an RFE 18 months after the port

- **Statement**: AC21 §106(c)'s "same or similar occupation" standard
  is administered by USCIS adjudicators reading SOC codes literally;
  a promotion from Software Engineer (15-1252) to Software
  Engineering Manager (11-3021) crosses major-group boundaries
  (15-xxxx Computer/Math vs 11-xxxx Management) and the framing's
  "you're fine, same domain" reassurance routes the asker into an
  RFE that surfaces 18 months later at AOS adjudication.
- **Source evidence**: `framings.md` §5 Excludes line on SOC code
  literalism on promotions; AILA-practitioner voice on the IC-to-
  manager port being the most-RFE'd transition pattern.
- **Trigger**: Asker is being recruited for a managerial role at a
  new employer AND is being advised the role is "same or similar"
  to their current IC role for AC21 purposes.
- **Failure mode**: Asker ports; supplement-J filed describing
  manager duties; RFE issues 18 months later asking for evidence the
  new role is same-or-similar to the original PERM role; the asker
  has to either argue the management role is similar (often loses)
  or restart the PERM at the new employer.
- **Recovery move**: For any port crossing SOC major-group boundaries
  (especially IC ↔ management, engineering ↔ product, or any
  cross-discipline move), get a written same-or-similar analysis
  from a licensed immigration attorney *before* accepting the new
  role; if the analysis is unfavorable, negotiate the role
  description to stay within the original SOC major group.

### 5.2 The new employer's immigration team may not respond to RFEs on time

- **Statement**: The framing assumes the new employer cooperates on
  supplement-J timing and on responding to RFEs about job duties; in
  practice the new employer may have no in-house immigration team,
  may use a generalist HR vendor unfamiliar with AC21 portability,
  or may simply not respond to RFE requests within the 87-day window.
- **Source evidence**: `framings.md` §5 Excludes line on new employer
  immigration-team cooperation assumption; AILA-practitioner forum
  threads on RFE-response-failure at smaller employers.
- **Trigger**: Asker is porting to a smaller employer (Series B
  startup, agency, consulting firm) without in-house immigration
  counsel.
- **Failure mode**: RFE issues; new employer's HR doesn't recognize
  the request's procedural urgency; 87-day deadline lapses; AOS
  denial; asker is now both employer-changed AND out of underlying
  approved-petition status.
- **Recovery move**: Before accepting an offer that requires AC21
  porting, confirm in writing that the new employer (a) maintains
  immigration counsel reachable on a 7-day response time AND
  (b) commits to producing job-duty letters and RFE responses
  within USCIS-set windows; if the employer can't commit, the asker
  should retain their *own* licensed immigration attorney to manage
  the port and budget for parallel attorney spend.

### 5.3 The 180-day mark assumes I-485 doesn't get denied procedurally

- **Statement**: AC21 §106(c) portability after 180 days of I-485
  pendency presumes the I-485 receipt is the lock-in event; the
  framing doesn't catch that USCIS-initiated AOS denials in the
  180-day window (for a procedural defect in the underlying I-140
  that surfaces later, or for an applicant-side disclosure error
  caught during background check) can re-open the abandonment risk
  even after the 180-day mark has nominally passed.
- **Source evidence**: `framings.md` §5 Excludes line on USCIS-
  initiated AOS denials potentially re-opening the abandonment risk;
  AILA-practitioner voice on Motion-to-Reopen practice when the
  AC21-portability assumption is undercut.
- **Trigger**: Asker has ported under AC21 §106(c) AND receives an
  RFE / NOID / denial on the underlying I-140 or I-485 after the
  port.
- **Failure mode**: Asker has been at new employer 6+ months;
  underlying I-485 is denied for I-140-defect; the AC21-portability
  argument no longer protects status (it was premised on a valid
  I-485); asker is suddenly unauthorized at the new employer.
- **Recovery move**: At any RFE/NOID on the underlying I-140/I-485
  post-port, do not assume AC21 portability still protects status;
  consult a licensed immigration attorney immediately about
  Motion-to-Reopen mechanics, parallel H-1B extension at the new
  employer, and the time-sensitive options to bridge an interruption
  while the underlying defect is challenged.

### 5.4 Human portability is not the same as legal portability

- **Statement**: The framing prices employer change as a *legal*
  portability question and skips the *human* portability question:
  the asker's PERM was sponsored by a hiring manager who would
  write the reference call, whose 4-year relationship is the de
  facto employment-based GC machinery. The new employer's HR has
  no equivalent context, which lengthens RFE response cycles and
  can change role-description in ways that compromise the AC21
  same-or-similar argument.
- **Source evidence**: `framings.md` §5 Excludes line on human-
  portability being skipped; founder-engineer-blogger voice on the
  hiring-manager-as-GC-machinery dynamic.
- **Trigger**: Asker is porting AND the relationship-to-PERM-sponsor
  is the asker's first long-term employer relationship in the US.
- **Failure mode**: Asker ports; new employer's HR doesn't know the
  PERM history; future RFE on similar-occupation requires evidence
  from the original PERM employer that the asker can no longer easily
  obtain; PERM-restart becomes the only recovery.
- **Recovery move**: Before porting, request the PERM file from the
  original employer (Form ETA-9089, all supporting evidence, role-
  description language); preserve every email establishing the role
  history; consult a licensed immigration attorney on whether to
  re-engage original-employer counsel as a witness in case future
  RFE evidence is needed.

### 5.5 Layoff-during-grace AC21 supplement-J has a 60-day clock most askers miss

- **Statement**: When an H-1B holder with approved I-140 and I-485
  pending 180+ days is laid off, AC21 §106(c) allows porting to a
  new employer via supplement-J within the 60-day H-1B grace period.
  The framing's portability vocabulary doesn't always foreground the
  60-day clock as the binding constraint, and the asker who waits to
  evaluate offers carefully runs the clock out.
- **Source evidence**: `framings.md` §5 Mental model line on
  supplement-J within the 60-day grace; reinforced by
  `domain_knowledge/tech-career/communities/founder-engineer-bloggers.md`
  Known-blindspot 1 on H-1B 60-day grace period mechanics being
  treated as someone else's problem in tech-career advice.
- **Trigger**: Asker is laid off mid-AOS pendency AND is being told
  to "take time to find the right next role" without the 60-day
  AC21-supplement-J clock surfaced.
- **Failure mode**: Asker uses 75 days to evaluate offers; 60-day
  grace expired on day 60; AC21 portability is foreclosed; asker
  must restart from H-1B cap-subject filing or accept a worse offer
  at any willing sponsor.
- **Recovery move**: On day 1 of layoff, surface the 60-day clock as
  the binding constraint, NOT the 90-day-for-decision-comfort default;
  consult a licensed immigration attorney within the first week of
  layoff to model AC21 portability, H-1B transfer, and any parallel
  options (cap-exempt employer, EAD-based work if I-485 has EAD).

---

## 6. CSPA-and-family-clock framing

### 6.1 Immediate-relative children of USCs get a different (often stronger) CSPA protection

- **Statement**: The CSPA formula doesn't apply uniformly across
  categories: immediate-relative children of US citizens get a
  different (and in some readings stronger) protection than
  employment-based or F-preference derivative children. The framing's
  single-formula summary glosses category-specific nuance.
- **Source evidence**: `framings.md` §6 Excludes line on CSPA formula
  not applying uniformly across categories; AILA-practitioner voice
  on the IR-2 stronger-protection pattern.
- **Trigger**: Asker is considering marriage timing (USC vs LPR
  petitioner) with a child age 17–21 in the picture; or asker is in
  EB-2/3 with a 17–21 child; framing-voice is applying a single CSPA
  formula across both.
- **Failure mode**: Asker chooses the petitioning pathway based on
  the wrong CSPA formula; child ages out under the actual
  category-specific rule that would have been preserved under the
  alternative; family is split in green-card timing.
- **Recovery move**: For any family with a child age 17–21 and a
  petitioning-pathway choice, get a written category-by-category
  CSPA-age projection from a licensed immigration attorney before
  committing to one pathway; this is one of the highest-leverage
  decisions in the entire immigration system and the wrong choice
  is rarely recoverable.

### 6.2 "Sought to acquire" trigger shifted from FAD-current to DFF-current in 2023

- **Statement**: The "sought to acquire" 1-year window from PD-current
  to act has been re-litigated repeatedly (Cuellar de Osorio, etc.);
  the practical USCIS reading shifted in 2023 from FAD-current to
  DFF-current as the trigger. The framing's prior-vintage documents
  and 2019-era attorney memos may still anchor on the FAD-current
  reading, which costs the asker months of CSPA-protection time.
- **Source evidence**: `framings.md` §6 Excludes line on the 2023
  USCIS policy shift; AILA-practitioner voice on the post-2023
  CSPA-age-lock-in mechanics.
- **Trigger**: Asker is referencing pre-2023 CSPA guidance OR
  attorney memo OR a community-forum thread that uses FAD-current
  as the sought-to-acquire trigger.
- **Failure mode**: Asker waits for FAD-current to act on a child's
  AOS filing; DFF-current passed months earlier; child's CSPA age
  is calculated to the FAD-current date that is too late, child
  ages out.
- **Recovery move**: Confirm the operative USCIS policy is the
  post-2023 DFF-current reading via the USCIS Policy Manual Vol 7
  Part A; consult a licensed immigration attorney for any child
  with a CSPA-age projection within 6 months of 21 on the
  DFF-current vs FAD-current question.

### 6.3 Marriage by the child during pendency converts F2A derivative to F3 standalone

- **Statement**: Marriage by the child *before* CSPA crystallizes
  converts the F2A derivative into an F3 / F4 standalone — a step
  the framing treats as a footnote when it should be the headline
  for askers with adult children considering marriage timing.
- **Source evidence**: `framings.md` §6 Excludes line on marriage-
  converts-category mechanic; family-petitioner voice on the F3
  category timeline differential.
- **Trigger**: Asker is in a family-preference category (F2A
  derivative) AND has an unmarried adult child also in the
  petition AND the child is considering marriage during the
  pendency window.
- **Failure mode**: Child marries; F2A derivative converts to F3
  standalone with a multi-decade priority-date queue; family
  green-card timing is set back 10–20 years for that child.
- **Recovery move**: For any F2A petition with an unmarried adult
  child, treat the child's marriage timing as a critical-path
  immigration decision (not only a personal decision); consult a
  licensed immigration attorney to model the marriage-timing
  scenarios before any wedding date is set.

### 6.4 CSPA derivative-child status doesn't extend to children-of-children

- **Statement**: A CSPA-protected child whose own children are
  born during pendency doesn't transmit derivative status to those
  grandchildren — they are not "derivative beneficiaries" of the
  original petition; they need separate petitions once the
  CSPA-protected child becomes LPR. The framing's "the family moves
  together" reflex assumes a three-generation continuity that the
  statute doesn't grant.
- **Source evidence**: `framings.md` §6 Excludes line on children-
  of-dependents having separate aging-out logic;
  `framings.md` §8 Excludes line on children of dependents not
  inheriting derivative status.
- **Trigger**: Asker is in a multi-generation petition (principal,
  derivative child, child's own children) and is treating all
  generations as derivative.
- **Failure mode**: Asker's I-485 is approved; CSPA-protected child
  becomes LPR; grandchildren born during pendency are not LPRs and
  must enter on separate petitions, often with multi-year waits.
- **Recovery move**: For any multi-generation family in a single
  petition's pendency, surface the grandchild question explicitly;
  consult a licensed immigration attorney about whether parallel
  petitions for grandchildren are needed and whether the timing
  can be coordinated.

### 6.5 Foreign-school time during pendency may not count uniformly toward CSPA preservation

- **Statement**: A CSPA-protected child whose CSPA-age would be 20.5
  at PD-current may be enrolling in a foreign university during
  pendency; the framing's "they're protected" doesn't address
  whether the time abroad counts the same way against the formula,
  whether long absences from US presence affect the sought-to-acquire
  determination, or whether re-entry as F-1 student vs as F-2
  dependent affects the analysis.
- **Source evidence**: `framings.md` §6 Excludes line on the
  cross-border school decision and CSPA-formula interaction.
- **Trigger**: Asker has a CSPA-protected child considering or
  enrolled in foreign higher education during the pendency window.
- **Failure mode**: Child spends 2 years at foreign university;
  returns to act on the I-485 derivative filing; USCIS interprets
  the time abroad as evidence of non-sought-to-acquire intent or as
  a complication on the residence-during-AOS analysis; CSPA
  protection is contested.
- **Recovery move**: For any child considering foreign higher
  education during pendency, consult a licensed immigration attorney
  *before* the enrollment decision on (a) whether foreign-time
  affects the CSPA-age formula directly, (b) whether re-entry
  visa-class choice (F-1 vs F-2) affects the sought-to-acquire
  analysis, (c) whether biometric and interview attendance during
  the absence is preserved.

---

## 7. Priority-date-portability framing

### 7.1 PD doesn't port from PERM-based EB-2 to NIW self-petition

- **Statement**: "PD ports forward to the new petition" is correct
  only when the new petition is also employer-sponsored using the
  same underlying labor certification; for a switch from EB-2 PERM
  to EB-2 NIW (self-petition), the PD does *not* port — the asker
  starts over with a fresh PD. The framing's portability shorthand
  misses this and the asker who self-petitions expecting to keep
  their May 2014 PD discovers they're now reasoning from a 2026 PD.
- **Source evidence**: `framings.md` §7 Excludes line on PD-not-
  porting from PERM-based to NIW self-petition.
- **Trigger**: Asker has approved EB-2 PERM-based I-140 AND is being
  advised to also file EB-2 NIW "to use the existing priority date."
- **Failure mode**: Asker files NIW; approved; assumes the PD
  carries; at I-485 filing realizes the NIW PD is the NIW-filing-
  date, not the PERM PD; the velocity gain the asker reasoned
  toward never materializes.
- **Recovery move**: Before filing any second I-140 in a different
  EB sub-category, confirm in writing with a licensed immigration
  attorney exactly which PD attaches to the new petition — the
  rules differ by sub-category (NIW vs PERM-based EB-2; EB-1A vs
  PERM-based EB-1B/C; cross-employer PERM-based portability).

### 7.2 Interfile administrative variance is large across service centers

- **Statement**: The interfile process (moving a pending I-485 from
  one I-140 / category to another) is administratively governed at
  the field-office level; some service centers accept the interfile
  request quickly, others batch it and the I-485 ages unattended for
  18+ months. The framing's "interfile and you move to EB-3
  velocity" assumes a procedural reliability USCIS doesn't deliver
  uniformly.
- **Source evidence**: `framings.md` §7 Excludes line on interfile
  variance across service centers; AILA-practitioner voice on
  Nebraska vs Texas vs national-benefits-center interfile-response
  timing.
- **Trigger**: Asker is being advised to interfile from EB-2 to EB-3
  (or vice versa) on the assumption of fast acceptance.
- **Failure mode**: Asker files the downgrade I-140; submits the
  interfile request; service center batches it; 18 months pass with
  the I-485 still attached to the original I-140; the alternate-
  category velocity opportunity has closed.
- **Recovery move**: Before filing the interfile, request from a
  licensed immigration attorney the service-center-specific recent
  interfile-acceptance timing (national-benefits-center data, AILA
  practitioner-list discussions); if the asker's service center has
  6+ month interfile lag, the downgrade strategy may not be
  worthwhile.

### 7.3 Cross-chargeability via spouse is a separate move under-promoted

- **Statement**: Cross-chargeability (using a non-quota-backlogged
  spouse's country of birth as the chargeability country) is a
  separate PD-portability move the framing's category-only
  vocabulary doesn't name — under-promoted relative to its impact
  for India / China asker-spouse pairs where the spouse was born in
  a non-backlogged country.
- **Source evidence**: `framings.md` §7 Excludes line on cross-
  chargeability via spouse being under-promoted; DOS-watcher voice
  on cross-chargeability as one of the highest-leverage moves
  available for India/China principals.
- **Trigger**: Asker is India- or China-born AND has a spouse born
  in a non-backlogged country (anywhere outside India/China/Mexico/
  Philippines for most EB categories) AND is being shown a category-
  arbitrage path without cross-chargeability surfaced.
- **Failure mode**: Asker pursues an expensive EB-2-to-EB-1A pivot
  attempting to shave years off the queue; cross-chargeability
  through the spouse would have given the same effect at lower cost
  with no petition-restart risk; the asker spends effort on the
  wrong axis.
- **Recovery move**: For any India- or China-born principal with a
  non-backlogged-country spouse, evaluate cross-chargeability
  before any category-arbitrage moves; consult a licensed
  immigration attorney to confirm the cross-chargeability
  documentation requirements and the petitioning-sequence (spouse
  may need to be primary on certain documents to claim the benefit).

### 7.4 F2A → IR1 automatic conversion ports the PD but accelerates the category

- **Statement**: When an LPR petitioner naturalizes mid-pendency,
  F2A petitions automatically convert to IR1 — the PD ports but the
  category accelerates from F2A's backlog to IR1's
  immediate-availability. This is the family-side equivalent of
  EB-2/EB-3 portability the framing treats as a separate vocabulary
  and rarely connects to the principal portability discussion.
- **Source evidence**: `framings.md` §7 Excludes line on F2A → IR1
  automatic conversion mechanic; family-petitioner voice on the
  naturalization-of-petitioner-as-acceleration-event.
- **Trigger**: Asker is in F2A pendency (spouse of LPR) AND the
  petitioning LPR is eligible to naturalize OR is in the
  naturalization process.
- **Failure mode**: Asker doesn't connect the petitioning LPR's
  naturalization to the asker's own AOS timeline; petitioner
  naturalizes; F2A → IR1 conversion happens silently; asker doesn't
  file the I-485 for months because they didn't realize the
  category became immediately current.
- **Recovery move**: For any F2A pendency, treat the petitioning
  LPR's naturalization as a critical-path event on the asker's
  immigration timeline; consult a licensed immigration attorney to
  pre-stage the I-485 filing package so it can be submitted within
  weeks of the petitioner's naturalization-oath.

### 7.5 Marriage during pendency can break F-preference derivative status

- **Statement**: Derivative status in F-preference categories is
  fragile to changes in the derivative's own marital status: an
  unmarried adult child marrying during F1/F2B pendency converts
  the category and resets the PD effectively; the framing's PD-
  portability vocabulary doesn't surface marriage-as-conversion-
  event for derivatives.
- **Source evidence**: `framings.md` §7 cross-reference to §6.3
  on marriage-converts-category; AILA-practitioner voice on the
  F-preference marriage-conversion as a frequent applicant-side
  surprise.
- **Trigger**: Asker is a derivative in an F-preference petition
  AND is considering marriage during pendency.
- **Failure mode**: Asker marries; petition is now in the wrong
  category; PD attaches to the new (slower) category; asker waits
  10+ additional years.
- **Recovery move**: For any F-preference derivative considering
  marriage, treat the marriage timing as immigration-binding;
  consult a licensed immigration attorney on whether the marriage
  should be timed pre- or post-LPR-grant of the principal, and on
  whether any alternative petition pathway preserves more value.

---

## 8. Dependent-status-coupling framing

### 8.1 L-2 grandfathering: pre-2022 holders may still need to convert to L-2S formally

- **Statement**: The framing's "L-2 spouses have automatic work
  authorization" is true only for L-2S category (post-2022 rule);
  pre-rule L-2 holders were grandfathered into the I-765 EAD
  process and may still need to refile to convert to L-2S formally
  to benefit from the no-EAD-required posture.
- **Source evidence**: `framings.md` §8 Excludes line on L-2 vs L-2S
  grandfathering; dual-intent / corporate-immigration voice on the
  category-conversion mechanics.
- **Trigger**: Asker is L-2 spouse with EAD AND is being told "you
  don't need an EAD anymore" without verification of category-
  designation (L-2 vs L-2S) on the most recent I-94.
- **Failure mode**: Asker stops renewing EAD on the assumption it's
  unnecessary; employer's E-Verify rejects the work authorization
  because the I-94 shows L-2 not L-2S; asker is suspended and may
  accrue §245(c) unauthorized-employment exposure.
- **Recovery move**: Verify I-94 category designation (L-2 vs L-2S)
  on each entry; if L-2 (not L-2S), continue EAD renewal AND
  consult a licensed immigration attorney on the conversion path
  to L-2S to gain the no-EAD-required benefit.

### 8.2 Principal's H-1B premium processing doesn't accelerate H-4 EAD

- **Statement**: The framing treats principal-dependent coupling as
  symmetric; in fact, the principal can renew H-1B in 15 days under
  premium processing while the dependent's H-4 EAD sits in a separate
  USCIS queue with 8–18 month lag (2023–24 data). The framing's "in
  lockstep" reflex misses the rate-mismatch that decouples the
  dependent's EAD from the principal's status renewal.
- **Source evidence**: `framings.md` §8 Excludes line on principal-
  dependent rate mismatch; USCIS Ombudsman annual report data on
  H-4 EAD processing-time variance.
- **Trigger**: Asker is H-4 EAD holder AND principal is renewing
  H-1B AND the asker is assuming the H-4 EAD will renew on the same
  timeline.
- **Failure mode**: Principal's H-1B renews fast; asker's H-4 EAD
  is in 12-month queue; asker's EAD expires during the queue;
  employer suspends the asker; family income halved during the gap.
- **Recovery move**: File the H-4 EAD renewal 180 days before
  expiry (the earliest allowed window) regardless of principal's
  renewal timeline; for any H-4 EAD renewal, evaluate the 540-day
  automatic extension applicability; consult a licensed immigration
  attorney about premium-processing availability for I-539 / I-765
  if USCIS has temporarily expanded premium processing.

### 8.3 Divorce ends dependent status with limited grace; VAWA exists for abuse cases

- **Statement**: Divorce / separation breaks principal-dependent
  coupling with limited grace; the dependent must self-petition
  (VAWA in abusive cases) or transition to own status. The framing
  has no native vocabulary for the abusive-relationship case
  (VAWA exception, §204(a)(1)(A)(iii)) where the coupling-mechanic
  is dangerous to the dependent.
- **Source evidence**: `framings.md` §8 Excludes line on VAWA
  carve-out for abusive relationships; AILA-practitioner voice on
  VAWA self-petitioning as the under-promoted path.
- **Trigger**: Asker is H-4 / L-2 / J-2 / F-2 dependent AND
  reports abusive conditions in the principal-dependent
  relationship AND is being told they have no status options
  outside the relationship.
- **Failure mode**: Asker remains in abusive relationship to
  preserve status; abuse escalates; eventual departure costs
  status anyway plus the years of harm.
- **Recovery move**: For any abusive-relationship dependent case,
  immediately consult a licensed immigration attorney with VAWA
  practice experience (specifically — VAWA is its own sub-specialty
  within immigration law) about VAWA self-petition eligibility,
  T-visa and U-visa alternatives, and the timing of safety-planning
  steps relative to status-application timing.

### 8.4 H-4 child aging out has separate logic from principal-dependent coupling

- **Statement**: Children's derivative status follows the principal's
  path but children of dependents (e.g. H-4 child reaching 21) have
  separate aging-out logic from the principal-dependent coupling
  the framing focuses on. The 21-year cliff intervenes regardless of
  principal's status.
- **Source evidence**: `framings.md` §8 Excludes line on H-4 child
  aging-out logic being separate from principal-dependent coupling.
- **Trigger**: Asker has H-4 child approaching age 21 AND is
  reasoning from principal-status-flow-down logic without
  surfacing the 21-year cliff.
- **Failure mode**: H-4 child turns 21; loses derivative status
  immediately (no grace period for H-4 aging out); must pivot to
  F-1 (with university enrollment evidence) or accept departure;
  family is split during the principal's still-pending AOS.
- **Recovery move**: For any H-4 child age 17–21, pre-stage F-1 COS
  (with admission to a SEVIS-certified university) at least 6
  months before the 21st birthday; consult a licensed immigration
  attorney about CSPA-age applicability if the principal's AOS is
  in flight (CSPA may preserve derivative status that the H-4
  aging-out rule would otherwise terminate).

### 8.5 H-4 EAD eligibility tying to AC21 extension creates a layoff cliff for dependents

- **Statement**: H-4 EAD eligibility specifically requires either
  approved I-140 OR AC21 §104(c) 3-year H-1B extension; if the
  principal's I-140 has not been approved at the layoff event, the
  60-day grace doesn't extend H-4 EAD eligibility — the EAD lapses
  with the principal's status, and the dependent loses work
  authorization on day 61 even if the principal pivots to a new
  H-1B sponsor.
- **Source evidence**: `framings.md` §8 Mental model line on H-4
  EAD eligibility tying to I-140 OR AC21 extension; reinforced by
  `domain_knowledge/tech-career/communities/reddit-tech-collective.md`
  Known-blindspot 1 on H-4 EAD-dependent spouses falling off the
  cscareerquestions map.
- **Trigger**: Asker is H-4 EAD holder AND principal's H-1B employer
  is in layoff cycle AND principal's I-140 is pending (not approved).
- **Failure mode**: Principal is laid off; 60-day grace period
  starts; principal pivots to new sponsor; H-4 EAD requires
  *approved* I-140 to continue, which the asker doesn't have; H-4
  EAD lapses; asker stops working; family income halved at the
  worst possible moment.
- **Recovery move**: For any H-4 EAD holder whose principal is
  in a layoff-risk environment AND whose principal's I-140 is not
  yet approved, prioritize expediting the I-140 approval (premium
  processing where available) BEFORE any layoff event; consult a
  licensed immigration attorney on the principal-side I-140
  acceleration AND the H-4-side fallback options (own H-1B cap
  filing, COS to F-1, dependent's own self-petition eligibility
  if criteria met).

---

## 9. Evidentiary-bar framing

### 9.1 USCIS adjudication isn't a steady-state criterion-checker

- **Statement**: The framing treats USCIS adjudication as a reasoned
  application of criteria; in practice RFE rates on EB-1A vary 2–3×
  by service center and by political administration's stance, and
  identical petitions filed in 2017 vs 2020 vs 2023 receive
  materially different scrutiny. "The case is strong" is calibrated
  to a steady-state adjudicator that doesn't exist.
- **Source evidence**: `framings.md` §9 Excludes line on adjudication
  variance by service center and administration; AILA-practitioner
  voice on the 2020 EB-1A RFE spike vs the 2023 partial recovery.
- **Trigger**: Asker is being shown an EB-1A or NIW case-strength
  assessment based on attorney experience from a different
  administration / service-center pair than the current one.
- **Failure mode**: Asker files; receives RFE / denial that pattern-
  matches the current scrutiny regime; the case-strength assessment
  was correct for the prior regime and wrong for the current one.
- **Recovery move**: Require service-center- and administration-
  specific RFE-rate data on the exact petition type before filing;
  size the cash and time budget for at least one RFE response;
  consult a licensed immigration attorney whose practice tracks
  current-administration RFE patterns (not 2017-vintage
  case-strength heuristics).

### 9.2 Template letters of recommendation trigger adjudicator skepticism

- **Statement**: Letters of recommendation are presented as a
  criterion the asker controls; in practice the *circulation
  pattern* of template letters across the immigration-attorney
  community has produced an adjudicator skepticism the framing
  rarely surfaces — a too-polished letter that pattern-matches
  AILA-boilerplate is sometimes weaker than a less-polished
  independent letter.
- **Source evidence**: `framings.md` §9 Excludes line on template-
  letter circulation creating adjudicator skepticism; AILA-
  practitioner voice on the post-2018 "boilerplate letter" RFE
  pattern.
- **Trigger**: Asker is preparing EB-1A or NIW with attorney-
  drafted reference-letter templates AND has not significantly
  customized each letter to the writer's actual voice and
  relationship.
- **Failure mode**: Adjudicator pattern-matches letters as
  attorney-template; weights them lower or RFEs requesting
  evidence of the writer's actual relationship to the asker;
  the time invested in collecting signatures produces minimal
  evidentiary weight.
- **Recovery move**: For each reference letter, the writer
  (not the attorney) should draft the substantive paragraphs in
  their own voice describing the specific original-contribution
  evidence they witnessed; the attorney may format and verify
  but should not draft the substantive content; consult a
  licensed immigration attorney specifically about the
  letter-customization standard for the current adjudication
  environment.

### 9.3 "Comparable evidence" pathway is heavily scrutinized

- **Statement**: "Comparable evidence" is presented as a flexibility
  (you can substitute X for criterion Y); in adjudication, the
  comparable-evidence pathway is heavily scrutinized and the
  framing's optimism on substitution rarely tracks RFE patterns
  — adjudicators often reject substitutions and require the
  numbered criteria be met directly.
- **Source evidence**: `framings.md` §9 Excludes line on comparable-
  evidence over-optimism; AILA-practitioner voice on the
  Kazarian-two-step where comparable-evidence claims are
  systematically downgraded in the final-merits stage.
- **Trigger**: Asker is being told to argue 3 of 10 EB-1A criteria
  via comparable-evidence rather than directly-meeting-the-criterion.
- **Failure mode**: Asker files with 2 directly-met criteria + 1
  comparable-evidence; RFE issues on the comparable-evidence
  criterion; asker doesn't have a fallback because the strategy was
  premised on the substitution succeeding.
- **Recovery move**: Plan to directly meet at least 3 (better: 4–5)
  criteria; treat comparable-evidence as supplementary support
  rather than as a primary criterion-fill; consult a licensed
  immigration attorney about current RFE patterns on comparable-
  evidence specifically for the petition type at the target
  service center.

### 9.4 EB-1A approval doesn't auto-trigger I-485 readiness

- **Statement**: The framing optimizes the *petition* but rarely
  the *post-approval flow*: an EB-1A approval triggers I-485
  filing eligibility, but the asker who hasn't pre-staged medical
  exams, affidavit of support, employer letters, etc. loses 6
  months of priority-date-current window while assembling the
  consequent paperwork.
- **Source evidence**: `framings.md` §9 Excludes line on post-
  approval flow being neglected; MurthyDotCom-style consumer-
  rights voice on the "approval-then-paperwork-rush" pattern.
- **Trigger**: Asker has filed EB-1A AND has not pre-staged the
  I-485 supporting documents (medical exam, photos, financial
  documentation, biographical evidence).
- **Failure mode**: EB-1A approves on a current PD; asker spends
  4 months gathering medical exams, biometric photos, employment
  verification, etc.; PD retrogresses during the gathering; I-485
  filing window closes; asker waits 12+ additional months for
  PD to return current.
- **Recovery move**: Pre-stage I-485 supporting documents in
  parallel with EB-1A filing (medical exam can wait given indefinite
  validity post-late-2024, but biographic documents, employment
  letters, financial evidence should be ready); consult a licensed
  immigration attorney on a sequenced filing-readiness checklist.

### 9.5 EB-1A vs O-1A criterion sets are similar but not identical

- **Statement**: O-1A and EB-1A share criterion-style adjudication
  but differ in the criteria sets (10 vs 8), the "sustained acclaim"
  requirement (EB-1A only), and the intent-to-continue requirement
  (EB-1A only). The framing's "build EB-1A evidence, you can use it
  for O-1 too" reflex doesn't account for criteria-set divergence,
  and an asker who builds toward one may have a weaker case for
  the other.
- **Source evidence**: `framings.md` §9 Mental model line on the
  O-1A 8 / EB-1A 10 criterion divergence; AILA-practitioner voice
  on the cross-petition portfolio-reuse limits.
- **Trigger**: Asker is building an evidence portfolio for one
  category (O-1A or EB-1A) AND assuming the same portfolio works
  for the other.
- **Failure mode**: Asker pivots from O-1A to EB-1A (or vice versa)
  mid-portfolio-build; discovers the new category requires
  criteria the existing portfolio doesn't meet; substantial re-
  work needed; deadline pressure compromises evidence quality.
- **Recovery move**: Before building an evidence portfolio,
  decide explicitly which category is the primary target and
  which (if any) is the secondary target; consult a licensed
  immigration attorney on the portfolio-design tradeoffs between
  O-1A and EB-1A criterion sets and the cross-category reuse
  limits.

---

## 10. Visa-as-employer-leverage framing

### 10.1 "Build visa-independent leverage" is most actionable for askers who already have it

- **Statement**: The framing's "build visa-independent leverage"
  advice (self-petition EB-1A / NIW; cap-exempt optionality;
  spouse's independent status) is most actionable for askers who
  already have the EB-1A portfolio or the cap-exempt opportunity;
  for the modal asker (4 years into H-1B at a BigCo, EB-2 India
  backlog, no publications), the framing names a real problem
  without a practical exit.
- **Source evidence**: `framings.md` §10 Excludes line on the
  framing naming a real problem without a practical exit for
  modal askers.
- **Trigger**: Asker is modal H-1B holder (BigCo employee, no
  EB-1A profile, deep EB-2/3 backlog) AND is being told to "build
  leverage" without a concrete pathway.
- **Failure mode**: Asker spends mental cycles on hypothetical
  EB-1A profiles instead of on the moves that are actually
  available (sponsor-quality optimization, PERM-velocity
  management at current employer, spouse cap-lottery filing);
  the leverage framing produces anxiety without action.
- **Recovery move**: For modal askers, route to the actually-
  available leverage instruments: (1) employer-PERM velocity
  monitoring with explicit escalation rights; (2) spouse's
  independent H-1B cap-filing as a separate principal-petition
  pathway; (3) cap-exempt employer optionality research
  (universities, research nonprofits); consult a licensed
  immigration attorney to evaluate which of these is feasible
  given the asker's specific facts.

### 10.2 The employer's immigration team's loyalty is to the company, not the asker

- **Statement**: The framing treats employer-sponsor relationship
  as transactional; the practical interface is often a long-tenured
  in-house immigration attorney whose loyalty is to the company,
  not the asker. The asker's leverage in that relationship is even
  narrower than the headline employer relationship, and
  attorney-client privilege does not run from the in-house
  attorney to the asker.
- **Source evidence**: `framings.md` §10 Excludes line on employer's
  immigration team being the practical interface with company
  loyalty; AILA-practitioner voice on the in-house-vs-outside
  attorney engagement distinction.
- **Trigger**: Asker is sharing case-strategy or facts with the
  employer's in-house immigration attorney AND believes those
  communications are protected.
- **Failure mode**: Asker discloses strategic position
  (considering self-petition; layoff vulnerability; AC21 plans);
  in-house attorney shares with HR / management; asker's
  negotiating position is now known to the counterparty.
- **Recovery move**: Treat communications with the employer's
  in-house immigration attorney as communications with the
  employer; for any strategic decision (self-petition, AC21
  portability planning, layoff response), retain a separate
  licensed immigration attorney whose attorney-client privilege
  runs to the asker, not to the employer.

### 10.3 Dependent-status asymmetry widens employer leverage further

- **Statement**: The framing's individual-focused vocabulary
  glides over that an asker whose spouse and children depend on
  the H-1B principal's continued employment for H-4 status
  experiences leverage asymmetry the headline-employer-relationship
  vocabulary doesn't capture. The employer effectively has
  leverage over the asker's entire family's status, not only the
  asker's.
- **Source evidence**: `framings.md` §10 Excludes line on
  dependent-status leverage asymmetry being underweighted;
  `domain_knowledge/tech-career/communities/founder-engineer-bloggers.md`
  Known-blindspot 1 explicitly naming the "H-1B 60-day grace
  period after termination" and the "I-140-pending portability
  rules" as load-bearing constraints the standard
  negotiation-advice framework ignores.
- **Trigger**: Asker has H-4 dependents AND is reasoning about
  comp / layoff response / sponsor-change with employer-leverage
  vocabulary calibrated to a single-person asker.
- **Failure mode**: Asker accepts a worse comp / role outcome
  under the framing's individual-leverage calculus; the actual
  leverage gap is wider because the family-status exposure
  isn't priced; future negotiations are anchored to the
  worse outcome.
- **Recovery move**: Compute the family-status risk explicitly
  (H-4 EAD lapse cost, H-4 children's status, spouse's
  employability mid-renewal) as an additional employer-leverage
  factor; consult a licensed immigration attorney on whether
  the asker's family can pre-stage independent status pathways
  (spouse's own H-1B cap filing, dependent's COS-eligible
  status alternatives) to reduce the leverage asymmetry.

### 10.4 RFE-then-denial restarts the dependency cycle while consuming the spent cash

- **Statement**: The "self-petition independence" framing prices
  attorney fees ($8–15k for EB-1A, $3–5k for NIW) and applicant
  evidence-curation time as one-time costs; the framing skips that
  USCIS rejection or RFE-then-denial restarts the dependency cycle
  while consuming the cash and time already spent.
- **Source evidence**: `framings.md` §10 Excludes line on RFE-
  then-denial restarting dependency.
- **Trigger**: Asker is being sold EB-1A / NIW as a clean exit
  from employer dependency without RFE / denial probability
  surfaced.
- **Failure mode**: Asker self-petitions; denial issues; cash
  reserves depleted; back to employer-sponsored dependency with
  *less* leverage than before because the cash buffer is gone
  and the denied petition is now a record.
- **Recovery move**: Before self-petitioning, model the
  RFE-and-denial scenario (probability × downside cost) and
  size the cash reserve for two attempts; consult a licensed
  immigration attorney on the denial-record consequence for
  future filings and on whether parallel employer-sponsored
  filings should remain active throughout the self-petition.

### 10.5 Cap-exempt employer optionality is geographically constrained

- **Statement**: The framing names "cap-exempt employer
  optionality" (universities, affiliated nonprofits, qualifying
  research institutions) as a leverage move; the optionality is
  geographically constrained — cap-exempt employers cluster around
  major university towns and research-institution metros, and an
  asker rooted in a city without that infrastructure can't
  realistically exercise the option.
- **Source evidence**: `framings.md` §10 Mental model on cap-exempt
  optionality; reinforced by `framings.md` §12 Mental model on
  employer-side optionality being location-dependent.
- **Trigger**: Asker is being advised to "look at cap-exempt
  employers" while rooted in a metro without major university or
  research-institution infrastructure (mortgage, spouse's job,
  children's school).
- **Failure mode**: Asker pursues cap-exempt search; finds no
  local options; the leverage move requires relocation that the
  asker's family situation doesn't tolerate; the framing's
  optionality was theoretical.
- **Recovery move**: Before treating cap-exempt as a real
  optionality, map the asker's commutable cap-exempt employer
  list (USCIS publishes employer-petition data; AILA-practitioner
  forums maintain working lists); if the list is empty, the
  leverage move is unavailable and the asker should consult a
  licensed immigration attorney on alternative leverage
  instruments.

---

## 11. Marriage-good-faith framing

### 11.1 Non-cohabiting bona fide marriages don't fit the standard evidence pattern

- **Statement**: The framing's "build evidence as the marriage
  builds" advice assumes the marriage is structurally cohabiting
  and US-resident from inception; for couples whose relationship
  matures non-linearly (long-distance, separate careers, separate
  residences for non-immigration reasons), the evidentiary baseline
  the framing recommends is a poor fit despite the marriage being
  entirely bona fide.
- **Source evidence**: `framings.md` §11 Excludes line on non-
  linear marriages having a poor fit to the standard evidence
  pattern.
- **Trigger**: Asker is in a marriage-based filing AND the
  couple lives separately (different cities for work; separate
  residences during medical residency / military deployment /
  caregiving for parent) AND is being told the case is weak on
  cohabitation evidence.
- **Failure mode**: Asker assembles cohabitation evidence that
  doesn't exist; substitutes weak or misleading documentation
  (lease signed for appearance, joint accounts opened only post-
  filing); USCIS adjudicator reads the inconsistency as bad-faith
  signal even though the marriage is bona fide.
- **Recovery move**: For non-cohabiting bona fide marriages,
  build evidence patterns that match the actual relationship
  (frequent travel records, communication archives, joint
  decision-making documentation, joint financial commitments
  even without shared address); consult a licensed immigration
  attorney with experience in non-traditional-relationship
  marriage cases (specifically — this is a sub-specialty
  within marriage-based practice).

### 11.2 LGBTQ+ couples face a different evidentiary terrain

- **Statement**: LGBTQ+ couples with prior partnerships in
  jurisdictions where same-sex marriage was not recognized face
  a different evidentiary terrain (prior unrecognized cohabitation,
  foreign civil-union records of varying authenticity) the framing's
  US-centered defaults don't address well.
- **Source evidence**: `framings.md` §11 Excludes line on LGBTQ+
  couples facing different evidentiary terrain; AILA-practitioner
  voice on the post-Obergefell I-130 patterns with retroactive
  partnership evidence.
- **Trigger**: Asker is in an LGBTQ+ marriage-based filing AND
  the couple's relationship pre-dates legal recognition in the
  jurisdiction(s) where they lived.
- **Failure mode**: Asker assembles evidence under the framing's
  standard pattern; USCIS adjudicator unfamiliar with the
  retroactive-recognition context reads the timeline as suspicious;
  RFE on bona fides; case is delayed or denied.
- **Recovery move**: For LGBTQ+ marriage-based filings with
  pre-recognition history, prepare a contextual narrative
  explaining the jurisdiction-specific recognition history with
  supporting evidence (timeline of jurisdictional recognition
  changes; documentation of the relationship through the pre-
  recognition period); consult a licensed immigration attorney
  with documented LGBTQ+ marriage-case experience.

### 11.3 Divorce during conditional PR has three distinct evidence regimes

- **Statement**: The framing protects against fraud findings but
  doesn't address divorce-during-conditional-PR, where the foreign
  spouse must show either (a) marriage was bona fide at inception
  but ended via divorce, (b) hardship to a USC child, or (c) abuse
  — three distinct evidence regimes the "build the evidence"
  advice doesn't differentiate.
- **Source evidence**: `framings.md` §11 Excludes line on divorce-
  during-conditional-PR having three distinct evidence regimes.
- **Trigger**: Asker is in conditional PR (post-marriage-based AOS
  with 2-year conditional grant) AND the marriage is ending.
- **Failure mode**: Asker files I-751 waiver under the wrong
  category (divorce-waiver when abuse-waiver fits, or vice versa);
  USCIS rejects the waiver; conditional PR terminates and asker
  enters removal proceedings.
- **Recovery move**: Before filing any I-751 waiver after
  marriage breakdown, consult a licensed immigration attorney on
  which of the three waiver categories applies to the specific
  facts; the attorney should also evaluate whether multiple
  waiver categories can be filed in the alternative.

### 11.4 The I-864 affidavit of support is a 10-year obligation surviving divorce

- **Statement**: The I-864 affidavit of support is a 10-year
  obligation surviving divorce; the framing presents it as a
  filing checkbox when it is a financial commitment with case-
  law-enforced creditor rights against the US-citizen sponsor.
  The sponsor's exposure (and the foreign spouse's potential
  enforcement leverage) is not understood at filing time.
- **Source evidence**: `framings.md` §11 Excludes line on I-864
  as a 10-year obligation; AILA-practitioner voice and
  divorce-bar voice on Cheshire / Toure-line I-864
  enforcement case law.
- **Trigger**: Asker is the petitioning USC sponsor in a marriage-
  based filing AND is treating the I-864 as procedural without
  surfacing its enforceable creditor character.
- **Failure mode**: Marriage ends; foreign spouse files
  enforcement action under I-864 case law; sponsor is liable
  for income support to the federal poverty level for the
  foreign spouse's remaining period until naturalization, 40
  qualifying quarters of work, or other terminating event.
- **Recovery move**: Before signing an I-864, consult a licensed
  immigration attorney *and* a family-law attorney about the
  10-year sponsor-obligation in the asker's state's divorce-law
  regime; understand whether prenuptial agreements can address
  it (case law splits) and what the sponsor's actual exposure
  is on a worst-case marriage-end timeline.

### 11.5 Stokes interview is a fraud-unit referral path, not a standard step

- **Statement**: The Stokes interview (separate interrogations
  of spouses to test marriage bona fides) is presented as a
  potential step in the I-130 / I-485 process; in practice it
  is a fraud-unit referral path that triggers when an
  adjudicator perceives inconsistency in the initial interview,
  and the threshold for that referral varies wildly by field
  office. The framing's "if Stokes happens, just answer the
  questions" reflex misses that the referral itself signals
  the case is on a high-scrutiny track.
- **Source evidence**: `framings.md` §11 Mental model on Stokes
  interview and fraud-unit referral; AILA-practitioner voice on
  field-office Stokes-referral threshold variance.
- **Trigger**: Asker has received notice of a Stokes interview
  or any field-office secondary interview AND is treating it as
  routine.
- **Failure mode**: Asker enters Stokes without preparation;
  inconsistency in answers (timing of meeting, family details,
  daily routine) is recorded as fraud signal; case is referred
  to fraud unit; I-751 / I-485 is denied with fraud finding
  that cascades to every future immigration benefit.
- **Recovery move**: On any Stokes-interview notice, immediately
  consult a licensed immigration attorney before the interview
  date; the attorney should attend the interview (or the
  attorney's representative) and the asker and spouse should
  prepare answers to common Stokes question patterns
  separately to identify and resolve genuine memory
  inconsistencies in advance.

---

## 12. STEM-OPT-lottery-arbitrage framing

### 12.1 The 2024 H-1B beneficiary-centric rule changed multi-attempt arithmetic

- **Statement**: The framing's lottery-arithmetic optimism (3
  attempts ≈ 70%+ aggregate odds) assumed pre-2024 single-
  registration mechanics; the 2024 USCIS beneficiary-centric rule
  capped multi-registrations and changed the per-cycle math
  materially. Framings calibrated to pre-2024 attempt-rates
  over-predict cumulative success.
- **Source evidence**: `framings.md` §12 Excludes line on the
  2024 beneficiary-centric rule changing per-cycle math; USCIS
  Ombudsman annual reports on the 2024 registration cycle data.
- **Trigger**: Asker is being shown a 3-attempt cumulative-odds
  calculation calibrated to pre-2024 multi-registration data
  (often from blog posts dated 2020–2023).
- **Failure mode**: Asker plans a 3-year STEM-OPT runway expecting
  ≥70% aggregate H-1B success; actual cumulative success rate
  under the new rule is lower; STEM-OPT exhausts without H-1B
  selection; asker must depart or pivot to harder paths (O-1,
  EB-1A, cap-exempt move).
- **Recovery move**: Use post-2024 cumulative-success rate data
  (USCIS publishes annual cap-cycle outcomes) for runway
  planning, not pre-2024 multi-registration estimates; consult
  a licensed immigration attorney on contingency options
  (O-1, EB-1A, cap-exempt routes) before STEM-OPT exhaustion to
  preserve flexibility.

### 12.2 STEM CIP-code verification matters at degree-application time

- **Statement**: The framing assumes STEM-eligible degree confers
  24-month extension uniformly; in practice the degree must be
  from a SEVIS-certified institution AND on the DHS STEM-
  designated CIP code list (currently 400+ codes), and some
  adjacent degrees (data analytics, technology management) sit
  just outside the list. The framing's "STEM means 24 months"
  glides past CIP-code verification.
- **Source evidence**: `framings.md` §12 Excludes line on CIP-code
  verification; F-1 student-forum voice on the data-analytics-vs-
  data-science CIP-code distinction.
- **Trigger**: Asker is choosing a graduate program AND is
  assuming the STEM extension applies AND is selecting a program
  in the analytics / technology-management / interdisciplinary
  edge zone.
- **Failure mode**: Asker enrolls; completes degree; applies for
  24-month STEM extension; DSO finds the program's CIP code is
  not on the DHS STEM list; extension denied; asker has 12-month
  OPT only and one fewer H-1B cap attempt than planned.
- **Recovery move**: Before enrolling in a graduate program,
  verify the specific CIP code against the current DHS STEM-
  designated list (published by ICE / SEVP); for any edge-case
  program, consult a licensed immigration attorney about whether
  the program's CIP code qualifies and whether an alternative
  similar program qualifies cleanly.

### 12.3 H-1B-filing track record is hard for the asker to verify at offer time

- **Statement**: "Pick employers based on H-1B-filing track
  record" is the right instruction but requires the asker to have
  visibility into employer H-1B filing data the asker rarely has
  at offer-acceptance time. The framing's optimization is correct
  in direction but practically constrained by information
  asymmetry.
- **Source evidence**: `framings.md` §12 Excludes line on H-1B-
  filing data being practically inaccessible to the asker; AILA-
  practitioner voice on the employer-side H-1B-filing-quality
  variance.
- **Trigger**: Asker has a job offer AND is being told to
  "evaluate H-1B filing track record" without a concrete data
  source named.
- **Failure mode**: Asker accepts the offer; employer turns out
  to have poor H-1B filing-quality track record (late filings,
  inadequate LCAs, lottery-cycle miss); asker's H-1B is not
  filed on time; STEM-OPT lottery attempt is lost.
- **Recovery move**: Before accepting an offer, request from
  the prospective employer (a) prior 3-year H-1B filing volume
  and approval rate, (b) named in-house counsel or external
  immigration firm, (c) commitment on cycle-N H-1B filing
  timing; if the data isn't available or the employer won't
  commit, consult a licensed immigration attorney about whether
  the offer's H-1B filing path is reliable enough to accept.

### 12.4 OPT unemployment-tolerance clock-start is interpreted variably by DSOs

- **Statement**: The 90 / 150-day unemployment tolerance on OPT /
  STEM-OPT is presented as a known constraint; the *clock-start*
  moment (last day of paid employment vs last day of authorized
  employment vs SEVIS-update lag) is interpreted variably by DSOs.
  The framing's reliance on the day-count vocabulary masks the
  ambiguity.
- **Source evidence**: `framings.md` §12 Excludes line on clock-
  start moment being interpreted variably.
- **Trigger**: Asker is OPT / STEM-OPT holder AND has recently
  separated from employer AND is being told they have 90 / 150
  days of tolerance without DSO-specific clock-start
  confirmation.
- **Failure mode**: Asker counts 90 days from last paycheck; DSO
  counts 90 days from a different event (notification of
  termination, SEVIS-update, last actual work day); SEVIS shows
  asker out of compliance; F-1 status is terminated.
- **Recovery move**: On any OPT employment separation, contact
  the DSO immediately to confirm (a) the asker's clock-start
  moment per the specific DSO's interpretation and (b) the
  SEVIS-update timing; consult a licensed immigration attorney
  if the DSO's interpretation seems inconsistent with USCIS or
  ICE published guidance or if the asker's day-count is close
  to the tolerance limit.

### 12.5 STEM-OPT employer must be E-Verify AND submit I-983 reports on schedule

- **Statement**: STEM-OPT extension requires the employer to be
  E-Verify enrolled AND to submit I-983 training plans / reports
  on the published schedule; the framing focuses on E-Verify
  status at offer-acceptance but rarely on I-983 reporting
  compliance, which can lapse silently and put STEM-OPT
  authorization at risk.
- **Source evidence**: `framings.md` §12 Mental model on the
  E-Verify requirement; AILA-practitioner voice on the I-983
  reporting compliance as the under-monitored ongoing
  obligation.
- **Trigger**: Asker is on STEM-OPT AND the employer is small
  (no in-house immigration team) AND I-983 reporting compliance
  is not actively monitored.
- **Failure mode**: Employer misses I-983 reporting deadline; SEVP
  terminates the STEM extension; asker has 60 days to depart or
  re-enroll; cap-gap and H-1B planning are disrupted.
- **Recovery move**: For STEM-OPT at any small employer, take
  personal responsibility for tracking I-983 reporting deadlines
  (6-month evaluation, 12-month evaluation, employer-update reports)
  and confirm with the employer's HR each cycle; consult a
  licensed immigration attorney if any deadline approaches and
  the employer hasn't confirmed submission.

---

## 13. Consular-vs-COS-discretion framing

### 13.1 Consulate-specific refusal-rate patterns matter; "consular discretion" is too generic

- **Statement**: "Consular discretion is broad" is true at the
  policy level but the framing glides over that *specific
  consulates* have documented refusal-rate patterns by visa
  category — Chennai's H-1B refusal rate vs Mumbai's, Manila's
  vs Bangkok's, Lagos's vs Accra's — that should change the
  CP-or-COS calculus. The framing's generic "consular discretion"
  doesn't capture granular consulate variance.
- **Source evidence**: `framings.md` §13 Excludes line on
  consulate-specific refusal-rate variance; DOS-watcher voice
  on consulate-by-consulate refusal-pattern data (DOS publishes
  this annually).
- **Trigger**: Asker is being advised on CP-vs-COS with the
  consulate identified but no consulate-specific refusal-rate
  data presented.
- **Failure mode**: Asker chooses CP at a high-refusal-rate
  consulate based on general "CP is cleaner" advice; receives
  214(b) refusal; cannot re-enter US until a different consulate
  approves; asker's life is disrupted for months.
- **Recovery move**: Before any CP decision, pull the consulate-
  specific refusal-rate data for the exact visa category from
  DOS published statistics; if the consulate's refusal rate is
  materially above the global mean for that category, consult
  a licensed immigration attorney about third-country processing
  options or COS-instead-of-CP.

### 13.2 §214(b) findings outside the 90-day window are real

- **Statement**: The 90-day preconceived-intent rule is presented
  as a hard line; in practice it's a FAM guideline and §214(b)
  refusal can apply *outside* the 90-day window when other facts
  support preconceived intent. The framing's "wait until day 91"
  advice is structurally weak — the asker who waits 91 days but
  has documentary evidence of pre-entry intent gets the refusal
  anyway.
- **Source evidence**: `framings.md` §13 Excludes line on §214(b)
  applying outside the 90-day window with other facts.
- **Trigger**: Asker is timing a COS filing to day 91 of
  B-visitor stay AND has documentary evidence of pre-entry
  intent (LinkedIn post, signed lease, school admission letter
  dated pre-arrival).
- **Failure mode**: Asker files on day 91; COS denied for
  preconceived intent based on the documentary evidence; asker
  must depart; future visa applications carry the refusal record.
- **Recovery move**: Audit pre-entry documentary record before
  any COS from B-visitor status; if any pre-entry-intent evidence
  exists, the day-91 heuristic is insufficient and the asker
  should consult a licensed immigration attorney on whether COS
  is viable or whether departing and applying CP from outside is
  the lower-risk path.

### 13.3 Administrative processing (§221(g)) can strand CP applicants for months

- **Statement**: "CP after a denial is harder" understates the
  *administrative processing* (Section 221(g)) regime where a
  consular officer refers a case for security / FBI / interagency
  clearance with no fixed timeline; CP applicants in
  administrative processing can be stuck abroad for 3–18 months
  and the framing rarely names AP as a distinct risk category.
- **Source evidence**: `framings.md` §13 Excludes line on §221(g)
  administrative processing being a distinct risk category;
  DOS-watcher voice on administrative-processing pattern data.
- **Trigger**: Asker is considering CP AND has any factor that
  could trigger administrative processing (technology-export
  background, scientific-research field, born / educated in a
  country subject to security review, prior visa history
  inconsistency).
- **Failure mode**: Asker departs for CP; consular interview
  results in 221(g) refusal pending administrative processing;
  asker is stranded abroad for unknown duration; US job /
  housing / family situation collapses during the wait.
- **Recovery move**: Before any CP decision, evaluate
  administrative-processing risk profile with a licensed
  immigration attorney; for high-risk profiles, CP may not be
  worth the stranding risk even with consulate-discretion
  advantages, and COS or alternative status paths may be
  preferable.

### 13.4 Re-entry after CP triggers CBP inspection, which is a separate authority

- **Statement**: The framing's COS-vs-CP binary skips the
  re-entry-after-CP risk: even an approved consular stamp
  triggers a CBP inspection at port of entry where any factor
  (DS-160 inconsistency, social-media review, prior I-94
  history) can result in re-refusal at the border. CBP and DOS
  are separate authorities and the framing's "consular approval
  is the answer" is one step short.
- **Source evidence**: `framings.md` §13 Excludes line on
  re-entry-after-CP CBP-inspection risk.
- **Trigger**: Asker has approved consular stamp AND is
  preparing to re-enter US AND has not pre-verified DS-160
  consistency with the asker's actual social-media presence and
  I-94 history.
- **Failure mode**: Asker arrives at port of entry; CBP officer
  finds inconsistency (DS-160 says "no prior visa refusals" but
  CBP records show one; or social-media post inconsistent with
  visa-category claim); asker is refused entry; consular
  approval is now contested.
- **Recovery move**: Before re-entry on a fresh consular stamp,
  audit DS-160 answers against actual visa / I-94 / social-media
  history; for any inconsistency, consult a licensed immigration
  attorney about whether to delay travel and reconcile records
  before attempting re-entry.

### 13.5 COS pendency bridge between B-visa expiry and decision is procedurally fragile

- **Statement**: An asker who files COS while in valid B-1/B-2
  status, then the B-1/B-2 I-94 expires before USCIS decides
  the COS, is in pendency-bridge status — the asker is not yet
  COS-granted but is also not out-of-status (the timely-filed
  COS preserves status during USCIS review). The framing's "you
  filed in time, you're fine" reflex misses that a denial after
  the original I-94 expired puts the asker immediately out-of-
  status with no grace period.
- **Source evidence**: `framings.md` §13 cross-reference to §1
  on COS-pendency-bridge mechanics; AILA-practitioner voice on
  the post-I-94-expiry COS-denial scenario.
- **Trigger**: Asker has filed COS AND original I-94 has expired
  during USCIS review AND COS hasn't been adjudicated yet.
- **Failure mode**: COS denial issues 2 months after I-94 expiry;
  asker is immediately out-of-status with no grace period;
  unlawful-presence clock starts; asker must depart immediately
  to avoid §212(a)(9)(B) bar.
- **Recovery move**: For any COS filing where the original I-94
  may expire during pendency, pre-plan the denial-scenario
  departure path (booking flexibility, document portability)
  before the I-94 expiry; consult a licensed immigration attorney
  about whether to file a parallel I-539 extension of the
  underlying B-status to preserve a fallback if COS is denied.

---

## 14. Pro-se / consumer-rights framing

### 14.1 USCIS form-edition turnover makes pro-se filing a procedural minefield

- **Statement**: The framing's pro-se confidence is calibrated to a
  USCIS-of-record that issues clear instructions and consistent
  adjudication; current USCIS form-edition turnover (multiple
  editions per fiscal year for high-volume forms; rejection of
  wrong-edition filings without refund of fee) makes pro-se
  filing a procedural minefield the framing under-weights.
- **Source evidence**: `framings.md` §14 Excludes line on form-
  edition turnover; USCIS Ombudsman annual report data on
  form-edition rejection rates.
- **Trigger**: Asker is filing pro-se AND is using a form edition
  downloaded > 90 days ago OR is following instructions from a
  community-forum post > 12 months old.
- **Failure mode**: Asker files wrong-edition form; USCIS rejects
  without refund; filing-date is lost (priority date impact, COS
  bridge impact, EAD renewal gap); asker has to re-file with
  new fee and lose months.
- **Recovery move**: For every pro-se filing, download the form
  from USCIS.gov *on the day of filing* and verify the edition
  date matches USCIS's current-edition announcement; for any
  high-stakes filing (I-485, I-130, I-140), consult a licensed
  immigration attorney for form-edition verification before
  submitting.

### 14.2 The procedural/substantive boundary is itself a judgment call

- **Statement**: "Substantive defects need representation" is
  correct but the boundary between procedural and substantive is
  itself a judgment call; an asker pro-se on I-485 who answers a
  public-charge question incorrectly may not recognize the answer
  as substantive until the RFE arrives. The framing's decision
  rule has a self-referential gap.
- **Source evidence**: `framings.md` §14 Excludes line on the
  procedural-substantive boundary being a judgment call.
- **Trigger**: Asker is pro-se on I-485 or I-130 AND is making
  judgment calls on questions involving public-charge, criminal-
  history disclosure, prior-visa-history reconciliation, or
  marriage-bona-fides language.
- **Failure mode**: Asker answers a substantive question pro-se;
  RFE issues; asker now needs to respond with attorney help on
  short deadline; cost is higher than would have been pre-filing.
- **Recovery move**: Before filing pro-se on I-485 or I-130,
  schedule a one-hour pre-filing review with a licensed
  immigration attorney to identify any substantive judgment-call
  questions in the asker's specific filing; the cost is modest
  ($300–800) compared to the cost of RFE response after a
  substantive mistake.

### 14.3 Cost asymmetry: attorney fees are small relative to removal-recovery cost

- **Statement**: Cost asymmetry: $10k of attorney fees is large
  in the moment but small relative to the cost of a removal-
  proceedings recovery; the framing's "save the attorney for
  the hard cases" can route the asker into a hard case they
  don't recognize as such. The pro-se confidence inverts the
  cost-benefit at the high-consequence tail.
- **Source evidence**: `framings.md` §14 Excludes line on
  cost-asymmetry vs removal-recovery cost; AILA-practitioner
  voice on removal-defense fees (typically $25k–$100k+ for
  contested cases).
- **Trigger**: Asker is being told to file pro-se on a
  high-consequence form (I-485 with any complicating factor,
  I-130 with prior unlawful presence, I-751 with marriage
  breakdown) on cost-saving grounds.
- **Failure mode**: Pro-se filing produces denial → NTA →
  removal proceedings; asker spends $25k–$100k on removal
  defense instead of the $5k–$15k that would have prevented
  the issue at filing time.
- **Recovery move**: For any high-consequence form with any
  complicating factor in the asker's history, the
  cost-benefit favors attorney engagement at filing; consult
  a licensed immigration attorney for at least a pre-filing
  case-assessment before pro-se filing.

### 14.4 Modular engagement modes exist between full retainer and pro-se

- **Statement**: The framing prices attorney representation as
  binary (have one / don't); in practice modular engagement
  (one-hour review of a pro-se draft, RFE-response-only
  retainer, post-filing consultation) is available and the
  framing rarely distinguishes engagement modes. The asker who
  thinks "I can't afford a full retainer" forgoes the modular
  options that would address most of their risk for 10–20% of
  the full-retainer cost.
- **Source evidence**: `framings.md` §14 Excludes line on
  modular engagement modes being available; AILA-practitioner
  voice on the unbundled / limited-scope representation as the
  growth-area of immigration practice.
- **Trigger**: Asker has decided against attorney engagement on
  cost grounds AND has not evaluated unbundled / limited-scope
  options.
- **Failure mode**: Asker proceeds fully pro-se to avoid the
  $5–15k full retainer; misses a $500 one-hour review that
  would have caught a substantive issue; ends up with RFE
  costing more than the original review would have.
- **Recovery move**: For any pro-se filing decision, explicitly
  evaluate the modular-engagement options: one-hour pre-filing
  review, RFE-response-only retainer, interview-preparation
  retainer; consult a licensed immigration attorney about
  which engagement mode fits the asker's risk profile and
  budget.

### 14.5 Pro-se reading of USCIS Policy Manual misses unpublished sub-regulatory guidance

- **Statement**: The framing's "read the regulation and the
  Policy Manual" advice misses that USCIS adjudicators also
  follow unpublished sub-regulatory guidance — adjudicator
  training memos, NSC / TSC internal practice memos, FOIA-
  released guidance — that the pro-se asker can't access. The
  Policy Manual is necessary but not sufficient for predicting
  adjudication outcomes.
- **Source evidence**: `framings.md` §14 Mental model line on
  Policy Manual / regulation as pro-se's primary resources;
  AILA-practitioner voice on the FOIA-released-memo corpus that
  attorneys reference but pro-se filers don't access.
- **Trigger**: Asker is pro-se on a complex filing (I-140 self-
  petition, I-751 waiver, complex AOS with prior status gaps)
  AND is relying on Policy Manual reading as the sufficient
  preparation.
- **Failure mode**: Asker's filing aligns with the Policy Manual
  reading; adjudicator applies an internal-memo standard the
  asker didn't know existed; RFE / denial; asker has to
  reverse-engineer the adjudicator's standard from the
  RFE wording.
- **Recovery move**: For complex pro-se filings, at minimum
  engage a licensed immigration attorney for a one-hour
  pre-filing review *specifically* to identify sub-regulatory
  guidance the asker's Policy-Manual-only reading misses;
  this is one of the highest-leverage modular engagements
  available.

---

## Cross-framing tensions

These call out where blindspots in one framing are the *recovery move*
of another, mirroring the structure in
[`framings.md` "Cross-framing tensions"](./framings.md). The pairings
are useful for the Triage / Risk Officer when the asker is clearly
inside one framing — the contrarian framing's blindspot list is often
the right intervention.

- **§1 Status-continuity ↔ §2 Route-optimality**. F1's reflex is
  "never let status lapse"; F2's reflex is "tolerate temporary status
  fragility for structural route gain." §1.5 (strategic short
  out-of-status is rarely right but sometimes only call) and §2.1
  (route-velocity buries family-cost) are the cross-framing tensions:
  surface §2.5 (self-petition independence presumes success) when
  the asker is over-confident in route-velocity, and surface §1.3
  (245(k) under-use) when the asker is over-cautious on status.

- **§1 Status-continuity ↔ §13 Consular-vs-COS-discretion**. F1's
  reflex is "don't leave the country during a pending filing"; F13's
  reflex is "CP is the cleaner path for clean records." §13.2
  (preconceived-intent applies outside 90-day window) and §13.3
  (administrative processing) are the F13 blindspots that should
  surface when F13 is dominant; §1.1 (out-of-status vs
  unlawful-presence regime distinction) should surface when F1 is
  pushing rash departure. The COS-pendency-bridge case (§13.5) is
  the synthesis: status-continuity logic needs to hold during the
  bridge AND consular alternatives need to be pre-planned in case
  of denial.

- **§9 Evidentiary-bar ↔ §10 Visa-as-employer-leverage**. F9 reads
  the EB-1A petition record as a procedural-strength question; F10
  reads the same record as a leverage-instrument question. §9.4
  (post-approval flow neglected) and §10.4 (RFE-then-denial restarts
  dependency) are the cross-framing intersection: the same petition
  is procedural-pass-or-fail under F9 and leverage-on-or-off under
  F10. The asker over-anchored on F10's "build leverage" framing
  needs F9.4 (post-approval-flow gap) surfaced; the asker over-
  anchored on F9's "strong case will succeed" framing needs F10.4
  (denial restarts dependency) surfaced.

- **§5 AC21-portability ↔ §10 Visa-as-employer-leverage**. F5 prices
  the AC21 port as a category-velocity preservation move; F10 prices
  it as a leverage-rebalance with the current employer. §5.4 (human
  portability ≠ legal portability) and §10.3 (dependent-status
  asymmetry widens leverage gap) are the cross-framing tensions:
  the asker who reasons purely from F5's SOC-code mechanics misses
  F10's family-status-leverage dimension; the asker who reasons
  purely from F10's leverage-instrument framing misses F5's
  procedural-cooperation-failure modes at the new employer.

- **§6 CSPA-and-family-clock ↔ §11 Marriage-good-faith**. F6's reflex
  is to optimize for CSPA-age preservation via filing-timing; F11's
  reflex is to optimize for marriage-bona-fides evidence-density
  via marriage-timing. §6.3 (child's marriage converts category) and
  §11.3 (divorce-during-conditional-PR three regimes) are the
  cross-framing tensions: marriage decisions cascade through both
  framings, and the asker reasoning from one needs the other's
  blindspot list surfaced. Family decisions in immigration are
  rarely uni-framing.

- **§14 Pro-se / consumer-rights ↔ §9 Evidentiary-bar, §10 Visa-as-
  employer-leverage, §11 Marriage-good-faith**. F14's pro-se
  confidence clashes with F9 (EB-1A pro-se filings rarely meet the
  comparable-evidence pattern adjudicators expect), with F10 (modular
  engagement is the leverage-preserving compromise the framing
  rarely names), and with F11 (Stokes-interview preparation is a
  classic case where pro-se under-prepares for what the framing
  treats as routine). §14.3 (removal-recovery cost asymmetry) and
  §14.5 (sub-regulatory guidance) are the F14 blindspots that
  invert the pro-se cost-benefit at the high-consequence tail.

## Maturity note

This file is `planned` maturity per
[`_meta_ontology.md` §2](../_meta_ontology.md) (the immigration domain
is `planned`, not `in-migration` like tech-career). Source-evidence
lines below currently anchor to:

- `framings.md` Excludes lines (load-bearing — the framing-level
  Excludes were authored specifically to seed Layer 3, per the
  Notes-for-downstream-layers section of `framings.md`).
- V1 community-profile bullets that touched immigration topics from
  tech-career adjacency (`domain_knowledge/tech-career/communities/
  founder-engineer-bloggers.md` Known-blindspot 1 on visa-status
  mechanics; `domain_knowledge/tech-career/communities/reddit-tech-
  collective.md` Known-blindspot 1 on demographic-scope exclusion of
  visa / caregiving / dual-income constraints; `domain_knowledge/
  tech-career/communities/long-form-references.md` on
  multi-specialty fact patterns; `domain_knowledge/tech-career/
  communities/hn-collective.md` on layoff-time immigration-attorney
  unavailability).
- Conceptual references to the immigration-specific community classes
  named in `framings.md` voice-anchors (immigration-attorney blogs,
  AILA practitioner forums, MurthyDotCom-style consumer-rights voice,
  USCIS Ombudsman annual reports, r/immigration / trackitt forums,
  Boundless / Cyrus D. Mehta blog network, family-petitioner /
  research-track-scientist / DOS-watcher voices).

When `domain_knowledge/immigration/sources.yaml` is authored and
`domain_knowledge/immigration/communities/*.md` community profiles
land, source-evidence lines should be tightened to specific source-view
ids. Until then, this file's grounding is the framings-Excludes seed
plus the immigration-adjacent V1 community-profile content.

**Date-stamp risk**: anchor numbers below carry the date-stamp risk
inherited from the underlying USCIS / DOS policy corpus. Entries to
re-check before relying on for an active decision:

- §1.1, §1.3, §1.4 — §245(c), §245(i), §245(k) eligibility rules
  (statutory; relatively stable but the 245(i) sunset date and any
  legislative revisions need re-check).
- §1.2 — 540-day automatic EAD extension applicability (USCIS rule
  extended through 2025; check current renewal).
- §3.2 — I-693 indefinite-validity rule (late-2024 USCIS update;
  check whether this has been modified or rescinded).
- §6.2 — Post-2023 USCIS policy shift on CSPA sought-to-acquire
  trigger (FAD-current → DFF-current); check whether subsequent
  litigation or USCIS update has changed the operative reading.
- §8.1 — L-2S automatic-work-authorization rule (post-2022;
  check current).
- §12.1 — 2024 H-1B beneficiary-centric registration rule
  (USCIS rule effective FY2025 H-1B cap cycle; check whether
  modified).
- §14.1 — USCIS form-edition turnover rate (changes annually;
  always re-check current edition before filing).

**Mechanism E posture**: every Recovery move above includes the
phrase "consult a licensed immigration attorney" (or equivalent
professional-counsel deferral). This file IS decision-support, NOT
legal advice. The framings name where the analysis happens; the
binding determination on any specific filing comes from the
attorney with case-specific facts, current USCIS / DOS policy, and
the asker's full filing history.
