import pytest

from flaskr.cpu import temp


@pytest.mark.unit
def test_temp(mocker):
    def mock_temperature(self):
        return 40.0

    mocker.patch(
        'gpiozero.CPUTemperature.temperature',
        mock_temperature
    )

    temperature = temp()
    assert 40.0 == temperature
