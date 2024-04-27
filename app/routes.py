# Monday, 22 April 2024
from flask import render_template, flash, redirect, url_for,request
from app import flask_app
from app.form import LoginForm,SignUpForm
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
@login_required
def about():
    return render_template('about.html',title='About')


# View function for the login page
@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('about'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('about')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)


# View function for the signup page
@flask_app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

# route for the logout function
@flask_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('about'))