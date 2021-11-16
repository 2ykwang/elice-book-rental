from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import get_config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(get_config(config_name))

    db.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)
    return app
