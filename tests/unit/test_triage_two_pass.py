"""Tests for the V2 two-pass Triage Officer with graceful V1 fallback.

The four cases the spec calls out:

1. Pass-1 returns the right domains for a tech-career situation
2. Pass-1 returns empty for an out-of-scope situation → refusal
3. Pass-2 with no `domain_pack.md` files = identical output to V1
   (the bit-for-bit fallback)
4. Pass-2 with a stub `domain_pack.md` = system prompt contains the
   pack content (round-trip check that the loader actually injects)

The fallback case is the load-bearing one — it's what guarantees no
V1 eval regression in the current state where no pack files exist.
"""

from __future__ import annotations

import pytest

from blindspot.agents import triage as triage_mod
from blindspot.agents.triage import run_triage
from blindspot.config import Config
from blindspot.types import Facet


class _RecordingLLM:
    """LLM stub that records every call so tests can assert on system prompts.

    Routing matches what production code sends: the pass-1 prompt opens
    with "You are the Triage Officer ... pass 1"; the pass-2 prompt
    opens with "You are the Triage Officer for Blindspot" (the V1
    prompt). The integration test stub already uses the same opening-
    phrase pattern.
    """

    def __init__(
        self,
        pass1_domains: list[str] | None = None,
        pass2_payload: dict | None = None,
    ):
        self.pass1_domains = pass1_domains if pass1_domains is not None else []
        self.pass2_payload = pass2_payload or {
            "domains": ["tech-career/equity"],
            "entities": ["ISO"],
            "risk_surfaces": ["tax"],
            "personas": ["first-time-offer"],
        }
        self.calls: list[dict] = []

    async def complete(
        self, system, user, model="x", max_tokens=4096, json_schema=None
    ):
        self.calls.append(
            {"system": system, "user": user, "model": model, "schema": json_schema}
        )
        # Pass 1 is uniquely identified by mentioning "pass 1" in its
        # system prompt — keeps routing unambiguous even though both
        # prompts mention the Triage Officer role.
        if "pass 1" in system:
            return {"domains": list(self.pass1_domains)}
        return dict(self.pass2_payload)


@pytest.fixture(autouse=True)
def _isolate_domain_knowledge(tmp_path, monkeypatch):
    """Point the triage module at an empty domain_knowledge dir by default.

    Tests that want pack files create them under this tmp dir and the
    module's helpers (which take an optional ``root``) are also exposed
    via the patched ``DOMAIN_KNOWLEDGE_DIR`` for the public ``run_triage``
    entry point.
    """
    empty_root = tmp_path / "domain_knowledge"
    empty_root.mkdir()
    monkeypatch.setattr(triage_mod, "DOMAIN_KNOWLEDGE_DIR", empty_root)
    yield empty_root


def _write_pack(root, domain_slug: str, body: str) -> None:
    """Helper: create ``<root>/<domain>/domain_pack.md`` with the given body."""
    d = root / domain_slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "domain_pack.md").write_text(body)


# ---------------------------------------------------------------------------
# Case 3 — the load-bearing fallback. No pack files → V1 single-call path.
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_no_domain_packs_falls_back_to_v1_single_call(_isolate_domain_knowledge):
    """With zero packs on disk, run_triage MUST issue exactly one LLM call
    (the V1 path) — no pass-1, no extra system content.
    """
    llm = _RecordingLLM()

    sit = await run_triage("I got a Series B offer with ISOs", llm, Config())

    # Exactly one call — pass-1 is skipped when there are no packs to consume.
    assert len(llm.calls) == 1, (
        f"V1 fallback must issue exactly one LLM call; got {len(llm.calls)}"
    )
    only_call = llm.calls[0]
    # Bit-for-bit V1 system prompt: no extra appended content.
    assert "pass 1" not in only_call["system"]
    assert only_call["system"].endswith("Now extract tags from this situation:"), (
        "V1 fallback should send the unmodified triage.md prompt"
    )
    # The returned Situation should reflect pass-2's payload directly.
    assert sit.tags[Facet.DOMAIN] == ["tech-career/equity"]
    assert sit.tags[Facet.ENTITY] == ["ISO"]


