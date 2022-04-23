from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Date , ForeignKey
from app.configs.database import db


@dataclass
class Comment(db.Model):
    
    __tablename__ = 'comments'
    
    id: str
    comment: str
    created_at: str
    user_id: str
    
    now = datetime.utcnow()
    
    id = Column(String, primary_key=True, default=uuid4())
    comment = Column(String(255), nullable=False)
    created_at = Column(Date, default=now)
    user_id = Column(String, ForeignKey('user.id'), nullable=False)
    event_id = Column(String, ForeignKey('event.id'), nullable=False)

