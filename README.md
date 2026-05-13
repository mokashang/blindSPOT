# Blindspot

Decision-aware advisor surfacing unknown unknowns from curated community sources.

See `docs/specs/2026-05-13-blindspot-v1-design.md` for the design.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

**macOS note:** if `import blindspot` fails after install, strip macOS provenance xattrs from the venv and reinstall:
```bash
xattr -cr .venv && pip install -e ".[dev]" --force-reinstall --no-deps
```

## Use

```bash
blindspot ask "I got a Series B offer..."
```

## Develop

```bash
pytest
```
