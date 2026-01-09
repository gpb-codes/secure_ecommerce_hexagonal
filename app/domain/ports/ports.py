from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from domain.entities.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product) -> Product:
        ...

    @abstractmethod
    def get_by_id(self, product_id: UUID) -> Optional[Product]:
        ...

    @abstractmethod
    def list_all(self) -> List[Product]:
        ...

    @abstractmethod
    def delete(self, product_id: UUID) -> None:
        ...
