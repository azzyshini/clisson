import os

class Config(object):
    # Statement for enabling the development environment
    DEBUG = False
    TESTING = False

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'clisson'
    MYSQL_PASSWORD = 'clisson2017'
    MYSQL_DB = 'clisson_library'
    MYSQL_CHARSET = 'utf8mb4'
    MYSQL_USE_UNICODE = True

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False