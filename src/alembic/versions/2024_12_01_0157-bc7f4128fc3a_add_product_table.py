"""Add product table

Revision ID: bc7f4128fc3a
Revises: 
Create Date: 2024-12-01 01:57:15.528674

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bc7f4128fc3a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), server_default="", nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "price >= 0", name=op.f("ck_product_check_price_nonnegative")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_product")),
    )


def downgrade() -> None:
    op.drop_table("product")
