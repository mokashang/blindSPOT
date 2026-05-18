"""Triage Officer agent — two-pass with V1 fallback.

Design (kept from the original two-pass introduction in the
pre-pivot ROADMAP §4 "Architecture changes" — applies as-is to the
narrow single-vertical scope, with one in-scope domain instead of
ten):

- **Pass 1** classifies the situation as in-scope (`cn-sde-jobhunt`)
  or out-of-scope (empty list). Uses `prompts/triage_pass1.md` — a
  deliberately small prompt that only asks for the `domains` field.
  If pass 1 returns an empty list, the agent follows the existing
  scope-refusal path and returns all-empty arrays without calling
  pass 2.

- **Pass 2** runs the full triage extraction (entities / risk_surfaces
  / personas / domain sub-paths) using `prompts/triage.md`. For the
  matched domain, any `domain_knowledge/<domain>/domain_pack.md` is
  concatenated into the system prompt so the LLM has vertical-specific
  context. Missing pack files are silently ignored (best-effort).

- **Fallback to V1**: if NO `domain_pack.md` exists anywhere on disk
  the two-pass detour adds zero value and would only burn a second
  LLM call per turn. In that case the agent SKIPS pass 1 entirely
  and calls the legacy triage prompt directly. As soon as the first
  `domain_pack.md` lands, two-pass activates automatically — no
  config flag required.

Post-2026-05-18 scope-narrow note: with a single in-scope vertical,
the two-pass design is structurally redundant (pass 1 is a yes/no
classifier). The ROADMAP's V4-freeze checklist contains an item to
fold the two passes into one. Until that lands, the two-pass code
path is kept as-is — it works correctly for one vertical too.

The mirror of this pattern is `sources.registry.load_all_sources` (PR
#29) which does per-domain glob with V1 fallback. Same shape: V2 path
when V2 artifacts exist, otherwise V1 path bit-for-bit.

Public API (`run_triage(situation_text, llm, cfg) -> Situation`) is
unchanged so the orchestrator and existing tests need no edits.
"""

from __future__ import annotations

from pathlib import Path

from blindspot.agents.base import DOMAIN_KNOWLEDGE_DIR, load_prompt
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import Facet, Situation

TRIAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "domains": {"type": "array", "items": {"type": "string"}},
        "entities": {"type": "array", "items": {"type": "string"}},
        "risk_surfaces": {"type": "array", "items": {"type": "string"}},
        "personas": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["domains", "entities", "risk_surfaces", "personas"],
}

