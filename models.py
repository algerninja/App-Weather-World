from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    
    create_date = db.Column(db.DateTime, default=dt.datetime.now)


    def __init__(self, username, firstname, lastname, password, email):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = self.__create_pw(password)
        self.email = email


    def __create_pw(self, password):
        return generate_password_hash(password, method="sha256")


    def verify_password(self, password):
        return check_password_hash(self.password, password)

