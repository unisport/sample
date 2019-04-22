import pytest
import requests
from app.get_data_from_api import request_api


#Status_code 200 ok when requesting the API.
@pytest.mark.get_reponse
def test_response():

    """
    GIVEN a request is made
    WHEN when the connection is established
    THEN status 200 ok is returned
    """""

    r = requests.get('https://www.unisport.dk/api/sample/')

    assert r.status_code == 200


#Datatype for the data object
@pytest.mark.test_api_data
def test_data():
    data = request_api()

    """
    GIVEN i access the data object
    WHEN i check the datatype of the object data
    THEN list is returned
    """""

    assert type(data) == list


#index 0 in data
@pytest.mark.test_api_data
def test_data():
    data = request_api()

    """
    GIVEN i access the data object
    WHEN i access index 0 in data
    THEN the key "name" returns index[0] 'Nike Mercurial Vapor 12 Elite FG Game Over - Gr\u00e5/Gul'
    """""

    assert data[0]['name'] == 'Nike Mercurial Vapor 12 Elite FG Game Over - Gr\u00e5/Gul'


#Are the keys "kid" and "kid_adult" are in the data object.
@pytest.mark.test_api_data
def test_data():
    data = request_api()

    """
    GIVEN i access the data object
    WHEN i query for "kids" and "kid_adult"
    THEN it returns None
    """""

    assert 'kids' not in data
    assert 'kid_adult' not in data
