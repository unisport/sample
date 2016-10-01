from decimal import Decimal
from config import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    package = db.Column(db.Integer)
    women = db.Column(db.Integer)
    price = db.Column(db.Numeric(asdecimal=True), default=Decimal('0.0'))
    price_old = db.Column(db.Numeric(asdecimal=True), default=Decimal('0.0'))
    online = db.Column(db.Integer)
    url = db.Column(db.String)
    image = db.Column(db.String)
    img_url = db.Column(db.String)
    delivery = db.Column(db.String)
    currency = db.Column(db.String)
    name = db.Column(db.String)
    sizes = db.Column(db.String)
    kids = db.Column(db.String)
    kid_adult = db.Column(db.Integer)
    free_porto = db.Column(db.Integer)
