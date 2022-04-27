from uuid import uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


class UsersGiveaway(db.Model):
    __tablename__ = "users_giveaway"

    id = Column(UUID(as_uuid=True), default=uuid4(), primary_key=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    giveaway_id = Column(
        UUID(as_uuid=True),
        ForeignKey("giveaway.id", ondelete="CASCADE"),
        nullable=False,
    )
