from fastapi import APIRouter, Depends
from uuid import UUID

from application.product_use_cases import (
    CreateProduct, GetProduct, ListProducts, UpdateProduct, DeleteProduct
)
from infrastructure.api.schemas import ProductCreate, ProductResponse
from infrastructure.api.dependencies import get_product_repository

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    repo=Depends(get_product_repository),
):
    return CreateProduct(repo).execute(**data.dict())


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: UUID, repo=Depends(get_product_repository)):
    return GetProduct(repo).execute(product_id)


@router.get("/", response_model=list[ProductResponse])
def list_products(repo=Depends(get_product_repository)):
    return ListProducts(repo).execute()
