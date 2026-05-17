# immigration — domain_pack.md

Triage / Editor / Critic prompt overrides scoped to `immigration`,
per [`_schema.md` §`domain_pack.md`](../_schema.md). Triage Pass-2
concatenates this file into its system prompt when the domain is
active.

`immigration` is `high_stakes: true` per
[`_meta_ontology.md` §2](../_meta_ontology.md). Mechanism E gating (per
[ROADMAP §5](../../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating))
applies in full: Editor MUST label outputs "decision-support, not legal
advice" with an AILA / state-bar counsel-deferral; Critic MUST hold
numeric / statutory / regulatory claims to mandatory per-claim citation
and reject determinative "you should file X" guidance lacking the
deferral. Gating is sharper than in `tech-career` because missed filing
windows, §212(a)(9)(B) bars, §214(b) preconceived-intent findings, and
§212(a)(6)(C)(i) misrepresentation findings compound across every
future adjudication.

Companion files: [`decisions.md`](./decisions.md) (D1–D10),
[`framings.md`](./framings.md) (F1–F14),
[`blindspots.md`](./blindspots.md) (70 entries, ≥ 5 per framing).
This file does not restate their content.

---

## Triage

Pass-1 has already extracted generic `(domains, entities, risk_surfaces,
personas)` from [`src/blindspot/prompts/triage.md`](../../src/blindspot/prompts/triage.md).
Pass-2 enriches Pass-1; it adds and *sharpens*, never overwrites.

**Decision matching.** Match against D1–D10 by the *Sample situations*
in [`decisions.md`](./decisions.md). Emit `matched_decision: "D<n>"`.
Multi-match is common and worth surfacing (e.g. D3 concurrent-filing
AND D5 AP-travel for a pending I-485 + foreign trip); do NOT collapse
genuine ambiguity.

**Persona refinement.** Replace generic `h1b-holder` / `f1-student`
with the most-specific persona below — blindspot triggers in
[`blindspots.md`](./blindspots.md) are written against these labels:

- `cap-subject-h1b-year-3` (D1, D4)
- `cap-subject-h1b-near-max-out` (D1 — AC21 §104(c) eligibility)
- `f1-to-h1b-stem-opt-bridge` (D7)
- `ac21-portability-mid-perm` (D4)
- `aos-pending-with-travel-question` (D5)
- `eb-2-vs-eb-3-downgrade-evaluation` (D6)
- `marriage-status-timing-with-citizen-partner` (D2 — K-1 / AOS / CP)
- `marriage-status-timing-with-lpr-partner` (D2 — F2A, naturalize-first)
- `o1-evidentiary-bar-evaluation` (D1, D9)
- `eb-1a-niw-self-petition-decision` (D9)
- `j-1-waiver-decision` (D1, D2 — §212(e) home-residency waiver paths)
- `concurrent-vs-sequential-i140-i485` (D3)
- `consular-processing-stuck-abroad` (D8 — §214(b) / §221(g) limbo)
- `cap-gap-stem-opt-decision` (D7)
- `derivative-aging-out-csa` (D2, D3 — CSPA formula, child age 17–22)
- `non-immigrant-to-immigrant-intent-transition` (D8 — 90-day scrutiny)
- `h4-ead-renewal-under-principal-risk` (D10)

**Mechanism-specific risk surfaces.** Replace generic `tax` /
`employment` / `family` / `travel` from Pass-1 with these specifics.
Each maps to one or more blindspots in
[`blindspots.md`](./blindspots.md):

- `ac21-same-or-similar-occupation-foot-gun` — 6-digit SOC literalism;
  IC-to-Manager crosses major-group boundary
- `aos-abandonment-via-ap-vs-leaving-on-AP-only` — pending I-485 +
  departure without AP; H-1B dual-intent has visa-stamp-expiry traps
- `EB-2-EB-3-downgrade-priority-date-lock` — 8 CFR §204.5(e) PD
  retention across categories on same PERM
- `OPT-cap-gap-eligibility-mathematics` — timely H-1B petition required;
  approved-vs-pending; April 1 → October 1 bridge
- `concurrent-filing-after-2022-eligibility-window-shift` — DOS posts
  DFF; USCIS decides month-by-month whether to accept AOS under it
- `O-1-petition-attribution-vs-O-3-derivative-rules` — O-3 has no
  independent work authorization (no H-4-EAD analog)
