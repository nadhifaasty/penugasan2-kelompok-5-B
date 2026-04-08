from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.controllers.account_controller import AccountController
from app.schemas.account import AccountCreate, AccountUpdate, AccountResponse

router     = APIRouter(prefix="/accounts", tags=["Account"])
controller = AccountController()

@router.get("/", response_model=List[AccountResponse])
def get_all_accounts(db: Session = Depends(get_db)):
    return controller.get_all(db)

@router.get("/user/{user_id}", response_model=List[AccountResponse])
def get_accounts_by_user(user_id: int, db: Session = Depends(get_db)):
    return controller.get_by_user_id(db, user_id)

@router.get("/{id}", response_model=AccountResponse)
def get_account(id: int, db: Session = Depends(get_db)):
    return controller.get_by_id(db, id)

@router.post("/", response_model=AccountResponse, status_code=201)
def create_account(data: AccountCreate, db: Session = Depends(get_db)):
    return controller.create(db, data)

@router.patch("/{id}", response_model=AccountResponse)
def update_account(id: int, data: AccountUpdate, db: Session = Depends(get_db)):
    return controller.update(db, id, data)

@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    return controller.delete(db, id)