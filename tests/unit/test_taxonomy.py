from datetime import datetime, timezone

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.models import Base, TagVocabularyRow
from blindspot.tags.taxonomy import add_or_merge_tag, seed_vocabulary


class StubEmbedder:
    """Returns deterministic vectors so we can pin similarity outcomes."""

    def __init__(self, mapping):
        self.mapping = mapping

    async def embed(self, texts):
        return [self.mapping.get(t, [0.0, 0.0, 1.0]) for t in texts]


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        yield s


@pytest.mark.asyncio
async def test_exact_match_returns_existing(db):
    db.add(
        TagVocabularyRow(
            facet="entity",
            tag="ISO",
            added_at=datetime.now(timezone.utc),
            embedding_blob=b"\x00",
            status="active",
        )
    )
    db.commit()
    cfg = Config()
    res = await add_or_merge_tag(db, StubEmbedder({}), cfg, "entity", "ISO")
    assert res.accepted_tag == "ISO"
    assert res.was_merged is False
    assert res.similarity == 1.0


@pytest.mark.asyncio
async def test_seed_populates_vocabulary(db):
    embedder = StubEmbedder({"ISO": [1.0, 0.0, 0.0], "RSU": [0.0, 1.0, 0.0]})
    await seed_vocabulary(db, embedder, {"entity": ["ISO", "RSU"]})
    rows = db.query(TagVocabularyRow).all()
    assert {r.tag for r in rows} == {"ISO", "RSU"}
