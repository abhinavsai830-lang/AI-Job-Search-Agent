"""Normalization helpers for external job records."""

from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, Field, HttpUrl


class NormalizedJob(BaseModel):
    external_id: str | None = None
    title: str = Field(min_length=1)
    company: str = Field(min_length=1)
    location: str | None = None
    description: str = Field(min_length=1)
    source: str = Field(min_length=1)
    source_url: HttpUrl | None = None


def _clean_text(value: Any) -> str | None:
    if value is None:
        return None
    text = re.sub(r"\s+", " ", str(value)).strip()
    return text or None


def normalize_job(raw_job: dict[str, Any], *, source: str) -> NormalizedJob:
    """Convert a provider-specific dictionary into the internal job shape."""
    title = _clean_text(raw_job.get("title") or raw_job.get("job_title"))

    company_value = raw_job.get("company")
    if isinstance(company_value, dict):
        company_value = company_value.get("name") or company_value.get("company_name")

    company = _clean_text(
        company_value or raw_job.get("company_name")
    )

    description = _clean_text(
        raw_job.get("description")
        or raw_job.get("content")
        or raw_job.get("job_description")
    )

    location_value = raw_job.get("location")
    if isinstance(location_value, dict):
        location_value = (
            location_value.get("name")
            or location_value.get("location")
            or location_value.get("city")
        )
    location = _clean_text(location_value)

    if not title:
        raise ValueError("Job title is required for normalization.")
    if not company:
        raise ValueError("Company is required for normalization.")
    if not description:
        raise ValueError("Job description is required for normalization.")

    source_url = (
        raw_job.get("absolute_url")
        or raw_job.get("url")
        or raw_job.get("source_url")
    )

    return NormalizedJob(
        external_id=str(raw_job["id"]) if raw_job.get("id") is not None else None,
        title=title,
        company=company,
        location=location,
        description=description,
        source=source,
        source_url=source_url,
    )
