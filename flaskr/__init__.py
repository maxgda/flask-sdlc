from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import ping
    app.register_blueprint(ping.bp)

    return app
