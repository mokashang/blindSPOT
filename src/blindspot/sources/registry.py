"""Loads source_registry.yaml into typed SourceView objects."""

from __future__ import annotations

from pathlib import Path

import yaml

from blindspot.sources.base import SourceView


def load_registry(path: Path | str = "data/source_registry.yaml") -> list[SourceView]:
    with open(path) as f:
        raw = yaml.safe_load(f) or []
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
        for e in raw
    ]


def get_view(views: list[SourceView], view_id: str) -> SourceView:
    for v in views:
        if v.id == view_id:
            return v
    raise KeyError(f"unknown source view: {view_id}")
