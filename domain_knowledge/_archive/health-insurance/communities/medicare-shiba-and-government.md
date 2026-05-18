# Medicare SHIBA and Government

State Health Insurance Assistance Program (SHIP / SHIBA) counselor +
Medicare.gov + CMS bulletin voice — the federally-funded, non-
commissioned, plan-agnostic Medicare-enrollment counseling network
operating under SSA §4360, paired with the regulatory ground-truth
publishers (CMS Medicare & You handbook, MLN Matters articles, CMS
Manual System). This community is the **Mechanism E anchor for D4
and D8 specifically** — Medicare-timing decisions where the IEP /
GEP / SEP windows, Part B Late Enrollment Penalty (10% per 12-month
period, permanent, cumulative), and the 6-month Medigap Guaranteed-
Issue window after Part B effective date carry irreversible
consequences. The blog post or handbook tells you the rule; the SHIP
counselor with the asker's specific birthdate, current coverage
status, and chronic-condition profile is where the decision happens.

## Identity

State-by-state SHIP / SHIBA volunteer counselors trained under the
SHIP National Technical Assistance Center curriculum (federally
funded via SSA §4360 and ACL grants, administered through state
units on aging), plus the CMS / Medicare.gov publication apparatus
(the *Medicare & You* annual handbook, the Medicare Plan Finder web
application, MLN Matters provider-education articles, and the
CMS-12036-N annual final rule). They reason about Medicare as a
statutorily-irreversible enrollment-timing problem: Part A premium-
free for most enrollees at 65 but with quality-credit eligibility
rules; Part B with permanent LEP for late enrollment without
qualifying coverage; Medigap with a one-shot 6-month GI window
during which insurers cannot underwrite, after which underwriting is
generally permitted and chronic-condition applicants are routinely
declined; Part D with its own 1%-per-uncovered-month permanent LEP.
They are *not* the broker community — counselors are explicitly
non-commissioned, plan-agnostic, and structurally counterweight to
broker MA-commission steering.

## Voice anchors

- Source-views from `health-insurance/sources.yaml` under this
  community_tag:
  - `medicare-gov-and-cms-bulletins` — Medicare.gov + CMS bulletins
    (*Medicare & You* annual handbook, MLN Matters, CMS Manual
    System chapters on enrollment timing and LEP calculation).
  - `ship-state-resources` — state SHIP / SHIBA published consumer
    brochures, Medigap-rate-comparison spreadsheets, Extra Help /
    MSP eligibility worksheets, SHIP National Technical Assistance
    Center training modules.
- Adjacent named voices / outlets: Medicare Rights Center (national
  consumer-advocacy organization, also publishes the *Medicare
  Watch* newsletter and operates the consumer helpline); Center for
  Medicare Advocacy (legal-advocacy nonprofit, files §1395ff appeal
  amicus briefs); Justice in Aging (low-income elder advocacy);
  Medicare Interactive (Medicare Rights Center's online consumer
  guide); SHIP National Technical Assistance Center counselor-
  training documentation; *Generations* and *American Society on
  Aging* publications.

## Mental model

Medicare enrollment is a one-shot timing problem with permanent
consequences on the downside, governed by a fixed schedule of
windows: the 7-month Initial Enrollment Period straddling the 65th-
birthday month (three months before, the birthday month, three
months after); the General Enrollment Period (Jan 1 – Mar 31 each
year for those who missed IEP, with Part B effective July 1 of that
year and a 10% LEP accruing from each full 12-month period of
late enrollment); Special Enrollment Periods triggered by loss of
qualifying employer coverage (SSA §1837(i), 8-month window from
coverage end); the Annual Election Period (Oct 15 – Dec 7) for MA /
Part D changes; the Medicare Advantage Open Enrollment Period (Jan 1
– Mar 31) for one MA-to-MA or MA-to-Original-Medicare switch; and
the Medigap Guaranteed-Issue 6-month window starting Part B
effective date during which insurers cannot underwrite or charge a
preexisting-condition rate-up. Counselors reason out of *the
asker's actual current coverage status* — "do you have qualifying
employer coverage, is it from an employer of 20+ or <20, are you
covered as an active employee or a retiree, what is your spouse's
status" — because the SEP triggers and the LEP exposure both depend
on these facts. The MA-vs-traditional-Medicare decision is framed
as a *future-state robustness* problem: traditional + Medigap costs
more upfront and trades that for unrestricted-network and no-prior-
auth access if a chronic condition develops; MA costs less upfront
and trades that for prior-auth and network constraints that bind
later. The Medigap GI window is the decision's irreversibility
lever.

