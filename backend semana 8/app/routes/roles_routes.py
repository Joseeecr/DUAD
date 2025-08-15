from flask import Blueprint, request, jsonify, Response
from repos.roles_repository import RolesRepository
from db.tables import engine
from validators.roles_validators import RoleValidators
from routes.utils_routes import admin_only
from exceptions.generated_exceptions import RoleNotFoundError, ValidationError, ColumnNotFoundError

role_validator = RoleValidators()
role_repo = RolesRepository(engine, role_validator)
role_bp = Blueprint("role", __name__, url_prefix="/roles")


@role_bp.route('/', methods=['GET'])
@admin_only
def list_roles():
  raw_params = request.args.to_dict()

  try:
    filters = role_validator.validate_role_filters(raw_params)
    role = role_repo.get_roles(filters)
    return jsonify(role), 200

  except ValidationError as e:
    return jsonify({"error": str(e)}), 400
  except RoleNotFoundError as e:
    return jsonify({"error": str(e)}), 404


@role_bp.route('/', methods=['POST'])
@admin_only
def add_role():
  data = request.get_json()

  role = data.get("role")

  errors = role_validator.insert_role_validator(data)
  
  if errors:
    return {"errors": errors}, 400

  elif role_repo.insert_role(role=role):
    return {"success": "role was successfully inserted"}, 200

  else:
    return {"error": "that role is already in the DB"}, 400


@role_bp.route('/update/<int:_id>', methods=['PATCH'])
@admin_only
def update(_id):
  try:
    data = request.get_json()
    role_repo.update_role(_id, data)
    return jsonify("Role successfully updated"), 200
  except ColumnNotFoundError as e:
    return jsonify({"error": str(e)}), 400


@role_bp.route('/delete/<int:_id>', methods=['DELETE'])
@admin_only
def delete(_id):
  success = role_repo.delete_role(_id)

  if not success:
    return Response("Role not found", status=404)

  return Response("Resource deleted successfully", status=200)