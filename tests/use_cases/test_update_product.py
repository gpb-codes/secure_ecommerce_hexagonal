
import pytest
from uuid import uuid4
from domain.entities.product import Product
from application.use_cases.update_product import UpdateProduct


class FakeRepo:
    def __init__(self, product):
        self.product = product

    def get_by_id(self, product_id):
        return self.product

    def save(self, product):
        return product


def test_update_product_ok():
    product = Product.create("Old", 100, 5)
    repo = FakeRepo(product)

    use_case = UpdateProduct(repo)
    updated = use_case.execute(product.id, "New", 200, 10)

    assert updated.name == "New"
