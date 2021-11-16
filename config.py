import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 공통 부분
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    BOOK_PER_PAGE = 8
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               f"sqlite:///{os.path.join(basedir, 'data-dev.sqlite')}")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
                               f"sqlite:///{os.path.join(basedir, 'data-test.sqlite')}")


class ProductionConfig(Config): 
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               f"sqlite:///{os.path.join(basedir, 'data.sqlite')}")



__config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config(config_name):
    if config_name in __config:
        return __config[config_name]
    else:
        return __config['default']
