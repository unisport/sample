import json

import requests
from flask import request, redirect, url_for, render_template, flash

from config import app, db, PAGINATED
from forms import ProductForm
from models import Product


def convert_price_str_to_float(price):
    """
    I try use:
        locale.setlocale(locale.LC_ALL, 'da_DK')
        return locale.atof(d)
    But translate more faster.
    """
    try:
        return float(price.translate(str.maketrans(',', '.', '.')))
    except ValueError as e:
        # Add to log
        raise e


def get_original_data(base_url='https://www.unisport.dk/api/sample/'):
    """
    Get JSON from base_url and convert to python dict.
    """
    raw = requests.get(base_url).content.decode("utf-8")
    products = json.loads(raw)['products']
    return [{key: (convert_price_str_to_float(value) if key.startswith('price')
                   else value) for key, value in product.items()}
            for product in products]


def get_page_number():
    """
    Get page number from GET request(default 1).
    :return: page number in integer type
    """
    page = int(request.args.get('page', 1))
    if not page > 0:
        raise ValueError
    return page


@app.before_first_request
def _init_database():
    """
    Re init database after restart server.
    """
    db.drop_all()
    db.create_all()
    products = get_original_data()

    [db.session.add(Product(**product)) for product in products]
    db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products/')
def show_products():
    try:
        page = get_page_number()
    except ValueError:
        flash('Bad request: page must be integer type and more that 0.')
        return redirect(url_for('show_products'), code=302)

    products_query = Product.query.order_by('price').\
        paginate(page, PAGINATED, False)

    if not products_query.items:
        if not products_query.total:
            flash('Unfortunately we do not have products now.')
            return redirect(url_for('index'))

        flash('We have {} products, so the last page {}. '
              'You have been redirect'.format(products_query.total,
                                              products_query.pages))
        return redirect('/products/?page={}'.format(products_query.pages))

    start_num = (products_query.page-1)*PAGINATED+1
    return render_template('product_list.html', products=products_query,
                           start_number=start_num)


@app.route('/products/kids/')
def show_kids_products():
    try:
        page = get_page_number()
    except ValueError:
        flash('Bad request: page must be integer type and more that 0.')
        return redirect(url_for('show_kids_products'), code=302)

    products_query = Product.query.order_by('price').filter_by(kids=1).\
        paginate(page, PAGINATED, False)
    if not products_query.items:

        if not products_query.total:
            flash('Unfortunately we do not have products for kids now.')
            return redirect(url_for('index'))

        flash('We have {} products for kids, so the last page {}. '
              'You have been redirect'.format(products_query.total,
                                              products_query.pages))
        return redirect('/products/?page={}'.format(products_query.pages))

    start_num = (products_query.page - 1) * PAGINATED + 1
    return render_template('product_list.html', products=products_query,
                           start_number=start_num)


@app.route('/products/<product_id>', methods=['GET', 'POST'])
def show_or_edit_product_by_id(product_id):
    if request.method == 'GET':
        product = Product.query.get(product_id)
        if product is None:
            flash('The product with id={} not found'.format(product_id))
            return redirect(url_for('index'))
        form = ProductForm(obj=product)
        return render_template('detail.html', id=product_id, form=form)
    if request.method == 'POST':
        if request.form['submit'] == 'Delete':
            Product.query.filter_by(id=product_id).delete()
            db.session.commit()
            flash('The product with id={} has been deleted'.format(product_id))
            return redirect(url_for('index'))
        else:
            form = ProductForm(request.form)
            if form.validate():
                product = Product.query.get(product_id)
                for key, value in form.data.items():
                    setattr(product, key, value)
                db.session.commit()
                flash('The product with id={} has been updated'.
                      format(product_id))
                return redirect(url_for('index'))
            else:
                return render_template('detail.html', id=product_id, form=form)


@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'GET':
        form = ProductForm()
        return render_template('create.html', form=form)
    elif request.method == 'POST':
        form = ProductForm(request.form)
        if form.validate():
            new_product = Product(**form.data)
            db.session.add(new_product)
            db.session.commit()
            flash('The product has been added with new id={}'.
                  format(new_product.id))
            return redirect(url_for('index'))
        else:
            return render_template('create.html', form=form)


if __name__ == '__main__':
    app.run()
