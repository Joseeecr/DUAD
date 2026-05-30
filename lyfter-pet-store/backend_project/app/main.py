from flask import Flask
from flask_cors import CORS
from app.routes.user_routes import user_bp
from app.routes.products_routes import products_bp
from app.routes.carts_routes import carts_bp
from app.routes.invoices_routes import invoices_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(products_bp)
app.register_blueprint(carts_bp)
app.register_blueprint(invoices_bp)
CORS(app)


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)