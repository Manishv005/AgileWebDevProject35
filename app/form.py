from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User
from flask_wtf import FlaskForm



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if ' ' in username.data:
            raise ValidationError('Username cannot contain spaces.')
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')
    def validate_password(self, password):
        if ' ' in password.data:
            raise ValidationError('Password cannot contain spaces.')

        
class CreatePuzzleForm(FlaskForm):
    category = SelectField('Category', choices=[('fruits', "Fruits"), ('animals', "Animals"), ('countries', "Countries"), ('car_brands', "Car Brands")], validators=[DataRequired()])
    number_of_letters = IntegerField('Number of Letters', validators=[DataRequired()])
    word = StringField('Word', validators=[DataRequired()])
    submit = SubmitField('Create Puzzle')
