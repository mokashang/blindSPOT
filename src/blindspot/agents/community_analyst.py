"""Community Analyst: one per active community per turn. Profile-driven."""

from __future__ import annotations

from blindspot.agents.base import (
    load_community_profile,
    load_prompt,
    serialize_documents_for_prompt,
)
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import BlindSpot, CommunityAnalystOutput, Document, Situation

ANALYST_SCHEMA = {
    "type": "object",
    "properties": {
        "prose": {"type": "string"},
        "blind_spots": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "hook": {"type": "string"},
                    "body": {"type": "string"},
                    "citation_doc_ids": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["hook", "body", "citation_doc_ids"],
            },
        },
    },
    "required": ["prose", "blind_spots"],
}


async def run_community_analyst(
    community_tag: str,
    situation: Situation,
    docs: list[Document],
    llm: LLMClient,
    cfg: Config,
) -> CommunityAnalystOutput:
    base = load_prompt("community_analyst")
    profile = load_community_profile(community_tag)
    system = f"{base}\n\n---\n# Community profile\n\n{profile}"

    user = (
        f"# Situation\n{situation.raw_text}\n\n"
        f"# Documents for this community\n\n"
        f"{serialize_documents_for_prompt(docs)}"
    )
    out = await llm.complete(
        system=system,
        user=user,
        model=cfg.models.default,
        json_schema=ANALYST_SCHEMA,
    )
    assert isinstance(out, dict)

    return CommunityAnalystOutput(
        community_tag=community_tag,
        prose=out.get("prose", ""),
        blind_spots=[
            BlindSpot(
                hook=bs.get("hook", ""),
                body=bs.get("body", ""),
                community_tag=community_tag,
                citation_doc_ids=bs.get("citation_doc_ids", []),
            )
            for bs in out.get("blind_spots", [])
        ],
    )
