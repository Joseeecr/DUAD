from flask import Blueprint,request
from app.cache.cache_utils import check_cache, invalidate_cache
from app.cache.cache_instance import cache_manager
from app.controllers.products_controller import ProductsController
from app.auth.admin_only import admin_only
from app.db.database import engine
from app.repos.products_repository import ProductsRepository
from app.services.products_services import ProductsService
from app.validators.products_validators import ProductsValidator

products_validator = ProductsValidator()
products_repo = ProductsRepository(engine)
products_service = ProductsService(products_validator, products_repo)

products_controller = ProductsController(products_service)

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/", methods=['GET'])
@admin_only
@check_cache("products", cache_manager, request)
def get_products():
  return products_controller.get_products()


@products_bp.route("/<int:id>", methods=['GET'])
@admin_only
@check_cache("products", cache_manager)
def get_products_by_id(id):
  return products_controller.get_product_id(id)


@products_bp.route("/", methods=['POST'])
@admin_only
@invalidate_cache("products", cache_manager)
def post():
  return products_controller.post_product()


@products_bp.route("/update/<int:id>", methods=['PATCH'])
@admin_only
@invalidate_cache("products", cache_manager)
def update_products_by_admin(id):
  return products_controller.update_by_admin(id)


@products_bp.route("/delete/<int:id>", methods=['DELETE'])
@admin_only
@invalidate_cache("products", cache_manager)
def delete(id):
  return products_controller.delete_product(id)