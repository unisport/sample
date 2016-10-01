import flask
from marshmallow import Schema, fields, pre_load
from marshmallow.decorators import post_dump


class ProductSchema(Schema):
    id = fields.Integer()
    package = fields.Integer()
    women = fields.Integer()
    price = fields.Decimal(places=3)
    img_url = fields.Url()
    price_old = fields.Decimal(places=3)
    online = fields.Integer()
    url = fields.Url()
    delivery = fields.String()
    currency = fields.String()
    kids = fields.Integer()
    name = fields.String()
    sizes = fields.String()
    kid_adult = fields.Integer()
    free_porto = fields.Integer()
    image = fields.Url()

    @pre_load
    def format_price(self, data):
        data['price'] = data['price'].replace(',', '.')
        data['price_old'] = data['price_old'].replace(',', '.')
        return data

    @post_dump(pass_many=True)
    def jsonify(self, data, many):
        return flask.jsonify(data)
