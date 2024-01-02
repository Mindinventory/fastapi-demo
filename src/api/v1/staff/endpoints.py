from fastapi import APIRouter, Security, Request, Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from . import schema
from . import crud
from config.logger import logger
from ....db.session import get_db
from ....general.response import success_response, error_response, get_message


router = APIRouter()


@router.get("/{staff_id}")
def get_staff_details(staff_id: str, db: Session = Depends(get_db)):
    """
    Get staff details
    """
    try:
        staff = crud.get_staff_details(db=db, staff_id=staff_id)
        return success_response(staff, "Staff details retrieved successfullly")
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)
    

@router.post("")
def create_staff(
    input_data: schema.CreateUser, db: Session = Depends(get_db)
    ):
    """
    Create staff
    """
    try:
        crud.create_staff(db=db, input_data=input_data)
        return success_response(None, "Staff created successfully")
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)
    