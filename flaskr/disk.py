from flask import Blueprint

from gpiozero import DiskUsage

bp = Blueprint('disk', __name__, url_prefix='/disk')


@bp.route('/usage', methods=['GET'])
def usage():
    disk = DiskUsage()
    return str(disk.usage)
