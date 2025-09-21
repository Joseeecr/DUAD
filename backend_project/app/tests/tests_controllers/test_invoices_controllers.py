from app.exceptions.exceptions import NotFoundError, ValidationError
from flask import Flask, g

def test_get_invoices_returns_invoices_successfully_whith_no_query_params(invoices_controller, service_mock):

  service_mock.list_invoices.return_value = [
    {"id": 1, "user_id": 1, "cart_id": 1}
  ]

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = invoices_controller.get_invoices()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "user_id": 1, "cart_id": 1}]
  service_mock.list_invoices.assert_called_once_with({})


def test_get_invoices_returns_carts_successfully_with_query_params(invoices_controller, service_mock):

  service_mock.list_invoices.return_value = [
    {"id": 1, "user_id": 1, "cart_id": 1}
  ]

  app = Flask(__name__)
  with app.test_request_context("/?cart_id=1"):
    response, status_code = invoices_controller.get_invoices()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "user_id": 1, "cart_id": 1}]
  service_mock.list_invoices.assert_called_once_with({"cart_id": "1"})


def test_get_invoices_raises_validation_error(invoices_controller, service_mock):
  service_mock.list_invoices.side_effect = ValidationError("Invalid parameters")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = invoices_controller.get_invoices()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid parameters"}
  service_mock.list_invoices.assert_called_once_with({"name": "Manzana"})


def test_get_invoices_raises_not_found_error(invoices_controller, service_mock):
  service_mock.list_invoices.side_effect = NotFoundError("No matching invoices found.")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = invoices_controller.get_invoices()
  
  assert status_code == 404
  assert response.get_json() == {"error": "No matching invoices found."}
  service_mock.list_invoices.assert_called_once_with({"name": "Manzana"})


def test_get_invoices_raises_generic_exception(invoices_controller, service_mock):
  service_mock.list_invoices.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = invoices_controller.get_invoices()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.list_invoices.assert_called_once_with({})


def test_check_user_invoices_returns_invoices_successfully(invoices_controller, service_mock):
  service_mock.get_user_invoices.return_value = [
    {"id": 1, "user_id": 1, "cart_id": 1}
  ]

  app = Flask(__name__)
  with app.test_request_context("/"):
    g.user_id = 1
    response, status_code = invoices_controller.check_user_invoices()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "user_id": 1, "cart_id": 1}]
  service_mock.get_user_invoices.assert_called_once_with(1)


def test_check_user_invoices_raises_not_found_error(invoices_controller, service_mock):
  service_mock.get_user_invoices.side_effect = NotFoundError("Not found")

  app = Flask(__name__)
  with app.test_request_context("/"):
    g.user_id = 1
    response, status_code = invoices_controller.check_user_invoices()
  
  assert status_code == 404
  assert response.get_json() == {"error": "Not found"}
  service_mock.get_user_invoices.assert_called_once_with(1)


def test_check_user_invoices_raises_generic_exception(invoices_controller, service_mock):
  service_mock.get_user_invoices.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/"):
    g.user_id = 1
    response, status_code = invoices_controller.check_user_invoices()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.get_user_invoices.assert_called_once_with(1)