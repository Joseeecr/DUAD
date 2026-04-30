from unittest.mock import Mock
from flask import Flask, jsonify
from app.cache.cache_utils import check_cache, invalidate_cache

def test_check_cache_returns_cached_data_when_exists():
  cache_manager = Mock()
  cache_manager.get_data.return_value = {"id": 1, "name": "Cached"}

  @check_cache("test_key", cache_manager)
  def dummy_func(*args, **kwargs):
    return jsonify({"id": 1, "name": "Fresh"}), 200

  app = Flask(__name__)
  with app.test_request_context("/"):
    response = dummy_func(id=1)

  assert response == {"id": 1, "name": "Cached"}
  cache_manager.get_data.assert_called_once_with("test_key:1")

def test_check_cache_stores_data_when_cache_empty():
  cache_manager = Mock()
  cache_manager.get_data.return_value = None

  @check_cache("test_key", cache_manager)
  def dummy_func(*args, **kwargs):
    return jsonify({"id": 1, "name": "Fresh"}), 200

  app = Flask(__name__)
  with app.test_request_context("/"):
    response = dummy_func(id=1)

  assert response[1] == 200
  cache_manager.store_data.assert_called_once()
  cache_manager.get_data.assert_called_once_with("test_key:1")

def test_invalidate_cache_calls_delete_methods_on_success():
  cache_manager = Mock()
  cache_manager.delete_data.return_value = True
  cache_manager.delete_data_with_pattern.return_value = 1

  @invalidate_cache("test_key", cache_manager)
  def dummy_func(*args, **kwargs):
    return jsonify({"success": True}), 200

  app = Flask(__name__)
  with app.test_request_context("/"):
    response = dummy_func(id=1)

  cache_manager.delete_data.assert_called_once_with("test_key:1")
  cache_manager.delete_data_with_pattern.assert_called_once_with("test_key:all*")
  assert response[1] == 200


def test_invalidate_cache_does_not_delete_on_failure():
  cache_manager = Mock()

  @invalidate_cache("test_key", cache_manager)
  def dummy_func(*args, **kwargs):
    return jsonify({"error": "fail"}), 400

  app = Flask(__name__)
  with app.test_request_context("/"):
    response = dummy_func(id=1)

  # No debe borrar nada si status != 2xx
  cache_manager.delete_data.assert_not_called()
  cache_manager.delete_data_with_pattern.assert_not_called()
  assert response[1] == 400
