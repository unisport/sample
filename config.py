import os


# Config object that handles all the app configs.
class Config(object):
    SECRET_KEY = os.urandom(28)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRODUCTS_PER_PAGE = 10
