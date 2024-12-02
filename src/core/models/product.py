from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Text,
    func,
    Integer,
    DateTime,
    CheckConstraint,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import IntIdPkMixin


if TYPE_CHECKING:
    from core.models.category import Category


class Product(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    price: Mapped[int]
    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        server_default="0",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        server_default=func.now(),
    )
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products",
    )

    __table_args__ = (
        CheckConstraint("price >= 0", name="check_price_nonnegative"),
        CheckConstraint("quantity >= 0", name="check_quantity_nonnegative"),
    )
