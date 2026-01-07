from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Secure Ecommerce API")
app.include_router(router)