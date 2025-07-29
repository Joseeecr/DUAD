# from services.json_manager import read_json_file, write_json_file

# def get_invoice(invoice_number):
#     invoices = read_json_file("invoices.json")

#     invoice = next((i for i in invoices if i["invoice_number"] == invoice_number), None)
#     if not invoice:
#         # return {"error": "Invoice Number not found"}, 404

#     return invoice


# def refund_invoice(invoice_number):
#     invoices = read_json_file("invoices.json")
#     products = read_json_file("products.json")


#     invoice = next((i for i in invoices if i["invoice_number"] == invoice_number), None)
#     if not invoice:
#         return {"error": "Invoice Number not found"}, 404

#     for item in invoice["products"]:
#         for product in products:
#             if item["product_id"] == product["product_id"]:
#                 product["stock"] += item["amount"]

#     invoices.remove(invoice)

#     write_json_file("products.json", products)
#     write_json_file("invoices.json", invoices)

#     return f"Success, invoice {invoice} was succesfully refunded"
