from flask_login import UserMixin
from datetime import datetime
from . import db

class User(db.Model, UserMixin):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # Password needs to be encrypted before being stored in the db
    password_hash = db.Column(db.String(255), nullable=False)
    # The comment relation will only be used if we need to link users and comments
    #comments = db.relationship('Comment', backref='user')
    
    # string print method
    def __repr__(self):
        return f"Name: {self.name}"