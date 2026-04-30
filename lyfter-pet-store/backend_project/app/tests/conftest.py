import pytest
from unittest.mock import Mock, patch
from app.services.products_services import ProductsService
from app.services.user_services import UserService
from app.services.cart_services import CartServices
from app.services.invoices_services import InvoicesServices
from app.controllers.products_controller import ProductsController
from app.controllers.user_controller import UserController
from app.controllers.carts_controller import CartsController
from app.controllers.invoices_controller import InvoicesController
from app.cache.cache_manager import CacheManager

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
def products_controller(service_mock):
  return ProductsController(service_mock)

@pytest.fixture
def user_controller(service_mock, jwt_manager_mock):
  return UserController(service_mock, jwt_manager_mock)

@pytest.fixture
def cart_controller(service_mock):
  return CartsController(service_mock)

@pytest.fixture
def invoices_controller(service_mock):
  return InvoicesController(service_mock)

@pytest.fixture
def redis_mock():
  with patch("app.cache.cache_manager.redis.Redis") as mock:
    yield mock

@pytest.fixture
def cache_manager(redis_mock):
  manager = CacheManager("localhost", 6379, "password")
  return manager