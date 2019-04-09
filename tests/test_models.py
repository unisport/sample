import pytest
from app.models import Products
from app import db


#Add new product.
@pytest.mark.create_product
def test_create_product():

    """
    GIVEN a new product
    WHEN when the new product is created
    THEN the product is added to database
    """""

    new_product = Products(image='StringType', name='StringType', price=9999999)
    db.session.add(new_product)
    db.session.commit()

    assert new_product.image == 'StringType'
    assert new_product.name == 'StringType'
    assert new_product.price == 9999999

