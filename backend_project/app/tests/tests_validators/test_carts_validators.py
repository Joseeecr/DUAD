import pytest
from app.validators.carts_validators import CartsValidator
from app.exceptions.exceptions import ValidationError

def test_validate_is_int_with_int():
  validator = CartsValidator()
  value = 5

  result = validator.validate_is_int(value)

  assert result == 5
  assert isinstance(result, int)


def test_validate_is_int_with_numeric_string():
  validator = CartsValidator()
  value = "42"

  result = validator.validate_is_int(value)

  assert result == 42
  assert isinstance(result, int)


def test_validate_is_int_raises_error_with_non_numeric_string():
  validator = CartsValidator()
  value = "four"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_is_int(value)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_is_int_raises_error_with_empty_string():
  validator = CartsValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_is_int(value)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_is_int_with_negative_number():
  validator = CartsValidator()
  value = "-5"

  result = validator.validate_is_int(value)

  assert result == -5
  assert isinstance(result, int)


def test_validate_status_with_valid_active_returns_value():
  validator = CartsValidator()
  value = "active"

  result = validator.validate_status(value)

  assert result == "active"
  assert isinstance(result, str)


def test_validate_status_with_valid_closed_returns_value():
  validator = CartsValidator()
  value = "closed"

  result = validator.validate_status(value)

  assert result == "closed"
  assert isinstance(result, str)


def test_validate_status_with_valid_abandoned_returns_value():
  validator = CartsValidator()
  value = "abandoned"

  result = validator.validate_status(value)

  assert result == "abandoned"
  assert isinstance(result, str)


def test_validate_status_with_valid_expired_returns_value():
  validator = CartsValidator()
  value = "expired"

  result = validator.validate_status(value)

  assert result == "expired"
  assert isinstance(result, str)


def test_validate_status_with_numbers_raises_error():
  validator = CartsValidator()
  value = "active123"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_status_with_symbols_raises_error():
  validator = CartsValidator()
  value = "expired!"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_status_with_invalid_string_raises_error():
  validator = CartsValidator()
  value = "pending"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_status_with_empty_string_raises_error():
  validator = CartsValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_status(value)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_all_keys_valid_return_value():
  validator = CartsValidator()

  data = {
    "product_id": 1,
    "quantity":2,
    "status": "active",
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "product_id": 1,
    "quantity":2,
    "status": "active",
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }
  assert isinstance(result, dict)


def test_validate_dict_data_partial_keys_return_value():
  validator = CartsValidator()

  data = {
    "product_id": 1,
    "quantity":2,
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "product_id": 1,
    "quantity":2,
  }
  assert isinstance(result, dict)


