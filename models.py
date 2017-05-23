from unisport import db


# product model schema
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    is_customizable = db.Column(db.Boolean(0))
    delivery = db.Column(db.String(80))
    kids = db.Column(db.Boolean(0))
    name = db.Column(db.String(250))
    sizes = db.Column(db.String(250))
    free_porto = db.Column(db.Boolean(0))
    kid_adult = db.Column(db.Boolean(0))
    image = db.Column(db.String(250))
    package = db.Column(db.Boolean(0))
    price = db.Column(db.Float())
    url = db.Column(db.String(250))
    online = db.Column(db.Boolean(0))
    price_old = db.Column(db.Float())
    img_url = db.Column(db.String(250))
    women = db.Column(db.Boolean(0))

    # convert sqlalchemy object to dictionary
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
