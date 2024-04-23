# Monday, 22 April 2024
from flask import render_template, flash, redirect, url_for
from app import flask_app
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
    return render_template('login.html',title='Login')


# View function for the signup page
@flask_app.route('/signup')
def signup():
    return render_template('signup.html', title='SignUp')