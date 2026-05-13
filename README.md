# Blindspot

Decision-aware advisor surfacing unknown unknowns from curated community sources.

See `docs/specs/2026-05-13-blindspot-v1-design.md` for the design.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Use

```bash
blindspot ask "I got a Series B offer..."
```

## Develop

```bash
pytest
```
