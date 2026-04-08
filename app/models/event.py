from sqlalchemy import Column, Integer, Text, SmallInteger, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    quota       = Column(SmallInteger, nullable=False)
    started_at  = Column(DateTime, nullable=False)
    ended_at    = Column(DateTime, nullable=False)
    created_at  = Column(DateTime, server_default=func.now())
    updated_at  = Column(DateTime, onupdate=func.now())

    registrations = relationship("Registration", back_populates="event")