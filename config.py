import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

PAGINATED = 10

app = Flask(__name__)
app.config.from_object(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'product.db'),
    DEBUG=True,
    SECRET_KEY='uni',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'product.db')
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
db = SQLAlchemy(app)
