import os

class Config(object):
    SECRET_KEY = 'Password_Secret'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath(os.getcwd()) +'/database/User.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False