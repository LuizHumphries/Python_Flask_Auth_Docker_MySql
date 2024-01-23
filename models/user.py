from flask_login import UserMixin
from database import db

class User(db.Model, UserMixin):
    """ Default model for User in the db """
    # model cfg
    # id: int, username: string, password: string

    id = db.Column(db.Integer, primary_key=True) #unique key
    username = db.Column(db.String(80), nullable=False, unique=True) #unique username
    password = db.Column(db.String(80), nullable=False)