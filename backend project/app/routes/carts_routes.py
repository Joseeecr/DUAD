from flask import Blueprint
from controllers.carts_controller import CartsController
from auth.admin_only import admin_only
from controllers.controllers_utils import jwt_required

carts_bp = Blueprint("carts", __name__, url_prefix="/carts")
carts_controller = CartsController()

@carts_bp.route("/", methods=['GET'])
@admin_only

def get_carts():
  return carts_controller.get_carts()


@carts_bp.route("/add", methods=['POST'])
@jwt_required
def post():
  return carts_controller.post_cart()


@carts_bp.route("/checkout", methods=['POST'])
@jwt_required
def checkout():
  return carts_controller.checkout_cart()


@carts_bp.route("/update/<int:id>", methods=['PATCH'])
@admin_only
def update_carts_by_admin(id):
  return carts_controller.update_by_admin(id)

@carts_bp.route("/update-cart-items/", methods=['PATCH'])
@jwt_required
def update_carts_products():
  return carts_controller.update_carts_items()
