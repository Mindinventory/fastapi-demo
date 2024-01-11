from fastapi import APIRouter

from src.api.v1.staff.endpoints import router as staff_router
from src.api.v1.auth.endpoints import router as auth_router


router = APIRouter(prefix="/v1")

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(staff_router, prefix="/staff", tags=["Staff"])