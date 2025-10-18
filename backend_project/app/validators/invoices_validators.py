from app.exceptions.exceptions import ValidationError
from typing import Union, Optional
from decimal import Decimal, InvalidOperation

class InvoicesValidator:
  def __init__(self):
    self.validation_map = {
      "user_id": self.validate_id,
      "cart_id": self.validate_id,
      "payment_method_id": self.validate_id,
      "total": self.validate_price,
      "status": self.validate_status,
      "shipping_address_id": self.validate_id,
    }


  def validate_id(self, value : str) -> int:
    try:
      value = int(value)
      return value
    except ValueError:
      raise ValidationError("Id must be a number")


  def validate_status(self, status : str) -> str:
    status = str(status)
    if not status.isalpha() or status not in ["paid", "pending", "canceled"]:
      raise ValidationError("Invalid status")
    return status


  def validate_price(self, price : Union[str, int, float]) -> Optional[None|Decimal]:
    try:
      value = Decimal(str(price).strip())
      if abs(value.as_tuple().exponent) <= 2:
        return value
      raise ValidationError("Only two decimals are allowed")
    except InvalidOperation:
      raise ValidationError("Invalid operator")


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
    allowed_keys = {"id", "user_id", "cart_id", "payment_method_id", "total", "status", "shipping_address_id"}

    for key in params:
      if key not in allowed_keys:
        raise ValidationError(f"Unknown query parameter: '{key}'")

    if "id" in params:
      filters["id"] = self.validate_id(params["id"])

    if "user_id" in params:
      filters["user_id"] = self.validate_id(params["user_id"])

    if "cart_id" in params:
      filters["cart_id"] = self.validate_id(params["cart_id"])

    if "payment_method_id" in params:
      filters["payment_method_id"] = self.validate_id(params["payment_method_id"])

    if "total" in params:
      filters["total"] = self.validate_price(params["total"])

    if "status" in params:
      filters["status"] = self.validate_status(params["status"])

    if "shipping_address_id" in params:
      filters["shipping_address_id"] = self.validate_id(params["shipping_address_id"])

    return filters