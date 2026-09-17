"""migrate product category relationships

Revision ID: 088e4ea16430
Revises: c2ee67cad3cb
Create Date: 2026-09-16 22:16:15.845322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '088e4ea16430'
down_revision: Union[str, Sequence[str], None] = 'c2ee67cad3cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  """Upgrade schema."""
  op.execute(
        """
        INSERT INTO pets_eccomerce.product_categories (product_id, category_id)
        SELECT id, category_id
        FROM pets_eccomerce.products
        WHERE category_id IS NOT NULL;
        """

  
  )


def downgrade() -> None:
    """Downgrade schema."""
    pass
