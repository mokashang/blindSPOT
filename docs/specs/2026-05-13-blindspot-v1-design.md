# Blindspot V1 — Design Document

**Date:** 2026-05-13
**Status:** Approved — implementation pending
**Repo:** https://github.com/mokashang/blindSPOT

## 1. Problem

People don't know what they don't know. When facing a decision — a job offer, an equity package, a lease, a medical choice — the things that hurt most are the questions they didn't think to ask. The relevant knowledge usually exists, but it lives inside communities the asker isn't part of: tradespeople, lawyers, recruiters, immigrants who've been through it, people who got burned the same way.

Today, accessing that knowledge requires luck — knowing the right person. Blindspot uses Claude to bridge that gap. The user describes a decision; the system surfaces the questions, risks, and angles they likely haven't considered, grounded in real sources from the communities that actually know.

## 2. V1 scope

**In scope:**
- English-only input/output.
- Single domain: US tech career & equity.
- Hand-curated registry of 13 source-views across 8 community tags (English Reddit, RSS feeds, HN, one static corpus).
- 6-agent pipeline (intelligence-agency metaphor).
- CLI interface only.
- SQLite persistence at `~/.blindspot/blindspot.db`.
- Eval suite (fixture situations → quality regression scoring).
- Refinement-routine skill **written and committed** but not yet scheduled (user invokes manually first).

**Explicitly deferred:**
- Bilingual support (Chinese sources + i18n).
- Hostile-scrape sources: Blind, levels.fyi data API, 1point3acres, RedNote / 小红书, WeChat archives.
- Other domains (immigration, healthcare, real estate, trades, etc.).
- Multi-user / auth.
- Web UI, mobile.
- Production deployment — V1 is local subscription-only.

## 3. Architecture overview

A pipeline of 6 specialized agents borrowing the intelligence-agency metaphor. Each agent is a single async function — not a heavyweight framework object. State flows between them as typed dataclasses. Specialization lives in **system prompts**, not in code abstractions.

| Layer | Agent | Concurrency |
|-------|-------|-------------|
| Entry | Triage Officer | single |
| Collection | Collection Officers (one per active source-view) | parallel |
| Analysis | Community Analysts (one per active community) | parallel |
| Analysis | Risk Officer | single |
| Quality | Red Team / Critic | single |
| Quality | Editor | single |

**Latency budget:** 30–60 seconds per turn, dominated by parallel community-analyst calls. Subscription quota covers V1.

## 4. LLM backend

Pluggable `LLMClient` interface, two implementations:

| Backend | When | How |
|---------|------|-----|
| `ClaudeAgentClient` | V1 default | Uses the `claude-agent-sdk` Python package, which invokes the local `claude` CLI and bills against the Claude Code subscription. |
| `AnthropicAPIClient` | Future production | Direct Anthropic API with API key, per-token billing. |

Selected via `config.yaml`:

```yaml
llm_backend: claude_agent_sdk   # or: anthropic_api
```

All V1 agents call `claude-opus-4-7`. Mixed-model strategy (Haiku for triage/critic, Opus for synthesis) is deferred to production cost optimization; the abstraction already supports it via a `model` parameter.

**Embeddings** use a separate `Embedder` interface. V1 ships `VoyageEmbedder` using `voyage-3` (its own API key, cheap). Embeddings are used for tag-vocabulary normalization and notes-based source-view fallback matching.

## 5. Source layer

### Source-views, not raw sources

The unit of curation is a **source-view**: a configured, filtered, annotated lens into one source. "r/cscareerquestions filtered to equity discussions with min_upvotes=50" is a source-view; "r/cscareerquestions" alone is not.

Source-views are the project's moat. They encode tacit knowledge — which lens on which source for which type of decision — that the LLM alone does not have.

### Registry

Stored in `data/source_registry.yaml`. Schema for each entry:

