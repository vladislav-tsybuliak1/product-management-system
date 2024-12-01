from fastapi import APIRouter

from core.config import settings
from api.api_v1.products import router as products_router
from api.api_v1.categories import router as categories_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    products_router,
    prefix=settings.api.v1.products,
)
router.include_router(
    categories_router,
    prefix=settings.api.v1.categories,
)
