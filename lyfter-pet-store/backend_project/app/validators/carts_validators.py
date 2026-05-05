from app.exceptions.exceptions import ValidationError
from decimal import Decimal, InvalidOperation
from typing import Optional
from typing import Union

class CartsValidator:
  def __init__(self):
    self.validation_map = {
      "product_id": self.validate_is_int,
      "user_id": self.validate_is_int,
      "quantity": self.validate_is_int,
      "status": self.validate_status,
      "payment_method": self.validate_payment_method,
      "price": self.validate_price,
      "shipping_address": self.validate_shipping_address
    }


  def validate_is_int(self, value : Union[str, int]) -> int:
    try:
      value = int(value)
      return value
    except ValueError:
      raise ValidationError("Only numbers are allowed")


  def validate_price(self, price : Union[str, int, float]) -> Optional[None|Decimal]:
    try:

      value = Decimal(str(price).strip())

      if not abs(value.as_tuple().exponent) <= 2:
        raise ValidationError("Only two decimals are allowed")
      if not value >= 0:
        raise ValidationError("Only positive numbers are allowed")

      return value

    except InvalidOperation:
      raise ValidationError("Invalid operator")


  def validate_status(self, status : str) -> str:
    status = str(status)
    if not status.isalpha() or status not in ["active", "closed", "abandoned", "expired"]:
      raise ValidationError("Invalid status")
    return status


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
    allowed_keys = {"id", "user_id", "status"}

    for key in params:
      if key not in allowed_keys:
        raise ValidationError(f"Unknown query parameter: '{key}'")

    if "id" in params:
      filters["id"] = self.validate_is_int(params["id"])
    
    if "user_id" in params:
      filters["user_id"] = self.validate_is_int(params["user_id"])

    if "status" in params:
      filters["status"] = self.validate_status(params["status"])

    return filters


  def validate_payment_method(self, pay_method : str) -> str:
    pay_method = str(pay_method)
    if not pay_method.isalpha() or pay_method not in ["sinpe", "card", "cash"]:
      raise ValidationError("Invalid method")
    return pay_method


  def validate_insert_products_to_cart(self, data : dict):
    required_keys = {"product_id", "quantity"}


    for field in required_keys:
      if field not in data:
        raise ValidationError(f"Missing field: {field}")

    for key in data:
      if key not in required_keys:
        raise ValidationError(f"Invalid field: {key}")

    return self._validate_dict_data(data)


  def validate_shipping_address(self, data : dict):
    required_keys = {"street", "city", "province", "zip_code", "country"}

    for field in required_keys:
      if field not in data:
        raise ValidationError(f"Missing field: {field}")

    for key in data:
      if key not in required_keys:
        raise ValidationError(f"Invalid field: {key}")

    if not isinstance(data["street"], str) or not data["street"].strip():
      raise ValidationError("street must be a non-empty string")

    if not isinstance(data["city"], str) or not data["city"].strip():
      raise ValidationError("city must be a non-empty string")

    if not isinstance(data["province"], str) or not data["province"].strip():
      raise ValidationError("province must be a non-empty string")

    if not (isinstance(data["zip_code"], str) or isinstance(data["zip_code"], int)):
      raise ValidationError("zip_code must be a string or integer")

    if isinstance(data["zip_code"], str) and not data["zip_code"].strip():
        raise ValidationError("zip_code must be a non-empty string")

    if not isinstance(data["country"], str) or not data["country"].strip():
      raise ValidationError("country must be a non-empty string")

    return data


  def validate_update_cart_admin(self, data : dict) -> dict:
    optional_keys_to_update = {"user_id", "status", "cart_id", "product_id", "quantity", "price"}

    for key in data:
      if key not in optional_keys_to_update:
        raise ValidationError(f"Invalid key: '{key}'")
    
    return self._validate_dict_data(data)


  def validate_create_invoice(self, data : dict):
    required_keys = {"payment_method", "shipping_address"}

    for field in required_keys:
      if field not in data:
        raise ValidationError(f"Missing field: {field}")

    for key in data:
      if key not in required_keys:
        raise ValidationError(f"Invalid field: {key}")

    if not isinstance(data["shipping_address"], dict):
        raise ValidationError("shipping_address must be an object/dict")

    return self._validate_dict_data(data)