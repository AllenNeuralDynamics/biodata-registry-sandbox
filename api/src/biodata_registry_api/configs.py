"""Module for settings to connect to Postgres backend"""

from urllib.parse import quote_plus

from aind_settings_utils.aws import SecretsManagerBaseSettings
from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict
from typing import Optional


class Settings(SecretsManagerBaseSettings):
    """Settings needed to connect to Registry Database"""

    # noinspection SpellCheckingInspection
    model_config = SettingsConfigDict(env_prefix="REGISTRY_")
    host: str = Field(
        ...,
        title="Server",
        description="Host address of the Postgres Server.",
    )
    port: int = Field(
        ..., title="Port", description="Port number of the Postgres Server"
    )
    database: str = Field(
        ..., title="Database", description="Name of the database."
    )
    user: str = Field(..., title="User", description="User")
    password: SecretStr = Field(..., title="Password", description="Password")
    ssl_cert: Optional[str] = Field(default=None)

    @property
    def db_connection_str(self):
        """Compute the connection string from other settings"""
        encoded_password = quote_plus(self.password.get_secret_value())
        return (
            f"postgresql+asyncpg://{self.user}:{encoded_password}@"
            f"{self.host}:{self.port}/{self.database}"
        )
