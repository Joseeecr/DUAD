from flask import jsonify
def checking_cache(key, cache_manager):
  try:
    cached =  cache_manager.get_data(key)
    
    if cached:
      return jsonify(cached), 200

  except Exception as e:
    print(f"Cache error: {e}")
    return None