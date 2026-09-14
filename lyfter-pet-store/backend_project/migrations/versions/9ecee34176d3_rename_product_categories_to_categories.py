"""rename product_categories to categories

Revision ID: 9ecee34176d3
Revises: 6461302df5ed
Create Date: 2026-09-14 15:43:10.114328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ecee34176d3'
down_revision: Union[str, Sequence[str], None] = '6461302df5ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  """Upgrade schema."""
  op.rename_table("product_categories", "categories", schema="pets_eccomerce")


def downgrade() -> None:
    """Downgrade schema."""
    pass
