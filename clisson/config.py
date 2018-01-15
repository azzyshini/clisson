import os

class Config(object):
    # Statement for enabling the development environment
    DEBUG = False
    TESTING = False

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'clisson'
    MYSQL_DATABASE_PASSWORD = 'clisson2017'
    MYSQL_DATABASE_DB = 'clisson_library'
    MYSQL_DATABASE_CHARSET = 'utf8mb4'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False