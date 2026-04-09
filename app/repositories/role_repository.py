from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate
from typing import Optional

class RoleRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
        query = db.query(Role)
        if search:
            query = query.filter(Role.name.contains(search))
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id: int):
        return db.query(Role).filter(Role.id == id).first()

    def create(self, db: Session, data: RoleCreate):
        role = Role(**data.model_dump())
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def update(self, db: Session, id: int, data: RoleUpdate):
        role = self.get_by_id(db, id)
        if not role:
            return None
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(role, key, val)
        db.commit()
        db.refresh(role)
        return role

    def delete(self, db: Session, id: int):
        role = self.get_by_id(db, id)
        if not role:
            return None
        db.delete(role)
        db.commit()
        return role