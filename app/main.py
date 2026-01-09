from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
)

app.include_router(api_router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
