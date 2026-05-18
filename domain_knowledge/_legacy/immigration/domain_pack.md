# immigration — domain_pack.md

Triage / Editor / Critic prompt overrides scoped to the `immigration`
domain, per [`_schema.md` §`domain_pack.md`](../_schema.md). Triage's
pass-2 concatenates this file into its system prompt when this domain
is active. Editor and Critic use the corresponding sections when the
situation routes here.

`immigration` is `high_stakes: true` per
[`_meta_ontology.md` §2](../_meta_ontology.md). Mechanism E gating
(per [ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating))
applies in full: Editor labels every answer "decision-support, not
legal advice" and explicitly defers binding determinations to a
licensed immigration attorney; Critic enforces stricter grounding on
every statutory / regulatory / USCIS-policy claim and treats unanchored
"the law says..." sentences as automatic fails. This is the core
posture difference from
[`tech-career/domain_pack.md`](../tech-career/domain_pack.md) — there
equity-tax claims carry locally-high-stakes grounding strictness but
the domain itself is recoverable; here the entire domain is
non-recoverable on a multi-year horizon. A wrong filing window, a
mistaken AP departure, or a §245(c) misclassification ripples into
every future adjudication.

Companion files: [`decisions.md`](./decisions.md) (D1–D10),
[`framings.md`](./framings.md) (F1–F14),
[`blindspots.md`](./blindspots.md),
[`sources.yaml`](./sources.yaml). Reference them; this file does not
restate their content.

---

## Triage

Pass-1 has already extracted generic `(domains, entities, risk_surfaces,
personas)` from [`src/blindspot/prompts/triage.md`](../../src/blindspot/prompts/triage.md).
Pass-2 with this domain active enriches that output with the
domain-specific facets below. The Pass-1 vocabulary stays the
authoritative ground set; Pass-2 adds and *sharpens*, never overwrites.

**Decision matching.** Identify the closest match from D1–D10 in
[`decisions.md`](./decisions.md) by the *Sample situations* under each
decision (those are written for this purpose). Emit it as
`matched_decision: "D<n>"`. Multiple-decision matches are allowed and
common in immigration — an H-1B-with-pending-I-140 asker considering
a job switch typically spans D1 (status-category change), D4 (AC21
portability), and D9 (self-petition route option). Emit a list ordered
by closeness. A genuinely ambiguous situation between two decisions is
a routing signal worth surfacing; do NOT collapse it.

**Persona refinement.** Pass-1 may have emitted a generic persona like
`visa-holder` or `green-card-applicant`. Replace with the most-specific
persona from this controlled list when the situation supports it:

- `f1-student-on-opt` / `f1-student-on-stem-opt` — F-1 in 12-month
  OPT vs 24-month STEM extension (D7)
- `h1b-cap-subject-pre-i140` — H-1B without approved I-140 (D1, D4)
- `h1b-with-approved-i140-backlogged` — I-140 approved, PD not current
  (D1, D3, D4, D6, D9)
- `h1b-near-six-year-cap` — H-1B year 5–6, AC21 §104(c) live (D1, D9)
- `l1-intracompany-transferee` / `o1-extraordinary-ability-holder` —
  L-1A/B and O-1A/B (D1, D9)
- `b1-b2-visitor-with-status-pivot` — visitor considering F-1 / H-1B
  (D8)
- `aos-applicant-with-pending-i485` — I-485 pending (D3, D4, D5)
- `marriage-based-petitioner-usc-spouse` /
  `marriage-based-petitioner-lpr-spouse` — IR vs F2A petitioner (D2)
- `h4-spouse-with-ead` / `h4-spouse-pending-ead-renewal` — H-4
  dependent with EAD active vs in renewal lag (D10)
- `self-petitioner-eb1a-candidate` / `self-petitioner-niw-candidate`
  — researcher / senior IC, Dhanasar fit (D9)
- `recently-terminated-on-h1b` — within 60-day grace (D1, D10)
- `child-aging-out-derivative` — CSPA-eligible (D2, D3, F6)

These are the personas the per-domain blindspot triggers in
[`blindspots.md`](./blindspots.md) are written against. Generic
persona labels will miss most triggers.

**Risk-surface vocabulary.** Replace generic `legal` / `timing` /
`status` / `family` from Pass-1 with the specific risk surfaces below
when the situation supports them. Each maps to one or more blindspots
in [`blindspots.md`](./blindspots.md); using the generic label loses
the routing:

- Grace / extension clocks: `60-day-grace-period`
  (8 CFR §214.1(l)(2)), `240-day-work-auth-extension`,
  `540-day-automatic-EAD-extension`, `EAD-renewal-gap`
- Cap / OPT mechanics: `H-1B-cap-lottery` (beneficiary-centric
  multi-registration, 2024+), `cap-gap-bridge`, `STEM-OPT-eligibility`
  (E-Verify + CIP-code)
