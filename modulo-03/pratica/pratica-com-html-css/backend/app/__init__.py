from uuid import uuid4
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = uuid4().hex
    from .web import web_blueprint
    app.register_blueprint(web_blueprint)
    return app
