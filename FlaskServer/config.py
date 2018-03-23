# configuration

class Config(object):
    SECRET_KEY = '4af1ad90da71ab41e0e5010c85811ab8'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog?charset=utf8'