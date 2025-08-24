from sqlalchemy import insert, select, delete, update
from db.tables import user_table
from repos.repos_utils import with_connection, is_valid_id, validate_column_and_query_value
from typing import Optional
from exceptions.generated_exceptions import UserNotFoundError
import bcrypt 

class UserRepository:
  def __init__(self, engine, user_validator):
    self.engine = engine
    self.user_validator = user_validator

  @with_connection
  def get_users(self, conn, filters : dict) -> dict:
    stmt = select(user_table)

    if "id" in filters:
      if validate_column_and_query_value(conn, user_table, "id", filters["id"]):
        stmt = stmt.where(user_table.c.id == filters["id"])
      else:
        raise UserNotFoundError(f"User with id {filters["id"]} not found")

    if "user_name" in filters:
      if validate_column_and_query_value(conn, user_table, "user_name", filters["user_name"]):
        stmt = stmt.where(user_table.c.user_name == filters["user_name"])
      else:
        raise UserNotFoundError(f"User '{filters["name"]}' not found")
  
    if "role_id" in filters:
      if validate_column_and_query_value(conn, user_table, "role_id", filters["role_id"]):
        stmt = stmt.where(user_table.c.role_id == filters["role_id"])
      else:
        raise UserNotFoundError(f"User with role id '{filters["role_id"]}' not found")

    results = conn.execute(stmt)

    users = [dict(row._mapping) for row in results]

    if not users:
      raise UserNotFoundError("No matching users found.")

    return users


  @with_connection
  def insert_user(self, conn, username : str, password : str, role_id : int) -> int:

    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    encript = bcrypt.hashpw(password, salt).decode("utf-8")

    stmt = insert(user_table).returning(user_table.c.id).values(username=username, password=encript, role_id=role_id)
    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def get_user(self, conn, username : str, password : str) -> Optional[int]:
    stmt = select(user_table).where(user_table.c.username == username)
    result = conn.execute(stmt)

    user = result.fetchone()

    if user is None:
      return None

    stored_hash = user.password.encode("utf-8") if isinstance(user.password, str) else user.password
    if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
      return user
    else:
      return None


  @with_connection
  def get_user_by_id(self, conn, id : int) -> Optional[int]:
    if not is_valid_id(conn, user_table, id):
      return False

    stmt = select(user_table).where(user_table.c.id == id)
    result = conn.execute(stmt)
    users = result.all()

    if len(users) ==0:
        return None
    else:
        return users[0]


  @with_connection
  def update_user(self, conn, id : int, data : dict) -> int:
    if not is_valid_id(conn, user_table, id):
      return False

    stmt = (
      update(user_table).returning(user_table.c.id)
      .where(user_table.c.id == id)
      .values(**data)
    )
    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def delete_user(self, conn, _id : int) -> bool:
    if not is_valid_id(conn, user_table, _id):
      return False

    stmt = delete(user_table).where(user_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()
    return True