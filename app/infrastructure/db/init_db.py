# app/infrastructure/db/init_db.py
from app.infrastructure.db.connection import engine
from app.infrastructure.db.models import Base

def init_db() -> None:
    Base.metadata.create_all(bind=engine)
