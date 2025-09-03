from typing import Optional
from exceptions.generated_exceptions import ValidationError
from datetime import datetime, time

class ProductValidators:

  def insert_product_validator(self, data : dict) -> Optional[list]:
    errors = []

    if not data.get("name"):
      errors.append("Name is required")

    if not data.get("price"):
      errors.append("Price is required")

    if not data.get("quantity"):
      errors.append("Quantity is required")

    return errors


  def validate_product_filters(self, params: dict) -> dict:
    filters = {}

    if "id" in params:
      if params["id"].isdigit():
        filters["id"] = int(params["id"])
      else:
        raise ValidationError("Id must be a number")

    if "name" in params: 
      if params["name"].isalpha():
        filters["name"] = params["name"] 
      else:
        raise ValidationError("Name must be a valid text, it doesn't support numbers or special characters")

    if "price" in params:
      try:
        filters["price"] = float(params["price"])
      except ValueError:
        raise ValidationError("Price must be a number")

    if "entry_date" in params:
      try:
        date_only = datetime.strptime(params["entry_date"], "%Y-%m-%d").date()
        filters["entry_date_from"] = datetime.combine(date_only, time.min)
        filters["entry_date_to"] = datetime.combine(date_only, time.max)
      except ValueError:
        raise ValidationError("Invalid format for entry_date. Use YYYY-MM-DD.")

    if "quantity" in params:
      if params["quantity"].isdigit():
        filters["quantity"] = int(params["quantity"])
      else:
        raise ValidationError("Quantity must be a number")

    return filters