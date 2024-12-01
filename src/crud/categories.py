from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category
from core.schemas.category import CategoryCreateUpdate
from core.validators import validate_category_unique_name


async def create_category(
    session: AsyncSession,
    category_create: CategoryCreateUpdate,
) -> Category:
    await validate_category_unique_name(
        category_name=category_create.name,
        session=session,
    )

    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category


async def get_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)
