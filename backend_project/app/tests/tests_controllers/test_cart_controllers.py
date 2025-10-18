from flask import Flask, g
from app.exceptions.exceptions import NotFoundError, ValidationError

def test_get_carts_returns_carts_successfully_whith_no_query_params(cart_controller, service_mock):

  service_mock.list_carts.return_value = [
    {"id": 1, "user_id": 1, "status": "active"}
  ]

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = cart_controller.get_carts()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "user_id": 1, "status": "active"}]
  service_mock.list_carts.assert_called_once_with({})


def test_get_carts_returns_carts_successfully_with_query_params(cart_controller, service_mock):

  service_mock.list_carts.return_value = [
    {"id": 1, "user_id": 1, "status": "active"}
  ]

  app = Flask(__name__)
  with app.test_request_context("/?status=active"):
    response, status_code = cart_controller.get_carts()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "user_id": 1, "status": "active"}]
  service_mock.list_carts.assert_called_once_with({"status": "active"})


def test_get_carts_raises_validation_error(cart_controller, service_mock):
  service_mock.list_carts.side_effect = ValidationError("Invalid parameters")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = cart_controller.get_carts()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid parameters"}
  service_mock.list_carts.assert_called_once_with({"name": "Manzana"})


def test_get_carts_raises_not_found_error(cart_controller, service_mock):
  service_mock.list_carts.side_effect = NotFoundError("No matching users found.")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = cart_controller.get_carts()
  
  assert status_code == 404
  assert response.get_json() == {"error": "No matching users found."}
  service_mock.list_carts.assert_called_once_with({"name": "Manzana"})


def test_get_carts_raises_generic_exception(cart_controller, service_mock):
  service_mock.list_carts.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = cart_controller.get_carts()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.list_carts.assert_called_once_with({})


def test_post_cart_adds_products_successfully(cart_controller, service_mock):
  data = {
    "product_id": 10,
    "quantity" : 1
  }

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.post_cart()
  
  assert status_code == 201
  assert response.get_json() == {"success": "Products added to the cart"}
  service_mock.add_product_to_cart.assert_called_once_with(1, data)


def test_post_cart_raises_validation_error(cart_controller, service_mock):
  data = {
    "user": 10,
    "quantity" : 1
  }

  service_mock.add_product_to_cart.side_effect = ValidationError("Invalid Payload")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.post_cart()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid Payload"}
  service_mock.add_product_to_cart.assert_called_once_with(1, data)


def test_post_cart_raises_not_found_error(cart_controller, service_mock):
  data = {
    "product_id": 10,
    "quantity" : 1
  }

  service_mock.add_product_to_cart.side_effect = NotFoundError("Not Found")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.post_cart()
  
  assert status_code == 404
  assert response.get_json() == {"error": "Not Found"}
  service_mock.add_product_to_cart.assert_called_once_with(1, data)


def test_post_cart_raises_generic_exception(cart_controller, service_mock):
  data = {
    "product_id": 10,
    "quantity" : 1
  }

  service_mock.add_product_to_cart.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.post_cart()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.add_product_to_cart.assert_called_once_with(1, data)


def test_update_by_admin_updates_cart_successfully(cart_controller, service_mock):
  data = {"state": "active"}

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = cart_controller.update_by_admin(1)
  
  assert status_code == 200
  assert response.get_json() == {"message": "cart successfully updated"}
  service_mock.update_cart_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_validation_error(cart_controller, service_mock):
  data = {"state": "active"}

  service_mock.update_cart_by_admin.side_effect = ValidationError("Invalid Payload")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = cart_controller.update_by_admin(1)
  
  assert status_code == 422
  assert response.get_json() == {"error": "Invalid Payload"}
  service_mock.update_cart_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_not_found_error(cart_controller, service_mock):
  data = {"state": "active"}

  service_mock.update_cart_by_admin.side_effect = NotFoundError("Not Found")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = cart_controller.update_by_admin(1000)
  
  assert status_code == 404
  assert response.get_json() == {"error": "Not Found"}
  service_mock.update_cart_by_admin.assert_called_once_with(1000, data)


def test_update_by_admin_raises_generic_exception(cart_controller, service_mock):
  data = {"state": "active"}

  service_mock.update_cart_by_admin.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = cart_controller.update_by_admin(1)
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.update_cart_by_admin.assert_called_once_with(1, data)


def test_update_carts_items_updates_products_successfully(cart_controller, service_mock):
  data = {
    "quantity": 1, 
    "product_id": 1
  }

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    g.user_id = 1
    response, status_code = cart_controller.update_carts_items()
  
  assert status_code == 200
  assert response.get_json() == {"message": "cart successfully updated"}
  service_mock.update_cart_products.assert_called_once_with(1, data)

def test_update_carts_items_raises_validation_error(cart_controller, service_mock):
  data = {
    "quantity": 1, 
    "product_id": 1
  }

  service_mock.update_cart_products.side_effect = ValidationError("Invalid Payload")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    g.user_id = 1
    response, status_code = cart_controller.update_carts_items()
  
  assert status_code == 422
  assert response.get_json() == {"error": "Invalid Payload"}
  service_mock.update_cart_products.assert_called_once_with(1, data)


def test_update_carts_items_raises_not_found_error(cart_controller, service_mock):
  data = {
    "quantity": 1, 
    "product_id": 1
  }

  service_mock.update_cart_products.side_effect = NotFoundError("Not found")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    g.user_id = 1
    response, status_code = cart_controller.update_carts_items()
  
  assert status_code == 404
  assert response.get_json() == {"error": "Not found"}
  service_mock.update_cart_products.assert_called_once_with(1, data)


def test_update_carts_items_raises_generic_exception(cart_controller, service_mock):
  data = {
    "quantity": 1, 
    "product_id": 1
  }

  service_mock.update_cart_products.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    g.user_id = 1
    response, status_code = cart_controller.update_carts_items()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.update_cart_products.assert_called_once_with(1, data)


def test_checkout_cart_creates_invoice_successfully(cart_controller, service_mock):
  data = {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    }
  }
  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.checkout_cart()
  
  assert status_code == 201
  assert response.get_json() == {"success": "invoice created"}
  service_mock.checkout_cart.assert_called_once_with(1, data)


def test_checkout_cart_raises_validation_error(cart_controller, service_mock):
  data = {
    "quantity": 1, 
    "product_id": 1
  }

  service_mock.checkout_cart.side_effect = ValidationError("Invalid Payload")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.checkout_cart()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid Payload"}
  service_mock.checkout_cart.assert_called_once_with(1, data)


def test_checkout_cart_raises_not_found_error(cart_controller, service_mock):
  data = {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    }
  }

  service_mock.checkout_cart.side_effect = NotFoundError("Not found")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.checkout_cart()
  
  assert status_code == 404
  assert response.get_json() == {"error": "Not found"}
  service_mock.checkout_cart.assert_called_once_with(1, data)



def test_checkout_cart_raises_generic_exception(cart_controller, service_mock):
  data = {
    "payment_method": "sinpe",
    "shipping_address": {
      "street": "Calle 0, Avenida Central",
      "city": "San José",
      "province": "San José",
      "zip_code": "10101",
      "country": "Costa Rica"
    }
  }

  service_mock.checkout_cart.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    g.user_id = 1
    response, status_code = cart_controller.checkout_cart()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.checkout_cart.assert_called_once_with(1, data)

