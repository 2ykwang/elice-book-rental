from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import get_config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(get_config(config_name))

    db.init_app(app)
    app.jinja_env.filters['datetime'] = format_datetime
    
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    return app


def format_datetime(value, format=None):
    if format is None: 
        format = "%Y년 %m월 %d일"
        formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    else:
        formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
    return formatted