- AC21 portability: `AC21-§106(c)-same-or-similar-SOC`,
  `AC21-§104(c)-three-year-extension`, `priority-date-retrogression`,
  `DFF-vs-FAD-divergence`, `CSPA-age-formula` (INA §203(h)),
  `cross-chargeability-via-spouse`
- Dual-intent + abandonment: `dual-intent-statutory` (H-1B / L-1 /
  O-1), `dual-intent-nonimmigrant-presumption` (INA §214(b) on F-1 /
  B-1 / B-2 / TN / J-1), `90-day-preconceived-intent` (DOS FAM),
  `AOS-abandonment-on-non-AP-departure`
- AOS eligibility / unlawful presence: `245(a)-eligibility`,
  `245(c)-bar`, `245(k)-180-day-aggregate-grace`,
  `212(a)(9)(B)-3-year-bar` (180+ days), `212(a)(9)(B)-10-year-bar`
  (365+ days), `222(g)-automatic-visa-voidance`
- Marriage-based: `bona-fide-marriage-evidence`,
  `conditional-PR-I-751`, `I-864-affidavit-of-support-obligation`
  (10-year), `public-charge-grounds` (INA §212(a)(4))
- Consular / re-entry: `consular-§214(b)-refusal-risk`,
  `consular-administrative-processing-221(g)`,
  `CBP-secondary-inspection-at-re-entry`
- Self-petition adjudication: `Kazarian-two-step-RFE`,
  `Matter-of-Dhanasar-three-prong`, `service-center-RFE-rate-variance`

If a Pass-1 risk surface generalizes into one of these, emit the
specific. If the situation supports a risk not in this list, emit it
as-is (the list is non-exhaustive; new entries should follow the same
specific-statute-or-mechanism naming rule).

**Framing-signal vocabulary.** Pass-2 also emits an optional
`active_framings` field — the F1–F14 framings from
[`framings.md`](./framings.md) the situation's vocabulary already
indicates the asker is reasoning inside. Match against each framing's
*Characteristic vocabulary*. This routes the Risk Officer to surface
the **opposing** framing's blindspots. The load-bearing oppositions
(per `framings.md` "Cross-framing tensions"):

- F1 (status-continuity) ↔ F2 (route-optimality) — "extend the H-1B
  again" reads F1; "self-petition EB-1A" reads F2. Same facts, opposite
  advice.
- F1 (status-continuity) ↔ F13 (consular-vs-COS) — "file COS now to
  lock status" reads F1; "fly home and consular-process to avoid
  90-day-rule scrutiny" reads F13.
- F9 (evidentiary-bar) ↔ F10 (visa-as-employer-leverage) — same EB-1A
  portfolio is a procedural input under F9 and a leverage instrument
  under F10.
- F14 (pro-se) ↔ F2 / F9 (route-optimality / evidentiary-bar) — pro-se
  filing optimism clashes with route-velocity and evidentiary-portfolio
  discipline.

The asker's framing is itself a blind spot — Triage emits the opposing
framing in `active_framings` even when the asker's vocabulary doesn't
match it, so the Risk Officer has the opposing surface to work from.

**Cross-domain routing flags.** When Pass-1 surfaces signals that imply
an adjacent domain, emit `cross_domain: [<slug>, ...]`. Immigration is
the densest cross-domain hub in the ontology after `career-pivots`; per
[`_meta_ontology.md` §"Cross-domain notes"](../_meta_ontology.md) the
most load-bearing edges are:

- Employer / comp / role / equity / layoff mentioned → add `tech-career`
  (D1, D4, D7, D9, D10 boundary `tech-career`)
- Marriage / fiancé / partner / divorce / custody mentioned → add
  `family-planning` (D2 boundary `family-planning`)
- COBRA / marketplace / Medicaid / spouse-coverage on status change →
  add `health-insurance` (D5, D10 boundary `health-insurance`)
- 401(k) / exit-tax / asset-allocation on stay-or-leave-the-US
  decisions → add `personal-finance`
- Wrongful-termination / retaliation / EEOC during PERM / I-140 →
  add `legal-disputes`

These flags inform the orchestrator's source-view selection; Pass-2
itself does not call those domains' packs. The `tech-career` ↔
`immigration` edge is the most frequently active — any H-1B-and-job-
offer situation lands on both, and the Risk Officer needs to surface
visa-status considerations as the *concentration risk on the human*
(per F10) that mirrors tech-career's equity concentration.

---

## Editor

The generic editor prompt in
[`src/blindspot/prompts/editor.md`](../../src/blindspot/prompts/editor.md)
governs structure. The additions below apply when this domain is active.

