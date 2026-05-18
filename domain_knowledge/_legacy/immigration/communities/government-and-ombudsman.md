# Government and Ombudsman

The authoritative-document voice — USCIS's binding policy manual, the
DHS Ombudsman's annual reports to Congress, and the DOL Office of
Foreign Labor Certification's regulatory bulletins. This community is
a SOURCE of ground-truth eligibility criteria, systemic-issue data,
and procedural rules; it is **not a substitute** for case-specific
licensed-counsel advice on whether a particular asker's facts meet a
criterion or qualify for an exception. The Policy Manual states the
rule the adjudicator is supposed to apply; the attorney engagement is
where the rule meets the asker's full filing history.

## Voice

Formal, statutory, depersonalized. The USCIS Policy Manual reads like
a regulation: definitions, numbered subsections, cross-references to
8 CFR and INA citations, dated revision notices at the top of each
chapter. The CIS Ombudsman annual reports read like a policy white
paper: data tables, recurring-issue case studies, recommendations
USCIS has accepted-implemented-or-rejected, and a year-over-year
comparison of processing times. DOL OFLC bulletins read like trade
notices: prevailing-wage methodology updates, PERM filing schedule
changes, BALCA decision summaries, H-2A / H-2B program announcements.
None of this voice is hortatory; none is reassuring. The voice's job
is to be correct on the rule, the rate, and the date.

## Voice anchors

- Source-views from `immigration/sources.yaml` under this community_tag:
  - `uscis-policy-manual` — USCIS Policy Manual (static_corpus; the
    binding adjudicative reference; Volumes 6, 7, 12 cover the
    high-traffic chapters)
  - `uscis-ombudsman-reports` — CIS Ombudsman Annual Reports to
    Congress (static_corpus; systemic-issue evidence, processing-time
    data with provenance, USCIS responsiveness patterns)
  - `dol-flag-updates` — DOL Office of Foreign Labor Certification
    (FLAG) updates (RSS; PERM processing queue, prevailing-wage
    rules, LCA requirements, BALCA decisions)
- Adjacent named anchors: USCIS Policy Manual update tracker at
  uscis.gov/policy-manual/updates; CIS Ombudsman office at
  dhs.gov/topic/cis-ombudsman; DOL OFLC Performance Data and prevailing-
  wage determination history.

## Mental model

- The Policy Manual is the binding adjudicative reference; what an
  adjudicator does in practice should track what the Policy Manual
  says. Where it doesn't, the Ombudsman's annual report names the
  divergence and reports it to Congress.
- Each immigration benefit is administered by a specific agency at a
  specific stage: DOL adjudicates PERM and prevailing wage; USCIS
  adjudicates I-140, I-485, naturalization, and most of the
  nonimmigrant petitions; DOS sets the Visa Bulletin and adjudicates
  consular processing; CBP inspects at the port of entry; ICE handles
  removal. The handoffs are where things break.
- Processing times have a published "case processing times" tool
  (uscis.gov/processing-times) reflecting average completion at the
  service-center level; the Ombudsman reports document the cases that
  blow the average and the systemic issues behind them.
- Volumes of the Policy Manual are versioned and dated; updates are
  posted with effective dates. Any blog or forum citing "the Policy
  Manual says" without a volume / chapter / date is uncalibrated.
- DOL's PERM clock is upstream of every employment-based GC timeline;
  the prevailing-wage determination is upstream of the LCA which is
  upstream of the H-1B petition. The OFLC backlog ripples downstream
  into USCIS volume.

## Characteristic vocabulary

- "USCIS Policy Manual Volume X Part Y Chapter Z", "PM revision dated
  YYYY-MM-DD", "PM-2023-XXXX"
- "8 CFR §204.5(e)", "8 CFR §214.2(h)(9)(iv)", "INA §245(a) / §245(c) /
  §245(i) / §245(k)", "INA §214(b) presumption"
- "CIS Ombudsman recommendation accepted / partially accepted /
  rejected", "annual report to Congress for FY-YYYY", "systemic
  issue case study"
- "DOL OFLC FLAG (Foreign Labor Application Gateway)", "PERM ETA Form
  9089", "prevailing wage determination (PWD)", "Form ETA-9141",
  "LCA Form ETA-9035", "BALCA decision summary"
- "Service-center performance data", "USCIS receipt-to-completion
  pendency", "median vs 80th-percentile processing time"
- "Final Rule effective YYYY-MM-DD", "Federal Register notice citation"

## Known blind spots OF this community

- **Authoritative-document voice mistaken for adjudicator behavior.**
  The Policy Manual states the rule; service centers apply it
  inconsistently. The same I-140 with the same evidentiary profile
  draws an RFE in Nebraska Service Center 2020 and an approval in
  Texas Service Center 2022 — the Manual is silent on this variance
  because the Manual is the rule, not the application. Trigger: an
  asker pastes a Policy Manual sentence into a planning document and
  concludes "USCIS will rule X" because the Manual says X. Failure
  mode: the asker treats Policy Manual citation as adjudication
  prediction; the actual filing draws an RFE pattern the practitioner-
  forum sources would have flagged; the asker is unprepared for the
  RFE-response cycle because the Manual reading was treated as legal
  advice rather than as decision-support input. Recovery: read the
  Policy Manual chapter alongside an AILA practice advisory or
  practitioner-forum thread (this community ↔ `practitioner-forums`
  cross-check) to surface service-center variance; for any substantive
  filing, consult a licensed immigration attorney who has caseload
  data on the specific service center the petition will route to.

