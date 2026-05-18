# immigration — decisions.md (Layer 1)

Decision ontology for `immigration`. Scope inherits from
[`_meta_ontology.md` §2](../_meta_ontology.md): US inbound only —
nonimmigrant work / study statuses, employer-sponsored vs self-petitioned
permanent-residence paths, status transitions, dependent statuses, and
the timing decisions that couple to filing windows, priority-date
movement, and travel. Excludes outbound emigration (deferred to V3+),
asylum/refugee adjudication merits (handled by counsel, not framing),
and citizenship-by-investment routes (not modeled).

The `immigration` domain is **high_stakes** per `_meta_ontology.md` §2.
Mechanism E gating applies: this file is decision-support-oriented, not
legal-advice-oriented. Every framing axis below points to the *trade-off
the applicant must reason about*, not the legal answer — the latter
comes from a qualified attorney with case-specific facts. Where a
decision threshold is governed by statute (e.g. INA §245(a) eligibility,
AC21 portability, 240-day work-authorization extension), the
authoritative position is whatever USCIS / DOS publishes as of filing
date. Framing-axes named below are pointers — full framings will live
in `framings.md` (later artifact).

Cross-domain edges are flagged inline. `tech-career` overlaps heavily
(visa-status couples to employer choice, comp negotiation, layoff
response — `_meta_ontology.md` "Cross-domain notes"). `family-planning`
overlaps on marriage-based filings. `personal-finance` overlaps on
exit-tax / 401(k) decisions when a status decision is also a
stay-or-leave decision. Routing across edges is V2-Triage's job; the
edge annotations here help future `framings.md` authors name the
adjacent domains.

---

## 1. H-1B to O-1 transition timing while I-140 is pending

- **Scope**: User is on cap-subject H-1B (typically year 4–6), has an
  approved or pending EB-1/EB-2 I-140, and is considering transition
  to O-1 — usually because H-1B counter is filling and an additional
  cap-exempt option (or a softer evidentiary bar than EB-1A) is
  attractive. Distinct from decision 9 (self-petition path choice at
  the I-140 layer) — here the question is *nonimmigrant* status
  flexibility, not the permanent-residence route itself.
- **Framing-axes-covered**: H-1B-six-year-cap-and-AC21-extension-
  eligibility, O-1-extraordinary-ability-evidentiary-bar-vs-EB-1A,
  employer-portability-and-self-sponsorship-options, dependent-
  status-implications (O-3 vs H-4), priority-date-preservation-across-
  status-change, gap-in-work-authorization-during-COS-vs-CP.
- **Sample situations**:
  - "Year 5 on H-1B; I-140 approved 18 months ago; priority date won't
    be current for 6+ years; want to move from BigCo to a research-
    track role at a startup — should I switch to O-1 first?"
  - "H-1B max-out in 9 months; AC21 3-year extension available because
    I-140 is approved and priority date is not current, but employer
    is hesitant to refile. Is O-1 a real alternative?"

## 2. Marry-for-status timing when partner's own GC priority date is current

- **Scope**: User is in nonimmigrant status (commonly F-1, H-1B, or
  L-1) and is in a relationship with a US-citizen or LPR partner.
  Either marriage itself, or marriage *timing*, is being shaped by
  the user's status pressures (visa expiration, OPT clock, EAD
  renewal lag, layoff exposure). Distinct from a purely personal
  decision because the status-coupling changes the calculus on
  timing, ceremony location, and which spouse petitions. Boundaries
  `family-planning` (the marriage decision itself) — this entry
  covers the *status-timing-and-route* slice only.
- **Framing-axes-covered**: K-1-fiance-vs-marriage-then-AOS-vs-
  marriage-then-CP, immediate-relative-vs-F2A-preference-category-
  (USC-vs-LPR-petitioner), 245(a)-eligibility-and-prior-unlawful-
  presence, two-year-conditional-permanent-residence-and-I-751-burden,
  good-faith-marriage-evidence-and-fraud-presumption-risk, public-
  charge-affidavit-of-support-thresholds.
- **Sample situations**:
  - "F-1 OPT expires in 4 months; H-1B lottery missed; US-citizen
    partner of 2 years has proposed — does it matter whether we marry
    before or after OPT lapses?"
  - "Partner is an LPR (not USC yet); F2A backlog moves slowly — would
    we be better off if they naturalized first and then petitioned, or
    file F2A now and upgrade later?"

