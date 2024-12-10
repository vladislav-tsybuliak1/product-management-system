import pytest
import pytest_asyncio
from sqlalchemy import Result, select

from core.models import Category
from tests.api_v1.config_tests import TestSessionLocal, async_client
from tests.api_v1.config_tests import initialize_database


CATEGORIES_URL = "/api/v1/categories/"
CATEGORY_ID = 1


@pytest_asyncio.fixture(scope="session", autouse=True)
async def populate_db_with_categories() -> None:
    categories = [
        Category(name="Category 1"),
        Category(name="Category 2"),
        Category(name="Category 3"),
    ]
    async with TestSessionLocal() as session:
        session.add_all(categories)
        await session.commit()


@pytest.mark.asyncio
async def test_get_categories(async_client) -> None:
    stmt = select(Category).order_by(Category.id)
    async with TestSessionLocal() as session:
        result: Result = await session.execute(stmt)

    categories_from_db = result.scalars().all()
    response = await async_client.get(CATEGORIES_URL)
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
    response = await async_client.post(CATEGORIES_URL, json=category_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == category_data["name"]
    assert data["description"] == category_data["description"]


@pytest.mark.asyncio
async def test_create_category_with_not_unique_name(async_client) -> None:
    category_data_1 = {"name": "The same name"}
    response_1 = await async_client.post(CATEGORIES_URL, json=category_data_1)
    assert response_1.status_code == 201

    category_data_2 = {"name": "The same name"}
    response_2 = await async_client.post(CATEGORIES_URL, json=category_data_2)
    assert response_2.status_code == 400

    data = response_2.json()
    assert (
        data["detail"]
        == f"Category with name {category_data_1["name"]} already exists."
    )


@pytest.mark.asyncio
async def test_get_single_category(async_client) -> None:
    async with TestSessionLocal() as session:
        category_from_db = await session.get(Category, CATEGORY_ID)

    response = await async_client.get(f"{CATEGORIES_URL}{CATEGORY_ID}/")
    assert response.status_code == 200
    category = response.json()
    assert category_from_db.id == category["id"]
    assert category_from_db.name == category["name"]
    assert category_from_db.description == category["description"]


@pytest.mark.asyncio
async def test_get_single_non_existing_category(async_client) -> None:
    response = await async_client.get(f"{CATEGORIES_URL}999/")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Category 999 not found!"


@pytest.mark.asyncio
async def test_update_category(async_client) -> None:
    category_data = {"name": "Updated name", "description": "Updated description"}
    response = await async_client.put(f"{CATEGORIES_URL}{CATEGORY_ID}/", json=category_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == category_data["name"]
    assert data["description"] == category_data["description"]


@pytest.mark.asyncio
async def test_delete_category(async_client) -> None:
    category = Category(name="Category To Delete")
    async with TestSessionLocal() as session:
        session.add(category)
        await session.commit()
        await session.refresh(category)

    response = await async_client.delete(f"{CATEGORIES_URL}{category.id}/")
    assert response.status_code == 204

    async with TestSessionLocal() as session:
        category_from_db = await session.get(Category, category.id)

    assert category_from_db is None
