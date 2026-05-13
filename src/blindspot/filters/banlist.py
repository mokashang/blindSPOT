"""Load banlist phrases for the Editor prompt."""

from __future__ import annotations

from pathlib import Path

BANLIST_PATH = Path(__file__).parent / "banlist.txt"


def load_banlist() -> list[str]:
    return [
        line.strip()
        for line in BANLIST_PATH.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]
