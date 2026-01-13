from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import BigInteger, ForeignKey, Identity, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.source_database.models.base import Base


class Announcement(Base):
    __tablename__ = "announcement"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    announcementdetail_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("announcement_detail.id"), unique=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    board: Mapped[str] = mapped_column(String(255))
    written_at: Mapped[date | None] = mapped_column()
    view_count: Mapped[int] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column()
    modified_at: Mapped[datetime] = mapped_column()
    target_url: Mapped[str] = mapped_column(String(255))
    scraping_key: Mapped[str | None] = mapped_column(String(255), unique=True)
    major: Mapped[str | None] = mapped_column(String(255))
    detail: Mapped[AnnouncementDetail] = relationship()


class AnnouncementDetail(Base):
    __tablename__ = "announcement_detail"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    url: Mapped[str] = mapped_column(String(255))
    html: Mapped[str] = mapped_column(Text)
