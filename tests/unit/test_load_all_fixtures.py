"""Tests for the V2-first / V1-fallback eval-fixture loader.

Mirrors ``tests/unit/test_load_all_sources.py`` (PR #29) — same
architectural pattern: per-domain ``domain_knowledge/<domain>/fixtures/*.yaml``
preferred over legacy monolithic ``fixtures/eval_situations.yaml``,
with bit-for-bit V1 preservation when no per-domain files exist.

The committed repo state has NO per-domain fixture files yet (only
``domain_knowledge/tech-career/decisions.md`` and ``framings.md``), so
the V1 fallback path is the active production path. That is the most
important behavior to lock down — see ``test_real_v1_fixtures_match_legacy``.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import yaml

from blindspot.eval.runner import V1_LEGACY_DOMAIN, load_all_fixtures


def _write_v1_fixtures(path: Path) -> list[dict]:
    """Write a minimal but well-formed V1 ``fixtures/eval_situations.yaml`` at ``path``.

    Returns the raw dicts written (before the ``domain`` annotation the
    loader adds) so tests can assert round-trip equality on every field
    except the additive ``domain`` key.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = [
        {
            "id": "series-b-iso-cliff",
            "text": (
                "I got a Series B offer with 0.1% in ISOs over 4 years "
                "with a 1-year cliff. Take it?"
            ),
            "expected_domains": ["tech-career/equity"],
            "expected_entities": ["ISO", "series-B"],
        },
        {
            "id": "rsu-vs-base",
            "text": "Public co: $250k base + $400k RSUs. Which is better?",
            "expected_domains": ["tech-career/comp"],
            "expected_entities": ["RSU"],
        },
    ]
    path.write_text(yaml.safe_dump(raw))
    return raw


def test_v1_fallback_when_no_per_domain_files(tmp_path):
    """No domain_knowledge/<domain>/fixtures/ exists → returns legacy file annotated with domain=tech-career."""
    legacy = tmp_path / "fixtures" / "eval_situations.yaml"
    raw = _write_v1_fixtures(legacy)

    fixtures = load_all_fixtures(root=tmp_path)

    assert len(fixtures) == len(raw) == 2
    # Every loaded fixture is annotated with the V1 default domain.
    for loaded, source in zip(fixtures, raw):
        assert loaded["id"] == source["id"]
        assert loaded["text"] == source["text"]
        assert loaded["expected_domains"] == source["expected_domains"]
        assert loaded["expected_entities"] == source["expected_entities"]
        assert loaded["domain"] == V1_LEGACY_DOMAIN


def test_v1_fallback_with_empty_domain_knowledge_dir(tmp_path):
    """An empty domain_knowledge dir (no per-domain fixtures inside) still triggers V1 fallback."""
    legacy = tmp_path / "fixtures" / "eval_situations.yaml"
    _write_v1_fixtures(legacy)

    # domain_knowledge exists but contains only underscored scaffolding
    # and a domain dir with NO fixtures/ subfolder.
    (tmp_path / "domain_knowledge").mkdir()
    (tmp_path / "domain_knowledge" / "_schema.md").write_text("# schema")
    (tmp_path / "domain_knowledge" / "tech-career").mkdir()
    (tmp_path / "domain_knowledge" / "tech-career" / "decisions.md").write_text(
        "# decisions"
    )

    fixtures = load_all_fixtures(root=tmp_path)

    # V1 fallback active — legacy file's 2 fixtures returned.
    assert len(fixtures) == 2
    assert {f["domain"] for f in fixtures} == {V1_LEGACY_DOMAIN}


def test_v2_single_domain_single_file(tmp_path):
    """One domain_knowledge/foo/fixtures/test.yaml with 1 fixture → returns 1 entry annotated domain=foo."""
    fx_yaml = tmp_path / "domain_knowledge" / "foo" / "fixtures" / "test.yaml"
    fx_yaml.parent.mkdir(parents=True)
    fx_yaml.write_text(
        textwrap.dedent(
            """
            - id: foo-fixture-1
              text: A foo-domain situation.
              expected_domains: [foo/topic]
            """
        ).lstrip()
    )

    fixtures = load_all_fixtures(root=tmp_path)

    assert len(fixtures) == 1
    fx = fixtures[0]
    assert fx["id"] == "foo-fixture-1"
    assert fx["text"] == "A foo-domain situation."
    assert fx["expected_domains"] == ["foo/topic"]
    assert fx["domain"] == "foo"


def test_v2_single_fixture_top_level_mapping(tmp_path):
    """A fixture file containing a single top-level mapping (not a list) is supported."""
    fx_yaml = tmp_path / "domain_knowledge" / "foo" / "fixtures" / "solo.yaml"
    fx_yaml.parent.mkdir(parents=True)
    fx_yaml.write_text(
        textwrap.dedent(
            """
            id: solo-fixture
            text: A single-fixture file.
            """
        ).lstrip()
    )

    fixtures = load_all_fixtures(root=tmp_path)

    assert len(fixtures) == 1
    assert fixtures[0]["id"] == "solo-fixture"
    assert fixtures[0]["domain"] == "foo"


