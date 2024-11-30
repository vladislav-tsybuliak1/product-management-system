from datetime import datetime

from sqlalchemy import String, Text, func, Integer, DateTime, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Product(Base):
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    price: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        default=datetime.now(),
    )

    __table_args__ = (
        CheckConstraint("price >= 0", name="check_price_nonnegative"),
    )
