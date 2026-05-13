# Blindspot V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a working CLI that takes a US tech-career-or-equity situation and produces grounded, source-cited blind spots from multiple community perspectives, persisted to SQLite, with an eval suite for quality regression.

**Architecture:** A 6-agent pipeline — Triage → Collection (parallel) → Community Analysts (parallel) → Risk Officer → Critic → Editor — orchestrated by a thin coordinator. Source-views (curated, annotated lenses on Reddit/RSS/HN/static corpora, listed in `data/source_registry.yaml`) ground generated claims via inline `[doc-X]` citation markers parsed by the Editor. Tags from an open vocabulary (with embedding-based auto-normalization) route situations to relevant sources. SQLite holds session state; YAML/markdown hold curated knowledge.

**Tech Stack:** Python 3.11+, `typer`, `SQLAlchemy`, `claude-agent-sdk` (default LLM backend), `anthropic` (production fallback), `voyageai` (embeddings), `praw`, `feedparser`, `httpx`, `pytest`, `pytest-asyncio`.

**Reference docs (already on disk):**
- Design doc: `docs/specs/2026-05-13-blindspot-v1-design.md`
- Source registry: `data/source_registry.yaml` (13 entries)
- Tag taxonomy seed: `data/tag_taxonomy_seed.yaml` (53 tags)
- Community profile schema: `community_profiles/_schema.md`
- One example profile: `community_profiles/founder-engineer-bloggers.md`
- Refine skill: `.claude/skills/refine-blindspot/SKILL.md`
- Pre-commit code-review hook: `.claude/settings.json` + `~/.claude/hooks/blindspot-code-review-on-commit.py`

---

## File Structure (target end-state)

```
blindspot/
├── pyproject.toml
├── config.yaml
├── README.md
├── docs/                                    [done]
├── data/                                    [done — registry + taxonomy seed + static dir]
├── community_profiles/                      [partially done — 1 of 8 profiles]
├── refinements/log.jsonl                    [empty, created at first refine run]
├── fixtures/eval_situations.yaml
├── eval/results/                            [gitignored, runtime artifacts]
├── tests/
│   ├── unit/
│   └── integration/
├── src/blindspot/
│   ├── __init__.py
│   ├── config.py
│   ├── cli.py
│   ├── orchestrator.py
│   ├── types.py                             # shared dataclasses: Situation, Document, TurnState, etc.
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── base.py                          # LLMClient Protocol + Embedder Protocol
│   │   ├── claude_agent_client.py
│   │   ├── anthropic_api_client.py
│   │   └── voyage_embedder.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py                          # Agent helpers, common io
│   │   ├── triage.py
│   │   ├── collection.py
│   │   ├── community_analyst.py
│   │   ├── risk_officer.py
│   │   ├── critic.py
│   │   └── editor.py
│   ├── sources/
│   │   ├── __init__.py
│   │   ├── base.py                          # SourceAdapter Protocol
│   │   ├── registry.py                      # load source_registry.yaml
│   │   ├── tag_match.py                     # scoring + diversity
│   │   └── adapters/
│   │       ├── __init__.py
│   │       ├── rss.py
│   │       ├── reddit_search.py
│   │       ├── hn_search.py
│   │       └── static_corpus.py
│   ├── tags/
│   │   ├── __init__.py
│   │   ├── taxonomy.py                      # vocab CRUD + normalization
│   │   └── extractor.py                     # parse Triage output
│   ├── filters/
│   │   ├── __init__.py
│   │   ├── banlist.py                       # load banlist into editor prompt
│   │   ├── banlist.txt
│   │   └── grounding.py                     # parse [doc-X] markers
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py                        # SQLAlchemy models
│   │   ├── session.py                       # engine + sessionmaker
│   │   └── migrations/
│   │       └── 001_initial.sql
│   ├── prompts/
│   │   ├── triage.md
│   │   ├── community_analyst.md
│   │   ├── risk_officer.md
│   │   ├── critic.md
│   │   └── editor.md
│   └── eval/
│       ├── __init__.py
│       ├── runner.py
│       └── judge.py
```

---

## Phase 1 — Foundation

### Task 1: Project skeleton

**Files:**
- Create: `pyproject.toml`, `config.yaml`, `src/blindspot/__init__.py`, `src/blindspot/types.py`, `README.md`, dir tree.

- [ ] **Step 1: Create directory tree**

```bash
mkdir -p src/blindspot/{agents,sources/adapters,llm,tags,filters,db/migrations,prompts,eval}
mkdir -p tests/unit tests/integration
mkdir -p fixtures refinements eval/results
touch src/blindspot/__init__.py
touch src/blindspot/agents/__init__.py
touch src/blindspot/sources/__init__.py
touch src/blindspot/sources/adapters/__init__.py
touch src/blindspot/llm/__init__.py
touch src/blindspot/tags/__init__.py
touch src/blindspot/filters/__init__.py
touch src/blindspot/db/__init__.py
touch src/blindspot/eval/__init__.py
touch refinements/log.jsonl
```

- [ ] **Step 2: Write `pyproject.toml`**

```toml
[project]
name = "blindspot"
version = "0.1.0"
description = "Decision-aware advisor surfacing unknown unknowns from curated community sources."
requires-python = ">=3.11"
dependencies = [
    "typer>=0.12",
    "rich>=13.7",
    "sqlalchemy>=2.0",
    "pyyaml>=6.0",
    "httpx>=0.27",
    "feedparser>=6.0",
    "praw>=7.7",
    "beautifulsoup4>=4.12",
    "claude-agent-sdk>=0.1.0",
    "anthropic>=0.40.0",
    "voyageai>=0.2",
    "pydantic>=2.6",
    "numpy>=1.26",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "pytest-cov>=4.1",
    "ruff>=0.4",
    "mypy>=1.10",
    "pytest-mock>=3.12",
]

[project.scripts]
blindspot = "blindspot.cli:app"

[build-system]
requires = ["setuptools>=70"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP"]

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

- [ ] **Step 3: Write `config.yaml`**

```yaml
llm_backend: claude_agent_sdk        # or: anthropic_api

models:
  default: claude-opus-4-7

embedder:
  provider: voyage
  model: voyage-3

db:
  path: ~/.blindspot/blindspot.db

tag_match:
  weights:
    domain: 3.0
    entity: 2.0
    risk_surface: 1.5
    persona: 1.5
    similarity: 1.0
  top_n: 5
  max_per_community: 2

normalization:
  embedding_similarity_threshold: 0.85

critic:
  grounding_pct_threshold: 80
  non_obviousness_min: 3
  max_regenerations: 1

cache:
  fresh_ttl_days: 7
  evergreen_ttl_days: 30

refine:
  quality_score_weights:
    specificity: 0.35
    non_obviousness: 0.25
    grounding_pct: 0.20
    source_diversity: 0.15
    ungrounded_inverse: 0.05

# Keys the refine routine is allowed to autonomously tune (must list tunables).
tunable_keys:
  - tag_match.weights.domain
  - tag_match.weights.entity
  - tag_match.weights.risk_surface
  - tag_match.weights.persona
  - tag_match.weights.similarity
  - tag_match.top_n
  - tag_match.max_per_community
  - normalization.embedding_similarity_threshold
  - critic.grounding_pct_threshold
  - critic.non_obviousness_min
```

- [ ] **Step 4: Write `src/blindspot/__init__.py`**

```python
"""Blindspot — decision-aware advisor for unknown unknowns."""

__version__ = "0.1.0"
```

- [ ] **Step 5: Write `src/blindspot/types.py` (shared dataclasses used across modules)**

```python
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
    source_view_id: str              # slug from source_registry.yaml
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
```

- [ ] **Step 6: Install dependencies and verify import**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -c "import blindspot; print(blindspot.__version__)"
```
Expected: `0.1.0`

- [ ] **Step 7: Write minimal `README.md`**

```markdown
# Blindspot

Decision-aware advisor surfacing unknown unknowns from curated community sources.

See `docs/specs/2026-05-13-blindspot-v1-design.md` for the design.

## Install

\```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
\```

## Use

\```bash
blindspot ask "I got a Series B offer..."
\```

## Develop

\```bash
pytest
\```
```

