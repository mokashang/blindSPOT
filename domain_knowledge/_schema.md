# Per-Domain Knowledge Writing Guide

## Purpose

This file defines **how to write** each per-domain folder under
`domain_knowledge/<slug>/`. It is the companion to
[`_meta_ontology.md`](./_meta_ontology.md): that file names *which*
domains exist; this file specifies the conventions for the four
knowledge layers that fill each domain — Layers 1–4 of the model in
[ROADMAP §3](../docs/specs/ROADMAP.md#3-the-4-layer-knowledge-model).
The file layout itself (which files exist per domain) is roadmap-level;
this guide governs only the authoring of those files. Read
`_meta_ontology.md` first (slug, scope, high-stakes flag, sample
decisions), then this file, then work in the order given in
"Authoring workflow" below.

## Per-file conventions

### `decisions.md` — Layer 1 (decision ontology)

V1 left this layer implicit (in the author's head); V2 makes it
explicit. Each entry:

- **Decision name** — short noun phrase, the way an insider would name
  it. Not "tax considerations" — `"Exercise ISOs early vs
  wait-and-pay-ordinary at IPO"`.
- **Scope** — one sentence on which subset of the domain this decision
  belongs to and which adjacent decisions it is NOT.
- **Framing-axes-covered** — the 2–4 dimensions any framing of this
  decision typically argues over (e.g. for ISO exercise: *AMT
  exposure / liquidity / dilution timing / ordinary-income clock*).
  Pointers only; the actual framings live in `framings.md`.
- **Sample situations** — 2–3 concrete situations (1–2 sentences
  each) where a user would be making this exact decision. Triage
  matches against these; vague situations hurt routing.

**Minimum 8 distinct decisions per domain** (per
[V2 §4 per-domain checklist](../docs/specs/ROADMAP.md#per-domain-checklist)).
Style: concrete and situation-grounded, never abstract. "Plan for
retirement" is not a decision; "401k contribution ordering vs HSA
priority when employer offers a partial match" is.

### `framings.md` — Layer 2 (framing library)

A framing is a lens — the way one community / tradition / profession
argues about a decision. Per entry:

- **Framing name** — short label (e.g. `"AMT-minimization framing"`,
  `"liquidity-preservation framing"`).
- **Decision it applies to** — name from `decisions.md`. One framing
  can apply to multiple decisions; list each.
- **Mental model summary** — 3–6 sentences: what someone in this
  framing takes for granted, axioms reasoned from, numbers or
  concepts that anchor the conversation.
- **Characteristic vocabulary** — 5–10 phrases this framing uses
  distinctively. Triage uses these to detect when the user is
  already inside this framing.
- **Excludes** — explicit list of what this framing *fails to see*.
  Load-bearing: this is the seed for Layer 3 (blindspots). Without
  it, blindspots have no anchor. 3–5 pointed bullets.

**Minimum 3 framings per major decision.** Only one framing means
either the decision is too narrow or the author hasn't listened to
enough adjacent communities. Major decisions usually have 3–5 live
framings in the wild.

### `blindspots.md` — Layer 3 (blindspot catalogue)

Per
[ROADMAP §5 Mechanism B](../docs/specs/ROADMAP.md#mechanism-b--layers-12-generation-decisions--framings),
Layer 3 is **LLM-weak** — blindspots are precisely what's
underrepresented in training data. V2 hand-writes them from real
evidence (community forum threads, user feedback, post-mortems), not
from LLM generation. Each entry:

- **Blindspot statement** — one sentence naming what is missed.
  Specific, not vague: not "people forget about taxes" but `"engineers
  who exercise during a public-co cliff event miss that AMT triggers
  in years where ISO FMV is more than ~2.5× strike, regardless of
  whether they sell."`
- **Framing it lives inside** — name from `framings.md`. A blindspot is
  always relative to a framing; without that anchor the entry is just
  trivia.
- **Situation pattern that triggers it** — 1–2 sentences describing
  the kind of user situation where this blindspot is most costly to
  miss. Triage / Risk Officer use this to match.
- **Concrete recovery move** — what the user can do once they see the
  blindspot. Specific action, not vague advice.

**Minimum 5 typical blind spots per framing.** Quality bar: a blindspot
entry should make an insider go "yeah, I've seen people fall into that
one." If it reads like a generic LLM bullet point, it does not belong
here.

### `sources.yaml` — Layer 4 (per-domain source-views)

Per source-view, these fields:

- `id` — kebab-case, globally unique. Example: `bogleheads-retirement-acct-ordering`.
- `community_tag` — the slug of a community profile under
  `communities/`. Must match an existing
  `communities/<community-tag>.md`; the registry loader rejects orphan tags.
- `tags` — flat list of decisions / framings / personas this source
  covers, drawn from `decisions.md` / `framings.md` / `_meta_ontology.md`.
- `reliability` — integer 1–5. 1 = unverified candidate; 5 = consistently
  cited, repeatedly hit-rated by users.
- `keyword_filter` — list of terms that should appear in a document for
  it to count as on-topic. Tightening this is one of the most common
  refine actions.
- `notes` — one-line moat statement: why THIS source is high-signal for
  THIS domain (not generic praise). What does it cover that the next-
  best source misses?

**Minimum 8 source-views per domain, with ≥ 4 distinct
`community_tag` values** (per
[V2 §4 per-domain checklist](../docs/specs/ROADMAP.md#per-domain-checklist)).
Concentrating all 8 source-views in one community defeats the
multi-perspective design.

### `communities/<community-tag>.md`

Community profiles, scoped under the domain folder rather than at the
repo root as in V1. Follow the existing
[`community_profiles/_schema.md`](../community_profiles/_schema.md)
exactly — same four required sections (Voice / Mental model / Typical
concerns / Known blind spots OF this community), same optional
sections, same 250–500 word target, same naming convention. The only
change between V1 and V2 is the **location**: top-level
`community_profiles/` becomes per-domain
`domain_knowledge/<domain>/communities/`.

### `fixtures/<id>.yaml`

Per fixture:

- `id` — kebab-case, unique within the domain.
- `text` — the user-facing situation prompt. 2–6 sentences, written
  the way a real user would type it (shorthand, lived context), not
  the way an evaluator would phrase it.
- `expected_domains` — list of domain slugs from
  [`_meta_ontology.md`](./_meta_ontology.md). Most fixtures resolve
  to one domain; cross-domain situations (especially anything
  touching `career-pivots`) list multiple.
- `expected_entities` — named entities (companies, regulators,
  programs) whose mention or relevance the judge expects.
- `expected_personas` — persona slugs matching the situation (e.g.
  `single-tech-worker`, `dual-income-family-with-kids`).
- `expected_risk_surfaces` — short list of risk areas a good answer
  must cover (e.g. `[liquidity, tax-timing, dilution]`).
- `domain:` — the *primary* domain slug from `_meta_ontology.md`.
  This is the folder the fixture lives under and the domain whose
  `domain_pack.md` Triage loads.

**Minimum 8 fixtures per domain.** Cover different personas and risk
surfaces — not 8 variants of the same decision.

### `domain_pack.md`

This file holds the Triage / Editor / Critic system-prompt overrides
scoped to the active domain. Per
[V2 §4 Architecture changes](../docs/specs/ROADMAP.md#architecture-changes),
Triage's pass-2 concatenates each active domain's `domain_pack.md` into
its system prompt. Format: three `##` subsections.

```markdown
## Triage
<additional instructions Triage gets when this domain is active —
domain-specific facets to extract, vocabulary to attend to,
decisions to surface>

## Editor
<voice and framing overrides — e.g. for high-stakes domains:
"Label the answer 'decision-support, not professional advice.'">

## Critic
<grounding-threshold tweaks and domain-specific claim categories
the Critic must verify; stricter for high-stakes domains>
```

Keep each subsection short (≤ 300 words). The generic agent prompts
already cover most behaviour; `domain_pack.md` is *delta*, not
duplication.

## Cross-file invariants

Enforced by the registry loader and by reviewers. Authors should
write to them from the start:

- **Decision names are the cross-reference key.** Decision names in
  `decisions.md` are the units that `framings.md`, `blindspots.md`,
  `sources.yaml` (`tags`), and `fixtures/*.yaml` (`expected_domains`
  and `expected_risk_surfaces`) reference. Rename one and every
  reference must move with it.
- **Community-tag closure.** Every `community_tag` in `sources.yaml`
  MUST have a matching `communities/<community-tag>.md` file in the
  same domain folder. The registry loader rejects orphan tags.
- **High-stakes propagation.** The `high_stakes: true` flag from
  `_meta_ontology.md` must propagate into `domain_pack.md`'s Critic
  (stricter grounding) and Editor ("decision-support, not
  professional advice" label) subsections per
  [ROADMAP §5 Mechanism E](../docs/specs/ROADMAP.md#mechanism-e--high-stakes-domain-gating).
- **Fixture domain matches folder.** Every fixture's `domain:` must
  be a slug present in `_meta_ontology.md` AND equal the enclosing
  folder's slug. Cross-domain fixtures list additional slugs in
  `expected_domains`; primary `domain:` is always the home folder.

## Maturity progression

Each domain carries a `maturity` field in its frontmatter (typically
in `decisions.md` or a small `_meta.yaml`). Allowed values, per
[ROADMAP §5 Mechanism B](../docs/specs/ROADMAP.md#mechanism-b--layers-12-generation-decisions--framings):

- `planned` — domain is named in `_meta_ontology.md` but folder is
  empty or stub. Runtime ignores this domain.
- `in-migration` — V2 is converting V1 artifacts into the new layout.
  Currently applies to `tech-career` only (the others were `planned`
  from day one).
- `experimental` — folder has draft content (typically V3-grown via
  Mechanism B). Runtime uses the content but Editor surfaces a caveat
  on any answer sourced from it.
- `stable` — fully hand-authored and reviewed; runtime uses without
  caveat.

V2's job is to bring all 10 domains to `stable` by hand. V3 grows
new domains starting at `experimental` and promotes to `stable` only
on accumulated evidence (≥ N positive ratings or explicit human
approval). Refine routine never auto-promotes maturity; that is a
deliberate human step.

## Quality bar

Writing for Blindspot is **voice work**, not encyclopedic listing.
Each file must surface what an *insider* would consider
obvious-but-uncomfortable — what the community knows but rarely says
to outsiders unprompted. Vague entries ("be careful about taxes",
"consider the long-term impact") are worse than no entries: they
dilute the signal Triage routes on and crowd out the entry that
would actually help. The bar is the specific framing: "the AMT cliff
in years where ISO FMV > strike × 2.5 catches engineers who exercise
during a public-co cliff event and forget the parallel calculation."
If you cannot make an entry specific enough to make an insider nod,
leave it out.

## Authoring workflow

When opening a new (or in-migration) domain folder, work in this
order. Later files reference earlier ones, so this order minimizes
rework.

1. Read `_meta_ontology.md` to confirm slug, scope, high-stakes flag,
   and sample decisions.
2. Draft `sources.yaml` first. Layer 4 grounds the rest — knowing
   *which voices you can cite* shapes which decisions and framings
   you'll find evidence for. Hit the ≥ 8 / ≥ 4 minimums up front.
3. `decisions.md`. Use the sample decisions in `_meta_ontology.md` as
   seeds; widen to ≥ 8 based on what `sources.yaml` covers well.
4. `framings.md`. For each major decision, name the 3+ framings the
   sources you collected actually argue from.
5. `blindspots.md`. Sweep the `Excludes` lines from every framing —
   each is a candidate blindspot. Promote ≥ 5 per framing, grounded
   in source evidence (not LLM extrapolation).
6. `fixtures/`. Write ≥ 8 fixtures spanning different personas and
   risk surfaces — routing tests as well as quality tests.
7. `domain_pack.md` last. The Triage / Editor / Critic overrides need
   the other files solid before you know what overrides are needed.

## Update policy

Edits to this writing guide go through normal refine review (PR +
auto-reviewer). The **file layout itself** (which files exist per
domain) is roadmap-level: changing it means editing
[ROADMAP §3 "File layout"](../docs/specs/ROADMAP.md#file-layout-v2-introduces-this),
not this file. If a refine attempt thinks a new per-domain file is
needed (e.g. a `personas.yaml`), it must propose the change in
ROADMAP.md first; this guide updates only after the layout change is
merged.