- `H-4-EAD-eligibility-from-spouse-PERM-progress` — 8 CFR §214.2(h)(9)(iv)
  requires approved I-140 OR AC21 §104(c)/§106(a); PERM-pending does NOT
  qualify
- `priority-date-portability-EB-1-to-EB-2-downgrade` — earlier EB PD
  ports forward only with same employer / PERM; self-petition PDs do
  NOT port to employer-sponsored
- `INA-§245(k)-180-day-out-of-status-grace` — EB-AOS forgiveness up to
  180 aggregate days; under-used recovery
- `INA-§245(i)-grandfathered-eligibility` — late-1990s-filed petitions
  conferring §245(a)-bar forgiveness for some derivatives
- `B-1/B-2-to-COS-30-60-day-rule-and-preconceived-intent` — 9 FAM
  302.9-4 90-day guideline; §212(a)(6)(C)(i) misrepresentation findings
  ripple into every future adjudication
- `J-1-two-year-home-residency-NIH-or-Conrad-30-waiver-paths` —
  §212(e); home-residency required before H, L, or LPR change
- `concurrent-AOS-while-naturalization-not-yet-clean` — petitioner USC
  vs LPR mid-pendency; F2A → IR1 automatic conversion
- `CSPA-age-frozen-vs-AOS-pending` — derivative-age formula + USCIS
  Feb-2023 sought-to-acquire DFF-current trigger shift
- `i-485-receipt-notice-vs-145-day-EAD-clock` — biometrics / interview
  lag; EAD/AP combo-card service-center variance
- `BUTLER-FINAL-RULE-PROCESS-DATES` — 2024 H-1B beneficiary-centric
  registration rule shifts lottery-attempt arithmetic
- `September-30-FY-deadline-for-DV-AOS` — DV forfeit cliff
- `H-1B-six-year-cap-and-AC21-3y-extension-conditions-precedent` —
  §104(c) needs approved I-140 + PD-not-current; §106(a) needs labor-
  cert filed > 365 days before max-out
- `unlawful-presence-vs-out-of-status` — §212(a)(9)(B) clock vs §245(c)
  out-of-status; distinct inadmissibility regimes
- `§222(g)-automatic-visa-voidance` — overstay even one day voids the
  visa stamp for future use

If a Pass-1 surface generalizes into one of these, emit the specific.
New entries should follow the same statutory-anchor naming rule.

**Framing-signal vocabulary.** Pass-2 emits an optional
`active_framings` field — the F1–F14 framings from
[`framings.md`](./framings.md) the asker's vocabulary indicates they
are reasoning inside. The asker's framing is itself a blind spot;
this routes the Risk Officer to surface the **opposing** framing's
blindspots. Opposing pairs documented in `framings.md` §Cross-framing
tensions:

- **F1 (status-continuity) ↔ F2 (route-optimality)** — F1 "never let
  status lapse" vs F2 "tolerate status fragility for years off the GC
  timeline." Same H-1B-max-out facts get opposite advice.
- **F1 ↔ F13 (consular-vs-COS-discretion)** — F1 "file COS now to lock
  status" vs F13 "fly home and consular-process to avoid 90-day-rule
  scrutiny." Common on D8.
- **F9 (evidentiary-bar) ↔ F10 (visa-as-employer-leverage)** — same
  CV portfolio is procedural input (F9) vs leverage instrument (F10).
- **F14 (pro-se) ↔ F2** — pro-se procedural defects restart cycles
  route-velocity arithmetic ignores.
- **F14 ↔ F9** — pro-se EB-1A filings rarely meet comparable-evidence
  patterns adjudicators expect.

When Pass-1 vocabulary aligns with one framing in a pair, emit BOTH
the asker's framing AND the opposing framing, with the opposing one
flagged for Risk Officer non-obviousness lift.

**Cross-domain routing flags.** Emit `cross_domain: [<slug>, ...]`
when Pass-1 surfaces persona signals implying an adjacent domain:

- Comp / RSU / ISO / layoff / PIP combined with H-1B / I-140 / PERM →
  `tech-career` (highest-frequency edge per D1, D4, D7, D10)
- Marriage / fiancé / wedding / partner-petition → `family-planning`
  (D2 — the marriage decision itself lives there)
- COBRA / health-insurance / spouse-coverage on stay-or-leave →
  `health-insurance` (D5, D10 — coverage gaps on status lapse)
- 401(k) / IRA / exit-tax / FBAR / PFIC with stay-or-leave framing →
  `personal-finance` (exit-tax often binds the immigration choice)
