from flask import Blueprint
from controllers.products_controller import ProductsController

products_bp = Blueprint("products", __name__, url_prefix="/products")
products_controller = ProductsController()

@products_bp.route("/", methods=['GET'])
def get_products():
  return products_controller.get_products()


@products_bp.route("/", methods=['POST'])
def post():
  return products_controller.post_product()


@products_bp.route("/update/<int:id>", methods=['PATCH'])
def update_products_by_admin(id):
  return products_controller.update_by_admin(id)


@products_bp.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
  return products_controller.delete_product(id)