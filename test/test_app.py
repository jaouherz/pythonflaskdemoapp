import json
from flaskr import random_name


def test_index_route(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = '<h2 class="text-center">flask example ci/cd</h2>'
    assert expected in res.get_data(as_text=True)


def test_hello_route(app, client):
    # default route
    res = client.get('/hello')
    assert res.status_code == 308
    res = client.get('/hello/')
    assert res.status_code == 200
    expected = "Hello Anonymous."
    assert expected in res.get_data(as_text=True)
    # custom name
    res = client.get('/hello/test')
    assert res.status_code == 200
    expected = "Hello test."
    assert expected in res.get_data(as_text=True)
    # random name
    res = client.get('/hello/random')
    assert res.status_code == 200


def test_get_primes_route(app, client):
    res = client.get('/getPrime/')
    assert res.status_code == 200
    res = client.get('/getPrime/10')
    assert res.status_code == 200
    expected = '<p class="text-center">29</p>'
    assert expected in res.get_data(as_text=True)
    res = client.get('/getPrime/1001')
    assert res.status_code == 200
    expected = "Please select a natural number lower or equal to 1000."
    assert expected == res.get_data(as_text=True)
    
