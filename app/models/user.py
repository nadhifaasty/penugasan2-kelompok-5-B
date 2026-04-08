from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=True)
    whatsapp = Column(String(30), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    accounts = relationship("Account", back_populates="user")
    registrations = relationship("Registration", back_populates="user")