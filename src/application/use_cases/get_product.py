
from uuid import UUID
from domain.ports.product_repository import ProductRepository


class GetProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: UUID):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Producto no encontrado")
        return product
