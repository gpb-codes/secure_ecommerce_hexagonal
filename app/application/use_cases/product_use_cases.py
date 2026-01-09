from uuid import UUID
from domain.product import Product
from domain.ports import ProductRepository
from domain.exceptions import ProductNotFoundError


class CreateProduct:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, name: str, price: float, stock: int) -> Product:
        return self.repo.save(Product.create(name, price, stock))


class GetProduct:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, product_id: UUID) -> Product:
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ProductNotFoundError()
        return product


class ListProducts:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self):
        return self.repo.list_all()


class UpdateProduct:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, product_id: UUID, name: str, price: float, stock: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ProductNotFoundError()
        product.update(name, price, stock)
        return self.repo.save(product)


class DeleteProduct:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, product_id: UUID):
        self.repo.delete(product_id)