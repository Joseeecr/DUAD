import pytest
from unittest.mock import Mock
from app.services.products_services import ProductsService
from app.services.user_services import UserService
from app.services.cart_services import CartServices

@pytest.fixture
def validator_mock():
  return Mock()

@pytest.fixture
def repo_mock():
  return Mock()

@pytest.fixture
def jwt_manager_mock():
  return Mock()

@pytest.fixture
def products_service(validator_mock, repo_mock):
  return ProductsService(validator_mock, repo_mock)

@pytest.fixture
def user_service(validator_mock, repo_mock, jwt_manager_mock):
  return UserService(validator_mock, repo_mock, jwt_manager_mock)

@pytest.fixture
def cart_service(validator_mock, repo_mock):
  return CartServices(validator_mock, repo_mock)

