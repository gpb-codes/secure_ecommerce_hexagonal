from abc import ABC, abstractmethod
from typing import Optional
from .product import Product
from typing import List


class ProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        pass
    
    @abstractmethod
    def list_all(self) -> List[Product]:
        pass


    
