from pydantic import BaseModel
from uuid import UUID


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int


class ProductResponse(BaseModel):
    id: UUID
    name: str
    price: float
    stock: int
    is_active: bool

    class Config:
        from_attributes = True
