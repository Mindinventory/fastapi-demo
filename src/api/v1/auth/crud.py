from sqlalchemy.orm import Session

from src.api.v1.auth.models import User


def get_user(db: Session, username: str):
    user = db.query(
        User
    ).filter(
        User.username == username
    )
    return user.first()
