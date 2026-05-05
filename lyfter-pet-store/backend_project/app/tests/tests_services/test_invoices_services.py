from unittest.mock import Mock
from app.exceptions.exceptions import NotFoundError, ValidationError
import pytest


def test_list_invoices_returns_all_users_when_no_filters(invoices_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {}

  repo_mock.get_invoices.return_value = [
      Mock(_mapping={
        "id": 1, 
        "invoice_number": "7F8UAW3MSE", 
        "user_id": 1, 
        "cart_id": 2, 
        "payment_method_id": 1,
        "total": 10,
        "status": "paid",
        "shipping_address_id": 1
      }),
  ]

  result = invoices_service.list_invoices({})

  assert result== [{
    "id": 1, 
    "invoice_number": "7F8UAW3MSE", 
    "user_id": 1, 
    "cart_id": 2, 
    "payment_method_id": 1,
    "total": 10,
    "status": "paid",
    "shipping_address_id": 1
  }]
  validator_mock.validate_filters.assert_called_once_with({})
  repo_mock.get_invoices.assert_called_once()


def test_list_invoices_returns_filtered_users_when_valid_filters_provided(invoices_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"payment_method_id": 1}

  repo_mock.get_invoices.return_value = [
      Mock(_mapping={
        "id": 1, 
        "invoice_number": "7F8UAW3MSE", 
        "user_id": 1, 
        "cart_id": 2, 
        "payment_method_id": 1,
        "total": 10,
        "status": "paid",
        "shipping_address_id": 1
      }),
  ]

  result = invoices_service.list_invoices({"payment_method_id": 1})

  assert result[0]["invoice_number"] == "7F8UAW3MSE"
  validator_mock.validate_filters.assert_called_once_with({"payment_method_id": 1})
  repo_mock.get_invoices.assert_called_once()


def test_list_invoices_raises_not_found_error_when_no_invoices_match(invoices_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"user_id": 1}
  repo_mock.get_invoices.return_value = []

  with pytest.raises(NotFoundError) as exc_info:   
    invoices_service.list_invoices({"user_id": 1})

  assert str(exc_info.value) == "No matching invoices found."
  validator_mock.validate_filters.assert_called_once_with({"user_id": 1})
  repo_mock.get_invoices.assert_called_once()


def test_list_invoices_raises_validation_error_when_filters_invalid(invoices_service, validator_mock, repo_mock):
  validator_mock.validate_filters.side_effect = ValidationError("Invalid filters")

  with pytest.raises(ValidationError) as exc_info:   
    invoices_service.list_invoices({"id": "hello"})

  assert str(exc_info.value) == "Invalid filters"
  validator_mock.validate_filters.assert_called_once_with({"id": "hello"})
  repo_mock.get_invoices.assert_not_called()


def test_list_invoices_propagates_exception_when_repo_fails(invoices_service, validator_mock, repo_mock):
  validator_mock.validate_filters.return_value = {"payment_method_id": 1}

  repo_mock.get_invoices.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    invoices_service.list_invoices({"payment_method_id": 1})

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_filters.assert_called_once_with({"payment_method_id": 1})
  repo_mock.get_invoices.assert_called_once()


def test_get_user_invoices_returns_invoices_successfully(invoices_service, repo_mock):

  repo_mock.get_user_invoices.return_value = [
    {
      "id": 1, 
      "invoice_number": "7F8UAW3MSE", 
      "user_id": 1, 
      "cart_id": 2, 
      "payment_method_id": 1,
      "total": 10,
      "status": "paid",
      "shipping_address_id": 1
    }
  ]

  result = invoices_service.get_user_invoices(1)

  assert result[0]["invoice_number"] == "7F8UAW3MSE"
  repo_mock.get_user_invoices.assert_called_once_with(1)


def test_get_user_invoices_raises_not_found_error_when_no_invoices(invoices_service, repo_mock):
  repo_mock.get_user_invoices.return_value = []

  with pytest.raises(NotFoundError) as exc_info:   
    invoices_service.get_user_invoices(1)

  assert str(exc_info.value) == "Invoices for 1 not found."
  repo_mock.get_user_invoices.assert_called_once_with(1)


def test_get_user_invoices_propagates_exception_when_repo_fails(invoices_service, repo_mock):
  repo_mock.get_user_invoices.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    invoices_service.get_user_invoices(1)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_user_invoices.assert_called_once_with(1)
