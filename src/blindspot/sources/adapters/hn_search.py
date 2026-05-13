"""Hacker News source adapter via Algolia HN search API (no auth)."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone

import httpx

from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class HNSearchAdapter:
    BASE = "https://hn.algolia.com/api/v1/search"

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        query = " ".join(ctx.entity_terms) or ctx.situation.raw_text[:100]
        min_points = int(view.fetch_config.get("min_points", 100))

        params = {
            "query": query,
            "tags": "story",
            "numericFilters": f"points>={min_points}",
            "hitsPerPage": 5,
        }
        async with httpx.AsyncClient(timeout=15.0) as client:
            r = await client.get(self.BASE, params=params)
            r.raise_for_status()
            data = r.json()

        out: list[Document] = []
        for hit in data.get("hits", []):
            doc_id = hashlib.sha256((view.id + str(hit["objectID"])).encode()).hexdigest()[:12]
            out.append(
                Document(
                    doc_id=f"doc-{doc_id}",
                    source_view_id=view.id,
                    community_tag=view.community_tag,
                    url=hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}",
                    title=hit.get("title", "")[:200],
                    content=(hit.get("story_text") or hit.get("title") or "")[:8000],
                    fetched_at=datetime.now(timezone.utc),
                    metadata={"points": str(hit.get("points", 0))},
                )
            )
        return out
