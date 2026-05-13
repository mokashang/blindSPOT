"""Tag-match scoring with diversity constraint.

Given the situation's tags and the registry of source-views, score every
source-view and return the top-N subject to the per-community cap.
"""

from __future__ import annotations

import numpy as np

from blindspot.config import Config
from blindspot.llm.base import Embedder
from blindspot.sources.base import SourceView
from blindspot.types import Facet, Situation


async def select_top_n(
    views: list[SourceView],
    situation: Situation,
    cfg: Config,
    embedder: Embedder,
) -> list[SourceView]:
    weights = cfg.tag_match.weights
    top_n = cfg.tag_match.top_n
    cap = cfg.tag_match.max_per_community

    sit_emb_list = await embedder.embed([situation.raw_text])
    note_embs = await embedder.embed([v.notes or v.id for v in views])
    sit_vec = np.asarray(sit_emb_list[0])
    note_mat = np.asarray(note_embs)

    def cosine(a, b):
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        return float(a @ b / (na * nb)) if na and nb else 0.0

    scored: list[tuple[float, SourceView]] = []
    for view, note_vec in zip(views, note_mat, strict=True):
        d = len(set(view.domains) & set(situation.tags.get(Facet.DOMAIN, [])))
        # Entity/risk/persona aren't first-class fields on SourceView yet — V1
        # approximates by mentions in the `notes` field. A later refinement
        # can add typed `entity_coverage` / `risk_coverage` / `persona_fit` lists.
        notes_lower = view.notes.lower()
        e_count = sum(1 for ent in situation.tags.get(Facet.ENTITY, []) if ent.lower() in notes_lower)
        r_count = sum(1 for r in situation.tags.get(Facet.RISK_SURFACE, []) if r.lower() in notes_lower)
        p_count = sum(1 for p in situation.tags.get(Facet.PERSONA, []) if p.lower() in notes_lower)

        sim = cosine(sit_vec, note_vec)
        score = (
            weights.domain * d
            + weights.entity * e_count
            + weights.risk_surface * r_count
            + weights.persona * p_count
            + weights.similarity * sim
        )
        score *= view.reliability / 3.0
        scored.append((score, view))

    scored.sort(key=lambda p: p[0], reverse=True)

    selected: list[SourceView] = []
    per_community: dict[str, int] = {}
    for _score, view in scored:
        if per_community.get(view.community_tag, 0) >= cap:
            continue
        selected.append(view)
        per_community[view.community_tag] = per_community.get(view.community_tag, 0) + 1
        if len(selected) >= top_n:
            break
    return selected
