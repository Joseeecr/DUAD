import pytest
from app.validators.products_validators import ProductsValidator
from app.exceptions.exceptions import ValidationError
from decimal import Decimal

def test_validate_is_number_with_int():
  validator = ProductsValidator()
  value = 5

  result = validator.validate_is_number(value)

  assert result == 5
  assert isinstance(result, int)


def test_validate_is_number_with_numeric_string():
  validator = ProductsValidator()
  value = "42"

  result = validator.validate_is_number(value)

  assert result == 42
  assert isinstance(result, int)


def test_validate_is_number_raises_error_with_non_numeric_string():
  validator = ProductsValidator()
  value = "four"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_is_number(value)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_is_number_raises_error_with_empty_string():
  validator = ProductsValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_is_number(value)

  assert str(exc_info.value) == "Only numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_is_number_with_negative_number():
  validator = ProductsValidator()
  value = "-5"

  result = validator.validate_is_number(value)

  assert result == -5
  assert isinstance(result, int)


def test_validate_product_name_accepts_valid_name():
  validator = ProductsValidator()
  value = "Apple Juice"

  result = validator.validate_product_name(value)

  assert result == "Apple Juice"
  assert isinstance(result, str)

def test_validate_product_name_accepts_spanish_accents():
  validator = ProductsValidator()
  value = "Café"

  result = validator.validate_product_name(value)

  assert result == "Café"
  assert isinstance(result, str)

def test_validate_product_name_accepts_unicode_letters():
  validator = ProductsValidator()
  value = "اسم"

  result = validator.validate_product_name(value)

  assert result == "اسم"
  assert isinstance(result, str)


def test_validate_product_name_raises_error_if_only_numbers():
  validator = ProductsValidator()
  value = "12345"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_product_name(value)

  assert str(exc_info.value) == "Invalid name"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_product_name_raises_error_if_only_spaces():
  validator = ProductsValidator()
  value = " "

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_product_name(value)

  assert str(exc_info.value) == "Invalid name"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_product_name_raises_error_if_empty_string():
  validator = ProductsValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_product_name(value)

  assert str(exc_info.value) == "Invalid name"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_product_name_accepts_name_with_letters_and_numbers():
  validator = ProductsValidator()
  value = "Apple Juice 1L"

  result = validator.validate_product_name(value)

  assert result == "Apple Juice 1L"
  assert isinstance(result, str)


def test_validate_product_name_raises_error_if_special_characters():
  validator = ProductsValidator()
  value = "Apple Juice 1L!"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_product_name(value)

  assert str(exc_info.value) == "Invalid name"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_price_with_integer():
  validator = ProductsValidator()
  value = 3
  result = validator.validate_price(value)

  assert result == Decimal(str(value))
  assert isinstance(result, Decimal)


def test_validate_price_with_float_two_decimals():
  validator = ProductsValidator()
  value = 3.99

  result = validator.validate_price(value)

  assert result == Decimal(str(value))
  assert isinstance(result, Decimal)


def test_validate_price_with_string_number():
  validator = ProductsValidator()
  value = "3.99"

  result = validator.validate_price(value)

  assert result == Decimal(str(value))
  assert isinstance(result, Decimal)


def test_validate_price_raises_error_more_than_two_decimals():
  validator = ProductsValidator()
  value = 3.999

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_price(value)

  assert str(exc_info.value) == "Only two decimals are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_price_raises_error_invalid_string():
  validator = ProductsValidator()
  value = "abcd"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_price(value)

  assert str(exc_info.value) == "Invalid operator"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_price_with_price_zero():
  validator = ProductsValidator()
  value = 0.99

  result = validator.validate_price(value)

  assert result == Decimal(str(value))
  assert isinstance(result, Decimal)


def test_validate_price_with_spaces():
  validator = ProductsValidator()
  value = "  0.99  "

  result = validator.validate_price(value)

  assert result == Decimal(str(value))
  assert isinstance(result, Decimal)


def test_validate_price_raises_error_invalid_negative_numbers():
  validator = ProductsValidator()
  value = -10.99

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_price(value)

  assert str(exc_info.value) == "Only positive numbers are allowed"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_sku_correct_format():
  validator = ProductsValidator()
  value = "ABCD1234"

  result = validator.validate_sku(value)

  assert result == "ABCD1234"
  assert isinstance(result, str)


def test_validate_sku_incorrect_letters_raises_validate_error():
  validator = ProductsValidator()
  value = "abcd1234"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_sku(value)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_sku_incorrect_numbers_raises_validate_error():
  validator = ProductsValidator()
  value = "ABCDonetwothreefour"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_sku(value)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_sku_too_short_raises_validate_error():
  validator = ProductsValidator()
  value = "AB12"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_sku(value)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_sku_too_long_raises_validate_error():
  validator = ProductsValidator()
  value = "ABCDEFG123456789"

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_sku(value)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_sku_empty_string_raises_validate_error():
  validator = ProductsValidator()
  value = ""

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_sku(value)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_sku_with_spaces_only_raises_validate_error():
  validator = ProductsValidator()
  value = " "

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_sku(value)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_all_keys_valid():
  validator = ProductsValidator()

  data = {
    "name": "Manzana",
    "price": "12.50",
    "sku": "ABCD1234",
    "category_id": "5",
    "stock": 100
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "name": "Manzana",
    "price":Decimal("12.50"),
    "sku": "ABCD1234",
    "category_id": 5,
    "stock": 100
  }
  assert isinstance(result, dict)


