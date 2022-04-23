from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String

from app.configs.database import db


@dataclass
class EventTypes(db.Model):
    type: str

    __tablename__ = "event_types"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)

    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
