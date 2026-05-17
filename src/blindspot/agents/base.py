"""Agent-side helpers: prompt loader, community profile loader, doc serialization."""

from __future__ import annotations

import sys
from pathlib import Path

from blindspot.types import Document

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
PROFILES_DIR = Path(__file__).parent.parent.parent.parent / "community_profiles"
DOMAIN_KNOWLEDGE_DIR = Path(__file__).parent.parent.parent.parent / "domain_knowledge"


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.md").read_text().strip()


def load_community_profile(community_tag: str) -> str:
    """Load a community profile by tag.

    Lookup order (V2 layout preferred, V1 fallback during migration):

    1. ``domain_knowledge/<domain>/communities/<community_tag>.md`` —
       per-domain location. Glob across every domain. Exactly one match
       returns its content. Multiple matches resolve deterministically
       (alphabetically-first domain) and emit a warning to stderr naming
       every match — same tag claimed by multiple domains is a real
       config bug worth surfacing loudly.
    2. ``community_profiles/<community_tag>.md`` — legacy V1 location.
       Used when no per-domain copy exists.

    If neither exists, raise ``FileNotFoundError`` whose message names
    both paths that were tried.
    """
    domain_matches = sorted(DOMAIN_KNOWLEDGE_DIR.glob(f"*/communities/{community_tag}.md"))

    if domain_matches:
        if len(domain_matches) > 1:
            paths = ", ".join(str(p) for p in domain_matches)
            print(
                f"warning: community_tag {community_tag!r} found in multiple "
                f"domain_knowledge locations: {paths}. "
                f"Using {domain_matches[0]} (alphabetically first).",
                file=sys.stderr,
            )
        return domain_matches[0].read_text().strip()

    legacy_path = PROFILES_DIR / f"{community_tag}.md"
    if legacy_path.exists():
        return legacy_path.read_text().strip()

    domain_glob = DOMAIN_KNOWLEDGE_DIR / f"*/communities/{community_tag}.md"
    raise FileNotFoundError(
        f"community profile {community_tag!r} not found. Tried: "
        f"{domain_glob} (per-domain V2 layout), {legacy_path} (legacy V1 layout)."
    )


def serialize_documents_for_prompt(docs: list[Document]) -> str:
    """Render docs with stable IDs so the model can cite [doc-X]."""
    parts = []
    for d in docs:
        parts.append(
            f"[{d.doc_id}] {d.title}  ({d.community_tag} via {d.source_view_id})\n"
            f"URL: {d.url}\n"
            f"---\n{d.content}\n---"
        )
    return "\n\n".join(parts)
