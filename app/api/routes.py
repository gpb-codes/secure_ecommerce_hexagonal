from fastapi import APIRouter
from app.services.product_service import ProductService

router = APIRouter(prefix="/api")

@router.get("/products")
def list_products():
    return ProductService().list_products()