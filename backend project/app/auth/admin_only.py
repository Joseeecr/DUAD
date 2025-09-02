from functools import wraps
from flask import request, jsonify
from auth.jwt_instance import jwt_manager

def admin_only(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      token = request.headers.get('Authorization')

      if not token:
        return jsonify({"error": "Token needed"}), 401

      raw_token = token.replace("Bearer " , "")
      decoded = jwt_manager.decode(raw_token)
      
      if not decoded:
        return jsonify({"error": "Invalid token"}), 403

      is_admin = decoded.get("is_admin")

      if isinstance(is_admin, bool) and is_admin:
        return func(*args, **kwargs)

      else:
        return jsonify({"error": "Forbidden"}), 403
        
    except Exception as e:
      return jsonify({"error": str(e)})
    
  return wrapper