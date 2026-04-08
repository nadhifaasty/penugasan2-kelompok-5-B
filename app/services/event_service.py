from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.event_repository import EventRepository
from app.schemas.event import EventCreate, EventUpdate

repo = EventRepository()

class EventService:

    def get_all(self, db: Session):
        return repo.get_all(db)

    def get_by_id(self, db: Session, id: int):
        event = repo.get_by_id(db, id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

    def get_upcoming(self, db: Session):
        return repo.get_upcoming(db)

    def create(self, db: Session, data: EventCreate):
        # validasi sudah dilakukan di schema (validator)
        return repo.create(db, data)

    def update(self, db: Session, id: int, data: EventUpdate):
        event = self.get_by_id(db, id)

        # validasi tanggal jika keduanya dikirim
        new_start = data.started_at or event.started_at
        new_end   = data.ended_at   or event.ended_at
        if new_end <= new_start:
            raise HTTPException(
                status_code=400,
                detail="ended_at must be after started_at"
            )

        # validasi quota tidak boleh kurang dari peserta terdaftar
        if data.quota is not None:
            current_count = len(event.registrations)
            if data.quota < current_count:
                raise HTTPException(
                    status_code=400,
                    detail=f"Quota cannot be less than current registrations ({current_count})"
                )

        return repo.update(db, id, data)

    def delete(self, db: Session, id: int):
        event = self.get_by_id(db, id)

        # cek apakah event punya registrasi aktif
        if len(event.registrations) > 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete event that has active registrations"
            )

        repo.delete(db, id)
        return {"message": "Event deleted successfully"}