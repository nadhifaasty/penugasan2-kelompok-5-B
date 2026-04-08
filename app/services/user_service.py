from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate

repo = UserRepository()

class UserService:

    def get_all(self, db: Session):
        users = repo.get_all(db)
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
        self.get_by_id(db, id)
        repo.delete(db, id)
        return {"message": "User deleted successfully"}