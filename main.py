from flask import Flask
from .api.endpoints.products.index import products


def create_app():
    app = Flask(__name__)
    app.register_blueprint(products)

    return app
