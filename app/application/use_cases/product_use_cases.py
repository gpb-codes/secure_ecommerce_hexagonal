from decimal import Decimal
from app.domain.ports.product import Product
from app.domain.ports.ports import ProductRepository
from app.domain.ports.exceptions import ProductNotFound


class CreateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str, name: str, price: Decimal) -> Product:
        product = Product(
            id=product_id,
            name=name,
            price=price,
        )
        self.repository.save(product)
        return product


class GetProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product {product_id} no existe")
        return product


class DeactivateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product {product_id} no existe")

        product = product.deactivate()
        self.repository.save(product)
        return product

class ListProductsUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        return self.repository.list_all()