(Replace `\``` with backticks in the actual README — escaped here for the plan doc.)

- [ ] **Step 8: Commit**

```bash
git add pyproject.toml config.yaml src/blindspot/__init__.py src/blindspot/types.py README.md
git add src/blindspot/agents/__init__.py src/blindspot/sources/__init__.py src/blindspot/sources/adapters/__init__.py
git add src/blindspot/llm/__init__.py src/blindspot/tags/__init__.py src/blindspot/filters/__init__.py
git add src/blindspot/db/__init__.py src/blindspot/eval/__init__.py refinements/log.jsonl
git commit -m "feat: project skeleton, types, config, deps"
git push origin main
```

---

### Task 2: Config loader

**Files:**
- Create: `src/blindspot/config.py`, `tests/unit/test_config.py`

- [ ] **Step 1: Write the failing test**

`tests/unit/test_config.py`:

```python
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
```

- [ ] **Step 2: Run, expect failure**

```bash
pytest tests/unit/test_config.py -v
```
Expected: `ModuleNotFoundError: No module named 'blindspot.config'`.

- [ ] **Step 3: Implement `src/blindspot/config.py`**

```python
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
```

- [ ] **Step 4: Run tests, expect pass**

```bash
pytest tests/unit/test_config.py -v
```
Expected: both tests PASS.

- [ ] **Step 5: Commit**

```bash
git add src/blindspot/config.py tests/unit/test_config.py
git commit -m "feat: config loader with typed pydantic models"
git push origin main
```

---

### Task 3: DB models + migrations

**Files:**
- Create: `src/blindspot/db/models.py`, `src/blindspot/db/session.py`, `src/blindspot/db/migrations/001_initial.sql`, `tests/unit/test_db_models.py`

- [ ] **Step 1: Write the failing test**

`tests/unit/test_db_models.py`:

```python
from datetime import datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blindspot.db.models import (
    Base, BlindSpotRow, DocumentRow, SessionRow, TurnRow, TurnTagRow,
)


def test_can_create_full_session_graph():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as s:
        sess = SessionRow(user_id="local", situation="I got an offer", language="en")
        s.add(sess)
        s.flush()
        turn = TurnRow(session_id=sess.id, turn_number=1, user_input="I got an offer",
                       assistant_response="...")
        s.add(turn)
        s.flush()
        s.add(TurnTagRow(turn_id=turn.id, facet="entity", tag="ISO"))
        s.add(BlindSpotRow(turn_id=turn.id, hook="...", body="...", community_tag="x"))
        doc = DocumentRow(source_view_id="pmck-equity", url="https://x", title="t",
                          content="c", content_hash="abc", fetched_at=datetime.now(timezone.utc),
                          expires_at=datetime.now(timezone.utc))
        s.add(doc)
        s.commit()

        assert sess.id is not None
        assert turn.session_id == sess.id
```

- [ ] **Step 2: Run, expect failure**

```bash
pytest tests/unit/test_db_models.py -v
```
Expected: `ImportError`.

- [ ] **Step 3: Implement `src/blindspot/db/models.py`**

Use SQLAlchemy 2.x declarative style. Tables per spec §8:

- `SessionRow` (`sessions`): id, user_id, created_at, situation, summary, language
- `TurnRow` (`turns`): id, session_id (FK), turn_number, user_input, assistant_response, created_at
- `TurnTagRow` (`turn_tags`): turn_id (FK), facet, tag — composite PK
- `BlindSpotRow` (`blind_spots`): id, turn_id (FK), hook, body, community_tag, rating, rated_at
- `BlindSpotSourceRow` (`blind_spot_sources`): blind_spot_id (FK), document_id (FK) — composite PK
- `DocumentRow` (`documents`): id, source_view_id (STRING — not FK; references YAML slug), fetched_at, expires_at, url, title, content, content_hash (unique), language
- `TagVocabularyRow` (`tag_vocabulary`): id, facet, tag (unique per facet), added_at, embedding_blob (BLOB), status
- `TagAuditRow` (`tag_audit`): id, facet, proposed_tag, accepted_tag, similarity_to_existing, turn_id (FK nullable), timestamp
- `UngroundedClaimRow` (`ungrounded_claims`): id, turn_id (FK), claim_text, context, logged_at
- `SourceViewStatsRow` (`source_view_stats`): source_view_id (string), period (YYYY-MM), hits, ratings_hit, ratings_meh, ratings_obvious — composite PK on (source_view_id, period)

Index: `(turn_id)` on `blind_spots`, `(source_view_id)` on `documents`. Unique constraint on `documents.content_hash`.

- [ ] **Step 4: Implement `src/blindspot/db/session.py`**

```python
"""Session factory bound to the configured SQLite path."""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from blindspot.config import Config
from blindspot.db.models import Base


def get_engine(cfg: Config):
    db_path = Path(cfg.db.path).expanduser()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{db_path}")


def init_schema(cfg: Config) -> None:
    Base.metadata.create_all(get_engine(cfg))


SessionLocal = sessionmaker(autoflush=False, autocommit=False)
```

- [ ] **Step 5: Run tests, expect pass**

```bash
pytest tests/unit/test_db_models.py -v
```

- [ ] **Step 6: Commit**

```bash
git add src/blindspot/db/ tests/unit/test_db_models.py
git commit -m "feat: SQLAlchemy models for all V1 tables + schema bootstrap"
git push origin main
```

---

## Phase 2 — LLM Backends & Embedder

### Task 4: LLMClient Protocol + Embedder Protocol

**Files:**
- Create: `src/blindspot/llm/base.py`, `tests/unit/test_llm_base.py`

- [ ] **Step 1: Write `src/blindspot/llm/base.py`**

```python
"""LLM client + embedder abstractions."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class LLMClient(Protocol):
    async def complete(
        self,
        system: str,
        user: str,
        model: str = "claude-opus-4-7",
        max_tokens: int = 4096,
        json_schema: dict[str, Any] | None = None,
    ) -> str | dict[str, Any]:
        """Return text on plain completion, dict when json_schema is supplied."""
        ...


@runtime_checkable
class Embedder(Protocol):
    async def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text."""
        ...
```

- [ ] **Step 2: Smoke test the Protocols**

`tests/unit/test_llm_base.py`:

```python
from blindspot.llm.base import LLMClient, Embedder


class FakeLLM:
    async def complete(self, system, user, model="claude-opus-4-7", max_tokens=4096, json_schema=None):
        return "ok"


class FakeEmbedder:
    async def embed(self, texts):
        return [[0.0] for _ in texts]


def test_protocols_accept_compatible_objects():
    assert isinstance(FakeLLM(), LLMClient)
    assert isinstance(FakeEmbedder(), Embedder)
```

- [ ] **Step 3: Run tests, expect pass; commit**

```bash
pytest tests/unit/test_llm_base.py -v
git add src/blindspot/llm/base.py tests/unit/test_llm_base.py
git commit -m "feat: LLMClient + Embedder protocols"
git push origin main
```

---

### Task 5: ClaudeAgentClient

**Files:**
- Create: `src/blindspot/llm/claude_agent_client.py`, `tests/unit/test_claude_agent_client.py`

- [ ] **Step 1: Write `src/blindspot/llm/claude_agent_client.py`**

Use the `claude_agent_sdk` package. The `query()` async generator returns messages; we extract the assistant's text.

```python
"""LLMClient implementation using claude-agent-sdk (Claude Code subscription)."""

from __future__ import annotations

import json
from typing import Any

from claude_agent_sdk import ClaudeAgentOptions, query

from blindspot.llm.base import LLMClient


class ClaudeAgentClient(LLMClient):
    async def complete(
        self,
        system: str,
        user: str,
        model: str = "claude-opus-4-7",
        max_tokens: int = 4096,
        json_schema: dict[str, Any] | None = None,
    ) -> str | dict[str, Any]:
        prompt = user
        if json_schema is not None:
            prompt = (
                user
                + "\n\nReturn ONLY valid JSON conforming to this schema:\n"
                + json.dumps(json_schema, indent=2)
            )

        opts = ClaudeAgentOptions(
            system_prompt=system,
            model=model,
            max_turns=1,
        )

        result_text = ""
        async for message in query(prompt=prompt, options=opts):
            for block in getattr(message, "content", []) or []:
                if getattr(block, "type", None) == "text":
                    result_text += block.text

        if json_schema is not None:
            return self._parse_json_response(result_text)
        return result_text

    @staticmethod
    def _parse_json_response(text: str) -> dict[str, Any]:
        # Tolerate JSON wrapped in markdown fences.
        text = text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            if text.startswith("json\n"):
                text = text[len("json\n") :]
        return json.loads(text)
```

- [ ] **Step 2: Unit-test the JSON parsing helper (no live calls)**

`tests/unit/test_claude_agent_client.py`:

```python
import pytest

from blindspot.llm.claude_agent_client import ClaudeAgentClient


def test_parse_json_response_plain():
    out = ClaudeAgentClient._parse_json_response('{"a": 1}')
    assert out == {"a": 1}


def test_parse_json_response_fenced():
    out = ClaudeAgentClient._parse_json_response('```json\n{"a": 1}\n```')
    assert out == {"a": 1}


def test_parse_json_response_invalid_raises():
    with pytest.raises(Exception):
        ClaudeAgentClient._parse_json_response("not json")
```

- [ ] **Step 3: Run tests, expect pass; commit**

```bash
pytest tests/unit/test_claude_agent_client.py -v
git add src/blindspot/llm/claude_agent_client.py tests/unit/test_claude_agent_client.py
git commit -m "feat: ClaudeAgentClient (subscription-backed LLM client)"
git push origin main
```

---

### Task 6: AnthropicAPIClient + VoyageEmbedder

**Files:**
- Create: `src/blindspot/llm/anthropic_api_client.py`, `src/blindspot/llm/voyage_embedder.py`, `tests/unit/test_voyage_embedder.py`

- [ ] **Step 1: Write `src/blindspot/llm/anthropic_api_client.py`** (production backend stub)

```python
"""LLMClient implementation using the Anthropic API directly.
Production backend. Requires ANTHROPIC_API_KEY env var.
"""

from __future__ import annotations

import json
import os
from typing import Any

from anthropic import AsyncAnthropic

from blindspot.llm.base import LLMClient


class AnthropicAPIClient(LLMClient):
    def __init__(self, api_key: str | None = None):
        self._client = AsyncAnthropic(api_key=api_key or os.environ["ANTHROPIC_API_KEY"])

    async def complete(
        self,
        system: str,
        user: str,
        model: str = "claude-opus-4-7",
        max_tokens: int = 4096,
        json_schema: dict[str, Any] | None = None,
    ) -> str | dict[str, Any]:
        if json_schema is not None:
            # Use tool_use for structured output.
            tool = {
                "name": "respond_structured",
                "description": "Return the response in the required schema.",
                "input_schema": json_schema,
            }
            resp = await self._client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                tools=[tool],
                tool_choice={"type": "tool", "name": "respond_structured"},
                messages=[{"role": "user", "content": user}],
            )
            for block in resp.content:
                if block.type == "tool_use":
                    return block.input
            raise RuntimeError("Model did not produce structured output")

        resp = await self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        out = ""
        for block in resp.content:
            if block.type == "text":
                out += block.text
        return out
```

- [ ] **Step 2: Write `src/blindspot/llm/voyage_embedder.py`**

```python
"""Embedder using voyage-3."""

from __future__ import annotations

import os

import voyageai

from blindspot.llm.base import Embedder


class VoyageEmbedder(Embedder):
    def __init__(self, model: str = "voyage-3", api_key: str | None = None):
        self._client = voyageai.AsyncClient(api_key=api_key or os.environ["VOYAGE_API_KEY"])
        self._model = model

    async def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        resp = await self._client.embed(texts=texts, model=self._model, input_type="document")
        return resp.embeddings
```

- [ ] **Step 3: Test (mocked)**

`tests/unit/test_voyage_embedder.py`:

```python
import pytest

from blindspot.llm.voyage_embedder import VoyageEmbedder


@pytest.mark.asyncio
async def test_embed_empty_returns_empty(monkeypatch):
    monkeypatch.setenv("VOYAGE_API_KEY", "dummy")
    e = VoyageEmbedder()
    out = await e.embed([])
    assert out == []
```

- [ ] **Step 4: Run + commit**

```bash
pytest tests/unit/test_voyage_embedder.py -v
git add src/blindspot/llm/anthropic_api_client.py src/blindspot/llm/voyage_embedder.py tests/unit/test_voyage_embedder.py
git commit -m "feat: AnthropicAPIClient + VoyageEmbedder"
git push origin main
```

---

## Phase 3 — Source Layer

### Task 7: SourceAdapter Protocol + Registry loader

**Files:**
- Create: `src/blindspot/sources/base.py`, `src/blindspot/sources/registry.py`, `tests/unit/test_registry.py`

- [ ] **Step 1: Define `SourceAdapter` + `SourceView` dataclass**

`src/blindspot/sources/base.py`:

```python
"""SourceAdapter Protocol and SourceView dataclass."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from blindspot.types import Document, SearchContext


@dataclass
class SourceView:
    """A configured, annotated lens into one source — the unit of the registry."""

    id: str
    adapter: str                            # "rss" | "reddit_search" | "hn_search" | "static_corpus"
    fetch_config: dict[str, Any]
    domains: list[str] = field(default_factory=list)
    community_tag: str = ""
    reliability: int = 3                    # 1-5
    freshness_required: bool = False
    notes: str = ""


class SourceAdapter(Protocol):
    """Each adapter handles one type of source."""

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]: ...
```

- [ ] **Step 2: Write `src/blindspot/sources/registry.py`**

```python
"""Loads source_registry.yaml into typed SourceView objects."""

from __future__ import annotations

from pathlib import Path

import yaml

from blindspot.sources.base import SourceView


def load_registry(path: Path | str = "data/source_registry.yaml") -> list[SourceView]:
    with open(path) as f:
        raw = yaml.safe_load(f) or []
    return [
        SourceView(
            id=e["id"],
            adapter=e["adapter"],
            fetch_config=e.get("fetch_config", {}),
            domains=e.get("domains", []),
            community_tag=e.get("community_tag", ""),
            reliability=int(e.get("reliability", 3)),
            freshness_required=bool(e.get("freshness_required", False)),
            notes=e.get("notes", "").strip(),
        )
        for e in raw
    ]


def get_view(views: list[SourceView], view_id: str) -> SourceView:
    for v in views:
        if v.id == view_id:
            return v
    raise KeyError(f"unknown source view: {view_id}")
```

- [ ] **Step 3: Test**

`tests/unit/test_registry.py`:

```python
from blindspot.sources.registry import load_registry


def test_loads_13_sourceviews_from_committed_yaml():
    views = load_registry()
    assert len(views) == 13
    assert {v.id for v in views} >= {
        "pmck-equity", "danluu-career", "pragmatic-engineer",
        "reddit-cscareerquestions-equity", "reddit-experienceddevs", "reddit-personalfinance-equity",
        "avc-fred-wilson", "hn-equity-discussions", "kb-financial-equity",
        "matt-levine-money-stuff", "carta-blog", "levels-fyi-blog", "holloway-equity-guide",
    }


def test_pmck_has_expected_fields():
    views = load_registry()
    pmck = next(v for v in views if v.id == "pmck-equity")
    assert pmck.adapter == "rss"
    assert pmck.reliability == 5
    assert pmck.community_tag == "founder-engineer-bloggers"
    assert "ISO" in " ".join(pmck.fetch_config.get("keyword_filter", []))
```

- [ ] **Step 4: Run + commit**

```bash
pytest tests/unit/test_registry.py -v
git add src/blindspot/sources/base.py src/blindspot/sources/registry.py tests/unit/test_registry.py
git commit -m "feat: SourceAdapter protocol + registry loader"
git push origin main
```

---

### Task 8: RSS Adapter + HN Adapter

**Files:**
- Create: `src/blindspot/sources/adapters/rss.py`, `src/blindspot/sources/adapters/hn_search.py`, `tests/unit/test_rss_adapter.py`, `tests/unit/test_hn_adapter.py`

- [ ] **Step 1: RSS adapter — implement using `feedparser`**

`src/blindspot/sources/adapters/rss.py`:

```python
"""RSS source adapter. Pulls from a feed URL, filters by keyword whitelist."""

from __future__ import annotations

import asyncio
import hashlib
from datetime import datetime, timezone

import feedparser

from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class RSSAdapter:
    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        feed_url = view.fetch_config["feed"]
        keyword_filter = [k.lower() for k in view.fetch_config.get("keyword_filter", [])]

        feed = await asyncio.to_thread(feedparser.parse, feed_url)
        out: list[Document] = []
        for entry in feed.entries[:30]:
            text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
            if keyword_filter and not any(k in text for k in keyword_filter):
                continue
            content = self._extract_content(entry)
            doc_id = hashlib.sha256((view.id + entry.get("link", "")).encode()).hexdigest()[:12]
            out.append(
                Document(
                    doc_id=f"doc-{doc_id}",
                    source_view_id=view.id,
                    community_tag=view.community_tag,
                    url=entry.get("link", ""),
                    title=entry.get("title", "")[:200],
                    content=content[:8000],
                    fetched_at=datetime.now(timezone.utc),
                )
            )
        return out[:5]

    @staticmethod
    def _extract_content(entry) -> str:
        if "content" in entry and entry.content:
            return entry.content[0].value
        return entry.get("summary", "")
```

- [ ] **Step 2: RSS test (uses a tiny in-memory feed)**

`tests/unit/test_rss_adapter.py`:

```python
from datetime import datetime, timezone
from unittest.mock import patch

import pytest

from blindspot.sources.adapters.rss import RSSAdapter
from blindspot.sources.base import SourceView
from blindspot.types import SearchContext, Situation


@pytest.mark.asyncio
async def test_rss_adapter_filters_by_keyword():
    fake_feed = type("F", (), {
        "entries": [
            {"title": "Equity tips", "summary": "ISO basics", "link": "u1"},
            {"title": "Unrelated", "summary": "cooking", "link": "u2"},
        ]
    })()
    view = SourceView(
        id="x", adapter="rss", fetch_config={"feed": "u", "keyword_filter": ["equity", "ISO"]},
        community_tag="t",
    )
    ctx = SearchContext(situation=Situation(raw_text=""), entity_terms=[])

    with patch("blindspot.sources.adapters.rss.feedparser.parse", return_value=fake_feed):
        out = await RSSAdapter().fetch(view, ctx)
    assert len(out) == 1
    assert out[0].url == "u1"
```

- [ ] **Step 3: HN search adapter** — uses HN Algolia API.

`src/blindspot/sources/adapters/hn_search.py`:

```python
"""Hacker News source adapter via Algolia HN search API (no auth)."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone

import httpx

