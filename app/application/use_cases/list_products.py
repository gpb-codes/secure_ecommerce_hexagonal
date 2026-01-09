
from domain.ports.product_repository import ProductRepository


class ListProducts:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        return self.repository.list_all()
