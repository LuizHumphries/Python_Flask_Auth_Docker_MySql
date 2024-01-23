from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # model cfg
    # id: int, username: string, password: string

    id = db.Column(db.Integer, primary_key=True) #unique key
    username = db.Column(db.String(80), nullable=False, unique=True) #unique username
    password = db.Column(db.String(80), nullable=False)

    

