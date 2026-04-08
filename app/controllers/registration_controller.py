from sqlalchemy.orm import Session
from app.services.registration_service import RegistrationService
from app.schemas.registration import RegistrationCreate

service = RegistrationService()

class RegistrationController:

    def get_all(self, db: Session):
        return service.get_all(db)

    def get_by_id(self, db: Session, id: int):
        return service.get_by_id(db, id)

    def get_by_user_id(self, db: Session, user_id: int):
        return service.get_by_user_id(db, user_id)

    def get_by_event_id(self, db: Session, event_id: int):
        return service.get_by_event_id(db, event_id)

    def create(self, db: Session, data: RegistrationCreate):
        return service.create(db, data)

    def delete(self, db: Session, id: int):
        return service.delete(db, id)