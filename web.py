from flask import Flask, jsonify, render_template, request, url_for

from sample.api import Unisport


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(error=None):
        message = {
                'status': 404,
                'message': 'Not Found: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    @app.route('/products/', endpoint='products')
    def products():
        api = Unisport()
        # If pagination is in action, default to "first" page.
        page = int(request.args.get('page', 1))
        return jsonify(api.get_products(page=page))

    @app.route('/products/<id>/', endpoint='product')
    def product(id):
        api = Unisport()
        product = api.get_product(product_id=id)
        if product is None:
            return not_found()
        return jsonify(product)

    @app.route('/', endpoint='index')
    def index():
        documentation = dict(
            products=url_for('products'),
            product="test"
        )
        return render_template('index.html')

    return app
