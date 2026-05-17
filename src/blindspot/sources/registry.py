"""Loads source-view registry entries from YAML.

V2 layout (preferred during migration): per-domain ``domain_knowledge/<domain>/sources.yaml``.
V1 layout (legacy fallback): monolithic ``data/source_registry.yaml``.

``load_registry(path)`` keeps its V1 signature so existing callers (the
orchestrator integration test, the static ``sources list`` CLI) continue
to work unchanged. ``load_all_sources(root)`` is the new V2-first entry
point used by production callers.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

from blindspot.sources.base import SourceView


def _entries_to_source_views(raw: list[dict] | None) -> list[SourceView]:
    """Convert a parsed YAML list of dicts into ``SourceView`` instances.

    Shared by both the V1 monolithic loader and the V2 per-domain loader
    so the two paths produce bit-for-bit identical output for identical
    input YAML.
    """
    return [
        SourceView(
            id=e["id"],
            adapter=e["adapter"],
            fetch_config=e.get("fetch_config", {}),
            domains=e.get("domains", []),
            community_tag=e.get("community_tag", ""),
            reliability=int(e.get("reliability", 3)),
            freshness_required=bool(e.get("freshness_required", False)),
            notes=e.get("notes", "").strip(),
        )
        for e in (raw or [])
    ]


def load_registry(path: Path | str = "data/source_registry.yaml") -> list[SourceView]:
    """Load source-views from a single monolithic YAML file (V1 layout).

    Kept for backward compatibility — existing callers (tests, ``sources list``)
    pass an explicit path. Production callers should prefer
    ``load_all_sources`` which scans per-domain files first and falls back
    to this path.
    """
    with open(path) as f:
        raw = yaml.safe_load(f) or []
    return _entries_to_source_views(raw)


def load_all_sources(root: Path | str = ".") -> list[SourceView]:
    """Load source-views, preferring per-domain YAML over the legacy monolithic file.

    Lookup order (V2 preferred, V1 fallback during migration):

    1. Glob ``<root>/domain_knowledge/<domain>/sources.yaml`` where
       ``<domain>`` is any subdirectory whose name does NOT start with
       ``_`` (excludes ``_meta_*`` / ``_schema.md`` style scaffolding).
       Every match is loaded and its entries concatenated. Domains are
       iterated in sorted order for deterministic output.
    2. If no per-domain files are found, fall back to
       ``<root>/data/source_registry.yaml`` — the legacy V1 monolithic
       path.

    If BOTH layouts exist, V2 wins (per-domain files are returned) and a
    one-line warning naming the shadowed V1 file is printed to stderr.
    Same-tag claimed from multiple domains is the caller's responsibility
    to validate; this loader does not deduplicate.

    Bit-for-bit V1 preservation: when no per-domain files exist,
    ``load_all_sources()`` returns exactly the same ``list[SourceView]``
    as ``load_registry("data/source_registry.yaml")`` — both go through
    the shared ``_entries_to_source_views`` helper.
    """
    root_path = Path(root)
    domain_knowledge_dir = root_path / "domain_knowledge"

    per_domain_files: list[Path] = []
    if domain_knowledge_dir.is_dir():
        for child in sorted(domain_knowledge_dir.iterdir()):
            # Only scan real domain subdirectories — skip files (e.g.
            # ``_schema.md``) and underscored scaffolding directories
            # (``_meta_ontology``, etc.).
            if not child.is_dir():
                continue
            if child.name.startswith("_"):
                continue
            candidate = child / "sources.yaml"
            if candidate.is_file():
                per_domain_files.append(candidate)

    legacy_path = root_path / "data" / "source_registry.yaml"

    if per_domain_files:
        if legacy_path.is_file():
            print(
                f"warning: per-domain sources.yaml files take precedence; "
                f"shadowing legacy {legacy_path}",
                file=sys.stderr,
            )
        views: list[SourceView] = []
        for f in per_domain_files:
            with open(f) as fh:
                raw = yaml.safe_load(fh) or []
            views.extend(_entries_to_source_views(raw))
        return views

    # V1 fallback — no per-domain files found.
    return load_registry(legacy_path)


def get_view(views: list[SourceView], view_id: str) -> SourceView:
    for v in views:
        if v.id == view_id:
            return v
    raise KeyError(f"unknown source view: {view_id}")
