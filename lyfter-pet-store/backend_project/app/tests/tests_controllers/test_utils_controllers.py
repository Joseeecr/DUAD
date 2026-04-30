from flask import Flask, g, jsonify
from unittest.mock import patch
from app.controllers.controllers_utils import jwt_required

# Dummy endpoint protegido con el decorador
@jwt_required
def protected_endpoint():
  return jsonify({"message": f"Hello user {g.user_id}"}), 200


def test_jwt_required_returns_401_when_no_token():
  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = protected_endpoint()

  assert status_code == 401
  assert response.get_json() == {"error": "Authorization token missing"}


def test_jwt_required_returns_401_when_decode_fails():
  app = Flask(__name__)
  with patch("app.controllers.controllers_utils.jwt_required") as jwt_manager_mock:
    jwt_manager_mock.decode.side_effect = Exception("Invalid token")

    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()

  assert status_code == 401
  assert response.get_json() == {"error": "Invalid token"}


def test_jwt_required_returns_401_when_decoded_is_not_dict():
  app = Flask(__name__)
  with patch("app.controllers.controllers_utils.jwt_required") as jwt_manager_mock:
    jwt_manager_mock.decode.return_value = "not a dict"

    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()

  assert status_code == 401
  assert response.get_json() == {"error": "Invalid token"}


def test_jwt_required_returns_401_when_id_missing():
  app = Flask(__name__)
  with patch("app.controllers.controllers_utils.jwt_manager") as jwt_manager_mock:
    jwt_manager_mock.decode.return_value = {"name": "user"}

    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()

  assert status_code == 401
  assert response.get_json() == {"error": "id field missing"}


def test_jwt_required_passes_when_token_valid():
  app = Flask(__name__)
  with patch("app.controllers.controllers_utils.jwt_manager") as jwt_manager_mock:
    jwt_manager_mock.decode.return_value = {"id": 1}

    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()

  assert status_code == 200
  assert response.get_json() == {"message": "Hello user 1"}
