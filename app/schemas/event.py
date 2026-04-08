from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
from datetime import datetime

class EventCreate(BaseModel):
    name:        str
    description: Optional[str] = None
    quota:       int
    started_at:  datetime
    ended_at:    datetime

    @field_validator("quota")
    @classmethod
    def quota_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("quota must be greater than 0")
        return v

    @model_validator(mode="after")
    def ended_after_started(self):
        if self.ended_at <= self.started_at:
            raise ValueError("ended_at must be after started_at")
        return self

class EventUpdate(BaseModel):
    name:        Optional[str]      = None
    description: Optional[str]      = None
    quota:       Optional[int]      = None
    started_at:  Optional[datetime] = None
    ended_at:    Optional[datetime] = None

class EventResponse(BaseModel):
    id:          int
    name:        str
    description: Optional[str]
    quota:       int
    started_at:  datetime
    ended_at:    datetime
    created_at:  Optional[datetime]
    updated_at:  Optional[datetime]

    class Config:
        from_attributes = True