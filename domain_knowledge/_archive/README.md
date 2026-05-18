# Deprecated domains — archived 2026-05-18

This directory holds 5 domain knowledge folders that were under
active construction as part of the original V1 → V5 plan (universal
cross-domain blind-spot tool, 10 life-decision domains). On
2026-05-18 the project was scope-narrowed to a single vertical —
`cn-sde-jobhunt` (Chinese international students in the US SDE
job-hunt) — and these 5 domains were dropped from runtime scope:

- `housing/` — rent vs buy, mortgage, location choice
- `health-insurance/` — US plan selection, HSA, COBRA, Medicare
- `personal-finance/` — retirement accounts, debt vs invest, taxes
- `entrepreneurship/` — founding, fundraising, co-founder structure
- `education-funding/` — student loans, grad-school ROI, 529 plans

They remain readable as the project's history but the runtime does
not load them. Triage refuses any situation matching these scopes.
The refine routine never edits anything under this directory; the
auto-reviewer rejects any PR that touches `_archive/**`.

If you want to revive this content in a future project, the file
layout follows `domain_knowledge/_schema.md` (decisions.md,
framings.md, blindspots.md, sources.yaml, communities/,
fixtures/, domain_pack.md).
