from decimal import Decimal
from schema import ProductSchema


def test_deserialization_of_product():
    input_data = {
        'id': '1',
        'women': '0',
        'price': '0,00',
        'img_url': 'https://example.com/example.jpg',
        'price_old': '0,00',
        'online': '1',
        'url': 'https://example.com/example.jpg',
        'delivery': '1-2 dage',
        'currency': 'DKK',
        'kids': '0',
        'name': 'Gavekort',
        'sizes': 'One Size',
        'kid_adult': '0',
        'free_porto': '0',
        'image': 'https://example.com/exampl.jpg',
        'package': '0'
    }
    product = ProductSchema().load(input_data).data

    assert type(product['women']) == int
    assert type(product['price']) == Decimal
    assert type(product['price_old']) == Decimal
    assert type(product['img_url']) == unicode
    assert type(product['online']) == int
    assert type(product['url']) == unicode
    assert type(product['delivery']) == unicode
    assert type(product['id']) == int
    assert type(product['currency']) == unicode
    assert type(product['kids']) == int
    assert type(product['name']) == unicode
    assert type(product['sizes']) == unicode
    assert type(product['kid_adult']) == int
    assert type(product['free_porto']) == int
    assert type(product['image']) == unicode
    assert type(product['package']) == int


def test_deserialization_of_multiple_product():
    input_data = [
        {
            'id': '1',
            'women': '0',
            'price': '0,00',
            'img_url': 'https://example.com/example.jpg',
            'price_old': '0,00',
            'online': '1',
            'url': 'https://example.com/example.jpg',
            'delivery': '1-2 dage',
            'currency': 'DKK',
            'kids': '0',
            'name': 'Gavekort',
            'sizes': 'One Size',
            'kid_adult': '0',
            'free_porto': '0',
            'image': 'https://example.com/exampl.jpg',
            'package': '0'
        },
        {
            'id': '2',
            'women': '0',
            'price': '0,00',
            'img_url': 'https://example.com/example.jpg',
            'price_old': '0,00',
            'online': '1',
            'url': 'https://example.com/example.jpg',
            'delivery': '1-2 dage',
            'currency': 'DKK',
            'kids': '0',
            'name': 'Gavekort',
            'sizes': 'One Size',
            'kid_adult': '0',
            'free_porto': '0',
            'image': 'https://example.com/exampl.jpg',
            'package': '0'
        }
    ]

    products = ProductSchema().load(input_data, many=True).data

    assert len(products) == 2
    for product in products:
        assert type(product['women']) == int
        assert type(product['price']) == Decimal
        assert type(product['price_old']) == Decimal
        assert type(product['img_url']) == unicode
        assert type(product['online']) == int
        assert type(product['url']) == unicode
        assert type(product['delivery']) == unicode
        assert type(product['id']) == int
        assert type(product['currency']) == unicode
        assert type(product['kids']) == int
        assert type(product['name']) == unicode
        assert type(product['sizes']) == unicode
        assert type(product['kid_adult']) == int
        assert type(product['free_porto']) == int
        assert type(product['image']) == unicode
        assert type(product['package']) == int
