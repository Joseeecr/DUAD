import pytest
from unittest.mock import Mock
from app.services.products_services import ProductsService
from app.services.user_services import UserService
from app.services.cart_services import CartServices
from app.services.invoices_services import InvoicesServices
from app.controllers.products_controller import ProductsController

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
def service_mock():
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

@pytest.fixture
def invoices_service(validator_mock, repo_mock):
  return InvoicesServices(validator_mock, repo_mock)

@pytest.fixture
def products_controller():
  mock_service = Mock()
  controller = ProductsController(mock_service)
  return controller, mock_service

@pytest.fixture
def products_controller(service_mock):
  return ProductsController(service_mock)