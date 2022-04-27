from dataclasses import dataclass
from datetime import datetime as dt
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class Giveaway(db.Model):
    id: str
    name: str
    description: str
    award: str
    award_picture: str
    active: bool
    created_at: str
    event_id: str

    __tablename__ = "giveaway"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    award = Column(String(50), nullable=False)
    award_picture = Column(String)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=dt.utcnow())
    event_id = Column(
        UUID(as_uuid=True), ForeignKey("events.id", ondelete="CASCADE"), nullable=False
    )
