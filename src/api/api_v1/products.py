from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Product
from core.schemas.product import ProductRead, ProductCreateUpdate
from crud import products as products_crud
from crud.dependecies import get_product_by_id

router = APIRouter(tags=["Products"])


@router.post(
    "/",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product_create: ProductCreateUpdate,
) -> Product:
    product = await products_crud.create_product(
        session=session,
        product_create=product_create,
    )
    return product


@router.get("/{product_id}/", response_model=ProductRead)
async def get_product(
    product: Annotated[Product, Depends(get_product_by_id)],
):
    return product