def test_validate_dict_data_partial_keys():
  validator = ProductsValidator()

  data = {
    "name": "Manzana",
    "price": "12.50"
  }

  result = validator._validate_dict_data(data)

  assert result == {
    "name": "Manzana",
    "price":Decimal("12.50"),
  }
  assert isinstance(result, dict)


def test_validate_dict_data_unknown_key():
  validator = ProductsValidator()

  data = {"random": "Gabriel"}

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "No validation method for key: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_dict_data_empty_dict():
  validator = ProductsValidator()

  data = {}

  result = validator._validate_dict_data(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_dict_data_some_keys_invalid():
  validator = ProductsValidator()

  data = {
    "name": "Manzana",
    "price": "12.50",
    "sku": 12345,
    "category_id": "5",
    "stock": 100
  }

  with pytest.raises(ValidationError) as exc_info:
    validator._validate_dict_data(data)

  assert str(exc_info.value) == "Incorrect SKU structure"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_all_valid_keys():
  validator = ProductsValidator()

  data = {
    "id": "1", 
    "name": "Manzana", 
    "price": "2.99", 
    "sku":"ANSC1234", 
    "category_id" : "1",
    "stock" : "100"
  }

  result = validator.validate_filters(data)

  assert result == {
    "id": 1, 
    "name": "Manzana", 
    "price": Decimal("2.99"), 
    "sku":"ANSC1234", 
    "category_id" : 1,
    "stock" : 100
  }
  assert isinstance(result, dict)


def test_validate_filters_with_unknown_key():
  validator = ProductsValidator()

  data = {
    "id": "1", 
    "name": "Manzana", 
    "price": "2.99", 
    "random": 1,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Unknown query parameter: 'random'"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_filters_partial_valid_keys():
  validator = ProductsValidator()

  data = { 
    "price": "2.99",
    "category_id": "1" 
  }

  result = validator.validate_filters(data)

  assert result == { 
    "price": Decimal("2.99"), 
    "category_id": 1
  }
  assert isinstance(result, dict)


def test_validate_filters_empty_params():
  validator = ProductsValidator()

  data = {}

  result = validator.validate_filters(data)

  assert result == {}
  assert isinstance(result, dict)


def test_validate_filters_invalid_value_type():
  validator = ProductsValidator()

  data = {
    "id": "1", 
    "name": "Manzana", 
    "price": "asdfadfasd",
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_filters(data)

  assert str(exc_info.value) == "Invalid operator"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_all_required_keys_present():
  validator = ProductsValidator()

  data = {
    "name": "Manzana", 
    "price": "2.99", 
    "category_id": 1,
    "stock": 100
  }

  result = validator.validate_insert_products(data)

  assert result == {
    "name": "Manzana", 
    "price": Decimal("2.99"), 
    "category_id" : 1,
    "stock" : 100
  }
  assert isinstance(result, dict)


def test_validate_insert_products_missing_required_key():
  validator = ProductsValidator()

  data = {
    "price": "2.99", 
    "category_id" :1,
    "stock" : 100,
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_products(data)

  assert str(exc_info.value) == "Missing field: name"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_with_extra_key():
  validator = ProductsValidator()

  data = {
    "name": "Manzana",
    "price": "2.99", 
    "category_id" :1,
    "stock" : 100,
    "random": "deaa"
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_insert_products(data)

  assert str(exc_info.value) == "Invalid field: random"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_insert_products_validates_values():
  validator = ProductsValidator()

  data = {
    "name": "Manzana", 
    "price": "2.99", 
    "category_id" : "1",
    "stock" : "100"
  }

  result = validator.validate_insert_products(data)

  assert result == {
    "name": "Manzana", 
    "price": Decimal("2.99"), 
    "category_id" : 1,
    "stock" : 100
  }
  assert isinstance(result, dict)


def test_validate_update_products_with_valid_keys():
  validator = ProductsValidator()

  data = {
    "name": "Manzana", 
    "price": "2.99", 
  }

  result = validator.validate_update_products(data)

  assert result == {
    "name": "Manzana", 
    "price": Decimal("2.99"), 
  }
  assert isinstance(result, dict)


def test_validate_update_products_with_invalid_key():
  validator = ProductsValidator()

  data = {
    "random": "Manzana", 
    "price": "2.99", 
  }

  with pytest.raises(ValidationError) as exc_info:
    validator.validate_update_products(data)

  assert str(exc_info.value) == "Invalid"
  assert isinstance(exc_info.value, ValidationError)


def test_validate_update_products_validates_values():
  validator = ProductsValidator()

  data = {
    "price": "2.99", 
    "category_id" : "1",
    "stock" : "100"
  }

  result = validator.validate_update_products(data)

  assert result == { 
    "price": Decimal("2.99"), 
    "category_id" : 1,
    "stock" : 100
  }
  assert isinstance(result, dict)