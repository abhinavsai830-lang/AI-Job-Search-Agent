import pytest

from app.services.job_normalization import normalize_job


def test_normalize_common_job_payload() -> None:
    job = normalize_job(
        {
            "id": 101,
            "title": "  AI   Engineer ",
            "company": {"name": "Example AI"},
            "location": {"name": "Hyderabad"},
            "content": "  Build RAG systems.  ",
            "absolute_url": "https://example.com/jobs/101",
        },
        source="greenhouse",
    )

    assert job.external_id == "101"
    assert job.title == "AI Engineer"
    assert job.company == "Example AI"
    assert job.location == "Hyderabad"
    assert job.description == "Build RAG systems."
    assert str(job.source_url) == "https://example.com/jobs/101"


def test_normalize_rejects_missing_description() -> None:
    with pytest.raises(ValueError, match="description"):
        normalize_job(
            {
                "id": 102,
                "title": "AI Engineer",
                "company": "Example AI",
                "location": "Hyderabad",
            },
            source="manual",
        )