## 3. Concurrent I-140 / I-485 vs sequential filing under known retrogression

- **Scope**: User's PERM is approved or about to be; visa bulletin
  *Dates for Filing* is current for the user's category and country
  of chargeability, but *Final Action Date* is not, and retrogression
  is plausibly in the forecast. Decision is whether to file I-140 +
  I-485 concurrently now (unlocking EAD/AP benefits and locking in
  the filing date) versus filing I-140 only and waiting for the
  Final Action Date to be current. Distinct from decision 4 (mid-PERM
  employer change) and decision 6 (EB-2/EB-3 category choice).
- **Framing-axes-covered**: dates-for-filing-vs-final-action-date-
  divergence, EAD-AP-pendency-benefits-vs-COS-options-preserved-on-
  H-1B, AC21-job-portability-after-180-days-of-I-485-pendency,
  child-aging-out-and-CSPA-formula-protection, dual-intent-vs-status-
  abandonment-on-pending-AOS, fee-and-medical-exam-timing-risk-if-
  retrogression-arrives.
- **Sample situations**:
  - "EB-2 India, PERM approved last month; DOS Visa Bulletin moved
    DFF current this month but FAD is 8 years back. Concurrent file
    or wait?"
  - "Spouse on H-4 with EAD; child is 19 and CSPA age is 17 — does
    concurrent filing now lock in the CSPA-protected age?"

## 4. Stay on H-1B vs switch employer mid-PERM (AC21 portability)

- **Scope**: User is on H-1B with PERM in progress (or just-approved
  I-140) at current employer; recruited externally with a comparable
  role and similar SOC code. Decision is whether to use AC21 §106(c)
  to port the approved I-140 to a new employer, or stay through to
  I-485-filing eligibility before moving. Distinct from decision 1
  (status-category change) and decision 6 (EB category change at
  filing).
- **Framing-axes-covered**: AC21-§106(c)-same-or-similar-occupation-
  standard, I-140-approval-and-180-day-validity-rules, supplement-J-
  filing-and-PERM-restart-risk, priority-date-portability-across-
  employers, retention-of-H-1B-cap-exempt-extension-eligibility,
  unvested-equity-and-comp-trade-against-status-progress (boundary
  `tech-career` decision 6).
- **Sample situations**:
  - "I-140 approved 13 months ago at BigCo; competitor offered 30%
    more cash but a different department; SOC code matches at the
    6-digit level. Port now or wait until I-485 is filed?"
  - "Layoff rumors at current employer; PERM filed 5 months ago, not
    yet approved; offered a role at a smaller co willing to restart
    PERM. What's actually preserved if I jump now?"

## 5. Apply for Advance Parole before international travel during AOS

- **Scope**: User has a pending I-485 (adjustment-of-status). A
  foreign trip is planned or required (family event, work travel,
  funeral). Decision is whether to apply for Advance Parole (I-131)
  before departing, and whether to risk travel on a parallel
  nonimmigrant visa (typically H-1B / L-1) instead. The "abandonment
  trap" — departing without AP causes I-485 to be deemed abandoned
  unless one of the narrow dual-intent carve-outs applies — is the
  load-bearing risk.
- **Framing-axes-covered**: AP-pendency-time-and-emergency-AP-
  thresholds, dual-intent-H-1B-and-L-1-travel-carve-outs-vs-other-
  statuses, abandonment-of-pending-I-485-on-non-AP-departure, re-
  entry-inspection-and-CBP-discretion, biometrics-and-interview-
  scheduling-while-abroad, AP-document-validity-period-vs-trip-
  duration.
- **Sample situations**:
  - "I-485 filed 4 months ago; mother is hospitalized abroad; AP
    receipt issued but document not yet in hand. Do I qualify for
    emergency AP, or do I travel on my still-valid H-1B?"
  - "I-485 pending; conference in Europe in 6 weeks; no AP filed
    yet — file expedited AP, file regular AP and reschedule the
    trip, or travel on the L-1?"

## 6. EB-2 vs EB-3 downgrade / upgrade timing under current priority dates

- **Scope**: User has an approved I-140 in one EB category (commonly
  EB-2) and the Visa Bulletin shows the *other* category (EB-3) with
  a sooner current date for their country of chargeability — or vice
  versa, in the reverse direction. Decision is whether to file a new
  I-140 in the alternate category to use the currently-favorable
  date, while preserving the priority date from the original I-140.
