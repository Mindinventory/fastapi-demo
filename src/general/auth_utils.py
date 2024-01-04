from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt, JWTError
from sqlalchemy.orm import Session

# from src.api.v1.user_authentication.models.user_models import User
# from src.api.v1.user_authentication.schemas.user_schemas import UserResponseSchema, RoleChoices
from ..api.v1.auth import crud
from ..general.constant import scopes_list
from ..db.session import get_db
from config.config import JWTSettings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
    scopes={
        "patient": "For patients",
        "staff": "For staff members",
        "owner": "For owner",
        "admin": "For admin"
    }
)

secret_key = JWTSettings().AUTH_SECRET_KEY
algorithm = JWTSettings().JWT_ALGORITHM


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        user: str = payload.get("username")
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    if payload.get("scopes") not in scopes_list:
        raise credentials_exception
    
    user = crud.get_user(db=db, username=payload.get("username"))
    if user is None:
        raise credentials_exception
    return payload
