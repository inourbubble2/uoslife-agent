import uuid
from datetime import date

from pgvector.sqlalchemy import Vector
from sqlalchemy import UUID, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.agent_database.models.base import Base


class AnnouncementEmbedding(Base):
    __tablename__ = "announcement_embedding"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    embedding: Mapped[Vector] = mapped_column(Vector(1536))
    document: Mapped[str] = mapped_column(Text)
    chunk_index: Mapped[int] = mapped_column(Integer)

    announcement_id: Mapped[int] = mapped_column(Integer)
    author: Mapped[str] = mapped_column(String(255))
    board: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255))
    major: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))
    written_at: Mapped[date | None] = mapped_column()
