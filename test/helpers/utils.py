from model.product import Product


def add_product(db, **kwargs):
    default_product = {}
    default_product.update(**kwargs)
    db.session.add(Product(**default_product))
    db.session.commit()
