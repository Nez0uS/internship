import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base

class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    completed = Column(Boolean, default = False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, description={self.description}, completed={self.completed}, created_at={self.created_at})>"
