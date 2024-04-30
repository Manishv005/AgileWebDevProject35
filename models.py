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
    password_hash = db.Column(db.String(128))

    puzzles = db.relationship("Puzzle", backref="creator", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Puzzle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    number_of_letters = db.Column(db.Integer)
    word = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Puzzle {self.category} {self.word}>"


""" 
Everytime you add a class( i.e. Table ) or make changes ot create a new table to this file, 
run "flask db migrate -m "{your_message_here}"
and "flask db upgrade" 
to generate a new database migration
"""


# Leaderboard Table Creation
class LeaderBoard(db.Model):
    word_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(128))
    username = db.Column(db.String(64))
    missed_trials = db.Column(db.Integer)
    time_spent = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __repr__(self):
        return f"<LeaderBoard {self.word} - {self.username}>"
