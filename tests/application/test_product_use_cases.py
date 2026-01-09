from uuid import uuid4
import pytest
from domain.entities.product import Product
from domain.ports.exceptions import ProductNotFoundError
from application.product_use_cases import *


class FakeRepo:
    def __init__(self):
        self.products = {}

    def save(self, product):
        self.products[product.id] = product
        return product

    def get_by_id(self, product_id):
        return self.products.get(product_id)

    def list_all(self):
        return list(self.products.values())

    def delete(self, product_id):
        self.products.pop(product_id, None)


def test_create_product():
    repo = FakeRepo()
    product = CreateProduct(repo).execute("Laptop", 1000, 5)
    assert product.id in repo.products


def test_get_product_not_found():
    repo = FakeRepo()
    with pytest.raises(ProductNotFoundError):
        GetProduct(repo).execute(uuid4())


def test_update_product():
    repo = FakeRepo()
    product = CreateProduct(repo).execute("Old", 100, 1)
    updated = UpdateProduct(repo).execute(product.id, "New", 200, 2)
    assert updated.name == "New"


def test_delete_product():
    repo = FakeRepo()
    product = CreateProduct(repo).execute("Mouse", 20, 5)
    DeleteProduct(repo).execute(product.id)
    assert repo.list_all() == []