def test_validate_dict_data_unknown_key_raises_error():
  validator = CartsValidator()

  data = {"random": "Gabriel"}

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "No validation method for key: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_empty_dict_return_value():
  validator = CartsValidator()

  data = {}

  result = validator._validate_dict_data(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_dict_data_some_keys_invalid_raises_error():
  validator = CartsValidator()

  data = {
    "product_id": "uno",
    "quantity":2,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_all_valid_keys_return_value():
  validator = CartsValidator()

  data = {
    "id": 1,
    "user_id": 1,
    "status": "active",
  }

  result = validator.validate_filters(data)

  assert result == {
    "id": 1,
    "user_id": 1,
    "status": "active",
  }
  assert isinstance(result, dict)


def test_validate_filters_with_unknown_key_raises_error():
  validator = CartsValidator()

  data = {
    "is_admin": True,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Unknown query parameter: 'is_admin'"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_partial_valid_keys_return_value():
  validator = CartsValidator()

  data = { 
    "status": "active",
  }

  result = validator.validate_filters(data)

  assert result == { 
    "status": "active"
  }
  assert isinstance(result, dict)


def test_validate_filters_empty_params_return_value():
  validator = CartsValidator()

  data = {}

  result = validator.validate_filters(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_filters_invalid_value_type_raises_error():
  validator = CartsValidator()

  data = {
    "id": "1", 
    "user_id": "1", 
    "status": 1,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_payment_method_with_valid_sinpe_returns_value():
  validator = CartsValidator()
  value = "sinpe"

  result = validator.validate_payment_method(value)

  assert result == "sinpe"
  assert isinstance(result, str)


def test_validate_payment_method_with_valid_card_returns_value():
  validator = CartsValidator()
  value = "card"

  result = validator.validate_payment_method(value)

  assert result == "card"
  assert isinstance(result, str)


def test_validate_payment_method_with_valid_cash_returns_value():
  validator = CartsValidator()
  value = "cash"

  result = validator.validate_payment_method(value)

  assert result == "cash"
  assert isinstance(result, str)


def test_validate_payment_method_with_numbers_raises_error():
  validator = CartsValidator()
  value = "cash123"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_payment_method(value)

  assert str(exc_info.value) == "Invalid method"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_payment_method_with_symbols_raises_error():
  validator = CartsValidator()
  value = "cash!"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_payment_method(value)

  assert str(exc_info.value) == "Invalid method"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_payment_method_with_invalid_string_raises_error():
  validator = CartsValidator()
  value = "efectivo"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_payment_method(value)

  assert str(exc_info.value) == "Invalid method"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_payment_method_with_empty_string_raises_error():
  validator = CartsValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_payment_method(value)

  assert str(exc_info.value) == "Invalid method"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_to_cart_with_valid_data_returns_dict():
  validator = CartsValidator()

  data = {
    "product_id": 1,
    "quantity": 5,
  }

  result = validator.validate_insert_products_to_cart(data)

  assert result == {
    "product_id": 1,
    "quantity": 5
  }
  assert isinstance(result, dict)


def test_validate_insert_products_to_cart_missing_product_id_raises_error():
  validator = CartsValidator()

  data = {
    "quantity": 5,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_products_to_cart(data)

  assert str(exc_info.value) == "Missing field: product_id"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_to_cart_missing_quantity_raises_error():
  validator = CartsValidator()

  data = {
    "product_id": 1,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_products_to_cart(data)

  assert str(exc_info.value) == "Missing field: quantity"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_to_cart_with_extra_field_raises_error():
  validator = CartsValidator()

  data = {
    "product_id": 1,
    "quantity": 5,
    "random": 5
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_products_to_cart(data)

  assert str(exc_info.value) == "Invalid field: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_to_cart_validates_values():
  validator = CartsValidator()

  data = {
    "product_id": "1",
    "quantity": "5",
  }

  result = validator.validate_insert_products_to_cart(data)

  assert result == {
    "product_id": 1,
    "quantity": 5,
  }
  assert isinstance(result, dict)


def test_validate_shipping_address_with_valid_data_returns_dict():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica"
  }

  result = validator.validate_shipping_address(data)

  assert result == {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica"
  }
  assert isinstance(result, dict)


def test_validate_shipping_address_missing_street_raises_error():
  validator = CartsValidator()

  data = {
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "Missing field: street"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_missing_city_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "Missing field: city"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_missing_province_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "zip_code": "10101",
    "country": "Costa Rica"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "Missing field: province"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_missing_zip_code_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "country": "Costa Rica"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "Missing field: zip_code"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_missing_country_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "Missing field: country"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_extra_field_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica",
    "random": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "Invalid field: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_non_string_street_raises_error():
  validator = CartsValidator()

  data = {
    "street": 123,
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "street must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)

def test_validate_shipping_address_with_empty_street_raises_error():
  validator = CartsValidator()

  data = {
    "street": "",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "street must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_non_string_city_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": 123,
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "city must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_empty_city_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "",
    "province": "San José",
    "zip_code": "10101",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "city must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_non_string_province_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": 123,
    "zip_code": "10101",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "province must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_empty_province_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "",
    "zip_code": "10101",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "province must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_invalid_zip_code_type_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "",
    "country": "Costa Rica",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "zip_code must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_non_string_country_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": 1234,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "country must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_shipping_address_with_empty_country_raises_error():
  validator = CartsValidator()

  data = {
    "street": "Calle 0, Avenida Central",
    "city": "San José",
    "province": "San José",
    "zip_code": "10101",
    "country": "",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_shipping_address(data)

  assert str(exc_info.value) == "country must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_cart_admin_with_valid_keys_returns_dict():
  validator = CartsValidator()

  data = {
    "status": "active", 
    "quantity": 1, 
  }

  result = validator.validate_update_cart_admin(data)

  assert result == {
    "status": "active", 
    "quantity": 1, 
  }
  assert isinstance(result, dict)


def test_validate_update_cart_admin_with_invalid_key_raises_error():
  validator = CartsValidator()

  data = {
    "random": "Manzana", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_cart_admin(data)

  assert str(exc_info.value) == "Invalid key: 'random'"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_cart_admin_validates_values():
  validator = CartsValidator()

  data = {
    "quantity": "1", 
  }

  result = validator.validate_update_cart_admin(data)

  assert result == { 
    "quantity": 1
  }
  assert isinstance(result, dict)


def test_validate_update_cart_admin_with_invalid_user_id_raises_error():
  validator = CartsValidator()

  data = {
    "user_id": "uno", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_cart_admin(data)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_cart_admin_with_invalid_status_raises_error():
  validator = CartsValidator()

  data = {
    "status": "uno", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_cart_admin(data)

  assert str(exc_info.value) == "Invalid status"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_cart_admin_with_invalid_quantity_raises_error():
  validator = CartsValidator()

  data = {
    "quantity": "uno", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_cart_admin(data)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_cart_admin_with_invalid_price_raises_error():
  validator = CartsValidator()

  data = {
    "price": "uno", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_cart_admin(data)

  assert str(exc_info.value) == "Invalid operator"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_create_invoice_with_valid_data_returns_dict():
  validator = CartsValidator()

  data = {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }

  result = validator.validate_create_invoice(data)

  assert result == {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }
  assert isinstance(result, dict)


def test_validate_create_invoice_missing_payment_method_raises_error():
  validator = CartsValidator()

  data = {
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_create_invoice(data)

  assert str(exc_info.value) == "Missing field: payment_method"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_create_invoice_missing_shipping_address_raises_error():
  validator = CartsValidator()

  data = {
    "payment_method": "sinpe",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_create_invoice(data)

  assert str(exc_info.value) == "Missing field: shipping_address"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_create_invoice_with_extra_field_raises_error():
  validator = CartsValidator()

  data = {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
    "random": "123"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_create_invoice(data)

  assert str(exc_info.value) == "Invalid field: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_create_invoice_with_non_dict_shipping_address_raises_error():
  validator = CartsValidator()

  data = {
    "payment_method": "sinpe",
    "shipping_address": 1,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_create_invoice(data)

  assert str(exc_info.value) == "shipping_address must be an object/dict"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_create_invoice_with_invalid_payment_method_raises_error():
  validator = CartsValidator()

  data = {
    "payment_method": "bitcoin",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_create_invoice(data)

  assert str(exc_info.value) == "Invalid method"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_create_invoice_with_invalid_shipping_address_field_raises_error():
  validator = CartsValidator()

  data = {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": 1,
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    },
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_create_invoice(data)

  assert str(exc_info.value) == "street must be a non-empty string"
  assert isinstance(exc_info.value, ValidationError)