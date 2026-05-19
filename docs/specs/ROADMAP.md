# Blindspot — Roadmap (Scope-Narrowed, Portfolio-Track)

**Date:** 2026-05-18 (scope-narrowed pivot)
**Status:** Active. Target completion: 2026-06-01 (~2-week sprint).
**End-state:** Frozen portfolio artifact; not a product.

## 0. Scope narrow — what changed and why

The original roadmap (V1 → V5) aimed at a universal blind-spot tool
spanning 10 life-decision domains, with cross-domain frame-breaking
as the long-term north star.

**That plan is deprecated as of 2026-05-18.** The reason is honest:
the universal scope competes head-on with general-purpose LLM chat
and has no defensible moat at the product level. The work was
worth doing as a craft exercise — the multi-agent pipeline, the
4-layer knowledge model, the autonomous refine loop — but those
ideas belong to a *project*, not a product.

The project is being completed as a **deep, well-built single-vertical
advisor**: a tech-showcase artifact for the author's portfolio, then
archived. The chosen vertical:

> **Chinese international students in the US, making SDE job-hunt
> and visa-coupled career decisions.**

Why this vertical:

- It sits at the intersection of two domains the existing build
  already invested in (`tech-career` + `immigration`).
- It has *Chinese-language community knowledge* that general LLM
  training data underrepresents — 1point3acres (一亩三分地), Zhihu
  career threads, 海归 podcasts. This is the moat.
- It is the author's lived experience, so authoring per-decision
  knowledge files at the required quality bar is achievable in days
  rather than months.
- The decisions are high-stakes (visa lapses are irreversible) and
  the relevant blind spots are concrete enough to eval against.

The 2-week sprint covers content depth + a minimal web UI; then
the project is frozen. After freeze, the author moves time to SDE
interview preparation (the reason narrowing happened in the first
place).

## 1. Versioning (revised)

| Version | Capability | Status |
|---|---|---|
| V1.0 | Single-domain 6-agent pipeline end-to-end | ✅ shipped |
| V1.x | Refine loop matured; eval baseline stable | ✅ closed at pivot |
| V2-orig | 10-domain build across the 4-layer model | ⛔ **deprecated 2026-05-18** |
| **V2-narrow** | Single vertical `cn-sde-jobhunt` reaches depth | 🟡 in progress |
| **V3-ui** | Minimal browsable web UI with streaming + citations | ⬜ pending |
| **V4-freeze** | Pin, document, tag, archive; disable refine cron | ⬜ pending |

V2-orig content (tech-career, immigration, housing, health-insurance,
personal-finance, entrepreneurship, education-funding) is **archived
under `domain_knowledge/_archive/`**. It remains readable as the
project's history but the runtime does not load it. The `tech-career`
and `immigration` archives are explicitly cited as source material
when authoring `cn-sde-jobhunt` content — they overlap heavily but
their framings and blindspots are *not* CN-student-specific.

## 2. How to read the progress tracker

Each version section below contains:

```
Status: ⬜ not started | 🟡 in progress | ✅ complete
Progress: ████░░░░░░░░░░░░░░░░ 20% (N/M)
Last completed: <git SHA or task slug>
Next up: <single concrete sub-task>
```

The progress bar **is the contract**. Update it when a checkbox flips
`[ ]` → `[x]`. A sub-task is `[x]` only when its definition-of-done
bullets all pass.

## 3. The vertical: `cn-sde-jobhunt`

Slug: `cn-sde-jobhunt`. Single domain folder: `domain_knowledge/cn-sde-jobhunt/`.

**In scope:**

- Offer comparison under H1B-sponsorship constraint
  (FAANG vs unicorn vs Series B startup, willing-to-sponsor filter,
  green-card timeline implications).
- OPT / STEM OPT / cap-gap timing decisions.
- H1B lottery strategy (multiple registrations, alternative paths
  if not selected — O1, L1 transfer, day-1-CPT risk, study back to
  F1).
- Employer switch mid-PERM / mid-I-140, AC21 portability mechanics.
- Layoff response under visa-status pressure (60-day grace,
  H1B transfer timing, downgrade-to-F1 fallback).
- Return-to-China (海归) timing: when does ROI of staying flip
  negative given GC backlog, family pressure, geopolitics?
