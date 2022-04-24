from app.configs.database import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

users_giveaway = db.Table('users_giveaway',
    db.Column('id', UUID(as_uuid = True), default=uuid4(), primary_key=True),
    db.Column('user_id', UUID(as_uuid = True), db.ForeignKey('users.id'), ondelete='CASCADE', nullable=False),
    db.Column('giveaway_id', UUID(as_uuid = True), db.ForeignKey('giveaway.id'), ondelete='CASCADE', nullable=False)
)
    
 