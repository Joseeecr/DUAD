from app.auth.jwt_instance import jwt_manager
from functools import wraps
from flask import request, jsonify, g

def jwt_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    token = request.headers.get("Authorization")
    if not token:
      return jsonify({"error": "Authorization token missing"}), 401

    try:
      raw_token = token.replace("Bearer ", "")
      decoded = jwt_manager.decode(raw_token)
      if not isinstance(decoded, dict):
        return jsonify({"error": "Invalid token"}), 401

      if "id" not in decoded:
        return jsonify({"error": "id field missing"}), 401

      g.user_id = decoded.get("id")
      return func(*args, **kwargs)

    except Exception as e:
      return jsonify({"error": str(e)}), 401

  return wrapper
