from flask import request, jsonify, g
from app.db.database import engine
from app.exceptions.exceptions import ValidationError, NotFoundError
from app.services.invoices_services import InvoicesServices
from app.repos.invoices_repository import InvoicesRepository
from app.validators.invoices_validators import InvoicesValidator

invoices_validator = InvoicesValidator()
invoices_repo = InvoicesRepository(engine)
invoices_service = InvoicesServices(invoices_validator, invoices_repo)

class InvoicesController:

  def get_invoices(self):
    try:

      params = request.args.to_dict()
      return invoices_service.list_invoices(params)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def check_user_invoices(self):
    try:
      return invoices_service.get_user_invoices(g.user_id)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500