from functools import wraps
from flask import request, jsonify, Response
from auth.jwt_instance import jwt_manager

def admin_only(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    token = request.headers.get("Authorization")
    if not token:
      return jsonify({"error": "Authorization token missing"}), 401

    try:
      raw_token = token.replace("Bearer ", "")
      decoded = jwt_manager.decode(raw_token)

      if not isinstance(decoded, dict):
        return jsonify({"error": "invalid token"}), 401

      role_id = decoded["role_id"]

      if role_id == 1:
        return func(*args, **kwargs)

      else:
        return jsonify({"error": "Forbidden"}), 403

    except Exception as e:
      return jsonify({"error": str(e)})
    
  return wrapper