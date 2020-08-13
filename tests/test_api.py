import pytest


class TestUnisport:
    def test_fetch_products(self, api):
        api.fetch_products()
        assert len(api.products) == 4

    def test_sort_products(self, api):
        api.fetch_products()
        # Test products are not sorted by price
        assert ['3', '2', '1', '4'] == [p['price'] for p in api.products]
        api.sort_products()
        assert ['1', '2', '3', '4'] == [p['price'] for p in api.products]

    def test_get_products(self, api):
        products = api.get_products()
        assert len(products) == 4
        products = api.get_products(page=2)
        assert len(products) == 0

    def test_get_kids_products(self, api):
        with pytest.raises(NotImplementedError):
            api.get_kids_products()

    def test_get_product(self, api):
        product = api.get_product(1)
        assert product == {'price': '3', 'id': '1'}

    def test_get_none_existing_product(self, api):
        product = api.get_product(5)
        assert product is None
