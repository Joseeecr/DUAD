from typing import Optional
from exceptions.generated_exceptions import ValidationError
from datetime import datetime, time

class ShoppingCartValidators:

  def create_cart_registration(self, data : dict) -> Optional[list]:
    errors = []
    user_id  = data.get("user_id")
    if not user_id:
      errors.append("User id is required")
    elif not str(user_id).isdigit():
      errors.append("User id must be a number")
    return errors


  def validate_cart_filters(self, params: dict) -> dict:
    filters = {}

    if "id" in params:
      if params["id"].isdigit():
        filters["id"] = int(params["id"])
      else:
        raise ValidationError("Id must be a number")

    if "user_id" in params: 
      if params["user_id"].isdigit():
        filters["user_id"] = int(params["user_id"])
      else:
        raise ValidationError("User Id must be a number")

    if "status" in params:
      if params["status"] in ["active", "closed", "canceled"]:
        filters["status"] = params["status"]
      else:
        raise ValidationError("Status must be a 'active', 'closed' or 'canceled'")

    if "created_at" in params:
      try:
        date_only = datetime.strptime(params["created_at"], "%Y-%m-%d").date()
        print("This is date only:", date_only)
        filters["created_from"] = datetime.combine(date_only, time.min)
        filters["created_to"] = datetime.combine(date_only, time.max)
      except ValueError:
        raise ValidationError("Invalid format for entry_date. Use YYYY-MM-DD.")

    return filters