```yaml
- id: <unique-slug>
  adapter: rss | reddit_search | hn_search | static_corpus
  fetch_config: <adapter-specific>
  domains: [<tag>, ...]
  community_tag: <single-tag>
  reliability: 1-5             # initial; auto-adjusted via rating feedback
  freshness_required: bool     # true → cache TTL 7 days; false → 30 days
  notes: |
    Multi-paragraph description: what this view is good for, what it's
    bad for, typical caveats, expected output character.
```

The `notes` field is load-bearing — (a) it explains the source's value to a human curator, (b) it is embedded and serves as semantic fallback when tag matching produces no hits.

### V1 seed: 13 source-views across 8 community tags

Full content in `data/source_registry.yaml`. Community tags covered:

- `founder-engineer-bloggers` — pmck-equity, danluu-career, pragmatic-engineer
- `reddit-tech-collective` — reddit-cscareerquestions-equity, reddit-experienceddevs, reddit-personalfinance-equity
- `vc-blogosphere` — avc-fred-wilson
- `hn-collective` — hn-equity-discussions
- `tax-and-finance-professionals` — kb-financial-equity
- `matt-levine-school` — matt-levine-money-stuff
- `carta-and-platform-data` — carta-blog, levels-fyi-blog
- `long-form-references` — holloway-equity-guide (manual ingest)

### Diversity constraint at retrieval

Each turn selects top 5 source-views by match score, then enforces **at most 2 source-views per `community_tag`**. The product's value comes from cross-bubble coverage; a result drawing from 5 different communities is structurally better than 5 results from the same forum.

### Adapters

```python
class SourceAdapter(Protocol):
    async def fetch(self, ctx: SearchContext) -> list[Document]: ...
```

`SearchContext` carries the situation text, extracted tags (entities, etc.), and adapter-specific hints. Each adapter decides how to use them.

V1 adapters:

- `RedditSearchAdapter` — PRAW with read-only credentials.
- `RSSAdapter` — `feedparser`; applies the registry's `keyword_filter`.
- `HNSearchAdapter` — Algolia HN search API (no auth required).
- `StaticCorpusAdapter` — splits a local markdown file into chunks, retrieves top-K by `voyage-3` semantic similarity.

All adapters cache fetched documents in the `documents` table (see §8) with `expires_at` derived from `freshness_required`.

## 6. Tag taxonomy

### Four facets

Each situation is described by tags across four facets:

| Facet | Structure | V1 seed size |
|-------|-----------|--------------|
| domain | hierarchical (`tech-career/equity`) | 9 |
| entity | flat controlled string | 27 |
| risk_surface | flat controlled string | 9 |
| persona | flat controlled string | 8 |

Total V1 seed: 53 tags. Full seed at `data/tag_taxonomy_seed.yaml`.

### Open vocabulary + auto-normalization

V1 starts with the seed but the vocabulary is **open**: the Triage Officer may propose new tags. No human-review gate. Fragmentation is prevented by automatic normalization:

1. For each proposed new tag, compute `voyage-3` embedding.
2. Compare to embeddings of all existing tags in the same facet.
3. If max cosine similarity > 0.85, **merge** into the existing tag.
4. Otherwise, **add** the new tag and append a row to `tag_audit` (audit log, no gate).

Source-views' tag coverage also evolves: when a new tag is added, a lightweight background job scans every source-view's `notes`; if the new tag (or close synonym via embedding) is mentioned, it's appended to that source-view's `coverage` set.

### Matching score

For each candidate source-view:

```
score =   3.0 × |domain ∩ situation.domain|
        + 2.0 × |entity ∩ situation.entity|
        + 1.5 × |risk_surface ∩ situation.risk_surface|
        + 1.5 × |persona ∩ situation.persona|
        + 1.0 × cosine(embed(situation), embed(source.notes))
score *= reliability_multiplier
```

Where `reliability_multiplier = reliability / 3.0` (reliability 5 → ×1.67; reliability 3 → ×1.0; reliability 1 → ×0.33).

Top-5 selection, then apply diversity constraint (max 2 per `community_tag`).

