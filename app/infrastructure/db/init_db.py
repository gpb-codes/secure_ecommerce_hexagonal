# app/infrastructure/db/init_db.py
from infrastructure.db.connection import engine
from infrastructure.db.models import Base

def init_db() -> None:
    Base.metadata.create_all(bind=engine)
