from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.api import health
from app.config import Settings, get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await app.state.engine.dispose()


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()

    app = FastAPI(title="Meeting Intel", lifespan=lifespan)
    app.state.settings = settings
    # The engine connects lazily, so the app starts even if Postgres is down.
    app.state.engine = create_async_engine(settings.database_url, pool_pre_ping=True)
    app.state.session_factory = async_sessionmaker(app.state.engine, expire_on_commit=False)

    app.include_router(health.router)
    return app
