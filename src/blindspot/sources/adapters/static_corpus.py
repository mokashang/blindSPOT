"""Static corpus adapter: chunk a local markdown file, retrieve top-K by embedding similarity."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from blindspot.llm.base import Embedder
from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class StaticCorpusAdapter:
    """Loads the corpus once, then serves top-K similarity matches."""

    def __init__(self, embedder: Embedder, chunk_size: int = 1500, top_k: int = 3):
        self._embedder = embedder
        self._chunk_size = chunk_size
        self._top_k = top_k
        self._cache: dict[str, tuple[list[str], np.ndarray]] = {}

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        path = Path(view.fetch_config["path"])
        chunks, embeds = await self._load(path)
        if not chunks:
            return []

        query = ctx.situation.raw_text
        query_emb_list = await self._embedder.embed([query])
        query_emb = np.array(query_emb_list[0])

        # Cosine similarity (voyage-3 returns normalized vectors).
        scores = embeds @ query_emb
        top_idx = np.argsort(scores)[-self._top_k :][::-1]

        out: list[Document] = []
        for idx in top_idx:
            chunk = chunks[idx]
            doc_id = hashlib.sha256((view.id + str(idx)).encode()).hexdigest()[:12]
            out.append(
                Document(
                    doc_id=f"doc-{doc_id}",
                    source_view_id=view.id,
                    community_tag=view.community_tag,
                    url=f"file://{path.resolve()}#chunk-{idx}",
                    title=f"{path.stem} chunk {idx}",
                    content=chunk,
                    fetched_at=datetime.now(timezone.utc),
                )
            )
        return out

    async def _load(self, path: Path) -> tuple[list[str], np.ndarray]:
        key = str(path)
        if key in self._cache:
            return self._cache[key]
        if not path.exists():
            self._cache[key] = ([], np.array([]))
            return self._cache[key]
        text = path.read_text()
        chunks = self._chunk(text)
        if not chunks:
            self._cache[key] = ([], np.array([]))
            return self._cache[key]
        embed_list = await self._embedder.embed(chunks)
        embeds = np.array(embed_list)
        self._cache[key] = (chunks, embeds)
        return self._cache[key]

    def _chunk(self, text: str) -> list[str]:
        # Naive paragraph-grouping chunker; good enough for V1.
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        chunks: list[str] = []
        cur = ""
        for p in paragraphs:
            if len(cur) + len(p) + 2 <= self._chunk_size:
                cur = f"{cur}\n\n{p}" if cur else p
            else:
                if cur:
                    chunks.append(cur)
                cur = p
        if cur:
            chunks.append(cur)
        return chunks
