""" First shot at Flask -- seems less boilerplate than Django

Notes:

Singlethreaded app, no need to think of concurrency here
debug=True is ok in non-prod environments

Started out with products() that did the sorting and returned 10 items

Then kids, and sorting and returning any number of product
was made in get_items_by_price and products() changed also

Then I did the product by id, but first turned data structure into dict.
It was trivial to change get_items_by_price and products() and kids()
did not have to be changed.

For the pagination I first implemented the optional offset in
get_items_by_price(). Then changed products() to support ?page and ?count.

I have no experience in testing web apps so this Flask app is without tests
for now. Obviously wrong!


"""

import flask
import json

# our dict of products.
import db

db.setup()

app = flask.Flask(__name__)


# also supports /products/?count=20&page=4
@app.route('/products/')
def products():
    """ return products, supports any number and offset """
    # users count from 1
    page = int(flask.request.args.get('page', '1'))
    # computer scientists from 0
    page -= 1
    count = int(flask.request.args.get('count', '10'))
    # this is wrong if we add/remove products while user is paginating
    return json.dumps(db.get_items_by_price(count, count*page))

@app.route('/products/kids')
def kids():
    """ return kids stuff """
    return json.dumps(filter(lambda x: x['kids'], db.get_items_by_price()))

@app.route('/products/<int:pid>/')
def by_id(pid):
    """ lookup by product id """
    # in list to be consistent with other methods
    return json.dumps([db.get_product(pid)])


if __name__ == '__main__':
    app.run(debug=True)
