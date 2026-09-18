"""remove category_id column from products table

Revision ID: bfb98af9e58f
Revises: 6b5913b2f9b8
Create Date: 2026-09-18 14:24:42.538996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfb98af9e58f'
down_revision: Union[str, Sequence[str], None] = '6b5913b2f9b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  """Upgrade schema."""
  op.drop_column("products", "category_id", schema="pets_eccomerce")


def downgrade() -> None:
    """Downgrade schema."""
    pass
