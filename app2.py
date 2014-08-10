""" Main flask-restfull app """

from flask import Flask, request
from flask.ext.restful import reqparse, Api, Resource
import db

app = Flask(__name__)
api = Api(app)

db.setup()
# shortcuts
sort_by = db.sort_by
pick_items = db.pick_items

#def abort_not_exist(pid):
#    if not db.exists(pid):
#        abort(404, message="product %d not found" % pid)


class Product(Resource):
    """ for getting, deleting and updateing a single existing product """

    def get(self, pid):
        return db.get_product(pid)

    def delete(self, pid):
        db.del_product(pid)
        return '%d deleted' % pid, 204

    def put(self, pid):
        json_data = request.get_json(force=True)
        db.update(pid, json_data)
        return db.get_product(pid), 201


class ProductList(Resource):
    """ for returning list of product and inserting a new product  """

    # request parser for handling /?page=4&?count=20
    parser = reqparse.RequestParser()
    parser.add_argument('page', type=int, default=1)
    parser.add_argument('count', type=int, default=10)

    def paginate(self, lst):
        args = self.parser.parse_args()
        # users count from 1, computer scientists from 0
        args.page -= 1
        return pick_items(lst, args.count, args.page*args.count)

    def get(self):
        return self.paginate(sort_by(db.get_all_products(), 'price'))

    def post(self):
        json_data = request.get_json(force=True)
        db.insert(json_data)
        return db.get_product(json_data['id']), 201

class ProductListSearch(ProductList):
    """ for searching in products, e.g /kids or /free_porto """
    def get(self, search):
        return self.paginate(
            sort_by(
                db.get_all_matching_products(**{str(search): True}),
                'price'))

api.add_resource(Product, '/products/<int:pid>/')
api.add_resource(ProductListSearch, '/products/<string:search>/')
api.add_resource(ProductList, '/products/')




if __name__ == '__main__':
    app.run(debug=True)
