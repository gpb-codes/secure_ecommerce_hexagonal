import pytest
from domain.entities.product import Product


def test_create_product_ok():
    product = Product.create("Laptop", 1000, 5)
    assert product.price == 1000
    assert product.stock == 5


def test_invalid_price():
    with pytest.raises(ValueError):
        Product.create("Laptop", -10, 5)


def test_invalid_stock():
    with pytest.raises(ValueError):
        Product.create("Laptop", 1000, -1)
