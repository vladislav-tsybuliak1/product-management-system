import pytest
from sqlalchemy import Result, select

from core.models import Category
from tests.api_v1.config_tests import main_app, TestSessionLocal
from tests.api_v1.config_tests import initialize_database, async_client


@pytest.mark.asyncio
async def test_create_category(async_client) -> None:
    category_data = {"name": "Test Category", "description": "A test category"}
    response = await async_client.post("/api/v1/categories/", json=category_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == category_data["name"]
    assert data["description"] == category_data["description"]
