from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.schemas import ProductCreate, ProductResponse
from app.api.dependencies import get_product_repository
from app.application.use_cases.product_use_cases import (
    CreateProductUseCase,
    GetProductUseCase,
)
from app.domain.ports.exceptions import ProductNotFound

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    repository=Depends(get_product_repository),
):
    use_case = CreateProductUseCase(repository)
    product = use_case.execute(
        product_id=data.id,
        name=data.name,
        price=data.price,
    )
    return product


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: str,
    repository=Depends(get_product_repository),
):
    use_case = GetProductUseCase(repository)
    try:
        product = use_case.execute(product_id)
        return product
    except ProductNotFound:
        raise HTTPException(status_code=404, detail="Product not found")
