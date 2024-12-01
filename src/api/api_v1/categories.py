from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from unicodedata import category

from core.models import db_helper, Category
from core.schemas.category import CategoryRead, CategoryCreateUpdate
from crud.dependecies import get_category_by_id
from crud import categories as crud


router = APIRouter(tags=["Categories"])


@router.get("/", response_model=list[CategoryRead])
async def get_categories(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await crud.get_categories(session=session)


@router.post(
    "/",
    response_model=CategoryRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    category_create: CategoryCreateUpdate,
) -> Category:
    category = await crud.create_category(
        session=session,
        category_create=category_create,
    )
    return category


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    category: Annotated[Category, Depends(get_category_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> None:
    await crud.delete_category(session=session, category=category)
