from sqlalchemy import insert, select, delete, update
from db.tables import products_table
from repos.repos_utils import with_connection, validate_column_and_query_value
from typing import Optional
from exceptions.generated_exceptions import ProductNotFoundError, ColumnNotFoundError



class ProductsRepository:
  def __init__(self, engine, product_validator):
    self.engine = engine
    self.product_validator = product_validator

  @with_connection
  def get_products(self, conn, filters : dict) -> dict:
    stmt = select(products_table)

    if "id" in filters:
      if validate_column_and_query_value(conn, products_table, "id", filters["id"]):
        stmt = stmt.where(products_table.c.id == filters["id"])
      else:
        raise ProductNotFoundError(f"Product with id {filters["id"]} not found")

    if "name" in filters:
      if validate_column_and_query_value(conn, products_table, "name", filters["name"]):
        stmt = stmt.where(products_table.c.name == filters["name"])
      else:
        raise ProductNotFoundError(f"Product with name '{filters["name"]}' not found")
  
    if "price" in filters:
      if validate_column_and_query_value(conn, products_table, "price", filters["price"]):
        stmt = stmt.where(products_table.c.price == filters["price"])
      else:
        raise ProductNotFoundError(f"Product with price '{filters["price"]}' not found")

    if "entry_date_from" in filters:
      if validate_column_and_query_value(conn, products_table, "entry_date", filters["entry_date_from"]):
        stmt = stmt.where(products_table.c.entry_date >= filters["entry_date_from"])
      else:
        raise ProductNotFoundError(f"Product with date '{filters["entry_date_from"]}' not found")

    if "entry_date_to" in filters:
      if validate_column_and_query_value(conn, products_table, "entry_date", filters["entry_date_to"]):
        stmt = stmt.where(products_table.c.entry_date >= filters["entry_date_to"])
      else:
        raise ProductNotFoundError(f"Product with date '{filters["entry_date_to"]}' not found")

    if "quantity" in filters:
      if validate_column_and_query_value(conn, products_table, "quantity", filters["quantity"]):
        stmt = stmt.where(products_table.c.quantity == filters["quantity"])
      else:
        raise ProductNotFoundError(f"Product with quantity '{filters["quantity"]}' not found")


    results = conn.execute(stmt)

    products = [dict(row._mapping) for row in results]

    if not products:
      raise ProductNotFoundError("No matching products found.")

    return products

  @with_connection
  def get_product_by_id(self, conn, id : int) -> Optional[int]:

    stmt = select(products_table).where(products_table.c.id == id)
    result = conn.execute(stmt)
    product = result.first()

    if not product:
      raise ProductNotFoundError("No matching products found.")
    
    product = dict(product._mapping)

    return product


  @with_connection
  def insert_product(self, conn, name : str, price : int, quantity : int) -> int:
    if validate_column_and_query_value(conn, products_table, "name", name):
      return False

    stmt = insert(products_table).returning(products_table.c.id).values(name=name, price=price, quantity=quantity)
    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def update_product(self, conn, id : int, data : dict) -> int:
    if not validate_column_and_query_value(conn, products_table, "id", id):
      raise ProductNotFoundError("No matching products found")

    valid_columns = set(products_table.columns.keys())
    incoming_columns = set(data.keys())
    invalid_columns = incoming_columns - valid_columns

    if invalid_columns:
      raise ColumnNotFoundError(f"Invalid columns in update: {', '.join(invalid_columns)}")

    stmt = (
      update(products_table).returning(products_table.c.id)
      .where(products_table.c.id == id)
      .values(**data)
    )

    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def delete_product(self, conn, _id : int) -> bool:
    if not validate_column_and_query_value(conn, products_table, "id", _id):
      return False

    stmt = delete(products_table).where(products_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()
    return True