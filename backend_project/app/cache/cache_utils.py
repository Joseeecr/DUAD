from functools import wraps
from flask import g

def check_cache(base_key, cache_manager, request = None, ttl= 600):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if "id" in kwargs:
        final_cache_key = f"{base_key}:{kwargs["id"]}"

      elif hasattr(g, "user_id"):
        final_cache_key = f"{base_key}:user:{g.user_id}"

      else:
        params = request.args.to_dict()
        final_cache_key = cache_manager.make_cache_key(f"{base_key}:all", params)

      cached = cache_manager.get_data(final_cache_key)

      if cached:
        print("returning cache")
        return cached

      response = func(*args, **kwargs)
      data, status = response

      if status == 200 and "id" in kwargs or hasattr(g, "user_id"):
        cache_manager.store_data(final_cache_key, data.get_json(), time_to_live = ttl)
      elif status == 200:
        cache_manager.store_data(final_cache_key, data.get_json(), time_to_live = ttl)
      return response
    return wrapper
  return decorator


def invalidate_cache(base_key, cache_manager):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      response = func(*args, **kwargs)
      status = response[1]

      if 200 <= status < 300:
        if "id" in kwargs:
          cache_manager.delete_data(f"{base_key}:{kwargs["id"]}")
          cache_manager.delete_data_with_pattern(f"{base_key}:all*")

        elif hasattr(g, "user_id"):
          cache_manager.delete_data(f"{base_key}:user:{g.user_id}")
          cache_manager.delete_data_with_pattern(f"{base_key}:all*")
        else:
          cache_manager.delete_data_with_pattern(f"{base_key}:all*")

      return response
    return wrapper
  return decorator