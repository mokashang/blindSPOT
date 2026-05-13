"""Editor: assembles final markdown response. No structured JSON output."""

from __future__ import annotations

import json

from blindspot.agents.base import load_prompt
from blindspot.config import Config
from blindspot.filters.banlist import load_banlist
from blindspot.llm.base import LLMClient
from blindspot.types import (
    CommunityAnalystOutput,
    Document,
    Facet,
    RiskOfficerOutput,
    Situation,
)


async def run_editor(
    situation: Situation,
    analyst_outputs: list[CommunityAnalystOutput],
    risk_output: RiskOfficerOutput,
    documents: list[Document],
    llm: LLMClient,
    cfg: Config,
) -> str:
    banlist = load_banlist()
    raw = load_prompt("editor")
    system = raw.replace("{{BANLIST}}", "\n".join(f"  - {b}" for b in banlist))

    payload = {
        "situation": situation.raw_text,
        "domains": situation.tags.get(Facet.DOMAIN, []),
        "analysts": [
            {
                "community_tag": o.community_tag,
                "prose": o.prose,
                "blind_spots": [b.__dict__ for b in o.blind_spots],
            }
            for o in analyst_outputs
        ],
        "risk_output": [b.__dict__ for b in risk_output.cross_community_blind_spots],
        "documents": [
            {"doc_id": d.doc_id, "url": d.url, "title": d.title} for d in documents
        ],
    }

    out = await llm.complete(
        system=system,
        user=json.dumps(payload, default=str, indent=2),
        model=cfg.models.default,
    )
    assert isinstance(out, str)
    return out
