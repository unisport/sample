from app import db


#creating DB model matching the .csv data.
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Integer)