- Wrongful-termination / EEOC / retaliation on a layoff that also
  implicates H-1B 60-day grace → `legal-disputes`

Flags inform orchestrator source-view selection; Pass-2 does not call
adjacent packs. The `tech-career` edge is the canonical coupling —
emit it on any H-1B / I-140 / PERM / O-1 / EB-1A / EB-2 / EB-3
situation where employer choice is in scope.

---

## Editor

The generic editor prompt in
[`src/blindspot/prompts/editor.md`](../../src/blindspot/prompts/editor.md)
governs structure. Additions below apply when this domain is active.

**Mechanism E "decision-support, not legal advice" label is MANDATORY.**
Because `immigration.high_stakes` is `true`, EVERY response MUST carry
the decision-support disclaimer, prominently placed. Required shape
(wording may be edited; *substance* is required):

> *Decision-support, not legal advice. Immigration adjudications turn
> on case-specific facts and current USCIS / DOS policy that shifts
> month-by-month. Before any filing, consult a licensed immigration
> attorney — AILA's Immigration Lawyer Search (aila.org) or your
> state bar's referral service is the canonical path.*

Required substance: (a) response is decision-support; (b) case-specific
facts govern; (c) AILA / state-bar referral is the canonical path.
Omission is a Critic regeneration trigger. This is the immigration-
domain analog of tech-career's "no professional-advice label" rule
running in the opposite direction.

**Numeric specificity is load-bearing.** Immigration blindspots
collapse without statutory anchors, day counts, and dollar figures.
Required shapes:

- *Priority dates* — Visa Bulletin month/year + category × country.
  "Your PD is current" without bulletin month is padding; "EB-2 India
  FAD is May 2014 in the November 2025 bulletin; DFF is January 2015"
  is not.
- *USCIS fees (Jan-2024 schedule)* — I-485 $1,440 (adult, includes
  biometrics) + $260 EAD + $630 AP; I-140 $715; I-130 $675 paper /
  $625 online; I-129 H-1B $780 + $1,500 ACWIA (large employers) +
  $4,000 §214(c)(12) border-security fee; PERM-9089 $1,000 standard /
  $4,500 with 2024 PERM premium-processing.
- *Processing times* — service center, form code, current USCIS-posted
  range. "USCIS is slow" is padding; "I-485 at NSC is 8.5–25.5 months
  for EB I-140-based as of November 2025" is not.
- *AC21 windows* — 180-day I-485-pendency, supplement-J timing,
  60-day termination grace, 240-day work-auth extension on timely
  H-1B extension.
- *Status / EAD extensions* — 60-day grace on terminated H-1B/L-1/O-1
  (8 CFR §214.1(l)(2)); 540-day automatic EAD extension on timely
  renewal (2024 rule); 145-day biometrics-to-EAD-print clock.
- *CSPA* — explicit formula: derivative-age = (chronological age at
  PD-current) − (I-140 pendency days). Name Matter of Wang and the
  USCIS Feb-2023 sought-to-acquire DFF-current shift.
- *Statutory / regulatory citations* — name the section. INA §245(a)
  AOS eligibility; §245(c) EB bars; §245(k) 180-day forgiveness;
  §212(a)(9)(B) 3/10-year bars; §245(i) grandfathered eligibility;
  §214(b) nonimmigrant-intent; §222(g) voidance; §216 conditional PR;
  §216(c)(4) I-751 waivers; AC21 §106(c) portability; AC21 §104(c)
  3-year extension; 8 CFR §214.2(h)(9)(iv) H-4 EAD; 9 FAM 502.1-1 PD
  attachment.

A blindspot or action naming a regime without the section number, or
a fee without form/date, is Critic-failing padding even when the
underlying reasoning is sound.

**Opportunity-cost framing for path-comparison personas.** When the
matched persona is `eb-2-vs-eb-3-downgrade-evaluation`,
`o1-evidentiary-bar-evaluation`, `eb-1a-niw-self-petition-decision`,
`marriage-status-timing-with-citizen-partner` (K-1 vs AOS-after-marriage
vs CP), or `concurrent-vs-sequential-i140-i485`, the Editor MUST name
the path NOT taken with its current PD math, bulletin position, and
USCIS RFE-rate posture. Keep this in the response body; do NOT
collapse it into "Concrete next steps." Template adapted from
tech-career F11 (foregone $2M FAANG cash): name the foregone EB-1A
path (8–15 months current adjudication), the foregone EB-3 path
(current bulletin position), or the foregone K-1 path (7–10 month
processing incl. consular interview), explicitly against the leaned-
toward path.

