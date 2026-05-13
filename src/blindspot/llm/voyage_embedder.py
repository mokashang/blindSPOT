"""Embedder using voyage-3."""

from __future__ import annotations

import os

import voyageai

from blindspot.llm.base import Embedder


class VoyageEmbedder(Embedder):
    def __init__(self, model: str = "voyage-3", api_key: str | None = None):
        self._client = voyageai.AsyncClient(api_key=api_key or os.environ["VOYAGE_API_KEY"])
        self._model = model

    async def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        resp = await self._client.embed(texts=texts, model=self._model, input_type="document")
        return resp.embeddings
