from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from ..api.v1.auth.models import User # noqa