# Monday, 22 April 2024
# Creates models used in the Database


from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa 
import sqlalchemy.orm as so 
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
# The database is represented using classes in Flask-SQLAlchemy
# These classes are mapped to actual rows in the database by the ORM engine
# Here, we create a User class, representing a User table in the database

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # Useful for debugging only, tells python how to print the objects of this class
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
''' 
Everytime you add a class( i.e. Table ), 
run "flask db migrate -m "{your_message_here}"
and "flask db upgrade" 
to generate a new database migration
'''