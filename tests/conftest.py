import pytest
from service.web import create_app
from service.api import Unisport
from service.constants import URL


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def api(requests_mock):
    # Price and id are string in original response!
    requests_mock.get(URL, json={'products': [
        {'price': '3', 'id': '1'},
        {'price': '2', 'id': '2'},
        {'price': '1', 'id': '3'},
        {'price': '4', 'id': '4'}
    ]})
    api = Unisport()
    return api
