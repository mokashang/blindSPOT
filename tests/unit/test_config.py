from pathlib import Path

from blindspot.config import Config, load_config


def test_load_config_returns_typed_object(tmp_path: Path):
    p = tmp_path / "config.yaml"
    p.write_text(
        "llm_backend: anthropic_api\n"
        "models:\n  default: claude-opus-4-7\n"
        "tag_match:\n"
        "  weights:\n"
        "    domain: 3.0\n"
        "    entity: 2.0\n"
        "    risk_surface: 1.5\n"
        "    persona: 1.5\n"
        "    similarity: 1.0\n"
        "  top_n: 5\n"
        "  max_per_community: 2\n"
    )
    cfg = load_config(p)
    assert cfg.llm_backend == "anthropic_api"
    assert cfg.tag_match.weights.domain == 3.0
    assert cfg.tag_match.top_n == 5


def test_tunable_keys_can_be_inspected(tmp_path: Path):
    p = tmp_path / "config.yaml"
    p.write_text("tunable_keys:\n  - tag_match.weights.domain\n  - critic.grounding_pct_threshold\n")
    cfg = load_config(p)
    assert "tag_match.weights.domain" in cfg.tunable_keys
