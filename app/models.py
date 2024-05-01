""" 
Everytime you add a class( i.e. Table ) or make changes to a class, 
run "flask db migrate -m "{your_message_here}"
and "flask db upgrade" 
to generate a new database migration
"""
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
    # Define the attributes
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # WriteOnlyMapped defines a collection meaning a one to many relationship
    # Define the relations
    puzzles: so.WriteOnlyMapped["Puzzle"] = db.relationship(back_populates="creator", lazy="dynamic")
    plays_games: so.WriteOnlyMapped["GameResult"] = db.relationship(back_populates="player", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"

# Puzzle table creation
class Puzzle(db.Model):
    puzzle_id = db.Column(db.Integer, primary_key=True)
    # word_id = db.Column(db.String(128), db.ForeignKey("Word.word_id"))
    puzzle_creator: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.user_id))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    creator: so.Mapped["User"] = db.relationship(back_populates="puzzles", lazy="dynamic")

    def __repr__(self):
        return f"<Puzzle {self.category}>"


# Results Table Creation
class GameResult(db.Model):
    puzzle_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(128))
    username = db.Column(db.String(64))
    time_spent = db.Column(db.Integer)
    score = db.Column(db.Integer)

    player: so.Mapped["User"] = db.relationship(back_populates="plays_games", lazy="dynamic")
    def __repr__(self):
        return f"<LeaderBoard {self.word} - {self.username}>"

# Word Table Creation
class Word(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    word_length = db.Column(db.Integer)
    word = db.Column(db.String(128))

    def __repr__(self):
        return f"<Word {self.word}>"