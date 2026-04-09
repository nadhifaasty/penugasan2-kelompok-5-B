from pydantic import BaseModel
from typing import Optional

class RoleCreate(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Admin"
            }
        }

class RoleUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Super Admin"
            }
        }

class RoleResponse(RoleCreate):
    id: int
    class Config:
        from_attributes = True