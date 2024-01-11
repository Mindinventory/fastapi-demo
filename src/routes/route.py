from fastapi import APIRouter

from src.routes import v1

router = APIRouter()

router.include_router(v1.router, prefix="/api")