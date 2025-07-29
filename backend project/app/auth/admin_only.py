from functools import wraps
from flask import request, jsonify
from auth.jwt_instance import jwt_manager

def admin_only(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      token = request.headers.get('Authorization')
      
      if token is not None:
        raw_token = token.replace("Bearer " , "")
        decoded = jwt_manager.decode(raw_token)

        is_admin = decoded.get("is_admin")

        if isinstance(is_admin, bool) and is_admin:
          return func(*args, **kwargs)

        else:
          return jsonify({"error": "Forbidden"}), 403
      else:
        return jsonify({"error": "Token needed"}), 401
    except Exception as e:
      return jsonify({"error": str(e)})
    
  return wrapper