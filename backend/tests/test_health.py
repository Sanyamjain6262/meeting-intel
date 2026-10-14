from httpx import AsyncClient


async def test_health_ok(client_without_db: AsyncClient) -> None:
    response = await client_without_db.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


async def test_health_db_ok(client: AsyncClient) -> None:
    response = await client.get("/health/db")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


async def test_health_db_unavailable(client_without_db: AsyncClient) -> None:
    response = await client_without_db.get("/health/db")

    assert response.status_code == 503
    assert response.json() == {"status": "unavailable"}

    # The app keeps serving after a database failure.
    assert (await client_without_db.get("/health")).status_code == 200
