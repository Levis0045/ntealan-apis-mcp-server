from enum import Enum

from pydantic import BaseModel, Extra, Field, SecretStr
from pydantic_settings import SettingsConfigDict


class McpResourceResponse(BaseModel):
    status: str = Field(default_factory=str)
    client_id: bool | None = Field(default=None)
    request_id: str | None = Field(default=None)
    data: dict | str = Field(default={})
    error_code: int | None = Field(default=None)
    error_message: str | None = Field(default=None)


class HttpResourceAllowMedodsEnum(str, Enum):
    GET = "GET"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class HttpToolAllowMedodsEnum(str, Enum):
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class ConfigModel(BaseModel, extra=Extra.forbid):
    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        env_nested_delimiter="__",
        env_prefix="NTEALAN_",
        # env_file=,
        env_file_encoding="utf-8",
        # case_sensitive=True,
    )
    base_api_url: str = Field(
        default="https://apis.ntealan.net/ntealan/",
        env="NTEALAN_BASE_API_URL",
        description="Base URL for the NTEALAN API",
    )
    api_key: SecretStr | None = Field(
        default=None, env="NTEALAN_API_KEY", description="API key for authentication"
    )
    api_secret: str = Field(
        default="your_api_secret_here",
        env="NTEALAN_API_SECRET",
        description="API secret for authentication",
    )
    api_version: str = Field(default="v1", env="NTEALAN_API_VERSION", description="API version")
    api_aiohttp_connect_timeout: int = Field(
        default=30, env="NTEALAN_API_AIOHTTP_TIMEOUT", description="API timeout in seconds"
    )
    api_aiohttp_connect_perhost: int = Field(
        default=10, env="NTEALAN_API_AIOHTTP_PERHOST", description="API timeout in seconds"
    )
    api_aiohttp_connect_total: int = Field(
        default=3, env="NTEALAN_API_AIOHTTP_TOTAL", description="Number of retries for API requests"
    )
    api_aiohttp_retry_delay: int = Field(
        default=5,
        env="NTEALAN_API_AIOHTTP_RETRY_DELAY",
        description="Delay between retries in seconds",
    )
    api_log_enable: bool = Field(
        default=False, env="NTEALAN_API_LOG_ENABLE", description="Enable logging for API requests"
    )
    api_log_level: str = Field(
        default="info", env="NTEALAN_API_LOG_LEVEL", description="Log level for API requests"
    )
