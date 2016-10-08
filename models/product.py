from decimal import Decimal
from config import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    package = db.Column(db.Boolean)
    women = db.Column(db.Boolean)
    price = db.Column(db.Numeric(asdecimal=True), default=Decimal('0.0'))
    price_old = db.Column(db.Numeric(asdecimal=True), default=Decimal('0.0'))
    online = db.Column(db.Boolean)
    url = db.Column(db.String)
    image = db.Column(db.String)
    img_url = db.Column(db.String)
    delivery = db.Column(db.String)
    currency = db.Column(db.String)
    name = db.Column(db.String)
    sizes = db.Column(db.String)
    kids = db.Column(db.Boolean)
    kid_adult = db.Column(db.Boolean)
    free_porto = db.Column(db.Boolean)
