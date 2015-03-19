"""
App builder for flask-locate. Can be imported and used to start the site
"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
import logging

from config import config

bootstrap = Bootstrap()

def create_app(config_name):
    """
    Creates the flask app with specified config
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)

    from .main import main
    app.register_blueprint(main)

    return app
