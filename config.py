import os

class Config(object):
    SECRET_KEY = 'Password_Secret'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/app-weather-world'
    SQLALCHEMY_TRACK_MODIFICATIONS = False