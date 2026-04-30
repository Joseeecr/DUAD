from flask import Flask
from app.exceptions.exceptions import NotFoundError, ValidationError

def test_get_user_returns_users_successfully(user_controller, service_mock):

  service_mock.list_users.return_value = [
    {"id": 1, "name": "Jose", "last_name": "Blanco", "email":"useremail@example.com"}
  ]

  app = Flask(__name__)
  with app.test_request_context("/?name=Jose"):
    response, status_code = user_controller.get_user()

  assert status_code == 200
  assert response.get_json() == [{"id": 1, "name": "Jose", "last_name": "Blanco", "email":"useremail@example.com"}]
  service_mock.list_users.assert_called_once_with({"name": "Jose"})


def test_get_user_raises_validation_error(user_controller, service_mock):
  service_mock.list_users.side_effect = ValidationError("Invalid parameters")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = user_controller.get_user()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid parameters"}
  service_mock.list_users.assert_called_once_with({"name": "Manzana"})


def test_get_user_raises_not_found_error(user_controller, service_mock):
  service_mock.list_users.side_effect = NotFoundError("No matching users found.")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = user_controller.get_user()
  
  assert status_code == 404
  assert response.get_json() == {"error": "No matching users found."}
  service_mock.list_users.assert_called_once_with({"name": "Manzana"})


def test_get_user_raises_generic_exception(user_controller, service_mock):
  service_mock.list_users.side_effect = Exception("Internal server error")

  app = Flask(__name__)
  with app.test_request_context("/?name=Manzana"):
    response, status_code = user_controller.get_user()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal server error"}
  service_mock.list_users.assert_called_once_with({"name": "Manzana"})


def test_register_successfully(user_controller, service_mock):
  data = {
    "name": "user",
    "last_name": "users",
    "email": "user@example.com",
  }

  service_mock.insert_user.return_value = "mocked_token"

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = user_controller.register()
  
  assert status_code == 201
  assert response.get_json() == {"token": "mocked_token"}
  service_mock.insert_user.assert_called_once_with(data)


def test_register_raises_validation_error(user_controller, service_mock):
  service_mock.insert_user.side_effect = ValidationError("Invalid data")
  data = {"name": "Jose"}

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = user_controller.register()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Invalid data"}
  service_mock.insert_user.assert_called_once_with({"name": "Jose"})


def test_register_raises_generic_exception(user_controller, service_mock):
  service_mock.insert_user.side_effect = Exception("Internal Server error")
  data = {"name": "Jose"}

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = user_controller.register()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server error"}
  service_mock.insert_user.assert_called_once_with({"name": "Jose"})


def test_login_successfully(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  service_mock.login_user.return_value = "mocked_token"

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = user_controller.login()
  
  assert status_code == 200
  assert response.get_json() == {"token": "mocked_token"}
  service_mock.login_user.assert_called_once_with(data.get("email"), data.get("password"))


def test_login_raises_value_error(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  service_mock.login_user.side_effect = ValueError("Incorrect email or password")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = user_controller.login()
  
  assert status_code == 400
  assert response.get_json() == {"error": "Incorrect email or password"}
  service_mock.login_user.assert_called_once_with(data.get("email"), data.get("password"))


def test_login_raises_generic_exception(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  service_mock.login_user.side_effect = Exception("Internal Server error")

  app = Flask(__name__)
  with app.test_request_context("/", method="POST", json=data):
    response, status_code = user_controller.login()
  
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server error"}
  service_mock.login_user.assert_called_once_with(data.get("email"), data.get("password"))


def test_me_returns_user_info_successfully(user_controller, service_mock, jwt_manager_mock):
  jwt_manager_mock.decode.return_value = {"id": 1}

  service_mock.get_user_by_id.return_value = {"name": "User", "is_admin": True}

  app = Flask(__name__)
  with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
    response, status_code = user_controller.me()

  assert status_code == 200
  assert response.get_json() == {"id": 1, "name": "User", "is_admin": True}
  service_mock.get_user_by_id.assert_called_once_with(1)

def test_me_returns_403_when_no_token_provided(user_controller):

  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = user_controller.me()
  
  assert status_code == 403
  assert response.get_json() == {"error": "Forbidden"}


def test_me_raises_generic_exception(user_controller, service_mock, jwt_manager_mock):
  jwt_manager_mock.decode.side_effect = Exception("Internal Server error")

  app = Flask(__name__)
  with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
    response, status_code = user_controller.me()

  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server error"}
  service_mock.get_user_by_id.assert_not_called()


def test_update_by_admin_updates_user_successfully(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = user_controller.update_by_admin(1)
  
  assert status_code == 200
  assert response.get_json() == {"message": "User successfully updated"}
  service_mock.update_user_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_validation_error(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  service_mock.update_user_by_admin.side_effect = ValidationError("Invalid payload")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = user_controller.update_by_admin(1)
  assert status_code == 422
  assert response.get_json() == {"error": "Invalid payload"}
  service_mock.update_user_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_value_error(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  service_mock.update_user_by_admin.side_effect = NotFoundError("Not found")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = user_controller.update_by_admin(1)
  assert status_code == 404
  assert response.get_json() == {"error": "Not found"}
  service_mock.update_user_by_admin.assert_called_once_with(1, data)


def test_update_by_admin_raises_generic_exception(user_controller, service_mock):
  data = {
    "email": "user@example.com",
    "password": "userpass123",
  }

  service_mock.update_user_by_admin.side_effect = Exception("Internal Server Error")

  app = Flask(__name__)
  with app.test_request_context("/", method="PATCH", json=data):
    response, status_code = user_controller.update_by_admin(1)
  assert status_code == 500
  assert response.get_json() == {"error": "Internal Server Error"}
  service_mock.update_user_by_admin.assert_called_once_with(1, data)


def test_delete_user_successfully(user_controller, service_mock):
  app = Flask(__name__)
  with app.test_request_context("/", method="DELETE"):
    response, status_code = user_controller.delete(1)
  
  assert status_code == 204
  assert response.get_json() is None
  service_mock.delete_user.assert_called_once_with(1)


def test_delete_user_raises_value_error(user_controller, service_mock):
  service_mock.delete_user.side_effect = NotFoundError("Not found")

  app = Flask(__name__)
  with app.test_request_context("/", method="DELETE"):
    response, status_code = user_controller.delete(1)

  assert status_code == 404
  assert response.get_json() == {"error": "Not found"}
  service_mock.update_user_by_admin.delete_user(1)
