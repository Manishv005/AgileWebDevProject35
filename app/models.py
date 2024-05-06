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
def load_user(user_id):
    return User.query.get(int(user_id))


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
    puzzles: so.WriteOnlyMapped["Puzzle"] = so.relationship(back_populates="creator", lazy="dynamic")
    plays_games: so.WriteOnlyMapped["GameResult"] = so.relationship(back_populates="solver", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.user_id)
    
    def __repr__(self):
        return f"<User {self.username}>"

# Word Table Creation
class Word(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    word_length = db.Column(db.Integer)
    word = db.Column(db.String(128))

    puzzle_word: so.Mapped["Puzzle"] = so.relationship(back_populates="has_word")
    def __repr__(self):
        return f"<Word {self.word}>"
    
# Puzzle table creation
class Puzzle(db.Model):
    puzzle_id = db.Column(db.Integer, primary_key=True)
    word_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Word.word_id),
                                               index=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.user_id),index=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    creator: so.Mapped["User"] = so.relationship(back_populates="puzzles")
    has_word: so.Mapped["Word"] = so.relationship(back_populates="puzzle_word")
    puzzle_result: so.Mapped["GameResult"] = so.relationship(back_populates="has_puzzle")
    
    def __repr__(self):
        return f"<Puzzle {self.puzzle_id} {self.user_id} {self.word_id}>"


# Results Table Creation
class GameResult(db.Model):
    result_id = db.Column(db.Integer, primary_key=True)
    puzzle_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Puzzle.puzzle_id),index=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.user_id),index=True)
    time_spent = db.Column(db.Integer)
    score = db.Column(db.Integer)

    solver: so.Mapped["User"] = so.relationship(back_populates="plays_games")
    has_puzzle: so.Mapped["Puzzle"] = so.relationship(back_populates="puzzle_result")

    def __repr__(self):
        return f"<GameResult {self.word} - {self.user_id}>"

