"""Blindspot CLI."""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from sqlalchemy.orm import Session

from blindspot.config import load_config
from blindspot.db.models import (
    BlindSpotRow,
    SessionRow,
    SourceViewStatsRow,
    TurnRow,
    UngroundedClaimRow,
)
from blindspot.db.session import get_engine, init_schema
from blindspot.llm.anthropic_api_client import AnthropicAPIClient
from blindspot.llm.claude_agent_client import ClaudeAgentClient
from blindspot.llm.voyage_embedder import VoyageEmbedder
from blindspot.orchestrator import Orchestrator
from blindspot.sources.registry import load_registry

app = typer.Typer(no_args_is_help=True)
sources_app = typer.Typer(no_args_is_help=True)
app.add_typer(sources_app, name="sources")
console = Console()


def _bootstrap_readonly():
    """For commands that just touch the DB — no LLM, no embedder.

    Avoids `KeyError: VOYAGE_API_KEY` etc. when the user runs `history` or
    `sources list` without LLM credentials set.
    """
    cfg = load_config(Path("config.yaml"))
    init_schema(cfg)
    engine = get_engine(cfg)
    return cfg, engine


def _bootstrap_full():
    """For commands that actually call the LLM / embedder."""
    cfg, engine = _bootstrap_readonly()
    if cfg.llm_backend == "anthropic_api":
        llm = AnthropicAPIClient()
    elif cfg.llm_backend == "claude_agent_sdk":
        llm = ClaudeAgentClient()
    else:
        raise typer.BadParameter(
            f"Unknown llm_backend in config.yaml: {cfg.llm_backend!r}. "
            f"Must be 'claude_agent_sdk' or 'anthropic_api'."
        )
    embedder = VoyageEmbedder(
        model=cfg.embedder.model, max_retries=cfg.embedder.max_retries
    )
    return cfg, engine, llm, embedder


@app.command()
def ask(situation: str = typer.Argument(None)):
    """One-shot or interactive: produce blind spots for a situation."""
    if situation is None:
        console.print("[bold]Describe your situation:[/bold]")
        situation = typer.prompt("")
    cfg, engine, llm, embedder = _bootstrap_full()
    with Session(engine) as db:
        orch = Orchestrator.create(cfg, llm, embedder, db)
        resp = asyncio.run(orch.run(situation))
    console.print(Markdown(resp.rendered_markdown))


@app.command(name="continue")
def continue_session(session_id: int, message: str = typer.Argument(None)):
    """Add a turn to an existing session.

    The new turn is appended to the same SessionRow (turn_number = max + 1),
    so `history` / `review` show a real multi-turn thread.
    """
    if message is None:
        message = typer.prompt("Follow-up:")
    cfg, engine, llm, embedder = _bootstrap_full()
    with Session(engine) as db:
        sess = db.get(SessionRow, session_id)
        if sess is None:
            console.print(f"[red]No session {session_id}[/red]")
            raise typer.Exit(1)
        orch = Orchestrator.create(cfg, llm, embedder, db)
        resp = asyncio.run(orch.run(message, session_id=session_id))
    console.print(Markdown(resp.rendered_markdown))


@app.command()
def history(limit: int = 20):
    """List past sessions with one-line summaries."""
    _cfg, engine = _bootstrap_readonly()
    with Session(engine) as db:
        rows = (
            db.query(SessionRow)
            .order_by(SessionRow.created_at.desc())
            .limit(limit)
            .all()
        )
        for r in rows:
            console.print(
                f"[cyan]{r.id}[/cyan]  {r.created_at:%Y-%m-%d %H:%M}  "
                f"{(r.situation or '')[:80]}"
            )


@app.command()
def review(session_id: int):
    """Pretty-print a full session."""
    _cfg, engine = _bootstrap_readonly()
    with Session(engine) as db:
        sess = db.get(SessionRow, session_id)
        if sess is None:
            console.print(f"[red]No session {session_id}[/red]")
            raise typer.Exit(1)
        console.print(
            f"[bold]Session {sess.id}[/bold] — "
            f"{sess.created_at:%Y-%m-%d %H:%M}\n"
        )
        console.print(f"Situation: {sess.situation}\n")
        turns = (
            db.query(TurnRow)
            .filter_by(session_id=sess.id)
            .order_by(TurnRow.turn_number)
            .all()
        )
        for t in turns:
            console.print(Markdown(t.assistant_response))


