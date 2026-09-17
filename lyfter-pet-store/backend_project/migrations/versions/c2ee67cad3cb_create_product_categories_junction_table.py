"""create product categories junction table

Revision ID: c2ee67cad3cb
Revises: 195dd04fa210
Create Date: 2026-09-16 20:52:14.915357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c2ee67cad3cb'
down_revision: Union[str, Sequence[str], None] = '195dd04fa210'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  """Upgrade schema."""
  op.create_table(
    "product_categories",
    sa.Column("id", sa.Integer(), primary_key=True),
    sa.Column("product_id", sa.Integer(), sa.ForeignKey("pets_eccomerce.products.id"), nullable=False),
    sa.Column("category_id", sa.Integer(), sa.ForeignKey("pets_eccomerce.categories.id"), nullable=False),
    schema='pets_eccomerce'
  )


def downgrade() -> None:
    """Downgrade schema."""
    pass
