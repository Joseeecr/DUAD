from typing import Optional
from exceptions.generated_exceptions import ValidationError
from datetime import datetime, time

class UserValidators:

  def validate_user_filters(self, params: dict) -> dict:
    filters = {}

    if "id" in params:
      if params["id"].isdigit():
        filters["id"] = int(params["id"])
      else:
        raise ValidationError("Id must be a number")

    if "user_name" in params: 
      if params["user_name"].isalpha():
        filters["user_name"] = params["user_name"]
      else:
        raise ValidationError("User name must be text")

    if "role_id" in params:
      if params["role_id"].isdigit():
        filters["role_id"] = int(params["role_id"])
      else:
        raise ValidationError("Role Id must be a number")

    return filters