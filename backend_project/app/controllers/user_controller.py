from flask import request, jsonify, Response
from app.exceptions.exceptions import ValidationError, NotFoundError

class UserController:
  def __init__(self, user_service, jwt_manager):
    self.user_service = user_service
    self.jwt_manager = jwt_manager

  def get_user(self):
    try:

      params = request.args.to_dict()
      users = self.user_service.list_users(params)
      return jsonify(users), 200

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print(f"error : {str(e)}")
      return jsonify({"error": "Internal server error"}), 500


  def register(self):
    try:

      data = request.get_json()
      token = self.user_service.insert_user(data)
      return jsonify(token=token), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      print(f"error: {e}")
      return jsonify({"error": "Internal Server error"}), 500


  def login(self):
    try:
      data = request.get_json()
      token = self.user_service.login_user(data.get("email"), data.get("password"))
      return jsonify(token=token), 200
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      print(f"error: {e}")
      return jsonify({"error": "Internal Server error"}), 500


  def me(self):

    try:
      token = request.headers.get('Authorization')
      
      if token is not None:
        test = token.replace("Bearer ","")
        decoded = self.jwt_manager.decode(test)
        user_id = decoded['id']
        user_row = self.user_service.get_user_by_id(user_id)

        return jsonify(id=user_id, name=user_row["name"], is_admin=user_row["is_admin"]), 200

      else:
        return jsonify({"error": "Forbidden"}), 403

    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def update_by_admin(self, id):
    try:
      data = request.get_json()
      self.user_service.update_user_by_admin(id, data)
      return jsonify({"message": "User successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500


  def delete(self, id):
    try:
      self.user_service.delete_user(id)
      return jsonify(), 204
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404