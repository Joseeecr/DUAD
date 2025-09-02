from flask import Blueprint
from controllers.invoices_controller import InvoicesController
from auth.admin_only import admin_only
from controllers.controllers_utils import jwt_required


invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")
invoices_controller = InvoicesController()

@invoices_bp.route("/", methods=['GET'])
@admin_only
def get_invoices():
  return invoices_controller.get_invoices()


@invoices_bp.route("/check-invoices", methods=['GET'])
@jwt_required
def check_user_invoices():
  return invoices_controller.check_user_invoices()