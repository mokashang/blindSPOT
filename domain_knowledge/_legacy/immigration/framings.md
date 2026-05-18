# immigration — framings.md (Layer 2)

Framing library for `immigration`. Each entry names one lens — the way
a specific community / tradition argues about a decision — and lists the
decisions from [`decisions.md`](./decisions.md) it applies to. Per
[`_schema.md`](../_schema.md), this file is the anchor for Layer 3
(`blindspots.md`): every `Excludes` bullet below is a candidate
blindspot seed. Lines that are vague here dilute the blindspot work
downstream — every `Excludes` bullet should be specific enough that an
insider in this lens would nod.

The `immigration` domain is **high_stakes: true** per
[`_meta_ontology.md` §2](../_meta_ontology.md). Mechanism E gating
applies (per [ROADMAP §5](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating)):
this file names *axioms and trade-offs the applicant must reason about*,
not legal answers. Every framing below is a decision-support pointer —
the binding determination on any specific case comes from a licensed
immigration attorney with case-specific facts, current USCIS / DOS
policy, and the applicant's full filing history. Where a framing names
a statute, rule, or threshold (INA §245(a), AC21 §106(c), CSPA, Matter
of Dhanasar, etc.), treat the citation as a pointer to where the
analysis happens, not as the answer.

Voice anchors (conceptual, not source URLs — those live in `sources.yaml`
once authored): **immigration-attorney voice** (procedural rigor,
"check the statute, then the regulation, then the policy manual");
**AILA-practitioner voice** (case-specific RFE patterns, USCIS
adjudicator temperature, service-center variance); **MurthyDotCom-style
consumer-rights voice** (priority-date watching, Visa Bulletin
archeology, retrogression trauma); **founder-engineer-blogger voice**
(visa-as-employer-leverage, self-petition-as-independence); **F-1
student-forum voice** (OPT clock, cap-gap, STEM extension mechanics);
**dual-intent / corporate-immigration voice** (multinational L-1, EB-1C,
intra-company sequencing); **family-petitioner voice** (marriage-based
filings, conditional PR, I-751 burden); **research-track-scientist
voice** (EB-1A criteria calibration, NIW under Dhanasar); **DOS-watcher
voice** (Visa Bulletin monthly read, forecasting heuristics).

Cross-domain edges: D1, D4, D7, D10 boundary `tech-career`
(employer / comp / layoff coupled to status); D2 boundaries
`family-planning` (marriage decision itself); D5 and D10 boundary
`health-insurance` (coverage gaps on status lapse); D9 boundaries
`tech-career` recognition criteria (EB-1A evidence overlaps with
senior-IC artifacts). Routing across edges is V2-Triage's job; these
edges help framings name adjacent domains rather than absorb their
content.

---

## 1. Status-continuity framing

- **Decisions it applies to**: D1 (H-1B to O-1 transition), D2 (Marry-
  for-status timing), D4 (AC21 portability vs stay), D5 (Advance
  Parole / international travel during AOS), D7 (STEM-OPT / cap-gap),
  D8 (COS from B-1/B-2 vs CP), D10 (H-4 EAD under principal's risk).
- **Mental model summary**: Out-of-status is the only unrecoverable
  state. Every other concern — comp, role, route optimality, attorney
  fees — is recoverable from. Reasons in clock-and-grace-period terms:
  current I-94 expiration, COS pendency-bridge windows, 60-day grace
  on H-1B termination, 90-day window of unauthorized employment that
  flips into a 245(c) inadmissibility, the 540-day automatic-extension
  for EAD-category-eligible renewals, the 240-day work-authorization
  extension on a timely-filed H-1B extension. The framing's reflex on
  every decision is "what status am I in on the morning after this
  move, and what bridges what." Characteristic move: file the bridge
  application *first* (I-539, H-1B extension, I-765 renewal), then
  evaluate the substantive choice. Anchor numbers: 60-day grace on
  termination of H-1B / L-1 / O-1 employment (8 CFR §214.1(l)(2));
  240-day work-auth extension on timely extension filing; 540-day
  automatic EAD extension on timely renewal (for eligible categories
  as of 2024).
- **Characteristic vocabulary**: "out of status", "240-day rule",
  "60-day grace period", "I-94 expiry", "bridge application",
  "timely filing", "automatic EAD extension", "unlawful presence
  vs out-of-status (distinct concepts)", "8 CFR §214.1(l)(2)",
  "INA §222(g) automatic visa voidance."
- **Excludes**:
  - Treats every status-loss as equivalently bad; misses that
    *out-of-status* (failure to maintain conditions) and *unlawful
    presence* (the §222(g) / §212(a)(9)(B) clock) are different
    inadmissibility regimes — a person can be out-of-status without
    yet accruing unlawful presence (USCIS counts unlawful presence
    from formal USCIS / IJ determinations, not from I-94 expiry per
    the 2018 F/J/M memo), and the framing's "never let status lapse"
    elides cases where the I-94 has expired but unlawful presence
    has not started accruing.
  - Risk-aversion bias: routes the asker into status-preserving
    moves (file the H-1B extension, accept the slow PERM at current
    employer) even when the route-optimal move (port to a faster-
    PERM employer; pursue EB-1A self-petition) would resolve the
    underlying constraint in 2–3 years. Opposes F2.
  - Cap-gap and 540-day extensions are presented as automatic; in
    practice both require *timely* filing and the employer / school
    DSO meeting their own procedural deadlines — an HR delay
    invalidates the automatic extension and the framing's
    "you're covered" reassurance evaporates.
  - The framing has no native vocabulary for *strategic accrual* of
    unlawful presence (rare but real for asylum-pending applicants,
    DACA holders considering AOS through marriage, TPS recipients
    considering CP) — situations where the asker's correct move is
    sometimes to allow short out-of-status while a different status
    matures.

## 2. Route-optimality framing

- **Decisions it applies to**: D1 (H-1B to O-1), D3 (concurrent vs
  sequential I-140 / I-485), D6 (EB-2 vs EB-3 downgrade), D9 (EB-1A /
  NIW self-petition vs employer-dependent).
- **Mental model summary**: Status is a means; permanent residence (or
  the right nonimmigrant status for the work) is the end. A 6-month
  status gamble that shaves 4 years off the green-card timeline is the
  rational trade for an applicant whose horizon is decades, not visa-
  cycles. Reasons in queue-length / category-velocity terms: current
  Visa Bulletin, retrogression history, USCIS RFE / approval rate by
  category, attorney's success rate on the specific petition type,
  the priority-date math under "what if I were filing today vs
  filing under the alternate route." Characteristic move: model the
  *route* and back-solve the status — accept temporary status
  fragility (file an EB-1A while H-1B max-out approaches; downgrade
  EB-2→EB-3 to catch a faster bulletin; do CP instead of AOS to clear
  USCIS backlog) when the route gain is structural. Anchor: EB-1A /
  NIW priority dates are often current for non-China / non-India
  even when EB-2 / EB-3 are years backlogged; the EB-1A self-petition
  closes a 5–10 year gap for ROW applicants in months.
- **Characteristic vocabulary**: "priority date", "category velocity",
  "retrogression history", "Final Action Date", "Dates for Filing",
  "category arbitrage", "downgrade-and-interfile", "Matter of
  Dhanasar three-prong", "EB-1A three-of-ten criteria", "Country of
  chargeability", "cross-chargeability via spouse."
- **Excludes**:
  - Treats route gain as the dominant axis, under-weighting that
    *during* the transition the asker's family (H-4 spouse, H-4
    children, school continuity) may face EAD lapses, school re-
    enrollment, or health-insurance gaps the framing's "10 years
    faster" headline buries. Opposes F1, F8.
  - Visa Bulletin forecasting is presented with more confidence than
    DOS's own analyst Charlie Oppenheim retains in his public
    briefings — the framing's "EB-3 India is faster this fiscal
    year" anchor is a one-bulletin-out projection that has reversed
    inside 6 months multiple times (notably EB-3 India 2020–22).
  - Assumes USCIS adjudication quality is constant across service
    centers and policy administrations; in practice RFE rates on
    EB-1A and NIW have varied 2–3× between 2017 and 2023, and the
    framing's "the case is strong, file it" advice is calibrated
    to a different RFE regime than the current one.
  - Doesn't price attorney time and dollar cost: a sophisticated
    EB-1A petition is $8–15k in attorney fees plus 100–200 hours
    of the applicant's own evidence-curation time; if the
    incremental green-card-velocity is 2 years on a 8-year wait,
    the per-hour wage on the time invested is often less than the
    asker's day-job opportunity cost.

