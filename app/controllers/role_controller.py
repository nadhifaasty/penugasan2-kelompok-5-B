from sqlalchemy.orm import Session
from app.services.role_service import RoleService
from app.schemas.role import RoleCreate

service = RoleService()

class RoleController:
    def get_all(self, db: Session):
        return service.get_all(db)

    def get_by_id(self, db: Session, id: int):
        return service.get_by_id(db, id)

    def create(self, db: Session, data: RoleCreate):
        return service.create(db, data)

    def update(self, db: Session, id: int, data: RoleCreate):
        return service.update(db, id, data)

    def delete(self, db: Session, id: int):
        return service.delete(db, id)