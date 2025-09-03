import redis
import json
from decimal import Decimal
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    if isinstance(obj, datetime):
      return obj.isoformat()
    return super().default(obj)


class CacheManager:
  def __init__(self, host, port, password,  *args, **kwargs):
    self.redis_client = redis.Redis(
      host = host,
      port = port,
      password = password,
      decode_responses=True,
      *args,
      **kwargs
  )


  def get_data(self, key : str):
    value = self.redis_client.get(key)

    if not value:
      return None

    return json.loads(value)


  def store_data(self, key : str, data, time_to_live = None):
    try:
      json_data = json.dumps(data, cls=CustomJSONEncoder)

      if time_to_live is None:
        self.redis_client.set(key, json_data)
        return data

      self.redis_client.setex(key, time_to_live, json_data)
      return data
    except redis.RedisError as error:
      print(f"An error ocurred while storing data in Redis: {error}")


  def make_cache_key(self, base: str, params: dict) -> str:
    if not params:
      return base
    query_str = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
    return f"{base}?{query_str}"
  
  
  def delete_data(self, key):
    try:
      output = self.redis_client.delete(key)

      return output == 1

    except redis.RedisError as error:
      print(f"An error ocurred while deleting data from Redis: {error}")
      return False


  def delete_data_with_pattern(self, pattern):
    deleted_count = 0
    try:
      for key in self.redis_client.scan_iter(match=pattern):
        self.delete_data(key)
        deleted_count += 1
      print(f"Deleted keys = {deleted_count}")
      return deleted_count
    except redis.RedisError as e:
      print(f"An error ocurred while deleting data from Redis: {e}")
      return None