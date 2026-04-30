import pytest
from app.validators.invoices_validators import InvoicesValidator
from app.exceptions.exceptions import ValidationError
from decimal import Decimal

def test_validate_status_with_valid_paid_returns_value():
  validator = InvoicesValidator()
  value = "paid"

  result = validator.validate_status(value)

  assert result == "paid"
  assert isinstance(result, str)


def test_validate_status_with_valid_pending_returns_value():
  validator = InvoicesValidator()
  value = "pending"

  result = validator.validate_status(value)

  assert result == "pending"
  assert isinstance(result, str)


def test_validate_status_with_valid_canceled_returns_value():
  validator = InvoicesValidator()
  value = "canceled"

  result = validator.validate_status(value)

  assert result == "canceled"
  assert isinstance(result, str)


def test_validate_status_with_numbers_raises_error():
  validator = InvoicesValidator()
  value = "canceled123"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_status_with_symbols_raises_error():
  validator = InvoicesValidator()
  value = "canceled!"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_status_with_invalid_string_raises_error():
  validator = InvoicesValidator()
  value = "active"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_status_with_empty_string_raises_error():
  validator = InvoicesValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_all_keys_valid_return_value():
  validator = InvoicesValidator()

  data = {
    "user_id": 1,
    "cart_id": 1,
    "payment_method_id": 1,
    "total": 22.90,
    "status": "paid",
    "shipping_address_id": 10,
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "user_id": 1,
    "cart_id": 1,
    "payment_method_id": 1,
    "total": Decimal("22.90"),
    "status": "paid",
    "shipping_address_id": 10,
    }

  assert isinstance(result, dict)


def test_validate_dict_data_partial_keys_return_value():
  validator = InvoicesValidator()

  data = {
    "user_id": 1,
    "cart_id":2,
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "user_id": 1,
    "cart_id":2
  }
  assert isinstance(result, dict)


def test_validate_dict_data_unknown_key_raises_error():
  validator = InvoicesValidator()

  data = {"random": "Gabriel"}

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "No validation method for key: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_empty_dict_return_value():
  validator = InvoicesValidator()

  data = {}

  result = validator._validate_dict_data(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_dict_data_some_keys_invalid_raises_error():
  validator = InvoicesValidator()

  data = {
    "user_id": "uno",
    "cart_id":2,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "Id must be a number"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_all_valid_keys_return_value():
  validator = InvoicesValidator()

  data = {
    "id": 1,
    "user_id": 1,
    "cart_id": 1,
    "payment_method_id": 1,
    "total": 22.90,
    "status": "paid",
    "shipping_address_id": 10,
  }

  result = validator.validate_filters(data)

  assert result == {
    "id": 1,
    "user_id": 1,
    "cart_id": 1,
    "payment_method_id": 1,
    "total": Decimal("22.90"),
    "status": "paid",
    "shipping_address_id": 10,
  }
  assert isinstance(result, dict)


def test_validate_filters_with_unknown_key_raises_error():
  validator = InvoicesValidator()

  data = {
    "is_admin": True,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Unknown query parameter: 'is_admin'"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_partial_valid_keys_return_value():
  validator = InvoicesValidator()

  data = { 
    "payment_method_id": 1
  }

  result = validator.validate_filters(data)

  assert result == { 
    "payment_method_id": 1
  }
  assert isinstance(result, dict)


def test_validate_filters_empty_params_return_value():
  validator = InvoicesValidator()

  data = {}

  result = validator.validate_filters(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_filters_invalid_value_type_raises_error():
  validator = InvoicesValidator()

  data = {
    "id": "1", 
    "user_id": 1,
    "cart_id": "one",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Id must be a number"
  assert isinstance(exc_info.value, ValidationError)