## 3. Filing-window-arbitrage framing

- **Decisions it applies to**: D3 (concurrent I-140 / I-485 under
  retrogression), D5 (AP / international travel), D6 (EB-2 vs EB-3
  downgrade timing).
- **Mental model summary**: USCIS / DOS structure benefits via filing
  *windows* rather than continuous eligibility — DFF vs FAD divergence
  opens a window to file I-485 (unlocking EAD/AP) even when the green
  card itself is years off; emergency AP windows open and close based
  on documented hardship; downgrade interfile windows are bounded by
  visa availability at the moment of the request. The asker who reads
  the Visa Bulletin monthly and pre-stages medical exams, photos,
  affidavits of support, and signed I-693s captures windows the asker
  who waits for a clean signal does not. Reasons in calendar-deadline
  terms: bulletin release date (mid-month for the following month),
  acceptance receipt date as the lock-in event, biometrics scheduling
  lag, RFE response 87-day clock. Characteristic move: pre-stage every
  document that could ever be needed, then file the *moment* the
  window opens — bulletin watching is a continuous activity, not a
  pre-filing event.
- **Characteristic vocabulary**: "Visa Bulletin watch", "DFF / FAD
  divergence", "lock-in receipt date", "concurrent filing benefits",
  "EAD / AP combo card", "I-693 sealed envelope shelf life",
  "biometrics ASC scheduling", "RFE 87-day clock", "request for
  premium processing", "Charlie Oppenheim guidance."
- **Excludes**:
  - The framing's optimism on "DFF means you can file now" is
    routinely undercut by *USCIS's own determination* that it will
    accept I-485s based on DFF (USCIS posts this monthly; the
    answer is sometimes no). The framing rarely names that DFF is
    *DOS's* table and AOS filing eligibility is *USCIS's* call —
    they can diverge.
  - "Pre-stage your I-693" misses the medical-exam validity window
    (USCIS extended I-693 validity to "indefinite if signed by
    civil surgeon, no expiration" in late 2024 — prior to that, the
    sealed envelope was good 60 days from signing; the framing's
    docs from earlier vintage carry expired logic).
  - Treats the filing-window as costless when *open* — but the
    concurrent-I-485 filing locks the asker out of certain status
    moves (abandons pending non-immigrant intent in some readings;
    H-4 dependents must also file or risk losing derivative
    eligibility on age-out), which the framing's "file when the
    window opens" reflex doesn't surface.
  - Visa Bulletin "watch" presumes the asker has bandwidth to read
    a monthly DOS document and translate it into action; for an
    asker without an attorney on retainer the practical question
    "do I have to do anything this month" is opaque, and the
    framing's "monitor continuously" advice is over-asked.

## 4. Dual-intent-and-abandonment framing

- **Decisions it applies to**: D5 (AP during AOS), D8 (COS vs CP for
  F-1 / H-1B / etc.).
