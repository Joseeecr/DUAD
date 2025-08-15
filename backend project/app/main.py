from flask import Flask
from routes.user_routes import user_bp
from routes.products_routes import products_bp
from routes.carts_routes import carts_bp
from routes.invoices_routes import invoices_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(products_bp)
app.register_blueprint(carts_bp)
app.register_blueprint(invoices_bp)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)