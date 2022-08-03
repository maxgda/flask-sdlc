import pytest

from flaskr.ping import ping


@pytest.mark.unit
def test_ping():
    response = ping()
    assert 'ping' == response


@pytest.mark.integration
def test_ping_call(client):
    response = client.get('/ping')
    assert b"ping" in response.data