@app.command()
def rate(
    session_id: int,
    turn: int,
    blind_spot_idx: int,
    rating: str = typer.Argument(..., help="hit | meh | obvious"),
):
    """Rate a specific blind spot from a past turn."""
    if rating not in {"hit", "meh", "obvious"}:
        console.print("[red]rating must be hit, meh, or obvious[/red]")
        raise typer.Exit(1)
    _cfg, engine = _bootstrap_readonly()
    with Session(engine) as db:
        turn_row = (
            db.query(TurnRow)
            .filter_by(session_id=session_id, turn_number=turn)
            .first()
        )
        if turn_row is None:
            console.print("[red]turn not found[/red]")
            raise typer.Exit(1)
        bs_rows = (
            db.query(BlindSpotRow)
            .filter_by(turn_id=turn_row.id)
            .order_by(BlindSpotRow.id)
            .all()
        )
        if not (0 <= blind_spot_idx < len(bs_rows)):
            console.print("[red]blind_spot_idx out of range[/red]")
            raise typer.Exit(1)
        bs_rows[blind_spot_idx].rating = rating
        bs_rows[blind_spot_idx].rated_at = datetime.now(timezone.utc)
        db.commit()
    console.print(f"Rated: {rating}")


@app.command()
def stats():
    """Overall rating distribution + recent activity."""
    _cfg, engine = _bootstrap_readonly()
    with Session(engine) as db:
        counts = {
            r: db.query(BlindSpotRow).filter_by(rating=r).count()
            for r in ("hit", "meh", "obvious")
        }
    total = sum(counts.values())
    if total == 0:
        console.print("[yellow]No ratings yet.[/yellow]")
        return
    for r, c in counts.items():
        console.print(f"  {r:8s}  {c}  ({100 * c / total:.1f}%)")


@sources_app.command(name="list")
def sources_list():
    """List all source-views in the registry."""
    for v in load_registry():
        console.print(
            f"  [cyan]{v.id}[/cyan]  "
            f"({v.community_tag}, reliability {v.reliability})  "
            f"{v.adapter}"
        )


@sources_app.command(name="gaps")
def sources_gaps(days: int = 30):
    """Show recent ungrounded_claims patterns."""
    _cfg, engine = _bootstrap_readonly()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    with Session(engine) as db:
        rows = (
            db.query(UngroundedClaimRow)
            .filter(UngroundedClaimRow.logged_at >= cutoff)
            .order_by(UngroundedClaimRow.logged_at.desc())
            .limit(50)
            .all()
        )
    if not rows:
        console.print("[green]No ungrounded claims in window.[/green]")
        return
    for r in rows[:20]:
        console.print(f"  [{r.logged_at:%Y-%m-%d}]  {r.claim_text[:120]}")


@sources_app.command(name="stats")
def sources_stats():
    """Per-source-view performance stats."""
    _cfg, engine = _bootstrap_readonly()
    with Session(engine) as db:
        rows = db.query(SourceViewStatsRow).all()
    for r in rows:
        total = (r.ratings_hit or 0) + (r.ratings_meh or 0) + (r.ratings_obvious or 0)
        hit_rate = (r.ratings_hit / total) if total else 0
        console.print(
            f"  {r.source_view_id}  hits {r.hits}  hit-rate {hit_rate:.2f}"
        )


@app.command(name="eval")
def eval_cmd(
    per_fixture_timeout: int = typer.Option(
        None,
        "--per-fixture-timeout",
        help=(
            "Wall-clock cap (seconds) per fixture. On timeout the fixture is "
            "recorded as timed_out:true and the eval continues to the next. "
            "Default falls back to config.yaml `eval.per_fixture_timeout_seconds`."
        ),
    ),
):
    """Run the eval suite. Writes results to eval/results/<timestamp>.json."""
    cfg, _engine, llm, embedder = _bootstrap_full()
    from blindspot.eval.runner import run_eval

    path = asyncio.run(
        run_eval(cfg, llm, embedder, per_fixture_timeout_seconds=per_fixture_timeout)
    )
    console.print(f"[green]Wrote results to {path}[/green]")


if __name__ == "__main__":
    app()
