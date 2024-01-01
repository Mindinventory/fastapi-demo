from fastapi import APIRouter

from ..api.v1.staff.endpoints import router as user_router


router = APIRouter(prefix="/v1")

router.include_router(user_router, prefix="/user", tags=["User"])