All weights live in `config.yaml`, tunable without code change.

## 7. Quality pipeline

### Grounding: inline citation markers (option A)

Synthesizer agents (Community Analysts, Risk Officer) are given each fetched document with a stable per-turn ID like `[doc-37]`. The system prompt requires each blind spot and each community-knowledge claim to be followed by one or more `[doc-X]` markers naming the supporting document(s). The Editor parses these:

- Extract markers from the final assembled response.
- For each blind-spot row, populate the `blind_spot_sources` join table.
- If any claim has zero markers, log to the `ungrounded_claims` table with the claim text and surrounding context.

The Editor does NOT remove unmarked claims — it preserves them but flags them. This avoids over-strict pipeline failures on minor formatting drift.

### Critic / Red Team

Single Opus call. Returns structured JSON across three checks:

1. **Specificity** — does the output contain concrete numbers, named entities, dollar amounts, mechanisms, named documents/processes? Generic statements ("be careful with equity") get flagged for regeneration.
2. **Non-obviousness** — would a smart 25-year-old college-educated tech worker already know this? Critic explicitly rejects baseline-knowledge claims.
3. **Grounding density** — what fraction of claims have at least one `[doc-X]` marker? Threshold 80%.

Output schema:

```json
{
  "specificity": "pass" | "fail",
  "non_obviousness": 1-5,
  "grounding_pct": 0-100,
  "regenerate_required": true|false,
  "feedback": "..."
}
```

Max 1 regeneration per turn. On second failure, ship with a quality warning and log to `ungrounded_claims`. The user sees what happened.

### Banlist (in Editor, not a separate pass)

`filters/banlist.txt` lists forbidden patterns ("do your research", "consult a professional" as standalone advice, "knowledge is power", "compound interest is powerful", etc.). The list is loaded into the Editor's system prompt at startup. The Editor judges context — "consult a lawyer for your I-485 question" is fine; "consult a professional" alone is not. Static substring matching is too brittle for this.

### Eval suite

CLI: `blindspot eval`. Runs ~15 fixture situations through the full pipeline. Writes a JSON quality report to `eval/results/<timestamp>.json` with per-situation specificity, non-obviousness, grounding %, and source-diversity index; aggregate means; and regression vs the previous run.

Fixture situations live at `fixtures/eval_situations.yaml`. The user runs `eval` periodically and reviews regressions manually. The refinement routine (§12) consumes this output programmatically.

## 8. DB schema

SQLite via SQLAlchemy. All tables include `user_id` defaulting to `"local"` for future multi-user.

```
sessions            (id, user_id, created_at, situation, summary, language)
turns               (id, session_id, turn_number, user_input,
                     assistant_response, created_at)
turn_tags           (turn_id, facet, tag)            -- multiple rows per turn
blind_spots         (id, turn_id, hook, body, community_tag,
                     rating, rated_at)
blind_spot_sources  (blind_spot_id, document_id)     -- many-to-many join
documents           (id, source_view_id, fetched_at, expires_at,
                     url, content, content_hash, language)
                                                     -- renamed from `sources`
tag_vocabulary      (id, facet, tag, added_at, embedding_blob, status)
tag_audit           (id, facet, proposed_tag, accepted_tag,
                     similarity_to_existing, turn_id, timestamp)
ungrounded_claims   (id, turn_id, claim_text, context, logged_at)
source_view_stats   (source_view_id, period, hits,
                     ratings_hit, ratings_meh, ratings_obvious)
```

**Stored outside the DB:**

- Source-view registry → `data/source_registry.yaml` (version-controlled, hand-editable).
- Community profiles → `community_profiles/*.md` (version-controlled).
- Refinement log → `refinements/log.jsonl` (committed to git, append-only).

`source_view_id` in `documents` and `source_view_stats` is the slug string from the YAML registry (e.g. `"pmck-equity"`), not an FK to a DB table. Referential integrity is enforced at write-time by the registry loader, not by the schema.

