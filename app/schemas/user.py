from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    whatsapp: Optional[str] = None

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    whatsapp: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    whatsapp: Optional[str]
    created_at: Optional[datetime]
    class Config:
        from_attributes = True