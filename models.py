from config import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3), default='DKK')
    delivery = db.Column(db.String, default='1-2 dage')
    kids = db.Column(db.SmallInteger, default=0)
    name = db.Column(db.Text)
    package = db.Column(db.SmallInteger, default=0)
    kid_adult = db.Column(db.SmallInteger, default=0)
    free_porto = db.Column(db.SmallInteger, default=0)
    image = db.Column(db.Text)
    sizes = db.Column(db.Text, default='One Size')
    price = db.Column(db.Float, default=0)
    url = db.Column(db.Text, default=0)
    online = db.Column(db.SmallInteger, default=0)
    price_old = db.Column(db.Float, default=0)
    img_url = db.Column(db.Text)
    women = db.Column(db.SmallInteger, default=0)

    def __repr__(self):
        return 'Product name: {}'.format(self.name)