**Indexes:** `(turn_id)` on `blind_spots`; `(source_view_id)` on `documents`; unique `(content_hash)` on `documents` (dedup across fetches).

## 9. CLI commands

Implemented via `typer`. All commands operate on the local DB at `~/.blindspot/blindspot.db`.

```
blindspot ask                                  # interactive: prompt then run
blindspot ask "<situation>"                    # one-shot
blindspot continue <session_id>                # add a turn to existing session
blindspot history                              # list past sessions
blindspot review <session_id>                  # pretty-print full session
blindspot rate <session_id> <turn> <bs_idx> <hit|meh|obvious>
blindspot sources list                         # show registry
blindspot sources add                          # interactive add to registry
blindspot sources gaps                         # ungrounded_claims report
blindspot sources stats                        # per-source-view performance
blindspot stats                                # overall stats + rating distribution
blindspot eval                                 # run eval suite
```

## 10. File / module structure

```
blindspot/
├── README.md
├── pyproject.toml
├── config.yaml
├── .gitignore
├── docs/
│   └── specs/
│       └── 2026-05-13-blindspot-v1-design.md
├── src/blindspot/
│   ├── __init__.py
│   ├── cli.py
│   ├── orchestrator.py
│   ├── llm/
│   │   ├── base.py                       # LLMClient Protocol + Embedder
│   │   ├── claude_agent_client.py
│   │   ├── anthropic_api_client.py
│   │   └── voyage_embedder.py
│   ├── agents/
│   │   ├── base.py
│   │   ├── triage.py
│   │   ├── collection.py
│   │   ├── community_analyst.py
│   │   ├── risk_officer.py
│   │   ├── critic.py
│   │   └── editor.py
│   ├── sources/
│   │   ├── base.py                       # SourceAdapter Protocol
│   │   ├── registry.py                   # load + match against tags
│   │   ├── tag_match.py                  # scoring + diversity
│   │   └── adapters/
│   │       ├── reddit_search.py
│   │       ├── rss.py
│   │       ├── hn_search.py
│   │       └── static_corpus.py
│   ├── tags/
│   │   ├── taxonomy.py                   # vocab CRUD + normalization
│   │   └── extractor.py                  # parse Triage structured output
│   ├── filters/
│   │   ├── banlist.py
│   │   ├── banlist.txt
│   │   └── grounding.py                  # parse [doc-X] markers
│   ├── db/
│   │   ├── models.py                     # SQLAlchemy
│   │   └── migrations/
│   ├── prompts/
│   │   ├── triage.md                     # one .md per agent — agent loads its
│   │   ├── community_analyst.md          #   system prompt from here at startup.
│   │   ├── risk_officer.md               #   Refine routine edits these.
│   │   ├── critic.md
│   │   └── editor.md
│   └── eval/
│       ├── runner.py
│       └── judge.py
├── community_profiles/
│   ├── _schema.md                        # how to write a profile
│   ├── founder-engineer-bloggers.md
│   ├── reddit-tech-collective.md
│   ├── vc-blogosphere.md
│   ├── hn-collective.md
│   ├── tax-and-finance-professionals.md
│   ├── matt-levine-school.md
│   ├── carta-and-platform-data.md
│   └── long-form-references.md
├── data/
│   ├── source_registry.yaml
│   ├── tag_taxonomy_seed.yaml
│   └── static/
│       └── holloway-equity-guide.md      # paste relevant chapters
├── fixtures/
│   └── eval_situations.yaml
├── refinements/
│   └── log.jsonl                         # written by refine-blindspot skill
├── .claude/
│   ├── settings.json                     # pre-commit code-review hook
│   └── skills/
│       └── refine-blindspot/
│           └── SKILL.md                  # scaffolded, not yet scheduled
└── tests/
```

## 11. Pipeline walkthrough

User enters:

> "I got a Series B offer, 0.1% in ISOs over 4 years with 1-year cliff. Comp below market but I like the team. Take it?"