## Characteristic vocabulary

- "IEP" (Initial Enrollment Period), "GEP" (General Enrollment
  Period), "SEP" (Special Enrollment Period), "AEP" (Annual
  Election Period), "MA-OEP" (Medicare Advantage Open Enrollment
  Period)
- "Part B LEP" (Late Enrollment Penalty, 10% per 12-month period,
  permanent and cumulative), "Part D LEP" (1% of national base
  beneficiary premium per uncovered month, also permanent)
- "Medigap GI window" (Guaranteed-Issue, 6 months from Part B
  effective date, 42 USC §1395ss-1(b)), "open enrollment for
  Medigap", "underwriting" (post-GI window)
- "Creditable coverage" (Part D), "qualifying employer coverage"
  (Part B SEP trigger), "employer of 20+ vs <20" (primary vs
  secondary payer determination), "active vs retiree coverage"
- "Plan Finder" (Medicare.gov Medicare Plan Finder), "formulary
  snapshot" (Plan Finder shows current-year formulary; 60-day mid-
  year change notice for non-protected classes)
- "Extra Help" / "LIS" (Low-Income Subsidy for Part D), "MSP"
  (Medicare Savings Program — QMB / SLMB / QI), "state buy-in"
- "Medicare Advantage RAF score" (risk adjustment factor), "STARS
  ratings", "supplemental benefits", "MOOP" (Maximum Out-of-
  Pocket, MA-specific)
- "QIC" (Qualified Independent Contractor, Medicare appeal level
  2), "ALJ" (Administrative Law Judge, level 3), "MAC" (Medicare
  Appeals Council, level 4)

## Known blind spots OF this community

- **State-by-state Medigap-pricing variance is documented but
  rarely surfaced in the moment of decision.** SHIP / SHIBA
  publishes the state rate sheets, but the asker on a national
  Medicare.gov call doesn't necessarily get routed to local SHIP in
  time to use them. Same NAIC Plan G can run $130/month in one
  state and $280/month in another for the same 65-year-old applicant;
  carrier and rating method (attained-age vs issue-age vs community-
  rated) drive 20-year cost trajectories that diverge by tens of
  thousands. Trigger: a Medicare.gov general-audience post
  recommending "compare Medigap quotes from at least 3 carriers"
  without naming the state-specific SHIP rate-sheet resource.
  Failure mode: the asker buys the first Medigap plan a captive
  agent quotes, locked into an attained-age plan in a state where
  community-rated alternatives existed; 15 years later premium has
  doubled relative to the community-rated option. Recovery: route
  to local SHIP / SHIBA for the state's published rate sheet *during
  the 6-month GI window*, before the irreversibility binds.

- **Extra Help / MSP under-enrollment is a known systemic
  blindspot the community itself names but cannot fix.** Roughly
  a third of Medicare beneficiaries eligible for Extra Help (LIS)
  or one of the Medicare Savings Programs (QMB / SLMB / QI) are
  not enrolled — they qualify on income (135–150% FPL bands) but
  never applied. Trigger: an asker on D8 (post-65 with limited
  income / assets) whose SHIP counselor is over-booked during AEP
  and the eligibility-screen conversation is rushed. Failure mode:
  the asker pays full Part B premium ($174.70+/month at authoring)
  out of a fixed income that would have qualified for state buy-in
  paying it entirely; the asker also pays Part D out of pocket for
  prescriptions Extra Help would have subsidized at $0 / $1.45 /
  $4.50 tiers. Recovery: explicit MSP / Extra Help eligibility
  screen at every D4 / D8 conversation; use SSA's "Apply for Extra
  Help with Medicare Prescription Drug Plan Costs" form (SSA-1020)
  as the trigger.

- **Plan Finder formulary-snapshot caveat is in the documentation
  but not in the workflow.** The Medicare Plan Finder shows the
  *current-year* formulary at the moment of search; plans can
  change formulary mid-year with 60-day notice for non-protected
  drug classes, and AEP-period Plan Finder data describes the
  upcoming plan year. The asker who shops AEP in November, picks
  a Part D / MA-PD plan based on a specialty-tier drug being on
  formulary, and discovers in June the drug has been moved to a
  non-formulary tier with 60-day notice has no Mid-Year Switch
  remedy outside narrow MA-OEP (Jan 1 – Mar 31) and SEP
  categories. Trigger: AEP Plan Finder workflow that ends at
  "this plan covers your drugs"; counselor does not name the
  60-day-notice possibility. Failure mode: mid-year non-formulary
  move; asker pays cash for the drug or step-therapy-substitutes
  to a clinically-inferior alternative. Recovery: include the
  formulary-change-risk conversation in the Plan Finder workflow;
  for chronic-condition askers on specialty-tier drugs, prefer
  Part D plans with a track record of formulary stability and
  protected-class membership (anti-cancer, HIV, immunosuppressants,
  antipsychotics, anticonvulsants).

