from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class EventsCategories(db.Model):
    __tablename__ = "events_categories"

    event_id = (
        Column(
            UUID(as_uuid=True),
            ForeignKey("events.id", ondelete="CASCADE"),
            nullable=False,
        ),
    )
    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
    )