- **Mental model summary**: Most nonimmigrant statuses (B-1, B-2,
  F-1, J-1, TN) carry a *nonimmigrant intent* presumption — entry or
  status maintenance is conditioned on the noncitizen showing they
  intend to depart. H-1B and L-1 are statutory dual-intent (and O-1
  is informally treated as such), so they tolerate concurrent
  immigrant-intent activity (I-140 pending, I-485 filed). A pending
  I-485 *itself* creates abandonment risk on any departure without
  Advance Parole, except for the narrow dual-intent carve-outs.
  Reasons in intent-evidence terms: what does the I-94 stamp /
  consular officer / CBP officer perceive as the asker's current
  intent, and what statutory regime tolerates the underlying
  immigrant filing. Characteristic move: never depart on a non-dual-
  intent status with a pending I-485 (no AP, even with a valid H-1B
  visa, is a category-mistake the framing catches first); always
  file the I-131 in advance with realistic processing-time padding.
- **Characteristic vocabulary**: "dual intent", "INA §214(b)
  presumption", "abandonment of pending I-485", "Advance Parole",
  "I-131 emergency criteria", "nonimmigrant-intent visas",
  "preconceived intent", "F-1 dual-intent rejection", "AP
  travel document", "parolee inspection at port of entry."
- **Excludes**:
  - The "H-1B is dual-intent so I can travel" advice is broadly
    correct but skips that *the visa stamp itself* (the consulate
    stamp permitting entry, not the I-94) may have expired during
    the AOS pendency; the asker travels on a valid I-94 with a
    pending I-485 and discovers at re-entry that they need to
    renew the visa stamp at a consulate before returning. CBP /
    DOS coordination is not the framing's strong suit.
  - 245(k) carve-outs for employment-based AOS applicants who fell
    out of status briefly (up to 180 aggregate days) are mentioned
    in passing but the framing's "any abandonment is fatal"
    posture under-uses 245(k) as a recovery path.
  - Frames Advance Parole as *the* permission slip to travel —
    misses that travel on AP carries a procedural risk (some
    older case law treated AP-departure-and-return as breaking
    H-1B status, requiring a fresh H-1B stamping abroad before
    extension); newer USCIS guidance softened this but circuit
    splits remain in fringe cases.
  - The framing protects the asker from *AOS abandonment* but
    not from *CBP secondary inspection* on return — a returning
    AP holder with an inconsistent I-94 history, prior 214(b)
    refusal, or evidence of unauthorized employment can be
    paroled in but referred to ICE-detained removal proceedings
    in extreme cases.

## 5. AC21-portability framing

- **Decisions it applies to**: D4 (Stay on H-1B vs switch employer
  mid-PERM).
- **Mental model summary**: AC21 §106(c) lets an H-1B holder with an
  approved I-140 port to a new employer in a "same or similar
  occupation" once the I-485 has been pending ≥180 days; AC21 §104(c)
  allows H-1B extensions beyond the 6-year max when I-140 is approved
  and priority date is not current. The framing treats the I-140
  approval and the 180-day I-485 mark as *unlocks*: once cleared, the
  asker has portable green-card progress that survives employer
  changes. Reasons in milestone terms: PERM filed, PERM approved,
  I-140 filed, I-140 approved, I-485 filed, I-485 pending 180 days,
  AC21 ported. Characteristic move: do not port until the I-140 is
  approved (porting on a pending I-140 forces PERM re-start at the
  new employer); supplement-J the new role within the 60-day grace
  window after a layoff if I-485 has been pending 180+ days. Anchor:
  SOC code at the 6-digit level is the most common adjudicator
  reference; same broad job family is the policy-manual standard but
  RFE risk rises as the new role drifts from the old.
- **Characteristic vocabulary**: "AC21 §106(c) same-or-similar",
  "180-day mark", "supplement J", "I-140 approval portability",
  "AC21 §104(c) 3-year extension", "SOC code match", "successor-
  in-interest filing", "transferring H-1B with approved I-140",
  "porting on a pending I-140 (don't)", "job-portability under
  pending I-485."
- **Excludes**:
  - The "same or similar occupation" standard is administered by
    USCIS adjudicators reading SOC codes literally; a promotion
    from Software Engineer (15-1252) to Software Engineering
    Manager (11-3021) crosses major-group boundaries and the
    framing's "you're fine, same domain" reassurance can route the
    asker into an RFE that surfaces 18 months after the port.
  - The framing assumes the new employer cooperates on supplement-J
    timing and on responding to RFEs about job duties; in practice
    the new employer may not have an in-house immigration team, and
    the asker discovers post-port that the employer cannot produce
    a job-duty letter satisfactorily.
  - 180-day milestone presumes the I-485 receipt is the lock-in
    event; doesn't catch that USCIS-initiated AOS denials in the
    180-day window (e.g. for a procedural defect in the underlying
    I-140 that surfaces later) can re-open the abandonment risk
    even after the 180-day mark has nominally passed.
  - The framing prices employer change as a *legal* portability
    question and skips the *human* portability question — the
    asker's PERM was sponsored by a hiring manager who would
    write the reference call, whose 4-year relationship is the
    de facto employment-based GC machinery; the new employer's
    HR has no equivalent context, which lengthens RFE response
    cycles.

## 6. CSPA-and-family-clock framing

- **Decisions it applies to**: D2 (Marry-for-status timing), D3
  (Concurrent I-140 / I-485 under retrogression).
