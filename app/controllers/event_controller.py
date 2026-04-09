from sqlalchemy.orm import Session
from app.services.event_service import EventService
from app.schemas.event import EventCreate, EventUpdate
from typing import Optional

service = EventService()

class EventController:

    def get_all(self, db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
        return service.get_all(db, skip, limit, search)

    def get_by_id(self, db: Session, id: int):
        return service.get_by_id(db, id)

    def get_upcoming(self, db: Session):
        return service.get_upcoming(db)

    def create(self, db: Session, data: EventCreate):
        return service.create(db, data)

    def update(self, db: Session, id: int, data: EventUpdate):
        return service.update(db, id, data)

    def delete(self, db: Session, id: int):
        return service.delete(db, id)