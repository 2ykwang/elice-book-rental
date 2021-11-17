from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import get_config
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    
    # load config
    app.config.from_object(get_config(config_name))
    
    # init
    db.init_app(app)
    login_manager.init_app(app)
    
    # jinja date format
    from .jinja_datetime import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    # blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app