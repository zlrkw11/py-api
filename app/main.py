from fastapi import FastAPI
from app.routers.router import router as api_router
from app.handlers.errorHandlers import register_exception_handlers
from app.db.db import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="Py API",
    description="FastAPI scaffold v1 for microservices",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(api_router)
register_exception_handlers(app)


@app.get("/", tags=["system"], summary="Root")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/health", tags=["system"], summary="Check heath")
async def health() -> dict[str, str]:
    return {"status": "ok"}
