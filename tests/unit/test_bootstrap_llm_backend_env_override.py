"""Unit tests for `_bootstrap_full` LLM backend selection.

The refine routine's parallel eval subagents need to override the
`config.yaml`-declared backend without editing the shared config file —
otherwise `claude_agent_sdk.query()` deadlocks under concurrent callers
from sibling worktrees (see CLAUDE.md "Quirks"). The escape hatch is the
`BLINDSPOT_LLM_BACKEND` env var, which overrides `cfg.llm_backend` for
the current process and emits a stderr notice when it does.

These tests stub out the actual client classes so they don't try to read
real env-var API keys, and stub the embedder / engine bootstrap path so
the test isolates the backend-selection branch.
"""

from __future__ import annotations

import pytest
import typer

from blindspot import cli as cli_module


class _FakeCfg:
    """Minimum surface `_bootstrap_full` reads on the cfg object."""

    def __init__(self, llm_backend: str):
        self.llm_backend = llm_backend

        class _Emb:
            model = "voyage-3"
            max_retries = 1

        self.embedder = _Emb()


def _patch_bootstrap_deps(monkeypatch: pytest.MonkeyPatch, *, llm_backend: str):
    """Stub `_bootstrap_readonly` plus the three constructors so
    `_bootstrap_full` exercises only the backend-selection branch.

    Each constructor returns a string sentinel so the test can assert
    which class was selected without instantiating real network clients.
    """
    cfg = _FakeCfg(llm_backend)
    monkeypatch.setattr(
        cli_module, "_bootstrap_readonly", lambda: (cfg, "fake-engine")
    )
    monkeypatch.setattr(
        cli_module, "AnthropicAPIClient", lambda *a, **kw: "anthropic-api-client"
    )
    monkeypatch.setattr(
        cli_module, "ClaudeAgentClient", lambda *a, **kw: "claude-agent-client"
    )
    monkeypatch.setattr(
        cli_module, "VoyageEmbedder", lambda *a, **kw: "voyage-embedder"
    )
    return cfg


def test_env_var_unset_uses_config_backend(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    """When BLINDSPOT_LLM_BACKEND is unset, cfg.llm_backend wins and no
    override notice is emitted."""
    monkeypatch.delenv("BLINDSPOT_LLM_BACKEND", raising=False)
    _patch_bootstrap_deps(monkeypatch, llm_backend="claude_agent_sdk")

    _cfg, _engine, llm, embedder = cli_module._bootstrap_full()

    assert llm == "claude-agent-client"
    assert embedder == "voyage-embedder"
    captured = capsys.readouterr()
    assert "BLINDSPOT_LLM_BACKEND" not in captured.err
    assert "overridden" not in captured.err


def test_env_var_overrides_config_backend(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    """When BLINDSPOT_LLM_BACKEND differs from cfg.llm_backend, the env
    var wins and a one-line stderr notice is emitted naming both values."""
    monkeypatch.setenv("BLINDSPOT_LLM_BACKEND", "anthropic_api")
    _patch_bootstrap_deps(monkeypatch, llm_backend="claude_agent_sdk")

    _cfg, _engine, llm, _embedder = cli_module._bootstrap_full()

    assert llm == "anthropic-api-client"
    captured = capsys.readouterr()
    assert "BLINDSPOT_LLM_BACKEND" in captured.err
    assert "claude_agent_sdk" in captured.err
    assert "anthropic_api" in captured.err


def test_env_var_matching_config_emits_no_notice(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    """When the env var is set but to the same value as cfg.llm_backend,
    behavior is unchanged and no override notice is emitted (the override
    only "fires" when it actually changes something)."""
    monkeypatch.setenv("BLINDSPOT_LLM_BACKEND", "claude_agent_sdk")
    _patch_bootstrap_deps(monkeypatch, llm_backend="claude_agent_sdk")

    _cfg, _engine, llm, _embedder = cli_module._bootstrap_full()

    assert llm == "claude-agent-client"
    captured = capsys.readouterr()
    assert "overridden" not in captured.err


def test_invalid_env_var_value_raises_with_source_attribution(
    monkeypatch: pytest.MonkeyPatch,
):
    """An invalid BLINDSPOT_LLM_BACKEND value raises BadParameter and the
    message identifies the env var as the source (not config.yaml), so a
    user debugging eval immediately knows where to look."""
    monkeypatch.setenv("BLINDSPOT_LLM_BACKEND", "not-a-real-backend")
    _patch_bootstrap_deps(monkeypatch, llm_backend="claude_agent_sdk")

    with pytest.raises(typer.BadParameter) as exc_info:
        cli_module._bootstrap_full()

    msg = str(exc_info.value)
    assert "not-a-real-backend" in msg
    assert "BLINDSPOT_LLM_BACKEND" in msg
    assert "claude_agent_sdk" in msg
    assert "anthropic_api" in msg


def test_invalid_config_backend_attributes_to_config_yaml(
    monkeypatch: pytest.MonkeyPatch,
):
    """When the bad value comes from config.yaml (env var unset), the
    error message points at config.yaml — preserving the pre-override
    diagnostic behavior."""
    monkeypatch.delenv("BLINDSPOT_LLM_BACKEND", raising=False)
    _patch_bootstrap_deps(monkeypatch, llm_backend="garbage_backend")

    with pytest.raises(typer.BadParameter) as exc_info:
        cli_module._bootstrap_full()

    msg = str(exc_info.value)
    assert "garbage_backend" in msg
    assert "config.yaml" in msg
    assert "BLINDSPOT_LLM_BACKEND" not in msg
