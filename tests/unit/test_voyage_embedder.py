import pytest

import blindspot.llm.voyage_embedder as voyage_embedder
from blindspot.llm.voyage_embedder import VoyageEmbedder


@pytest.mark.asyncio
async def test_embed_empty_returns_empty(monkeypatch):
    monkeypatch.setenv("VOYAGE_API_KEY", "dummy")
    e = VoyageEmbedder()
    out = await e.embed([])
    assert out == []


def test_default_max_retries_is_nonzero(monkeypatch):
    """voyageai's own AsyncClient defaults max_retries=0 (no retry at all).

    Regression: a single Voyage RateLimitError crashed the whole pipeline
    because nothing retried. The embedder must opt into retries by default.
    """
    monkeypatch.setenv("VOYAGE_API_KEY", "dummy")
    captured = {}

    class FakeAsyncClient:
        def __init__(self, api_key=None, max_retries=0, **kw):
            captured["max_retries"] = max_retries

    monkeypatch.setattr(voyage_embedder.voyageai, "AsyncClient", FakeAsyncClient)
    VoyageEmbedder()
    assert captured["max_retries"] > 0


def test_max_retries_is_forwarded_to_client(monkeypatch):
    monkeypatch.setenv("VOYAGE_API_KEY", "dummy")
    captured = {}

    class FakeAsyncClient:
        def __init__(self, api_key=None, max_retries=0, **kw):
            captured["max_retries"] = max_retries

    monkeypatch.setattr(voyage_embedder.voyageai, "AsyncClient", FakeAsyncClient)
    VoyageEmbedder(max_retries=9)
    assert captured["max_retries"] == 9
