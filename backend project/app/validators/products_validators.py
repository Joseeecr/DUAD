from exceptions.exceptions import ValidationError
from decimal import Decimal, InvalidOperation
from typing import Union, Optional
import re


class ProductsValidator:
  def __init__(self):
    self.validation_map = {
      "name": self.validate_product_name,
      "price": self.validate_price,
      "sku": self.validate_sku,
      "category_id": self.validate_is_number,
      "stock": self.validate_is_number,
    }


  def validate_is_number(self, value : Union[str, int]) -> int:
    try:
      value = int(value)
      return value
    except ValueError:
      raise ValidationError("Only numbers are allowed")


  def validate_product_name(self, value : str) -> str:
    if not re.match(r'^(?=.*[a-zA-Z])[\S0-9\s]+$', value):
      raise ValidationError("Invalid name")
    return value


  def validate_price(self, price : Union[str, int, float]) -> Optional[None|Decimal]:
    try:
      value = Decimal(str(price).strip())
      if abs(value.as_tuple().exponent) <= 2:
        return value
      raise ValidationError("Only two decimals are allowed")
    except InvalidOperation:
      raise ValidationError("Invalid operator")


  def validate_sku(self, sku: str) -> str:
    sku_structure = r"^[A-Z]{4}+[0-9]{4}$"
    match = re.search(sku_structure, sku)

    if not match:
      raise ValidationError("Incorrect SKU structure")
    return sku


  def _validate_dict_data(self, data : dict):
    validate_data = {}
    for key, value in data.items():
      if key in self.validation_map:
        validated_value = self.validation_map[key](value)
        validate_data[key] = validated_value
      else:
        raise ValidationError(f"No validation method for key: {key}")
    return validate_data


  def validate_filters(self, params : dict) -> dict:
    filters = {}
    allowed_keys = {"id", "name", "price", "sku", "category_id", "stock"}

    for key in params:
      if key not in allowed_keys:
        raise ValidationError(f"Unknown query parameter: '{key}'")

    if "id" in params:
      filters["id"] = self.validate_is_number(params["id"])
    
    if "name" in params:
      filters["name"] = self.validate_product_name(params["name"])

    if "price" in params:
      filters["price"] = self.validate_price(params["price"])

    if "sku" in params:
      filters["sku"] = self.validate_sku(params["sku"])

    if "stock" in params:
      filters["stock"] = self.validate_is_number(params["stock"])

    return filters


  def validate_insert_products(self, data : dict):
    required_keys = {"name", "price", "sku", "category_id", "stock"}


    for field in required_keys:
      if field not in data:
        raise ValidationError(f"Missing field: {field}")

    for key in data:
      if key not in required_keys:
        raise ValidationError(f"Invalid field: {key}")

    return self._validate_dict_data(data)


  def validate_update_products(self, data : dict) -> dict:
    optional_keys_to_update = {"name", "price", "sku", "category_id", "stock"}

    for key in data:
      if key not in optional_keys_to_update:
        raise ValidationError(f"Invalid")
    
    return self._validate_dict_data(data)
