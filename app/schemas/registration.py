from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegistrationCreate(BaseModel):
    user_id:  int
    event_id: int

class RegistrationResponse(BaseModel):
    id:         int
    user_id:    int
    event_id:   int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True