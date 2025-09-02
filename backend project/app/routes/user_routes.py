from flask import Blueprint
from controllers.user_controller import UserController
from auth.admin_only import admin_only

user_bp = Blueprint("user", __name__, url_prefix="/users")
user_controller = UserController()


@user_bp.route("/", methods=['GET'])
@admin_only
def get_users():
  return user_controller.get_user()


@user_bp.route("/register", methods=['POST'])
def register_user():
  return user_controller.register()


@user_bp.route("/login", methods=['POST'])
def login_user():
  return user_controller.login()


@user_bp.route('/me')
def me():
  return user_controller.me()


@user_bp.route("/update/<int:id>", methods=['PATCH'])
@admin_only
def update_user_by_admin(id):
  return user_controller.update_by_admin(id)


@user_bp.route("/delete/<int:id>", methods=['DELETE'])
@admin_only
def delete_user(id):
  return user_controller.delete(id)