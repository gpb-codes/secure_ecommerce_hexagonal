
from application.use_cases.create_product import CreateProduct
from domain.entities.product import Product


class FakeRepo:
    def save(self, product):
        return product


def test_create_product_use_case():
    repo = FakeRepo()
    use_case = CreateProduct(repo)

    product = use_case.execute("Mouse", 20, 10)

    assert isinstance(product, Product)
