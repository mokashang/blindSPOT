import pytest

from blindspot.llm.voyage_embedder import VoyageEmbedder


@pytest.mark.asyncio
async def test_embed_empty_returns_empty(monkeypatch):
    monkeypatch.setenv("VOYAGE_API_KEY", "dummy")
    e = VoyageEmbedder()
    out = await e.embed([])
    assert out == []
