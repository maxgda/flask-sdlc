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
