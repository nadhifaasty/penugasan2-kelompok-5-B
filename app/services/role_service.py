from sqlalchemy.orm import Session
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate
from fastapi import HTTPException

repo = RoleRepository()

class RoleService:
    def get_all(self, db: Session):
        return repo.get_all(db)

    def get_by_id(self, db: Session, id: int):
        role = repo.get_by_id(db, id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    def create(self, db: Session, data: RoleCreate):
        return repo.create(db, data)

    def update(self, db: Session, id: int, data: RoleCreate):
        role = repo.update(db, id, data)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    def delete(self, db: Session, id: int):
        role = repo.delete(db, id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return {"message": "Role deleted"}