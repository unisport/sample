from config import app
from model.product import Product
from schema import ProductSchema


@app.route('/products')
def products():
    with app.app_context():
        items = Product.query.order_by(Product.price).all()
        return ProductSchema().dump(items[:10], many=True)


@app.route('/products/kids')
def kids():
    with app.app_context():
        items = Product.query.filter(Product.kids == '1').order_by(Product.price).all()
        return ProductSchema().dump(items, many=True)


if __name__ == '__main__':
    app.run()
