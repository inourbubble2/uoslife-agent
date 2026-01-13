from datetime import date

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.agent_database.models.base import Base


class Announcement(Base):
    __tablename__ = "announcement"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    announcement_id: Mapped[int] = mapped_column(Integer, unique=True)
    author: Mapped[str] = mapped_column(String(255))
    board: Mapped[str] = mapped_column(String(255))
    body: Mapped[str | None] = mapped_column(Text)
    title: Mapped[str] = mapped_column(String(255))
    major: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(255))
    written_at: Mapped[date | None] = mapped_column()
