from itertools import product

import pytest
import pytest_asyncio

from core.models import Category, Product
from tests.api_v1.config_tests import TestSessionLocal, async_client
from tests.api_v1.config_tests import initialize_database


PRODUCTS_URL = "/api/v1/products/"


@pytest_asyncio.fixture(scope="session", autouse=True)
async def sample_category() -> Category:
    category = Category(name="Category for product")
    async with TestSessionLocal() as session:
        session.add(category)
        await session.commit()
        await session.refresh(category)

    return category


@pytest_asyncio.fixture(scope="session")
async def sample_product(sample_category) -> Product:
    product = Product(
        name="Product 1",
        price=1,
        quantity=1,
        category_id=sample_category.id,
    )
    async with TestSessionLocal() as session:
        session.add(product)
        await session.commit()
        await session.refresh(product)

    return product


@pytest.mark.asyncio
async def test_create_product(async_client, sample_category: Category) -> None:
    product_data = {
        "name": "Test",
        "description": "Some test",
        "price": 0,
        "quantity": 0,
        "category_id": sample_category.id,
    }
    response = await async_client.post(PRODUCTS_URL, json=product_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == product_data["name"]
    assert data["description"] == product_data["description"]
    assert data["price"] == product_data["price"]
    assert data["quantity"] == product_data["quantity"]
    assert data["category_id"] == product_data["category_id"]


@pytest.mark.asyncio
async def test_create_product_with_negative_price(
    async_client,
    sample_category: Category,
) -> None:
    product_data = {
        "name": "Test",
        "price": -1,
        "quantity": 0,
        "category_id": sample_category.id,
    }
    response = await async_client.post(PRODUCTS_URL, json=product_data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_product_with_negative_quantity(
    async_client,
    sample_category: Category,
) -> None:
    product_data = {
        "name": "Test",
        "price": 0,
        "quantity": -1,
        "category_id": sample_category.id,
    }
    response = await async_client.post(PRODUCTS_URL, json=product_data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_single_product(async_client, sample_product: Product) -> None:
    async with TestSessionLocal() as session:
        product_from_db = await session.get(Product, sample_product.id)

    response = await async_client.get(f"{PRODUCTS_URL}{sample_product.id}/")
    assert response.status_code == 200
    product = response.json()
    assert product_from_db.id == product["id"]
    assert product_from_db.name == product["name"]
    assert product_from_db.description == product["description"]
    assert product_from_db.price == product["price"]
    assert product_from_db.quantity == product["quantity"]
    assert product_from_db.category_id == product["category_id"]


@pytest.mark.asyncio
async def test_get_single_non_existing_product(async_client) -> None:
    response = await async_client.get(f"{PRODUCTS_URL}999/")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Product 999 not found!"
