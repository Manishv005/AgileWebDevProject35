# Monday, 22 April 2024
from flask import jsonify, render_template, flash, redirect, url_for, request
from app import flask_app
from app.form import LoginForm, SignUpForm, CreatePuzzleForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User, GameResult, Word, Puzzle
from urllib.parse import urlsplit

# The routes for / and home using the view function home()
# A decorator(@flask_app) modifies the function that follows it.


# View function for the home page
@flask_app.route("/home")
@login_required
def home():
    # current_user is provided by Flask-Login and represents the logged-in user
    return render_template("home.html", title="Home", username=current_user.username)


# View function for the about page
@flask_app.route("/")
def about():
    return render_template("about.html", title="About")


# View function for the login page
@flask_app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        # Authenticate the user
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )

        # Check if user exists
        if user is None:
            flash("Invalid username")
            return redirect(url_for("login"))

        # Check if the password is correct
        if not user.check_password(form.password.data):
            flash("Invalid password")
            return redirect(url_for("login"))

        # Log the user in
        login_user(user, remember=form.remember_me.data)

        # Redirect to the next page
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("home")
        return redirect(next_page)
    return render_template("login.html", title="Log In", form=form)


# View function for the signup page
@flask_app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign Up", form=form)


# View function for the Create page
@flask_app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = CreatePuzzleForm()
    if form.validate_on_submit():
        # Retrieve the word from the form data
        selected_word = form.word.data

        # Create a new Word using data from the form
        new_word = Word(
            category=form.category.data,
            word=selected_word,
            word_length=len(selected_word)  # Calculate word length dynamically
        )
        db.session.add(new_word)
        db.session.commit()

        # Create a new Puzzle instance using data from the form
        new_puzzle = Puzzle(
            user_id=current_user.user_id,
            word_id=new_word.id # Use the id of the newly created word
        )
        db.session.add(new_puzzle)
        db.session.commit()  # Commit the session to save the puzzle to the database
        flash("Puzzle created successfully!", "success")
        return redirect(url_for("home"))  # Redirect to the home page after successful creation

    # Render the create.html template with the form
    return render_template("create.html", title="Create Puzzles", form=form)

# Word Creation and AJAX to fetch the word based on category selected.
@flask_app.route('/get_words/')
def get_words():
    category = request.args.get('category', '', type=str)
    words_dict = {
        'fruits': [
            "Apple", "Blueberry", "Mandarin", "Pineapple", "Pomegranate",
            "Watermelon", "Kiwi", "Guava", "Mango", "Apricot", "Cherry"
        ],
        'animals': [
            "Hedgehog", "Rhinoceros", "Squirrel", "Panther", "Walrus",
            "Zebra", "Elephant", "Giraffe", "Kangaroo", "Lion", "Tiger"
        ],
        'countries': [
            "India", "Hungary", "Kyrgyzstan", "Switzerland", "Zimbabwe",
            "Dominica", "Nepal", "Australia", "Morocco", "Portugal", "Brazil"
        ],
        'car_brands': [
            "Toyota", "Honda", "Ford", "Chevrolet", "Tesla",
            "Nissan", "BMW", "Mercedes", "Audi", "Volkswagen", "Porsche"
        ],
        'colors': [
            "Red", "Blue", "Green", "Yellow", "Orange",
            "Purple", "Black", "White", "Pink", "Gray", "Cyan"
        ]
    }
    words = words_dict.get(category, [])
    return jsonify(words)


# View function for the Search page
@flask_app.route("/search")
def search():
    return render_template("search.html", title="Search Puzzles")


# route for the logout function
@flask_app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("about"))


# LeaderBoard changes


@flask_app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", title="Leaderboard")


@flask_app.route("/get_leaderboard")
def get_leaderboard():
    leaderTable = GameResult.query.all()
    data = [{"username": entry.user_id, "score": entry.score} for entry in leaderTable]
    return jsonify(data)
