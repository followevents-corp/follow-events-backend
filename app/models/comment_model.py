from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Date , ForeignKey
from app.configs.database import db


@dataclass
class ModelComment(db.Model):
    
    comment_id: str
    comment: str
    created_at: str
    user_id: str
    username = str
    user_profile_picture = str
    
    now = datetime.utcnow()
    
    comment_id = Column(String, primary_key=True, default=uuid4())
    comment = Column(String(255), nullable=False)
    created_at = Column(Date, default=now)
    user_id = Column(String, ForeignKey('user.id'))
    event_id = Column(String, ForeignKey('event.id'))
    username = Column(String, nullable=False)
    user_profile_picture = Column(String, nullable=False)

