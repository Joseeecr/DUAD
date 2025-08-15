from sqlalchemy import insert, select, delete, update, Select
from sqlalchemy.engine import CursorResult, Row
from db.models import products_table
from repos.utils import with_connection
from typing import Optional

class ProductsRepository:
  def __init__(self, engine):
    self.engine = engine

  @with_connection
  def get_products(self, conn, stmt : Select) -> CursorResult:
    return conn.execute(stmt)


  @with_connection
  def get_product_by_id(self, conn, id : int) -> Optional[Row]:
    stmt = select(products_table).where(products_table.c.id == id)
    result = conn.execute(stmt).first()

    if result:
      return dict(result._mapping)
    return None


  @with_connection
  def insert_product(self, conn, data : dict) -> int:

    stmt = insert(products_table).values(**data).returning(products_table.c.id)
    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def update_product(self, conn, id : int, data : dict) -> int:

    stmt = (
      update(products_table).returning(products_table.c.id)
      .where(products_table.c.id == id)
      .values(**data)
    )

    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def delete_product(self, conn, id : int) -> int:

    stmt = delete(products_table).where(products_table.c.id == id)
    result = conn.execute(stmt)
    conn.commit()
    return result.rowcount