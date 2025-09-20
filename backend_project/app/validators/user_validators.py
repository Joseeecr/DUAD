from app.exceptions.exceptions import ValidationError
from typing import Union
import re

class UserValidator:
  def __init__(self):
    self.validation_map = {
      "name": self.validate_user_name_lastname,
      "last_name": self.validate_user_name_lastname,
      "email": self.validate_user_email,
      "password": self.validate_password,
      "phone_number": self.validate_phone_number,
      "is_admin": self.validate_role
    }


  def validate_id(self, value : Union[str, int]) -> int:
    try:
      value = int(value)
      return value
    except ValueError:
      raise ValidationError("Id must be a number")


  def validate_user_name_lastname(self, value : str) -> str:
    if not value.isalpha():
      raise ValidationError("Name/Last name must be only letters")
    return value


  def validate_user_email(self, email : str) -> str:
    email_structure = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    match = re.search(email_structure, email)

    if not match:
      raise ValidationError("Incorrect email structure")
    return email


  def validate_password(self, password : str) -> str:
    if len(password) < 8:
      raise ValidationError("Password too short")
    elif password.isalpha() or password.isdigit():
      raise ValidationError("Password must include letters, numbers and symbols")
    elif " " in password:
      raise ValidationError("Passwords must not contain spaces")
    
    return password


  def validate_phone_number(self, phone: str) -> str:
    if not phone.isdigit():
      raise ValidationError("Phone number must be all digits without spaces")
    return phone


  def validate_role(self, role : str):
    if str(role).lower() == "true":
      return True
    elif str(role).lower() == "false":
      return False
    else:
      raise ValidationError("Role must be a boolean value")


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
    allowed_keys = {"id", "name", "last_name", "email", "is_admin"}

    for key in params:
      if key not in allowed_keys:
        raise ValidationError(f"Unknown query parameter: '{key}'")

    if "id" in params:
      filters["id"] = self.validate_id(params["id"])
    
    if "name" in params:
      filters["name"] = self.validate_user_name_lastname(params["name"])

    if "last_name" in params:
      filters["last_name"] = self.validate_user_name_lastname(params["last_name"])

    if "email" in params:
      filters["email"] = self.validate_user_email(params["email"])

    if "is_admin" in params:
      filters["is_admin"] = self.validate_role(params["is_admin"])

    return filters


  def validate_insert_user(self, data : dict):
    required_keys = {"name", "last_name", "email", "password", "phone_number", "is_admin"}

    for field in required_keys:
      if field not in data:
        raise ValidationError(f"Missing field: {field}")

    for key in data:
      if key not in required_keys:
        raise ValidationError(f"Invalid field: {key}")

    return self._validate_dict_data(data)


  def validate_update_user(self, data : dict) -> dict:
    optional_keys_to_update = {"name", "last_name", "email", "password", "phone_number", "is_admin"}

    for key in data:
      if key not in optional_keys_to_update:
        raise ValidationError(f"Invalid")
    
    return self._validate_dict_data(data)
