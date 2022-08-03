from flask import Blueprint

bp = Blueprint('ping', __name__, url_prefix='/ping')


@bp.route('', methods=['GET'])
def ping():
    return 'ping'
