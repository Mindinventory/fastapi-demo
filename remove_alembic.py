from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

from config.config import settings


database_url = f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
table_name_to_delete = "alembic_version"


def delete_table_from_database():
    # Create a SQLAlchemy engine
    engine = create_engine(database_url)
    Base = declarative_base()

    # Create a metadata object
    metadata = MetaData()

    # Reflect the existing database schema
    metadata.reflect(bind=engine)

    # # Get the table to delete
    table = metadata.tables[table_name_to_delete]

    # Drop the table
    if table is not None:
        Base.metadata.drop_all(engine, [table], checkfirst=True)

if __name__ == "__main__":
    delete_table_from_database()
