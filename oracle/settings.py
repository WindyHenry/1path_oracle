from typing import Optional

from pydantic import BaseSettings, Field, RedisDsn


class Settings(BaseSettings):
    openapi_url: Optional[str] = None
    redis_dsn: RedisDsn = Field(default='redis://localhost/0:6379', env='redis_url')


settings = Settings()
