from flask import Blueprint

from gpiozero import DiskUsage

bp = Blueprint('disk', __name__, url_prefix='/disk')


@bp.route('/usage', methods=['GET'])
def usage():
    """
    Returns the current disk usage as percentage.
    """
    disk = DiskUsage()
    return str(disk.usage)
