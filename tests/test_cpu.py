import pytest

from flaskr.views.cpu import temp, temp_error


@pytest.mark.unit
def test_temp(mocker):
    mock_cpu = mocker.patch('flaskr.views.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 40.0

    temperature = temp()
    assert '40.0' == temperature


@pytest.mark.unit
def test_temp_error_fine(mocker):
    mock_cpu = mocker.patch('flaskr.views.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 60.0

    error = temp_error()
    assert 'fine' == error


@pytest.mark.unit
def test_temp_error_too_hot(mocker):
    mock_cpu = mocker.patch('flaskr.views.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 60.1

    error = temp_error()
    assert 'too hot' == error


@pytest.mark.integration
def test_temp_call(mocker, client):
    mock_cpu = mocker.patch('flaskr.views.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 40.0

    response = client.get('/cpu/temp')
    assert b'40.0' == response.data


@pytest.mark.integration
def test_temp_error_call(mocker, client):
    mock_cpu = mocker.patch('flaskr.views.cpu.CPUTemperature')
    mock_cpu.return_value.temperature = 40.0

    response = client.get('/cpu/temp/error')
    assert b'fine' == response.data
