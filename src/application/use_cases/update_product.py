
from uuid import UUID
from domain.ports.product_repository import ProductRepository


class UpdateProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: UUID, name: str, price: float, stock: int):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Producto no encontrado")

        if not name or len(name.strip()) == 0:
            raise ValueError("Nombre inválido")

        if price <= 0:
            raise ValueError("Precio inválido")

        if stock < 0:
            raise ValueError("Stock inválido")

        product.name = name
        product.price = price
        product.stock = stock

        return self.repository.save(product)
