
import pytest
from uuid import uuid4
from application.use_cases.get_product import GetProduct


class FakeRepo:
    def get_by_id(self, product_id):
        return None


def test_get_product_not_found():
    repo = FakeRepo()
    use_case = GetProduct(repo)

    with pytest.raises(ValueError):
        use_case.execute(uuid4())
