"""Reddit source adapter using PRAW (script-app credentials)."""

from __future__ import annotations

import asyncio
import hashlib
import os
from datetime import datetime, timezone

import praw

from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class RedditSearchAdapter:
    def __init__(self):
        self._reddit = praw.Reddit(
            client_id=os.environ["REDDIT_CLIENT_ID"],
            client_secret=os.environ["REDDIT_CLIENT_SECRET"],
            user_agent=os.environ.get("REDDIT_USER_AGENT", "blindspot/0.1 by /u/local"),
        )

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        subreddit_name = view.fetch_config["subreddit"]
        sort = view.fetch_config.get("sort", "top")
        time_window = view.fetch_config.get("time_window", "year")
        min_upvotes = int(view.fetch_config.get("min_upvotes", 0))

        query = " OR ".join(ctx.entity_terms) if ctx.entity_terms else ""

        return await asyncio.to_thread(
            self._fetch_sync, view, subreddit_name, query, sort, time_window, min_upvotes
        )

    def _fetch_sync(self, view, subreddit_name, query, sort, time_window, min_upvotes):
        sub = self._reddit.subreddit(subreddit_name)
        if query:
            results = sub.search(query, sort=sort, time_filter=time_window, limit=20)
        else:
            results = sub.top(time_filter=time_window, limit=20)
        out: list[Document] = []
        for post in results:
            if post.score < min_upvotes:
                continue
            content = (post.selftext or "")[:6000]
            top_comments = "\n\n".join(
                c.body
                for c in (post.comments[:3] if hasattr(post, "comments") else [])
                if hasattr(c, "body")
            )[:2000]
            doc_id = hashlib.sha256((view.id + post.id).encode()).hexdigest()[:12]
            out.append(
                Document(
                    doc_id=f"doc-{doc_id}",
                    source_view_id=view.id,
                    community_tag=view.community_tag,
                    url=f"https://reddit.com{post.permalink}",
                    title=post.title[:200],
                    content=f"{content}\n\n--- TOP COMMENTS ---\n{top_comments}",
                    fetched_at=datetime.now(timezone.utc),
                    metadata={"score": str(post.score), "comments": str(post.num_comments)},
                )
            )
            if len(out) >= 5:
                break
        return out
