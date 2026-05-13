"""Config loading. Backed by pydantic for typed access."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class _TagMatchWeights(BaseModel):
    domain: float = 3.0
    entity: float = 2.0
    risk_surface: float = 1.5
    persona: float = 1.5
    similarity: float = 1.0


class _TagMatch(BaseModel):
    weights: _TagMatchWeights = Field(default_factory=_TagMatchWeights)
    top_n: int = 5
    max_per_community: int = 2


class _Models(BaseModel):
    default: str = "claude-opus-4-7"


class _Embedder(BaseModel):
    provider: str = "voyage"
    model: str = "voyage-3"


class _DB(BaseModel):
    path: str = "~/.blindspot/blindspot.db"


class _Normalization(BaseModel):
    embedding_similarity_threshold: float = 0.85


class _Critic(BaseModel):
    grounding_pct_threshold: int = 80
    non_obviousness_min: int = 3
    max_regenerations: int = 1


class _Cache(BaseModel):
    fresh_ttl_days: int = 7
    evergreen_ttl_days: int = 30


class _RefineQualityWeights(BaseModel):
    specificity: float = 0.35
    non_obviousness: float = 0.25
    grounding_pct: float = 0.20
    source_diversity: float = 0.15
    ungrounded_inverse: float = 0.05


class _Refine(BaseModel):
    quality_score_weights: _RefineQualityWeights = Field(default_factory=_RefineQualityWeights)


class Config(BaseModel):
    llm_backend: str = "claude_agent_sdk"
    models: _Models = Field(default_factory=_Models)
    embedder: _Embedder = Field(default_factory=_Embedder)
    db: _DB = Field(default_factory=_DB)
    tag_match: _TagMatch = Field(default_factory=_TagMatch)
    normalization: _Normalization = Field(default_factory=_Normalization)
    critic: _Critic = Field(default_factory=_Critic)
    cache: _Cache = Field(default_factory=_Cache)
    refine: _Refine = Field(default_factory=_Refine)
    tunable_keys: list[str] = Field(default_factory=list)


def load_config(path: Path | str = "config.yaml") -> Config:
    with open(path) as f:
        raw = yaml.safe_load(f) or {}
    return Config.model_validate(raw)