- Family-located optimization: spouse on H4-EAD, kids' schooling,
  parents' visiting visas.
- Long-term-career-capital vs short-term-comp framing under
  visa-security constraint.
- Conversion decisions: PhD-to-industry, postdoc-to-industry,
  switching majors mid-degree to extend OPT.

**Out of scope (Triage refuses these):**

- General US tech career questions where visa status is irrelevant
  (those are the deprecated V2 `tech-career` domain).
- General US immigration questions for non-student paths
  (family-sponsored, asylum, EB-5 — out of scope).
- Decisions for non-CN international students (Indian, European,
  etc.) — the moat is CN-specific community knowledge, so the
  answers degrade outside that population.
- Anything not in the bullet list above.

**Communities (Layer 0):**

1. `oneponethreeacres` — 一亩三分地 (the dominant Chinese-language
   forum for US tech career + visa + life-in-US).
2. `reddit-us-tech-collective` — r/cscareerquestions, r/csMajors,
   r/leetcode (English-language tech career baseline).
3. `us-immigration-counsel` — immigration-attorney blogs (Murthy,
   Boundless, Reddy, Klasko) + r/immigration / r/h1b
   for legal-mechanic grounding.
4. `china-returnee-voices` — 海归 perspectives on returning to
   China after US tech work (Zhihu, WeChat blogs, podcast voices
   like 硅谷101 / 软实力).

Each community has known blind spots; the Risk Officer cross-checks
them. Diversity constraint caps any single community at 2 of the 5
selected source-views per turn — the same V1 mechanism.

## 4. V2-narrow — Build the `cn-sde-jobhunt` vertical to depth

**Capability jump:** the system answers CN-SDE-student-specific
decisions with citations from all 4 community classes, eval
quality_score ≥ 0.75 over ≥ 8 fixtures across 3 consecutive runs.

### Status

```
Status: 🟡 in progress
Progress: █████████████░░░░░░░ 67% (8/12)
Last completed: aff17ff — sources.yaml D8 single-community gap closure via NEW source-view 1p3a-phd-to-industry-threads (community_tag: oneponethreeacres; D8 1→2 communities, D10 1→2 communities side-effect; deferred static-corpus placeholder at data/static/1p3a-phd-to-industry-curated.md per ROADMAP §9 manual-curation rule) + 2 net-new V2 fixtures filling thinnest per-decision gaps (solo-h1b-layoff-60-day-clock D5 net-new persona laid-off-on-h1b without spouse coupling; newgrad-sponsor-willing-vs-faang-no-sponsor D1+D12 TC-vs-visa arithmetic distinct from bilingual code-switching angle; live-eval count 20 → 22) + tag-taxonomy 6 edge-case seeds (3 risk_surface: f1-opt-unemployment-cap, ead-renewal-gap, i-485-ac21-180day-rule; 2 persona: h-1b-laid-off-second-grace-period, married-to-citizen-mid-eb; 1 entity: I-140-revocation-window) (structural depth round; no checkbox flip)
Next up: cn-sde-jobhunt/decisions.md — author Layer 1 paragraph content (voice work, user-authored only per SKILL.md §5)
```

### Per-task checklist

Knowledge content — Layers 1–4 of `cn-sde-jobhunt/`:

- [ ] **decisions.md** (Layer 1) — ≥10 decisions specific to the
  vertical (not generic SDE comp, not generic visa). Cover:
  - Offer comparison under sponsorship-willingness filter
  - OPT/STEM-OPT/cap-gap timing
  - H1B lottery backup paths
  - Employer switch mid-PERM (AC21 §106(c) portability)
  - Layoff response under visa-status pressure
  - Return-to-China timing
  - Family-located optimization (H4-EAD, schooling)
  - PhD/postdoc-to-industry conversion
  - Long-term-career-capital vs visa-security tradeoffs
  - Sub-tasks: ≥10 entries each with name / scope / framing-axes /
    sample situations; cross-domain edges flagged inline.

