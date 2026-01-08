
from uuid import UUID
from domain.ports.product_repository import ProductRepository


class DeleteProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: UUID):
        self.repository.delete(product_id)
