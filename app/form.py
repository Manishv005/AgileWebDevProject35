from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User
from flask_wtf import FlaskForm
from flask_login import current_user



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
        
class ProfileForm(FlaskForm):
        
    def validate_email(self, email):
        user = User.query.filter(User.email == email.data).first()
        if user and user.user_id != current_user.user_id:
            raise ValidationError('Please use a different email address.')
    
    def validate_username(self, username):
        user = User.query.filter(User.username == username.data).first()
        if user and user.user_id != current_user.user_id:
            raise ValidationError('Username already in use')
        
    username = StringField('Username', validators=[DataRequired(), validate_username])
    email = StringField('Email', validators=[DataRequired(), Email(), validate_email])
    password = PasswordField('Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Update')

    

        
class CreatePuzzleForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('', 'Select a Category'),
        ('fruits', 'Fruits'),
        ('animals', 'Animals'),
        ('countries', 'Countries'),
        ('car_brands', 'Car Brands'),
        ('colors', 'Colors')
    ], validators=[DataRequired()])

    word = SelectField('word', choices=[('', 'Select a Word')], validate_choice=False)
    submit = SubmitField('Create Puzzle')
