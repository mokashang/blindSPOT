"""Engine factory and schema bootstrap.

V1 uses `Session(engine)` directly throughout the codebase rather than a
shared sessionmaker — each callsite scopes its own session via `with`.
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine

from blindspot.config import Config
from blindspot.db.models import Base


def get_engine(cfg: Config) -> Engine:
    db_path = Path(cfg.db.path).expanduser()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{db_path}")


def init_schema(cfg: Config) -> None:
    Base.metadata.create_all(get_engine(cfg))
