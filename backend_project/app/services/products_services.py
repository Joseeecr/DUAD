from sqlalchemy import select
from app.db.models import products_table
from app.exceptions.exceptions import NotFoundError



class ProductsService:
  def __init__(self, products_validator, product_repository):
    self.products_validator = products_validator
    self.product_repository = product_repository


  def list_products(self, params : dict) -> list[dict]:
    filters  = self.products_validator.validate_filters(params)

    stmt = (select(
      products_table.c.id,
      products_table.c.name,
      products_table.c.price,
      products_table.c.sku,
      products_table.c.category_id,
      products_table.c.stock
    ))

    if "id" in filters:
      stmt = stmt.where(products_table.c.id == filters["id"])

    if "name" in filters:
      stmt = stmt.where(products_table.c.name == filters["name"])

    if "price" in filters:
      stmt = stmt.where(products_table.c.price == filters["price"])

    if "sku" in filters:
      stmt = stmt.where(products_table.c.sku == filters["sku"])

    if "category_id" in filters:
      stmt = stmt.where(products_table.c.category_id == filters["category_id"])

    if "stock" in filters:
      stmt = stmt.where(products_table.c.stock == filters["stock"])

    result = self.product_repository.get_products(stmt)
  
    products = [dict(row._mapping) for row in result]

    if not products:
      raise NotFoundError("No matching products found.")

    return products


  def insert_product(self, data : dict) -> str:
    validate_data = self.products_validator.validate_insert_products(data)

    product = self.product_repository.insert_product(validate_data)

    return product


  def get_product_by_id(self, id : int) -> int:
    product = self.product_repository.get_product_by_id(id)

    if not product:
      raise ValueError("Product not found")

    return product


  def update_product_by_admin(self, products_id : int, data : dict):
    products = self.product_repository.get_product_by_id(products_id)

    if not products:
      raise ValueError("Product not found")
    
    validate_data = self.products_validator.validate_update_products(data)

    return self.product_repository.update_product(products_id, validate_data)


  def delete_product(self, products_id : int):
    products = self.product_repository.get_product_by_id(products_id)

    if not products:
      raise ValueError("products not found")
  
    return self.product_repository.delete_product(products_id)