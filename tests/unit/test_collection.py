from datetime import datetime, timezone

import pytest

from blindspot.agents import collection
from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext, Situation


class StubAdapter:
    def __init__(self, docs):
        self._docs = docs

    async def fetch(self, view, ctx):
        return self._docs


def _doc(view_id):
    return Document(
        doc_id="x",
        source_view_id=view_id,
        community_tag="t",
        url="u",
        title="t",
        content="c",
        fetched_at=datetime.now(timezone.utc),
    )


@pytest.mark.asyncio
async def test_collect_reassigns_sequential_doc_ids(monkeypatch):
    def fake_build(name, emb):
        return StubAdapter([_doc(name), _doc(name)])

    monkeypatch.setattr(collection, "build_adapter", fake_build)

    views = [
        SourceView(id="a", adapter="rss", fetch_config={}, community_tag="t"),
        SourceView(id="b", adapter="rss", fetch_config={}, community_tag="t"),
    ]
    ctx = SearchContext(situation=Situation(raw_text="x"), entity_terms=[])
    docs = await collection.collect(views, ctx, embedder=None)
    assert [d.doc_id for d in docs] == ["doc-1", "doc-2", "doc-3", "doc-4"]
