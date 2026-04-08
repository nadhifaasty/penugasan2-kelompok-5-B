from fastapi import FastAPI
from app.routers import role_router, user_router, account_router, registration_router, event_router

app = FastAPI(title="CRUD API", version="1.0.0")

app.include_router(role_router.router)
# Router lain di-include setelah anggota lain selesai