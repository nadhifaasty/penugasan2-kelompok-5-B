from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegistrationCreate(BaseModel):
    user_id:  int
    event_id: int

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "event_id": 2
            }
        }

class RegistrationUpdate(BaseModel):
    user_id:  Optional[int] = None
    event_id: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "event_id": 3
            }
        }

class RegistrationResponse(BaseModel):
    id:         int
    user_id:    int
    event_id:   int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True