**Frame the non-modal-outcome.** Per `blindspots.md` cross-framing
tensions (F1↔F2 and F4 abandonment), responses ship the success path
more readily than the failure path. Editor MUST name the specific
failure mode adjacent to the success guidance:

- I-485 denial after AOS abandonment via AP misuse → re-entry as
  §212(a)(7) inadmissible at port of entry; §245(k) recovery and CP
  fallback.
- B-1/B-2-to-COS denied as preconceived intent → §212(a)(6)(C)(i)
  misrepresentation finding; §237(a)(1)(A) removability exposure.
- EB-1A RFE-then-denial → sunk $8–15k; comparable-evidence reframing
  in AAO appeal; parallel EB-2/3 preservation should already be in
  flight.
- H-4 EAD lapse during principal's H-1B layoff → §245(c) exposure if
  spouse continued working past EAD expiry; H-1B-cap-lottery-as-
  status-independence recovery move.

Success path without the failure-mode counterpart is asymmetric hedging
the Critic should flag.

**Don't soften abandonment, 90-day-rule, or unlawful-presence
blindspots.** These are the highest-density anchors per
[`decisions.md`](./decisions.md) Notes (D3, D5, D6, D8, D9). When the
Risk Officer surfaces them, they ship verbatim. Editor hedging ("you
might want to consider AP before traveling") on a situation where AP-
vs-departure is the binding constraint is a Critic failure. Same for
90-day-rule scrutiny on a fresh B-visa entrant developing immigrant
intent; same for unlawful-presence clock confusion post-denial.

**No state-bar-jurisdictional overreach.** Immigration law is federal;
do NOT add "in your state" qualifications to the counsel-deferral —
immigration attorneys can represent in any state. State-bar admission
matters for state-law collateral questions (family law on divorce-
during-conditional-PR; employment law on the §245(c) employer-side);
when a question genuinely overlaps state law, name both deferrals.

---

## Critic

Generic Critic rules from
[`src/blindspot/prompts/critic.md`](../../src/blindspot/prompts/critic.md)
apply unchanged. Additions below tune for immigration-specific claim
categories and enforce the Mechanism E gate.

**Mechanism E violation flag — MANDATORY rejection.** If the response
contains a determinative case-specific recommendation — "you should
file X" / "do not file X" / "you qualify for X" / "you do not qualify
for X" — WITHOUT the Editor's required decision-support label naming
AILA / state-bar referral, set `regenerate_required = true` and name
the offending sentence verbatim in `feedback`. The deferral is
mandatory because (a) filing windows are time-bounded and an erroneous
"file X" can foreclose the correct filing forever (DV-AOS Sept 30
cliff, AC21 portability, J-1 two-year-home-residency); (b) visa-stamp
/ port-of-entry consequences turn on CBP discretion the response
cannot model; (c) §212(a)(6)(C)(i) misrepresentation findings compound
across all future adjudications and cannot be unwound.

**Per-claim citation spot-check — MANDATORY (not just recommended).**
Every sentence containing any of the following MUST carry a `[doc-X]`
marker in the same sentence or the immediately adjacent one. If absent,
set `regenerate_required = true` AND name the uncited specific verbatim:

- A Visa Bulletin priority date or month
- A USCIS form fee or service-center processing time
- A statutory section (INA §245(a), §245(c), §245(k), §245(i),
  §212(a)(9)(B), §214(b), §216, §222(g), AC21 §106(c), §104(c),
  §242 / §237 removability)
- A regulatory citation (8 CFR §214.1(l)(2), §214.2(h)(9)(iv),
  §204.5(e), 9 FAM 502.1-1, 9 FAM 302.9-4)
- A day-count (180-day I-485, 60-day grace, 240-day extension,
  540-day EAD, 90-day preconceived-intent guideline, 365-day AC21
  §106(a), 3/10-year §212(a)(9)(B) bars)
- A USCIS policy-manual citation or update date (Feb-2023 CSPA-DFF
  shift; 2024 EAD-540-day rule; 2024 H-1B beneficiary-centric
  registration rule)
- A case-law citation (Matter of Wang, Matter of Dhanasar, Kazarian,
  Cuellar de Osorio, Guilford College v. Wolf)
- A consulate processing posture (e.g. "Chennai's H-1B refusal rate")

Stricter than the generic rule because immigration numeric specifics
are exactly the category where uncited assertions turn out to be model
fabrications, and a fabrication routes the asker into an irreversible
action.

**Specificity bar.** Generic phrases passing the standard Critic check
are STILL fails on filing-window or status-eligibility questions:

- "Be careful with the 90-day rule" (no FAM section) — fail. Right
  shape: "9 FAM 302.9-4 treats activities inconsistent with B-status
  within 90 days of entry as evidence of preconceived intent under
  INA §214(b)."
- "AC21 portability lets you change employers" (no §106(c), no
  same-or-similar standard, no 180-day mark) — fail.
- "File before your status lapses" (no day-count, no bridge-app
  mechanic) — fail.
- "You'll need a waiver" (no §212(e) J-1, §212(d)(3) nonimmigrant,
  §212(i) fraud, §212(h) criminal — different regimes) — fail.
- "Your priority date will be current" (no bulletin month, no
  category × country, no DFF-vs-FAD distinction) — fail.

These shapes *look* specific (they name a mechanism) but contain no
statute, calendar, or jurisdictional specificity. Mark specificity
`fail` and name the offending sentence verbatim.

**+1 non-obviousness floor for high-stakes path-comparison personas.**
For `aos-pending-with-travel-question`, `eb-2-vs-eb-3-downgrade-
evaluation`, `ac21-portability-mid-perm`, or `concurrent-vs-sequential-
i140-i485`, the Critic MUST require ≥ 1 non-obvious blindspot per
response — one the asker would not have asked about themselves.
Askers reaching these personas have typically read MurthyDotCom /
r/USCIS / Boundless and heard the modal blindspots already. Per-
persona non-obvious surfaces:

- `aos-pending-with-travel-question` — visa-stamp expiration on return
  even with valid AP (F4); §245(k) recovery if AP-misuse triggers
  abandonment; CBP secondary-inspection risk with approved AP.
- `eb-2-vs-eb-3-downgrade-evaluation` — interfile administrative
  variance by service center (F7); EB-3 India 2020–22 retrogression-
  reversal precedent; cross-chargeability via spouse.
- `ac21-portability-mid-perm` — SOC-literalism on IC-to-Manager
  promotions (F5); 180-day milestone vulnerability to USCIS-initiated
  AOS denial; new-employer immigration-team-absence as RFE risk.
- `concurrent-vs-sequential-i140-i485` — DFF-is-DOS-table vs USCIS-
  acceptance-decision divergence (F3); H-4 derivatives must also file
  concurrently or risk age-out; concurrent-filing's effect on later
  COS / status-move options.

Floor is 4/5, not the generic 3/5; modal-only response is
`non_obviousness: fail`.

**Cross-framing tension as quality signal.** When the Risk Officer
surfaces blindspots from a framing OPPOSITE the asker's apparent one
(F1↔F2, F1↔F13, F9↔F10, F14↔F2, F14↔F9), raise non-obviousness by
1 point — the asker's vocabulary already excluded the opposing framing.
Load-bearing in immigration because forums are heavily lens-segmented
(status-continuity-anchored r/h1b vs route-optimality-anchored r/EB1
/ immigration-Twitter).

**High-stakes label enforcement.** Unlike `tech-career`'s Critic,
the Critic here MUST verify the Editor included the decision-support
/ counsel-deferral label; absence is a regeneration trigger (named
in the Mechanism E section above). This is the immigration-domain
inversion of tech-career's "No high-stakes label expected" rule —
both are Mechanism E gating, applied in opposite directions per the
high-stakes flag.

---

## Notes for refine

- `delta`, not duplication. To add a persona, risk-surface, or claim
  category, prefer editing the relevant short list above to growing
  the file beyond ~2500 words.
- Opposing-framing pairs (F1↔F2, F1↔F13, F9↔F10, F14↔F2, F14↔F9) are
  the highest-leverage routing tuning here. If eval shows Risk Officer
  underusing the opposing-framing surface, sharpen the Triage
  `active_framings` section first.
- Mechanism E rules above propagate the `high_stakes: true` flag from
  [`_meta_ontology.md`](../_meta_ontology.md). If that flag flips
  (unlikely), Editor MANDATORY-disclaimer and Critic MANDATORY-
  rejection-on-omission must be revised in the same change.
- Statutory anchors in the Editor list are current INA / 8 CFR / 9 FAM
  at authoring. Statutory numbers are stable; USCIS policy-manual
  update dates and Visa Bulletin month references in examples will
  need periodic refresh.
