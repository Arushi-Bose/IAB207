from flask_login import UserMixin
from . import db

class User(db.Model):
    __tablename__ == 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
