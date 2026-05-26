from pydantic import BaseModel, Field
from fastapi_filter.contrib.sqlalchemy import Filter
from datetime import datetime

class Page(BaseModel):
    next_token: str | None
    has_more: bool

#     created_at: datetime = Field(
#         default_factory=lambda: datetime.now(timezone.utc),
#         nullable=False,
#         sa_column_kwargs={"server_default": func.now()},
#         sa_type = TIMESTAMP(timezone=True),
#     )
#     created_by: int | None = Field(default=None, foreign_key="users.id")
#     updated_at: datetime = Field(
#         default_factory=lambda: datetime.now(timezone.utc),
#         nullable=False,
#         sa_column_kwargs={"onupdate": func.now()},
#         sa_type=TIMESTAMP(timezone=True),
#     )
#     last_updated_by: int | None = Field(default=None, foreign_key="users.id")

class PageFilter(Filter):
    next_token: str | None = None
    limit: int = Field(default=10, le=100, ge=1)
    created_at__gt: datetime | None = None
    created_at__lt: datetime | None = None
    created_at__gte: datetime | None = None
    created_at__lte: datetime | None = None
    updated_at__gt: datetime | None = None
    updated_at__lt: datetime | None = None
    updated_at__gte: datetime | None = None
    updated_at__lte: datetime | None = None
