"""Add qunatity column to product table

Revision ID: aeb10c7352f3
Revises: bc7f4128fc3a
Create Date: 2024-12-01 01:58:19.680747

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aeb10c7352f3"
down_revision: Union[str, None] = "bc7f4128fc3a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "product",
        sa.Column(
            "quantity", sa.Integer(), server_default="0", nullable=False
        ),
    )
    op.create_check_constraint(
        "check_quantity_nonnegative", "product", condition="quantity >= 0"
    )


def downgrade() -> None:
    op.drop_constraint("check_quantity_nonnegative", "product", type_="check")
    op.drop_column("product", "quantity")
