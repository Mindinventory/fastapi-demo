from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='allow', env_file_encoding='utf-8')
    DEBUG: bool = False
    HOST: str
    PORT: int


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='allow', env_file_encoding='utf-8')
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int


class DatabaseURLSettings(DatabaseSettings):    
    SQLALCHEMY_DATABASE_URL: str = f"mysql+pymysql://{DatabaseSettings().DB_USER}:{DatabaseSettings().DB_PASSWORD}@{DatabaseSettings().DB_HOST}:{DatabaseSettings().DB_PORT}/{DatabaseSettings().DB_NAME}"
