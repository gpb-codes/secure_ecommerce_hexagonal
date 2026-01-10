from typing import Optional, List
from domain.ports.ports import ProductRepository
from domain.ports.product import Product
from infrastructure.db.models import ProductModel


class ProductRepositorySQLAlchemy(ProductRepository):

    def __init__(self, session):
        self.session = session

    def save(self, product: Product) -> None:
        model = ProductModel(
            id=product.id,
            name=product.name,
            price=product.price,
            active=product.active,
        )
        self.session.merge(model)
        self.session.commit()

    def get_by_id(self, product_id: str) -> Optional[Product]:
        model = (
            self.session
            .query(ProductModel)
            .filter_by(id=product_id)
            .first()
        )
        if not model:
            return None

        return Product(
            id=model.id,
            name=model.name,
            price=model.price,
            active=model.active,
        )

    def list_all(self) -> List[Product]:
        models = self.session.query(ProductModel).all()
        return [
            Product(
                id=m.id,
                name=m.name,
                price=m.price,
                active=m.active,
            )
            for m in models
        ]
