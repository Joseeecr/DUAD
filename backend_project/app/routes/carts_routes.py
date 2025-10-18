from flask import Blueprint
from app.auth.admin_only import admin_only
from app.cache.cache_utils import invalidate_cache
from app.cache.cache_instance import cache_manager
from app.controllers.controllers_utils import jwt_required
from app.db.database import engine
from app.validators.carts_validators import CartsValidator
from app.repos.carts_repository import CartsRepository
from app.services.cart_services import CartServices
from app.controllers.carts_controller import CartsController

carts_validator = CartsValidator()
carts_repo = CartsRepository(engine)
cart_services = CartServices(carts_validator, carts_repo)
carts_controller = CartsController(cart_services)

carts_bp = Blueprint("carts", __name__, url_prefix="/carts")

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
@invalidate_cache("invoices", cache_manager)
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
