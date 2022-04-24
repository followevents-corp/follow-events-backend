from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db
from sqlalchemy.orm import validates


@dataclass
class Categories(db.Model):
    name: str

    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(30), nullable=False, unique=True)

    @validates("name")
    def normalize_name(self, key, name_to_be_normalized: str):
        return name_to_be_normalized.title()
