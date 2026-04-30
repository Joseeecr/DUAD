from sqlalchemy import insert, select, delete, update, Select
from sqlalchemy.engine import CursorResult, Row
from app.db.models import user_table
from app.repos.utils import with_connection
from typing import Optional

class UserRepository:
  def __init__(self, engine):
    self.engine = engine

  @with_connection
  def get_users(self, conn, stmt : Select) -> CursorResult:
    return conn.execute(stmt)


  @with_connection
  def get_user_by_email(self, conn, email : str) -> Optional[Row]:
    stmt = select(user_table).where(user_table.c.email == email)
    result = conn.execute(stmt).first()

    if result:
      return dict(result._mapping)
    return None


  @with_connection
  def get_user_by_id(self, conn, id : int) -> Optional[Row]:
    stmt = select(user_table).where(user_table.c.id == id)
    result = conn.execute(stmt).first()

    if result:
      return dict(result._mapping)
    return None


  @with_connection
  def insert_user(self, conn, data : dict) -> int:

    stmt = insert(user_table).values(**data).returning(user_table.c.id)
    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def update_user_by_admin(self, conn, id : int, data : dict) -> int:

    stmt = (
      update(user_table).returning(user_table.c.id)
      .where(user_table.c.id == id)
      .values(**data)
    )

    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def delete_user(self, conn, id : int) -> int:

    stmt = delete(user_table).where(user_table.c.id == id)
    result = conn.execute(stmt)
    conn.commit()
    return result.rowcount