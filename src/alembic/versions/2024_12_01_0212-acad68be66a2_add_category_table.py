"""Add category table

Revision ID: acad68be66a2
Revises: aeb10c7352f3
Create Date: 2024-12-01 02:12:35.189078

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "acad68be66a2"
down_revision: Union[str, None] = "aeb10c7352f3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=63), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_category")),
        sa.UniqueConstraint("name", name=op.f("uq_category_name")),
    )


def downgrade() -> None:
    op.drop_table("category")
