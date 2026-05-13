"""RSS source adapter. Pulls from a feed URL, filters by keyword whitelist."""

from __future__ import annotations

import asyncio
import hashlib
from datetime import datetime, timezone

import feedparser

from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class RSSAdapter:
    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        feed_url = view.fetch_config["feed"]
        keyword_filter = [k.lower() for k in view.fetch_config.get("keyword_filter", [])]

        feed = await asyncio.to_thread(feedparser.parse, feed_url)
        out: list[Document] = []
        for entry in feed.entries[:30]:
            text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
            if keyword_filter and not any(k in text for k in keyword_filter):
                continue
            content = self._extract_content(entry)
            doc_id = hashlib.sha256((view.id + entry.get("link", "")).encode()).hexdigest()[:12]
            out.append(
                Document(
                    doc_id=f"doc-{doc_id}",
                    source_view_id=view.id,
                    community_tag=view.community_tag,
                    url=entry.get("link", ""),
                    title=entry.get("title", "")[:200],
                    content=content[:8000],
                    fetched_at=datetime.now(timezone.utc),
                )
            )
        return out[:5]

    @staticmethod
    def _extract_content(entry) -> str:
        if "content" in entry and entry.content:
            return entry.content[0].value
        return entry.get("summary", "")
