import pytest
from app.validators.user_validators import UserValidator
from app.exceptions.exceptions import ValidationError

def test_validate_id_with_int():
  validator = UserValidator()
  value = 5

  result = validator.validate_id(value)

  assert result == 5
  assert isinstance(result, int)


def test_validate_id_with_numeric_string():
  validator = UserValidator()
  value = "42"

  result = validator.validate_id(value)

  assert result == 42
  assert isinstance(result, int)


def test_validate_id_raises_error_with_non_numeric_string():
  validator = UserValidator()
  value = "four"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_id(value)

  assert str(exc_info.value) == "Id must be a number"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_id_raises_error_with_empty_string():
  validator = UserValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_id(value)

  assert str(exc_info.value) == "Id must be a number"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_id_with_negative_number():
  validator = UserValidator()
  value = "-5"

  result = validator.validate_id(value)

  assert result == -5
  assert isinstance(result, int)


def test_validate_user_name_lastname_with_valid_name():
  validator = UserValidator()
  value = "Jose"

  result = validator.validate_user_name_lastname(value)

  assert result == "Jose"
  assert isinstance(result, str)


def test_validate_user_name_lastname_with_numbers_raises_error():
  validator = UserValidator()
  value = "Jose Blanco2"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_user_name_lastname(value)

  assert str(exc_info.value) == "Name/Last name must be only letters"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_user_name_lastname_with_special_chars_raises_error():
  validator = UserValidator()
  value = "Jose-Blanco"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_user_name_lastname(value)

  assert str(exc_info.value) == "Name/Last name must be only letters"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_user_email_with_valid_email():
  validator = UserValidator()
  value = "userexample.com@yahoo.com"

  result = validator.validate_user_email(value)

  assert result == "userexample.com@yahoo.com"
  assert isinstance(result, str)


def test_validate_user_email_with_dot_and_subdomain():
  validator = UserValidator()
  value = "user.name@sub.example.com"

  result = validator.validate_user_email(value)

  assert result == "user.name@sub.example.com"
  assert isinstance(result, str)


def test_validate_user_email_without_at_symbol_raises_error():
  validator = UserValidator()
  value = "userexample.com"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_user_email(value)

  assert str(exc_info.value) == "Incorrect email structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_user_email_without_domain_raises_error():
  validator = UserValidator()
  value = "user@"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_user_email(value)

  assert str(exc_info.value) == "Incorrect email structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_user_email_with_spaces_raises_error():
  validator = UserValidator()
  value = "user example.com@ yahoo.com"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_user_email(value)

  assert str(exc_info.value) == "Incorrect email structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_password_with_valid_password():
  validator = UserValidator()
  value = "passexample123*"

  result = validator.validate_password(value)

  assert result == "passexample123*"
  assert isinstance(result, str)


def test_validate_password_too_short_raises_error():
  validator = UserValidator()
  value = "pass"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_password(value)

  assert str(exc_info.value) == "Password too short"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_password_only_letters_raises_error():
  validator = UserValidator()
  value = "passwordddd"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_password(value)

  assert str(exc_info.value) == "Password must include letters, numbers and symbols"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_password_only_numbers_raises_error():
  validator = UserValidator()
  value = "12345678"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_password(value)

  assert str(exc_info.value) == "Password must include letters, numbers and symbols"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_password_with_spaces_raises_error():
  validator = UserValidator()
  value = "passexample 123"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_password(value)

  assert str(exc_info.value) == "Passwords must not contain spaces"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_phone_number_with_only_digits_returns_value():
  validator = UserValidator()
  value = "77665544"

  result = validator.validate_phone_number(value)

  assert result == "77665544"
  assert isinstance(result, str)


def test_validate_phone_number_with_letters_raises_error():
  validator = UserValidator()
  value = "unodostres"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_phone_number(value)

  assert str(exc_info.value) == "Phone number must be all digits without spaces"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_phone_number_with_spaces_raises_error():
  validator = UserValidator()
  value = "1234 5678"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_phone_number(value)

  assert str(exc_info.value) == "Phone number must be all digits without spaces"
  assert isinstance(exc_info.value, ValidationError)



def test_validate_phone_number_with_symbols_raises_error():
  validator = UserValidator()
  value = "12345678!"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_phone_number(value)

  assert str(exc_info.value) == "Phone number must be all digits without spaces"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_phone_number_empty_string_raises_error():
  validator = UserValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_phone_number(value)

  assert str(exc_info.value) == "Phone number must be all digits without spaces"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_role_true_string_lowercase_returns_value():
  validator = UserValidator()
  value = "true"

  result = validator.validate_role(value)

  assert result == True
  assert isinstance(result, bool)