**Numeric and statutory specificity is mandatory.** Immigration
blindspots are worthless without the specific form, the specific clock,
the specific statute. When a blind spot or action references:

- A filing — name the form: `I-129H`, `I-130`, `I-140`, `I-485`,
  `I-131` (AP), `I-765` (EAD), `I-539` (extension / COS), `I-751`
  (removal of conditions), `I-907` (premium processing), `I-864`,
  `I-693`, supplement-J. "File the right form" without the form
  number is Critic-failing padding.
- A clock — name the day count: 60-day grace, 90-day preconceived-
  intent, 180-day I-485 pendency for AC21 portability, 180-/365-day
  unlawful-presence thresholds for §212(a)(9)(B) 3-/10-year bars,
  240-day work-auth extension, 540-day automatic EAD extension,
  6-year H-1B cap, 87-day RFE response clock, 2-year I-751
  conditional-PR window.
- A statute / regulation / policy — cite the exact section: INA
  §214(b) / §245(a) / §245(c) / §245(i) / §245(k) / §216 / §212(a)(4)
  / §212(a)(9)(B), AC21 §106(c) / §104(c), 8 CFR §214.1(l)(2),
  8 CFR §214.2(h)(9)(iv), 8 CFR §204.5(e), 9 FAM 502.1-1, USCIS
  Policy Manual volume, Matter of Dhanasar, Matter of Wang. "The
  law says..." without a cite is a Critic-failing fabrication
  signal.
- A Visa Bulletin reference — name the bulletin month + year,
  EB / F category, country of chargeability, and DFF vs FAD.
  "Priority date might be current soon" without those is padding.
- A USCIS service center or consulate — name it specifically when
  RFE rate or refusal pattern is load-bearing. "Service centers
  vary" is padding; naming the specific service center plus an RFE-
  rate window is not.

**Decision-support, not legal advice — explicit label required.**
Because `immigration.high_stakes` is `true` per Mechanism E, every
final output MUST include language equivalent to: *"This is
decision-support framing, not legal advice. Immigration is
high-stakes — missed filing windows, mis-classified status, and
uninformed travel during pending filings cause irreversible harm.
The binding determination on your specific case requires a licensed
immigration attorney with your full filing history, current USCIS /
DOS policy, and case-specific facts."* The label belongs at the
head of the answer for D2, D5, D8 or any combination involving
prior unlawful presence; otherwise the tail. Critic flags soft
language ("may want to consider speaking with a lawyer") as
insufficient.

**Don't soften the high-density blindspot anchors.** Per
`decisions.md` "Notes for downstream layers," D3, D5, D6, D8, D9 are
the highest-density blindspot anchors and D8 is the highest-stakes
single mis-step (preconceived-intent findings ripple into every
future adjudication). When the Risk Officer surfaces a blindspot
tied to these decisions, it ships in the final output verbatim —
Editor hedging on AP-abandonment risk, 90-day-rule exposure, or
245(c) bar status is exactly the Critic-failing brand of padding
the high-stakes regime was written to catch.

**Opposing-framing surfacing is mandatory.** Per `framings.md`
"Cross-framing tensions," every Editor output on an immigration
situation must surface at least one blindspot from the framing
OPPOSITE the asker's apparent one (F1↔F2, F1↔F13, F9↔F10, F14↔F2/F9).
The opposing framing's `Excludes` line is the seed; surface it as a
"here is the lens your question's vocabulary excluded" paragraph,
not a buried bullet.

**Cross-domain handoff.** When the situation crosses `tech-career`
(most common), `family-planning`, or `health-insurance`, name the
coupling explicitly — e.g. "the comp decision and the visa decision
are coupled here because [reason]; F10's visa-as-employer-leverage
frame applies to the comp side as much as the immigration side."
Do not silo the immigration discussion when the asker's situation
spans domains.

---

## Critic

Generic Critic rules from
[`src/blindspot/prompts/critic.md`](../../src/blindspot/prompts/critic.md)
apply unchanged. The additions below tune the per-claim spot-check for
immigration-specific claim categories. Because the domain is
`high_stakes: true`, **every numeric, statutory, or USCIS-policy claim
is subject to mandatory per-claim grounding** — the generic
"recommended" spot-check is upgraded to hard pass / fail here.

**Statutory / regulatory citations carry strict grounding.** Every
sentence containing one of the following is a mandatory citation
check; missing or hallucinated cites fail Critic immediately:

- An INA / AC21 / 8 CFR / 9 FAM section reference (INA §214(b),
  §245(*), §212(a)(9)(B), §203(h), §216; AC21 §106(c), §104(c),
  §106(a); 8 CFR §214.1(l)(2), §214.2(h)(9)(iv), §204.5(e);
  9 FAM 502.1-1)
- A USCIS Policy Manual volume reference, or a BIA / AAO precedent
  (Matter of Dhanasar, Matter of Wang, Matter of Hosseinpour, etc.)
