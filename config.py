import os

class Config(object):
    DEBUG = False
    SECRET_KEY = 'Password_Secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://eopkmcubumsoyz:a8cf0dc2877529a94d9ee8e65189a42fae97e6c1d749019d5b6776c6c76a4fcf@ec2-54-147-98-183.compute-1.amazonaws.com:5432/d9ca0eo8dvmvn5'



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgre:password@localhost/app-weather-world'