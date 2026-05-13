"""Shared type definitions used across modules."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Facet(str, Enum):
    DOMAIN = "domain"
    ENTITY = "entity"
    RISK_SURFACE = "risk_surface"
    PERSONA = "persona"


@dataclass(frozen=True)
class Tag:
    facet: Facet
    value: str


@dataclass
class Situation:
    """A user's situation as extracted by the Triage Officer."""

    raw_text: str
    tags: dict[Facet, list[str]] = field(default_factory=dict)

    def all_tags(self) -> list[Tag]:
        return [Tag(facet, v) for facet, vs in self.tags.items() for v in vs]


@dataclass
class SearchContext:
    """Adapter-side input. Carries everything an adapter needs to plan a fetch."""

    situation: Situation
    entity_terms: list[str]


@dataclass
class Document:
    """A piece of fetched content with a per-turn stable ID."""

    doc_id: str                      # `doc-1`, `doc-2`, …  assigned at collection time
    source_view_id: str              # slug from data/source_registry.yaml
    community_tag: str
    url: str
    title: str
    content: str
    fetched_at: datetime
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class BlindSpot:
    hook: str
    body: str
    community_tag: str
    citation_doc_ids: list[str]


@dataclass
class CommunityAnalystOutput:
    community_tag: str
    prose: str                       # "What [community] would tell you" section
    blind_spots: list[BlindSpot]


@dataclass
class RiskOfficerOutput:
    cross_community_blind_spots: list[BlindSpot]


@dataclass
class CriticVerdict:
    specificity_pass: bool
    non_obviousness: int             # 1-5
    grounding_pct: int               # 0-100
    regenerate_required: bool
    feedback: str


@dataclass
class FinalResponse:
    situation: Situation
    community_outputs: list[CommunityAnalystOutput]
    risk_output: RiskOfficerOutput
    critic_verdict: CriticVerdict
    rendered_markdown: str           # what the user sees
    documents_used: list[Document]   # for citation rendering & ungrounded-claim logging
