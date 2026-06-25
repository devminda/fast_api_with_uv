"""Tests for the items endpoint."""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.fixture
async def client() -> AsyncClient:  # type: ignore[misc]
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


async def test_create_and_get_item(client: AsyncClient) -> None:
    response = await client.post(
        "/api/v1/items/",
        json={"name": "test", "description": "a test item"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "test"
    item_id = data["id"]

    get_response = await client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "test"


async def test_get_missing_item(client: AsyncClient) -> None:
    response = await client.get("/api/v1/items/99999")
    assert response.status_code == 404
