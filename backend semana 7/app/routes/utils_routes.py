from functools import wraps
from flask import request, jsonify, Response
from auth.jwt_instance import jwt_manager

def admin_only(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      token = request.headers.get('Authorization')
      
      if token is not None:
        test = token.replace("Bearer " , "")
        decoded = jwt_manager.decode(test)
        role_id = decoded["role_id"]

        if role_id == 1:
          return func(*args, **kwargs)

        else:
          return jsonify({"error": "Forbidden"}), 403
      else:
        return jsonify({"error": "Token needed"}), 401
    except Exception as e:
      return jsonify({"error": str(e)})
    
  return wrapper