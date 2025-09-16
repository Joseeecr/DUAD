from unittest.mock import Mock
from app.exceptions.exceptions import NotFoundError, ValidationError
import pytest
from types import SimpleNamespace
from unittest.mock import ANY

def test_list_carts_returns_all_carts_when_no_filters(cart_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {}

  repo_mock.get_carts.return_value = [
      Mock(_mapping={"id": 1, "user_id": 1, "status": "active"}),
  ]

  result = cart_service.list_carts({})

  assert result== [{"id": 1, "user_id": 1, "status": "active"}]
  validator_mock.validate_filters.assert_called_once_with({})
  repo_mock.get_carts.assert_called_once()


def test_list_carts_returns_filtered_carts_when_valid_filters_provided(cart_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"user_id": 1,"status": "active"}

  repo_mock.get_carts.return_value = [
      Mock(_mapping={"id": 1, "user_id": 1, "status": "active"}),
  ]

  result = cart_service.list_carts({"user_id": 1,"status": "active"})

  assert result[0]["user_id"] == 1
  validator_mock.validate_filters.assert_called_once_with({"user_id": 1,"status": "active"})
  repo_mock.get_carts.assert_called_once()


def test_list_carts_raises_not_found_error_when_no_carts_match(cart_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"user_id": 1000}
  repo_mock.get_carts.return_value = []

  with pytest.raises(NotFoundError) as exc_info:   
    cart_service.list_carts({"user_id": 1000})

  assert str(exc_info.value) == "No matching carts found."
  validator_mock.validate_filters.assert_called_once_with({"user_id": 1000})
  repo_mock.get_carts.assert_called_once()


def test_list_carts_raises_validation_error_when_filters_invalid(cart_service, validator_mock, repo_mock):
  validator_mock.validate_filters.side_effect = ValidationError("Invalid filters")

  with pytest.raises(ValidationError) as exc_info:   
    cart_service.list_carts({"random_key": 1, "user_id": "uno", "status": "unknown"})

  assert str(exc_info.value) == "Invalid filters"
  validator_mock.validate_filters.assert_called_once_with({"random_key": 1, "user_id": "uno", "status": "unknown"})
  repo_mock.get_carts.assert_not_called()


def test_list_carts_propagates_exception_when_repo_fails(cart_service, validator_mock, repo_mock):
  validator_mock.validate_filters.return_value = {"user_id": 1,"status": "active"}

  repo_mock.get_carts.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    cart_service.list_carts({"user_id": 1,"status": "active"})

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_filters.assert_called_once_with({"user_id": 1,"status": "active"})
  repo_mock.get_carts.assert_called_once()


def test_add_product_to_cart_adds_new_product_when_not_in_cart(cart_service, validator_mock, repo_mock):
  raw_payload = {"product_id": "1", "quantity": "1"}
  validated_payload = {"product_id": 1, "quantity": 1}

  repo_mock.get_cart_id_by_user.return_value = 1

  validator_mock.validate_insert_products_to_cart.return_value = validated_payload

  repo_mock.get_product_by_id.return_value = SimpleNamespace(
    id=1, name="Pelota", price=10.0
  )

  repo_mock.get_cart_product_entry.return_value = None

  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.return_value = "Inserted"

  result = cart_service.add_product_to_cart(user_id=1, data=raw_payload)

  assert result == "Inserted"
  validator_mock.validate_insert_products_to_cart.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  repo_mock.get_product_by_id.assert_called_once_with(ANY, 1)
  repo_mock.get_cart_product_entry.assert_called_once_with(ANY, 1, 1)
  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.assert_called_once_with(ANY, 1, 1, 1, 10.0)


def test_add_product_to_cart_updates_quantity_when_product_already_in_cart(cart_service, validator_mock, repo_mock):
  raw_payload = {"product_id": "1", "quantity": "1"}
  validated_payload = {"product_id": 1, "quantity": 1}

  repo_mock.get_cart_id_by_user.return_value = 1

  validator_mock.validate_insert_products_to_cart.return_value = validated_payload

  repo_mock.get_product_by_id.return_value = SimpleNamespace(
    id=1, name="Pelota", price=10.0
  )

  repo_mock.get_cart_product_entry.return_value = 1

  repo_mock.update_quantity_if_cart_product_already_exists.return_value = "Updated"

  result = cart_service.add_product_to_cart(user_id=1, data=raw_payload)

  assert result == "Updated"
  validator_mock.validate_insert_products_to_cart.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  repo_mock.get_product_by_id.assert_called_once_with(ANY, 1)
  repo_mock.get_cart_product_entry.assert_called_once_with(ANY, 1, 1)
  repo_mock.update_quantity_if_cart_product_already_exists.assert_called_once_with(ANY, 1, 1, 1, 1)


def test_add_product_to_cart_creates_cart_if_none_exists(cart_service, validator_mock, repo_mock):
  raw_payload = {"product_id": "1", "quantity": "1"}
  validated_payload = {"product_id": 1, "quantity": 1}

  repo_mock.get_cart_id_by_user.return_value = None

  validator_mock.validate_insert_products_to_cart.return_value = validated_payload

  repo_mock.get_product_by_id.return_value = SimpleNamespace(
    id=1, name="Pelota", price=10.0
  )

  repo_mock.insert_cart_if_needed.return_value = 1
  repo_mock.get_cart_product_entry.return_value = None

  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.return_value = "Inserted"

  result = cart_service.add_product_to_cart(user_id=1, data=raw_payload)

  assert result == "Inserted"
  validator_mock.validate_insert_products_to_cart.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  repo_mock.get_product_by_id.assert_called_once_with(ANY, 1)
  repo_mock.get_cart_product_entry.assert_called_once_with(ANY, 1, 1)
  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.assert_called_once_with(ANY, 1, 1, 1, 10.0)


def test_add_product_to_cart_raises_not_found_error_when_product_not_found(cart_service, validator_mock, repo_mock):
  raw_payload = {"product_id": "1000", "quantity": "1"}
  validated_payload = {"product_id": 1000, "quantity": 1}

  repo_mock.get_cart_id_by_user.return_value = 1

  validator_mock.validate_insert_products_to_cart.return_value = validated_payload

  repo_mock.get_product_by_id.return_value = None

  with pytest.raises(NotFoundError) as exc_info:   
    cart_service.add_product_to_cart(1, raw_payload)

  assert str(exc_info.value) == "Product not found."
  validator_mock.validate_insert_products_to_cart.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  repo_mock.get_product_by_id.assert_called_once_with(ANY, 1000)
  repo_mock.insert_cart_if_needed.assert_not_called()
  repo_mock.get_cart_product_entry.assert_not_called()
  repo_mock.update_quantity_if_cart_product_already_exists.assert_not_called()
  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.assert_not_called()


def test_add_product_to_cart_propagates_exception_when_validator_fails(cart_service, validator_mock, repo_mock):
  raw_payload = {"random_field": "zzz", "quantity": "1"}

  repo_mock.get_cart_id_by_user.return_value = 1

  validator_mock.validate_insert_products_to_cart.side_effect = ValidationError("Invalid payload")

  with pytest.raises(ValidationError) as exc_info:   
    cart_service.add_product_to_cart(1, raw_payload)

  assert str(exc_info.value) == "Invalid payload"
  validator_mock.validate_insert_products_to_cart.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  repo_mock.get_product_by_id.assert_not_called()
  repo_mock.insert_cart_if_needed.assert_not_called()
  repo_mock.get_cart_product_entry.assert_not_called()
  repo_mock.update_quantity_if_cart_product_already_exists.assert_not_called()
  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.assert_not_called()


def test_add_product_to_cart_propagates_exception_when_repo_fails(cart_service, validator_mock, repo_mock):
  raw_payload = {"product_id": "1000", "quantity": "1"}

  repo_mock.get_cart_id_by_user.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    cart_service.add_product_to_cart(1, raw_payload)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  validator_mock.validate_insert_products_to_cart.assert_not_called()
  repo_mock.get_product_by_id.assert_not_called()
  repo_mock.insert_cart_if_needed.assert_not_called()
  repo_mock.get_cart_product_entry.assert_not_called()
  repo_mock.update_quantity_if_cart_product_already_exists.assert_not_called()
  repo_mock.add_data_to_cart_if_cart_product_doesnt_exist.assert_not_called()


def test_get_or_create_address_returns_existing_address_when_found(cart_service, repo_mock):
  location = {
    "city": "San Jose",
    "country": "Costa Rica"
  }

  repo_mock.get_existing_address.return_value = 1

  result = cart_service.get_or_create_address(ANY, location)

  assert result == 1
  repo_mock.get_existing_address.assert_called_once_with(ANY, location)
  repo_mock.insert_address_if_needed.assert_not_called()


def test_get_or_create_address_inserts_new_address_when_not_found(cart_service, repo_mock):
  location = {
    "city": "San Jose",
    "country": "Costa Rica"
  }

  repo_mock.get_existing_address.return_value = None

  repo_mock.insert_address_if_needed.return_value = 2

  result = cart_service.get_or_create_address(ANY, location)

  assert result == 2
  repo_mock.insert_address_if_needed.assert_called_once_with(ANY, location)
  repo_mock.get_existing_address.assert_called_once_with(ANY, location)


def test_checkout_cart_creates_invoice_successfully(cart_service, validator_mock, repo_mock, mocker):
  raw_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validated_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validator_mock.validate_create_invoice.return_value = validated_payload

  mocker.patch.object(cart_service, "get_or_create_address", return_value=10)

  repo_mock.get_cart_id_by_user.return_value = 1

  fake_item = mocker.MagicMock()
  fake_item.product_id = 1
  fake_item.quantity = 2
  fake_item.price = 5.0
  session_mock = mocker.MagicMock()
  session_mock.execute().fetchall.return_value = [fake_item]

  fake_product = mocker.MagicMock()
  fake_product.stock = 10
  session_mock.execute().fetchone.return_value = fake_product

  repo_mock.get_payment_method.return_value = 1

  session_mock.execute().scalar_one.return_value = 12345

  mocker.patch("app.services.cart_services.SessionLocal", return_value=mocker.MagicMock(__enter__=lambda s: session_mock, __exit__=lambda *a: None))

  result = cart_service.checkout_cart(user_id=1, data=raw_payload)

  assert result == 12345
  validator_mock.validate_create_invoice.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(session_mock, 1)
  repo_mock.get_payment_method.assert_called_once_with(session_mock, "card")
  cart_service.get_or_create_address.assert_called_once_with(session_mock, {"street": "Main"})


def test_checkout_cart_raises_not_found_error_when_cart_does_not_exist(cart_service, validator_mock, repo_mock, mocker):
  raw_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validated_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validator_mock.validate_create_invoice.return_value = validated_payload

  mocker.patch.object(cart_service, "get_or_create_address", return_value=10)

  repo_mock.get_cart_id_by_user.return_value = None

  with pytest.raises(NotFoundError) as exc_info:   
    cart_service.checkout_cart(1, raw_payload)

  assert str(exc_info.value) == "Not found."
  validator_mock.validate_create_invoice.assert_called_once_with(raw_payload)
  cart_service.get_or_create_address.assert_called_once_with(ANY, {"street": "Main"})
  repo_mock.get_payment_method.assert_not_called()
  session_patch = mocker.patch("app.services.cart_services.SessionLocal", return_value=mocker.MagicMock())
  session_patch.assert_not_called()


def test_checkout_cart_raises_exception_when_product_not_found(cart_service, validator_mock, repo_mock, mocker):

  raw_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validated_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validator_mock.validate_create_invoice.return_value = validated_payload

  mocker.patch.object(cart_service, "get_or_create_address", return_value=10)

  repo_mock.get_cart_id_by_user.return_value = 1

  fake_item = mocker.MagicMock()
  fake_item.product_id = 1
  fake_item.quantity = 2
  fake_item.price = 5.0

  session_mock = mocker.MagicMock()
  session_mock.execute().fetchall.return_value = [fake_item]

  session_mock.execute().fetchone.return_value = None

  mocker.patch(
    "app.services.cart_services.SessionLocal",
    return_value=mocker.MagicMock(
        __enter__=lambda s: session_mock,
        __exit__=lambda *a: None
    )
  )

  with pytest.raises(NotFoundError) as exc_info:
    cart_service.checkout_cart(user_id=1, data=raw_payload)

  assert str(exc_info.value) == "Product not found"


def test_checkout_cart_raises_exception_when_not_enough_stock(cart_service, validator_mock, repo_mock, mocker):
  raw_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validated_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validator_mock.validate_create_invoice.return_value = validated_payload

  mocker.patch.object(cart_service, "get_or_create_address", return_value=10)
  repo_mock.get_cart_id_by_user.return_value = 1

  fake_item = mocker.MagicMock()
  fake_item.product_id = 1
  fake_item.quantity = 5
  fake_item.price = 5.0

  session_mock = mocker.MagicMock()
  session_mock.execute().fetchall.return_value = [fake_item]
  
  fake_product = mocker.MagicMock()
  fake_product.name = "Pelota"
  fake_product.stock = 2
  session_mock.execute().fetchone.return_value = fake_product  

  mocker.patch(
    "app.services.cart_services.SessionLocal",
    return_value=mocker.MagicMock(
        __enter__=lambda s: session_mock, __exit__=lambda *a: None
    )
  )

  with pytest.raises(Exception) as exc_info:
    cart_service.checkout_cart(1, raw_payload)

  assert str(exc_info.value) == "Not enough stock for product 'Pelota'"


def test_checkout_cart_propagates_exception_when_repo_fails(cart_service, validator_mock, repo_mock, mocker):
  raw_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validated_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validator_mock.validate_create_invoice.return_value = validated_payload

  mocker.patch.object(cart_service, "get_or_create_address", return_value=10)
  repo_mock.get_cart_id_by_user.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:
    cart_service.checkout_cart(1, raw_payload)

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_create_invoice.assert_called_once_with(raw_payload)
  cart_service.get_or_create_address.assert_called_once_with(ANY, {"street": "Main"})
  repo_mock.get_cart_id_by_user.assert_called_once_with(ANY, 1)
  repo_mock.get_payment_method.assert_not_called()
  session_patch = mocker.patch("app.services.cart_services.SessionLocal", return_value=mocker.MagicMock())
  session_patch.assert_not_called()

def test_checkout_cart_updates_product_stock_when_checkout_is_successful(cart_service, validator_mock, repo_mock, mocker):
  raw_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validated_payload = {"payment_method": "card", "shipping_address": {"street": "Main"}}
  validator_mock.validate_create_invoice.return_value = validated_payload

  mocker.patch.object(cart_service, "get_or_create_address", return_value=10)
  repo_mock.get_cart_id_by_user.return_value = 1
  repo_mock.get_payment_method.return_value = 1

  fake_item = mocker.MagicMock()
  fake_item.product_id = 1
  fake_item.quantity = 2
  fake_item.price = 5.0

  session_mock = mocker.MagicMock()
  session_mock.execute().fetchall.return_value = [fake_item]

  fake_product = mocker.MagicMock()
  fake_product.stock = 10
  session_mock.execute().fetchone.return_value = fake_product

  session_mock.execute().scalar_one.return_value = 123

  mocker.patch(
      "app.services.cart_services.SessionLocal",
      return_value=mocker.MagicMock(__enter__=lambda s: session_mock, __exit__=lambda *a: None)
  )

  result = cart_service.checkout_cart(1, raw_payload)

  assert result == 123
  validator_mock.validate_create_invoice.assert_called_once_with(raw_payload)
  repo_mock.get_cart_id_by_user.assert_called_once_with(session_mock, 1)
  repo_mock.get_payment_method.assert_called_once_with(session_mock, "card")
  cart_service.get_or_create_address.assert_called_once_with(session_mock, {"street": "Main"})

  session_mock.execute.assert_any_call(
      mocker.ANY  # no verificamos el objeto Update exacto, solo que se llamó
  )

  # Verificar que se cerró el carrito
  session_mock.execute.assert_any_call(
      mocker.ANY  # idem, no importa el objeto exacto
  )