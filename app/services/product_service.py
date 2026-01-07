from app.infrastructure.repositories.in_memory_product_repository import InMemoryProductRepository

class ProductService:

    def __init__(self):
        self.repo = InMemoryProductRepository()

    def list_products(self):
        return self.repo.list()