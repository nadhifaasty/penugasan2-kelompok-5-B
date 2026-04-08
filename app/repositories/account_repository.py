from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate

class AccountRepository:

    def get_all(self, db: Session):
        return db.query(Account).all()

    def get_by_id(self, db: Session, id: int):
        return db.query(Account).filter(Account.id == id).first()

    def get_by_username(self, db: Session, username: str):
        return db.query(Account).filter(Account.username == username).first()

    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(Account).filter(Account.user_id == user_id).all()

    def create(self, db: Session, data: AccountCreate):
        account = Account(**data.model_dump())
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def update(self, db: Session, id: int, data: AccountUpdate):
        account = self.get_by_id(db, id)
        if not account:
            return None
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(account, key, val)
        db.commit()
        db.refresh(account)
        return account

    def delete(self, db: Session, id: int):
        account = self.get_by_id(db, id)
        if not account:
            return None
        db.delete(account)
        db.commit()
        return account