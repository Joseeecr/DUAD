from exceptions.generated_exceptions import ValidationError
from typing import Optional

class RoleValidators:

  def insert_role_validator(self, data : dict) -> Optional[list]:
    errors = []

    if not data.get("role"):
      errors.append("Role is required")

    return errors


  def validate_role_filters(self, params: dict) -> dict:
    filters = {}

    if "id" in params:
      if params["id"].isdigit():
        filters["id"] = int(params["id"])
      else:
        raise ValidationError("Id must be a number")

    if "role" in params: 
      if params["role"].isalpha():
        filters["role"] = params["role"] 
      else:
        raise ValidationError("Role must be a valid text, it doesn't support numbers or special characters")

    return filters