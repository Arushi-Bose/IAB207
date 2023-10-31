from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # Password needs to be encrypted before being stored in the db
    password_hash = db.Column(db.String(255), nullable=False)
    # The comment relation will only be used if we need to link users and comments
    # comments = db.relationship('Comment', backref='user')
    
    # string print method
    def __repr__(self):
        return f"Name: {self.name}"
    
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Integer)