- **MA-OEP window is the only meaningful escape hatch from a bad
  MA election, and it's underused.** The Medicare Advantage Open
  Enrollment Period (Jan 1 – Mar 31 each year) permits *one*
  MA-to-MA switch or one MA-to-Original-Medicare switch, but the
  Medigap GI window does NOT generally re-open at that point —
  meaning the asker who switches from MA to Original Medicare in
  February still faces Medigap underwriting (state-specific
  exceptions exist: CT, MA, ME, NY have year-round Medigap GI;
  CA / OR / MO have "birthday rules"). Trigger: SHIP counselor
  who frames MA-OEP as a clean reset without naming the Medigap
  underwriting question. Failure mode: the asker switches off MA
  in February, applies for Medigap, is underwritten-out for
  chronic conditions, ends up on Original Medicare with no
  Medigap (20% Part B coinsurance with no OOP cap, unbounded
  catastrophic exposure). Recovery: before MA-OEP move, confirm
  the asker's state's Medigap GI posture; in non-GI-friendly
  states, screen for underwriting-likelihood before initiating
  the switch.

- **Medicare-Advantage prior-auth and post-acute denial pathology
  is documented in journalism but counselors are constrained
  from giving plan-specific warnings.** SHIP / SHIBA counselors
  are bound by plan-agnostic training; they cannot say "avoid
  this specific carrier's MA plan because their NaviHealth /
  naviHealth SNF-denial pattern is documented." Trigger: ProPublica
  has the documented body of work on UnitedHealthcare /
  NaviHealth's MA SNF denial algorithm (per `sources.yaml`
  community `healthcare-economics-journalism`,
  `propublica-health-care` source-view), but the SHIP counselor's
  framing remains "all MA plans have prior auth, read the
  Evidence of Coverage." Failure mode: the asker enrolls in a
  specific MA plan with high SNF-denial rates, hits a hip
  fracture at 78, and discovers the post-acute SNF approval has
  been declined at day 14 of a clinically-warranted 30+ day
  stay. Recovery: cross-reference plan choice against
  journalism-side reporting (`sources.yaml` community
  `healthcare-economics-journalism`); for the post-acute appeal
  itself, route to NAHAC / patient-advocate channels (`sources.yaml`
  community `patient-advocacy-and-billing-recovery`).

- **Cross-domain immigration boundary is rarely surfaced.** Non-
  citizen Medicare-eligibility (lawful permanent residents must
  have 5 years of LPR status to enroll; non-LPRs can buy in under
  narrow conditions; some immigrant categories are categorically
  ineligible) and mixed-status household Medicaid interactions are
  documented at the policy-research layer but rarely make it into
  the SHIP D8 conversation. Trigger: an LPR turning 65 who
  doesn't have 5 years of US residence yet; spouse is citizen on
  Medicare. Failure mode: asker delays Part B enrollment under a
  misreading of the SEP rule, accrues LEP, or enrolls without
  understanding the premium-Part-A buy-in pricing. Recovery: at
  any D8 conversation with cross-domain immigration facts, route
  to a counselor with immigration-status literacy or to a
  Medicare Rights Center helpline conversation with the asker's
  full status timeline.

## Mechanism E posture

Health-insurance is `high_stakes: true` per `_meta_ontology.md` §4.
Every blindspot above ends with a Recovery move routed to a named
professional channel. For medicare-shiba-and-government-sourced
framings the default channel is a **SHIBA / SHIP counselor for
Medicare timing decisions (D4 and D8)** — non-commissioned, plan-
agnostic, federally-funded under SSA §4360 and ACL grants. The
counselor is structurally the counterweight to broker MA-commission
steering and is the named professional for the irreversibility
levers (Part B IEP, Medigap GI 6-month window). Where the decision
crosses into post-acute-care / SNF denial appeals, Mechanism E re-
routes to a **patient-advocate channel** (NAHAC,
`sources.yaml` community `patient-advocacy-and-billing-recovery`);
where the decision crosses into ALJ-level appeals (Medicare appeal
level 3), to **Center for Medicare Advocacy** or a Medicare-side
attorney. This community is the timing-and-rule layer; the named
professional with the asker's specific birthdate, coverage status,
and chronic-condition profile is the binding-determination layer.
