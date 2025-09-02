from unittest.mock import Mock
from app.controllers.products_controller import ProductsController

def test_products():
  service_mock = Mock()
  service_mock.list_products.return_value = [
    {"id": 1, "name": "Pelota", "price": "2.50"},
    {"id": 2, "name": "Correa", "price": "5.99"},
    {"id": 3, "name": "Juguete de cuerda", "price": "4.99"}
]

  controller = ProductsController(service=service_mock)

  result = controller.get_products()

  assert result == [
    {"id": 1, "name": "Pelota", "price": "2.50"},
    {"id": 2, "name": "Correa", "price": "5.99"},
    {"id": 3, "name": "Juguete de cuerda", "price": "4.99"}
]

  service_mock.list_products.assert_called_once()