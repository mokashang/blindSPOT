"""Agent-side helpers: prompt loader, community profile loader, doc serialization."""

from __future__ import annotations

from pathlib import Path

from blindspot.types import Document

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
PROFILES_DIR = Path(__file__).parent.parent.parent.parent / "community_profiles"


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.md").read_text().strip()


def load_community_profile(community_tag: str) -> str:
    return (PROFILES_DIR / f"{community_tag}.md").read_text().strip()


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
