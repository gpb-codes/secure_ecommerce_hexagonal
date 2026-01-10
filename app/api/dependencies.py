from app.infrastructure.db.connection import sessionlocal
from app.infrastructure.repositories.product_repository_sqlalchemy import (
    ProductRepositorySQLAlchemy,
)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

def get_product_repository(db=next(get_db())):
    return ProductRepositorySQLAlchemy(db)
