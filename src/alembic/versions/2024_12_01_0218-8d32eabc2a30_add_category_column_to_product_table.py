"""Add category column to product table

Revision ID: 8d32eabc2a30
Revises: acad68be66a2
Create Date: 2024-12-01 02:18:26.468683

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8d32eabc2a30"
down_revision: Union[str, None] = "acad68be66a2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "product", sa.Column("category_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        op.f("fk_product_category_id_category"),
        "product",
        "category",
        ["category_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_product_category_id_category"), "product", type_="foreignkey"
    )
    op.drop_column("product", "category_id")
