def test_ping(client):
    response = client.get('/ping')
    assert b"ping" in response.data
