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
