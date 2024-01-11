from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from config.logger import logger
from src.api.v1.staff import schema, crud
from src.db.session import get_db
from src.general.constant import STAFF
from src.general.auth_utils import get_current_user
from src.general.response import success_response, error_response, get_message


router = APIRouter()


@router.get("/{staff_id}")
def get_staff_details(staff_id: str, db: Session = Depends(get_db),
                      user: dict = Security(get_current_user, scopes=[STAFF])):
    """
    Get staff details
    """
    try: 
        staff = crud.get_staff_details(db=db, staff_id=staff_id)        
        staff_data = schema.StaffDetails(**staff._mapping)
        return success_response(staff_data, "Staff details retrieved successfullly")
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
    