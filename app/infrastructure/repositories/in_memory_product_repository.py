from app.domain.models.product import Product
from app.domain.ports.product_repository import ProductRepository

class InMemoryProductRepository(ProductRepository):

    def list(self):
        return [
            Product(id=1, name="Laptop", price=1200),
            Product(id=2, name="Mouse", price=25)
        ]