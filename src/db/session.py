from contextlib import contextmanager

@contextmanager
def SqlAlchemyUnitOfWork():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from config.config import settings

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=100, max_overflow=200, pool_recycle=300)

    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = Session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        db.close()
