from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from uuid import uuid4

from ....db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), unique=True, nullable=False)
    username = Column(String(60), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    profile_picture = Column(String(100))
    is_patient = Column(Boolean, server_default='0', nullable=False)
    is_staff = Column(Boolean, server_default='0', nullable=False)
    is_owner = Column(Boolean, server_default='0', nullable=False)
    is_admin = Column(Boolean, server_default='0', nullable=False)
    is_mobile_verified = Column(Boolean(), server_default='0', nullable=False)
    is_policy_accepted = Column(Boolean(), server_default='0', nullable=False)
    is_password_updated = Column(Boolean(), server_default='0', nullable=False)
    is_email_verified = Column(Boolean(), server_default='0',nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    user_profile = relationship("UserProfile", back_populates="user")


class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), unique=True, nullable=False)
    user_id = Column(String(40), ForeignKey("users.id"), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50))
    last_name = Column(String(50), nullable=False)
    mobile_number = Column(String(15))
    home_number = Column(String(15))
    address = Column(String(255))
    city = Column(String(30))
    state = Column(String(15))
    country = Column(String(55))
    postal_code = Column(String(10))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    user = relationship("User", back_populates="user_profile")