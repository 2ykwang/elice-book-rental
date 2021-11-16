from flask import (
    Flask,
)
from config import get_config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(get_config(config_name))
    
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app
