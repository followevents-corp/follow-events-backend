from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from sqlalchemy import DATETIME, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class Comment(db.Model):

    __tablename__ = "comments"

    id: str
    comment: str
    created_at: str
    user_id: str

    now = datetime.utcnow()

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    comment = Column(String(255), nullable=False)
    created_at = Column(DATETIME, default=now)
    user_id = Column(UUID(as_uuid = True), ForeignKey('users.id', ondelete="CASCADE") , nullable=False)
    event_id = Column(UUID(as_uuid = True), ForeignKey('events.id', ondelete="CASCADE"), nullable=False)
