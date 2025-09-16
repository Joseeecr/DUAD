from unittest.mock import Mock
from app.exceptions.exceptions import NotFoundError, ValidationError
import pytest

def test_list_products_returns_products_without_filters(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {}
  repo_mock.get_products.return_value = [
      Mock(_mapping={"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 5}),
  ]

  result = products_service.list_products({})

  assert result== [{"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 5}]
  validator_mock.validate_filters.assert_called_once_with({})
  repo_mock.get_products.assert_called_once()


def test_list_products_returns_products_with_one_filter(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"name": "Pelota"}

  repo_mock.get_products.return_value = [
      Mock(_mapping={"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 5}),
  ]

  result = products_service.list_products({"name": "Pelota"})

  assert result[0]["name"] == "Pelota"
  validator_mock.validate_filters.assert_called_once_with({"name": "Pelota"})
  repo_mock.get_products.assert_called_once()


def test_list_products_returns_products_with_two_filters(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"name": "Pelota", "sku":"ABC123"}

  repo_mock.get_products.return_value = [
      Mock(_mapping={"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 5}),
  ]

  result = products_service.list_products({"name": "Pelota", "sku":"ABC123"})

  assert result[0]["name"] == "Pelota"
  assert result[0]["sku"] == "ABC123"
  validator_mock.validate_filters.assert_called_once_with({"name": "Pelota", "sku":"ABC123"})
  repo_mock.get_products.assert_called_once()


def test_list_products_returns_products_with_bunch_of_filters(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"name": "Pelota", "price": "2.50", "category_id": 3, "stock": 5}

  repo_mock.get_products.return_value = [
      Mock(_mapping={"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 5}),
  ]

  result = products_service.list_products({"name": "Pelota", "price": "2.50", "category_id": 3, "stock": 5})

  assert result[0]["name"] == "Pelota"
  assert result[0]["sku"] == "ABC123"
  assert result[0]["category_id"] == 3
  assert result[0]["stock"] == 5
  validator_mock.validate_filters.assert_called_once_with({"name": "Pelota", "price": "2.50", "category_id": 3, "stock": 5})
  repo_mock.get_products.assert_called_once()


def test_list_products_with_bunch_of_filters_one_filter_with_wrong_type_raises_error(products_service, validator_mock):

  validator_mock.validate_filters.side_effect = ValueError("Only numbers allowed")

  with pytest.raises(ValueError) as exc_info:   
    products_service.list_products({"id": "hello", "name": "Pelota", "price": "2.50", "category_id": 3, "stock": 5})

  assert str(exc_info.value) == "Only numbers allowed"
  validator_mock.validate_filters.assert_called_once_with({"id": "hello", "name": "Pelota", "price": "2.50", "category_id": 3, "stock": 5})


def test_list_products_returns_products_with_zero_stock_filter(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"stock": 0}

  repo_mock.get_products.return_value = [
      Mock(_mapping={"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 0}),
  ]

  result = products_service.list_products({"stock": 0})

  assert result[0]["name"] == "Pelota"
  assert result[0]["sku"] == "ABC123"
  assert result[0]["stock"] == 0
  validator_mock.validate_filters.assert_called_once_with({"stock": 0})
  repo_mock.get_products.assert_called_once()


def test_list_products_with_filters_passing_wrong_data_type_to_filter(products_service, validator_mock):

  validator_mock.validate_filters.side_effect = ValidationError("Invalid name")

  with pytest.raises(ValidationError) as exc_info:   
    products_service.list_products({"name": 1})

  assert str(exc_info.value) == "Invalid name"
  validator_mock.validate_filters.assert_called_once_with({"name": 1})


def test_list_products_not_products_found_with_filters(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"price": "5.50"}
  repo_mock.get_products.return_value = []

  with pytest.raises(NotFoundError) as exc_info:   
    products_service.list_products({"price": "5.50"})

  assert str(exc_info.value) == "No matching products found."
  validator_mock.validate_filters.assert_called_once_with({"price": "5.50"})
  repo_mock.get_products.assert_called_once()


def test_list_products_with_non_existent_fields(products_service, validator_mock):

  validator_mock.validate_filters.side_effect = ValidationError("Unknown query parameter")

  with pytest.raises(ValidationError) as exc_info:   
    products_service.list_products({"color": "Red"})

  assert str(exc_info.value) == "Unknown query parameter"
  validator_mock.validate_filters.assert_called_once_with({"color": "Red"})


def test_list_products_raises_exception_when_repo_fails(products_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {}

  repo_mock.get_products.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:
      products_service.list_products({})

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_filters.assert_called_once_with({})
  repo_mock.get_products.assert_called_once()

def test_get_product_by_id_returns_product(products_service, repo_mock):

  repo_mock.get_product_by_id.return_value = {"id": 1, "name": "Pelota", "price": "2.50", "sku": "ABC123", "category_id": 3, "stock": 5}
  result = products_service.get_product_by_id(1)

  assert result["name"] == "Pelota"

  repo_mock.get_product_by_id.assert_called_once()


def test_get_product_by_id_raises_value_error(products_service, repo_mock):

  repo_mock.get_product_by_id.return_value = None

  with pytest.raises(ValueError) as exc_info:
    products_service.get_product_by_id(1000)

  assert str(exc_info.value) == "Product not found"

  repo_mock.get_product_by_id.assert_called_once()


def test_insert_product_converts_values_to_correct_type(products_service, validator_mock, repo_mock):
  raw_data = {
      "name": "testing",
      "price": "2.50",
      "stock": "5",
      "category_id": "7"
  }

  validated_data = {
      "name": "testing",
      "price": 2.50,
      "stock": 5,
      "category_id": 7
  }

  validator_mock.validate_insert_products.return_value = validated_data
  repo_mock.get_product_by_name.return_value = None
  repo_mock.insert_product.return_value = validated_data

  result = products_service.insert_product(raw_data)

  assert result == validated_data
  validator_mock.validate_insert_products.assert_called_once_with(raw_data)
  repo_mock.insert_product.assert_called_once_with(validated_data)


def test_insert_product_with_values_with_correct_type(products_service, validator_mock, repo_mock):
  raw_data = {
      "name": "testing",
      "price": 2.50,
      "stock": 5,
      "category_id":7
  }

  validated_data = {
      "name": "testing",
      "price": 2.50,
      "stock": 5,
      "category_id": 7
  }

  validator_mock.validate_insert_products.return_value = validated_data
  repo_mock.get_product_by_name.return_value = None
  repo_mock.insert_product.return_value = validated_data

  result = products_service.insert_product(raw_data)

  assert result == validated_data
  validator_mock.validate_insert_products.assert_called_once_with(raw_data)
  repo_mock.insert_product.assert_called_once_with(validated_data)


def test_insert_product_raises_error_if_product_already_exists(products_service, validator_mock, repo_mock):

  validated_data = {
      "name": "testing",
      "price": 2.50,
      "stock": 5,
      "category_id": 7
  }

  validator_mock.validate_insert_products.return_value = validated_data
  repo_mock.get_product_by_name.return_value = {"id": 1, "name": "testing"}

  with pytest.raises(ValidationError) as exc_info:
    products_service.insert_product(validated_data)

  assert str(exc_info.value) == "Product already in DB"
  validator_mock.validate_insert_products.assert_called_once_with(validated_data)
  repo_mock.insert_product.assert_not_called()


def test_insert_product_raises_error_if_missing_required_key(products_service, validator_mock):

  validated_data = {
      "price": 2.50,
      "stock": 5,
      "category_id": 7
  }

  validator_mock.validate_insert_products.side_effect = ValidationError("Missing field")

  with pytest.raises(ValidationError) as exc_info:
    products_service.insert_product(validated_data)

  assert str(exc_info.value) == "Missing field"
  validator_mock.validate_insert_products.assert_called_once_with(validated_data)


def test_insert_products_raises_exception_when_repo_fails(products_service, validator_mock, repo_mock):

  validated_data = {
      "price": 2.50,
      "stock": 5,
      "category_id": 7
  }

  validator_mock.validate_insert_products.return_value = validated_data
  repo_mock.get_product_by_name.return_value = None
  repo_mock.insert_product.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:
      products_service.insert_product(validated_data)

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_insert_products.assert_called_once_with(validated_data)
  repo_mock.insert_product.assert_called_once()


def test_update_product_by_admin_converts_values_to_correct_type_returns_success(products_service, validator_mock, repo_mock):
  repo_mock.get_product_by_id.return_value = {
      "id": 1,
      "name": "Pelota",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 5,
      "category_id": 3,
  }

  raw_data = {
      "name": "new_name",
      "price": "2.50",
  }

  validated_data = {
      "name": "new_name",
      "price": 2.50,
  }

  validator_mock.validate_update_products.return_value = validated_data

  updated_product = {
      "id": 1,
      "name": "new_name",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 10,
      "category_id": 3,
  }
  repo_mock.update_product.return_value = updated_product

  result = products_service.update_product_by_admin(1, raw_data)

  assert result == updated_product
  repo_mock.get_product_by_id.assert_called_once_with(1)
  validator_mock.validate_update_products.assert_called_once_with(raw_data)
  repo_mock.update_product.assert_called_once_with(1, validated_data)


def test_update_product_by_admin_raises_value_error_product_not_found(products_service, repo_mock):
  repo_mock.get_product_by_id.return_value = None
  
  with pytest.raises(ValueError) as exc_info:
    products_service.update_product_by_admin(1000, {"name":"new_name"})

  assert str(exc_info.value) == "Product not found"

  repo_mock.get_product_by_id.assert_called_once_with(1000)


def test_update_product_by_admin_raises_validation_error(products_service, repo_mock, validator_mock):
  repo_mock.get_product_by_id.return_value = {
      "id": 1,
      "name": "Pelota",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 5,
      "category_id": 3,
  }

  raw_data = {
      "not_valid_key": "1234",
  }
  validator_mock.validate_update_products.side_effect = ValidationError("Invalid")

  with pytest.raises(ValidationError) as exc_info:
    products_service.update_product_by_admin(1, raw_data)

  assert str(exc_info.value) == "Invalid"

  repo_mock.get_product_by_id.assert_called_once_with(1)
  validator_mock.validate_update_products.assert_called_once_with(raw_data)
  repo_mock.update_product.assert_not_called()


def test_insert_products_raises_exception_when_repo_fails(products_service, validator_mock, repo_mock):
  repo_mock.get_product_by_id.return_value = {
      "id": 1,
      "name": "Pelota",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 5,
      "category_id": 3,
  }

  raw_data = {
      "name": "new_name",
      "price": "2.50",
  }

  validated_data = {
      "name": "new_name",
      "price": 2.50,
  }
  validator_mock.validate_update_products.return_value = validated_data

  repo_mock.update_product.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:
      products_service.update_product_by_admin(1, raw_data)

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_update_products.assert_called_once_with(raw_data)
  repo_mock.update_product.assert_called_once()


def test_delete_product_success(products_service, repo_mock):
  repo_mock.get_product_by_id.return_value = {
      "id": 1,
      "name": "Pelota",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 5,
      "category_id": 3,
  }

  repo_mock.delete_product.return_value = 1

  result = products_service.delete_product(1)

  assert result == 1
  repo_mock.get_product_by_id.assert_called_once_with(1)
  repo_mock.delete_product.assert_called_once_with(1)


def test_delete_product_raises_value_error_if_product_not_found(products_service, repo_mock):
  repo_mock.get_product_by_id.side_effect = ValueError("Product not found")

  with pytest.raises(ValueError) as exc_info:
      products_service.delete_product(1000)

  assert str(exc_info.value) == "Product not found"
  repo_mock.get_product_by_id.assert_called_once_with(1000)
  repo_mock.delete_product.assert_not_called()


def test_delete_product_raises_exception_when_repo_fails_by_get_product_by_id(products_service, repo_mock):
  repo_mock.get_product_by_id.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:
      products_service.delete_product(1000)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_product_by_id.assert_called_once_with(1000)
  repo_mock.delete_product.assert_not_called()


def test_delete_product_raises_exception_when_repo_fails_by_delete_product(products_service, repo_mock):
  repo_mock.get_product_by_id.return_value = {
      "id": 1,
      "name": "Pelota",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 5,
      "category_id": 3,
  }

  repo_mock.delete_product.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:
    products_service.delete_product(1)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_product_by_id.assert_called_once_with(1)
  repo_mock.delete_product.assert_called_once_with(1)


def test_delete_product_raises_value_error_if_rowcount_zero(products_service, repo_mock):
  repo_mock.get_product_by_id.return_value = {
      "id": 1,
      "name": "Pelota",
      "price": 2.50,
      "sku": "ABC123",
      "stock": 5,
      "category_id": 3,
  }

  repo_mock.delete_product.return_value = 0

  with pytest.raises(ValueError) as exc_info:
    products_service.delete_product(1)

  assert str(exc_info.value) == "No rows were deleted"
  repo_mock.get_product_by_id.assert_called_once_with(1)
  repo_mock.delete_product.assert_called_once_with(1)