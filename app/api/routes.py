from fastapi import APIRouter, Depends
from app.api.dependencies import get_product_repository
from app.application.use_cases.product_use_cases import ListProductsUseCase

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
def list_products(repository=Depends(get_product_repository)):
    use_case = ListProductsUseCase(repository)
    return use_case.execute()
