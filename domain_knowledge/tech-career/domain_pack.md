# tech-career — domain_pack.md

Triage / Editor / Critic prompt overrides scoped to the `tech-career`
domain, per [`_schema.md` §`domain_pack.md`](../_schema.md). Triage's
pass-2 concatenates this file into its system prompt when this domain
is active. Editor and Critic use the corresponding sections when the
situation routes here.

`tech-career` is `high_stakes: false` per
[`_meta_ontology.md` §1](../_meta_ontology.md) — material money but
recoverable. Mechanism E gating (Editor "decision-support, not
professional advice" labels, Critic stricter grounding) is therefore
NOT applied below. The exception is equity-tax content — AMT, QSBS,
83(b), ISO holding-period — which carries IRS-deadline risk that
behaves locally high-stakes even though the domain at large isn't. The
Critic subsection below names the equity-tax claim categories where
grounding strictness rises.

Companion files: [`decisions.md`](./decisions.md) (D1–D11),
[`framings.md`](./framings.md) (F1–F14),
[`blindspots.md`](./blindspots.md). Reference them; this file does
not restate their content.

---

## Triage

Pass-1 has already extracted generic `(domains, entities, risk_surfaces,
personas)` from [`src/blindspot/prompts/triage.md`](../../src/blindspot/prompts/triage.md).
Pass-2 with this domain active enriches that output with the
domain-specific facets below. The Pass-1 vocabulary stays the
authoritative ground set; Pass-2 adds and *sharpens*, never overwrites.

**Decision matching.** Identify the closest match from D1–D11 in
[`decisions.md`](./decisions.md) by the *Sample situations* under each
decision (those are written for this purpose). Emit it as
`matched_decision: "D<n>"`. Multiple-decision matches are allowed and
common — emit a list ordered by closeness. A genuinely ambiguous
situation between two decisions is a routing signal worth surfacing;
do NOT collapse it.

**Persona refinement.** Pass-1 may have emitted a generic persona like
`comparing-offers` or `early-employee`. Replace with the most-specific
persona from this controlled list when the situation supports it:

- `comparing-offers-cross-stage` (e.g. FAANG vs Series B vs seed)
- `comparing-offers-same-stage` (two public-co offers, or two seed offers)
- `early-stage-employee-pre-liquidity` (D2, D3, D4)
- `late-stage-employee-pre-tender` (D9)
- `public-co-employee-with-vested-equity` (D6)
- `laid-off-with-severance-pending` (D5)
- `on-pip-or-pip-pending` (D7)
- `mid-tenure-refresher-curious` (D8)
- `acquihire-target` (D10)
- `cofounder-pre-incorporation` (D11)
- `iso-holder-considering-exercise` (D3 — frequently overlays the above)
- `h1b-or-status-bounded` (cross-cuts D1, D4, D6 — routing flag for
  `immigration` overlap; see Cross-domain below)

These are the personas the per-domain blindspot triggers in
[`blindspots.md`](./blindspots.md) are written against. Generic
persona labels will miss most triggers.

**Risk-surface vocabulary.** Replace generic `tax` / `legal` /
`liquidity` / `regret` from Pass-1 with the specific risk surfaces
below when the situation supports them. Each maps to one or more
blindspots in [`blindspots.md`](./blindspots.md); using the generic
label loses the routing:

- `AMT-crossover` — bargain element triggers tentative minimum tax
- `AMT-credit-uncollectable` — exercise on a stock that ends near $0
- `83b-deadline` — 30-day post-grant clock on early-exercise filings
- `QSBS-5-year-clock` — Section 1202 holding period
- `90-day-PTE-window` — post-termination exercise expiry
- `ISO-disqualifying-disposition` — qualifying-disposition holding broken
- `golden-handcuffs` — large unvested grant anchors stay-vs-go
- `vesting-cliff-discontinuity` — quit/PIP/leave near a vest event
- `concentration-in-employer-stock` — > ~20% net worth in one ticker
- `dilution-and-pool-refresh` — pre-money pool top-up dilution
- `preference-stack-and-waterfall` — common-stock payout below
  preferred at sale
- `single-vs-double-trigger-acceleration` — change-of-control mechanics
- `OWBPA-21-day-consideration` — age-40+ severance signing window
- `non-compete-enforceability-by-state` — CA §16600 vs FL enforcement
- `release-of-claims-waiver` — what is being waived in severance
- `state-AMT-divergence` — CA, NY, NJ AMT and allocation rules
- `multi-state-residency-allocation` — partial-year vest allocation
- `409A-FMV-timing` — bargain element shifts with refresh dates
- `secondary-lender-due-diligence` — non-recourse loan path to exercise

If a Pass-1 risk surface generalizes into one of these, emit the
specific. If the situation supports a risk not in this list, emit it
as-is (the list is non-exhaustive; new entries should follow the same
specific-mechanism naming rule).

**Framing-signal vocabulary.** Pass-2 also emits an optional
`active_framings` field — the F1–F14 framings from
[`framings.md`](./framings.md) the situation's vocabulary already
indicates the asker is reasoning inside. Match against each framing's
*Characteristic vocabulary*. This routes the Risk Officer to surface
the **opposing** framing's blindspots — F3 (liquidity-preservation) ↔
F11 (asymmetric-bet-on-team), F4 (concentration-risk) ↔ F13
(insider-signal-reading), F1 (AMT-min) ↔ F3 (liquidity-preservation
under cash-bind). The asker's framing is itself a blind spot.

**Cross-domain routing flags.** When Pass-1 surfaces persona signals
that imply an adjacent domain, emit `cross_domain: [<slug>, ...]`:

- H-1B / O-1 / green-card / I-140 mentioned → add `immigration`
- 401(k) / mega-backdoor / asset allocation centered → add `personal-finance`
- Cap-table seat / founding-team work / pre-incorporation → add `entrepreneurship`
- Wrongful-termination / EEOC / retaliation claim → add `legal-disputes`
- Big-tech-to-finance / IC-to-PM / industry pivot → add `career-pivots`

These flags inform the orchestrator's source-view selection; Pass-2
itself does not call those domains' packs.

---

## Editor

The generic editor prompt in
[`src/blindspot/prompts/editor.md`](../../src/blindspot/prompts/editor.md)
governs structure. The additions below apply when this domain is active.

**Numeric specificity is load-bearing.** Tech-career blindspots are
worthless without numbers. When a blind spot or action references:

- AMT — name the exemption ($88,100 single / $137,000 MFJ for 2026),
  the 28% bracket break (~$232,600 AMTI), or the phase-out completion
  (~$1.2M) the asker is near. "AMT may apply" without a bracket is
  Critic-failing padding.
- Vesting cliffs — name the calendar gap in months/weeks, and the
  next-vest dollar amount when the situation provides enough to
  compute it. "Wait until your cliff" without a date is padding.
- Severance — name the OWBPA 21-day consideration window for age-40+
  signers, and 7-day post-signature revocation. "You have time" is
  padding; "You have 21 days under OWBPA to consider and 7 days after
  signing to revoke, both statutory for age-40+" is not.
- Concentration — name the ~20% net-worth threshold, the Bessembinder
  2018 base rate (~50% of individual stocks underperform cash over 10
  years), or a specific tender pro-rata percentage where applicable.
- Dilution — name a 15–25% per-round dilution range plus the typical
  10–20% pre-money pool refresh, and use those to project +1, +2, +3
  round outcomes if the situation justifies the math.

**Opportunity-cost framing for `comparing-offers-*` personas.** Per
PR-history pattern (#2, #6): when the matched persona is
`comparing-offers-cross-stage` or `comparing-offers-same-stage`,
the Editor MUST surface at least one blind spot framed as
opportunity-cost — what the asker forgoes by taking the offer they're
leaning toward, expressed in after-tax dollars across the 4-year
horizon. The opposing-framing rule from Triage above usually supplies
this; the Editor's job is to keep it in the output rather than collapse
it into the "Concrete next steps" section. F11's `Excludes` line on
foregone $2M FAANG cash is the template.

**Citation discipline for equity-tax claims.** Every numeric assertion
about AMT, 83(b), QSBS, ISO holding-period, OWBPA, or non-compete
enforceability MUST carry a `[doc-X]` marker in the same sentence or the
immediately adjacent one — these are the categories where uncited
"facts" most often turn out to be hallucinations. Generic comp-band
claims (levels.fyi percentiles) follow the standard grounding rules.

**Don't soften AMT or 83(b)-deadline blindspots.** These are the
high-density blindspot anchors (per `decisions.md` Notes for downstream
layers — decisions 3, 5, 7, 9). When the Risk Officer surfaces them,
they ship in the final output verbatim. Editor hedging ("you might
want to consider AMT") on a situation where AMT crossover is the
binding constraint is a Critic failure.

**No professional-advice label.** Because `tech-career.high_stakes`
is `false`, do NOT label the output "decision-support, not legal/tax
advice." That label is reserved for `immigration`, `health-insurance`,
`personal-finance` (when dollar-specific), `family-planning`,
`legal-disputes`. Adding it here over-warns and is itself a brand of
padding the Critic should flag.

---

## Critic

Generic Critic rules from
[`src/blindspot/prompts/critic.md`](../../src/blindspot/prompts/critic.md)
apply unchanged. The additions below tune the per-claim spot-check for
tech-career-specific claim categories.

**Equity-tax claim categories carry higher grounding strictness.**
Treat the per-claim citation spot-check as MANDATORY (not just
recommended) for any sentence containing:

- A specific AMT exemption / bracket / phase-out dollar figure
- A specific 83(b) / OWBPA / QSBS / ISO holding-period day count
- A specific non-compete enforceability claim about a named state
- A specific change-of-control acceleration percentage (single-trigger
  vs double-trigger, partial vs full)
- A specific levels.fyi / Carta / Index Ventures percentile band
- A specific PIP success-rate or severance-negotiation-rate empirical claim
- A specific Bessembinder / Slicing Pie / Markowitz reference

If any such sentence lacks an adjacent `[doc-X]` marker, set
`regenerate_required = true` AND name the uncited specific verbatim in
`feedback`. This is stricter than the generic rule because tech-career
numeric specifics are exactly the category where uncited assertions
turn out to be model fabrications.

**Specificity bar.** Generic phrases that pass the standard Critic
check are STILL fails in this domain when used on equity questions:

- "Be careful with AMT" (no bracket named) — fail.
- "Consider the dilution" (no per-round percentage) — fail.
- "Check your state's non-compete law" (no state named, no enforce-
  ability stance) — fail. The right shape: "California voids non-
  competes under §16600; Florida enforces with reasonableness test."
- "Watch your vesting cliff" (no calendar reference) — fail.

These are the failure shapes that *look* specific (they name a
mechanism) but contain no number, no clause, no jurisdiction. Mark
specificity as `fail` and name the offending sentence verbatim.

**Non-obviousness bar for `comparing-offers-*` situations.** When the
matched persona is `comparing-offers-cross-stage` or
`comparing-offers-same-stage`, raise the non-obviousness floor by one
point — a 25-year-old comparing offers has usually already heard
"compare base + equity + bonus." A 3/5 that would pass elsewhere is a
2/5 here. Specifically: the opportunity-cost framing the Editor
surfaces above should be at non-obviousness ≥ 4 to count toward the
blind-spot quota.

**Cross-framing tension as a quality signal.** When the Risk Officer
surfaces blindspots from a framing OPPOSITE the asker's apparent one
(F3↔F11, F4↔F13, F1↔F3 under cash-bind — see Triage above), that
typically raises non-obviousness by 1 point because the asker's
vocabulary already excluded the opposing framing. Score accordingly.

**No high-stakes label expected.** Unlike `immigration` or
`personal-finance`'s Critic sections, do NOT penalize the Editor for
omitting the "decision-support, not legal/tax advice" label here. The
domain is `high_stakes: false`. (See Editor section above.)

---

## Notes for refine

- This file is `delta`, not duplication. If a future refine wants to
  add another persona, risk-surface, or claim category, prefer
  editing the relevant short list above to growing the file beyond
  ~2500 words.
- The opposing-framing pairs (F3↔F11, F4↔F13, F1↔F3) are the
  highest-leverage routing tuning in this file. If eval shows the
  Risk Officer underusing the opposing-framing surface, sharpen the
  Triage `active_framings` section first.
- High-stakes propagation: this file currently says `high_stakes:
  false` per [`_meta_ontology.md`](../_meta_ontology.md). If
  `_meta_ontology.md` ever flips that flag, the Editor "No
  professional-advice label" and Critic "No high-stakes label
  expected" rules above MUST be removed in the same change.
