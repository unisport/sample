from flask import Flask
from flask import request, url_for, flash, make_response, jsonify
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from model.model import init_db, Base, Product
from utilities.normalizer import alchemy_to_json
from utilities.input_guard import guard_products_failed

# application instance
app = Flask(__name__)

# handle db init and seeding
init_db()

#model
engine = create_engine('sqlite:///storage/sample.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# CRUD
# Read - this endpoint is paginated
@app.route('/products', methods=['GET'])
def get_producsts():
    page = int(request.args.get('page', 1)) if request.args.get('page', 1) is not None else 1
    products = session.query(Product).order_by(Product.id.asc()).limit(10).offset((page-1)*10).all()
    return alchemy_to_json('products', products)    

# Read
@app.route('/products/kids', methods=['GET'])
def get_kids():
    products = session.query(Product).filter(Product.kids==1).limit(10).all()
    return alchemy_to_json('products', products)

# Read
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    try :
        products = session.query(Product).filter_by(id = id).one()
        return alchemy_to_json('products', products)    
    except exc.SQLAlchemyError :
        return make_response(jsonify({'error': 'Product found'}), 404)

# Create
@app.route("/products/create", methods=['POST'])
def create_product():
    if guard_products_failed(request.form.keys()) :
        return make_response(jsonify({'error': 'Input not allowed'}), 400)
    try :
        product = Product(
            name = request.form.get('name', '', type=str),
            delivery = request.form.get('delivery', '', type=str),
            free_porto = request.form.get('free_porto', 0, type=int),
            img_url = request.form.get('img_url', '', type=str),
            kid_adult = request.form.get('kid_adult', 0, type=int),
            kids = request.form.get('kids', 0, type=int),
            package = request.form.get('women', 0, type=int),
            price = request.form.get('price', '', type=str),
            price_old = request.form.get('price_old', '', type=str),
            sizes = request.form.get('sizes', 'M', type=str),
            url = request.form.get('url', '', type=str),
            women = request.form.get('women', 0, type=int)
        )
        session.add(product)
        session.commit()
        session.rollback()
    except exc.SQLAlchemyError :
        return make_response(jsonify({'error': 'Failed to create product'}), 400)
    return make_response(alchemy_to_json('products', product), 201)

# Edit
@app.route("/products/<int:id>/edit", methods=['PATCH', 'PUT'])
def edit_product(id):
    print request.form
    if guard_products_failed(request.form.keys()) :
        return make_response(jsonify({'error': 'Input not allowed'}), 400)
    try :
        product = session.query(Product).filter_by(id = id).one()
        product.name = request.form.get('name', '', type=str)
        product.delivery = request.form.get('delivery', '', type=str)
        product.free_porto = request.form.get('free_porto', 0, type=int)
        product.img_url = request.form.get('img_url', '', type=str)
        product.kid_adult = request.form.get('kid_adult', 0, type=int)
        product.kids = request.form.get('kids', 0, type=int)
        product.package = request.form.get('women', 0, type=int)
        product.price = request.form.get('price', '', type=str)
        product.price_old = request.form.get('price_old', '', type=str)
        product.sizes = request.form.get('sizes', 'M', type=str)
        product.url = request.form.get('url', '', type=str)
        product.women = request.form.get('women', 0, type=int)
        session.add(product)
        session.commit()
        session.rollback()
    except exc.SQLAlchemyError :
        return make_response(jsonify({'error': 'Failed to create product'}), 400)
    return make_response(alchemy_to_json('products', product), 201)

# Delete
@app.route("/products/<int:id>/delete", methods=['DELETE'])
def delete_product(id):
    try :
        product = session.query(Product).filter_by(id = id).one()
        session.delete(product)
        session.commit()
    except exc.SQLAlchemyError :
        return make_response(jsonify({'error': 'Failed to delete product'}), 404)
    return make_response(jsonify({'message': 'Product Deleted'}), 200)

if __name__ == '__main__':
    app.debug = True
    app.run()