from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product
from core.schemas.product import ProductCreateUpdate
from core.validators import validate_category_exists


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