- **Mental model summary**: The Child Status Protection Act freezes a
  derivative beneficiary's "age" for green-card purposes via a formula
  that subtracts the I-140 pendency time from the child's actual age
  at the moment the priority date becomes current. A child who turned
  21 chronologically is sometimes still a "child" under CSPA, and a
  child whose CSPA age crosses 21 before the priority date is current
  ages out and must re-file under F2B. Reasons in formula terms:
  derived-beneficiary age = (chronological age at PD current) − (I-140
  pendency days). Characteristic move: file concurrently the moment
  DFF opens — every day of I-140 pendency banked while the child is
  pre-21 is a day shaved off the CSPA age, and pre-21 filing of I-485
  *itself* locks the CSPA age determination per Matter of Wang and the
  2023 USCIS policy update. Anchor: CSPA-protected age is the
  load-bearing variable for any family with a child aged 17–22 at the
  PD-current event.
- **Characteristic vocabulary**: "CSPA age formula", "freezing the
  child's age", "Matter of Wang", "F2A vs F2B aging-out",
  "derivative beneficiary", "priority date sought-to-acquire",
  "USCIS CSPA policy manual update (Feb 2023)", "30/45/60-day
  sought-to-acquire window", "F2A immediate-relative crossover."
- **Excludes**:
  - The CSPA formula doesn't apply uniformly across categories —
    immediate-relative children of US citizens get a different (and
    in some readings stronger) protection than employment-based or
    F-preference derivative children. The framing's single-formula
    summary glosses the category-specific nuance.
  - "Sought to acquire" 1-year window from PD-current to act has
    been re-litigated repeatedly (Cuellar de Osorio, etc.); the
    practical USCIS reading shifted in 2023 from FAD-current to
    DFF-current as the trigger, but the framing's prior-vintage
    documents and 2019-era attorney memos may still anchor on the
    FAD-current reading.
  - Marriage by the child *before* CSPA crystallizes converts the
    F2A derivative into an F3 / F4 standalone — a step the framing
    treats as a footnote when it should be the headline for askers
    with adult children considering marriage timing.
  - Doesn't engage with the cross-border school decision: a CSPA-
    protected child whose CSPA-age would be 20.5 at PD-current may
    be enrolling in a foreign university; the framing's "they're
    protected" doesn't address whether the time abroad during
    pendency counts the same way against the formula.

## 7. Priority-date-portability framing

- **Decisions it applies to**: D6 (EB-2 vs EB-3 downgrade / upgrade),
  D9 (EB-1A / NIW self-petition vs employer-dependent).
- **Mental model summary**: A priority date attaches to the underlying
  labor certification or self-petition, not to the I-140 or category.
  An EB-2 PERM applicant whose PD is May 2014 can file a second I-140
  under EB-3 *using the same PERM*, keeping the May 2014 PD; an
  EB-1A self-petition does not re-use the PERM's PD but a separately-
  filed EB-1A's earlier PD ports forward to a subsequent EB-2 / EB-3
  *if those use the same employer / PERM*. The framing reasons in
  preservation-and-transfer terms: which filings carry which PDs,
  which can be ported, which freshly establish. Characteristic move:
  file the parallel petition (EB-3 downgrade I-140, EB-1A self-
  petition) without canceling the original — keep the earliest PD
  attached to whatever petition becomes current first. Anchor:
  9 FAM 502.1-1 (priority date is the date the qualifying petition
  is filed) and 8 CFR §204.5(e) (priority-date retention rules) are
  the governing texts.
- **Characteristic vocabulary**: "priority date retention",
  "9 FAM 502.1-1", "8 CFR §204.5(e)", "PD portability across
  categories", "interfile with prior PD", "fresh PD vs ported PD",
  "I-485 interfiling under existing PD", "supplement-J under
  prior PD."
- **Excludes**:
  - "PD ports forward to the new petition" is correct only when the
    new petition is also employer-sponsored and using the same
    underlying labor certification — for a switch from EB-2 PERM to
    EB-2 NIW (self-petition), the PD does *not* port; the asker
    starts over. The framing's portability shorthand misses this.
  - The interfile process is administratively governed at the
    field-office level; some service centers actually accept the
    interfile request quickly, others batch it and the I-485 ages
    unattended for 18+ months. The framing's "interfile and you
    move to EB-3 velocity" assumes a procedural reliability USCIS
    doesn't deliver uniformly.
  - Cross-chargeability via spouse (using a non-quota-backlogged
    spouse's country of birth as the chargeability country) is a
    separate PD-portability move that the framing's category-only
    vocabulary doesn't name — under-promoted relative to its
    impact for India / China asker-spouse pairs.
  - Doesn't engage with the *automatic conversion* mechanic:
    F2A→IR1 when the LPR petitioner naturalizes mid-pendency.
    The PD ports but the category accelerates — this is the
    family-side equivalent of EB-2/EB-3 portability the framing
    treats as a separate vocabulary.

## 8. Dependent-status-coupling framing

- **Decisions it applies to**: D2 (Marry-for-status timing), D10
  (H-4 EAD under principal's status risk).
- **Mental model summary**: Dependent statuses (H-4, L-2, O-3, F-2,
  J-2) derive from the principal — when the principal's status
  ends, suspends, or transitions, the dependent's status moves in
  lockstep. H-4 EAD eligibility specifically ties to either an
  approved I-140 (under 8 CFR §214.2(h)(9)(iv)) OR a one-year-
  extension of H-1B status under AC21 §104(c) / §106(a). L-2 spouses
  have automatic work authorization since 2022 (no I-765 required
  for category L-2S); J-2 spouses require I-765 with hardship
  showing. The framing reasons in derivative-mechanics terms: when
  does the EAD attach, when does it lapse, what triggers re-
  acquisition. Characteristic move: time the dependent's
  job-acceptance, business formation, or healthcare-enrollment
  *forward* of the principal's status-locking event (I-140
  approval, H-1B extension grant, COS approval), not backward
  from the dependent's preferred start date.
- **Characteristic vocabulary**: "H-4 EAD", "8 CFR §214.2(h)(9)(iv)",
  "L-2S automatic work authorization (2022)", "derivative
  beneficiary", "principal's status flow-down", "540-day automatic
  EAD extension for H-4 / L-2 / E", "J-2 hardship showing",
  "principal-dependent uncoupling on divorce."
- **Excludes**:
  - The framing's "L-2 spouses have automatic work auth" is true
    only for L-2S category (post-2022 rule); pre-rule L-2 holders
    grandfathered into the I-765 EAD process and the framing's
    "no EAD needed" misses that some L-2 spouses still need to
    refile to convert to L-2S formally.
  - Treats principal-dependent coupling as symmetric; doesn't
    catch that an H-4 dependent's I-765 EAD renewal lag (8–18
    months in 2023–24) is decoupled from the principal's H-1B
    extension speed — the principal can renew in 15 days under
    premium processing while the dependent's EAD sits, and the
    framing's "in lockstep" reflex misses the rate-mismatch.
  - Divorce / separation breaks the principal-dependent coupling
    with limited grace; the dependent must self-petition
    (VAWA in abusive cases) or transition to own status. The
    framing has no native vocabulary for the abusive-relationship
    case (VAWA exception, §204(a)(1)(A)(iii)) where the
    coupling-mechanic is dangerous to the dependent.
  - Children's derivative status follows the principal's path but
    children of dependents (e.g. H-4 child reaching 21) have
    separate aging-out logic — the framing's "the family moves
    together" assumes the 21-year cliff doesn't intervene.

