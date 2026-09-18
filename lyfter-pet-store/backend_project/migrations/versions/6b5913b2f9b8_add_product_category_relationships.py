"""add product category relationships

Revision ID: 6b5913b2f9b8
Revises: 088e4ea16430
Create Date: 2026-09-16 22:24:18.894762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b5913b2f9b8'
down_revision: Union[str, Sequence[str], None] = '088e4ea16430'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  """Upgrade schema."""

  op.execute(
    """
    INSERT INTO pets_eccomerce.product_categories (product_id, category_id)
    VALUES
        (1, 8),
        (2, 9),
        (3, 8),
        (4, 8),
        (4, 9),
        (5, 9),
        (6, 8),
        (6, 9),
        (7, 8),
        (8, 4),
        (9, 4),
        (10, 8),
        (11, 4),
        (12, 8),
        (13, 8),
        (14, 4),
        (15, 8),
        (15, 9),
        (15, 4),
        (26, 8);
    """
  )


def downgrade() -> None:
    """Downgrade schema."""
    pass
