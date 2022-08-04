from flask import Blueprint

from gpiozero import CPUTemperature

bp = Blueprint('cpu', __name__, url_prefix='/cpu')


@bp.route('/temp', methods=['GET'])
def temp():
    """
    Returns the current CPU temperature in degrees celsius as a string.
    """
    cpu = CPUTemperature()
    return str(cpu.temperature)


@bp.route('/temp/error', methods=['GET'])
def temp_error():
    """
    Returns error message depending on CPU temperature.
    <= 60 degree Celsius -> "fine"
    >  60 degree Celsius -> "too hot"
    """
    cpu = CPUTemperature()

    if cpu.temperature > 60.0:
        return 'too hot'

    return 'fine'
