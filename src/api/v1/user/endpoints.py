from fastapi import APIRouter

from config.logger import logger

router = APIRouter()


@router.get("")
def get_user_details():
    logger.info("Success")
    return "Sucess"