from sqlalchemy.orm import Session
from app.services.registration_service import RegistrationService
from app.schemas.registration import RegistrationCreate, RegistrationUpdate
from typing import Optional

service = RegistrationService()

class RegistrationController:

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return service.get_all(db, skip, limit)

    def get_by_id(self, db: Session, id: int):
        return service.get_by_id(db, id)

    def get_by_user_id(self, db: Session, user_id: int):
        return service.get_by_user_id(db, user_id)

    def get_by_event_id(self, db: Session, event_id: int):
        return service.get_by_event_id(db, event_id)

    def create(self, db: Session, data: RegistrationCreate):
        return service.create(db, data)

    def update(self, db: Session, id: int, data: RegistrationUpdate):
        return service.update(db, id, data)

    def delete(self, db: Session, id: int):
        return service.delete(db, id)