# 1point3acres (一亩三分地) — PhD-to-Industry Curated Threads

This file is a deferred static-corpus pointer pending manual curation
per `docs/specs/ROADMAP.md` §9 (hostile-scrape policy: 1point3acres
is loaded as `static_corpus` only because their ToS forbids automated
scraping and their bot-detection is aggressive). Content will be
hand-curated by the author from the 1p3a 博士 / 找工 / 跳槽 boards
over the V2-narrow sprint.

This corpus targets decision **D8** (PhD / postdoc-to-industry route
selection, including EB-1A / NIW evidentiary-bar discussions as 1p3a
askers themselves frame them — NOT as immigration counsel would frame
them) and decision **D10** (O-1 vs H-1B-lottery route selection,
to the extent post-defense PhD applicants discuss O-1 eligibility
on 1p3a). Persona anchor: `cs-phd-post-defense`.

## How to use

When the author encounters a 1p3a thread that exemplifies a typical
CN-PhD-to-industry decision pattern or surfaces a recurring blind
spot (e.g., postdoc-vs-industry-direct route choice; advisor
relations during the transition; CPT-during-PhD as a bridge to
industry; the EB-1A / NIW threads where 1p3a askers compare their
publication count and citation depth against the Dhanasar / Kazarian
bars), they:

1. Read the thread on 1point3acres.
2. Distill the load-bearing claims into 3–8 paragraphs here (their
   own paraphrase, not direct copy — respecting copyright).
3. Add a section header that includes the decision pattern (D8 /
   D10), the thread date, and a stable anchor for citation.

The Editor agent will cite chunks of this file as `[doc-X]` markers
just like any other source.

## Curation status

(Empty — author populates over the V2-narrow sprint. Until populated,
the `static_corpus` adapter at `src/blindspot/sources/adapters/static_corpus.py`
returns zero documents for this view; the source-view entry exists
so that the registry-level coverage shape is honest and the curation
pointer is durable. See `data/static/oneponethreeacres-curated.md`
for the parallel curation pattern on the offer / lottery / layoff
boards.)

## Caveat on F6 (Legal-mechanic-rigor) framing

1p3a's known blind spot (per `communities/oneponethreeacres.md` §
"Known blind spots") is that English-language adversarial /
contrarian framings — including immigration-attorney "consult counsel"
posture and self-petition route-choice (EB-1A / NIW) rigor — get
filtered through the community's own preferences. 1p3a askers DO
discuss EB-1A / NIW on the PhD-track threads (the EB-1A "凑材料"
genre is a recognizable subthread family), but the discussion is
applicant-anecdata-driven, not attorney-statute-driven. When the
curated content here is cited for F6 claims, the Editor / Critic
agents should cross-check against `murthy-newsletter-h1b-perm` or
`legacy-immigration-framings-corpus` for the statutory-rigor side
of the same claim. The tag `F6` on this source-view's entry in
`sources.yaml` reflects that 1p3a DOES touch F6 topics — not that
1p3a is the F6-rigor authority.
