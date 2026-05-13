from unittest.mock import AsyncMock, patch

import pytest

from blindspot.sources.adapters.hn_search import HNSearchAdapter
from blindspot.sources.base import SourceView
from blindspot.types import SearchContext, Situation


@pytest.mark.asyncio
async def test_hn_adapter_maps_hits_to_documents():
    fake_resp = type(
        "R",
        (),
        {
            "json": lambda self: {
                "hits": [
                    {
                        "objectID": "42",
                        "title": "ISO basics",
                        "url": "https://x",
                        "points": 200,
                    }
                ]
            },
            "raise_for_status": lambda self: None,
        },
    )()
    with patch("blindspot.sources.adapters.hn_search.httpx.AsyncClient") as Cls:
        Cls.return_value.__aenter__.return_value.get = AsyncMock(return_value=fake_resp)
        view = SourceView(
            id="hn",
            adapter="hn_search",
            fetch_config={"min_points": 100},
            community_tag="hn-collective",
        )
        ctx = SearchContext(situation=Situation(raw_text=""), entity_terms=["ISO"])
        out = await HNSearchAdapter().fetch(view, ctx)
    assert len(out) == 1
    assert out[0].title == "ISO basics"
