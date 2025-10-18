from flask import request, jsonify, Response
from db.database import engine
from exceptions.exceptions import ValidationError, NotFoundError
from services.user_services import UserService
from repos.user_repository import UserRepository
from validators.user_validators import UserValidator
from auth.jwt_instance import jwt_manager
from auth.admin_only import admin_only

user_validator = UserValidator()
user_repo = UserRepository(engine)
user_service = UserService(user_validator, user_repo, jwt_manager)


class UserController:
  @admin_only
  def get_user(self):
    try:

      params = request.args.to_dict()
      return user_service.list_users(params)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 


  def register(self):
    try:

      data = request.get_json()
      token = user_service.insert_user(data)
      return jsonify(token=token), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def login(self):
    try:
      data = request.get_json()
      token = user_service.login_user(data.get("email"), data.get("password"))
      return jsonify(token=token), 200
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def me(self):

    try:
      token = request.headers.get('Authorization')
      
      if token is not None:
        test = token.replace("Bearer ","")
        decoded = jwt_manager.decode(test)
        user_id = decoded['id']
        user_row = user_repo.get_user_by_id(user_id)

        return jsonify(id=user_id, name=user_row["name"], is_admin=user_row["is_admin"])

      else:
        return Response(status=403)

    except Exception as e:
      return Response(e, status=500)


  @admin_only
  def update_by_admin(self, id):
    try:
      data = request.get_json()
      user_service.update_user_by_admin(id, data)
      return jsonify({"message": "User successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except ValueError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  @admin_only
  def delete(self, id):
    try:
      user_service.delete_user(id)
      return jsonify(), 204
    except ValueError as e:
      return jsonify({"error": str(e)}), 404