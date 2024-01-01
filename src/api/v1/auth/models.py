from ....db.base import Base
from sqlalchemy import Column, Integer, String, JSON


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    # username = Column(String, unique=True)
    # email = Column(String)
    # first_name = Column(String)
    # last_name = Column(String)