"""Collection: dispatch each selected source-view to its adapter, fetch in parallel."""

from __future__ import annotations

import asyncio
import logging

from blindspot.llm.base import Embedder
from blindspot.sources.adapters.hn_search import HNSearchAdapter
from blindspot.sources.adapters.reddit_search import RedditSearchAdapter
from blindspot.sources.adapters.rss import RSSAdapter
from blindspot.sources.adapters.static_corpus import StaticCorpusAdapter
from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


def build_adapter(adapter_name: str, embedder: Embedder | None):
    if adapter_name == "rss":
        return RSSAdapter()
    if adapter_name == "reddit_search":
        return RedditSearchAdapter()
    if adapter_name == "hn_search":
        return HNSearchAdapter()
    if adapter_name == "static_corpus":
        assert embedder is not None, "static_corpus requires an embedder"
        return StaticCorpusAdapter(embedder)
    raise ValueError(f"unknown adapter: {adapter_name}")


async def collect(
    views: list[SourceView], ctx: SearchContext, embedder: Embedder | None
) -> list[Document]:
    async def _fetch_one(view: SourceView) -> list[Document]:
        try:
            adapter = build_adapter(view.adapter, embedder)
            return await adapter.fetch(view, ctx)
        except Exception as e:
            logging.warning("source %s failed: %s", view.id, e)
            return []

    results = await asyncio.gather(*(_fetch_one(v) for v in views))
    docs = [d for batch in results for d in batch]

    # Reassign stable per-turn IDs in case adapters issued long/hash-based ones.
    for i, d in enumerate(docs, start=1):
        d.doc_id = f"doc-{i}"
    return docs
