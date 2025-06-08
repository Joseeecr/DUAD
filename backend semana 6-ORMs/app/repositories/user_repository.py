from sqlalchemy import insert, select, update, delete
from db.tables import users_table
from repositories.repository_utils import with_connection, is_valid_id
class UserRepository:
  def __init__(self, engine):
    self.engine = engine


  @with_connection
  def add_user(self, conn, full_name : str, email: str, phone_number: int) -> None:

    user_data = insert(users_table).values(
      full_name = full_name,
      email = email,
      phone_number = phone_number
    )
    conn.execute(user_data)
    conn.commit()


  @with_connection
  def get_user_by_id(self, conn,  _id: int) -> None:
    if not is_valid_id(conn, users_table, _id):
      return

    stmt = select(users_table).where(users_table.c.id == _id)

    for row in conn.execute(stmt): 
      print(row)


  @with_connection
  def get_all_users(self, conn) -> None:
    stmt = select(users_table)

    for row in conn.execute(stmt):
      print(row)


  @with_connection
  def update_user(self, conn, _id : int, data: dict) -> None:
    if not is_valid_id(conn, users_table, _id):
      return

    stmt = (
      update(users_table)
      .where(users_table.c.id == _id)
      .values(**data)
)
    conn.execute(stmt)
    conn.commit()

  @with_connection
  def delete_user(self, conn, _id) -> None:
    if not is_valid_id(conn, users_table, _id):
      return

    stmt = delete(users_table).where(users_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()