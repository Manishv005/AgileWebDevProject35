# Monday, 22 April 2024
from flask import render_template, flash, redirect, url_for,request
from app import flask_app
from app.form import LoginForm,SignUpForm
from flask_login import current_user,login_user,logout_user,login_required
import sqlalchemy as sa 
from app import db
from app.models import User
from urllib.parse import urlsplit

# The routes for / and home using the view function home()
# A decorator(@flask_app) modifies the function that follows it.


# View function for the home page
@flask_app.route('/home')
@login_required
def home():
    # current_user is provided by Flask-Login and represents the logged-in user
    return render_template('home.html', title='Home', username=current_user.username)


# View function for the about page
@flask_app.route('/')
def about():
    return render_template('about.html',title='About')

# View function for the login page
@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Authenticate the user
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))

        # Check if user exists
        if user is None:
            flash('Invalid username', 'error')
        elif not user.check_password(form.password.data):
            # Check if the password is correct
            flash('Invalid password', 'error')
        else:
            # Log the user in
            login_user(user, remember=form.remember_me.data)
            
            # Redirect to the next page
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)
    
    # If form validation fails or authentication fails, render the login template again
    return render_template('login.html', title='Log In', form=form)



# View function for the signup page
@flask_app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!','success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

# View function for the Create page
@flask_app.route('/create')
def create():
    return render_template('create.html',title='Create Puzzles')

# View function for the Search page
@flask_app.route('/search')
def search():
    return render_template('search.html',title='Search Puzzles')

# route for the logout function
@flask_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('about'))

