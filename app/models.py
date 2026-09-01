from sqlalchemy import Column, DateTime, Integer, String, Boolean
from app.database import Base
from datetime import datetime

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )