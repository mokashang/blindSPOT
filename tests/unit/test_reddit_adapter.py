def test_imports_when_env_set(monkeypatch):
    monkeypatch.setenv("REDDIT_CLIENT_ID", "x")
    monkeypatch.setenv("REDDIT_CLIENT_SECRET", "y")
    from blindspot.sources.adapters.reddit_search import RedditSearchAdapter

    assert RedditSearchAdapter is not None
