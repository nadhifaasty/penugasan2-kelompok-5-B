from sqlalchemy.orm import Session
from app.services.role_service import RoleService
from app.schemas.role import RoleCreate, RoleUpdate
from typing import Optional

service = RoleService()

class RoleController:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
        return service.get_all(db, skip, limit, search)

    def get_by_id(self, db: Session, id: int):
        return service.get_by_id(db, id)

    def create(self, db: Session, data: RoleCreate):
        return service.create(db, data)

    def update(self, db: Session, id: int, data: RoleUpdate):
        return service.update(db, id, data)

    def delete(self, db: Session, id: int):
        return service.delete(db, id)