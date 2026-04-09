from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.role_controller import RoleController
from app.schemas.role import RoleCreate, RoleUpdate, RoleResponse
from typing import List, Optional

router = APIRouter(prefix="/roles", tags=["Role"])
controller = RoleController()

@router.get("/", response_model=List[RoleResponse])
def get_all(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None
):
    return controller.get_all(db, skip, limit, search)

@router.get("/{id}", response_model=RoleResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return controller.get_by_id(db, id)

@router.post("/", response_model=RoleResponse, status_code=201)
def create(data: RoleCreate, db: Session = Depends(get_db)):
    return controller.create(db, data)

@router.put("/{id}", response_model=RoleResponse)
def update(id: int, data: RoleUpdate, db: Session = Depends(get_db)):
    return controller.update(db, id, data)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return controller.delete(db, id)