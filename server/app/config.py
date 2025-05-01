from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class NarattaConfig(BaseSettings):
    """Global App Configuration"""

    # DATABASE
    database_url: str = Field(default="", description="Postgres Database URL")

    # LOAD CONFIG THROUGH ENV FILE
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache(maxsize=1)
def get_config() -> NarattaConfig:
    return NarattaConfig()
