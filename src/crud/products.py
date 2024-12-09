from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product
from core.schemas.product import ProductCreateUpdate
from crud.validators import validate_category_exists


async def create_product(
    session: AsyncSession,
    product_create: ProductCreateUpdate,
) -> Product:
    await validate_category_exists(category_id=product_create.category_id, session=session)

    product = Product(**product_create.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def get_product(
    session: AsyncSession,
    product_id: int
) -> Product | None:
    return await session.get(Product, product_id)


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductCreateUpdate,
) -> Product:
    for attr, value in product_update.model_dump().items():
        setattr(product, attr, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
