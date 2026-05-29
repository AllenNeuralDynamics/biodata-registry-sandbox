from pydantic import BaseModel, Field
from fastapi_filter.contrib.sqlalchemy import Filter
from datetime import datetime

class Page(BaseModel):
    next_token: str | None = Field(default=None)
    has_more: bool = Field(default=False)

class PageFilter(Filter):
    # next_token: str | None = Field(default=None)
    # limit: int = Field(default=10, le=100, ge=1)
    created_at__gt: datetime | None = Field(default=None)
    created_at__lt: datetime | None = Field(default=None)
    created_at__gte: datetime | None = Field(default=None)
    created_at__lte: datetime | None = Field(default=None)
    updated_at__gt: datetime | None = Field(default=None)
    updated_at__lt: datetime | None = Field(default=None)
    updated_at__gte: datetime | None = Field(default=None)
    updated_at__lte: datetime | None = Field(default=None)
