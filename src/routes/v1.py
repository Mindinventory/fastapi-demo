from fastapi import APIRouter

from ..api.v1.staff.endpoints import router as staff_router


router = APIRouter(prefix="/v1")

router.include_router(staff_router, prefix="/staff", tags=["Staff"])