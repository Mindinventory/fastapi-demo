from fastapi import APIRouter

from ..api.v1.user.endpoints import router as user_router


router = APIRouter(prefix="/v1")

router.include_router(user_router, prefix="/user", tags=["User"])