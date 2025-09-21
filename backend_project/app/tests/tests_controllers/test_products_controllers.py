from flask import Flask
from app.exceptions.exceptions import NotFoundError, ValidationError
import pytest

def test_get_products_returns_products_successfully(products_controller, service_mock):

  service_mock.list_products.return_value = [
    {"id": 1, "name": "Manzana", "price": 12.5}
  ]

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = products_controller.get_products()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "name": "Manzana", "price": 12.5}]
  service_mock.list_products.assert_called_once_with({"name": "Manzana"})


def test_get_products_raises_validation_error(products_controller, service_mock):
  service_mock.list_products.side_effect = ValidationError("Invalid parameters")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = products_controller.get_products()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid parameters"}
  service_mock.list_products.assert_called_once_with({"name": "Manzana"})


def test_get_products_raises_not_found_error(products_controller, service_mock):
  service_mock.list_products.side_effect = NotFoundError("No matching products found.")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = products_controller.get_products()
  
  assert status_code == 404
  assert response.get_json() == {"error": "No matching products found."}
  service_mock.list_products.assert_called_once_with({"name": "Manzana"})


def test_get_products_raises_generic_exception(products_controller, service_mock):
  service_mock.list_products.side_effect = Exception("Internal server error")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = products_controller.get_products()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal server error"}
  service_mock.list_products.assert_called_once_with({"name": "Manzana"})


def test_get_product_id_returns_product_successfully(products_controller, service_mock):
  service_mock.get_product_by_id.return_value = {"id": 1, "name": "Manzana", "price": 12.5}

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = products_controller.get_product_id(1)

  assert status_code == 200
  assert response.get_json() == {"id": 1, "name": "Manzana", "price": 12.5}
  service_mock.get_product_by_id.assert_called_once_with(1)


def test_get_product_id_raises_not_found_error(products_controller, service_mock):
  service_mock.get_product_by_id.side_effect = NotFoundError("Product not found")

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = products_controller.get_product_id(1)
  
  assert status_code == 404
  assert response.get_json() == {"error": "Product not found"}
  service_mock.get_product_by_id.assert_called_once_with(1)


def test_get_product_id_raises_generic_exception(products_controller, service_mock):
  service_mock.get_product_by_id.side_effect = Exception("Internal server error")

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = products_controller.get_product_id(1)
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal server error"}
  service_mock.get_product_by_id.assert_called_once_with(1)


def test_post_product_inserts_product_successfully(products_controller, service_mock):
  data = {
      "name": "Juguete Hueso para morder",
      "price": 2.50,
      "sku": "ABCD1234",
      "stock": "5",
      "category_id": 7
  }

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = products_controller.post_product()
  
  assert status_code == 201
  assert response.get_json() == {"success": "new product added"}
  service_mock.insert_product.assert_called_once_with(data)


def test_post_product_raises_validation_error(products_controller, service_mock):
  service_mock.insert_product.side_effect = ValidationError("Invalid product data")
  data = {"name": "Juguete Hueso para morder", "price": 2.50}
  app = Flask(__name__)

  with app.test_request_context("/", method="POST", json=data):
    response, status_code = products_controller.post_product()

  assert status_code == 400
  assert response.get_json() == {"error": "Invalid product data"}
  service_mock.insert_product.assert_called_once_with(data)


def test_post_product_raises_generic_exception(products_controller, service_mock):
  service_mock.insert_product.side_effect = Exception("Unexpected error")

  data = {"name": "Juguete Hueso para morder", "price": 2.50}

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = products_controller.post_product()

  assert status_code == 500
  assert response.get_json() == {"error": "Unexpected error"}
  service_mock.insert_product.assert_called_once_with(data)


def test_update_by_admin_successfully(products_controller, service_mock):
  data = {"name": "Nuevo Nombre", "price": 15.5}
  
  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = products_controller.update_by_admin(1)

  assert status_code == 200
  assert response.get_json() == {"message": "product successfully updated"}
  service_mock.update_product_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_validation_error(products_controller, service_mock):
  service_mock.update_product_by_admin.side_effect = ValidationError("Invalid data")
  data = {"name": "", "price": -5}

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = products_controller.update_by_admin(1)

  assert status_code == 422
  assert response.get_json() == {"error": "Invalid data"}
  service_mock.update_product_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_value_error(products_controller, service_mock):
  service_mock.update_product_by_admin.side_effect = ValueError("Product not found")
  data = {"name": "Nuevo Nombre"}

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = products_controller.update_by_admin(1)

  assert status_code == 404
  assert response.get_json() == {"error": "Product not found"}
  service_mock.update_product_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_generic_exception(products_controller, service_mock):
  service_mock.update_product_by_admin.side_effect = Exception("Unexpected error")
  data = {"name": "Nuevo Nombre"}

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = products_controller.update_by_admin(1)

  assert status_code == 500
  assert response.get_json() == {"error": "Unexpected error"}
  service_mock.update_product_by_admin.assert_called_once_with(1, data)


def test_delete_product_successfully(products_controller, service_mock):
  app = Flask(__name__)
  with app.test_request_context("/", method="DELETE"):
    response, status_code = products_controller.delete_product(1)

  assert status_code == 204
  assert response.get_json() is None
  service_mock.delete_product.assert_called_once_with(1)


def test_delete_product_raises_value_error(products_controller, service_mock):
  service_mock.delete_product.side_effect = ValueError("Product not found")

  app = Flask(__name__)
  with app.test_request_context("/", method="DELETE"):
    response, status_code = products_controller.delete_product(1)

  assert status_code == 404
  assert response.get_json() == {"error": "Product not found"}
  service_mock.delete_product.assert_called_once_with(1)