## 9. Evidentiary-bar framing

- **Decisions it applies to**: D1 (H-1B to O-1 transition), D9 (EB-1A
  / NIW self-petition vs employer-dependent).
- **Mental model summary**: O-1, EB-1A, and NIW are evidence-based
  categories — adjudicators evaluate a portfolio of objective
  artifacts (publications, citations, judging panels, original-
  contribution evidence, media coverage, awards, salary percentile)
  against statutory criteria. O-1A requires "extraordinary ability"
  in science / education / business / athletics; EB-1A requires the
  same plus "sustained acclaim" and "intent to continue work in the
  field of extraordinary ability"; NIW requires Matter of Dhanasar
  three-prong (substantial merit + well-positioned + beneficial to
  waive labor certification). The framing reasons in criterion-checks
  and final-merits-determination terms: which of the 10 EB-1A criteria
  has the asker met (need 3 minimum), which of the 8 O-1A criteria
  (need 3, or comparable evidence), and how the Kazarian two-step
  analysis applies. Characteristic move: build the petition as a
  systematic answer to each criterion with cross-cited evidence;
  prepare letters of recommendation from independent experts who
  can speak to original contribution, not just acquaintance.
- **Characteristic vocabulary**: "EB-1A 10 criteria", "O-1A 8
  criteria", "comparable evidence", "Kazarian two-step",
  "Matter of Dhanasar three-prong", "substantial merit and national
  importance", "well positioned to advance the endeavor",
  "balance of factors", "AAO precedent decisions",
  "independent expert testimony."
- **Excludes**:
  - The framing treats USCIS adjudication as a reasoned application
    of criteria; in practice RFE rates on EB-1A vary 2–3× by service
    center and by the political administration's stance, and
    identical petitions filed in 2017 vs 2020 vs 2023 receive
    materially different scrutiny. The framing's "the case is
    strong" calibration assumes a steady-state adjudicator.
  - Letters of recommendation are presented as a criterion the
    asker controls; in practice the *circulation pattern* of
    template letters across the immigration-attorney community
    has produced an adjudicator skepticism that the framing rarely
    surfaces — a too-polished letter that pattern-matches AILA-
    boilerplate is sometimes weaker than a less-polished
    independent letter.
  - "Comparable evidence" is presented as a flexibility (you can
    substitute X for criterion Y); in adjudication, the comparable-
    evidence pathway is heavily scrutinized and the framing's
    optimism on substitution rarely tracks RFE patterns. Opposes
    F10.
  - The framing optimizes the *petition* but rarely the *post-
    approval flow*: an EB-1A approval triggers I-485 filing
    eligibility, but the asker who hasn't pre-staged medical exams,
    affidavit of support, etc. loses 6 months of priority-date-
    current window while assembling the consequent paperwork.

## 10. Visa-as-employer-leverage framing

- **Decisions it applies to**: D1 (H-1B to O-1 transition), D4 (AC21
  portability vs stay-with-sponsor), D10 (H-4 EAD under principal's
  risk).
- **Mental model summary**: Employer-sponsored visa status is a
  retention tool. The asker's leverage in any comp / role / layoff
  conversation is bounded by their visa status; the employer's
  leverage is amplified by it. Sponsorship of PERM, payment for
  attorney work, refresher of an O-1 renewal — these are
  employer-discretionary acts that bind the asker in ways an
  at-will US-citizen colleague doesn't experience. The framing
  reasons in independence-and-portability terms: what is the cost
  to me of having to find a new sponsor in 60 days, what is the
  cost to the employer of losing my role, where is the leverage
  point that doesn't depend on the visa. Characteristic move:
  build *visa-independent* leverage (self-petitioned EB-1A or NIW,
  cap-exempt employer optionality, spouse's independent status,
  EAD-eligible status) such that the next compensation conversation
  is structured on labor-market terms, not status-bounded terms.
  Anchor: AC21 portability and self-petition independence are the
  two routes out of visa-bounded labor.
- **Characteristic vocabulary**: "visa handcuff", "golden cage",
  "sponsorship dependency", "self-petition independence",
  "EB-1A as freedom", "cap-exempt optionality", "60-day grace
  reality", "the company knows you can't walk", "EAD as
  leverage equalizer", "visa-independent BATNA."
