"""Risk Officer: cross-community blind-spot synthesis."""

from __future__ import annotations

import json

from blindspot.agents.base import load_prompt, serialize_documents_for_prompt
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import (
    BlindSpot,
    CommunityAnalystOutput,
    Document,
    RiskOfficerOutput,
    Situation,
)

RISK_SCHEMA = {
    "type": "object",
    "properties": {
        "cross_community_blind_spots": {
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
    "required": ["cross_community_blind_spots"],
}


async def run_risk_officer(
    situation: Situation,
    analyst_outputs: list[CommunityAnalystOutput],
    docs: list[Document],
    llm: LLMClient,
    cfg: Config,
) -> RiskOfficerOutput:
    user = (
        f"# Situation\n{situation.raw_text}\n\n"
        f"# Documents (all communities)\n\n{serialize_documents_for_prompt(docs)}\n\n"
        f"# Community analyst outputs\n\n"
        + json.dumps(
            [
                {
                    "community_tag": o.community_tag,
                    "prose": o.prose,
                    "blind_spots": [
                        {
                            "hook": b.hook,
                            "body": b.body,
                            "citation_doc_ids": b.citation_doc_ids,
                        }
                        for b in o.blind_spots
                    ],
                }
                for o in analyst_outputs
            ],
            indent=2,
        )
    )

    out = await llm.complete(
        system=load_prompt("risk_officer"),
        user=user,
        model=cfg.models.default,
        json_schema=RISK_SCHEMA,
    )
    assert isinstance(out, dict)
    return RiskOfficerOutput(
        cross_community_blind_spots=[
            BlindSpot(
                hook=b.get("hook", ""),
                body=b.get("body", ""),
                community_tag="cross",
                citation_doc_ids=b.get("citation_doc_ids", []),
            )
            for b in out.get("cross_community_blind_spots", [])
        ]
    )
