from dataclasses import dataclass
from uuid import UUID, uuid4
from domain.exceptions import InvalidProductDataError


@dataclass
class Product:
    id: UUID
    name: str
    price: float
    stock: int
    is_active: bool = True

    @staticmethod
    def create(name: str, price: float, stock: int) -> "Product":
        Product._validate(name, price, stock)
        return Product(uuid4(), name, price, stock)

    def update(self, name: str, price: float, stock: int) -> None:
        Product._validate(name, price, stock)
        self.name = name
        self.price = price
        self.stock = stock

    @staticmethod
    def _validate(name: str, price: float, stock: int):
        if not name or not name.strip():
            raise InvalidProductDataError("Nombre inválido")
        if price <= 0:
            raise InvalidProductDataError("Precio inválido")
        if stock < 0:
            raise InvalidProductDataError("Stock inválido")
