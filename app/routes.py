from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.models import Products
from app.forms import CreateProduct, EditProduct


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('products'))


@app.route('/products', methods=['GET', 'POST'])
def products():
    form = CreateProduct()
    if form.validate_on_submit():
        new_product = Products(name=form.name.data, price=form.price.data, image=form.image.data)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added')
        return redirect(url_for('products', _anchor="msg"))

    page = request.args.get('page', 1, type=int)

    #Query the DB to get all items (ascending order) and adding SQLAlchemy pagination
    products = Products.query.order_by(Products.price.asc()).paginate(page, app.config['POSTS_PER_PAGE'], False)

    #Create next or prev links
    next_url = url_for('products', page=products.next_num) if products.has_next else None
    prev_url = url_for('products', page=products.prev_num) if products.has_prev else None

    return render_template('products.html', form=form,
                           products=products,
                           next_url=next_url,
                           prev_url=prev_url)



@app.route('/products/id/<id>', methods=['GET', 'POST'])
def product_page(id):

    # query the DB for the product matching the ID. Returns 404 if id not found
    product = Products.query.filter_by(id=id).first_or_404()

    form = EditProduct()
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.image = form.image.data
        db.session.commit()
        return redirect(url_for('product_page', id=product.id))
    elif request.method == 'GET':
        form.name.data = product.name
        form.price.data = product.price
        form.image.data = product.image

    return render_template('product_page.html', product=product, form=form)


@app.route('/products/delete/<int:id>/delete', methods=['POST'])
def product_deletion(id):
    delete_product = Products.query.get_or_404(id)
    db.session.delete(delete_product)
    db.session.commit()
    flash('Product deleted')

    return redirect(url_for('products'))


@app.route('/products/kids')
def kids():

    #08-04-2019 --> No products in the API matched "kids" or "kid_adult"

    return "<p>Nothing here</p>"
