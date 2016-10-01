import logging

import flask
from marshmallow import Schema, fields, pre_load
from marshmallow.decorators import post_dump, post_load

logger = logging.getLogger(__name__)


class ValidationException(Exception):
    pass


def error_handler(cls, error, data):
    if error:
        logger.error(error)
        raise ValidationException


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


class PageSchema(Schema):
    __error_handler__ = error_handler
    page = fields.Integer(default=1)

    @post_load
    def default_page(self, data, pass_original=True):
        if 'page' not in data or data['page'] <= 0:
            data.update({'page': 1})
        return data
