"""Tests for the community-profile loader's V2 per-domain + V1 legacy fallback."""

from __future__ import annotations

import pytest

from blindspot.agents import base


def test_legacy_path_still_resolves_real_v1_profile():
    """A real V1 community_tag (nothing migrated yet) resolves via the legacy path."""
    content = base.load_community_profile("hn-collective")
    assert content  # non-empty
    # Sanity: it really is the V1 file content
    assert "hn" in content.lower() or "hacker" in content.lower()


def test_per_domain_path_takes_precedence_over_legacy(tmp_path, monkeypatch):
    """If both V1 and V2 copies exist for the same tag, V2 wins."""
    legacy_dir = tmp_path / "community_profiles"
    legacy_dir.mkdir()
    (legacy_dir / "foo.md").write_text("LEGACY V1 CONTENT")

    domain_dir = tmp_path / "domain_knowledge"
    (domain_dir / "tech-careers" / "communities").mkdir(parents=True)
    (domain_dir / "tech-careers" / "communities" / "foo.md").write_text("V2 PER-DOMAIN CONTENT")

    monkeypatch.setattr(base, "PROFILES_DIR", legacy_dir)
    monkeypatch.setattr(base, "DOMAIN_KNOWLEDGE_DIR", domain_dir)

    result = base.load_community_profile("foo")
    assert result == "V2 PER-DOMAIN CONTENT"


def test_multiple_per_domain_matches_pick_alphabetically_first_and_warn(
    tmp_path, monkeypatch, capsys
):
    """Same tag in two domains → pick alphabetically-first, warn to stderr naming both."""
    legacy_dir = tmp_path / "community_profiles"
    legacy_dir.mkdir()

    domain_dir = tmp_path / "domain_knowledge"
    # Create two domains that both claim "foo" — "alpha" should win alphabetically.
    (domain_dir / "alpha-domain" / "communities").mkdir(parents=True)
    (domain_dir / "alpha-domain" / "communities" / "foo.md").write_text("ALPHA CONTENT")
    (domain_dir / "beta-domain" / "communities").mkdir(parents=True)
    (domain_dir / "beta-domain" / "communities" / "foo.md").write_text("BETA CONTENT")

    monkeypatch.setattr(base, "PROFILES_DIR", legacy_dir)
    monkeypatch.setattr(base, "DOMAIN_KNOWLEDGE_DIR", domain_dir)

    result = base.load_community_profile("foo")
    assert result == "ALPHA CONTENT"

    captured = capsys.readouterr()
    assert "alpha-domain" in captured.err
    assert "beta-domain" in captured.err
    assert "foo" in captured.err


def test_both_missing_raises_clear_filenotfound(tmp_path, monkeypatch):
    """Neither V2 nor V1 has the profile → FileNotFoundError naming both attempted paths."""
    legacy_dir = tmp_path / "community_profiles"
    legacy_dir.mkdir()

    domain_dir = tmp_path / "domain_knowledge"
    domain_dir.mkdir()

    monkeypatch.setattr(base, "PROFILES_DIR", legacy_dir)
    monkeypatch.setattr(base, "DOMAIN_KNOWLEDGE_DIR", domain_dir)

    with pytest.raises(FileNotFoundError) as excinfo:
        base.load_community_profile("nonexistent-tag")

    msg = str(excinfo.value)
    # Must mention both attempted paths and the tag
    assert "nonexistent-tag" in msg
    assert "domain_knowledge" in msg
    assert "community_profiles" in msg
    assert "V2" in msg or "per-domain" in msg
    assert "V1" in msg or "legacy" in msg
