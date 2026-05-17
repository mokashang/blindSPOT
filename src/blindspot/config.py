"""Config loading. Backed by pydantic for typed access."""

from __future__ import annotations

import warnings
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
    # Voyage's own AsyncClient defaults to 0 retries; the free tier (3 RPM)
    # rate-limits a single pipeline run, so retry with backoff by default.
    max_retries: int = 6


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
    source_diversity: float = 0.20


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


# Documented safe-ranges for tunable knobs. Each entry maps a dotted-path
# config key to the (min, max) range from its inline comment in config.yaml.
# Values outside the range produce a UserWarning at load time but do not
# crash — a user may intentionally tune past the range during experiments;
# we just want the deviation visible. Only knobs whose config.yaml comment
# explicitly specifies a numeric range are listed here.
_SAFE_RANGES: dict[str, tuple[float, float]] = {
    "embedder.max_retries": (3, 10),
    "tag_match.weights.domain": (2.5, 4.0),
    "tag_match.weights.entity": (1.5, 2.5),
    "tag_match.weights.risk_surface": (1.0, 2.0),
    "tag_match.weights.persona": (1.0, 2.0),
    "tag_match.top_n": (3, 8),
    "tag_match.max_per_community": (1, 3),
    "normalization.embedding_similarity_threshold": (0.80, 0.92),
    "critic.grounding_pct_threshold": (60, 90),
    "critic.non_obviousness_min": (2, 4),
    "critic.max_regenerations": (0, 3),
    "cache.fresh_ttl_days": (3, 14),
    "cache.evergreen_ttl_days": (14, 90),
}


def _get_dotted(cfg: Config, dotted: str) -> float | int:
    """Resolve a dotted-path key against a Config instance."""
    obj: object = cfg
    for part in dotted.split("."):
        obj = getattr(obj, part)
    return obj  # type: ignore[return-value]


def validate_safe_ranges(cfg: Config) -> None:
    """Warn (don't crash) on knobs outside their documented safe-range.

    The safe-ranges themselves are sourced from inline comments in
    `config.yaml`; this function machine-enforces them so a refine-time
    tune that drifts beyond a range becomes visible immediately.
    """
    for dotted, (lo, hi) in _SAFE_RANGES.items():
        value = _get_dotted(cfg, dotted)
        if value < lo or value > hi:
            warnings.warn(
                f"config knob '{dotted}' = {value} is outside documented "
                f"safe-range [{lo}, {hi}]",
                UserWarning,
                stacklevel=2,
            )


def load_config(path: Path | str = "config.yaml") -> Config:
    with open(path) as f:
        raw = yaml.safe_load(f) or {}
    cfg = Config.model_validate(raw)
    validate_safe_ranges(cfg)
    return cfg
