from flask import Blueprint
from controllers.carts_controller import CartsController

carts_bp = Blueprint("carts", __name__, url_prefix="/carts")
carts_controller = CartsController()

@carts_bp.route("/", methods=['GET'])
def get_carts():
  return carts_controller.get_carts()


@carts_bp.route("/add", methods=['POST'])
def post():
  return carts_controller.post_cart()


@carts_bp.route("/checkout", methods=['POST'])
def checkout():
  return carts_controller.checkout_cart()


@carts_bp.route("/update/<int:id>", methods=['PATCH'])
def update_carts_by_admin(id):
  return carts_controller.update_by_admin(id)

@carts_bp.route("/update-carts-items/", methods=['PATCH'])
def update_carts_products():
  return carts_controller.update_carts_items()
