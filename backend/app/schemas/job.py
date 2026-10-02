from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class JobCreate(BaseModel):
    external_id: str | None = Field(default=None, max_length=255)
    title: str = Field(min_length=1, max_length=255)
    company: str = Field(min_length=1, max_length=255)
    location: str | None = Field(default=None, max_length=255)
    description: str = Field(min_length=1)
    source: str = Field(min_length=1, max_length=100)
    source_url: str | None = None
    posted_at: datetime | None = None


class JobRead(JobCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
