from flask import Blueprint
from controllers.invoices_controller import InvoicesController

invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")
invoices_controller = InvoicesController()

@invoices_bp.route("/", methods=['GET'])
def get_invoices():
  return invoices_controller.get_invoices()



@invoices_bp.route("/check-invoices", methods=['GET'])
def check_user_invoices():
  return invoices_controller.check_user_invoices()