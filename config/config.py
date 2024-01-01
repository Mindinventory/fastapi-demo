from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    DEBUG: bool = False
    HOST: str
    PORT: int

    class Config:
        env_file = './.env'
        env_file_encoding = 'utf-8'


settings = Settings()