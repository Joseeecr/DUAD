from flask import Flask, jsonify
from app.auth.admin_only import admin_only
from unittest.mock import patch

# Dummy endpoint protegido con el decorador
@admin_only
def protected_endpoint():
  return jsonify({"message": "ok"}), 200


def test_admin_only_returns_401_when_no_token():
  app = Flask(__name__)
  with app.test_request_context("/"):
    response, status_code = protected_endpoint()
  
  assert status_code == 401
  assert response.get_json() == {"error": "Token needed"}


def test_admin_only_returns_403_when_token_invalid():
  app = Flask(__name__)
  with patch("app.auth.admin_only.jwt_manager.decode") as decode_mock:
    decode_mock.return_value = None
    
    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()
  
  assert status_code == 403
  assert response.get_json() == {"error": "Invalid token"}


def test_admin_only_returns_403_when_user_not_admin():
  app = Flask(__name__)
  with patch("app.auth.admin_only.jwt_manager.decode") as decode_mock:
    decode_mock.return_value = {"is_admin": False}
    
    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()
  
  assert status_code == 403
  assert response.get_json() == {"error": "Forbidden"}


def test_admin_only_allows_access_when_user_is_admin():
  app = Flask(__name__)
  with patch("app.auth.admin_only.jwt_manager.decode") as decode_mock:
    decode_mock.return_value = {"is_admin": True}
    
    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code = protected_endpoint()
  
  assert status_code == 200
  assert response.get_json() == {"message": "ok"}


def test_admin_only_handles_decode_exception():
  app = Flask(__name__)
  with patch("app.auth.admin_only.jwt_manager.decode") as decode_mock:
    decode_mock.side_effect = Exception("Decode error")
    
    with app.test_request_context("/", headers={"Authorization": "Bearer fake_token"}):
      response, status_code  = protected_endpoint()
  
  assert status_code == 500

  assert response.get_json() == {"error": "Decode error"}
