from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from helpers import DecimalJSONEncoder

app = Flask(__name__)
app.json_encoder = DecimalJSONEncoder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/products.db'
app.config.update(DATABASE='data.json')
db = SQLAlchemy(app)
