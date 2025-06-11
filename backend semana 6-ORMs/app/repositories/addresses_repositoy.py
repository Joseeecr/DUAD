from sqlalchemy import insert, select, update, delete
from db.tables import address_table
from repositories.repository_utils import with_connection, is_valid_id
class AddressRepository:
  def __init__(self, engine):
    self.engine = engine


  @with_connection
  def add_address(self, conn, street : str, city: str, province: str, zip_code : str, country : str, user_id : int) -> None:

    address_data = insert(address_table).values(
      street = street,
      city = city,
      province = province,
      zip_code = zip_code,
      country = country,
      user_id = user_id
    )
    conn.execute(address_data)
    conn.commit()


  @with_connection
  def get_address_by_id(self, conn,  _id: int) -> None:
    if not is_valid_id(conn, address_table, _id):
      return

    stmt = select(address_table).where(address_table.c.id == _id)

    for row in conn.execute(stmt): 
      print(row)


  @with_connection
  def get_all_address(self, conn) -> None:
    stmt = select(address_table)

    for row in conn.execute(stmt):
      print(row)


  @with_connection
  def update_address(self, conn, _id : int, data: dict) -> None:
    if not is_valid_id(conn, address_table, _id):
      return

    stmt = (
      update(address_table)
      .where(address_table.c.id == _id)
      .values(**data)
)
    conn.execute(stmt)
    conn.commit()


  @with_connection
  def delete_address(self, conn, _id) -> None:
    if not is_valid_id(conn, address_table, _id):
      return

    stmt = delete(address_table).where(address_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()