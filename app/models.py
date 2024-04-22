# Monday, 22 April 2024
# Creates models used in the Database


from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


# The database is represented using classes in Flask-SQLAlchemy
# These classes are mapped to actual rows in the database by the ORM engine
# Here, we create a User class, representing a User table in the database

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256)) # Optional allows nulls
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)

    # Useful for debugging only, tells python how to print the objects of this class
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
''' 
Everytime you add a class( i.e. Table ), 
run "flask db migrate -m "{your_message_here}"
and "flask db upgrade" 
to generate a new database migration
'''