"""Triage Officer agent."""

from __future__ import annotations

from blindspot.agents.base import load_prompt
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import Facet, Situation

TRIAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "domains": {"type": "array", "items": {"type": "string"}},
        "entities": {"type": "array", "items": {"type": "string"}},
        "risk_surfaces": {"type": "array", "items": {"type": "string"}},
        "personas": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["domains", "entities", "risk_surfaces", "personas"],
}


async def run_triage(situation_text: str, llm: LLMClient, cfg: Config) -> Situation:
    system = load_prompt("triage")
    out = await llm.complete(
        system=system,
        user=situation_text,
        model=cfg.models.default,
        json_schema=TRIAGE_SCHEMA,
    )
    assert isinstance(out, dict)
    return Situation(
        raw_text=situation_text,
        tags={
            Facet.DOMAIN: out.get("domains", []),
            Facet.ENTITY: out.get("entities", []),
            Facet.RISK_SURFACE: out.get("risk_surfaces", []),
            Facet.PERSONA: out.get("personas", []),
        },
    )
