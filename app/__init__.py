from flask import Flask, abort
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
    login_manager.login_view = 'auth.login'

    # jinja date format
    from .utility import format_datetime, created_datetime
    app.jinja_env.filters['format_datetime'] = format_datetime
    app.jinja_env.filters['created_datetime'] = created_datetime

    # blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .mybook import mybook as mybook_bp
    app.register_blueprint(mybook_bp, url_prefix='/mybook')

    return app


@login_manager.unauthorized_handler
def unauthorized():
    abort(401)
