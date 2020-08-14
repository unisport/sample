from decimal import Decimal

import factory
import pytest
from django.urls import reverse


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'products.Product'

    name = factory.Sequence(lambda n: 'Product %d' % n)
    price = Decimal('123.45')
    image = 'https://baconmockup.com/600/600/'


@pytest.mark.django_db
class TestViews:
    def test_products(self, client):
        response = client.get(reverse('product-list'))
        assert response.status_code == 200

    def test_create_product(self, client):
        data = {
            'name': 'Product 1',
            'price': '123,45',
            'image': 'https://baconmockup.com/600/600/'
        }
        response = client.post(reverse('product-create'), data=data)
        assert response.status_code == 200

    def test_update_product(self, client):
        product = ProductFactory()
        old_name = product.name
        new_name = "New Product Name"
        assert old_name != new_name
        data = {
            'name': new_name,
            'price': product.price,
            'image': product.image
        }
        response = client.post(
            reverse('product-update', kwargs={'pk': product.pk}),
            data=data
        )
        assert response.status_code == 302
        product.refresh_from_db()
        assert product.name == new_name
