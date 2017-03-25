# coding:utf8
# need python >= 2.7
from importlib import import_module
from flask import Flask

def create_app(config=None, name=None):
    if not name:
        name = __name__

    app = Flask(name)
    app.config.from_pyfile('config.py')

    configure_extensions(app)
    configure_views(app)
    return app


def configure_extensions(app):
    pass


def configure_views(app):
    for it  in app.config['BLUEPRINTS']:
        app.register_blueprint(import_module(it[0]).bp, url_prefix=it[1])