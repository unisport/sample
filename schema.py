from marshmallow import Schema, fields, pre_load


class ProductSchema(Schema):
    id = fields.Integer()
    package = fields.Integer()
    women = fields.Integer()
    price = fields.Decimal()
    img_url = fields.Url()
    price_old = fields.Decimal()
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


class ProductSchemaDump(Schema):
    pass
