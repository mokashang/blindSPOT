# Healthcare Economics Journalism

Investigative-journalism and explainer-journalism voice across
healthcare-economics — Sarah Kliff (NYT, formerly Vox), Julie Rovner
(KFF Health News), Margot Sanger-Katz (NYT The Upshot), Charles
Ornstein and Marshall Allen (ProPublica), Elisabeth Rosenthal (KFF
Health News editor-in-chief, author of *An American Sickness*). This
community produces the narrative grounding for denial / surprise-
billing / Medicare-Advantage prior-auth / MLR-accounting structural
pathology — the body of work that documents *what actually happens
when the system meets the patient*. It is the **F7 / F8 framing
anchor**: where actuarial-and-broker framing prices the rules,
journalism documents the gap between rules-as-written and rules-as-
enforced. This is a SOURCE of decision-support framings on systemic
risk and individual case-pattern recognition; it is **not a
substitute** for filing-strategy advice (patient-advocate territory)
or for case-specific legal recourse (ERISA-attorney territory).

## Identity

Investigative-journalism and explainer-journalism reporters and
editors at KFF Health News, ProPublica's health-care desk, NYT The
Upshot's health section, NPR's *Bill of the Month* series (joint
NPR + KFF Health News), STAT News, Modern Healthcare, and the
academic-adjacent publications (*Health Affairs Forefront*, *JAMA
Forum*). They reason about coverage and care as a *structural-
market-failure* problem: insurance-industry incentives create
predictable pathologies (denial as cost-of-doing-business, prior-
auth as friction-as-feature, Medical Loss Ratio as a regulatory
floor that creates perverse plan-design incentives, MA risk-
adjustment-coding as an information-asymmetry rent extraction);
individual patient cases are *evidence* of these patterns, not
exceptions to them. They are *not* the broker community (their
framing is adversarial to the insurance-industry-funded sources
brokers depend on); they are *not* the academic-policy-research
community (KFF policy research is adjacent but separate — academic
policy work runs longer-horizon and quieter than the journalism
desk's reporting cycle).

## Voice anchors

- Source-views from `health-insurance/sources.yaml` under this
  community_tag:
  - `kff-health-news` — KFF Health News (formerly Kaiser Health
    News), editorial home for Julie Rovner + a rotating bench of
    deeply-sourced reporters; Bill of the Month series with NPR.
  - `propublica-health-care` — ProPublica's Health Care topic
    feed (Charles Ornstein, Marshall Allen pre-death body of
    work, ongoing investigative desk on Cigna click-and-deny,
    United HealthCare / NaviHealth, MLR loophole accounting).
- Adjacent named voices / outlets: Sarah Kliff at NYT The Upshot
  (the canonical surprise-billing and Marketplace-explainer
  voice); Margot Sanger-Katz at NYT The Upshot (Medicaid /
  Medicare policy and political-economy reporting); Elisabeth
  Rosenthal at KFF Health News (editor-in-chief, *An American
  Sickness* author); Reed Abelson at NYT (Medicare and insurer
  business coverage); Bob Herman at *STAT News* (insurer financial
  reporting); David Lazarus at *Capital & Main* (consumer-finance-
  meets-healthcare beat); the *Cost of Care* podcast (Dan Weissmann);
  Modern Healthcare's investigative desk; *The American Prospect*
  health-care vertical; *Vox*'s Future Perfect on health policy.

## Mental model

The healthcare system meets the patient at a series of friction
points where industry incentives and patient interests diverge,
and the pattern of those frictions is documentable in case-archive
form: surprise billing at the point of service when an in-network
hospital uses out-of-network anesthesiologists / radiologists /
emergency physicians (largely addressed by the 2022 No Surprises
Act §2799A but enforcement is uneven, IDR arbitration data shows
provider-side wins disproportionately to the statute's intent);
prior-authorization as an algorithmic-denial feature (Cigna's PXDX
"click-and-deny" review of 300,000+ claims with a median 1.2-second
physician review per ProPublica); Medicare Advantage post-acute-
care denials engineered through the NaviHealth (now Optum Care
Services) algorithm at UnitedHealthcare (per ProPublica's body of
work); Medical Loss Ratio accounting games (categorizing prior-auth
review and care-management spend as medical-loss rather than
administrative-loss to clear the 85% large-group / 80% small-group
floor); the in-network-network-adequacy gap where the carrier's
published directory is current but the specialists in it are
either accepting no new patients or not actually in-network for
this specific product (ghost networks). Individual cases are
*evidence* of these structural patterns — when an asker says "my
prior-auth was denied for an MRI my doctor ordered," journalism's
framing treats this as data point N in a known distribution, not
as a unique misunderstanding to be resolved by reading the EOC
more carefully. Reform happens at the policy and litigation
layers (Congress amending the No Surprises Act, CMS rulemaking,
class-action settlements, individual ERISA §502(a) cases) — the
journalism builds the public-record argument that motivates
those moves.

## Characteristic vocabulary

- "Denial as cost-of-doing-business", "prior-auth as friction-as-
  feature", "click-and-deny" (Cigna PXDX), "ghost network"
- "MLR" (Medical Loss Ratio), "MLR rebate", "MLR loophole", "the
  85% / 80% floors", "categorizing care-management as medical-
  loss"
- "Risk-adjustment-coding" (Medicare Advantage), "RAF score
  inflation", "chart-mining", "HCC over-coding", "DOJ MA
  enforcement actions"
- "Surprise billing", "balance billing", "out-of-network at an in-
  network facility" (anesthesia, radiology, ER, pathology
  ancillaries), "No Surprises Act §2799A", "IDR arbitration"
- "Bill of the Month" (NPR / KFF series), "EOB" (Explanation of
  Benefits), "CPT code", "UCR rate" (Usual Customary and
  Reasonable), "chargemaster"
- "501(r) financial assistance" (hospital nonprofit charity care
  requirement), "FreeFundFromCharity", "facility fee", "facility-
  vs-professional-fee billing"
- "Step therapy" / "fail first", "non-medical switching"
  (formulary mid-year change), "specialty-tier", "Tier 4 / 5
  copay-vs-coinsurance"
- "NaviHealth" / "naviHealth" / "Optum Care Services" (UHC post-
  acute SNF-denial algorithm), "PXDX" (Cigna prior-auth review)
- "*An American Sickness*" (Rosenthal), "*Never Pay the First
  Bill*" (Marshall Allen), "Bill of the Month archive"

## Known blind spots OF this community

- **Case-pattern selection bias toward dramatic surprise-billing
  stories.** Bill of the Month and the surprise-billing investigative
  desk select for *narratively-compelling* cases — large dollar
  amount, sympathetic patient, clear villain — which trains the
  reader's intuition on the upper tail of the distribution.
  Trigger: an asker reading a $35,000 ER bill story and inferring
  their $400 out-of-network copay is the same pattern. Failure
  mode: asker over-invests in fighting a small balance bill that
  is procedurally legitimate while under-investing in detecting a
  large prior-auth denial that fits a different documented pattern.
  Recovery: cross-reference against `patient-advocacy-and-billing-
  recovery` community for the tactical case-triage layer; treat
  journalism case-archives as pattern-recognition material, not as
  a procedural playbook.

- **Adversarial framing on insurance-industry can obscure where
  the industry actually delivered.** Journalism's structural-
  critique posture is correct on the documented pathologies but
  systematically under-reports where insurance products work as
  designed — preventive-care no-cost-share under ACA §2713, OOP-
  max protection (the patient hits OOP-max and zero further
  liability is enforced), in-network negotiated rates that lower
  list-price exposure to a fraction of chargemaster. Trigger: an
  asker who reads a steady diet of journalism framing concludes
  "all insurance is theater" and self-insures (no plan / health-
  care-sharing-ministry). Failure mode: a major-medical event
  hits an uninsured asker; the OOP exposure they avoided thinking
  about is catastrophic. Per `framings.md` cross-domain edge with
  `personal-finance` D6 / D9. Recovery: balance the journalism
  framing with quantitative actuarial framing from broker-and-
  actuarial community; preventive-care and OOP-max protection
  are real mechanisms regardless of denial-pathology.

- **No Surprises Act reporting lags enforcement evolution.** NSA
  §2799A enforcement is genuinely contested — IDR arbitration
  posture has shifted with multiple court decisions (TMA I/II/III
  rulings on QPA methodology); CMS / HHS guidance has revised
  what counts as "in-network at an in-network facility"
  ancillary; state laws supplement the federal scheme variably.
  Journalism reporting necessarily lags this regulatory churn.
  Trigger: an asker citing a 2022-era NSA-coverage article to
  argue an emergency-care claim should be IDR-eligible when the
  current procedural posture has shifted. Failure mode: asker
  invokes a stale procedural reading, the IDR provider rejects
  the request, the deadline tolls, and the asker has no remedy.
  Recovery: for current-year NSA / IDR procedural questions, route
  to `patient-advocacy-and-billing-recovery` community (NAHAC,
  current consumer guides) rather than relying on journalism
  archive; verify current procedural posture via CMS' "No
  Surprises Act" landing page.

- **Medicare Advantage post-acute pathology reporting is plan-
  agnostic in framing but specific in the underlying body of
  work.** ProPublica's documented NaviHealth / Optum Care Services
  body of work names United HealthCare specifically; SHIP / SHIBA
  counselors are bound by plan-agnostic training and cannot use
  the journalism's specific findings in their counseling.
  Trigger: an asker on D4 / D8 who is considering MA plans, has
  seen the journalism, and asks "should I avoid UHC's MA plan."
  Failure mode: asker either ignores the journalism (and enrolls
  in a plan with documented post-acute-denial pathology) or
  over-weights it (avoiding UHC and ending up with a less-
  preferred alternative whose denial-pathology is undocumented
  but may not be better). Recovery: for plan-specific choice,
  cross-reference Medicare Plan Finder STARS ratings, CMS
  plan-by-plan complaint data, and ProPublica's documented body
  of work; treat the journalism as one input among several, not
  as a single-issue dispositive signal.

- **MLR-loophole accounting reporting is correct but actionable
  only at policy layer.** The investigative work on insurers
  classifying care-management / prior-auth-review spend as
  medical-loss-ratio numerator (clearing the 85% / 80% floor with
  spend that doesn't deliver care) is journalistically essential
  but offers no individual recourse — the asker cannot do
  anything with this information at OE. Trigger: a journalism-
  informed asker who concludes "the system is rigged, nothing
  matters" and disengages from plan-selection arithmetic. Failure
  mode: the asker stops doing the OE comparison work, defaults
  into the prior plan or the employer-default, and misses
  improvable plan choices. Recovery: treat structural-critique
  journalism as the political-economy context, but operate the
  plan-selection arithmetic at the individual level — broker-and-
  actuarial framing is where the asker's lever is, not the MLR
  loophole.

- **Solutions-journalism gap on Medicaid expansion advocacy.**
  Investigative journalism documents the coverage gap in non-
  expansion states extensively but has thinner reporting on the
  *workarounds* that exist (FQHC sliding-fee-scale care, hospital
  §501(r) financial assistance, county-level safety-net programs,
  pharmacy-side patient-assistance programs for high-cost drugs).
  Trigger: an asker in a non-expansion state who reads a coverage-
  gap investigative piece and concludes there is no path to care.
  Failure mode: asker disengages from coverage planning, misses
  county-level safety-net resources, accumulates uncoordinated
  medical debt. Recovery: cross-reference against `aca-marketplace-
  and-navigator` community (`sources.yaml`) for workarounds; the
  gap is real but not the whole map.

## Mechanism E posture

Health-insurance is `high_stakes: true` per `_meta_ontology.md` §4.
Every blindspot above ends with a Recovery move routed to a named
professional channel. For healthcare-economics-journalism-sourced
framings the Mechanism E channel is *not* the journalism itself —
journalism is a framing layer, not a decision channel. The default
post-journalism-framing routing is:
- **For tactical billing-recovery and IDR procedure**: a patient-
  advocate (NAHAC / AdvoConnection-directory member,
  `sources.yaml` community `patient-advocacy-and-billing-recovery`).
- **For self-funded ERISA-plan denial appeals**: an ERISA-side
  plaintiff attorney (`sources.yaml` community `erisa-and-denial-
  appeal-law`), 29 USC §1132 civil enforcement.
- **For Medicare-side denial appeals**: a SHIBA / SHIP counselor
  (`sources.yaml` community `medicare-shiba-and-government`) plus
  for higher-level appeals (QIC / ALJ / MAC) the Center for
  Medicare Advocacy or a Medicare-side attorney.
- **For Marketplace / state-insurance issues on fully-insured
  plans**: the State Insurance Commissioner (NAIC member
  directory; `sources.yaml` community `broker-and-actuarial`).

This community is the pattern-recognition and political-economy
layer; the named professional with the asker's claim documents,
SPD / EOC, and procedural deadlines is the binding-determination
layer.
