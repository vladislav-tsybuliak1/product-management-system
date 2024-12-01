from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


if TYPE_CHECKING:
    from core.models.product import Product


class Category(Base):
    name: Mapped[str] = mapped_column(String(63), nullable=False, unique=True)

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
    )