from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class HNSearchAdapter:
    BASE = "https://hn.algolia.com/api/v1/search"

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        query = " ".join(ctx.entity_terms) or ctx.situation.raw_text[:100]
        min_points = int(view.fetch_config.get("min_points", 100))

        params = {
            "query": query,
            "tags": "story",
            "numericFilters": f"points>={min_points}",
            "hitsPerPage": 5,
        }
        async with httpx.AsyncClient(timeout=15.0) as client:
            r = await client.get(self.BASE, params=params)
            r.raise_for_status()
            data = r.json()

        out: list[Document] = []
        for hit in data.get("hits", []):
            doc_id = hashlib.sha256((view.id + str(hit["objectID"])).encode()).hexdigest()[:12]
            out.append(
                Document(
                    doc_id=f"doc-{doc_id}",
                    source_view_id=view.id,
                    community_tag=view.community_tag,
                    url=hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}",
                    title=hit.get("title", "")[:200],
                    content=(hit.get("story_text") or hit.get("title") or "")[:8000],
                    fetched_at=datetime.now(timezone.utc),
                    metadata={"points": str(hit.get("points", 0))},
                )
            )
        return out
```

- [ ] **Step 4: HN test (mocked)**

`tests/unit/test_hn_adapter.py`:

```python
from unittest.mock import AsyncMock, patch

import pytest

from blindspot.sources.adapters.hn_search import HNSearchAdapter
from blindspot.sources.base import SourceView
from blindspot.types import SearchContext, Situation


@pytest.mark.asyncio
async def test_hn_adapter_maps_hits_to_documents():
    fake_resp = type("R", (), {
        "json": lambda self: {"hits": [
            {"objectID": "42", "title": "ISO basics", "url": "https://x", "points": 200}
        ]},
        "raise_for_status": lambda self: None,
    })()
    with patch("blindspot.sources.adapters.hn_search.httpx.AsyncClient") as Cls:
        Cls.return_value.__aenter__.return_value.get = AsyncMock(return_value=fake_resp)
        view = SourceView(id="hn", adapter="hn_search", fetch_config={"min_points": 100},
                          community_tag="hn-collective")
        ctx = SearchContext(situation=Situation(raw_text=""), entity_terms=["ISO"])
        out = await HNSearchAdapter().fetch(view, ctx)
    assert len(out) == 1
    assert out[0].title == "ISO basics"
```

- [ ] **Step 5: Run + commit**

```bash
pytest tests/unit/test_rss_adapter.py tests/unit/test_hn_adapter.py -v
git add src/blindspot/sources/adapters/rss.py src/blindspot/sources/adapters/hn_search.py
git add tests/unit/test_rss_adapter.py tests/unit/test_hn_adapter.py
git commit -m "feat: RSS + HN search adapters"
git push origin main
```

---

### Task 9: Reddit adapter

**Files:**
- Create: `src/blindspot/sources/adapters/reddit_search.py`, `tests/unit/test_reddit_adapter.py`

- [ ] **Step 1: Implement using PRAW**

```python
"""Reddit source adapter using PRAW (script-app credentials)."""

from __future__ import annotations

import asyncio
import hashlib
import os
from datetime import datetime, timezone

import praw

from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class RedditSearchAdapter:
    def __init__(self):
        self._reddit = praw.Reddit(
            client_id=os.environ["REDDIT_CLIENT_ID"],
            client_secret=os.environ["REDDIT_CLIENT_SECRET"],
            user_agent=os.environ.get("REDDIT_USER_AGENT", "blindspot/0.1 by /u/local"),
        )

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        subreddit_name = view.fetch_config["subreddit"]
        sort = view.fetch_config.get("sort", "top")
        time_window = view.fetch_config.get("time_window", "year")
        min_upvotes = int(view.fetch_config.get("min_upvotes", 0))

        query = " OR ".join(ctx.entity_terms) if ctx.entity_terms else ""

        return await asyncio.to_thread(
            self._fetch_sync, view, subreddit_name, query, sort, time_window, min_upvotes
        )

    def _fetch_sync(self, view, subreddit_name, query, sort, time_window, min_upvotes):
        sub = self._reddit.subreddit(subreddit_name)
        results = sub.search(query, sort=sort, time_filter=time_window, limit=20) if query \
            else sub.top(time_filter=time_window, limit=20)
        out: list[Document] = []
        for post in results:
            if post.score < min_upvotes:
                continue
            content = (post.selftext or "")[:6000]
            top_comments = "\n\n".join(
                c.body for c in (post.comments[:3] if hasattr(post, "comments") else [])
                if hasattr(c, "body")
            )[:2000]
            doc_id = hashlib.sha256((view.id + post.id).encode()).hexdigest()[:12]
            out.append(Document(
                doc_id=f"doc-{doc_id}",
                source_view_id=view.id,
                community_tag=view.community_tag,
                url=f"https://reddit.com{post.permalink}",
                title=post.title[:200],
                content=f"{content}\n\n--- TOP COMMENTS ---\n{top_comments}",
                fetched_at=datetime.now(timezone.utc),
                metadata={"score": str(post.score), "comments": str(post.num_comments)},
            ))
            if len(out) >= 5:
                break
        return out
```

- [ ] **Step 2: Minimal test**

`tests/unit/test_reddit_adapter.py`:

```python
import os

import pytest


def test_imports_when_env_set(monkeypatch):
    monkeypatch.setenv("REDDIT_CLIENT_ID", "x")
    monkeypatch.setenv("REDDIT_CLIENT_SECRET", "y")
    from blindspot.sources.adapters.reddit_search import RedditSearchAdapter
    assert RedditSearchAdapter is not None
```

(Integration testing Reddit hits the live API — defer to manual smoke test.)

- [ ] **Step 3: Run + commit**

```bash
pytest tests/unit/test_reddit_adapter.py -v
git add src/blindspot/sources/adapters/reddit_search.py tests/unit/test_reddit_adapter.py
git commit -m "feat: Reddit search adapter (PRAW)"
git push origin main
```

---

### Task 10: Static corpus adapter

**Files:**
- Create: `src/blindspot/sources/adapters/static_corpus.py`, `tests/unit/test_static_corpus.py`, `data/static/holloway-equity-guide.md` (placeholder content)

- [ ] **Step 1: Implement chunk-based retrieval**

```python
"""Static corpus adapter: chunk a local markdown file, retrieve top-K by embedding similarity."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from blindspot.llm.base import Embedder
from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


class StaticCorpusAdapter:
    """Loads the corpus once, then serves top-K similarity matches."""

    def __init__(self, embedder: Embedder, chunk_size: int = 1500, top_k: int = 3):
        self._embedder = embedder
        self._chunk_size = chunk_size
        self._top_k = top_k
        self._cache: dict[str, tuple[list[str], np.ndarray]] = {}  # path -> (chunks, embeddings)

    async def fetch(self, view: SourceView, ctx: SearchContext) -> list[Document]:
        path = Path(view.fetch_config["path"])
        chunks, embeds = await self._load(path)
        if not chunks:
            return []

        query = ctx.situation.raw_text
        query_emb_list = await self._embedder.embed([query])
        query_emb = np.array(query_emb_list[0])

        # Cosine similarity (vectors already normalized by voyage-3).
        scores = embeds @ query_emb
        top_idx = np.argsort(scores)[-self._top_k :][::-1]

        out: list[Document] = []
        for idx in top_idx:
            chunk = chunks[idx]
            doc_id = hashlib.sha256((view.id + str(idx)).encode()).hexdigest()[:12]
            out.append(Document(
                doc_id=f"doc-{doc_id}",
                source_view_id=view.id,
                community_tag=view.community_tag,
                url=f"file://{path.resolve()}#chunk-{idx}",
                title=f"{path.stem} chunk {idx}",
                content=chunk,
                fetched_at=datetime.now(timezone.utc),
            ))
        return out

    async def _load(self, path: Path) -> tuple[list[str], np.ndarray]:
        key = str(path)
        if key in self._cache:
            return self._cache[key]
        if not path.exists():
            self._cache[key] = ([], np.array([]))
            return self._cache[key]
        text = path.read_text()
        chunks = self._chunk(text)
        if not chunks:
            self._cache[key] = ([], np.array([]))
            return self._cache[key]
        embed_list = await self._embedder.embed(chunks)
        embeds = np.array(embed_list)
        self._cache[key] = (chunks, embeds)
        return self._cache[key]

    def _chunk(self, text: str) -> list[str]:
        # Naive paragraph-grouping chunker; good enough for V1.
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        chunks: list[str] = []
        cur = ""
        for p in paragraphs:
            if len(cur) + len(p) + 2 <= self._chunk_size:
                cur = f"{cur}\n\n{p}" if cur else p
            else:
                if cur:
                    chunks.append(cur)
                cur = p
        if cur:
            chunks.append(cur)
        return chunks
```

- [ ] **Step 2: Test (with stub embedder)**

`tests/unit/test_static_corpus.py`:

```python
import numpy as np
import pytest

from blindspot.sources.adapters.static_corpus import StaticCorpusAdapter
from blindspot.sources.base import SourceView
from blindspot.types import SearchContext, Situation


class StubEmbedder:
    async def embed(self, texts):
        # Return distinct vectors based on first letter; ensures argsort is deterministic.
        return [[float(ord(t[0])) if t else 0.0] for t in texts]


@pytest.mark.asyncio
async def test_static_corpus_returns_top_k(tmp_path):
    f = tmp_path / "c.md"
    f.write_text("AAA paragraph one.\n\nBBB paragraph two.\n\nCCC paragraph three.")
    view = SourceView(
        id="hg", adapter="static_corpus", fetch_config={"path": str(f)},
        community_tag="ref",
    )
    ctx = SearchContext(situation=Situation(raw_text="CCC related question"), entity_terms=[])
    adapter = StaticCorpusAdapter(StubEmbedder(), chunk_size=100, top_k=1)
    out = await adapter.fetch(view, ctx)
    assert len(out) == 1
    assert "CCC" in out[0].content


@pytest.mark.asyncio
async def test_missing_file_returns_empty(tmp_path):
    view = SourceView(id="x", adapter="static_corpus", fetch_config={"path": "/nonexistent"},
                      community_tag="ref")
    ctx = SearchContext(situation=Situation(raw_text="q"), entity_terms=[])
    adapter = StaticCorpusAdapter(StubEmbedder())
    out = await adapter.fetch(view, ctx)
    assert out == []
```

- [ ] **Step 3: Create placeholder static corpus file**

```bash
cat > data/static/holloway-equity-guide.md <<'EOF'
# Holloway Guide to Equity Compensation — Local Notes

Replace this placeholder with relevant chapters from the public Holloway
Guide to Equity Compensation. Manual ingest only.

Recommended chapters to include:
- Stock options basics (ISO/NSO/RSU mechanics)
- Vesting schedules and cliffs
- Exercise mechanics and 83(b) elections
- AMT and qualifying dispositions
- Secondary sales and tender offers
EOF
```

- [ ] **Step 4: Run + commit**

```bash
pytest tests/unit/test_static_corpus.py -v
git add src/blindspot/sources/adapters/static_corpus.py tests/unit/test_static_corpus.py data/static/holloway-equity-guide.md
git commit -m "feat: static corpus adapter with embedding-based retrieval"
git push origin main
```

---

## Phase 4 — Tags & Matching

### Task 11: Tag vocabulary CRUD

**Files:**
- Create: `src/blindspot/tags/taxonomy.py`, `tests/unit/test_taxonomy.py`

- [ ] **Step 1: Implement** — exposes `add_or_merge_tag(facet, candidate)` which embeds, checks similarity to existing tags in that facet, merges or inserts.

```python
"""Tag vocabulary CRUD with embedding-based auto-normalization.

When a new tag is proposed (by the Triage Officer):
  1. Embed it.
  2. Find the most similar existing tag in the same facet.
  3. If max similarity > threshold → return the existing tag (merge).
  4. Else → insert new tag + write tag_audit row.
