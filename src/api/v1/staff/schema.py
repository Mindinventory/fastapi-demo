from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class CreateUser(BaseModel):
    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)
    username: str
    email: str = Field(max_length=60, pattern="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+")
    profile_picture: Optional[str] = None
    first_name : str
    middle_name : Optional[str] = None
    last_name : str
    mobile_number : str
    home_number : Optional[str] = None
    address : Optional[str] = None
    city : Optional[str] = None
    state : Optional[str] = None
    country : Optional[str] = None
    postal_code : Optional[str] = None


class StaffDetails(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="ignore")
    username: str
    first_name: str