- A specific form number with claimed validity period or filing
  window (e.g. "I-693 is valid indefinitely if signed by civil
  surgeon" must cite the late-2024 USCIS policy update)
- A specific day-count clock (60-/90-/180-/240-/365-/540-day,
  6-year, 87-day, etc.) tied to a statutory or regulatory source
- A Visa Bulletin month + EB/F category + country + DFF/FAD claim
- A specific USCIS service center or consulate RFE-rate / refusal-
  rate claim

If any such sentence lacks an adjacent `[doc-X]` marker citing a
source-view in [`sources.yaml`](./sources.yaml), set
`regenerate_required = true` AND name the uncited specific verbatim
in `feedback`. This is stricter than the tech-career equity-tax
grounding rule because immigration fabrications cause irreversible
harm — the §212(a)(9)(B) 10-year-bar clock cannot be undone by a
follow-up correction the way an AMT misstatement can.

**Specificity bar.** Generic phrases that pass the standard Critic
check are STILL fails in this domain. The shapes below all *look*
specific (they name a mechanism) but contain no statute, no clock,
no form:

- "Be careful about timing" (no clock named) — fail.
- "There's a grace period after termination" (no 60-day named, no
  CFR cite) — fail.
- "Consider speaking to an immigration attorney" (no specific
  decision-support handoff, generic deferral) — fail when used as a
  substitute for analysis; pass only as the Mechanism E label on
  decision-support framing.
- "Your priority date matters" (no Visa Bulletin reference, no DFF/FAD
  distinction) — fail.
- "Don't travel without proper authorization" (no AP / I-131 / dual-
  intent vocabulary) — fail.
- "USCIS rules vary by service center" (no specific service center
  named, no specific RFE-rate claim) — fail.

Mark specificity as `fail` and name the offending sentence verbatim
in `feedback`.

**Non-obviousness floor — `+1` for multi-route situations.** When
the matched persona spans multiple visa types or routes (e.g.
`h1b-with-approved-i140-backlogged` who is also
`self-petitioner-eb1a-candidate`; or `marriage-based-petitioner-usc-
spouse` who is also `f1-student-on-opt`), raise the non-obviousness
floor by one point. A 3/5 that would pass for a single-route asker
is a 2/5 here. Multi-route askers have already heard the single-
route advice; surfacing only what they already know fails non-
obviousness. This is the immigration parallel to tech-career's
`comparing-offers-*` non-obviousness raise.

**Cross-framing tension as a quality signal.** When the Risk Officer
surfaces blindspots from a framing OPPOSITE the asker's apparent one
(F1↔F2, F1↔F13, F9↔F10, F14↔F2/F9 — see Triage above), that typically
raises non-obviousness by 1 point because the asker's vocabulary
already excluded the opposing framing. Score accordingly — the
opposing-framing surfacing is the highest-leverage signal that the
answer is doing the asker's framing-correction work, not just
restating their starting position.

**Mechanism E label check.** If the final output lacks the
decision-support / not-legal-advice / consult-licensed-immigration-
attorney language required of every high-stakes-domain answer (see
Editor section above), set `regenerate_required = true` regardless
of other quality dimensions. This is non-negotiable per
[ROADMAP §5 Mechanism E](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating).
Soft variants ("you might want to talk to a lawyer eventually") fail
the check; the language must be explicit decision-support framing
plus an explicit attorney-consultation recommendation, and for the
highest-stakes situations (D2, D5, D8, anything with prior unlawful
presence) the label belongs at the head of the answer rather than
the tail.

---

## Notes for refine

- This file is `delta`, not duplication. If a future refine wants to
  add another persona, risk-surface, statute citation category, or
  claim shape, prefer editing the relevant short list above to growing
  the file beyond ~2500 words.
- The opposing-framing pairs (F1↔F2, F1↔F13, F9↔F10, F14↔F2/F9) are
  the highest-leverage routing tuning in this file. If eval shows the
  Risk Officer underusing the opposing-framing surface on immigration
  situations, sharpen the Triage `active_framings` section first.
- High-stakes propagation: this file currently says `high_stakes:
  true` per [`_meta_ontology.md`](../_meta_ontology.md). The Editor
  Mechanism E label and Critic mandatory-grounding rules above are
  load-bearing on that flag. If `_meta_ontology.md` ever softens that
  flag (extremely unlikely for immigration), the corresponding rules
  here must be removed in the same change.
- Cross-domain density: `immigration` ↔ `tech-career` is the most
  frequently active edge. When tech-career's `domain_pack.md` adds a
  new persona / risk surface, check whether the immigration side
  needs a parallel entry (e.g. tech-career's `h1b-or-status-bounded`
  persona corresponds to multiple personas here).