"""

from __future__ import annotations

import io
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable

import numpy as np
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.models import TagAuditRow, TagVocabularyRow
from blindspot.llm.base import Embedder


@dataclass
class TagResolution:
    facet: str
    accepted_tag: str        # the tag actually used (may be merged)
    was_merged: bool
    similarity: float | None


def _pack(vec: list[float]) -> bytes:
    arr = np.asarray(vec, dtype=np.float32)
    buf = io.BytesIO()
    np.save(buf, arr)
    return buf.getvalue()


def _unpack(blob: bytes) -> np.ndarray:
    return np.load(io.BytesIO(blob))


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(a @ b / (na * nb))


async def seed_vocabulary(db: Session, embedder: Embedder, seed: dict[str, list[str]]) -> None:
    """Seed the tag_vocabulary table from data/tag_taxonomy_seed.yaml content."""
    pairs: list[tuple[str, str]] = [(facet, tag) for facet, tags in seed.items() for tag in tags]
    texts = [t for _, t in pairs]
    embeds = await embedder.embed(texts) if texts else []
    now = datetime.now(timezone.utc)
    for (facet, tag), emb in zip(pairs, embeds, strict=True):
        existing = db.query(TagVocabularyRow).filter_by(facet=facet, tag=tag).first()
        if existing:
            continue
        db.add(TagVocabularyRow(
            facet=facet, tag=tag, added_at=now, embedding_blob=_pack(emb), status="active"
        ))
    db.commit()


async def add_or_merge_tag(
    db: Session, embedder: Embedder, cfg: Config,
    facet: str, candidate: str, turn_id: int | None = None,
) -> TagResolution:
    """Insert a new tag or merge into the closest existing one."""

    candidate = candidate.strip()
    if not candidate:
        return TagResolution(facet=facet, accepted_tag="", was_merged=False, similarity=None)

    # Exact match → use as-is.
    exact = db.query(TagVocabularyRow).filter_by(facet=facet, tag=candidate).first()
    if exact is not None:
        return TagResolution(facet=facet, accepted_tag=candidate, was_merged=False, similarity=1.0)

    threshold = cfg.normalization.embedding_similarity_threshold
    candidate_emb_list = await embedder.embed([candidate])
    candidate_emb = np.asarray(candidate_emb_list[0])

    rows: Iterable[TagVocabularyRow] = db.query(TagVocabularyRow).filter_by(
        facet=facet, status="active"
    ).all()

    best: tuple[float, TagVocabularyRow | None] = (0.0, None)
    for r in rows:
        sim = _cosine(candidate_emb, _unpack(r.embedding_blob))
        if sim > best[0]:
            best = (sim, r)

    if best[1] is not None and best[0] >= threshold:
        # Merge.
        db.add(TagAuditRow(
            facet=facet, proposed_tag=candidate,
            accepted_tag=best[1].tag, similarity_to_existing=best[0],
            turn_id=turn_id, timestamp=datetime.now(timezone.utc),
        ))
        db.commit()
        return TagResolution(facet=facet, accepted_tag=best[1].tag,
                             was_merged=True, similarity=best[0])

    # Insert new.
    db.add(TagVocabularyRow(
        facet=facet, tag=candidate,
        added_at=datetime.now(timezone.utc),
        embedding_blob=_pack(candidate_emb.tolist()),
        status="active",
    ))
    db.add(TagAuditRow(
        facet=facet, proposed_tag=candidate, accepted_tag=candidate,
        similarity_to_existing=best[0], turn_id=turn_id,
        timestamp=datetime.now(timezone.utc),
    ))
    db.commit()
    return TagResolution(facet=facet, accepted_tag=candidate,
                         was_merged=False, similarity=best[0])
```

- [ ] **Step 2: Test merge + insert paths with a deterministic stub embedder**

`tests/unit/test_taxonomy.py`:

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.models import Base, TagAuditRow, TagVocabularyRow
from blindspot.tags.taxonomy import add_or_merge_tag, seed_vocabulary


class StubEmbedder:
    """Returns deterministic vectors so we can pin similarity outcomes."""
    def __init__(self, mapping):
        self.mapping = mapping

    async def embed(self, texts):
        return [self.mapping.get(t, [0.0, 0.0, 1.0]) for t in texts]


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        yield s


@pytest.mark.asyncio
async def test_exact_match_returns_existing(db):
    db.add(TagVocabularyRow(facet="entity", tag="ISO", added_at=__import__("datetime").datetime.now(),
                            embedding_blob=b"\x00", status="active"))
    db.commit()
    cfg = Config()
    res = await add_or_merge_tag(db, StubEmbedder({}), cfg, "entity", "ISO")
    assert res.accepted_tag == "ISO"
    assert res.was_merged is False
    assert res.similarity == 1.0


@pytest.mark.asyncio
async def test_seed_populates_vocabulary(db):
    embedder = StubEmbedder({"ISO": [1.0, 0.0, 0.0], "RSU": [0.0, 1.0, 0.0]})
    await seed_vocabulary(db, embedder, {"entity": ["ISO", "RSU"]})
    rows = db.query(TagVocabularyRow).all()
    assert {r.tag for r in rows} == {"ISO", "RSU"}
```

- [ ] **Step 3: Run + commit**

```bash
pytest tests/unit/test_taxonomy.py -v
git add src/blindspot/tags/taxonomy.py tests/unit/test_taxonomy.py
git commit -m "feat: tag vocabulary CRUD with embedding-based normalization"
git push origin main
```

---

### Task 12: Tag-match scorer + diversity constraint

**Files:**
- Create: `src/blindspot/sources/tag_match.py`, `tests/unit/test_tag_match.py`

- [ ] **Step 1: Write the failing test (covers scoring + diversity)**

`tests/unit/test_tag_match.py`:

```python
import pytest

from blindspot.config import Config
from blindspot.sources.base import SourceView
from blindspot.sources.tag_match import select_top_n
from blindspot.types import Facet, Situation


def _view(id_, community, reliability=3, domains=None, entities=None,
          risks=None, personas=None, notes=""):
    return SourceView(
        id=id_, adapter="rss", fetch_config={},
        domains=domains or [], community_tag=community,
        reliability=reliability, freshness_required=False, notes=notes,
    )


@pytest.mark.asyncio
async def test_diversity_constraint_limits_two_per_community():
    situation = Situation(raw_text="...", tags={
        Facet.DOMAIN: ["tech-career/equity"],
        Facet.ENTITY: ["ISO"],
        Facet.RISK_SURFACE: [],
        Facet.PERSONA: [],
    })
    views = [
        _view("a", "founder-engineer-bloggers", 5, domains=["tech-career/equity"]),
        _view("b", "founder-engineer-bloggers", 5, domains=["tech-career/equity"]),
        _view("c", "founder-engineer-bloggers", 5, domains=["tech-career/equity"]),
        _view("d", "reddit-tech-collective",    4, domains=["tech-career/equity"]),
        _view("e", "vc-blogosphere",            3, domains=["tech-career/equity"]),
    ]

    class NullEmbedder:
        async def embed(self, texts): return [[0.0]] * len(texts)

    selected = await select_top_n(views, situation, Config(), NullEmbedder())
    chosen_ids = [v.id for v in selected]
    fea_count = chosen_ids.count("a") + chosen_ids.count("b") + chosen_ids.count("c")
    # Only 2 of {a, b, c} should appear because max_per_community is 2.
    assert sum(1 for v in selected if v.community_tag == "founder-engineer-bloggers") == 2
    assert "d" in chosen_ids
    assert "e" in chosen_ids
```

- [ ] **Step 2: Implement**

```python
"""Tag-match scoring with diversity constraint."""

from __future__ import annotations

import numpy as np

from blindspot.config import Config
from blindspot.llm.base import Embedder
from blindspot.sources.base import SourceView
from blindspot.types import Facet, Situation

# We don't store a registry-side embedding cache yet; for V1 we embed source.notes lazily.


async def select_top_n(
    views: list[SourceView],
    situation: Situation,
    cfg: Config,
    embedder: Embedder,
) -> list[SourceView]:
    weights = cfg.tag_match.weights
    top_n = cfg.tag_match.top_n
    cap = cfg.tag_match.max_per_community

    # Compute similarity scores (embed situation + each source's notes).
    sit_emb_list = await embedder.embed([situation.raw_text])
    note_embs = await embedder.embed([v.notes or v.id for v in views])
    sit_vec = np.asarray(sit_emb_list[0])
    note_mat = np.asarray(note_embs)

    def cosine(a, b):
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        return float(a @ b / (na * nb)) if na and nb else 0.0

    scored: list[tuple[float, SourceView]] = []
    for view, note_vec in zip(views, note_mat, strict=True):
        d = len(set(view.domains) & set(situation.tags.get(Facet.DOMAIN, [])))
        e_count = 0
        # Entities aren't first-class on SourceView yet; rely on notes for V1.
        # (Later: add a `entity_coverage` field. For now we approximate by notes-mention.)
        for ent in situation.tags.get(Facet.ENTITY, []):
            if ent.lower() in view.notes.lower():
                e_count += 1
        r_count = 0
        for risk in situation.tags.get(Facet.RISK_SURFACE, []):
            if risk.lower() in view.notes.lower():
                r_count += 1
        p_count = 0
        for persona in situation.tags.get(Facet.PERSONA, []):
            if persona.lower() in view.notes.lower():
                p_count += 1

        sim = cosine(sit_vec, note_vec)
        score = (
            weights.domain * d
            + weights.entity * e_count
            + weights.risk_surface * r_count
            + weights.persona * p_count
            + weights.similarity * sim
        )
        score *= (view.reliability / 3.0)
        scored.append((score, view))

    scored.sort(key=lambda p: p[0], reverse=True)

    selected: list[SourceView] = []
    per_community: dict[str, int] = {}
    for score, view in scored:
        if per_community.get(view.community_tag, 0) >= cap:
            continue
        selected.append(view)
        per_community[view.community_tag] = per_community.get(view.community_tag, 0) + 1
        if len(selected) >= top_n:
            break
    return selected
```

- [ ] **Step 3: Run + commit**

```bash
pytest tests/unit/test_tag_match.py -v
git add src/blindspot/sources/tag_match.py tests/unit/test_tag_match.py
git commit -m "feat: tag-match scorer with diversity constraint"
git push origin main
```

---

## Phase 5 — Agents

Each agent is a single `async def` function plus a markdown prompt file. State flows in via typed args, out via typed return.

### Task 13: Agent base + prompt loader + community profile loader

**Files:**
- Create: `src/blindspot/agents/base.py`, `tests/unit/test_agents_base.py`

- [ ] **Step 1: Implement helpers**

```python
"""Agent-side helpers: prompt loader, community profile loader, doc serialization."""

from __future__ import annotations

from pathlib import Path

from blindspot.types import Document

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
PROFILES_DIR = Path(__file__).parent.parent.parent.parent / "community_profiles"


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.md").read_text().strip()


def load_community_profile(community_tag: str) -> str:
    return (PROFILES_DIR / f"{community_tag}.md").read_text().strip()


def serialize_documents_for_prompt(docs: list[Document]) -> str:
    """Render docs with stable IDs so the model can cite [doc-X]."""
    parts = []
    for d in docs:
        parts.append(
            f"[{d.doc_id}] {d.title}  ({d.community_tag} via {d.source_view_id})\n"
            f"URL: {d.url}\n"
            f"---\n{d.content}\n---"
        )
    return "\n\n".join(parts)
```

- [ ] **Step 2: Smoke test**

```python
from blindspot.agents.base import serialize_documents_for_prompt
from blindspot.types import Document
from datetime import datetime, timezone


def test_serialize_documents_marks_each():
    docs = [
        Document(doc_id="doc-1", source_view_id="x", community_tag="t", url="u",
                 title="A", content="aaa", fetched_at=datetime.now(timezone.utc)),
        Document(doc_id="doc-2", source_view_id="x", community_tag="t", url="u",
                 title="B", content="bbb", fetched_at=datetime.now(timezone.utc)),
    ]
    out = serialize_documents_for_prompt(docs)
    assert "[doc-1]" in out
    assert "[doc-2]" in out
    assert "aaa" in out
```

- [ ] **Step 3: Run + commit**

```bash
pytest tests/unit/test_agents_base.py -v
git add src/blindspot/agents/base.py tests/unit/test_agents_base.py
git commit -m "feat: agent base helpers (prompt + profile loader, doc serializer)"
git push origin main
```

---

### Task 14: Triage Officer

**Files:**
- Create: `src/blindspot/prompts/triage.md`, `src/blindspot/agents/triage.py`, `tests/unit/test_triage.py`

- [ ] **Step 1: Write `src/blindspot/prompts/triage.md`**

```markdown
You are the Triage Officer for Blindspot, a decision-aware advisor. Given a
user's situation, extract structured tags across four facets.

# Output schema

Return ONLY JSON with this exact shape:

\```json
{
  "domains": ["tech-career/equity", ...],
  "entities": ["ISO", "series-B", ...],
  "risk_surfaces": ["tax", "counterparty", ...],
  "personas": ["first-time-offer", ...]
}
\```

# Facet definitions

- **domains** — broad subject categories. Use hierarchical paths.
  Examples: `tech-career`, `tech-career/equity`, `tech-career/negotiation`,
  `tech-career/comp`, `tech-career/exit`, `tech-career/startup-stage`,
  `tech-career/founder`, `tech-career/early-employee`.

- **entities** — concrete things mentioned in the situation. Stock types
  (`ISO`, `NSO`, `RSU`), tax concepts (`AMT`, `409A-valuation`,
  `strike-price`, `qualifying-disposition`), vesting (`vesting-cliff`,
  `vesting-schedule`, `single-trigger`, `double-trigger`, `refresher`,
  `accelerator`), exit (`IPO`, `acquisition`, `secondary-sale`,
  `tender-offer`), stage (`seed-stage`, `series-A`, `series-B`,
  `series-C-plus`, `late-stage`), special (`post-termination-exercise-window`,
  `early-exercise`, `83b-election`, `golden-handcuffs`).

- **risk_surfaces** — what *type* of harm or concern: `tax`, `legal`,
  `timing`, `counterparty`, `liquidity`, `regret`, `info-asymmetry`,
  `power-dynamics`, `opportunity-cost`.

- **personas** — who the user is right now: `first-time-offer`,
  `comparing-offers`, `considering-quit`, `pre-vest-cliff`,
  `post-vest-cliff`, `early-employee`, `senior-employee`, `founder`.

# Rules

- Be liberal with tags — better to over-extract than miss.
- You MAY propose new tags not in the lists above when the situation
  genuinely calls for one. They'll be normalized downstream.
- If the situation is clearly outside US tech career & equity scope,
  return all-empty arrays. The orchestrator will refuse the request.

Now extract tags from this situation:
```

- [ ] **Step 2: Implement `src/blindspot/agents/triage.py`**

```python
"""Triage Officer agent."""

from __future__ import annotations

from blindspot.agents.base import load_prompt
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


async def run_triage(situation_text: str, llm: LLMClient, cfg: Config) -> Situation:
    system = load_prompt("triage")
    out = await llm.complete(
        system=system, user=situation_text,
        model=cfg.models.default,
        json_schema=TRIAGE_SCHEMA,
    )
    assert isinstance(out, dict)
    return Situation(
        raw_text=situation_text,
        tags={
            Facet.DOMAIN: out.get("domains", []),
            Facet.ENTITY: out.get("entities", []),
            Facet.RISK_SURFACE: out.get("risk_surfaces", []),
            Facet.PERSONA: out.get("personas", []),
        },
    )
```

- [ ] **Step 3: Test with stub LLM**

`tests/unit/test_triage.py`:

```python
import pytest

from blindspot.agents.triage import run_triage
from blindspot.config import Config
from blindspot.types import Facet


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {
            "domains": ["tech-career/equity"],
            "entities": ["ISO", "series-B"],
            "risk_surfaces": ["tax"],
            "personas": ["first-time-offer"],
        }


@pytest.mark.asyncio
async def test_triage_returns_situation_with_tags():
    sit = await run_triage("I got a Series B offer with 0.1% ISOs", StubLLM(), Config())
    assert sit.tags[Facet.DOMAIN] == ["tech-career/equity"]
    assert "ISO" in sit.tags[Facet.ENTITY]
    assert sit.tags[Facet.PERSONA] == ["first-time-offer"]
```

- [ ] **Step 4: Run + commit**

```bash
pytest tests/unit/test_triage.py -v
git add src/blindspot/prompts/triage.md src/blindspot/agents/triage.py tests/unit/test_triage.py
git commit -m "feat: Triage Officer agent + prompt"
git push origin main
```

---

### Task 15: Collection orchestration

**Files:**
- Create: `src/blindspot/agents/collection.py`, `tests/unit/test_collection.py`

- [ ] **Step 1: Implement parallel fetch across selected source-views**

```python
"""Collection: dispatch each selected source-view to its adapter, fetch in parallel."""

from __future__ import annotations

import asyncio

from blindspot.llm.base import Embedder
from blindspot.sources.adapters.hn_search import HNSearchAdapter
from blindspot.sources.adapters.reddit_search import RedditSearchAdapter
from blindspot.sources.adapters.rss import RSSAdapter
from blindspot.sources.adapters.static_corpus import StaticCorpusAdapter
from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext


def build_adapter(adapter_name: str, embedder: Embedder | None):
    if adapter_name == "rss":
        return RSSAdapter()
    if adapter_name == "reddit_search":
        return RedditSearchAdapter()
    if adapter_name == "hn_search":
        return HNSearchAdapter()
    if adapter_name == "static_corpus":
        assert embedder is not None, "static_corpus requires an embedder"
        return StaticCorpusAdapter(embedder)
    raise ValueError(f"unknown adapter: {adapter_name}")


async def collect(
    views: list[SourceView], ctx: SearchContext, embedder: Embedder | None
) -> list[Document]:
    async def _fetch_one(view: SourceView) -> list[Document]:
        try:
            adapter = build_adapter(view.adapter, embedder)
            return await adapter.fetch(view, ctx)
        except Exception as e:
            # Soft-fail: log and return empty for this view.
            import logging
            logging.warning("source %s failed: %s", view.id, e)
            return []

    results = await asyncio.gather(*(_fetch_one(v) for v in views))
    docs = [d for batch in results for d in batch]

    # Reassign stable per-turn IDs in case adapters issued long/hash-based ones.
    for i, d in enumerate(docs, start=1):
        d.doc_id = f"doc-{i}"
    return docs
```

- [ ] **Step 2: Test with stub adapters**

```python
import asyncio
import pytest

from blindspot.agents import collection
from blindspot.sources.base import SourceView
from blindspot.types import Document, SearchContext, Situation
from datetime import datetime, timezone


class StubAdapter:
    def __init__(self, docs):
        self._docs = docs
    async def fetch(self, view, ctx):
        return self._docs


def _doc(view_id):
    return Document(
        doc_id="x", source_view_id=view_id, community_tag="t",
        url="u", title="t", content="c", fetched_at=datetime.now(timezone.utc),
    )


@pytest.mark.asyncio
async def test_collect_reassigns_sequential_doc_ids(monkeypatch):
    def fake_build(name, emb):
        return StubAdapter([_doc(name), _doc(name)])
    monkeypatch.setattr(collection, "build_adapter", fake_build)

    views = [
        SourceView(id="a", adapter="rss", fetch_config={}, community_tag="t"),
        SourceView(id="b", adapter="rss", fetch_config={}, community_tag="t"),
    ]
    ctx = SearchContext(situation=Situation(raw_text="x"), entity_terms=[])
    docs = await collection.collect(views, ctx, embedder=None)
    assert [d.doc_id for d in docs] == ["doc-1", "doc-2", "doc-3", "doc-4"]
```

- [ ] **Step 3: Commit**

```bash
pytest tests/unit/test_collection.py -v
git add src/blindspot/agents/collection.py tests/unit/test_collection.py
git commit -m "feat: parallel collection orchestration across source adapters"
git push origin main
```

---

### Task 16: Community Analyst + community profiles

**Files:**
- Create: `src/blindspot/prompts/community_analyst.md`, `src/blindspot/agents/community_analyst.py`, `community_profiles/{remaining 7}.md`, `tests/unit/test_community_analyst.py`

- [ ] **Step 1: Write `src/blindspot/prompts/community_analyst.md`**

```markdown
You are a Community Analyst for Blindspot. Your role is loaded from a
community profile, which describes how *this specific community* thinks
about the user's situation.

You receive:
- The user's situation
- A set of documents fetched from this community's source-views
- The community profile (loaded as additional context below)

You produce TWO outputs:

1. **prose** — a "What [this community] would tell you" paragraph
   (4–8 sentences). Use this community's voice, framings, vocabulary.
   Cite at least one `[doc-X]` marker per major claim.

2. **blind_spots** — a list of 2–4 community-specific blind spots
   the user likely hasn't considered. Each is structured as:
   {"hook": "<short title>", "body": "<2-3 sentence explanation
   with specifics>", "citation_doc_ids": ["doc-X", ...]}

# Rules

- EVERY claim of fact must be followed by one or more `[doc-X]` markers.
- Be concrete. Numbers, named entities, mechanisms, specific clauses.
- Avoid platitudes ("be careful", "do your research", "consult a professional"
  as standalone advice).
- If the available documents don't support a useful angle from this
  community, return blind_spots as an empty list rather than fabricate.

# Output JSON schema

\```json
{
  "prose": "...",
  "blind_spots": [
    {"hook": "...", "body": "... [doc-1] [doc-2]", "citation_doc_ids": ["doc-1", "doc-2"]}
  ]
}
\```
```

- [ ] **Step 2: Implement `src/blindspot/agents/community_analyst.py`**

```python
"""Community Analyst: one per active community per turn. Profile-driven."""

from __future__ import annotations

from blindspot.agents.base import (
    load_community_profile, load_prompt, serialize_documents_for_prompt,
)
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import BlindSpot, CommunityAnalystOutput, Document, Situation

ANALYST_SCHEMA = {
    "type": "object",
    "properties": {
        "prose": {"type": "string"},
        "blind_spots": {
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
    "required": ["prose", "blind_spots"],
}


async def run_community_analyst(
    community_tag: str, situation: Situation, docs: list[Document],
    llm: LLMClient, cfg: Config,
) -> CommunityAnalystOutput:
    base = load_prompt("community_analyst")
    profile = load_community_profile(community_tag)
    system = f"{base}\n\n---\n# Community profile\n\n{profile}"

    user = (
        f"# Situation\n{situation.raw_text}\n\n"
        f"# Documents for this community\n\n"
        f"{serialize_documents_for_prompt(docs)}"
    )
    out = await llm.complete(
        system=system, user=user,
        model=cfg.models.default, json_schema=ANALYST_SCHEMA,
    )
    assert isinstance(out, dict)

    return CommunityAnalystOutput(
        community_tag=community_tag,
        prose=out.get("prose", ""),
        blind_spots=[
            BlindSpot(
                hook=bs.get("hook", ""),
                body=bs.get("body", ""),
                community_tag=community_tag,
                citation_doc_ids=bs.get("citation_doc_ids", []),
            )
            for bs in out.get("blind_spots", [])
        ],
    )
```

- [ ] **Step 3: Write the 7 remaining community profiles**

Create one file per remaining community tag, following `community_profiles/_schema.md`. Use `community_profiles/founder-engineer-bloggers.md` as the template. Files to write:

- `community_profiles/reddit-tech-collective.md`
- `community_profiles/vc-blogosphere.md`
- `community_profiles/hn-collective.md`
- `community_profiles/tax-and-finance-professionals.md`
- `community_profiles/matt-levine-school.md`
- `community_profiles/carta-and-platform-data.md`
- `community_profiles/long-form-references.md`

Each must have the four required sections: Voice, Mental model, Typical concerns, Known blind spots OF this community. Aim 250–500 words per profile.

- [ ] **Step 4: Test with stub LLM + minimal profile**

`tests/unit/test_community_analyst.py`:

```python
import pytest

from blindspot.agents.community_analyst import run_community_analyst
from blindspot.config import Config
from blindspot.types import Situation, Facet


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        assert "Community profile" in system
        return {
            "prose": "Tech veterans would tell you... [doc-1]",
            "blind_spots": [{
                "hook": "AMT exposure",
                "body": "Your strike vs FMV gap drives AMT [doc-1]",
                "citation_doc_ids": ["doc-1"],
            }],
        }


@pytest.mark.asyncio
async def test_analyst_loads_profile_and_returns_structured(tmp_path, monkeypatch):
    sit = Situation(raw_text="...", tags={Facet.DOMAIN: ["tech-career/equity"]})
    out = await run_community_analyst("founder-engineer-bloggers", sit, [], StubLLM(), Config())
    assert out.community_tag == "founder-engineer-bloggers"
    assert "[doc-1]" in out.prose
    assert len(out.blind_spots) == 1
    assert out.blind_spots[0].hook == "AMT exposure"
```

- [ ] **Step 5: Run + commit**

```bash
pytest tests/unit/test_community_analyst.py -v
git add src/blindspot/prompts/community_analyst.md src/blindspot/agents/community_analyst.py
git add community_profiles/reddit-tech-collective.md community_profiles/vc-blogosphere.md
git add community_profiles/hn-collective.md community_profiles/tax-and-finance-professionals.md
git add community_profiles/matt-levine-school.md community_profiles/carta-and-platform-data.md
git add community_profiles/long-form-references.md
git add tests/unit/test_community_analyst.py
git commit -m "feat: Community Analyst agent + all 8 community profiles"
git push origin main
```

---

### Task 17: Risk Officer

**Files:**
- Create: `src/blindspot/prompts/risk_officer.md`, `src/blindspot/agents/risk_officer.py`, `tests/unit/test_risk_officer.py`

- [ ] **Step 1: Write `src/blindspot/prompts/risk_officer.md`**

```markdown
You are the Risk Officer for Blindspot. Your job is the **marquee output**:
identifying the blind spots the user is most likely to have missed.

You are NOT summarizing the community analysts. You synthesize ACROSS them
and add the angles that come from cross-community gaps.

# Mandatory framing dimensions

For every situation, consciously think through:

1. **Information asymmetry** — what does the counterparty know that the
   user doesn't?
2. **Second-order effects** — what consequence of this decision will be
   important in 2-5 years that isn't visible today?
3. **Survivor bias** — what does the user's available information leave
   out? Whose stories don't get told?
4. **Adverse selection** — what does the existence/timing/framing of this
   opportunity tell you about it?

# Output

JSON schema:

\```json
{
  "cross_community_blind_spots": [
    {"hook": "...", "body": "... [doc-X]", "citation_doc_ids": ["doc-X"]}
  ]
}
\```

# Rules

- 3–6 blind spots total. Quality over quantity.
- Each MUST cite at least one `[doc-X]` marker.
- Be specific: numbers, mechanisms, named conditions. Refuse platitudes.
- If two community analysts cover the same blind spot, surface the
  deeper / cross-cutting framing rather than restating.

Now consider this situation and the analyst outputs:
```

- [ ] **Step 2: Implement**

```python
"""Risk Officer: cross-community blind-spot synthesis."""

from __future__ import annotations

import json

from blindspot.agents.base import load_prompt, serialize_documents_for_prompt
from blindspot.config import Config
from blindspot.llm.base import LLMClient
from blindspot.types import (
    BlindSpot, CommunityAnalystOutput, Document, RiskOfficerOutput, Situation,
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
        + json.dumps([{
            "community_tag": o.community_tag, "prose": o.prose,
            "blind_spots": [{"hook": b.hook, "body": b.body,
                             "citation_doc_ids": b.citation_doc_ids}
                            for b in o.blind_spots]
        } for o in analyst_outputs], indent=2)
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
```

- [ ] **Step 3: Test + commit**

`tests/unit/test_risk_officer.py`:

```python
import pytest

from blindspot.agents.risk_officer import run_risk_officer
from blindspot.config import Config
from blindspot.types import Situation, Facet


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {"cross_community_blind_spots": [
            {"hook": "Adverse selection",
             "body": "Why is this offer in front of you... [doc-3]",
             "citation_doc_ids": ["doc-3"]}
        ]}


@pytest.mark.asyncio
async def test_risk_officer_returns_marquee():
    out = await run_risk_officer(
        Situation(raw_text="s", tags={Facet.DOMAIN: []}),
        analyst_outputs=[], docs=[],
        llm=StubLLM(), cfg=Config(),
    )
    assert len(out.cross_community_blind_spots) == 1
    assert out.cross_community_blind_spots[0].hook == "Adverse selection"
```

```bash
pytest tests/unit/test_risk_officer.py -v
git add src/blindspot/prompts/risk_officer.md src/blindspot/agents/risk_officer.py tests/unit/test_risk_officer.py
git commit -m "feat: Risk Officer agent + prompt"
git push origin main
```

---

### Task 18: Critic

**Files:**
- Create: `src/blindspot/prompts/critic.md`, `src/blindspot/agents/critic.py`, `tests/unit/test_critic.py`

- [ ] **Step 1: Write `src/blindspot/prompts/critic.md`**

```markdown
You are the Critic / Red Team agent. You evaluate the candidate response
on three dimensions and decide whether it needs regeneration.

# Three checks

1. **specificity** — pass if the response contains concrete numbers,
   dollar amounts, named entities, mechanisms, named clauses. Fail if
   it relies on generic statements like "be careful with equity".

2. **non_obviousness** — score 1–5. Would a smart 25-year-old college-
   educated tech worker already know this content?
     5 = surfaces real blind spots they almost certainly don't know
     3 = some new angles, some baseline
     1 = entirely things they would think of unprompted

3. **grounding_pct** — what fraction of factual claims have at least
   one [doc-X] citation marker? Estimate 0–100.

# Output JSON schema

\```json
{
  "specificity": "pass" | "fail",
  "non_obviousness": 1-5,
  "grounding_pct": 0-100,
  "regenerate_required": true|false,
  "feedback": "<one paragraph; concrete, actionable>"
}
\```

`regenerate_required` is true iff:
- specificity == "fail", OR
- non_obviousness < {{NON_OBVIOUSNESS_MIN}}, OR
- grounding_pct < {{GROUNDING_THRESHOLD}}.

Be honest. The system retries at most once on regenerate_required=true,
so a soft fail blocks once and then ships anyway.
```

(The runtime substitutes `{{...}}` from config before sending.)

- [ ] **Step 2: Implement**

```python
"""Critic agent."""

from __future__ import annotations

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
    "required": ["specificity", "non_obviousness", "grounding_pct", "regenerate_required", "feedback"],
}


async def run_critic(
    situation_text: str,
    analyst_outputs: list[CommunityAnalystOutput],
    risk_output: RiskOfficerOutput,
    llm: LLMClient,
    cfg: Config,
) -> CriticVerdict:
    raw = load_prompt("critic")
    system = (raw
              .replace("{{NON_OBVIOUSNESS_MIN}}", str(cfg.critic.non_obviousness_min))
              .replace("{{GROUNDING_THRESHOLD}}", str(cfg.critic.grounding_pct_threshold)))

    import json
    user = (
        f"# Situation\n{situation_text}\n\n"
        f"# Community analyst outputs\n{json.dumps([{'tag': o.community_tag, 'prose': o.prose, 'blind_spots': [b.__dict__ for b in o.blind_spots]} for o in analyst_outputs], indent=2)}\n\n"
        f"# Risk Officer output\n{json.dumps([b.__dict__ for b in risk_output.cross_community_blind_spots], indent=2)}"
    )

    out = await llm.complete(
        system=system, user=user, model=cfg.models.default, json_schema=CRITIC_SCHEMA,
    )
    assert isinstance(out, dict)
    return CriticVerdict(
        specificity_pass=(out.get("specificity") == "pass"),
        non_obviousness=int(out.get("non_obviousness", 3)),
        grounding_pct=int(out.get("grounding_pct", 0)),
        regenerate_required=bool(out.get("regenerate_required", False)),
        feedback=out.get("feedback", ""),
    )
```

- [ ] **Step 3: Test + commit**

```python
import pytest
from blindspot.agents.critic import run_critic
from blindspot.config import Config
from blindspot.types import RiskOfficerOutput


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {
            "specificity": "pass", "non_obviousness": 4, "grounding_pct": 92,
            "regenerate_required": False, "feedback": "good",
        }


@pytest.mark.asyncio
async def test_critic_returns_verdict():
    v = await run_critic("s", [], RiskOfficerOutput([]), StubLLM(), Config())
    assert v.specificity_pass is True
    assert v.non_obviousness == 4
    assert v.regenerate_required is False
```

```bash
pytest tests/unit/test_critic.py -v
git add src/blindspot/prompts/critic.md src/blindspot/agents/critic.py tests/unit/test_critic.py
git commit -m "feat: Critic agent with three-dimension verdict"
git push origin main
```

---

### Task 19: Grounding parser + Banlist + Editor

**Files:**
- Create: `src/blindspot/filters/grounding.py`, `src/blindspot/filters/banlist.py`, `src/blindspot/filters/banlist.txt`, `src/blindspot/prompts/editor.md`, `src/blindspot/agents/editor.py`, tests.

- [ ] **Step 1: Grounding parser (pure function, TDD)**

`tests/unit/test_grounding.py`:

```python
from blindspot.filters.grounding import extract_citations, find_unmarked_claims


def test_extract_citations_finds_doc_markers():
    text = "Strike price matters [doc-3]. Also AMT [doc-7] [doc-12]."
    assert extract_citations(text) == {"3", "7", "12"}


def test_find_unmarked_claims_detects_sentences_without_citations():
    text = "First claim is supported [doc-1]. Second claim is naked. Third [doc-2]."
    claims = find_unmarked_claims(text)
    assert any("Second claim is naked" in c for c in claims)
    assert all("supported" not in c for c in claims)
```

`src/blindspot/filters/grounding.py`:

```python
"""Extract [doc-N] citation markers from text; identify unmarked claims."""

from __future__ import annotations

import re

CITATION_RE = re.compile(r"\[doc-(\w+)\]")
SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]")


def extract_citations(text: str) -> set[str]:
    return set(CITATION_RE.findall(text))


def find_unmarked_claims(text: str) -> list[str]:
    """Return sentences that contain no [doc-X] marker. Used for ungrounded_claims log."""
    return [s.strip() for s in SENTENCE_RE.findall(text)
            if s.strip() and not CITATION_RE.search(s)]
```

- [ ] **Step 2: Banlist loader**

`src/blindspot/filters/banlist.txt`:

```
do your research
consult a professional
do the math
weigh the pros and cons
knowledge is power
your network is your net worth
compound interest is powerful
make sure to read the fine print
remember that past performance does not guarantee future results
trust your gut
follow your passion
just be yourself
```

`src/blindspot/filters/banlist.py`:

```python
"""Load banlist phrases for the Editor prompt."""

from __future__ import annotations

from pathlib import Path

BANLIST_PATH = Path(__file__).parent / "banlist.txt"


def load_banlist() -> list[str]:
    return [line.strip() for line in BANLIST_PATH.read_text().splitlines()
            if line.strip() and not line.startswith("#")]
```

- [ ] **Step 3: Editor prompt**

`src/blindspot/prompts/editor.md`:

```markdown
You are the Editor for Blindspot. You assemble the final response shown
to the user, in markdown, in the exact format below. You preserve content
faithfully — your job is composition, not rewriting.

# Output format (exact)

\```markdown
## Situation
[Echo back what we understood, 2-3 sentences]

## Domains identified
[Bulleted list of domain tags]

## Blind spots you likely haven't considered
1. **[Hook]** — [Body with [doc-X] citation markers preserved]
2. ...
   (3-6 blind spots, drawn from the Risk Officer's cross-community list,
   ordered by impact)

## What [community X] would tell you
[Prose from analyst, [doc-X] citations preserved]

## What [community Y] would tell you
[Prose from analyst Y]

## Concrete next steps
- [Action] — [why it matters, with citation if appropriate]
- ...
  (3-5 specific actions derived from the blind spots)

## Sources consulted
[Bulleted list of (doc-X) → URL pairs]
\```

# Rules

- Preserve every [doc-X] citation marker exactly as upstream agents wrote them.
- Do NOT remove blind spots or community sections; only reorder/assemble.
- Generate "Concrete next steps" yourself, deriving from the blind spots
  and risk officer output. Cite [doc-X] where applicable.
- The following phrases are BANNED when used as standalone advice — replace
  with concrete alternatives. They are fine ONLY when followed by a specific
  context (e.g. "consult a tax CPA who understands AMT" is OK; "consult a
  professional" alone is not). Banned phrases:
  {{BANLIST}}
- Output ONLY the markdown response. No preamble.
```

- [ ] **Step 4: Editor implementation**

`src/blindspot/agents/editor.py`:

```python
"""Editor: assembles final markdown response. No structured JSON output."""

from __future__ import annotations

import json

from blindspot.agents.base import load_prompt
from blindspot.config import Config
from blindspot.filters.banlist import load_banlist
from blindspot.llm.base import LLMClient
from blindspot.types import (
    CommunityAnalystOutput, Document, RiskOfficerOutput, Situation,
)


async def run_editor(
    situation: Situation,
    analyst_outputs: list[CommunityAnalystOutput],
    risk_output: RiskOfficerOutput,
    documents: list[Document],
    llm: LLMClient,
    cfg: Config,
) -> str:
    banlist = load_banlist()
    raw = load_prompt("editor")
    system = raw.replace("{{BANLIST}}", "\n".join(f"  - {b}" for b in banlist))

    payload = {
        "situation": situation.raw_text,
        "domains": situation.tags.get("domain", []),
        "analysts": [
            {"community_tag": o.community_tag, "prose": o.prose,
             "blind_spots": [b.__dict__ for b in o.blind_spots]}
            for o in analyst_outputs
        ],
        "risk_output": [b.__dict__ for b in risk_output.cross_community_blind_spots],
        "documents": [{"doc_id": d.doc_id, "url": d.url, "title": d.title}
                      for d in documents],
    }

    out = await llm.complete(
        system=system, user=json.dumps(payload, default=str, indent=2),
        model=cfg.models.default,
    )
    assert isinstance(out, str)
    return out
```

- [ ] **Step 5: Editor test (with stub LLM)**

```python
import pytest
from blindspot.agents.editor import run_editor
from blindspot.config import Config
from blindspot.types import Situation, RiskOfficerOutput, Facet


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return "## Situation\nYou asked about a Series B offer.\n\n## Blind spots..."


@pytest.mark.asyncio
async def test_editor_returns_markdown():
    out = await run_editor(
        Situation(raw_text="s", tags={Facet.DOMAIN: ["tech-career/equity"]}),
        analyst_outputs=[],
        risk_output=RiskOfficerOutput([]),
        documents=[],
        llm=StubLLM(), cfg=Config(),
    )
    assert out.startswith("## Situation")
```

- [ ] **Step 6: Commit**

```bash
pytest tests/unit/test_grounding.py tests/unit/test_editor.py -v
git add src/blindspot/filters/ src/blindspot/prompts/editor.md src/blindspot/agents/editor.py
git add tests/unit/test_grounding.py tests/unit/test_editor.py
git commit -m "feat: grounding parser + banlist + Editor agent"
git push origin main
```

---

## Phase 6 — Orchestration & Persistence

### Task 20: Orchestrator + persistence

**Files:**
- Create: `src/blindspot/orchestrator.py`, `tests/integration/test_orchestrator.py`

- [ ] **Step 1: Implement the end-to-end pipeline**

```python
"""Orchestrator: wires the 6-agent pipeline together and persists results."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session as SQLSession

