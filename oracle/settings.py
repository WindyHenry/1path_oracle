from typing import Optional

from pydantic import BaseSettings, Field, RedisDsn


class Settings(BaseSettings):
    openapi_url: Optional[str] = None
    redis_dsn: RedisDsn = Field(default='redis://localhost:6379/0', env='redis_url')


settings = Settings()
