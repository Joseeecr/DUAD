from flask import Blueprint
from controllers.user_controller import UserController


user_bp = Blueprint("user", __name__, url_prefix="/users")
user_controller = UserController()


@user_bp.route("/", methods=['GET'])
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
def update_user_by_admin(id):
  return user_controller.update_by_admin(id)


@user_bp.route("/delete/<int:id>", methods=['DELETE'])
def delete_user(id):
  return user_controller.delete(id)