- **Annual cadence vs real-time policy churn.** The Ombudsman annual
  reports are exactly that — annual. A May-published report covers
  FY ending the prior September. The 2018 F/J/M unlawful-presence
  memo, the 2022 L-2S automatic-work-authorization rule, the
  February 2023 CSPA sought-to-acquire update, the late-2024
  I-693 indefinite-validity rule, and the 2024 H-1B beneficiary-
  centric registration rule all post on USCIS-direct channels
  (policy-alert page, press releases) months before the Ombudsman's
  annual narrative catches up. Trigger: an asker reads an Ombudsman
  report from FY-N and treats its narrative as current operative
  policy at FY-N+1. Failure mode: the asker's filing strategy is
  built on a regime that was modified six months ago; the petition
  reaches the adjudicator under different rules than the Ombudsman
  report assumed. Recovery: cross-check every Ombudsman citation
  against the USCIS policy-alert page (uscis.gov/policy-manual/updates)
  and, for any time-sensitive filing decision, confirm current
  operative policy with a licensed immigration attorney.

- **Inter-agency handoff gaps invisible to single-agency documents.**
  DOL approves the PERM; USCIS approves the I-140; DOS issues the
  visa or USCIS approves the AOS; CBP inspects at the port; if
  consular processing, DOS conducts the interview; if administrative
  processing kicks in, DOS routes the case through FBI / agency
  clearance with no fixed timeline. Each agency's documents describe
  its own piece; the handoff failures (a CBP secondary inspection
  on an AP-approved return, a DOS Section 221(g) administrative
  processing limbo, a USCIS finding that overrides DOL's PERM
  approval on substantive grounds) are systemic but rarely
  documented in any single agency's authoritative output. Trigger:
  an asker plans a CP trip based on a USCIS I-140 approval and a
  DOS visa-availability reading, without modeling the CBP re-entry
  inspection or the DOS administrative-processing risk. Failure mode:
  the asker is stuck abroad in 221(g) administrative processing for
  3–18 months, or paroled-in but referred to ICE secondary inspection,
  with the Policy Manual / Ombudsman reading silent on the handoff
  risk. Recovery: for any cross-agency filing pathway (CP, AP travel,
  consular renewal during AOS pendency), the inter-agency risk is a
  practitioner-knowledge question that benefits from licensed
  immigration counsel familiar with the specific consulate's CBP /
  ICE referral patterns.

- **Policy-administration calibration absent from authoritative
  voice.** The Policy Manual is not the place where the political
  administration's enforcement posture is documented. RFE rates on
  EB-1A petitions varied 2–3× between 2017 and 2023 (per
  `framings.md` §9 Excludes; `blindspots.md` §9.1); the Manual chapters
  did not materially change during this swing. The Ombudsman reports
  do document recurring RFE patterns but lag the year. Trigger: an
  asker calibrates expected RFE-likelihood by reading the Policy
  Manual's EB-1A criteria as if they were a steady-state checklist.
  Failure mode: an EB-1A petition strong-by-Policy-Manual-criteria
  is filed during a high-scrutiny adjudication cycle and draws an
  RFE the asker hadn't planned to respond to; the response window
  (87 days) closes before the asker assembles the supplementary
  evidence the criteria don't strictly require but the current
  adjudicator cohort expects. Recovery: pair Policy Manual reading
  with current-year practitioner-forum RFE-pattern reporting
  (community ↔ `practitioner-forums`); for high-stakes self-petition
  filings, consult a licensed immigration attorney who tracks current-
  administration RFE-rate trends and adjudicator-cohort signals.

- **Authoritative reading mistaken for legal advice.** A reader can
  open the Policy Manual, read INA §245(k), read 8 CFR §245.1, and
  conclude "my facts qualify" — the documents are public, the
  language is in English, the reasoning is traceable. The reader
  is, however, not licensed to practice law and is reasoning under
  asymmetric information about case-specific facts the documents do
  not anticipate (prior unlawful-presence accrual, prior 214(b)
  refusal, prior order of removal, prior fraud determination, prior
  misrepresentation under §212(a)(6)(C)). Trigger: an asker who has
  read the Policy Manual chapter end-to-end and concluded their
  filing posture is correct on the law. Failure mode: the asker
  self-files based on a pro-se reading of the Manual that misses a
  case-specific bar (e.g. the §245(c)(2) unauthorized-employment bar
  that disqualifies the EB-based filer 245(k) does not cure for the
  family-based filer); the filing is denied, the fee is non-refundable,
  and the denial creates an adverse adjudication record that follows
  every subsequent filing. Recovery: treat Policy Manual self-reading
  as decision-support orientation — useful for understanding what is
  being adjudicated and what evidence is needed — but never as a
  substitute for case-specific licensed-counsel advice; the binding
  determination on whether the asker's facts meet a Policy Manual
  criterion is the attorney's job.
