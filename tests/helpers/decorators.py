import application
from config import db

application.app.config['TESTING'] = True
application.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/products_test.db'
instance = application.app.test_client()


def create_db(fn):
    def wrapper(*args, **kwargs):
        db.drop_all()
        db.init_app(application.app)
        db.create_all()
        fn(*args, **kwargs)
    return wrapper
