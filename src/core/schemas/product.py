from datetime import datetime
from typing import Annotated

from annotated_types import MaxLen, Ge
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: Annotated[str, MaxLen(255)]
    description: str | None = None
    price: Annotated[int, Ge(0)]
    quantity: Annotated[int | None, Ge(0)]
    category_id: int


class ProductCreateUpdate(ProductBase):
    pass


class ProductRead(ProductBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    created_at: datetime