- **Excludes**:
  - The framing's "build visa-independent leverage" advice is
    most actionable for askers who already have the EB-1A
    portfolio or the cap-exempt opportunity; for the modal asker
    (4 years into H-1B at a BigCo, EB-2 India backlog, no
    publications), the framing names a real problem without a
    practical exit. Opposes F1.
  - Treats employer-sponsor relationship as transactional;
    misses that the employer's *immigration team* (often a
    long-tenured attorney whose loyalty is to the company, not
    the asker) is the practical interface, and the asker's
    leverage in that relationship is even narrower than the
    headline employer relationship.
  - Underweights the dependent-status angle: an asker whose
    spouse and children depend on the H-1B principal's
    continued employment for H-4 status experiences leverage
    asymmetry the framing's individual-focused vocabulary
    glides over.
  - The "self-petition independence" framing prices attorney
    fees ($8–15k for EB-1A, $3–5k for NIW) and applicant
    evidence-curation time as one-time costs; the framing
    skips that USCIS rejection or RFE-then-denial restarts
    the dependency cycle while consuming the cash and time
    already spent.

## 11. Marriage-good-faith framing

- **Decisions it applies to**: D2 (Marry-for-status timing).
- **Mental model summary**: USCIS adjudicates marriage-based filings
  under a "good faith" standard — was the marriage entered for the
  purpose of building a life together, or was it entered to secure
  an immigration benefit. The 2-year conditional permanent residence
  (under INA §216) requires I-751 with shared-life evidence at the
  2-year mark; failure to file or insufficient evidence is a removal-
  proceedings trigger. The framing reasons in evidence-quality terms:
  joint financial accounts opened pre-marriage, joint lease /
  mortgage with both names, shared travel records, photographs across
  the relationship's timeline, affidavits from family and community,
  consistency of biographical details across the I-130 / I-485 /
  I-751 narrative. Characteristic move: build the documentation as
  the marriage builds, not retroactively — joint accounts from
  month one, shared address on every utility bill, consistent name
  usage on insurance and emergency contacts. Anchor: 8 CFR §204.2
  good-faith factors and the Stokes interview / fraud-unit referral
  workflow.
- **Characteristic vocabulary**: "good faith marriage", "I-751
  removal of conditions", "Stokes interview", "fraud unit referral",
  "joint financial commingling evidence", "8 CFR §204.2",
  "marriage-fraud presumption", "USCIS RFE on bona fides",
  "I-130 vs IR-1 vs CR-1", "Affidavit of support I-864 sponsor
  obligation."
- **Excludes**:
  - The framing's "build evidence as the marriage builds" advice
    assumes the marriage is structurally healthy; for couples whose
    relationship matures non-linearly (long-distance, separate
    careers, separate residences for non-immigration reasons), the
    evidentiary baseline the framing recommends is a poor fit
    despite the marriage being entirely bona fide.
  - LGBTQ+ couples with prior partnerships in jurisdictions where
    same-sex marriage was not recognized face a different
    evidentiary terrain (prior unrecognized cohabitation, foreign
    civil-union records of varying authenticity) the framing's
    US-centered defaults don't address well.
  - The framing protects against *fraud findings* but doesn't
    address the divorce-during-conditional-PR scenario, where
    the foreign spouse must show either (a) marriage was bona
    fide at inception but ended via divorce, (b) hardship to a
    USC child, or (c) abuse — three distinct evidence regimes
    that the "build the evidence" advice doesn't differentiate.
  - The I-864 affidavit of support is a 10-year obligation
    surviving divorce; the framing presents it as a filing checkbox
    when it is a financial commitment with case-law-enforced
    creditor rights against the US-citizen sponsor.

## 12. STEM-OPT-lottery-arbitrage framing

- **Decisions it applies to**: D1 (H-1B to O-1 transition), D7 (STEM-
  OPT / cap-gap / employer-sponsored H-1B for new grads).
- **Mental model summary**: An F-1 graduate's first 5–7 years of US
  career are structured by the H-1B cap lottery's roughly 25–35%
  per-attempt success rate, the 12-month OPT + 24-month STEM-OPT
  extension giving 3 lottery attempts, the cap-gap automatic
  extension covering the April–October waiting period if H-1B is
  filed on time, and the E-Verify requirement on the STEM-OPT
  employer. Reasons in lottery-attempt-budget terms: each year
  unselected is one of three cap-gap-bridged attempts consumed;
  STEM-eligible degree means the asker has 3 attempts vs the 1
  attempt for non-STEM. The framing optimizes employer choice
  (E-Verify yes/no), employer-side H-1B-filing reliability, and
  geography to maximize lottery-attempt count. Characteristic move:
  pick employers based on H-1B-filing track record (some BigCos
  multi-register; some small startups can't reliably file by
  April 1); maintain STEM-OPT employer with strong E-Verify
  posture even at modest comp discount.
- **Characteristic vocabulary**: "OPT clock", "STEM extension",
  "cap-gap", "E-Verify employer", "H-1B beneficiary registration",
  "multi-registration rule (2024+ updates)", "I-983 training
  plan", "unemployment tolerance (90 / 150 days)", "5-month
  reporting requirement", "DSO and SEVIS update cadence."
- **Excludes**:
  - The framing's lottery-arithmetic optimism (3 attempts ≈ 70%+
    aggregate odds) assumed pre-2024 single-registration mechanics;
    the 2024 USCIS beneficiary-centric rule that capped
    multi-registrations changed the per-cycle math materially and
    framings calibrated to pre-2024 attempt-rates over-predict
    cumulative success.
  - The framing assumes the asker's STEM-eligible degree confers a
    24-month extension uniformly; in practice the degree must be
    from a SEVIS-certified institution AND on the DHS STEM-
    designated list (currently 400+ CIP codes), and some adjacent
    degrees (data analytics, technology management) sit just
    outside the list and the framing's "STEM means 24 months"
    glides past CIP-code verification.
  - "Pick employers based on H-1B-filing track record" is the right
    instruction but requires the asker to have visibility into
    employer H-1B filing data the asker rarely has at offer-
    acceptance time. The framing's optimization is correct in
    direction but practically constrained by information
    asymmetry.
  - The 90 / 150-day unemployment tolerance on OPT / STEM-OPT is
    presented as a known constraint; in practice the *clock-start*
    moment (last day of paid employment vs last day of authorized
    employment) is interpreted variably by DSOs and the framing
    rarely names the variance.

