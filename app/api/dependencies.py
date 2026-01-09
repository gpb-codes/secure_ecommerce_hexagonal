from infrastructure.repositories.product_repository_sqlalchemy import (
    SQLAlchemyProductRepository,
)


def get_product_repository():
    return SQLAlchemyProductRepository()