def test_validate_role_false_string_lowercase_returns_value():
  validator = UserValidator()
  value = "false"

  result = validator.validate_role(value)

  assert result == False
  assert isinstance(result, bool)


def test_validate_role_true_string_uppercase_returns_value():
  validator = UserValidator()
  value = "TRUE"
  value2 = "FALSE"

  result = validator.validate_role(value)
  result2 = validator.validate_role(value2)

  assert result == True
  assert result2 == False
  assert isinstance(result, bool)
  assert isinstance(result2, bool)


def test_validate_role_invalid_string_raises_error():
  validator = UserValidator()
  value = "Hello World"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_role(value)

  assert str(exc_info.value) == "Role must be a boolean value"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_role_non_string_value_raises_error():
  validator = UserValidator()
  value = 1

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_role(value)

  assert str(exc_info.value) == "Role must be a boolean value"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_all_keys_valid_return_value():
  validator = UserValidator()

  data = {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234*",
    "phone_number": "11223345",
    "is_admin": True
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234*",
    "phone_number": "11223345",
    "is_admin": True
  }
  assert isinstance(result, dict)


def test_validate_dict_data_partial_keys_return_value():
  validator = UserValidator()

  data = {
    "name": "User",
    "is_admin": True
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "name": "User",
    "is_admin": True
  }
  assert isinstance(result, dict)


def test_validate_dict_data_unknown_key_raises_error():
  validator = UserValidator()

  data = {"random": "Gabriel"}

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "No validation method for key: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_empty_dict_return_value():
  validator = UserValidator()

  data = {}

  result = validator._validate_dict_data(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_dict_data_some_keys_invalid_raises_error():
  validator = UserValidator()

  data = {
    "name": "User",
    "is_admin": "Trueeeeee"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "Role must be a boolean value"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_all_valid_keys_return_value():
  validator = UserValidator()

  data = {
    "id": 1,
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "is_admin": True
  }

  result = validator.validate_filters(data)

  assert result == {
    "id": 1,
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "is_admin": True
  }
  assert isinstance(result, dict)


def test_validate_filters_with_unknown_key_raises_error():
  validator = UserValidator()

  data = {
    "is_admin": True,
    "random": 1,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Unknown query parameter: 'random'"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_partial_valid_keys_return_value():
  validator = UserValidator()

  data = { 
    "is_admin": True
  }

  result = validator.validate_filters(data)

  assert result == { 
    "is_admin": True
  }
  assert isinstance(result, dict)


def test_validate_filters_empty_params_return_value():
  validator = UserValidator()

  data = {}

  result = validator.validate_filters(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_filters_invalid_value_type_raises_error():
  validator = UserValidator()

  data = {
    "id": "1", 
    "name": "User", 
    "is_admin": "Truex",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Role must be a boolean value"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_user_all_required_keys_present():
  validator = UserValidator()

  data = {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234",
    "phone_number": "12345678",
    "is_admin": True
  }

  result = validator.validate_insert_user(data)

  assert result == {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234",
    "phone_number": "12345678",
    "is_admin": True
  }
  assert isinstance(result, dict)


def test_validate_insert_user_missing_required_key():
  validator = UserValidator()

  data = {
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234",
    "phone_number": "12345678",
    "is_admin": True
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_user(data)

  assert str(exc_info.value) == "Missing field: name"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_user_with_extra_key():
  validator = UserValidator()

  data = {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234",
    "phone_number": "12345678",
    "is_admin": True,
    "random": "deaa"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_user(data)

  assert str(exc_info.value) == "Invalid field: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_user_validates_values():
  validator = UserValidator()

  data = {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234",
    "phone_number": "12345678",
    "is_admin": "True",
  }

  result = validator.validate_insert_user(data)

  assert result == {
    "name": "User",
    "last_name": "White",
    "email": "user.name@sub.example.com",
    "password": "abcd1234",
    "phone_number": "12345678",
    "is_admin": True,
  }
  assert isinstance(result, dict)


def test_validate_update_user_with_valid_keys():
  validator = UserValidator()

  data = {
    "name": "User", 
    "is_admin": "false", 
  }

  result = validator.validate_update_user(data)

  assert result == {
    "name": "User", 
    "is_admin": False, 
  }
  assert isinstance(result, dict)


def test_validate_update_user_with_invalid_key():
  validator = UserValidator()

  data = {
    "random": "Manzana", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_user(data)

  assert str(exc_info.value) == "Invalid"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_user_validates_values():
  validator = UserValidator()

  data = {
    "is_admin": "False", 
  }

  result = validator.validate_update_user(data)

  assert result == { 
    "is_admin": False 
  }
  assert isinstance(result, dict)