## 13. Consular-vs-COS-discretion framing

- **Decisions it applies to**: D7 (STEM-OPT / cap-gap / H-1B for new
  grads), D8 (COS from B-1/B-2 vs CP for F-1 / H-1B / etc.).
- **Mental model summary**: Change-of-status (COS) inside the US
  proceeds through USCIS adjudication on the paper file; consular
  processing (CP) abroad requires a consular officer interview at
  which §214(b) nonimmigrant-intent presumption is administered
  with broad officer discretion. Reasons in discretion-and-record
  terms: USCIS rules against the asker on the file, the consular
  officer rules with reference to the file plus the impression of
  the interview. The 90-day-rule on B-visa entrants (entering on
  B-1/B-2 with intent that crystallizes within 90 days as F-1 /
  H-1B / etc. is "preconceived intent" and grounds for visa
  cancellation). Characteristic move: avoid CP after any prior US
  visa refusal, prior overstay, or any contact with US law
  enforcement; prefer CP when the asker has a clean record and a
  consulate (home country) where the officer cohort is known to
  be moderately friendly to the visa category being applied for.
- **Characteristic vocabulary**: "INA §214(b) presumption",
  "consular officer discretion", "90-day preconceived-intent
  rule", "visa annotation", "CEAC appointment scheduling",
  "DS-160 consistency", "AP (administrative processing) at
  consulate", "third-country processing", "visa stamping",
  "post-COS travel risk."
- **Excludes**:
  - "Consular discretion is broad" is true at the policy level but
    the framing glides over that *specific consulates* have
    documented refusal-rate patterns by visa category — Chennai's
    H-1B refusal rate vs Mumbai's, Manila's vs Bangkok's, Lagos's
    vs Accra's — that should change the CP-or-COS calculus and
    the framing's generic "consular discretion" doesn't capture
    granular consulate variance.
  - The 90-day preconceived-intent rule is presented as a hard
    line; in practice it's the DOS Foreign Affairs Manual's
    *guideline* and a §214(b) refusal can apply outside the 90-
    day window when other facts support preconceived intent. The
    framing's "wait until day 91" advice is structurally weak.
  - "CP after a denial is harder" understates the *administrative
    processing* (Section 221(g)) regime where a consular officer
    refers a case for security / FBI / agency clearance with no
    fixed timeline; CP applicants in administrative processing
    can be stuck abroad for 3–18 months and the framing rarely
    names AP as a distinct risk category.
  - The framing's COS-vs-CP binary skips the *re-entry-after-CP*
    risk: even an approved consular stamp triggers a CBP
    inspection at port of entry where any factor (DS-160
    inconsistency, social-media review) can result in re-refusal
    at the border. CBP and DOS are separate authorities and the
    framing's "consular approval is the answer" is one step short.

## 14. Pro-se / consumer-rights framing

