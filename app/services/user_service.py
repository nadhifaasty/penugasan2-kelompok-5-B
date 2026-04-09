from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional

repo = UserRepository()

class UserService:

    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
        users = repo.get_all(db, skip, limit, search)
        return users

    def get_by_id(self, db: Session, id: int):
        user = repo.get_by_id(db, id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create(self, db: Session, data: UserCreate):
        return repo.create(db, data)

    def update(self, db: Session, id: int, data: UserUpdate):
        # pastikan user ada dulu
        self.get_by_id(db, id)
        user = repo.update(db, id, data)
        return user

    def delete(self, db: Session, id: int):
        # pastikan user ada dulu
        user = self.get_by_id(db, id)

        if len(user.accounts) > 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete user with active accounts"
            )

        if len(user.registrations) > 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete user with active registrations"
            )

        try:
            repo.delete(db, id)
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete user because related records still exist"
            )

        return {"message": "User deleted successfully"}