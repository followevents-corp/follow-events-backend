from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class UserModel(db.Model):
    id: str
    name: str
    username: str
    email: str
    profile_picture: str
    creator: bool
    # schedule: str
    # events: str

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hash_password = Column(String)
    profile_picture = Column(String)
    creator = Column(Boolean, nullable=False)

    # schedule = relationship("EventModel", secondary=schedule_table)

    # events = relationship("EventModel", backref=backref("creator", uselist=False))

    @property
    def password(self):
        raise AttributeError("Não é possível acessar o atributo password")

    @password.setter
    def password(self, password_to_hash):
        self.hash_password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.hash_password, password_to_compare)
