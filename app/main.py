from fastapi import FastAPI
from app.api.routes import router
from app.infrastructure.db.init_db import init_db

app = FastAPI(title="Secure Ecommerce API")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router)

@app.get("/health", tags=["health"])
def health():
    return {
        "service": "secure-ecommerce",
        "status": "up"
    }