1. **Triage Officer** (Opus, structured JSON output)
   - Extracts: `domain: [tech-career/equity, tech-career/comp]`, `entity: [series-B, ISO, vesting-cliff]`, `risk: [tax, counterparty, opportunity-cost]`, `persona: [considering-offer, comparing-offers]`.
   - May propose new tags; these go through the normalization pipeline (§6) before being attached to the turn.

2. **Source matching** (pure data, no LLM)
   - Score each source-view against extracted tags using the formula in §6.
   - Top 5 with diversity constraint applied. Example output:
     - `pmck-equity` (founder-engineer-bloggers)
     - `kb-financial-equity` (tax-and-finance-professionals)
     - `reddit-experienceddevs` (reddit-tech-collective)
     - `avc-fred-wilson` (vc-blogosphere)
     - `carta-blog` (carta-and-platform-data)
   - The set of *active communities* for this turn is the union of `community_tag` values across these selected source-views — here, 5 communities.

3. **Collection Officers** (parallel async, ~5–10 s)
   - Each adapter fetches documents matching the entity terms. Cache hits skip the network.
   - Output: 15–30 documents total, each assigned a per-turn stable ID `doc-1` … `doc-N`.

4. **Community Analysts** (parallel async, ~15 s)
   - 4 analysts run concurrently. Each is loaded with its community profile as system prompt + the documents from source-views in its community.
   - Each emits: "What [community] would tell you" prose section + 2–4 community-specific blind spots, all with `[doc-X]` citation markers.

5. **Risk Officer** (Opus, ~10 s)
   - Receives full situation + all analyst outputs.
   - System prompt explicitly primes information-asymmetry / second-order effects / survivor bias / adverse selection thinking.
   - Emits the marquee blind-spots list — cross-community synthesis of what the user is most likely to miss.

6. **Critic** (Opus, ~5 s)
   - Scores specificity, non-obviousness, grounding %.
   - If `regenerate_required`, sends feedback to the offending upstream agent and reruns (max 1 retry).

7. **Editor** (Opus, ~5 s)
   - Receives all upstream outputs + banlist + format template.
   - Assembles final markdown. Removes banlist hits in non-justified contexts. Ensures every blind spot has hook + body + citation.
   - Returns final response + structured metadata for DB persistence.

8. **Persistence**
   - Insert/upsert: `turns`, `turn_tags`, `blind_spots`, `blind_spot_sources`, any new `documents`, any new `tag_vocabulary` entries, any `ungrounded_claims`.

9. **Output** to terminal in the format from the original brief.

## 12. Post-V1: Refinement Routine

Designed and scaffolded in V1; activated after V1 ships with at least the eval suite working.

### Skill: `refine-blindspot`

Lives at `.claude/skills/refine-blindspot/SKILL.md`. Invoked manually first, then scheduled hourly via the `schedule` skill once trust is established.

### Per-run procedure

1. **Read state**: last N entries from `refinements/log.jsonl`, recent `git log`, latest `eval/results/*.json`, any new user ratings.
2. **Evaluate previous change** — did the signal move as predicted?
   - POSITIVE → continue the suggested path with finer tweaks.
   - NEUTRAL → switch angle; the path isn't producing signal.
   - NEGATIVE → either `git revert` or refine in opposite direction.
3. **Decide direction** — structured monologue across four dimensions: *prompt clarity*, *coverage gaps*, *signal-to-noise*, *failure-mode patterns*. (Does NOT invoke the interactive `brainstorming` skill — the routine reasons solo.)
4. **Apply change** under strict scope (see Scope tiers below).
5. **Verify** — run eval suite. If eval regresses on aggregate signal, revert.
6. **Log** — append a JSON entry to `refinements/log.jsonl`: timestamp, action, prediction of effect, which signals to check next time.
7. **Commit + push** to GitHub.

### Scope tiers (the safety constraint)

There is no "never touch" tier — the worst case is always 🟡 (open a PR for the user to review). The PR mechanism is the safety net.

