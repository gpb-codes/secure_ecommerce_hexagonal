from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):
    id: str 
    name: str
    price: Decimal


class ProductResponse(BaseModel):
    id: str
    name: str
    price: Decimal
    active: bool