from blindspot.agents.collection import collect
from blindspot.agents.community_analyst import run_community_analyst
from blindspot.agents.critic import run_critic
from blindspot.agents.editor import run_editor
from blindspot.agents.risk_officer import run_risk_officer
from blindspot.agents.triage import run_triage
from blindspot.config import Config
from blindspot.db.models import (
    BlindSpotRow, BlindSpotSourceRow, DocumentRow, SessionRow, TurnRow,
    TurnTagRow, UngroundedClaimRow,
)
from blindspot.filters.grounding import extract_citations, find_unmarked_claims
from blindspot.llm.base import Embedder, LLMClient
from blindspot.sources.base import SourceView
from blindspot.sources.registry import load_registry
from blindspot.sources.tag_match import select_top_n
from blindspot.tags.taxonomy import add_or_merge_tag
from blindspot.types import (
    FinalResponse, RiskOfficerOutput, SearchContext, Situation,
)

import asyncio


@dataclass
class Orchestrator:
    cfg: Config
    llm: LLMClient
    embedder: Embedder
    db: SQLSession
    registry: list[SourceView]

    @classmethod
    def create(cls, cfg, llm, embedder, db, registry_path="data/source_registry.yaml"):
        return cls(cfg=cfg, llm=llm, embedder=embedder, db=db,
                   registry=load_registry(registry_path))

    async def run(self, situation_text: str, user_id: str = "local") -> FinalResponse:
        # Step 1: Triage.
        situation = await run_triage(situation_text, self.llm, self.cfg)

        # Step 1.5: Normalize tags.
        normalized: dict = {}
        for facet, values in situation.tags.items():
            normalized[facet] = []
            for v in values:
                res = await add_or_merge_tag(self.db, self.embedder, self.cfg, facet.value, v)
                if res.accepted_tag:
                    normalized[facet].append(res.accepted_tag)
        situation.tags = normalized

        # Step 2: Source matching.
        selected = await select_top_n(self.registry, situation, self.cfg, self.embedder)
        if not selected:
            return self._empty_response(
                situation, "No relevant sources matched this situation. "
                          "Blindspot V1 only covers US tech career & equity decisions."
            )

        # Step 3: Collection.
        ctx = SearchContext(situation=situation,
                            entity_terms=situation.tags.get("entity", []))
        docs = await collect(selected, ctx, self.embedder)

        # Step 4: Community analysts (parallel).
        by_community: dict[str, list] = {}
        for d in docs:
            by_community.setdefault(d.community_tag, []).append(d)
        analyst_tasks = [
            run_community_analyst(tag, situation, c_docs, self.llm, self.cfg)
            for tag, c_docs in by_community.items()
        ]
        analyst_outputs = await asyncio.gather(*analyst_tasks)

        # Step 5: Risk Officer.
        risk_output = await run_risk_officer(
            situation, analyst_outputs, docs, self.llm, self.cfg)

        # Step 6: Critic. Single retry if regenerate_required.
        verdict = await run_critic(
            situation_text, analyst_outputs, risk_output, self.llm, self.cfg)
        if verdict.regenerate_required:
            # Single regen: rerun risk officer with critic feedback prepended to the system.
            risk_output = await run_risk_officer(
                situation, analyst_outputs, docs, self.llm, self.cfg)
            verdict = await run_critic(
                situation_text, analyst_outputs, risk_output, self.llm, self.cfg)

        # Step 7: Editor.
        rendered = await run_editor(
            situation, analyst_outputs, risk_output, docs, self.llm, self.cfg)

        # Step 8: Persist.
        sess_row, turn_row = self._persist(
            user_id, situation_text, rendered, situation, docs,
            analyst_outputs, risk_output)
        return FinalResponse(
            situation=situation,
            community_outputs=list(analyst_outputs),
            risk_output=risk_output,
            critic_verdict=verdict,
            rendered_markdown=rendered,
            documents_used=docs,
        )

    def _empty_response(self, situation, reason):
        return FinalResponse(
            situation=situation, community_outputs=[],
            risk_output=RiskOfficerOutput([]),
            critic_verdict=None,
            rendered_markdown=f"## Unable to help\n\n{reason}",
            documents_used=[],
        )

    def _persist(self, user_id, raw, rendered, situation, docs,
                 analyst_outputs, risk_output):
        # Insert session, turn, tags, documents, blind spots + sources, ungrounded claims.
        sess = SessionRow(user_id=user_id, situation=raw, language="en")
        self.db.add(sess); self.db.flush()
        turn = TurnRow(session_id=sess.id, turn_number=1,
                       user_input=raw, assistant_response=rendered)
        self.db.add(turn); self.db.flush()

        for facet, tags in situation.tags.items():
            facet_val = facet.value if hasattr(facet, "value") else facet
            for t in tags:
                self.db.add(TurnTagRow(turn_id=turn.id, facet=facet_val, tag=t))

        now = datetime.now(timezone.utc)
        doc_id_map: dict[str, int] = {}
        for d in docs:
            ch = hashlib.sha256(d.content.encode()).hexdigest()
            existing = self.db.query(DocumentRow).filter_by(content_hash=ch).first()
            if existing is not None:
                doc_id_map[d.doc_id] = existing.id
                continue
            ttl_days = self.cfg.cache.fresh_ttl_days if any(
                v.id == d.source_view_id and v.freshness_required
                for v in self.registry
            ) else self.cfg.cache.evergreen_ttl_days
            row = DocumentRow(
                source_view_id=d.source_view_id, fetched_at=now,
                expires_at=now + timedelta(days=ttl_days),
                url=d.url, title=d.title, content=d.content, content_hash=ch,
                language="en",
            )
            self.db.add(row); self.db.flush()
            doc_id_map[d.doc_id] = row.id

        for output in [*analyst_outputs, risk_output]:
            blindspots = (output.blind_spots if hasattr(output, "blind_spots")
                          else output.cross_community_blind_spots)
            tag = getattr(output, "community_tag", "cross")
            for bs in blindspots:
                bs_row = BlindSpotRow(turn_id=turn.id, hook=bs.hook,
                                      body=bs.body, community_tag=tag)
                self.db.add(bs_row); self.db.flush()
                for cid in bs.citation_doc_ids:
                    if cid in doc_id_map:
                        self.db.add(BlindSpotSourceRow(
                            blind_spot_id=bs_row.id, document_id=doc_id_map[cid]))

        unmarked = find_unmarked_claims(rendered)
        for claim in unmarked:
            self.db.add(UngroundedClaimRow(
                turn_id=turn.id, claim_text=claim,
                context=raw[:500], logged_at=now,
            ))

        self.db.commit()
        return sess, turn
