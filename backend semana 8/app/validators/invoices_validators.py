from exceptions.generated_exceptions import ValidationError

class InvoiceValidators:

  def validate_invoice_filters(self, params: dict) -> dict:
    filters = {}

    if "id" in params:
      if params["id"].isdigit():
        filters["id"] = int(params["id"])
      else:
        raise ValidationError("Id must be a number")

    if "user_id" in params: 
      if params["user_id"].isdigit():
        filters["user_id"] = int(params["user_id"])
      else:
        raise ValidationError("User Id must be a number")

    if "shopping_cart_id" in params: 
      if params["shopping_cart_id"].isdigit():
        filters["shopping_cart_id"] = int(params["shopping_cart_id"])
      else:
        raise ValidationError("Cart Id must be a number")

    if "status" in params:
      if params["status"] in ["paid", "pending", "canceled"]:
        filters["status"] = params["status"]
      else:
        raise ValidationError("Status must be a 'paid', 'pending' or 'canceled'")

    return filters