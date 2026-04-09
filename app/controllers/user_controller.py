from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional

service = UserService()

class UserController:

    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
        return service.get_all(db, skip, limit, search)

    def get_by_id(self, db: Session, id: int):
        return service.get_by_id(db, id)

    def create(self, db: Session, data: UserCreate):
        return service.create(db, data)

    def update(self, db: Session, id: int, data: UserUpdate):
        return service.update(db, id, data)

    def delete(self, db: Session, id: int):
        return service.delete(db, id)