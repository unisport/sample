from flask import Flask


app = Flask(__name__)

@app.route('/products/')
def products():
    """If page arg *n* is passed (e.g /products/?page=2); return the items from
    n*10 - 10 to n*10. Else return the 10 first items ordered cheapest first."""
    return 'Products'

@app.route('/products/kids/')
def kid_products():
    """Return all items where kids=1 ordered cheapest first."""
    return 'Kids'

@app.route('/products/<id>/')
def product_by_id(id):
    """Return the product with id=id."""
    return 'Product by ID'
