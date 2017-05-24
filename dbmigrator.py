import productservice
import seeder
from unisport import app, db
from models import Product


def migrate():
    db.drop_all()
    db.create_all()
    seeder.run(db)

if __name__ == '__main__':
    migrate()
