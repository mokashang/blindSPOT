from blindspot.sources.registry import load_registry


def test_loads_13_sourceviews_from_committed_yaml():
    views = load_registry()
    assert len(views) == 13
    assert {v.id for v in views} >= {
        "pmck-equity",
        "danluu-career",
        "pragmatic-engineer",
        "reddit-cscareerquestions-equity",
        "reddit-experienceddevs",
        "reddit-personalfinance-equity",
        "avc-fred-wilson",
        "hn-equity-discussions",
        "kb-financial-equity",
        "matt-levine-money-stuff",
        "carta-blog",
        "levels-fyi-blog",
        "holloway-equity-guide",
    }


def test_pmck_has_expected_fields():
    views = load_registry()
    pmck = next(v for v in views if v.id == "pmck-equity")
    assert pmck.adapter == "rss"
    assert pmck.reliability == 5
    assert pmck.community_tag == "founder-engineer-bloggers"
    assert "ISO" in " ".join(pmck.fetch_config.get("keyword_filter", []))
