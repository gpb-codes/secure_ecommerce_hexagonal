from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: Decimal
    active: bool = True

    def __post_init__(self):
        if not self.id:
            raise ValueError("id requerido")
        if not self.name:
            raise ValueError("name requerido")
        if self.price <= 0:
            raise ValueError("price debe ser mayor a 0")

    def deactivate(self) -> "Product":
        if not self.active:
            raise ValueError("producto ya inactivo")
        return Product(
            id=self.id,
            name=self.name,
            price=self.price,
            active=False,
        )
