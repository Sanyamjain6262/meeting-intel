import os
from collections.abc import AsyncIterator

import pytest
from dotenv import dotenv_values
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from app.config import Settings
from app.main import create_app

# Nothing listens on port 1, so connections are refused immediately.
UNREACHABLE_DATABASE_URL = "postgresql+asyncpg://nobody:nothing@127.0.0.1:1/none"


@pytest.fixture(scope="session")
def test_database_url() -> str:
    url = os.environ.get("TEST_DATABASE_URL") or dotenv_values(".env").get("TEST_DATABASE_URL")
    if not url:
        pytest.fail("TEST_DATABASE_URL is not set in the environment or in backend/.env")
    return url


async def _client_for(app: FastAPI) -> AsyncIterator[AsyncClient]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
    await app.state.engine.dispose()


@pytest.fixture
async def client(test_database_url: str) -> AsyncIterator[AsyncClient]:
    """Client for an app connected to the test database."""
    app = create_app(Settings(database_url=test_database_url, secret_key="test-secret"))
    async for c in _client_for(app):
        yield c


@pytest.fixture
async def client_without_db() -> AsyncIterator[AsyncClient]:
    """Client for an app whose database cannot be reached."""
    app = create_app(Settings(database_url=UNREACHABLE_DATABASE_URL, secret_key="test-secret"))
    async for c in _client_for(app):
        yield c
