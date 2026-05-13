import pytest

from blindspot.sources.adapters.static_corpus import StaticCorpusAdapter
from blindspot.sources.base import SourceView
from blindspot.types import SearchContext, Situation


class StubEmbedder:
    async def embed(self, texts):
        return [[float(ord(t[0])) if t else 0.0] for t in texts]


@pytest.mark.asyncio
async def test_static_corpus_returns_top_k(tmp_path):
    f = tmp_path / "c.md"
    f.write_text("AAA paragraph one.\n\nBBB paragraph two.\n\nCCC paragraph three.")
    view = SourceView(
        id="hg",
        adapter="static_corpus",
        fetch_config={"path": str(f)},
        community_tag="ref",
    )
    ctx = SearchContext(situation=Situation(raw_text="CCC related question"), entity_terms=[])
    adapter = StaticCorpusAdapter(StubEmbedder(), chunk_size=100, top_k=1)
    out = await adapter.fetch(view, ctx)
    assert len(out) == 1
    assert "CCC" in out[0].content


@pytest.mark.asyncio
async def test_missing_file_returns_empty(tmp_path):
    view = SourceView(
        id="x",
        adapter="static_corpus",
        fetch_config={"path": "/nonexistent"},
        community_tag="ref",
    )
    ctx = SearchContext(situation=Situation(raw_text="q"), entity_terms=[])
    adapter = StaticCorpusAdapter(StubEmbedder())
    out = await adapter.fetch(view, ctx)
    assert out == []
