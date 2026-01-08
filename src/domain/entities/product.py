
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Product:
    id: UUID
    name: str
    price: float
    stock: int
    is_active: bool = True

    @staticmethod
    def create(name: str, price: float, stock: int) -> "Product":
        if not name or len(name.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")

        if len(name) > 100:
            raise ValueError("El nombre es demasiado largo")

        if price <= 0:
            raise ValueError("El precio debe ser mayor que 0")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        return Product(
            id=uuid4(),
            name=name,
            price=price,
            stock=stock,
        )