- **Framing-axes-covered**: priority-date-portability-across-EB-
  categories-on-same-PERM, second-I-140-filing-mechanics-and-fee,
  Visa-Bulletin-forecasting-and-reversal-risk-(EB-3-India-2020-22-
  cycle-as-precedent), interfiling-of-pending-I-485-vs-fresh-file,
  PERM-validity-and-position-requirement-still-met-at-downgrade-
  level, downgrade-not-a-demotion-employer-letter-language.
- **Sample situations**:
  - "EB-2 India, PD May 2014; current bulletin shows EB-3 India
    current by 8 months versus EB-2. Downgrade and interfile?"
  - "EB-3 China, PD 2019; EB-2 China is now advancing faster — would
    re-filing in EB-2 with the same PERM be worth the fee and
    interfile delay?"

## 7. STEM-OPT vs cap-gap vs employer-sponsored H-1B for new grads

- **Scope**: F-1 student graduating from a STEM-eligible US program
  whose initial 12-month OPT is in flight or about to start. Three
  routes typically compete: (a) extend with 24-month STEM-OPT under
  the current employer, (b) rely on the cap-gap automatic
  authorization if a timely H-1B cap petition is filed, or (c)
  pursue a non-cap H-1B at a cap-exempt employer or an alternate
  nonimmigrant status. Distinct from decision 1 (mid-career H-1B
  alternatives).
- **Framing-axes-covered**: STEM-OPT-employer-E-Verify-requirement-
  and-training-plan, cap-gap-eligibility-window-and-pending-vs-
  approved-petition-rules, lottery-odds-and-multi-year-attempt-
  strategy, cap-exempt-employer-options-(universities-research-
  affiliated-nonprofits), unemployment-tolerance-limits-on-OPT-and-
  STEM-OPT, dependent-F-2-vs-H-4-implications.
- **Sample situations**:
  - "Graduated MS-CS last May; on first-year OPT; H-1B lottery missed
    in March. STEM-OPT extension filed — what happens if I want to
    switch employers in month 6?"
  - "Offer from a startup that is not E-Verify; STEM-OPT requires
    E-Verify — accept the offer and rely on cap-gap, decline and
    take an E-Verify employer's offer, or try for an O-1?"

## 8. Change of status from B-1/B-2 vs consular processing for F-1 / H-1B / etc.

- **Scope**: User is physically in the US on a B-1 or B-2 visitor
  status (commonly extended once) and has identified a longer-term
  status (F-1 study, H-1B work, O-1, L-1) they want to enter.
  Decision is between filing an I-539 / I-129 *change of status*
  inside the US versus departing and pursuing *consular processing*
  abroad. Each path has distinct timing, risk, and re-entry
  consequences.
- **Framing-axes-covered**: 90-day-pre-conceived-intent-rule-on-
  B-visa-entries, COS-pendency-and-bridge-application-mechanics-if-
  B-status-expires, consular-officer-214(b)-discretion-on-prior-
  status-violations, gap-in-status-vs-gap-in-work-authorization,
  travel-during-pending-COS-(abandonment-risk), employer-attestation-
  language-on-when-job-was-offered-vs-when-applicant-entered.
- **Sample situations**:
  - "Entered as a B-2 visitor 6 weeks ago for family visit; received
    an unexpected H-1B job offer with the new employer willing to
    file. COS or fly home and consular-process?"
  - "B-1 visitor for 4 months; admitted to a US grad program starting
    in 8 weeks. F-1 change-of-status now risks 90-day-rule scrutiny
    — consular-process is cleaner but the timeline is tight."

## 9. Self-petition (EB-1A / NIW) vs employer-dependent (EB-2/3) under known PERM bottleneck

- **Scope**: User has a strong professional record (publications,
  patents, citations, awards, media coverage, leadership roles)
  *and* is in an EB-2/3 PERM queue with a multi-year backlog.
  Decision is whether to invest the time and (often) attorney spend
  to pursue an EB-1A (extraordinary ability) or NIW (national-
  interest-waiver) self-petition in parallel to the existing
  employer-sponsored path. Cross-routes `tech-career`: the evidence
  base for EB-1A (recognition criteria, judging panels, original
  contributions) overlaps with the artifacts a senior IC or
  research-track engineer accumulates.
