"""add new product categories

Revision ID: 195dd04fa210
Revises: 9ecee34176d3
Create Date: 2026-09-16 19:59:08.483731

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '195dd04fa210'
down_revision: Union[str, Sequence[str], None] = '9ecee34176d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  """Upgrade schema."""
  categories_table = sa.table("categories", sa.column("name", sa.String), schema="pets_eccomerce")

  op.bulk_insert(
    categories_table,
    [
        {"name": "perros"},
        {"name": "gatos"},
        {"name": "accesorios"},
    ]
  )



def downgrade() -> None:
  """Downgrade schema."""
  op.execute(
    """
    DELETE FROM pets_eccomerce.categories
    WHERE name IN ('perros', 'gatos', 'accesorios')
    """
  )