from sqlalchemy.orm import Session
from uuid import uuid4

from ..auth.models import User, UserProfile
from . import schema
from ....general.helper import get_hash_password


def create_staff(db: Session, input_data: schema.CreateUser):
    
    password, raw_password = get_hash_password(input_data.first_name, input_data.mobile_number)
    
    staff = User(
        id=uuid4(), username=input_data.username, password=password, is_staff=True
    )
    db.add(staff)
    
    staff_profile = UserProfile(
        id=uuid4(), user_id=staff.id, email=input_data.email, first_name=input_data.first_name,
        middle_name=input_data.middle_name, last_name=input_data.last_name, mobile_number=input_data.mobile_number,
        home_number=input_data.home_number, address=input_data.address, city=input_data.city,
        state=input_data.state, country=input_data.country, postal_code=input_data.postal_code
    )
    db.add(staff_profile)
    db.commit()
    db.refresh(staff)
    return True


def get_staff_details(db: Session, staff_id: str):
    staff = db.query(
        UserProfile
    ).filter(
        UserProfile.user_id == staff_id
    )
    return staff.first()
