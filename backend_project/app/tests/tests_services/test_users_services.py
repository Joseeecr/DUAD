from unittest.mock import Mock, patch
from app.exceptions.exceptions import NotFoundError, ValidationError
import pytest
import bcrypt 

def test_list_users_returns_all_users_when_no_filters(user_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {}

  repo_mock.get_users.return_value = [
      Mock(_mapping={"id": 1, "name": "Jose", "last_name": "Blanco", "email": "randomemail@hotmail.com", "is_admin": True}),
  ]

  result = user_service.list_users({})

  assert result== [{"id": 1, "name": "Jose", "last_name": "Blanco", "email": "randomemail@hotmail.com", "is_admin": True}]
  validator_mock.validate_filters.assert_called_once_with({})
  repo_mock.get_users.assert_called_once()


def test_list_users_returns_filtered_users_when_valid_filters_provided(user_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"name": "Jose","is_admin": True}

  repo_mock.get_users.return_value = [
      Mock(_mapping={"id": 1, "name": "Jose", "last_name": "Blanco", "email": "randomemail@hotmail.com", "is_admin": True}),
  ]

  result = user_service.list_users({"name": "Jose","is_admin": True})

  assert result[0]["name"] == "Jose"
  validator_mock.validate_filters.assert_called_once_with({"name": "Jose","is_admin": True})
  repo_mock.get_users.assert_called_once()


def test_list_users_raises_not_found_error_when_no_users_match(user_service, validator_mock, repo_mock):

  validator_mock.validate_filters.return_value = {"name": "Manolo"}
  repo_mock.get_users.return_value = []

  with pytest.raises(NotFoundError) as exc_info:   
    user_service.list_users({"name": "Manolo"})

  assert str(exc_info.value) == "No matching users found."
  validator_mock.validate_filters.assert_called_once_with({"name": "Manolo"})
  repo_mock.get_users.assert_called_once()


def test_list_users_raises_validation_error_when_filters_invalid(user_service, validator_mock, repo_mock):
  validator_mock.validate_filters.side_effect = ValidationError("Invalid filters")

  with pytest.raises(ValidationError) as exc_info:   
    user_service.list_users({"id": "hello", "name": 123, "last_name": "Blanco", "email": "randomemail@hotmail.com", "is_admin": True})

  assert str(exc_info.value) == "Invalid filters"
  validator_mock.validate_filters.assert_called_once_with({"id": "hello", "name": 123, "last_name": "Blanco", "email": "randomemail@hotmail.com", "is_admin": True})
  repo_mock.get_users.assert_not_called()


def test_list_users_propagates_exception_when_repo_fails(user_service, validator_mock, repo_mock):
  validator_mock.validate_filters.return_value = {"name": "Jose","is_admin": True}

  repo_mock.get_users.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    user_service.list_users({"name": "Jose","is_admin": True})

  assert str(exc_info.value) == "DB error"
  validator_mock.validate_filters.assert_called_once_with({"name": "Jose","is_admin": True})
  repo_mock.get_users.assert_called_once()


def test_insert_user_sends_hashed_password_to_repo(user_service, validator_mock, repo_mock, jwt_manager_mock):
  raw_data = {
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "test1234",
    "phone_number": "12345678",
    "is_admin": "True"
  }

  validated_data = {
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "test1234",
    "phone_number": "12345678",
    "is_admin": True
  }

  validator_mock.validate_insert_user.return_value = validated_data

  with patch("bcrypt.gensalt") as mock_gensalt, patch("bcrypt.hashpw") as mock_hashpw:
    mock_gensalt.return_value = b"fake_salt"
    mock_hashpw.return_value = b"hashed_password"

    repo_mock.insert_user.return_value = 1
    jwt_manager_mock.encode.return_value = "token123"

    token = user_service.insert_user(raw_data)

    validator_mock.validate_insert_user.assert_called_once_with(raw_data)
    repo_call_data = repo_mock.insert_user.call_args[0][0]
    assert repo_call_data["password"] == "hashed_password"
    assert repo_call_data["is_admin"] is True
    assert repo_call_data["email"] == "randomemail@hotmail.com"

    jwt_manager_mock.encode.assert_called_once_with({"id": 1, "is_admin": True})
    assert token == "token123"


def test_insert_user_raises_validation_error_when_data_invalid(user_service, validator_mock, repo_mock, jwt_manager_mock):
  validator_mock.validate_insert_user.side_effect = ValidationError("Error inserting user")

  with pytest.raises(ValidationError) as exc_info:   
    user_service.insert_user({"name": "Jose","is_admin": True})

  assert str(exc_info.value) == "Error inserting user"
  validator_mock.validate_insert_user.assert_called_once_with({"name": "Jose","is_admin": True})
  repo_mock.insert_user.assert_not_called()
  jwt_manager_mock.encode.assert_not_called()


def test_insert_user_propagates_exception_when_repo_fails(user_service, validator_mock, repo_mock, jwt_manager_mock):
  raw_data = {
  "name": "Patrick",
  "last_name": "Star",
  "email": "randomemail@hotmail.com",
  "password": "test1234",
  "phone_number": "12345678",
  "is_admin": "True"
  }

  validated_data = {
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "test1234",
    "phone_number": "12345678",
    "is_admin": True
  }

  validator_mock.validate_insert_user.return_value = validated_data

  repo_mock.insert_user.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    user_service.insert_user(raw_data)

  assert str(exc_info.value) == "DB error"
  repo_mock.insert_user.assert_called_once()
  validator_mock.validate_insert_user.assert_called_once_with(raw_data)
  jwt_manager_mock.encode.assert_not_called()


def test_insert_user_propagates_exception_when_jwt_manager_fails(user_service, validator_mock, repo_mock, jwt_manager_mock):
  raw_data = {
  "name": "Patrick",
  "last_name": "Star",
  "email": "randomemail@hotmail.com",
  "password": "test1234",
  "phone_number": "12345678",
  "is_admin": "True"
  }

  validated_data = {
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "test1234",
    "phone_number": "12345678",
    "is_admin": True
  }

  validator_mock.validate_insert_user.return_value = validated_data

  repo_mock.insert_user.return_value = 1

  jwt_manager_mock.encode.side_effect = Exception("JWT error")

  with pytest.raises(Exception) as exc_info:   
    user_service.insert_user(raw_data)

  assert str(exc_info.value) == "JWT error"
  validator_mock.validate_insert_user.assert_called_once_with(raw_data)
  repo_mock.insert_user.assert_called_once_with(validated_data)
  jwt_manager_mock.encode.assert_called_once_with({"id": 1, "is_admin": True})


def test_login_user_returns_jwt_token_when_credentials_are_valid(user_service, repo_mock, jwt_manager_mock):
  hashed = bcrypt.hashpw("test1234".encode(), bcrypt.gensalt())

  repo_mock.get_user_by_email.return_value = {
  "id": 1,
  "name": "Patrick",
  "last_name": "Star",
  "email": "randomemail@hotmail.com",
  "password": hashed.decode("utf-8"),
  "phone_number": "12345678",
  "is_admin": True
  }

  jwt_manager_mock.encode.return_value = "token123"

  result = user_service.login_user("randomemail@hotmail.com", "test1234")

  assert result == "token123"
  repo_mock.get_user_by_email.assert_called_once_with("randomemail@hotmail.com")
  jwt_manager_mock.encode.assert_called_once_with({"id": 1, "is_admin": True})


def test_login_user_raises_value_error_when_email_not_found(user_service, repo_mock, jwt_manager_mock):
  repo_mock.get_user_by_email.return_value = None

  with pytest.raises(ValueError) as exc_info:   
    user_service.login_user("notexistingemail@hotmail.com", "test1234")

  assert str(exc_info.value) == "Incorrect email or password"
  repo_mock.get_user_by_email.assert_called_once_with("notexistingemail@hotmail.com")
  jwt_manager_mock.encode.assert_not_called()


def test_login_user_raises_value_error_when_password_is_incorrect(user_service, repo_mock, jwt_manager_mock):
  hashed = bcrypt.hashpw("test1234".encode(), bcrypt.gensalt())

  repo_mock.get_user_by_email.return_value = {
  "id": 1,
  "name": "Patrick",
  "last_name": "Star",
  "email": "randomemail@hotmail.com",
  "password": hashed.decode("utf-8"),
  "phone_number": "12345678",
  "is_admin": True
  }

  with pytest.raises(ValueError) as exc_info:   
    user_service.login_user("randomemail@hotmail.com", "wrongpass123")

  assert str(exc_info.value) == "Incorrect email or password"
  repo_mock.get_user_by_email.assert_called_once_with("randomemail@hotmail.com")
  jwt_manager_mock.encode.assert_not_called()


def test_login_user_propagates_exception_when_repo_fails(user_service, repo_mock, jwt_manager_mock):
  repo_mock.get_user_by_email.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    user_service.login_user("randomemail@hotmail.com", "wrongpass123")

  assert str(exc_info.value) == "DB error"
  repo_mock.get_user_by_email.assert_called_once_with("randomemail@hotmail.com")
  jwt_manager_mock.encode.assert_not_called()


def test_login_user_propagates_exception_when_jwt_manager_fails(user_service, repo_mock, jwt_manager_mock):
  hashed = bcrypt.hashpw("test1234".encode(), bcrypt.gensalt())

  repo_mock.get_user_by_email.return_value = {
  "id": 1,
  "name": "Patrick",
  "last_name": "Star",
  "email": "randomemail@hotmail.com",
  "password": hashed.decode("utf-8"),
  "phone_number": "12345678",
  "is_admin": True
  }

  jwt_manager_mock.encode.side_effect = Exception("JWT error")

  with pytest.raises(Exception) as exc_info:   
    user_service.login_user("randomemail@hotmail.com", "test1234")

  assert str(exc_info.value) == "JWT error"
  repo_mock.get_user_by_email.assert_called_once_with("randomemail@hotmail.com")
  jwt_manager_mock.encode.assert_called_once_with({"id": 1, "is_admin": True})


def test_login_user_accepts_stored_password_bytes_and_returns_token(user_service, repo_mock, jwt_manager_mock):
  hashed_bytes = bcrypt.hashpw("test1234".encode(), bcrypt.gensalt())

  repo_mock.get_user_by_email.return_value = {
    "id": 1,
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": hashed_bytes,
    "phone_number": "12345678",
    "is_admin": True
}
  jwt_manager_mock.encode.return_value = "token123"

  result = user_service.login_user("randomemail@hotmail.com", "test1234")

  assert result == "token123"


def test_update_user_by_admin_updates_user_successfully(user_service, validator_mock, repo_mock):
  raw_data = {"is_admin": False}

  repo_mock.get_user_by_id.return_value = {
    "id": 1,
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "hashed_password",
    "phone_number": "12345678",
    "is_admin": True
}
  validate_data = {"is_admin": False}

  validator_mock.validate_update_user.return_value = validate_data

  repo_mock.update_user_by_admin.return_value = 1

  result = user_service.update_user_by_admin(1, validate_data)

  assert result == 1
  repo_mock.get_user_by_id.assert_called_once_with(1)
  validator_mock.validate_update_user.assert_called_once_with(raw_data)
  repo_mock.update_user_by_admin.assert_called_once_with(1, validate_data)


def test_update_user_by_admin_raises_value_error_user_not_found(user_service, validator_mock, repo_mock):
  repo_mock.get_user_by_id.return_value = None

  with pytest.raises(ValueError) as exc_info:   
    user_service.update_user_by_admin(1000, {"is_admin": False})

  assert str(exc_info.value) == "User not found"
  repo_mock.get_user_by_id.assert_called_once_with(1000)
  validator_mock.validate_update_user.assert_not_called()
  repo_mock.update_user_by_admin.assert_not_called()


def test_update_user_by_admin_raises_validation_error_for_invalid_data(user_service, validator_mock, repo_mock):
  repo_mock.get_user_by_id.return_value = {
    "id": 1,
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "hashed_password",
    "phone_number": "12345678",
    "is_admin": True
  }
  validate_data = {"random_field": True}
  validator_mock.validate_update_user.side_effect = ValidationError("Invalid")

  with pytest.raises(ValidationError) as exc_info:   
    user_service.update_user_by_admin(1, validate_data)

  assert str(exc_info.value) == "Invalid"
  repo_mock.get_user_by_id.assert_called_once_with(1)
  validator_mock.validate_update_user.assert_called_once_with(validate_data)
  repo_mock.update_user_by_admin.assert_not_called()


def test_update_user_by_admin_propagates_exception_when_repo_fails(user_service, validator_mock, repo_mock):
  raw_data = {"is_admin": False}

  repo_mock.get_user_by_id.return_value = {
    "id": 1,
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "hashed_password",
    "phone_number": "12345678",
    "is_admin": True
  }
  validate_data = {"is_admin": False}

  validator_mock.validate_update_user.return_value = validate_data

  repo_mock.update_user_by_admin.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    user_service.update_user_by_admin(1, validate_data)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_user_by_id.assert_called_once_with(1)
  validator_mock.validate_update_user.assert_called_once_with(raw_data)
  repo_mock.update_user_by_admin.assert_called_once_with(1, validate_data)


def test_delete_user_returns_rowcount_when_user_exists(user_service, repo_mock):
  repo_mock.get_user_by_id.return_value = {
    "id": 1,
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "hashed_password",
    "phone_number": "12345678",
    "is_admin": True
  }

  repo_mock.delete_user.return_value = 1

  result = user_service.delete_user(1)
  assert result == 1
  repo_mock.get_user_by_id.assert_called_once_with(1)
  repo_mock.delete_user.assert_called_once_with(1)


def test_delete_user_raises_value_error_when_user_not_found(user_service, repo_mock):
  repo_mock.get_user_by_id.return_value = None

  with pytest.raises(ValueError) as exc_info:   
    user_service.delete_user(1000)

  assert str(exc_info.value) == "User not found"
  repo_mock.get_user_by_id.assert_called_once_with(1000)
  repo_mock.delete_user.assert_not_called()


def test_delete_user_propagates_exception_when_repo_fails_on_get(user_service, repo_mock):
  repo_mock.get_user_by_id.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    user_service.delete_user(1)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_user_by_id.assert_called_once_with(1)
  repo_mock.delete_user.assert_not_called()


def test_delete_user_propagates_exception_when_repo_fails_on_delete(user_service, repo_mock):
  repo_mock.get_user_by_id.return_value = {
    "id": 1,
    "name": "Patrick",
    "last_name": "Star",
    "email": "randomemail@hotmail.com",
    "password": "hashed_password",
    "phone_number": "12345678",
    "is_admin": True
  }

  repo_mock.delete_user.side_effect = Exception("DB error")

  with pytest.raises(Exception) as exc_info:   
    user_service.delete_user(1)

  assert str(exc_info.value) == "DB error"
  repo_mock.get_user_by_id.assert_called_once_with(1)
  repo_mock.delete_user.assert_called_once_with(1)
