from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str
    password: str

class AccountUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None

class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    email: str
    username: str
    created_at: Optional[datetime]
    class Config:
        from_attributes = True