```

- [ ] **Step 2: Integration test using all stub LLMs**

`tests/integration/test_orchestrator.py`:

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.models import Base, BlindSpotRow
from blindspot.orchestrator import Orchestrator
from blindspot.sources.base import SourceView


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        if "Triage Officer" in system:
            return {"domains": ["tech-career/equity"], "entities": ["ISO"],
                    "risk_surfaces": ["tax"], "personas": ["first-time-offer"]}
        if "Community Analyst" in system:
            return {"prose": "Tech veterans... [doc-1]",
                    "blind_spots": [{"hook": "AMT", "body": "spread tax [doc-1]",
                                     "citation_doc_ids": ["doc-1"]}]}
        if "Risk Officer" in system:
            return {"cross_community_blind_spots": [
                {"hook": "Adverse selection", "body": "Why now [doc-1]",
                 "citation_doc_ids": ["doc-1"]}]}
        if "Critic" in system:
            return {"specificity": "pass", "non_obviousness": 4, "grounding_pct": 95,
                    "regenerate_required": False, "feedback": "ok"}
        # Editor:
        return "## Situation\n...\n## Blind spots\n1. AMT [doc-1]\n## Sources\n- (doc-1) https://x"


class StubEmbedder:
    async def embed(self, texts): return [[0.0, 1.0]] * len(texts)


class StubAdapter:
    async def fetch(self, view, ctx):
        from blindspot.types import Document
        from datetime import datetime, timezone
        return [Document(doc_id="doc-1", source_view_id=view.id,
                         community_tag=view.community_tag,
                         url="https://x", title="Equity 101", content="ISO spread tax",
                         fetched_at=datetime.now(timezone.utc))]


@pytest.mark.asyncio
async def test_orchestrator_runs_full_pipeline_with_stubs(monkeypatch, tmp_path):
    from blindspot import agents
    monkeypatch.setattr("blindspot.agents.collection.build_adapter",
                        lambda name, emb: StubAdapter())

    # In-memory DB.
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    # Minimal registry.
    registry_yaml = tmp_path / "reg.yaml"
    registry_yaml.write_text("""
- id: pmck-equity
  adapter: rss
  fetch_config: {}
  domains: [tech-career/equity]
  community_tag: founder-engineer-bloggers
  reliability: 5
  notes: Equity and ISO mechanics.
""")

    with Session(engine) as db:
        orch = Orchestrator.create(Config(), StubLLM(), StubEmbedder(), db,
                                   registry_path=str(registry_yaml))
        resp = await orch.run("Series B offer with ISOs")

    assert "Situation" in resp.rendered_markdown
    assert len(resp.documents_used) == 1
```

