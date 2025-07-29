from flask import Blueprint, request, jsonify, Response
from repos.user_repository import UserRepository
from db.tables import engine
from validators.users_validators import UserValidators
from auth.jwt_instance import jwt_manager
from routes.utils_routes import admin_only
from exceptions.generated_exceptions import UserNotFoundError, ValidationError, ColumnNotFoundError

user_validator = UserValidators()
user = UserRepository(engine, user_validator)
user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route('/', methods=['GET'])
@admin_only
def list_users():
  raw_params = request.args.to_dict()

  try:
    filters = user_validator.validate_user_filters(raw_params)
    users = user.get_users(filters)
    return jsonify(users), 200

  except ValidationError as e:
    return jsonify({"error": str(e)}), 400
  except UserNotFoundError as e:
    return jsonify({"error": str(e)}), 404


@user_bp.route("/register", methods=['POST'])
def register():
  data = request.get_json()  # data is empty

  if data.get('username') == None or data.get('password') == None or data.get('role_id') == None:
    return Response(status=400)
  else:
    user_id = user.insert_user(data.get('username'), data.get('password'), data.get('role_id'))

    token = jwt_manager.encode({
      'id':user_id,
      "role_id": user_id
    })

    return jsonify(token=token)


@user_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()  # data is empty

  if data.get('username') == None or data.get('password') == None:
    return Response(status=400)
  else:
    result = user.get_user(data.get('username'), data.get('password'))

  if result == None:
    return Response(status=403)
  else:
    user_row = dict(result._mapping)

    token = jwt_manager.encode({
      "id": user_row["id"],
      "role_id": user_row["role_id"]
    })

    return jsonify(token=token)


@user_bp.route('/me')
def me():

  try:
    token = request.headers.get('Authorization')
    
    if token is not None:
      test = token.replace("Bearer ","")
      decoded = jwt_manager.decode(test)
      user_id = decoded['id']
      user_row = user.get_user_by_id(user_id)

      return jsonify(id=user_id, username=user_row[1])

    else:
      return Response(status=403)

  except Exception as e:
    return Response(e, status=500)


@user_bp.route('/update/<int:_id>', methods=['PATCH'])
@admin_only
def update(_id):
  try:
    data = request.get_json()
    user.update_user(_id, data)
    return jsonify("User successfully updated"), 200
  except ColumnNotFoundError as e:
    return jsonify({"error": str(e)}), 400


@user_bp.route('/delete/<int:_id>', methods=['DELETE'])
@admin_only
def delete(_id):
  success = user.delete_user(_id)

  if not success:
    return Response("User not found", status=404)

  return Response(status=204)
