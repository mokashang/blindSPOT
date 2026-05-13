"""Critic agent."""

from __future__ import annotations

import json

from blindspot.agents.base import load_prompt
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import CommunityAnalystOutput, CriticVerdict, RiskOfficerOutput

CRITIC_SCHEMA = {
    "type": "object",
    "properties": {
        "specificity": {"type": "string", "enum": ["pass", "fail"]},
        "non_obviousness": {"type": "integer", "minimum": 1, "maximum": 5},
        "grounding_pct": {"type": "integer", "minimum": 0, "maximum": 100},
        "regenerate_required": {"type": "boolean"},
        "feedback": {"type": "string"},
    },
    "required": [
        "specificity",
        "non_obviousness",
        "grounding_pct",
        "regenerate_required",
        "feedback",
    ],
}


async def run_critic(
    situation_text: str,
    analyst_outputs: list[CommunityAnalystOutput],
    risk_output: RiskOfficerOutput,
    llm: LLMClient,
    cfg: Config,
) -> CriticVerdict:
    raw = load_prompt("critic")
    system = (
        raw.replace("{{NON_OBVIOUSNESS_MIN}}", str(cfg.critic.non_obviousness_min))
        .replace("{{GROUNDING_THRESHOLD}}", str(cfg.critic.grounding_pct_threshold))
    )

    analyst_payload = [
        {
            "tag": o.community_tag,
            "prose": o.prose,
            "blind_spots": [b.__dict__ for b in o.blind_spots],
        }
        for o in analyst_outputs
    ]
    risk_payload = [b.__dict__ for b in risk_output.cross_community_blind_spots]

    user = (
        f"# Situation\n{situation_text}\n\n"
        f"# Community analyst outputs\n{json.dumps(analyst_payload, indent=2)}\n\n"
        f"# Risk Officer output\n{json.dumps(risk_payload, indent=2)}"
    )

    out = await llm.complete(
        system=system,
        user=user,
        model=cfg.models.default,
        json_schema=CRITIC_SCHEMA,
    )
    assert isinstance(out, dict)
    return CriticVerdict(
        specificity_pass=(out.get("specificity") == "pass"),
        non_obviousness=int(out.get("non_obviousness", 3)),
        grounding_pct=int(out.get("grounding_pct", 0)),
        regenerate_required=bool(out.get("regenerate_required", False)),
        feedback=out.get("feedback", ""),
    )
