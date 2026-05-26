from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from typing import Optional
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import TIMESTAMP

def get_utc_now():
    return datetime.now(timezone.utc)

class BaseTable(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column_kwargs={"server_default": func.now()},
        sa_type = TIMESTAMP(timezone=True),
    )
    created_by: int | None = Field(default=None, foreign_key="users.id")
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
        sa_type=TIMESTAMP(timezone=True),
    )
    last_updated_by: int | None = Field(default=None, foreign_key="users.id")
