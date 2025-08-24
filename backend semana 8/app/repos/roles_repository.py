from sqlalchemy import insert, select, delete, update
from db.tables import roles_table
from repos.repos_utils import with_connection, is_valid_id, validate_column_and_query_value
from exceptions.generated_exceptions import RoleNotFoundError

class RolesRepository:
  def __init__(self, engine, role_validator):
    self.engine = engine
    self.role_validator = role_validator

  @with_connection
  def get_roles(self, conn, filters : dict) -> dict:
    stmt = select(roles_table)

    if "id" in filters:
      if validate_column_and_query_value(conn, roles_table, "id", filters["id"]):
        stmt = stmt.where(roles_table.c.id == filters["id"])
      else:
        raise RoleNotFoundError(f"Role with id {filters["id"]} not found")

    if "role" in filters:
      if validate_column_and_query_value(conn, roles_table, "role", filters["role"]):
        stmt = stmt.where(roles_table.c.role == filters["role"])
      else:
        raise RoleNotFoundError(f"Role '{filters["role"]}' not found")

    results = conn.execute(stmt)

    roles = [dict(row._mapping) for row in results]

    if not roles:
      raise RoleNotFoundError("No matching Roles found.")

    return roles


  @with_connection
  def insert_role(self, conn, role : str) -> int:

    stmt = insert(roles_table).returning(roles_table.c.id).values(role=role)
    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def update_role(self, conn, id : int, role : str) -> int:

    stmt = (
      update(roles_table).returning(roles_table.c.id)
      .where(roles_table.c.id == id)
      .values(role=role)
    )

    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def delete_role(self, conn, _id : int) -> bool:
    if not is_valid_id(conn, roles_table, _id):
      return False

    stmt = delete(roles_table).where(roles_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()
    return True