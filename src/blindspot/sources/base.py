"""SourceAdapter Protocol and SourceView dataclass."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from blindspot.types import Document, SearchContext


@dataclass
class SourceView:
    """A configured, annotated lens into one source — the unit of the registry."""

    id: str
    adapter: str                            # "rss" | "reddit_search" | "hn_search" | "static_corpus"
    fetch_config: dict[str, Any]
    domains: list[str] = field(default_factory=list)
    community_tag: str = ""
    reliability: int = 3                    # 1-5
    freshness_required: bool = False
    notes: str = ""


class SourceAdapter(Protocol):
    """Each adapter handles one type of source."""

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]: ...