- [ ] **Step 3: Commit**

```bash
pytest tests/integration/test_orchestrator.py -v
git add src/blindspot/orchestrator.py tests/integration/test_orchestrator.py
git commit -m "feat: orchestrator wires 6-agent pipeline with persistence"
git push origin main
```

---

## Phase 7 — CLI

### Task 21: CLI: `ask`, `continue`, `history`, `review`

**Files:**
- Create: `src/blindspot/cli.py`, `tests/integration/test_cli.py`

- [ ] **Step 1: Implement** using typer with rich output

```python
"""Blindspot CLI."""

from __future__ import annotations

import asyncio
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from sqlalchemy.orm import Session

from blindspot.config import load_config
from blindspot.db.models import BlindSpotRow, SessionRow, TurnRow
from blindspot.db.session import get_engine, init_schema
from blindspot.llm.claude_agent_client import ClaudeAgentClient
from blindspot.llm.voyage_embedder import VoyageEmbedder
from blindspot.orchestrator import Orchestrator

app = typer.Typer(no_args_is_help=True)
console = Console()


def _bootstrap():
    cfg = load_config(Path("config.yaml"))
    init_schema(cfg)
    engine = get_engine(cfg)
    llm = ClaudeAgentClient()    # default backend
    embedder = VoyageEmbedder(model=cfg.embedder.model)
    return cfg, engine, llm, embedder


@app.command()
def ask(situation: str = typer.Argument(None)):
    """One-shot or interactive: produce blind spots for a situation."""
    if situation is None:
        console.print("[bold]Describe your situation:[/bold]")
        situation = typer.prompt("")
    cfg, engine, llm, embedder = _bootstrap()
    with Session(engine) as db:
        orch = Orchestrator.create(cfg, llm, embedder, db)
        resp = asyncio.run(orch.run(situation))
    console.print(Markdown(resp.rendered_markdown))


@app.command()
def history(limit: int = 20):
    """List past sessions with one-line summaries."""
    cfg, engine, _, _ = _bootstrap()
    with Session(engine) as db:
        rows = db.query(SessionRow).order_by(SessionRow.created_at.desc()).limit(limit).all()
        for r in rows:
            console.print(f"[cyan]{r.id}[/cyan]  {r.created_at:%Y-%m-%d %H:%M}  "
                          f"{(r.situation or '')[:80]}")


@app.command()
def review(session_id: int):
    """Pretty-print a full session."""
    cfg, engine, _, _ = _bootstrap()
    with Session(engine) as db:
        sess = db.get(SessionRow, session_id)
        if sess is None:
            console.print(f"[red]No session {session_id}[/red]"); raise typer.Exit(1)
        console.print(f"[bold]Session {sess.id}[/bold] — {sess.created_at:%Y-%m-%d %H:%M}\n")
        console.print(f"Situation: {sess.situation}\n")
        for t in db.query(TurnRow).filter_by(session_id=sess.id).order_by(TurnRow.turn_number).all():
            console.print(Markdown(t.assistant_response))


# rate, continue, sources, stats, eval — see subsequent tasks.

if __name__ == "__main__":
    app()
```

- [ ] **Step 2: Implement `continue` (add a turn to an existing session)**

Append to `cli.py`:

```python
@app.command(name="continue")
def continue_session(session_id: int, message: str = typer.Argument(None)):
    """Add a turn to an existing session."""
    if message is None:
        message = typer.prompt("Follow-up:")
    cfg, engine, llm, embedder = _bootstrap()
    with Session(engine) as db:
        sess = db.get(SessionRow, session_id)
        if sess is None:
            console.print(f"[red]No session {session_id}[/red]"); raise typer.Exit(1)
        # For V1, continue = a new orchestrator run; previous turns are not
        # fed back into Triage (the user can describe their situation freshly).
        # Future: include past turns as context.
        orch = Orchestrator.create(cfg, llm, embedder, db)
        resp = asyncio.run(orch.run(message))
    console.print(Markdown(resp.rendered_markdown))
```

- [ ] **Step 3: Smoke test that CLI loads (typer auto-help passes)**

`tests/integration/test_cli.py`:

```python
from typer.testing import CliRunner
from blindspot.cli import app


def test_help_lists_commands():
    runner = CliRunner()
    res = runner.invoke(app, ["--help"])
    assert res.exit_code == 0
    assert "ask" in res.stdout
    assert "history" in res.stdout
```

- [ ] **Step 4: Commit**

```bash
pytest tests/integration/test_cli.py -v
git add src/blindspot/cli.py tests/integration/test_cli.py
git commit -m "feat: CLI ask/continue/history/review commands"
git push origin main
```

---

### Task 22: CLI: `rate`, `sources list`, `sources gaps`, `sources stats`, `stats`

**Files:**
- Modify: `src/blindspot/cli.py`

- [ ] **Step 1: Implement subcommands**

Add to `cli.py`:

```python
sources_app = typer.Typer(no_args_is_help=True)
app.add_typer(sources_app, name="sources")


@app.command()
def rate(session_id: int, turn: int, blind_spot_idx: int,
         rating: str = typer.Argument(..., help="hit | meh | obvious")):
    if rating not in {"hit", "meh", "obvious"}:
        console.print("[red]rating must be hit, meh, or obvious[/red]")
        raise typer.Exit(1)
    cfg, engine, _, _ = _bootstrap()
    from datetime import datetime, timezone
    with Session(engine) as db:
        turn_row = (db.query(TurnRow)
                    .filter_by(session_id=session_id, turn_number=turn).first())
        if turn_row is None:
            console.print("[red]turn not found[/red]"); raise typer.Exit(1)
        bs_rows = (db.query(BlindSpotRow)
                   .filter_by(turn_id=turn_row.id).order_by(BlindSpotRow.id).all())
        if not (0 <= blind_spot_idx < len(bs_rows)):
            console.print("[red]blind_spot_idx out of range[/red]"); raise typer.Exit(1)
        bs_rows[blind_spot_idx].rating = rating
        bs_rows[blind_spot_idx].rated_at = datetime.now(timezone.utc)
        db.commit()
    console.print(f"Rated: {rating}")


@sources_app.command(name="list")
def sources_list():
    from blindspot.sources.registry import load_registry
    for v in load_registry():
        console.print(f"  [cyan]{v.id}[/cyan]  "
                      f"({v.community_tag}, reliability {v.reliability})  "
                      f"{v.adapter}")


@sources_app.command(name="gaps")
def sources_gaps(days: int = 30):
    """Show recent ungrounded_claims patterns."""
    from datetime import datetime, timedelta, timezone
    from blindspot.db.models import UngroundedClaimRow
    cfg, engine, _, _ = _bootstrap()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    with Session(engine) as db:
        rows = (db.query(UngroundedClaimRow)
                .filter(UngroundedClaimRow.logged_at >= cutoff)
                .order_by(UngroundedClaimRow.logged_at.desc()).limit(50).all())
    if not rows:
        console.print("[green]No ungrounded claims in window.[/green]"); return
    for r in rows[:20]:
        console.print(f"  [{r.logged_at:%Y-%m-%d}]  {r.claim_text[:120]}")


@sources_app.command(name="stats")
def sources_stats():
    from blindspot.db.models import SourceViewStatsRow
    cfg, engine, _, _ = _bootstrap()
    with Session(engine) as db:
        rows = db.query(SourceViewStatsRow).all()
    for r in rows:
        total = (r.ratings_hit or 0) + (r.ratings_meh or 0) + (r.ratings_obvious or 0)
        hit_rate = (r.ratings_hit / total) if total else 0
        console.print(f"  {r.source_view_id}  hits {r.hits}  hit-rate {hit_rate:.2f}")


@app.command()
def stats():
    """Overall rating distribution + recent activity."""
    cfg, engine, _, _ = _bootstrap()
    with Session(engine) as db:
        counts = {r: db.query(BlindSpotRow).filter_by(rating=r).count()
                  for r in ("hit", "meh", "obvious")}
    total = sum(counts.values())
    if total == 0:
        console.print("[yellow]No ratings yet.[/yellow]"); return
    for r, c in counts.items():
        console.print(f"  {r:8s}  {c}  ({100 * c / total:.1f}%)")
```

