from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

# from . import schema
from . import crud
from config.logger import logger
from ....db.session import get_db
from ....general.constant import *
from ....general.hash_utils import Hasher
from ....general.token_utils import Token
from ....general.response import success_response, error_response, get_message


router = APIRouter()


@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login a user. Only select a single scope, options are "patient", "staff", "owner"
    """
    try:
        req_scopes = user.scopes
        if len(req_scopes) > 1:
            logger.info("More than one scope selected")
            return error_response(get_message("auth_login", "scope_greater"))
        if len(req_scopes) < 1:
            logger.info("No scope selected")
            return error_response(get_message("auth_login", "scope_lesser"))

        # Check validation for scope
        if req_scopes[0] not in (PATIENT, STAFF, OWNER, ADMIN):
            logger.info("Invalid scope selected")
            return error_response(get_message("auth_login", "invalid_scope"))


        dbUser = crud.get_user(db, user.username)

        if not dbUser:
            return error_response(get_message("auth_login", "invalid_credential"), 401)
        
        # check the password is correct or not
        if not Hasher().verify_password(user.password, dbUser.password):
            return error_response(get_message("auth_login", "invalid_credential"), 401)

        data = {
            "scopes": req_scopes,
            "ID": dbUser.id,
            "email": dbUser.username
        }

        jwt_token = Token().create_access_token(data)

        login_data = dbUser
        return {
            "user": login_data,
            "access_token": jwt_token,
            "token_type": "bearer"
        }
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)