def test_v2_path_multiple_domains(tmp_path):
    """Two per-domain fixture files in different domains → returns merged with correct domain annotations."""
    foo_yaml = tmp_path / "domain_knowledge" / "foo" / "fixtures" / "a.yaml"
    foo_yaml.parent.mkdir(parents=True)
    foo_yaml.write_text(
        textwrap.dedent(
            """
            - id: foo-1
              text: foo situation 1
            - id: foo-2
              text: foo situation 2
            """
        ).lstrip()
    )

    bar_yaml = tmp_path / "domain_knowledge" / "bar" / "fixtures" / "b.yaml"
    bar_yaml.parent.mkdir(parents=True)
    bar_yaml.write_text(
        textwrap.dedent(
            """
            - id: bar-1
              text: bar situation 1
            """
        ).lstrip()
    )

    fixtures = load_all_fixtures(root=tmp_path)

    assert len(fixtures) == 3
    by_id = {f["id"]: f for f in fixtures}
    assert by_id["foo-1"]["domain"] == "foo"
    assert by_id["foo-2"]["domain"] == "foo"
    assert by_id["bar-1"]["domain"] == "bar"

    # Domain iteration is sorted, so 'bar' fixtures come before 'foo' fixtures
    # in the returned list. This is deterministic ordering, matching the
    # pattern in load_all_sources.
    assert [f["id"] for f in fixtures] == ["bar-1", "foo-1", "foo-2"]


def test_underscored_subdirectory_excluded(tmp_path):
    """domain_knowledge/_meta/fixtures/*.yaml must NOT be loaded — falls back to V1."""
    meta_yaml = tmp_path / "domain_knowledge" / "_meta" / "fixtures" / "x.yaml"
    meta_yaml.parent.mkdir(parents=True)
    meta_yaml.write_text(
        textwrap.dedent(
            """
            - id: should-not-appear
              text: This must be skipped because _meta is underscored.
            """
        ).lstrip()
    )

    legacy = tmp_path / "fixtures" / "eval_situations.yaml"
    _write_v1_fixtures(legacy)

    fixtures = load_all_fixtures(root=tmp_path)
    ids = {f["id"] for f in fixtures}

    # _meta is excluded → V1 fallback path is taken → only legacy fixtures present.
    assert "should-not-appear" not in ids
    assert ids == {"series-b-iso-cliff", "rsu-vs-base"}
    assert {f["domain"] for f in fixtures} == {V1_LEGACY_DOMAIN}


def test_v2_path_shadows_v1_with_warning(tmp_path, capsys):
    """When BOTH V1 and V2 exist, V2 wins and a warning names the shadowed V1 file."""
    fx_yaml = tmp_path / "domain_knowledge" / "foo" / "fixtures" / "x.yaml"
    fx_yaml.parent.mkdir(parents=True)
    fx_yaml.write_text(
        textwrap.dedent(
            """
            - id: foo-fixture
              text: V2 wins
            """
        ).lstrip()
    )
    legacy = tmp_path / "fixtures" / "eval_situations.yaml"
    _write_v1_fixtures(legacy)

    fixtures = load_all_fixtures(root=tmp_path)

    # V2 wins — V1 legacy entries are shadowed.
    ids = {f["id"] for f in fixtures}
    assert ids == {"foo-fixture"}

    captured = capsys.readouterr()
    assert "eval_situations.yaml" in captured.err
    assert "shadow" in captured.err.lower() or "precedence" in captured.err.lower()


def test_v2_multiple_files_per_domain(tmp_path):
    """Multiple .yaml files inside one domain's fixtures/ dir are all loaded and annotated."""
    base = tmp_path / "domain_knowledge" / "foo" / "fixtures"
    base.mkdir(parents=True)
    (base / "a.yaml").write_text(
        textwrap.dedent(
            """
            - id: a1
              text: from file a
            """
        ).lstrip()
    )
    (base / "b.yaml").write_text(
        textwrap.dedent(
            """
            - id: b1
              text: from file b
            """
        ).lstrip()
    )

    fixtures = load_all_fixtures(root=tmp_path)

    assert {f["id"] for f in fixtures} == {"a1", "b1"}
    assert {f["domain"] for f in fixtures} == {"foo"}


def test_no_files_anywhere_returns_empty_list(tmp_path):
    """Neither V2 per-domain nor V1 legacy exists → returns empty list, no crash."""
    fixtures = load_all_fixtures(root=tmp_path)
    assert fixtures == []


def test_real_v1_fixtures_match_legacy():
    """End-to-end: against the committed repo state, the tech-career SUBSET of load_all_fixtures is bit-for-bit equivalent to the V1 monolith.

    The repo has migrated to per-domain fixture files under
    ``domain_knowledge/<domain>/fixtures/*.yaml``; the V1 monolithic
    ``fixtures/eval_situations.yaml`` is retained as a fallback for code
    paths that still reference it by path, but ``load_all_fixtures()``
    with no args (cwd=repo root) now hits the V2 per-domain path and
    shadows the V1 file (a warning is printed when both exist).

    Once V2 added additional domains beyond ``tech-career`` (immigration
    being the first), the loaded list is no longer the same length as
    the V1 monolith — additional per-domain fixtures live alongside the
    migrated tech-career set. The V1-preservation invariant therefore
    scopes to the ``tech-career`` subset: filter loaded fixtures by
    ``domain == V1_LEGACY_DOMAIN`` before comparing to the legacy
    monolith. The tech-career subset must still match the monolith
    bit-for-bit (same ids, same texts) — that is the migration contract
    PR #34 established and that subsequent V2 buildout must preserve.
    Order is not asserted because V2 loads files in sorted filename
    order while the V1 monolith preserved authoring order.
    """
    fixtures = load_all_fixtures()
    legacy_raw = yaml.safe_load(Path("fixtures/eval_situations.yaml").read_text())

    tech_career_loaded = [f for f in fixtures if f["domain"] == V1_LEGACY_DOMAIN]

    assert len(tech_career_loaded) == len(legacy_raw)
    assert {f["id"] for f in tech_career_loaded} == {r["id"] for r in legacy_raw}
    # Texts preserved bit-for-bit per id.
    legacy_by_id = {r["id"]: r for r in legacy_raw}
    for loaded in tech_career_loaded:
        assert loaded["text"] == legacy_by_id[loaded["id"]]["text"]