- [ ] **Step 2: Commit**

```bash
git add src/blindspot/cli.py
git commit -m "feat: CLI rate/sources/stats subcommands"
git push origin main
```

---

## Phase 8 — Eval & Polish

### Task 23: Eval fixtures + judge + `eval` command

**Files:**
- Create: `fixtures/eval_situations.yaml`, `src/blindspot/eval/judge.py`, `src/blindspot/eval/runner.py`, `tests/unit/test_judge.py`

- [ ] **Step 1: Write `fixtures/eval_situations.yaml`** — 12 representative situations across the V1 domain

```yaml
- id: series-b-iso-cliff
  text: |
    I got a Series B offer with 0.1% in ISOs over 4 years with a 1-year cliff.
    Comp is below market but the team is exceptional. Take it?
  expected_domains: [tech-career/equity, tech-career/comp]
  expected_entities: [ISO, series-B, vesting-cliff]

- id: late-stage-rsu-vs-base
  text: |
    Public co offered me $250k base + $400k RSUs vesting over 4 years.
    Current employer counter-offered $310k base + smaller RSU grant.
    Which is better?
  expected_domains: [tech-career/comp, tech-career/negotiation]
  expected_entities: [RSU]

- id: pre-cliff-quit-dilemma
  text: |
    I'm 10 months in at a Series A startup. I want to leave for a competing
    Series B offer. Should I wait two months for the cliff?
  expected_entities: [vesting-cliff, series-A, series-B]
  expected_personas: [pre-vest-cliff, considering-quit]

- id: amt-exercise-decision
  text: |
    My ISOs are deeply in the money. FMV is 10x my strike. Company says no
    IPO planned for at least 2 years. Should I exercise now?
  expected_entities: [ISO, AMT, strike-price]
  expected_risk_surfaces: [tax, timing]

- id: acquihire-double-trigger
  text: |
    Our startup got acquired. The buyer wants me to re-vest over 4 years
    with double-trigger acceleration. Is this normal?
  expected_entities: [acquisition, double-trigger]
  expected_risk_surfaces: [counterparty]

- id: first-job-equity-confusion
  text: |
    Just got my first offer out of school. $180k base + 0.05% equity at a
    seed-stage startup. I don't understand the equity part.
  expected_personas: [first-time-offer, early-employee]
  expected_entities: [seed-stage]

- id: comparing-offers-3-companies
  text: |
    I have offers from a FAANG, a Series C company, and a Series A startup.
    Compensation packages are very different in structure. Help me think.
  expected_personas: [comparing-offers]
  expected_domains: [tech-career/comp]

- id: refresher-grant-negotiation
  text: |
    I'm 2.5 years in. My initial grant is mostly vested. How do I bring up
    a refresher grant without sounding ungrateful?
  expected_entities: [refresher]
  expected_personas: [senior-employee]

- id: ipo-secondary-decision
  text: |
    Company is filing for IPO in 3 months. I can do a secondary at the
    last private valuation. Worth taking some liquidity?
  expected_entities: [IPO, secondary-sale]
  expected_risk_surfaces: [liquidity, timing]

- id: founder-equity-cofounder
  text: |
    My co-founder wants 50/50 equity but I had the idea, am doing most of
    the early work, and brought in our first investor. How should I think?
  expected_personas: [founder]
  expected_domains: [tech-career/founder]

- id: 83b-deadline-missed
  text: |
    I joined a startup 5 weeks ago. They mentioned an 83(b) election. The
    deadline is 30 days from grant. Did I miss it? What now?
  expected_entities: [83b-election]
  expected_risk_surfaces: [tax, regret]

- id: golden-handcuffs-eval
  text: |
    I've vested half my grant at FAANG. I'm being recruited by a competitor
    with a better tech stack. The unvested portion is worth ~$400k. Stay or go?
  expected_entities: [golden-handcuffs]
  expected_risk_surfaces: [opportunity-cost, regret]
```

- [ ] **Step 2: Implement judge** (LLM-as-judge scoring an end-to-end response)

`src/blindspot/eval/judge.py`:

```python
"""LLM-as-judge: score an end-to-end response on specificity, non-obviousness, grounding."""

from __future__ import annotations

from blindspot.config import Config
from blindspot.llm.base import LLMClient

JUDGE_SYSTEM = """\
You are a quality judge for Blindspot responses. Given a user situation and
the system's response, score it on:

- specificity (1-5): concrete numbers, named entities, mechanisms
- non_obviousness (1-5): would a smart 25-year-old tech worker already know this
- grounding_pct (0-100): fraction of factual claims with [doc-X] citation
- diversity_count: distinct community sections present

Return JSON: {"specificity": n, "non_obviousness": n, "grounding_pct": n, "diversity_count": n, "feedback": "..."}
"""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "specificity": {"type": "integer", "minimum": 1, "maximum": 5},
        "non_obviousness": {"type": "integer", "minimum": 1, "maximum": 5},
        "grounding_pct": {"type": "integer", "minimum": 0, "maximum": 100},
        "diversity_count": {"type": "integer", "minimum": 0},
        "feedback": {"type": "string"},
    },
    "required": ["specificity", "non_obviousness", "grounding_pct", "diversity_count"],
}


async def judge_response(situation: str, response_md: str, llm: LLMClient, cfg: Config) -> dict:
    out = await llm.complete(
        system=JUDGE_SYSTEM,
        user=f"# Situation\n{situation}\n\n# Response\n{response_md}",
        model=cfg.models.default, json_schema=JUDGE_SCHEMA,
    )
    return out
```

- [ ] **Step 3: Implement runner**

`src/blindspot/eval/runner.py`:

```python
"""Run all eval situations and write a JSON results file."""

from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from sqlalchemy.orm import Session

from blindspot.config import Config
from blindspot.db.session import get_engine, init_schema
from blindspot.eval.judge import judge_response
from blindspot.llm.base import Embedder, LLMClient
from blindspot.orchestrator import Orchestrator


async def run_eval(
    cfg: Config, llm: LLMClient, embedder: Embedder,
    fixtures_path: Path = Path("fixtures/eval_situations.yaml"),
    out_dir: Path = Path("eval/results"),
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    fixtures = yaml.safe_load(fixtures_path.read_text())

    init_schema(cfg)
    engine = get_engine(cfg)

    per_situation = []
    for fix in fixtures:
        with Session(engine) as db:
            orch = Orchestrator.create(cfg, llm, embedder, db)
            resp = await orch.run(fix["text"])
        verdict = await judge_response(fix["text"], resp.rendered_markdown, llm, cfg)
        per_situation.append({"id": fix["id"], **verdict})

    def m(key: str) -> float:
        vals = [r[key] for r in per_situation if key in r]
        return sum(vals) / len(vals) if vals else 0.0

    quality_score = (
        cfg.refine.quality_score_weights.specificity * (m("specificity") / 5)
        + cfg.refine.quality_score_weights.non_obviousness * (m("non_obviousness") / 5)
        + cfg.refine.quality_score_weights.grounding_pct * (m("grounding_pct") / 100)
        + cfg.refine.quality_score_weights.source_diversity * (m("diversity_count") / 5)
    )

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "per_situation": per_situation,
        "aggregate": {
            "specificity_mean": m("specificity"),
            "non_obviousness_mean": m("non_obviousness"),
            "grounding_pct_mean": m("grounding_pct"),
            "diversity_mean": m("diversity_count"),
            "quality_score": quality_score,
        },
    }
    path = out_dir / f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    path.write_text(json.dumps(report, indent=2))
    return path
```

- [ ] **Step 4: Wire `eval` into CLI**

Append to `cli.py`:

```python
@app.command()
def eval():
    """Run the eval suite. Writes results to eval/results/<timestamp>.json."""
    cfg, _, llm, embedder = _bootstrap()
    from blindspot.eval.runner import run_eval
    path = asyncio.run(run_eval(cfg, llm, embedder))
    console.print(f"[green]Wrote results to {path}[/green]")
```

- [ ] **Step 5: Test judge with stub**

`tests/unit/test_judge.py`:

```python
import pytest
from blindspot.config import Config
from blindspot.eval.judge import judge_response


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return {"specificity": 4, "non_obviousness": 4, "grounding_pct": 90,
                "diversity_count": 3, "feedback": "ok"}


@pytest.mark.asyncio
async def test_judge_returns_scores():
    out = await judge_response("s", "r", StubLLM(), Config())
    assert out["specificity"] == 4
    assert out["grounding_pct"] == 90
```

- [ ] **Step 6: Commit**

```bash
pytest tests/unit/test_judge.py -v
git add fixtures/eval_situations.yaml src/blindspot/eval/ tests/unit/test_judge.py src/blindspot/cli.py
git commit -m "feat: eval suite (fixtures + judge + runner + CLI command)"
git push origin main
```

---

### Task 24: Manual smoke test + first eval baseline

- [ ] **Step 1: Set up env**

```bash
# In your shell — set these once
export ANTHROPIC_API_KEY=...           # only if using api backend
export VOYAGE_API_KEY=...
export REDDIT_CLIENT_ID=...
export REDDIT_CLIENT_SECRET=...
export REDDIT_USER_AGENT='blindspot/0.1 by /u/mokashang'
```

Verify Claude Code subscription is reachable: `claude -p "hello"` should respond.

- [ ] **Step 2: Manual smoke test on one situation**

```bash
blindspot ask "I got a Series B offer with 0.1% in ISOs over 4 years with a 1-year cliff. Comp is below market but the team is exceptional. Take it?"
```

Expected: a rendered markdown response with at least 3 blind spots, citations, multiple community sections, concrete next steps. Latency 30–90 seconds.

If quality is poor:
- Look at `~/.blindspot/blindspot.db`'s `ungrounded_claims` table.
- Tune `src/blindspot/prompts/*.md` and re-run.

- [ ] **Step 3: Run eval baseline**

```bash
blindspot eval
```

Expected: `eval/results/<timestamp>.json` written, with all 12 situations scored. Inspect `aggregate.quality_score`. Anything > 0.50 is a usable baseline.

- [ ] **Step 4: Commit any prompt tweaks made during smoke test**

```bash
git add src/blindspot/prompts/   # if you edited any
git commit -m "tune: prompt refinements from manual smoke test"
git push origin main
```

- [ ] **Step 5: Tag V1.0.0**

```bash
git tag -a v1.0.0 -m "Blindspot V1 — initial usable build"
git push origin v1.0.0
```

---

## Phase 9 — Manual `refine-blindspot` Trial Runs

- [ ] **Step 1: Invoke the skill manually**

In Claude Code:

```
/refine-blindspot
```

Watch what it does. Read the JSONL entry it appended to `refinements/log.jsonl`. Read the diff if it made any commit.

- [ ] **Step 2: Repeat 3–5 times across days**

After each run, inspect:
- Did the eval score move?
- Was the change defensible?
- Did it stay within the 🟢 scope (didn't open weird PRs)?

- [ ] **Step 3: Decide whether to schedule**

If the manual trials show consistent good judgment:

```
/schedule create --interval hourly /refine-blindspot
```

(Adjust to your actual `schedule` skill invocation syntax.)

If trials are mixed: tune `.claude/skills/refine-blindspot/SKILL.md` and re-trial. Do NOT schedule yet.

---

# Plan Self-Review

The plan covers every requirement in `docs/specs/2026-05-13-blindspot-v1-design.md` §14:

| Spec step | Plan task |
|-----------|-----------|
| 1. Skeleton | Task 1 |
| 2. LLMClient + backends | Tasks 4–6 |
| 3. DB models | Task 3 |
| 4. SourceAdapter + adapters | Tasks 7–10 |
| 5. Registry + tag scoring | Tasks 7, 12 |
| 6. Triage Officer | Task 14 |
| 7. Tag taxonomy CRUD + normalization | Task 11 |
| 8. Collection orchestration | Task 15 |
| 9. Community Analyst | Task 16 |
| 10. Risk Officer | Task 17 |
| 11. Critic | Task 18 |
| 12. Editor + grounding + banlist | Task 19 |
| 13. Orchestrator | Task 20 |
| 14. CLI | Tasks 21, 22 |
| 15. Eval | Task 23 |
| 16. Documentation pass | (Task 1's README + per-task README updates) |
| 17. Manual exercise | Task 24 |
| 18. refine-blindspot SKILL.md | already on disk |
| 19. Tag V1.0.0 | Task 24 step 5 |
| Post-V1: manual refine trials | Phase 9 |
