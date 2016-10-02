import logging
from decimal import Decimal

import pytest

from schema import ProductSchema, PageSchema, ValidationException, ProductIdSchema

logging.disable(logging.CRITICAL)


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


def test_page_schema_null_page():
    page = PageSchema().load({'page': 0}).data['page']
    assert page == 1


def test_page_schema_negative_page():
    page = PageSchema().load({'page': -42}).data['page']
    assert page == 1


def test_page_schema_valid_page():
    page = PageSchema().load({'page': 100500}).data['page']
    assert page == 100500


def test_page_schema_empty_page():
    page = PageSchema().load({}).data['page']
    assert page == 1


def test_page_schema_garbage_instead_of_page():
    with pytest.raises(ValidationException):
        PageSchema().load({'page': 'GARBAGE'})


def test_prod_id_schema():
    prod_id = ProductIdSchema().load({'prod_id': 1}).data['prod_id']
    assert prod_id == 1


def test_prod_id_schema_id_is_empty():
    with pytest.raises(ValidationException):
        ProductIdSchema().load({})
