from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional

class UserRepository:

    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
        query = db.query(User)
        if search:
            query = query.filter(
                (User.first_name.contains(search)) |
                (User.last_name.contains(search)) |
                (User.whatsapp.contains(search))
            )
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def create(self, db: Session, data: UserCreate):
        user = User(**data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, id: int, data: UserUpdate):
        user = self.get_by_id(db, id)
        if not user:
            return None
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(user, key, val)
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, id: int):
        user = self.get_by_id(db, id)
        if not user:
            return None
        db.delete(user)
        db.commit()
        return user