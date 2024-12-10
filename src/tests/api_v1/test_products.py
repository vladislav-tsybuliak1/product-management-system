import pytest
import pytest_asyncio

from core.models import Category
from tests.api_v1.config_tests import TestSessionLocal, async_client
from tests.api_v1.config_tests import initialize_database


PRODUCTS_URL = "/api/v1/products/"
PRODUCT_ID = 1


@pytest_asyncio.fixture(scope="session", autouse=True)
async def category() -> Category:
    category = Category(name="Category for product")
    async with TestSessionLocal() as session:
        session.add(category)
        await session.commit()
        await session.refresh(category)

    return category


@pytest.mark.asyncio
async def test_create_product(async_client, category: Category) -> None:
    product_data = {
        "name": "Test",
        "description": "Some test",
        "price": 0,
        "quantity": 0,
        "category_id": category.id,
    }
    response = await async_client.post(PRODUCTS_URL, json=product_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == product_data["name"]
    assert data["description"] == product_data["description"]
    assert data["price"] == product_data["price"]
    assert data["quantity"] == product_data["quantity"]
    assert data["category_id"] == product_data["category_id"]