| Tier | Action | Files |
|------|--------|-------|
| 🟢 Auto-commit + push to main | direct edit on `main`, no review | `src/blindspot/prompts/*.md`, `community_profiles/*.md`, `data/source_registry.yaml` (only the `notes` / `reliability` / `freshness_required` fields on existing entries — not adding new entries), `fixtures/eval_situations.yaml` (additive only), `docs/**/*.md`, `config.yaml` (only fields declared under `tunable_keys` in the config schema, within their declared ranges) |
| 🟡 Branch + auto-PR | create branch, push, open PR via `gh`; never merge yourself | everything else, including: `src/**/*.py` (any code change), `db/migrations/**`, `pyproject.toml`, `.claude/settings.json`, `.claude/hooks/**`, `tests/**`, **new** entries in `source_registry.yaml` or `tag_taxonomy_seed.yaml`, **new** community profile files, config schema additions, **any file deletion** |

PRs that touch security-sensitive files (`.claude/settings.json`, `.claude/hooks/**`, `pyproject.toml` dependency additions) get an extra flag in the PR body so the user knows to scrutinize them harder.

### Signal function

```
quality_score =
    0.35 × eval_specificity_mean
  + 0.25 × eval_non_obviousness_mean
  + 0.20 × eval_grounding_pct_mean
  + 0.15 × source_diversity_index           # unique community_tags / N
  + 0.05 × (1 - ungrounded_claims_per_turn) # bounded to [0, 1]
```

When real user-rating data accumulates, add a fifth term (weight 0.40, rebalance the others):

```
+ 0.40 × hit_rate_30d
```

### Start gate

The routine does NOT auto-start. Sequence:

1. V1 ships. `blindspot eval` produces stable scores.
2. User manually invokes the skill 3–5 times. Reviews `refinements/log.jsonl` for quality of judgments.
3. User decides to schedule. The `schedule` skill mounts an hourly remote agent.
4. Weekly human review of the routine's `git log` — `git revert` any drift, tune the skill's system prompt as needed.

## 13. Risks & open questions

- **LLM-as-judge for "non-obviousness"** is known to be noisy. Mitigation: use the score as a coarse signal, not a hard threshold; show it in eval reports for human override.
- **Reddit API stability** — Reddit has changed pricing/access policies before. Mitigation: PRAW with read-only auth; cache aggressively; if blocked, fall back to manual ingest (treat the source as `static_corpus`).
- **30–60 s latency** is long for a CLI prompt. Mitigation: clear progress indicator per agent in V1; streaming editor output in V1.1.
- **Subscription quota under refine-routine** — hourly autonomous runs use significant quota. Mitigation: skip-if-no-change throttle in the skill; manual cadence first.
- **One-domain brittleness** — first user asking a non-tech-career question gets a poor answer. Mitigation: Triage Officer explicitly refuses out-of-domain queries with a clear message instead of generating low-quality output.

## 14. Implementation order

1. Project skeleton (`pyproject.toml`, dirs, deps, dev tooling).
2. `LLMClient` Protocol + `ClaudeAgentClient` + `VoyageEmbedder` + `AnthropicAPIClient` stub.
3. DB models + migrations.
4. `SourceAdapter` Protocol + Reddit + RSS + HN + StaticCorpus.
5. Registry loader + tag scoring + diversity constraint.
6. Triage Officer (with structured output).
7. Tag taxonomy CRUD + normalization (auto-merge / auto-add).
8. Collection orchestration.
9. Community Analyst (generic, profile-driven).
10. Risk Officer.
11. Critic.
12. Editor + grounding parser + banlist.
13. Orchestrator wiring all 6 agents.
14. CLI commands (one at a time).
15. Eval command + fixtures + judge.
16. Documentation pass + README.
17. Manual exercise across 5–10 real situations; tune prompts.
18. Write `refine-blindspot` skill (production-ready `SKILL.md`, don't schedule yet — done as part of V1 spec phase, see `.claude/skills/refine-blindspot/SKILL.md`).
19. Tag V1.0.0, push to GitHub.
