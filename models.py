from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Todo(Base):
    __tablename__ = "Todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    completed = Column(Boolean, default=False)