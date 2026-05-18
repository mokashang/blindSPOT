# Legacy domains — upstream sources for cn-sde-jobhunt

This directory holds 2 domain knowledge folders that were under
active construction in the original V1 → V5 plan and have content
that overlaps heavily with the new `cn-sde-jobhunt` vertical:

- `tech-career/` — US knowledge-worker comp, equity, offers, layoff
  response, intra-industry job changes.
- `immigration/` — US visa status, green-card timing, status
  transitions, dependent visas.

On 2026-05-18 the project was scope-narrowed to `cn-sde-jobhunt`
(Chinese international students in the US, SDE-job-hunt + visa-
coupled career decisions). The new vertical is the *intersection*
of these two legacy domains plus a third axis (Chinese-language
community knowledge from 1point3acres + 海归 voices) that general
LLM training data underrepresents.

## How these get used

The new vertical's source-view registry
(`domain_knowledge/cn-sde-jobhunt/sources.yaml`) cites individual
files from this directory as `adapter: static_corpus` source-views.
Specifically:

- `_legacy/tech-career/blindspots.md` is a high-reliability source
  on tech-career mechanics (RSU mechanics, vesting cliffs, AMT on
  ISO exercise, layoff response, perf review pathology, etc.) —
  cited when a situation has tech-career framing-axes.
- `_legacy/immigration/blindspots.md` is a high-reliability source
  on US visa mechanics (H-1B / OPT / STEM-OPT timing, PERM, I-140,
  AC21 portability, AOS, etc.) — cited when a situation has
  immigration framing-axes.

The other files in these directories (decisions.md, framings.md,
sources.yaml, communities/, fixtures/, domain_pack.md) are NOT
loaded by the runtime — only the two `blindspots.md` files cited
above.

## Editing posture

Refine routine: NEVER edit anything under `_legacy/**`. The
auto-reviewer rejects any PR touching this directory. If the new
vertical needs additional knowledge from these legacy files,
update the new vertical's own knowledge files (decisions.md,
framings.md, blindspots.md, sources.yaml) — that's the path.

The legacy content is *frozen as authored*. Cite, don't mutate.