# ---------------------------------------------------------------------------
# Case 1 — pass-1 routes the right domains for a tech-career situation.
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_pass1_classifies_tech_career_situation(_isolate_domain_knowledge):
    """With at least one pack on disk, pass-1 runs. When pass-1 returns
    `tech-career`, pass-2 receives the tech-career pack content.
    """
    _write_pack(_isolate_domain_knowledge, "tech-career", "TECH_CAREER_PACK_BODY")

    llm = _RecordingLLM(pass1_domains=["tech-career"])
    await run_triage("I got a Series B offer with ISOs", llm, Config())

    # Two LLM calls: pass-1 (classify) + pass-2 (extract).
    assert len(llm.calls) == 2
    pass1, pass2 = llm.calls
    assert "pass 1" in pass1["system"]
    # Pass-2 system prompt MUST include the pack body.
    assert "TECH_CAREER_PACK_BODY" in pass2["system"]
    assert "# Domain pack: tech-career" in pass2["system"]


# ---------------------------------------------------------------------------
# Case 2 — pass-1 empty → out-of-scope refusal (all-empty arrays, no pass-2).
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_pass1_empty_returns_refusal_without_running_pass2(
    _isolate_domain_knowledge,
):
    """Out-of-scope situations (medical, voting, etc.) get an empty pass-1
    result. The agent must short-circuit to all-empty arrays without
    spending an extra LLM call on pass-2.
    """
    _write_pack(_isolate_domain_knowledge, "tech-career", "irrelevant")

    llm = _RecordingLLM(pass1_domains=[])
    sit = await run_triage("Should I get a flu shot this year?", llm, Config())

    # Pass-2 must NOT be called.
    assert len(llm.calls) == 1
    assert "pass 1" in llm.calls[0]["system"]

    # All facets empty — consistent with the V1 scope-refusal behavior
    # (matches PR #13's contract: orchestrator refuses on empty domains).
    assert sit.tags[Facet.DOMAIN] == []
    assert sit.tags[Facet.ENTITY] == []
    assert sit.tags[Facet.RISK_SURFACE] == []
    assert sit.tags[Facet.PERSONA] == []


# ---------------------------------------------------------------------------
# Case 4 — multi-domain pass-1 concatenates all matching packs (and only
# the matching ones).
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_pass2_concatenates_only_matched_domain_packs(
    _isolate_domain_knowledge,
):
    """A multi-label pass-1 result must pull packs for every matched
    domain, and packs for unmatched domains must NOT leak into the
    system prompt.
    """
    _write_pack(_isolate_domain_knowledge, "tech-career", "PACK_TECH")
    _write_pack(_isolate_domain_knowledge, "immigration", "PACK_IMMIG")
    _write_pack(_isolate_domain_knowledge, "housing", "PACK_HOUSING_UNMATCHED")

    llm = _RecordingLLM(pass1_domains=["tech-career", "immigration"])
    await run_triage(
        "Series B offer with ISOs; I'm on H-1B and starting my I-140",
        llm,
        Config(),
    )

    assert len(llm.calls) == 2
    pass2_system = llm.calls[1]["system"]
    assert "PACK_TECH" in pass2_system
    assert "PACK_IMMIG" in pass2_system
    # Unmatched pack must NOT bleed in — pass-1's classification is the
    # whole point of two-pass; everything-always-included would defeat it.
    assert "PACK_HOUSING_UNMATCHED" not in pass2_system


# ---------------------------------------------------------------------------
# Case 4b — missing pack file for a matched domain is silently skipped
# (best-effort). Important for the migration window where pass-1 may
# match a domain whose pack hasn't been authored yet.
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_pass2_skips_matched_domain_without_pack_file(
    _isolate_domain_knowledge,
):
    """If pass-1 matches `immigration` but only `tech-career` has a pack
    on disk, pass-2 should still run (with just the tech-career pack)
    rather than erroring.
    """
    _write_pack(_isolate_domain_knowledge, "tech-career", "PACK_TECH_ONLY")

    llm = _RecordingLLM(pass1_domains=["tech-career", "immigration"])
    sit = await run_triage(
        "Series B offer with ISOs; I'm on H-1B and starting my I-140",
        llm,
        Config(),
    )

    assert len(llm.calls) == 2
    pass2_system = llm.calls[1]["system"]
    assert "PACK_TECH_ONLY" in pass2_system
    # The agent must NOT emit a "# Domain pack: immigration" header for
    # a domain whose pack file doesn't exist on disk. Silent skip is the
    # contract — fabricating a header would mislead the LLM.
    assert "# Domain pack: immigration" not in pass2_system
    # Pipeline produced a Situation (would have raised on error).
    assert isinstance(sit.tags[Facet.DOMAIN], list)
