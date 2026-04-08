from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate

class EventRepository:

    def get_all(self, db: Session):
        return db.query(Event).all()

    def get_by_id(self, db: Session, id: int):
        return db.query(Event).filter(Event.id == id).first()

    def get_upcoming(self, db: Session):
        from datetime import datetime
        return db.query(Event).filter(
            Event.started_at >= datetime.now()
        ).all()

    def create(self, db: Session, data: EventCreate):
        event = Event(**data.model_dump())
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    def update(self, db: Session, id: int, data: EventUpdate):
        event = self.get_by_id(db, id)
        if not event:
            return None
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(event, key, val)
        db.commit()
        db.refresh(event)
        return event

    def delete(self, db: Session, id: int):
        event = self.get_by_id(db, id)
        if not event:
            return None
        db.delete(event)
        db.commit()
        return event