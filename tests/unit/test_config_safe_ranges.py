"""Tests for machine-enforced safe-range validation in config loading.

Safe-ranges live as inline comments in `config.yaml`; the loader echoes
them as a `UserWarning` when a knob's value drifts outside its range.
The validation pass is warn-only on purpose — a user may intentionally
tune past the range during experimentation."""

from __future__ import annotations

import warnings
from pathlib import Path

import pytest

from blindspot.config import Config, validate_safe_ranges


def _in_range_config() -> Config:
    """Build a Config whose every safe-range knob sits inside its range."""
    return Config.model_validate(
        {
            "embedder": {"max_retries": 6},
            "tag_match": {
                "weights": {
                    "domain": 3.0,
                    "entity": 2.0,
                    "risk_surface": 1.5,
                    "persona": 1.5,
                    "similarity": 1.0,
                },
                "top_n": 5,
                "max_per_community": 2,
            },
            "normalization": {"embedding_similarity_threshold": 0.85},
            "critic": {
                "grounding_pct_threshold": 80,
                "non_obviousness_min": 3,
                "max_regenerations": 1,
            },
            "cache": {"fresh_ttl_days": 7, "evergreen_ttl_days": 30},
        }
    )


def test_in_range_values_produce_no_warning():
    cfg = _in_range_config()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        validate_safe_ranges(cfg)
    safe_range_warnings = [w for w in caught if issubclass(w.category, UserWarning)]
    assert safe_range_warnings == [], (
        f"expected no warnings on in-range config, got: "
        f"{[str(w.message) for w in safe_range_warnings]}"
    )


def test_out_of_range_value_produces_userwarning():
    # domain weight safe-range is 2.5-4.0; 5.0 is clearly above.
    cfg = _in_range_config()
    cfg.tag_match.weights.domain = 5.0
    with pytest.warns(UserWarning, match=r"tag_match\.weights\.domain.*5\.0"):
        validate_safe_ranges(cfg)


def test_load_config_invokes_validation(tmp_path: Path):
    """Loading a config.yaml with an out-of-range knob emits a warning."""
    from blindspot.config import load_config

    p = tmp_path / "config.yaml"
    p.write_text(
        "tag_match:\n"
        "  top_n: 20\n"  # safe-range 3-8; 20 is well above
    )
    with pytest.warns(UserWarning, match=r"tag_match\.top_n.*20"):
        load_config(p)
