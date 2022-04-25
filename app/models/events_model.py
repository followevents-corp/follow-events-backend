from flask import Flask
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, CheckConstraint
from datetime import datetime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.services.aws_s3 import AWS_S3
from sqlalchemy.orm import validates

@dataclass
class Events(db.Model):
    id: str
    name: str
    event_date: str
    type_banner: str
    link_banner: str
    quantity_users: int
    created_at: str
    creator_id: str

    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(50), unique = True, nullable = False)
    event_date = Column(String, nullable = False)
    type_banner = Column(String, nullable = False)
    link_banner = Column(String)
    quantity_users = Column(Integer, default = 0)
    created_at = Column(DateTime, default = datetime.utcnow())
    creator_id = Column(String, ForeignKey("user.id"), nullable = False)

    @validates("name")
    def validate_name(self, key, name_to_normalize):
        return name_to_normalize.strip().title()

    @property
    def create_at(self):
        raise AttributeError("Can't access create_at value")

    @property
    def link(self):
        raise AttributeError("Can't access link value")

    @link.setter
    def link(self, link_to_verify):
        object_name = self.name
        response = AWS_S3.upload_file(link_to_verify)
        self.link_banner = response[0]
        if response[1] in ["video", "image"]:
            self.type_banner = response[1]
        else:
            raise TypeError
            #colocar um erro personalizado!
