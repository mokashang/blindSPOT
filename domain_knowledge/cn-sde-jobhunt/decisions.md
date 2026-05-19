# cn-sde-jobhunt — Decisions (Layer 1)

Decision ontology for `cn-sde-jobhunt`. Scope inherits from
[`_meta_ontology.md`](../_meta_ontology.md): US-based SDE career
decisions made by Chinese international students whose visa status
(F-1, OPT, STEM-OPT, cap-gap, H-1B, H-4 / H-4-EAD, O-1, AOS-pending)
is a binding constraint on the move. The vertical lives at the
intersection of tech-career and immigration; purely-tech-career or
purely-visa situations are out of scope and Triage refuses them
(see `domain_pack.md` §Triage).

This file names **what** decisions exist, with scope and pointers to
the framing axes they argue over. The framings themselves live in
`framings.md` (F1–F6 cross-referenced below). Per-entry paragraph
content is voice-work and is authored by the human only.

---

## Cross-reference

| # | Decision | Layer-2 framings | Layer-3 risk surfaces | V2 fixtures | Blindspot-§ |
|---|---|---|---|---|---|
| 1 | Offer comparison under H-1B sponsorship-willingness filter | F1, F2, F3, F6 | visa-security, sponsorship-commitment, gc-timeline, comp-arithmetic | offer-comparison-sponsorship-asymmetry, mid-senior-ic-faang-to-non-sponsor-startup, senior-ic-startup-vs-faang-with-i140-approved | §F1, §F2, §F3, §F6 |
| 2 | OPT / STEM-OPT / cap-gap timing across employer choice | F1, F6 | opt-clock, e-verify-employer, cap-gap-eligibility | opt-stem-cap-gap-timing-fall-vs-spring-grad, non-stem-master-stem-pivot-for-opt-extension | §F1, §F6 |
| 3 | H-1B lottery backup paths (O-1, L-1, day-1-CPT, MS-pipeline) | F1, F4, F6 | second-lottery-strategy, day-1-cpt-risk, status-restoration | h1b-lottery-not-selected-backup-paths, opt-stem-cap-gap-timing-fall-vs-spring-grad | §F1, §F4, §F6 |
| 4 | Employer switch mid-PERM / mid-I-140 (AC21 §106(c)) | F1, F2, F6 | same-or-similar, i-140-portability, priority-date-preservation | ac21-employer-switch-mid-perm-with-priority-date, mid-i140-switch-same-or-similar-rfe-risk, bytedance-i140-approved-return-window | §F1, §F2, §F6 |
| 5 | Layoff response under H-1B / H-4 status pressure | F1, F5, F6 | 60-day-grace, severance-clock-interaction, h4-status-tracks-principal | layoff-on-h1b-with-h4-spouse | §F1, §F5, §F6 |
| 6 | Return-to-China (海归) timing decision | F2, F4, F5 | gc-backlog-roi, china-tech-window, 35-and-over-discount, family-pressure | return-to-china-timing-eb2-backlog, bytedance-i140-approved-return-window | §F2, §F4, §F5 |
| 7 | Family-located optimization (H-4-EAD spouse, parent B-2, school) | F1, F5 | h4-ead-vulnerability, state-residency-coupling, school-enrollment | h4-ead-spouse-considering-h1b-primary-switch, layoff-on-h1b-with-h4-spouse | §F1, §F5 |
| 8 | PhD / postdoc-to-industry conversion (route choice) | F1, F2, F6 | eb1a-niw-vs-h1b, opt-to-h1b-bridge, advisor-relationship-timing | phd-postdoc-to-industry-route-selection | §F1, §F2, §F6 |
| 9 | Long-term career capital vs visa security tradeoff | F1, F2 | skill-trajectory-vs-status-stability, employer-quality-premium | mid-senior-ic-faang-to-non-sponsor-startup, post-cliff-startup-jump-vs-faang-gc-stability, senior-ic-startup-vs-faang-with-i140-approved | §F1, §F2 |
| 10 | O-1 vs H-1B-lottery route selection | F1, F6 | evidentiary-bar, cap-exempt-flexibility, employer-cooperation | — | §F1, §F6 |
| 11 | Post-cliff (post-RSU-vest) career strategy under visa coupling | F1, F2, F3 | rsu-cliff-timing, gc-timeline-vs-comp-cycle, retention-vs-departure | post-cliff-startup-jump-vs-faang-gc-stability, senior-ic-startup-vs-faang-with-i140-approved, ac21-employer-switch-mid-perm-with-priority-date | §F1, §F2, §F3 |
| 12 | First-employer choice under "willing to sponsor" filter (new-grad) | F1, F3, F6 | sponsorship-history, h1b-vs-h4-vs-l1-strategy, comp-discount-for-sponsorship | offer-comparison-sponsorship-asymmetry | §F1, §F3, §F6 |

Each row's framing IDs reference `framings.md` (F1 = Visa-security
maximization; F2 = Long-term career capital; F3 = Comp maximization
in a 4-year window; F4 = Return-to-China optionality; F5 =
Family-located optimization; F6 = Legal-mechanic rigor).
Blindspot-§ column references `blindspots.md` §F1-§F6 sections (5 blindspot slots each).
V2 fixtures column references files in `fixtures/*.yaml` (slug =
filename without `.yaml`); fixtures listed exercise the decision via
their `text:` + `expected_*` annotations, and a single fixture may
legitimately exercise multiple decisions (mixed-case situations).

**Fixture coverage gap**: D10 (O-1 vs H-1B-lottery route selection
upfront) currently has **zero dedicated V2 fixtures** — the
closest, `h1b-lottery-not-selected-backup-paths`, treats O-1 as a
post-lottery-fail backup (D3), not as an upfront route choice. Add
a D10 fixture in a future eval-layer pass to close this gap.

---

## Entries

### 1. Offer comparison under H-1B sponsorship-willingness filter

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 2. OPT / STEM-OPT / cap-gap timing across employer choice

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 3. H-1B lottery backup paths (O-1, L-1, day-1-CPT, MS-pipeline)

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 4. Employer switch mid-PERM / mid-I-140 (AC21 §106(c) portability)

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 5. Layoff response under H-1B / H-4 status pressure

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 6. Return-to-China (海归) timing decision

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 7. Family-located optimization (H-4-EAD spouse, parent B-2, kids' schooling)

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 8. PhD / postdoc-to-industry conversion (route choice)

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 9. Long-term career capital vs visa-security tradeoff

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 10. O-1 vs H-1B-lottery route selection

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 11. Post-cliff (post-RSU-vest) career strategy under visa coupling

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)

### 12. First-employer choice under "willing to sponsor" filter (new-grad)

- **Scope** — (to be authored)
- **Framing-axes-covered** — (to be authored)
- **Sample situations** — (to be authored)
