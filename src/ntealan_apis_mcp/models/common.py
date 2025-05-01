from enum import Enum

from pydantic import BaseModel, Extra, Field, SecretStr
from pydantic_settings import SettingsConfigDict


class McpResourceResponse(BaseModel):
    status: str = Field(default_factory=str, description="Status of the response")
    client_id: bool | None = Field(default=None, description="Client identifier")
    request_id: str | None = Field(default=None, description="Request identifier")
    data: dict | str = Field(default={}, description="Response data")
    error_code: int | None = Field(default=None, description="Error code if any")
    error_message: str | None = Field(default=None, description="Error message if any")


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
        description="Base URL for the NTEALAN API",
    )
    api_key: SecretStr | None = Field(default=None, description="API key for authentication")
    api_secret: str = Field(
        default="your_api_secret_here",
        description="API secret for authentication",
    )
    api_version: str = Field(default="v1", description="API version")
    api_aiohttp_connect_timeout: int = Field(default=30, description="API timeout in seconds")
    api_aiohttp_connect_perhost: int = Field(default=10, description="API timeout in seconds")
    api_aiohttp_connect_total: int = Field(
        default=3, description="Number of retries for API requests"
    )
    api_aiohttp_retry_delay: int = Field(
        default=5,
        description="Delay between retries in seconds",
    )
    api_log_enable: bool = Field(default=False, description="Enable logging for API requests")
    api_log_level: str = Field(default="info", description="Log level for API requests")
