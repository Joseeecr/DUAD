from flask import Blueprint
from app.db.database import engine
from app.controllers.invoices_controller import InvoicesController
from app.auth.admin_only import admin_only
from app.controllers.controllers_utils import jwt_required
from app.services.invoices_services import InvoicesServices
from app.repos.invoices_repository import InvoicesRepository
from app.validators.invoices_validators import InvoicesValidator

invoices_validator = InvoicesValidator()
invoices_repo = InvoicesRepository(engine)
invoices_service = InvoicesServices(invoices_validator, invoices_repo)

invoices_controller = InvoicesController(invoices_service)

invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")

@invoices_bp.route("/", methods=['GET'])
@admin_only
def get_invoices():
  return invoices_controller.get_invoices()


@invoices_bp.route("/check-invoices", methods=['GET'])
@jwt_required
def check_user_invoices():
  return invoices_controller.check_user_invoices()