- [ ] **framings.md** (Layer 2) — ≥3 framings per major decision.
  Anchor framings to name them up-front (each maps to one or more
  communities):
  - "Visa-security maximization" — 一亩三分地 dominant framing
  - "Long-term career capital" — Bay-Area-engineer-mentor framing
  - "Comp maximization in a 4-year window" — Levels-fyi / Blind framing
  - "Return-to-China optionality" — 海归 / China-tech framing
  - "Family-located optimization" — H4-EAD-spouse + parent-visa framing
  - "Legal-mechanic rigor" — immigration-counsel framing

- [ ] **blindspots.md** (Layer 3) — ≥5 blindspots per framing. Each
  entry: statement / framing-anchor / trigger-situation / recovery
  move. Hand-authored from real evidence (1p3a threads, Reddit posts,
  attorney blog case studies). No generic LLM-generated bullets.

- [x] **sources.yaml** (Layer 4) — ≥12 source-views across ≥4
  community_tags. Mix RSS, Reddit, static-corpus (for 1p3a threads
  the author curates manually — 1p3a is hostile to automated scraping,
  so this stays static). Voice-anchor coverage from framings.
  *Done at pivot: 15 source-views across all 4 communities.*

- [x] **communities/** — one profile per community-tag (4 files
  matching §3): Voice / Mental model / Typical concerns / Known
  blind spots OF this community. 250–500 words each, per
  `community_profiles/_schema.md`. *Done at pivot: all 4 profiles
  authored (5–7 KB each).*

- [x] **fixtures/** — ≥10 eval fixtures. Cover all 4 communities, the
  ~10 decisions, and ≥6 distinct personas (first-time-OPT, post-PhD,
  laid-off-on-H1B, GC-backlog-considering-return, etc.). *Done
  2026-05-18 21:54 UTC via PR #96: 10 per-fixture YAMLs covering
  D1-D12 across the 4 communities and 6+ personas.*

- [x] **domain_pack.md** — Triage / Editor / Critic system-prompt
  overrides. Mechanism E (high-stakes referral) applies: Editor
  labels visa-decision output "decision-support, not legal advice"
  and routes to a named immigration-attorney channel. Editor
  bilingual posture: respond in the user's input language by
  default — Chinese in, Chinese out; English in, English out.
  Citations stay in source language. *Done at pivot: 119 lines,
  all three sections within the ≤300-words-per-section bar.*

Infra & data:

- [x] **Triage prompts updated** — `src/blindspot/prompts/triage.md`
  and `triage_pass1.md` narrowed to single in-scope domain
  (`cn-sde-jobhunt`). Pass-1 returns `["cn-sde-jobhunt"]` or `[]`;
  Pass-2 extracts the vertical-specific facets. Out-of-scope
  situations return all-empty arrays → orchestrator refuses.
  *Done at pivot.*

- [x] **Source registry replaced** — `data/source_registry.yaml`
  rewritten with the 4 communities' source-views. Old registry
  archived under `data/_archive/source_registry-v1.yaml`.
  *Done at pivot.*

- [x] **Tag taxonomy replaced** — `data/tag_taxonomy_seed.yaml`
  rewritten with vertical-specific facets (entities like
  `H1B`, `OPT`, `STEM-OPT`, `AC21`, `I-140`, `EB-2-NIW`, `cap-gap`;
  personas like `f1-final-year`, `post-opt-h1b-lottery`,
  `mid-PERM-employer-switch`, `gc-backlog-considering-return`).
  *Done at pivot.*

- [x] **Eval fixtures replaced** — `fixtures/eval_situations.yaml`
  replaced with cn-sde-jobhunt situations. Old fixtures archived.
  *Done at pivot (13 situations); extended 2026-05-18 21:54 UTC
  via PR #95 to 16 situations.*

- [ ] **Eval pass on cn-sde-jobhunt** — `./bin/blindspot eval`
  produces `quality_score` ≥ 0.75 over ≥ 8 of the new fixtures
  across 3 consecutive `main` runs within ±0.03 of each other.

### Entry gate

Already met. The pivot commit on 2026-05-18 closes V1.x and opens
V2-narrow with `Status: 🟡`.

### Exit criteria

All 13 checklist items above are `[x]`. Then promote V3-ui from
`⬜` to `🟡` and set its Next up to the first sub-task.

### Notes for refine

The refine skill (`.claude/skills/refine-blindspot/SKILL.md`) has
been rewritten for this narrow scope. The hourly cron, when (and
if) the user re-enables it, works ONLY on the V2-narrow checklist
above. It does not propose new domains, does not edit anything
under `_archive/`, does not expand scope.

The four detail layers from the old skill map cleanly onto this
narrow plan: Sources & knowledge → Layer 1-4 authoring; Agents →
prompt narrowing + critic tuning; Config → scoring weights for the
new entities; Eval → new fixtures + judge prompt tweaks.

## 5. V3-ui — Minimal browsable web UI

**Capability jump:** a portfolio-readable web demo. Anyone with the
repo URL can `docker compose up`, open `localhost:8080`, type a
situation, and watch the 6-agent pipeline run with hover-able
citations.

### Status

```
Status: ⬜ not started
Progress: ░░░░░░░░░░░░░░░░░░░░ 0% (0/7)
Last completed: —
Next up: pick stack — FastAPI + HTMX (recommended) vs FastAPI + minimal React
```

### Per-task checklist

- [ ] **HTTP wrapper** — `src/blindspot/web/app.py` (FastAPI):
  `POST /ask`, `GET /sessions/{id}`, `GET /sessions/{id}/turns`.
  Wraps the existing `orchestrator.run(situation, session_id)`
  without changing it.

- [ ] **Streaming editor output** — Editor agent streams tokens via
  Server-Sent Events. This was a V1.x checklist item that never
  closed; landing it here is the right time.

- [ ] **Single-page UI** — one `index.html` (HTMX if going minimal;
  React if the author wants the React reps for SDE interviews).
  Form: textarea for situation, Submit, agent-progress indicator,
  streaming response. No auth, no accounts.

- [ ] **Citation rendering** — `[doc-3]` markers in the response
  become hoverable tooltips showing the source title, URL, and a
  snippet. Click expands a side-panel with full source content.

- [ ] **Session history view** — UI lists past turns from the live
  SQLite DB; clicking one shows the full archived response. Enables
  the "continue session" demo path.

- [ ] **Docker packaging** — `Dockerfile` + `docker-compose.yml`
  for `docker compose up`. Volume mounts `~/.blindspot/` for the
  SQLite DB. Image tag `blindspot:portfolio`.

- [ ] **2-minute demo screencast** — walk through 3 example
  decisions: an offer-comparison case, a layoff-on-H1B case, a
  return-to-China case. Saved as `docs/demo/blindspot-demo.mp4`
  and linked from the portfolio README.

### Entry gate

V2-narrow exit criteria met.

### Exit criteria

All 7 checklist items `[x]`. Demo runs end-to-end from a clean
`docker compose up`. Then promote V4-freeze.

## 6. V4-freeze — Archive as portfolio artifact

**Capability jump:** the project becomes a frozen, citable thing.
No more changes. The README explains what it is and why it ended.

### Status

```
Status: ⬜ not started
Progress: ░░░░░░░░░░░░░░░░░░░░ 0% (0/6)
Last completed: —
Next up: pin pyproject.toml deps to exact versions
```

### Per-task checklist

- [ ] **Pin all dependencies** — `pyproject.toml` exact versions
  (no `>=` ranges). Commit a `uv.lock` or `requirements.txt`
  derived from the current `.venv`.

- [ ] **Disable refine cron** — remove any scheduled-tasks entry
  pointing at `refine-blindspot`. Move `.claude/skills/refine-blindspot/`
  to `archive/skills/refine-blindspot/` so the files remain for
  review but Claude Code no longer surfaces the skill.

- [ ] **Portfolio-grade README** — top-section explaining:
  - What the project does (one sentence).
  - The technically interesting parts: 6-agent pipeline,
    source-grounded citations, RAG with diversity constraint,
    eval-driven LLM-as-judge regression, autonomous refine loop
    (now disabled).
  - What it does NOT do, by design: universal scope, real-time
    chat, multi-user, production reliability.
  - Why it ended: scope-narrow for portfolio purposes; the author
    moved to SDE interview prep.
  - How to run the demo (`docker compose up`).
  - A link to the demo screencast.

- [ ] **Repo public + LICENSE** — flip GitHub repo to public
  (if not already). Add MIT or Apache-2 LICENSE.

- [ ] **Tag `v1.0-final`** on `main`. After tagging, no further
  commits.

- [ ] **Author retrospective** — `docs/retrospective.md`:
  ~500 words on what worked (multi-agent pipeline, source
  grounding, refine loop quality), what didn't (universal scope
  hubris, hostile sources stayed deferred, eval calibration drift),
  and what the author would do differently.

### Exit criteria

All 6 items `[x]`. The user does not invoke `./bin/blindspot`
again unless reviewing.

## 7. Cross-cutting principles (kept from the prior plan)

These survived the scope narrow because they're correct regardless
of breadth:

- **The 4-layer knowledge model** (decisions / framings / blindspots
  / source-views) is the right shape for the single vertical too.
  We're just building one column of the old 10-wide table.
- **The 6-agent pipeline** (Triage → Collection → Community Analysts
  → Risk Officer → Critic → Editor) is unchanged. Triage now refuses
  anything outside `cn-sde-jobhunt`; the rest of the pipeline runs
  the same way.
- **Source-grounding by `[doc-X]` citation markers** is unchanged.
  The Editor parses them; the Critic checks per-claim spot-check
  density. Visa decisions are high-stakes, so the Critic's
  grounding threshold stays at 80%+.
- **Mechanism E** (high-stakes professional-referral gating) applies
  to the new vertical. The Editor labels visa-decision output
  "decision-support, not legal advice" and routes to a named
  immigration-attorney channel when the situation calls for it.
- **Diversity constraint** (max 2 source-views per community per
  turn) is kept. With 4 communities and 12+ source-views, this
  forces at least 3 perspectives per response.

## 8. What the refine skill does after this pivot

The hourly refine cron, **when the user re-enables it**, works
ONLY on the V2-narrow checklist above. After V2-narrow exits,
the user manually runs refine for V3-ui infra sub-tasks (the
skill knows how to scaffold web routes too); after V3-ui exits,
the user kills the cron in V4-freeze.

The skill never:

- Proposes new vertical domains (the scope is frozen).
- Edits anything under `domain_knowledge/_archive/`,
  `data/_archive/`, or `fixtures/_archive/`.
- Touches the deprecated tech-career / immigration / housing /
  health-insurance / personal-finance / entrepreneurship /
  education-funding folders. They are out-of-runtime.

Detail-layer mapping from the old skill to this plan:

| Old layer | What it now does |
|---|---|
| Sources & knowledge | Author Layers 1–4 of `cn-sde-jobhunt/` |
| Agents | Narrow Triage to single vertical; tune analyst / risk-officer prompts for CN-student framings |
| Config & scoring | Re-tune `tag_match.weights` for the new entities; re-tune `critic.thresholds` after the new eval baseline lands |
| Eval | Author fixtures; tune judge prompts; cover all 6 personas |

Framework-level reflection is **disabled** — the framework is
frozen as part of the scope narrow. The skill no longer chooses
a 5th "framework" slot.

## 9. Honest limits

This roadmap explicitly does NOT plan for:

- **Multi-user, auth, real production** — out of scope. The demo
  is a local container.
- **Cross-domain frame-breaking** — V4 of the old plan. Killed.
- **Coverage beyond cn-sde-jobhunt** — Indian-student or
  European-student verticals would benefit from the same
  architecture but they require community knowledge the author
  doesn't have. Out of scope.
- **Hostile-scrape sources beyond what V1 deferred** — 1point3acres
  is loaded as static_corpus only; Blind, levels.fyi data, RedNote
  / 小红书 remain deferred.

## 10. Status summary

```
V1.0:      ✅ shipped
V1.x:      ✅ closed at pivot 2026-05-18
V2-orig:   ⛔ deprecated; content archived under domain_knowledge/_archive/
V2-narrow: 🟡 in progress (8/12)
V3-ui:     ⬜ pending (0/7)
V4-freeze: ⬜ pending (0/6)
```

Total remaining: 17 concrete sub-tasks across V2-narrow + V3-ui +
V4-freeze (8 V2-narrow items already complete: 7 carried by the
pivot commit + 1 via PR #96 on 2026-05-18 21:54 UTC). Target
completion 2026-06-01.