TRIAGE_PASS1_SCHEMA = {
    "type": "object",
    "properties": {
        "domains": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["domains"],
}


def _domain_pack_path(domain_slug: str, root: Path | None = None) -> Path:
    """Resolve the on-disk path of a domain's pack file (existence not checked)."""
    base = root if root is not None else DOMAIN_KNOWLEDGE_DIR
    # Strip any sub-path (pass 1 only emits top-level slugs, but defend
    # in case a stray `cn-sde-jobhunt/visa` slips through).
    top = domain_slug.split("/", 1)[0]
    return base / top / "domain_pack.md"


def _any_domain_pack_exists(root: Path | None = None) -> bool:
    """True if at least one `domain_knowledge/<domain>/domain_pack.md` exists.

    When this returns False the runtime is in V1-equivalent mode and the
    two-pass detour is skipped — preserving bit-for-bit V1 behavior
    until the first pack file lands.
    """
    base = root if root is not None else DOMAIN_KNOWLEDGE_DIR
    if not base.is_dir():
        return False
    # Glob keeps this O(domains), not O(files). Single-pass scan.
    return any(base.glob("*/domain_pack.md"))


def _load_relevant_domain_packs(
    domain_slugs: list[str], root: Path | None = None
) -> str:
    """Concatenate the `domain_pack.md` of every matched domain that has one.

    Missing pack files are silently skipped (best-effort). Returns an
    empty string when no matched domain has a pack — the caller treats
    that as "nothing to inject" and uses the unmodified V1 prompt.

    Each pack is wrapped in a labeled fence so the LLM can attribute
    instructions to the originating domain, and so multiple packs don't
    bleed into each other.
    """
    parts: list[str] = []
    seen_tops: set[str] = set()
    for slug in domain_slugs:
        top = slug.split("/", 1)[0]
        if top in seen_tops:
            continue
        seen_tops.add(top)
        path = _domain_pack_path(top, root=root)
        if not path.is_file():
            continue
        body = path.read_text().strip()
        if not body:
            continue
        parts.append(
            f"# Domain pack: {top}\n\n{body}"
        )
    return "\n\n---\n\n".join(parts)


async def _run_pass1(
    situation_text: str, llm: LLMClient, cfg: Config
) -> list[str]:
    """Pass-1 classification call. Returns the list of matched domain slugs."""
    pass1_system = load_prompt("triage_pass1")
    out = await llm.complete(
        system=pass1_system,
        user=situation_text,
        model=cfg.models.default,
        json_schema=TRIAGE_PASS1_SCHEMA,
    )
    # Most stubs and the real backend honor the schema; defend lightly
    # against a backend that returns text by mistake.
    if not isinstance(out, dict):
        return []
    raw = out.get("domains", []) or []
    # Strip whitespace, drop empties, preserve order, dedupe.
    cleaned: list[str] = []
    seen: set[str] = set()
    for d in raw:
        if not isinstance(d, str):
            continue
        s = d.strip()
        if not s or s in seen:
            continue
        seen.add(s)
        cleaned.append(s)
    return cleaned


async def _run_pass2(
    situation_text: str,
    llm: LLMClient,
    cfg: Config,
    extra_system: str = "",
) -> dict:
    """Pass-2 full-triage extraction.

    ``extra_system`` is the concatenated domain-pack content (or empty
    string when no relevant pack exists). When empty, the system prompt
    is bit-for-bit the V1 triage prompt.
    """
    base = load_prompt("triage")
    system = f"{base}\n\n{extra_system}" if extra_system else base
    out = await llm.complete(
        system=system,
        user=situation_text,
        model=cfg.models.default,
        json_schema=TRIAGE_SCHEMA,
    )
    assert isinstance(out, dict)
    return out


def _situation_from_triage_dict(situation_text: str, out: dict) -> Situation:
    return Situation(
        raw_text=situation_text,
        tags={
            Facet.DOMAIN: out.get("domains", []),
            Facet.ENTITY: out.get("entities", []),
            Facet.RISK_SURFACE: out.get("risk_surfaces", []),
            Facet.PERSONA: out.get("personas", []),
        },
    )


async def run_triage(situation_text: str, llm: LLMClient, cfg: Config) -> Situation:
    """Run the Triage Officer.

    Two-pass when at least one `domain_pack.md` exists on disk:
    pass 1 classifies domains, pass 2 extracts facets with the relevant
    packs injected into the system prompt. Pass-1-empty short-circuits
    to a refusal (all-empty arrays).

    Single-pass (V1 behavior) when no pack files exist anywhere — the
    detour would add a wasted LLM call with no upside.
    """
    if not _any_domain_pack_exists():
        # V1 fallback: bit-for-bit identical to the pre-two-pass code path.
        out = await _run_pass2(situation_text, llm, cfg, extra_system="")
        return _situation_from_triage_dict(situation_text, out)

    # V2 two-pass.
    matched_domains = await _run_pass1(situation_text, llm, cfg)
    if not matched_domains:
        # Scope refusal — same shape as pass-2 returning all-empty arrays.
        return _situation_from_triage_dict(
            situation_text,
            {"domains": [], "entities": [], "risk_surfaces": [], "personas": []},
        )

    extra_system = _load_relevant_domain_packs(matched_domains)
    out = await _run_pass2(situation_text, llm, cfg, extra_system=extra_system)
    return _situation_from_triage_dict(situation_text, out)
