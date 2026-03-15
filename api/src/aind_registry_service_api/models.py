
from typing import Literal

from pydantic import BaseModel

from aind_registry_service_api import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__
