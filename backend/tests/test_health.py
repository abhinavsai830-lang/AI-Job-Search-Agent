import os

# The health endpoint does not need PostgreSQL. Using SQLite here keeps this unit
# test runnable even when the developer has not started the external database yet.
os.environ.setdefault("DATABASE_URL", "sqlite:///./health_test.db")

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
