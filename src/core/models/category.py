from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


if TYPE_CHECKING:
    from core.models.product import Product


class Category(Base):
    name: Mapped[str] = mapped_column(String(63), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
    )
