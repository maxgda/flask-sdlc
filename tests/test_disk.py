import pytest

from flaskr.disk import usage


@pytest.mark.unit
def test_usage(mocker):
    mock_disk = mocker.patch('flaskr.disk.DiskUsage')
    mock_disk.return_value.usage = 20.0

    percent = usage()
    assert '20.0' == percent


@pytest.mark.integration
def test_usage_call(mocker, client):
    mock_disk = mocker.patch('flaskr.disk.DiskUsage')
    mock_disk.return_value.usage = 20.0

    response = client.get('/disk/usage')
    assert b'20.0' == response.data
