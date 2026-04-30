from unittest.mock import Mock
from app.cache.cache_manager import CustomJSONEncoder
import json
from decimal import Decimal
from datetime import datetime
import redis


def test_get_data_returns_none_when_key_missing(cache_manager):
  cache_manager.redis_client.get.return_value = None
  result = cache_manager.get_data("missing_key")
  assert result is None
  cache_manager.redis_client.get.assert_called_once_with("missing_key")


def test_get_data_returns_decoded_json_when_key_exists(cache_manager):
  data = {"a": 1}
  cache_manager.redis_client.get.return_value = json.dumps(data)
  result = cache_manager.get_data("my_key")
  assert result == data
  cache_manager.redis_client.get.assert_called_once_with("my_key")


def test_store_data_sets_data_without_ttl(cache_manager):
  data = {"num": Decimal("10.5")}
  result = cache_manager.store_data("key1", data)
  expected_json = json.dumps(data, cls=CustomJSONEncoder)
  cache_manager.redis_client.set.assert_called_once_with("key1", expected_json)
  assert result == data


def test_store_data_sets_data_with_ttl(cache_manager):
  data = {"date": datetime(2025, 1, 1)}
  ttl = 60
  result = cache_manager.store_data("key2", data, time_to_live=ttl)
  expected_json = json.dumps(data, cls=CustomJSONEncoder)
  cache_manager.redis_client.setex.assert_called_once_with("key2", ttl, expected_json)
  assert result == data


def test_make_cache_key_returns_base_when_params_empty(cache_manager):
  assert cache_manager.make_cache_key("base", {}) == "base"
  assert cache_manager.make_cache_key("base", None) == "base"


def test_make_cache_key_returns_correct_query_string(cache_manager):
  params = {"b": 2, "a": 1}
  key = cache_manager.make_cache_key("base", params)

  assert key == "base?a=1&b=2"


def test_delete_data_returns_true_when_key_deleted(cache_manager):
  cache_manager.redis_client.delete.return_value = 1
  assert cache_manager.delete_data("key") is True
  cache_manager.redis_client.delete.assert_called_once_with("key")


def test_delete_data_returns_false_when_key_not_deleted(cache_manager):
  cache_manager.redis_client.delete.return_value = 0
  assert cache_manager.delete_data("key") is False
  cache_manager.redis_client.delete.assert_called_once_with("key")


def test_delete_data_with_pattern_handles_redis_error(cache_manager):
  cache_manager.redis_client.scan_iter.side_effect = redis.RedisError("fail")
  count = cache_manager.delete_data_with_pattern("pattern*")
  assert count is None