- **Decisions it applies to**: D5 (AP / international travel during
  AOS), D7 (STEM-OPT / cap-gap), D8 (COS from B-1/B-2 vs CP), D10
  (H-4 EAD under principal's risk).
- **Mental model summary**: Immigration benefits are administered on
  forms with line-by-line instructions; an asker who reads the
  instructions, the relevant 8 CFR section, and the USCIS Policy
  Manual carefully can correctly file most non-adversarial
  applications (I-131 AP, I-765 EAD, I-539 extension / COS, I-130
  immediate-relative) without an attorney. Reasons in form-and-fee
  terms: which form, which evidence list, which filing fee, which
  USCIS lockbox or service center, which processing time. The
  framing reasons that USCIS denials for procedural defects
  (missed signature, wrong fee, expired form edition) are
  recoverable via re-filing in the same fee cycle; substantive
  defects need representation. Characteristic move: file pro se for
  I-131, I-765 renewal, I-539 extension; engage counsel for I-130
  / I-485 with prior unlawful presence, I-140 self-petition,
  removal-proceedings response, or any adversarial filing.
- **Characteristic vocabulary**: "pro se filing", "USCIS Policy
  Manual", "form edition compliance", "filing fee schedule",
  "lockbox vs service center", "case status check via receipt
  number", "USCIS InfoPass / online account", "e-filing
  availability", "RFE response template", "AAO appeal."
- **Excludes**:
  - The framing's pro-se confidence is calibrated to a USCIS-of-
    record that issues clear instructions and consistent
    adjudication; current USCIS form-edition turnover (multiple
    editions per fiscal year for high-volume forms; rejection of
    wrong-edition filings without refund of fee) makes pro-se
    filing a procedural minefield the framing under-weights.
  - "Substantive defects need representation" is correct but
    the boundary between procedural and substantive is itself
    a judgment call; an asker pro-se on I-485 who answers a
    public-charge question incorrectly may not recognize the
    answer as substantive until the RFE arrives. The framing's
    decision rule has a self-referential gap.
  - Cost asymmetry: $10k of attorney fees is large in the
    moment but small relative to the cost of a removal-
    proceedings recovery; the framing's "save the attorney for
    the hard cases" can route the asker into a hard case they
    don't recognize as such. Opposes F2 and F9 in calibration.
  - The framing prices attorney representation as binary (have
    one / don't); in practice modular engagement (one-hour
    review of a pro-se draft, RFE-response-only retainer, post-
    filing consultation) is available and the framing rarely
    distinguishes engagement modes.

---

## Coverage map

Per `_schema.md`, every decision needs ≥ 3 framings.

| Decision | Framings that cover it | Count |
|---|---|---|
| D1 H-1B to O-1 transition timing | F1, F2, F9, F10, F12 | 5 |
| D2 Marry-for-status timing | F1, F6, F8, F11 | 4 |
| D3 Concurrent I-140 / I-485 under retrogression | F2, F3, F6 | 3 |
| D4 AC21 portability vs stay-with-sponsor | F1, F5, F10 | 3 |
| D5 Advance Parole / international travel during AOS | F1, F3, F4, F14 | 4 |
| D6 EB-2 vs EB-3 downgrade / upgrade timing | F2, F3, F7 | 3 |
| D7 STEM-OPT / cap-gap / H-1B for new grads | F1, F12, F13, F14 | 4 |
| D8 COS from B-1/B-2 vs CP | F1, F4, F13, F14 | 4 |
| D9 EB-1A / NIW self-petition vs employer-dependent | F2, F7, F9 | 3 |
| D10 H-4 EAD under principal's status risk | F1, F8, F10, F14 | 4 |

All 10 decisions satisfy the ≥ 3 framings minimum.

## Cross-framing tensions

Direct axiom-level oppositions to surface in Layer 3 and to flag for
Triage / Risk Officer routing when the asker's prompt vocabulary lands
on one side:

- **F1 (status-continuity) ↔ F2 (route-optimality)**. F1 says: never
  let status lapse; the recoverable downside of staying-the-course is
  smaller than the unrecoverable downside of out-of-status. F2 says:
  optimize the route; tolerate temporary status fragility when the
  route gain shaves years off the green-card timeline. Same asker, same
  facts (H-1B max-out, EB-2 India PD May 2014, EB-1A-eligible CV) gets
  opposite advice. Triage should surface F2 when the asker's prompt
  reads as F1-anchored ("how do I extend the H-1B again") and
  vice-versa.
- **F1 (status-continuity) ↔ F13 (consular-vs-COS-discretion)**. F1's
  reflex is "don't leave the country during a pending filing"; F13's
  reflex is "if your record is clean, CP is the cleaner path and COS
  is a procedural drag." On D8, the asker entered on B-1/B-2 and got
  an unexpected H-1B offer: F1 says file COS now to lock the status;
  F13 says fly home and consular-process to avoid the 90-day-rule
  scrutiny on the COS file.
- **F9 (evidentiary-bar) ↔ F10 (visa-as-employer-leverage)**. F9 reads
  the petition record as the answer to whether EB-1A / NIW are viable
  — does the CV meet the criteria. F10 reads the same record as the
  answer to whether the asker has *exit option* from employer-
  sponsored dependency. The same publication / citation portfolio
  is a procedural input under F9 and a leverage instrument under F10;
  the question "should I self-petition" gets a yes / no based on
  petition quality (F9) vs a yes / no based on whether the asker
  needs negotiating room with the current employer (F10).
- **F14 (pro-se) ↔ F2, F9 (route-optimality, evidentiary-bar)**. F14's
  consumer-rights confidence in pro-se filings clashes with F2's
  route-velocity preference (procedural defects from pro-se filings
  can restart cycles that route-velocity arithmetic ignores) and with
  F9's evidentiary-portfolio discipline (an EB-1A pro-se filing
  rarely meets the comparable-evidence pattern that adjudicators
  expect). The opposing framings should both be surfaced when an
  asker proposes a complex self-petition pro-se.

## Notes for downstream layers

- **Blindspot anchors** (forward-pointer to `blindspots.md`): every
  `Excludes` bullet above is a Layer 3 candidate. Highest-density
  candidates are framings 1 (status-continuity — out-of-status vs
  unlawful-presence distinction; automatic-extension reliance traps),
  4 (dual-intent — visa-stamp expiration during AOS; 245(k)
  under-use), 5 (AC21 — SOC literalism on promotions; cooperative-
  employer assumption), 6 (CSPA — formula category-variance;
  sought-to-acquire window confusion), 9 (evidentiary-bar — adjudicator
  political-administration calibration; template-letter trap), and
  13 (consular-vs-COS — consulate-specific refusal patterns; 90-day-
  rule literalism; administrative processing at consulate). Sweep all
  14 framings × ~4 bullets each = ~56 blindspot candidates; promote
  ≥ 5 per framing into `blindspots.md` per the
  [`_schema.md`](../_schema.md) minimum.
- **High-stakes posture (Mechanism E)**: this file is decision-support,
  not legal advice. Editor on any answer that lands on these framings
  must (per `domain_pack.md` once authored) explicitly label output as
  "decision-support; consult licensed immigration counsel for case-
  specific facts." Critic must apply stricter grounding on
  citation-bearing claims (statute, CFR section, USCIS Policy Manual
  reference) — generic "the law says X" claims unanchored to a cite
  should fail Critic review.
- **Triage routing notes**: framings 5, 6, 9 carry the most
  distinctive vocabulary signatures (AC21 §106(c), CSPA-formula,
  Kazarian-two-step) and should be high-confidence routing matches.
  Framings 1 and 14 share vocabulary with general administrative-
  procedure topics (extensions, forms, USCIS) and will need
  disambiguation against adjacent domain packs once V2 two-pass
  Triage is wired.
- **Cross-domain edges from `decisions.md`**: F10 (visa-as-employer-
  leverage) is the principal cross-domain framing into `tech-career`
  (comp negotiation, layoff response). F11 (marriage-good-faith) is
  the principal cross-domain framing into `family-planning` (marriage
  decision itself). F8 (dependent-status-coupling) routes into
  `health-insurance` on coverage-on-spousal-status-lapse. Triage should
  surface these adjacencies when the user's situation spans both
  domains.
