"""Tests for the V2-first / V1-fallback source-view loader."""

from __future__ import annotations

import textwrap

from blindspot.sources.registry import load_all_sources, load_registry


def _write_v1_yaml(path):
    """Write a minimal but well-formed V1 source_registry.yaml at ``path``."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        textwrap.dedent(
            """
            - id: pmck-equity
              adapter: rss
              fetch_config:
                feed: https://example.com/pmck/feed
                keyword_filter: [equity, ISO]
              domains: [tech-career/equity]
              community_tag: founder-engineer-bloggers
              reliability: 5
              freshness_required: false
              notes: |
                Patrick McKenzie blog. Salary negotiation gold standard.
            """
        ).lstrip()
    )


def test_v1_fallback_when_no_per_domain_files(tmp_path):
    """No domain_knowledge/<domain>/sources.yaml exists → returns same as load_registry."""
    # Stub V1 monolithic file at <tmp_path>/data/source_registry.yaml.
    legacy_yaml = tmp_path / "data" / "source_registry.yaml"
    _write_v1_yaml(legacy_yaml)

    # No domain_knowledge dir at all — pure V1 fallback path.
    via_all = load_all_sources(root=tmp_path)
    via_legacy = load_registry(legacy_yaml)

    # Bit-for-bit V1 preservation: same length, same fields per SourceView.
    assert len(via_all) == len(via_legacy) == 1
    for a, b in zip(via_all, via_legacy):
        assert a.id == b.id
        assert a.adapter == b.adapter
        assert a.fetch_config == b.fetch_config
        assert a.domains == b.domains
        assert a.community_tag == b.community_tag
        assert a.reliability == b.reliability
        assert a.freshness_required == b.freshness_required
        assert a.notes == b.notes


def test_v1_fallback_with_empty_domain_knowledge_dir(tmp_path):
    """An empty (or all-underscored) domain_knowledge dir still triggers V1 fallback."""
    legacy_yaml = tmp_path / "data" / "source_registry.yaml"
    _write_v1_yaml(legacy_yaml)

    # domain_knowledge exists but contains only underscored scaffolding.
    (tmp_path / "domain_knowledge").mkdir()
    (tmp_path / "domain_knowledge" / "_schema.md").write_text("# schema")

    via_all = load_all_sources(root=tmp_path)
    assert len(via_all) == 1
    assert via_all[0].id == "pmck-equity"


def test_v2_path_single_domain(tmp_path):
    """One domain_knowledge/foo/sources.yaml with 1 entry → returns 1 SourceView."""
    domain_yaml = tmp_path / "domain_knowledge" / "foo" / "sources.yaml"
    domain_yaml.parent.mkdir(parents=True)
    domain_yaml.write_text(
        textwrap.dedent(
            """
            - id: foo-source
              adapter: rss
              fetch_config:
                feed: https://example.com/foo/feed
              domains: [foo/topic]
              community_tag: foo-community
              reliability: 4
              notes: Test V2 source.
            """
        ).lstrip()
    )

    views = load_all_sources(root=tmp_path)
    assert len(views) == 1
    v = views[0]
    assert v.id == "foo-source"
    assert v.adapter == "rss"
    assert v.community_tag == "foo-community"
    assert v.reliability == 4
    assert v.domains == ["foo/topic"]
    assert v.notes == "Test V2 source."


def test_v2_path_multiple_domains(tmp_path):
    """Two per-domain sources.yaml files each with 1 entry → returns 2 entries."""
    foo_yaml = tmp_path / "domain_knowledge" / "foo" / "sources.yaml"
    foo_yaml.parent.mkdir(parents=True)
    foo_yaml.write_text(
        textwrap.dedent(
            """
            - id: foo-source
              adapter: rss
              fetch_config: {}
              community_tag: foo-community
              reliability: 4
              notes: foo notes.
            """
        ).lstrip()
    )

    bar_yaml = tmp_path / "domain_knowledge" / "bar" / "sources.yaml"
    bar_yaml.parent.mkdir(parents=True)
    bar_yaml.write_text(
        textwrap.dedent(
            """
            - id: bar-source
              adapter: hn_search
              fetch_config: {}
              community_tag: bar-community
              reliability: 3
              notes: bar notes.
            """
        ).lstrip()
    )

    views = load_all_sources(root=tmp_path)
    ids = {v.id for v in views}
    assert ids == {"foo-source", "bar-source"}
    assert len(views) == 2
    # Each must be well-formed (every field a SourceView expects must be populated).
    for v in views:
        assert v.id
        assert v.adapter
        assert v.community_tag
        assert isinstance(v.fetch_config, dict)
        assert isinstance(v.domains, list)
        assert isinstance(v.reliability, int)


def test_underscored_subdirectory_excluded(tmp_path):
    """domain_knowledge/_meta/sources.yaml must NOT be loaded.

    Only real domain subdirs (no leading underscore) contribute. With ONLY
    underscored scaffolding present, the V1 fallback path is used.
    """
    meta_yaml = tmp_path / "domain_knowledge" / "_meta" / "sources.yaml"
    meta_yaml.parent.mkdir(parents=True)
    meta_yaml.write_text(
        textwrap.dedent(
            """
            - id: meta-source
              adapter: rss
              fetch_config: {}
              community_tag: meta-community
              reliability: 1
              notes: Should NOT appear.
            """
        ).lstrip()
    )

    legacy_yaml = tmp_path / "data" / "source_registry.yaml"
    _write_v1_yaml(legacy_yaml)

    views = load_all_sources(root=tmp_path)
    ids = {v.id for v in views}
    # _meta is excluded → V1 fallback path is taken → only pmck-equity present.
    assert "meta-source" not in ids
    assert ids == {"pmck-equity"}


def test_v2_path_shadows_v1_with_warning(tmp_path, capsys):
    """When BOTH V1 and V2 exist, V2 wins and a warning names the shadowed V1 file."""
    foo_yaml = tmp_path / "domain_knowledge" / "foo" / "sources.yaml"
    foo_yaml.parent.mkdir(parents=True)
    foo_yaml.write_text(
        textwrap.dedent(
            """
            - id: foo-source
              adapter: rss
              fetch_config: {}
              community_tag: foo-community
              reliability: 4
              notes: V2 wins.
            """
        ).lstrip()
    )
    legacy_yaml = tmp_path / "data" / "source_registry.yaml"
    _write_v1_yaml(legacy_yaml)

    views = load_all_sources(root=tmp_path)
    ids = {v.id for v in views}

    # V2 wins — V1's pmck-equity is shadowed.
    assert ids == {"foo-source"}
    captured = capsys.readouterr()
    assert "source_registry.yaml" in captured.err
    assert "shadow" in captured.err.lower() or "precedence" in captured.err.lower()


def test_real_v1_registry_returns_13_views():
    """End-to-end: against the committed repo state, load_all_sources matches load_registry."""
    # The repo currently has NO domain_knowledge/<domain>/sources.yaml files —
    # only _meta_ontology.md and _schema.md under domain_knowledge/.
    # So load_all_sources() with no args (cwd=repo root) must hit the V1
    # fallback and return the same 13 SourceViews as the existing test.
    via_all = load_all_sources()
    via_legacy = load_registry()
    assert len(via_all) == len(via_legacy) == 13
    assert {v.id for v in via_all} == {v.id for v in via_legacy}
