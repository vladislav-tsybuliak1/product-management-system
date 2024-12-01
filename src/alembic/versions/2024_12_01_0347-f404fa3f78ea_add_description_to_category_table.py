"""Add description to category table

Revision ID: f404fa3f78ea
Revises: 8d32eabc2a30
Create Date: 2024-12-01 03:47:21.202656

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f404fa3f78ea"
down_revision: Union[str, None] = "8d32eabc2a30"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "category",
        sa.Column("description", sa.Text(), server_default="", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("category", "description")
