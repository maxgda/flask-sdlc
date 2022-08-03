import pytest

from flaskr.cpu import temp


@pytest.mark.unit
def test_temp(mocker):
    mock_cpu = mocker.patch('flaskr.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 40.0

    temperature = temp()
    assert '40.0' == temperature


@pytest.mark.integration
def test_temp_call(mocker, client):
    mock_cpu = mocker.patch('flaskr.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 40.0

    response = client.get('/cpu/temp')
    assert b'40.0' == response.data
