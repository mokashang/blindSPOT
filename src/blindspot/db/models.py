"""SQLAlchemy 2.x declarative models for Blindspot V1.

All tables include a ``user_id`` column (default ``"local"``) to enable future
multi-user support without a migration. The schema mirrors spec §8.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import (
    Float,
    ForeignKey,
    LargeBinary,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def _now() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class SessionRow(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(default="local", index=True)
    created_at: Mapped[datetime] = mapped_column(default=_now)
    situation: Mapped[str] = mapped_column(Text)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    language: Mapped[str] = mapped_column(default="en")


class TurnRow(Base):
    __tablename__ = "turns"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"), index=True)
    turn_number: Mapped[int] = mapped_column()
    user_input: Mapped[str] = mapped_column(Text)
    assistant_response: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=_now)
    user_id: Mapped[str] = mapped_column(default="local")


class TurnTagRow(Base):
    __tablename__ = "turn_tags"

    turn_id: Mapped[int] = mapped_column(ForeignKey("turns.id"), primary_key=True)
    facet: Mapped[str] = mapped_column(primary_key=True)
    tag: Mapped[str] = mapped_column(primary_key=True)


class BlindSpotRow(Base):
    __tablename__ = "blind_spots"

    id: Mapped[int] = mapped_column(primary_key=True)
    turn_id: Mapped[int] = mapped_column(ForeignKey("turns.id"), index=True)
    hook: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column(Text)
    community_tag: Mapped[str] = mapped_column()
    rating: Mapped[str | None] = mapped_column(nullable=True)
    rated_at: Mapped[datetime | None] = mapped_column(nullable=True)


class BlindSpotSourceRow(Base):
    __tablename__ = "blind_spot_sources"

    blind_spot_id: Mapped[int] = mapped_column(
        ForeignKey("blind_spots.id"), primary_key=True
    )
    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id"), primary_key=True
    )


class DocumentRow(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_view_id: Mapped[str] = mapped_column(index=True)
    fetched_at: Mapped[datetime] = mapped_column()
    expires_at: Mapped[datetime] = mapped_column()
    url: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column(Text)
    content_hash: Mapped[str] = mapped_column(unique=True)
    language: Mapped[str] = mapped_column(default="en")


class TagVocabularyRow(Base):
    __tablename__ = "tag_vocabulary"
    __table_args__ = (
        UniqueConstraint("facet", "tag", name="uq_tag_vocabulary_facet_tag"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    facet: Mapped[str] = mapped_column()
    tag: Mapped[str] = mapped_column()
    added_at: Mapped[datetime] = mapped_column(default=_now)
    embedding_blob: Mapped[bytes] = mapped_column(LargeBinary)
    status: Mapped[str] = mapped_column(default="active")


class TagAuditRow(Base):
    __tablename__ = "tag_audit"

    id: Mapped[int] = mapped_column(primary_key=True)
    facet: Mapped[str] = mapped_column()
    proposed_tag: Mapped[str] = mapped_column()
    accepted_tag: Mapped[str] = mapped_column()
    similarity_to_existing: Mapped[float | None] = mapped_column(Float, nullable=True)
    turn_id: Mapped[int | None] = mapped_column(
        ForeignKey("turns.id"), nullable=True
    )
    timestamp: Mapped[datetime] = mapped_column(default=_now)


class UngroundedClaimRow(Base):
    __tablename__ = "ungrounded_claims"

    id: Mapped[int] = mapped_column(primary_key=True)
    turn_id: Mapped[int] = mapped_column(ForeignKey("turns.id"))
    claim_text: Mapped[str] = mapped_column(Text)
    context: Mapped[str | None] = mapped_column(Text, nullable=True)
    logged_at: Mapped[datetime] = mapped_column(default=_now)


class SourceViewStatsRow(Base):
    __tablename__ = "source_view_stats"

    source_view_id: Mapped[str] = mapped_column(primary_key=True)
    period: Mapped[str] = mapped_column(primary_key=True)
    hits: Mapped[int] = mapped_column(default=0)
    ratings_hit: Mapped[int] = mapped_column(default=0)
    ratings_meh: Mapped[int] = mapped_column(default=0)
    ratings_obvious: Mapped[int] = mapped_column(default=0)
