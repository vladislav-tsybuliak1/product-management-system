import pytest
import pytest_asyncio
from sqlalchemy import Result, select

from core.models import Category
from tests.api_v1.config_tests import main_app, TestSessionLocal
from tests.api_v1.config_tests import initialize_database, async_client


@pytest_asyncio.fixture(scope="session")
async def populate_db_with_categories():
    categories = [
        Category(name="Category 1"),
        Category(name="Category 2"),
        Category(name="Category 3"),
    ]
    session = TestSessionLocal()
    session.add_all(categories)
    await session.commit()


@pytest.mark.asyncio
async def test_get_categories(async_client, populate_db_with_categories) -> None:
    stmt = select(Category).order_by(Category.id)
    result: Result = await TestSessionLocal().execute(stmt)
    categories_from_db = result.scalars().all()

    response = await async_client.get("/api/v1/categories/")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories_from_db) == len(categories)

    for i in range(len(categories_from_db)):
        assert categories_from_db[i].id == categories[i]["id"]
        assert categories_from_db[i].name == categories[i]["name"]
        assert categories_from_db[i].description == categories[i]["description"]


@pytest.mark.asyncio
async def test_create_category(async_client) -> None:
    category_data = {"name": "Test Category", "description": "A test category"}
    response = await async_client.post("/api/v1/categories/", json=category_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == category_data["name"]
    assert data["description"] == category_data["description"]


@pytest.mark.asyncio
async def test_create_category_with_not_unique_name(async_client) -> None:
    category_data_1 = {"name": "The same name"}
    response_1 = await async_client.post("/api/v1/categories/", json=category_data_1)
    assert response_1.status_code == 201

    category_data_2 = {"name": "The same name"}
    response_2 = await async_client.post("/api/v1/categories/", json=category_data_2)
    assert response_2.status_code == 400

    data = response_2.json()
    assert data["detail"] == f"Category with name {category_data_1["name"]} already exists."
