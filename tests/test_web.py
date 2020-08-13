from flask import url_for, json


class TestWeb:
    def test_products(self, client, api):
        response = client.get(url_for('products'))
        assert response.status_code == 200
        products = json.loads(response.data)
        assert len(products) == 4

    def test_products_pagination_page1(self, client, api):
        url = f"{url_for('products')}?page=1"
        response = client.get(url)
        assert response.status_code == 200
        products = json.loads(response.data)
        assert len(products) == 4

    def test_products_pagination_page2_is_empty(self, client, api):
        url = f"{url_for('products')}?page=2"
        response = client.get(url)
        assert response.status_code == 200
        products = json.loads(response.data)
        assert len(products) == 0

    def test_product(self, client, api):
        assert client.get(url_for('product', id=1)).status_code == 200

    def test_none_existing_product(self, client, api):
        assert client.get(url_for('product', id=5)).status_code == 404

    def test_index(self, client):
        assert client.get(url_for('index', id=1)).status_code == 200
