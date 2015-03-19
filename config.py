import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = (os.environ.get('SECRET_KEY') or
                  'KwkxBiQbRCBMiCdYp}8yTTfQ^X{hmpU2M[wkFit3nxhwjiEm2e')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}