from typing import Annotated

from fastapi import HTTPException, status
from fastapi.params import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Category, Product
from crud import categories as categories_crud, products as products_crud


async def get_category_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    category_id: Annotated[int, Path],
) -> Category:
    category = await categories_crud.get_category(
        session=session,
        category_id=category_id,
    )
    if category:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category {category_id} not found!",
    )


async def get_product_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product_id: Annotated[int, Path],
) -> Product:
    product = await products_crud.get_product(
        session=session,
        product_id=product_id,
    )
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!",
    )
