from email.policy import default
from app.configs.database import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

users_giveaway = db.Table('users_giveaway',
    db.Column('id', UUID(as_uuid = True), default=uuid4(), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('giveaway_id', db.Integer, db.ForeignKey('giveaway.id'))
)
    
