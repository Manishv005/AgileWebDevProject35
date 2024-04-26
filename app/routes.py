# Monday, 22 April 2024
from flask import render_template, flash, redirect, url_for,request
from app import flask_app
from app.form import LoginForm
from flask_login import current_user,login_user,logout_user,login_required
import sqlalchemy as sa 
from app import db
from app.models import User
from urllib.parse import urlsplit
# here we import the Flask instance object flask_app from the app package(app directory)

# The routes for / and index using the view function index()
# A decorator modifies the function that follows it.

# View function for the index page
@flask_app.route('/')
@flask_app.route('/about')
def about():
    return render_template('about.html',title='About')


# View function for the login page
@flask_app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)


# View function for the signup page
@flask_app.route('/signup')
def signup():
    return render_template('signup.html', title='SignUp')