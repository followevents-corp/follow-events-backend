from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DATETIME , ForeignKey
from app.configs.database import db


@dataclass
class Comment(db.Model):
    
    __tablename__ = 'comments'
    
    id: str
    comment: str
    created_at: str
    user_id: str
    
    now = datetime.utcnow()
    
    id = Column(UUID(as_uuid = True), primary_key=True, default=uuid4())
    comment = Column(String(255), nullable=False)
    created_at = Column(DATETIME, default=now)
    user_id = Column(UUID(as_uuid = True), ForeignKey('user.id'), nullable=False)
    event_id = Column(UUID(as_uuid = True), ForeignKey('event.id'), nullable=False)

