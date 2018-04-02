import os

class Config(object):

    SERVER_HOST = 'localhost'
    SERVER_PORT = 6000
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):

    ENV = 'prod'
    DEBUG = True

    if 'RDS_HOSTNAME' in os.environ:
        SQLALCHEMY_DATABASE_URI = f"postgres://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"