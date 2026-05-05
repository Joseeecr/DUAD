from unittest.mock import patch
from app.auth.jwt_instance import JWT_Manager

def test_encode_returns_token_successfully():
  manager = JWT_Manager.__new__(JWT_Manager)
  manager.private_key = "fake_private_key"
  manager.algorithm = "RS256"

  with patch("jwt.encode") as jwt_encode_mock:
    jwt_encode_mock.return_value = "fake_token"
    token = manager.encode({"id": 1})
  
  assert token == "fake_token"
  jwt_encode_mock.assert_called_once_with({"id": 1}, "fake_private_key", algorithm="RS256")


def test_encode_returns_none_on_exception():
  manager = JWT_Manager.__new__(JWT_Manager)
  manager.private_key = "fake_private_key"
  manager.algorithm = "RS256"

  with patch("jwt.encode") as jwt_encode_mock:
    jwt_encode_mock.side_effect = Exception("Encode error")
    token = manager.encode({"id": 1})
  
  assert token is None
  jwt_encode_mock.assert_called_once()


def test_decode_returns_payload_successfully():
  manager = JWT_Manager.__new__(JWT_Manager)
  manager.public_key = "fake_public_key"
  manager.algorithm = "RS256"

  with patch("jwt.decode") as jwt_decode_mock:
    jwt_decode_mock.return_value = {"id": 1}
    payload = manager.decode("fake_token")
  
  assert payload == {"id": 1}
  jwt_decode_mock.assert_called_once_with("fake_token", "fake_public_key", algorithms=["RS256"])


def test_decode_returns_none_on_exception():
  manager = JWT_Manager.__new__(JWT_Manager)
  manager.public_key = "fake_public_key"
  manager.algorithm = "RS256"

  with patch("jwt.decode") as jwt_decode_mock:
    jwt_decode_mock.side_effect = Exception("Decode error")
    payload = manager.decode("fake_token")
  
  assert payload is None
  jwt_decode_mock.assert_called_once()
