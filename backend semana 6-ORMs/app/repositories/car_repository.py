from sqlalchemy import insert, select, update, delete
from db.tables import cars_table, users_table
from repositories.repository_utils import with_connection, is_valid_id
class CarRepository:
  def __init__(self, engine):
    self.engine = engine


  @with_connection
  def add_car(self, conn, make : str, model: str, year_of_manufacture: int, user_id = None) -> None:

    car_data = insert(cars_table).values(
      make = make,
      model = model,
      year_of_manufacture = year_of_manufacture,
      user_id = user_id
    )
    conn.execute(car_data)
    conn.commit()


  @with_connection
  def get_car_by_id(self, conn,  _id: int) -> None:

    if not is_valid_id(conn, cars_table, _id):
      return

    stmt = select(cars_table).where(cars_table.c.id == _id)

    for row in conn.execute(stmt): 
      print(row)


  @with_connection
  def get_all_cars(self, conn) -> None:
    stmt = select(cars_table)

    for row in conn.execute(stmt):
      print(row)


  @with_connection
  def update_car(self, conn, _id : int, data: dict) -> None:
    if not is_valid_id(conn, cars_table, _id):
      return

    stmt = (
      update(cars_table)
      .where(cars_table.c.id == _id)
      .values(**data)
)
    conn.execute(stmt)
    conn.commit()


  @with_connection
  def delete_car(self, conn, _id) -> None:
    if not is_valid_id(conn, cars_table, _id):
      return

    stmt = delete(cars_table).where(cars_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()


  @with_connection
  def create_car_user_relation(self, conn, car_id : int, user_id : int) -> None:
    if is_valid_id(conn, cars_table, car_id) and is_valid_id(conn, users_table, user_id):
      stmt = (
      update(cars_table)
      .where(cars_table.c.id == car_id)
      .values(user_id = user_id)
      )
      conn.execute(stmt)
      conn.commit()


