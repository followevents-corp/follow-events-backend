import re
from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.exceptions.user_exceptions import EmailFormatError, NameFormatError


@dataclass
class User(db.Model):
    id: str
    username: str
    name: str
    email: str
    profile_picture: str
    creator: bool

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(30), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    hash_password = Column(String(255))
    profile_picture = Column(String)
    creator = Column(Boolean, default=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed")

    @password.setter
    def password(self, password_to_hash):
        self.hash_password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.hash_password, password_to_compare)

    @validates("email")
    def verify_email(self, key, email_to_check: str):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if re.fullmatch(regex, email_to_check):
            return email_to_check.lower()
        else:
            raise EmailFormatError

    @validates("name")
    def normalize_name(self, key, name_to_be_normalized: str):
        regex = r"^[a-zA-Z-0-9\s\w+]*$"

        if re.fullmatch(regex, name_to_be_normalized):
            return name_to_be_normalized.title()
        else:
            raise NameFormatError

    @validates("username")
    def normalize_username(self, key, username_to_be_normalized: str):
        return username_to_be_normalized.lower()
