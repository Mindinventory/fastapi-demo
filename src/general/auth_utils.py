from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt, JWTError
from sqlalchemy.orm import Session

# from src.api.v1.user_authentication.models.user_models import User
# from src.api.v1.user_authentication.schemas.user_schemas import UserResponseSchema, RoleChoices
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


# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, secret_key, algorithms=[algorithm])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = User.get_user_by_username(db_session=db, user_name=username)
#     if user is None:
#         raise credentials_exception
#     return user


def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    # if security_scopes.scopes:
    #     authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    # else:
    #     authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    raw_token = token
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        print(payload)
        payload["token"] = raw_token
        user: str = payload.get("email")
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    tokenScopes = payload.get("scopes")
    if len(security_scopes.scopes) > 1:
        if tokenScopes[0] not in security_scopes.scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Incorrect scopes, need the following scope: "
                       + security_scopes.scope_str,
                headers={"WWW-Authenticate": authenticate_value},
            )
    else:
        for scope in security_scopes.scopes:
            if scope not in tokenScopes:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Incorrect scopes, need the following scope: "
                           + security_scopes.scope_str,
                    headers={"WWW-Authenticate": authenticate_value},
                )

    return payload

