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
             word_id=new_word.word_id # Use the id of the newly created word
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
@flask_app.route('/search', methods=['GET', 'POST'])
def search():
    # Find the latest users to create a puzzle
    recent_puzzles_query = Puzzle.query.order_by(Puzzle.date_created.desc()).limit(10).all()
    recent_creators_list =[]
    for recent_puzzle in recent_puzzles_query:
        word = Word.query.get(recent_puzzle.word_id)
        recent_creator = User.query.get(recent_puzzle.user_id)
        recent_creators_list.append({"username":recent_creator.username,"creation_time":recent_puzzle.date_created,"category":word.category,"puzzle_id":recent_puzzle.puzzle_id})
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash("No such user found.", "error")
            # Display the search page again with an error message
            return render_template('search.html')

        

        # Find the latest puzzle associated with this user
        puz_list = Puzzle.query.filter_by(user_id=user.user_id).order_by(Puzzle.date_created.desc()).limit(6).all() # Return List

        if not puz_list:
            flash("No puzzles found for this user.", "error")
            return render_template('search.html')
        
    
        puzzle_list = []
        for puzzle in puz_list:
            word = Word.query.get(puzzle.word_id)
            if not word:
                flash("No word found for the latest puzzle.", "error")
                return render_template('search.html')
            puzzle_list.append({"puzzle_id":puzzle.puzzle_id,"category":word.category, "word_length":word.word_length,"word":word.word})
        '''
        if not word:
            flash("No word found for the latest puzzle.", "error")
            return render_template('search.html')

        # Redirect to a new page that displays the category and blanks for the word length
        return render_template('display_word.html', category=word.category, word_length=word.word_length,word=word.word)
        '''
    
        return render_template('search.html',username=username, puzzle_list=puzzle_list, recent_creators_list = recent_creators_list)
        
    else:
        # Handle GET request to show an empty search form
        return render_template('search.html', recent_creators_list = recent_creators_list)

# View function for the Search page
@flask_app.route('/display_word/<username>/<puzzle_id>')
def display_word(username,puzzle_id):
    if current_user.is_authenticated:
        puzzle = Puzzle.query.get(puzzle_id)
        if puzzle:
            word = Word.query.get(puzzle.word_id)
            return render_template('display_word.html',puzzle_id=puzzle_id, category=word.category, word_length=word.word_length,word=word.word)
        else:
            return render_template('search.html')
    else:
        return redirect(url_for("about"))

@flask_app.route('/game_result', methods=['POST'])
def game_result():
    if current_user.is_authenticated:
        if request.method == 'POST':
            data = request.get_json()  # Get JSON data from the request
            puzzle_id = data["puzzle_id"]
            time_taken = data["time_taken"]

            current_loggedin_user_id = current_user.user_id

            if time_taken is None or puzzle_id is None or current_loggedin_user_id is None:
                return jsonify({'Error': 'Internal server error'})
            
            # Assuming you want to give 100 points for the fastest time and reduce points as the time increases
            SCORE = 100
            score = SCORE - time_taken
        
            result = GameResult(
                puzzle_id = puzzle_id,
                user_id = current_loggedin_user_id,
                time_spent = time_taken,
                score = score,
            )
            db.session.add(result)
            db.session.commit()

            return jsonify({'message': 'Data received successfully'})
        else:
            return jsonify({'Error': 'Internal server error'})
    else:
        return redirect(url_for("about"))
    


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
