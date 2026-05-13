"""Tag vocabulary CRUD with embedding-based auto-normalization.

When a new tag is proposed (by the Triage Officer):
  1. Embed it.
  2. Find the most similar existing tag in the same facet.
  3. If max similarity > threshold → return the existing tag (merge).
  4. Else → insert new tag + write tag_audit row.
"""

from __future__ import annotations

import io
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timezone

import numpy as np
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.models import TagAuditRow, TagVocabularyRow
from blindspot.llm.base import Embedder


@dataclass
class TagResolution:
    facet: str
    accepted_tag: str        # the tag actually used (may be merged)
    was_merged: bool
    similarity: float | None


def _pack(vec: list[float]) -> bytes:
    arr = np.asarray(vec, dtype=np.float32)
    buf = io.BytesIO()
    np.save(buf, arr)
    return buf.getvalue()


def _unpack(blob: bytes) -> np.ndarray:
    return np.load(io.BytesIO(blob))


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(a @ b / (na * nb))


async def seed_vocabulary(
    db: Session, embedder: Embedder, seed: dict[str, list[str]]
) -> None:
    """Seed the tag_vocabulary table from data/tag_taxonomy_seed.yaml content."""
    pairs: list[tuple[str, str]] = [
        (facet, tag) for facet, tags in seed.items() for tag in tags
    ]
    texts = [t for _, t in pairs]
    embeds = await embedder.embed(texts) if texts else []
    now = datetime.now(timezone.utc)
    for (facet, tag), emb in zip(pairs, embeds, strict=True):
        existing = db.query(TagVocabularyRow).filter_by(facet=facet, tag=tag).first()
        if existing:
            continue
        db.add(
            TagVocabularyRow(
                facet=facet,
                tag=tag,
                added_at=now,
                embedding_blob=_pack(emb),
                status="active",
            )
        )
    db.commit()


async def add_or_merge_tag(
    db: Session,
    embedder: Embedder,
    cfg: Config,
    facet: str,
    candidate: str,
    turn_id: int | None = None,
) -> TagResolution:
    """Insert a new tag or merge into the closest existing one."""

    candidate = candidate.strip()
    if not candidate:
        return TagResolution(facet=facet, accepted_tag="", was_merged=False, similarity=None)

    exact = db.query(TagVocabularyRow).filter_by(facet=facet, tag=candidate).first()
    if exact is not None:
        return TagResolution(
            facet=facet, accepted_tag=candidate, was_merged=False, similarity=1.0
        )

    threshold = cfg.normalization.embedding_similarity_threshold
    candidate_emb_list = await embedder.embed([candidate])
    candidate_emb = np.asarray(candidate_emb_list[0])

    rows: Iterable[TagVocabularyRow] = (
        db.query(TagVocabularyRow).filter_by(facet=facet, status="active").all()
    )

    best: tuple[float, TagVocabularyRow | None] = (0.0, None)
    for r in rows:
        sim = _cosine(candidate_emb, _unpack(r.embedding_blob))
        if sim > best[0]:
            best = (sim, r)

    if best[1] is not None and best[0] >= threshold:
        db.add(
            TagAuditRow(
                facet=facet,
                proposed_tag=candidate,
                accepted_tag=best[1].tag,
                similarity_to_existing=best[0],
                turn_id=turn_id,
                timestamp=datetime.now(timezone.utc),
            )
        )
        db.commit()
        return TagResolution(
            facet=facet, accepted_tag=best[1].tag, was_merged=True, similarity=best[0]
        )

    db.add(
        TagVocabularyRow(
            facet=facet,
            tag=candidate,
            added_at=datetime.now(timezone.utc),
            embedding_blob=_pack(candidate_emb.tolist()),
            status="active",
        )
    )
    db.add(
        TagAuditRow(
            facet=facet,
            proposed_tag=candidate,
            accepted_tag=candidate,
            similarity_to_existing=best[0],
            turn_id=turn_id,
            timestamp=datetime.now(timezone.utc),
        )
    )
    db.commit()
    return TagResolution(
        facet=facet, accepted_tag=candidate, was_merged=False, similarity=best[0]
    )
