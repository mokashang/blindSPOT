from unittest.mock import patch

import pytest

from blindspot.sources.adapters.rss import RSSAdapter
from blindspot.sources.base import SourceView
from blindspot.types import SearchContext, Situation


@pytest.mark.asyncio
async def test_rss_adapter_filters_by_keyword():
    fake_feed = type(
        "F",
        (),
        {
            "entries": [
                {"title": "Equity tips", "summary": "ISO basics", "link": "u1"},
                {"title": "Unrelated", "summary": "cooking", "link": "u2"},
            ]
        },
    )()
    view = SourceView(
        id="x",
        adapter="rss",
        fetch_config={"feed": "u", "keyword_filter": ["equity", "ISO"]},
        community_tag="t",
    )
    ctx = SearchContext(situation=Situation(raw_text=""), entity_terms=[])

    with patch("blindspot.sources.adapters.rss.feedparser.parse", return_value=fake_feed):
        out = await RSSAdapter().fetch(view, ctx)
    assert len(out) == 1
    assert out[0].url == "u1"
