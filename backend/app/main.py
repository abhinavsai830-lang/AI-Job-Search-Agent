from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.jobs import router as jobs_router
from app.core.config import get_settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Agentic job discovery and candidate-job intelligence platform.",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(jobs_router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "AI Job Intelligence API is running",
        "version": "0.1.0",
    }