- **Framing-axes-covered**: EB-1A-three-of-ten-criteria-bar-and-
  comparable-evidence, NIW-Matter-of-Dhanasar-three-prong-test,
  attorney-spend-and-RFE-likelihood-at-current-USCIS-temperature,
  parallel-employer-petition-preservation-(self-petition-doesn't-
  cancel-employer-I-140), priority-date-from-the-earlier-filing-
  applicable-to-EB-1-once-current, country-of-chargeability-cross-
  chargeability-via-spouse.
- **Sample situations**:
  - "EB-2 India PERM in flight; PD will be 2018 once filed; I have
    12 first-author papers, 800+ citations, served on 2 PCs. Worth
    the EB-1A attempt now or wait until PERM is approved?"
  - "Research scientist at a lab; employer is uncertain about
    sponsoring; have a coherent national-interest argument for the
    field. NIW now or push the employer harder on EB-2?"

## 10. H-4 EAD work-authorization decisions under H-1B principal's status risk

- **Scope**: User is the H-4 spouse of an H-1B principal whose H-1B
  is at a vulnerable point (PERM not yet approved, employer in
  layoff cycle, or principal's I-140 not yet approved — H-4 EAD
  eligibility requires either an approved I-140 OR an AC21-extension-
  qualifying H-1B). Decision is how to sequence EAD application /
  renewal, employer onboarding, and self-employment / contracting
  setup against principal's status timeline. Cross-routes
  `tech-career` (spouse's own employment decisions).
- **Framing-axes-covered**: H-4-EAD-eligibility-tying-to-principal's-
  I-140-approval-or-AC21-extension, EAD-renewal-pendency-and-540-
  day-automatic-extension-rules, principal-layoff-and-60-day-grace-
  period-impact-on-H-4-status, self-employment-and-LLC-structure-on-
  EAD, transition-to-own-H-1B-cap-lottery-as-status-independence,
  health-insurance-loss-on-principal-status-lapse (boundary
  `health-insurance`).
- **Sample situations**:
  - "Spouse's H-1B employer just announced layoffs; my H-4 EAD
    renewal is pending 4 months. If spouse is laid off in the 60-day
    grace period, what happens to my pending EAD?"
  - "Spouse's I-140 approved; I have an H-4 EAD and an offer to join
    a startup as employee #5. Better to take W-2, or set up my own
    LLC and contract?"

---

## Notes for downstream layers

- **Framings inventory** (forward-pointer to `framings.md`): the axes
  above cluster into ~7–9 reusable framings — status-continuity-
  vs-route-optimality, filing-date-vs-final-action-date-arbitrage,
  dual-intent-and-abandonment-mechanics, AC21-portability-mechanics,
  CSPA-age-protection, priority-date-portability, dependent-status-
  coupling, evidentiary-bar-by-category, employer-dependency-vs-
  self-petition.
- **Blindspot anchors** (forward-pointer to `blindspots.md`): decisions
  3, 5, 6, 9 are highest-density — Visa-Bulletin forecasting,
  abandonment mechanics during AOS travel, EB-category-portability
  rules, and EB-1A evidentiary calibration are frequently miscalibrated
  even among well-informed applicants. Decision 8 (90-day-rule on B
  entries) is the highest-stakes single mis-step because preconceived-
  intent findings ripple into future visa adjudications.
- **Cross-domain edges**: 1, 4, 7, 10 boundary `tech-career` (employer
  choice / comp / layoff response coupled to status); 2 boundaries
  `family-planning` (marriage decision); 5 and 10 boundary
  `health-insurance` (coverage gaps when status lapses); 9 boundaries
  `tech-career` recognition criteria (EB-1A evidence overlaps with
  senior-IC artifacts). Edges are documentation; routing is V2-Triage's
  job.
- **High-stakes posture** (`_meta_ontology.md` §2 Mechanism E): every
  decision above is decision-support, not legal-advice. The framing
  axes name *what to reason about*, not *what to do*. When a user
  situation maps to any of decisions 3, 5, 6, 8, 9, or any combination
  involving prior unlawful presence, the Editor layer should label
  output explicitly as decision-support and defer the binding
  determination to a qualified immigration attorney with case-specific
  facts.
