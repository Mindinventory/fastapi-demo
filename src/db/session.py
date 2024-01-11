from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import DatabaseURLSettings

engine = create_engine(DatabaseURLSettings().SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        db.close()
