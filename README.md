# Project : # AgileWebDevProject : PuzzleMe

## Author : Group 35
Date: May 2024

### UWA ID | Name | github user name
#### 23817492 | Manish Varada Reddy | Manishv005
#### 23762917 | Nishan Devkar | nishandevkar 
#### 23925353 | Sandeep Kumar | kumars21
#### 24139368 | Krish Goti | krishgoti2002


## Purpose of the PuzzleMe

PuzzleMe is a dynamic online platform designed to ignite the minds of puzzle enthusiasts and creators alike. 
At the heart of PuzzleMe is the ability for users to both craft and solve puzzles, creating a vibrant community of interactive engagement and intellectual challenge. 
Our platform encourages users to express their creativity by designing unique puzzles, ranging from simple riddles to complex crosswords and brain teasers.

## Application Design
PuzzleMe is developed using the following tech stack:

* HTML5
* CSS
* Bootstrap
* jQuery
* AJAX
* Flask
* Websockets
* SQLite (accessed via the SQLAlchemy package)

###  Unit Testing: Pytest

### Code Repository: GIT

### Issue Management: GIT/Issues


## Main Features

The PuzzleMe have the following features.

### User Management

* Signup: New users can register for an account.
* Login | Logout: Existing users can log in and out of their accounts.
* Profile Editing: Users can update their email and password.

### Create Puzzles

* Logged in users can create puzzles based on provided categories and words.


### Search Puzzles

* Created puzzles are available in "Search Puzzles".
* Players can select a user and view all the puzzles created by them to start playing.

### Play the Puzzle

* Users have to guess the word by selecting letters one at a time.
* Each correctly guessed letter will replace a corresponding dash (-) in the word.
* Each incorrect guess will contribute to the drawing of the hangman.
* The game ends in success if the user correctly guesses all letters of the word before the hangman is fully drawn.
* The game ends in failure if the hangman is fully drawn before the word is guessed.
* A timer starts at the beginning of each game and stops when the game ends. 
* The time taken affects the user's score and ranking on the leaderboard.

### Leaderboard
* The leaderboard displays the top 10 players who have scored the highest in the game.
* Usernames, total scores, and player ranks are displayed.
* As users play more games and gain points, their score and rank will be updated.
* Additional features include the ability to zoom in/out, capture screenshots of the leaderboard, etc.

### Puzzle Algorithm
Rules to play the game:

1. Guess the Word: Select letters one at a time to guess the word.

2. Replace Dashes: Each correctly guessed letter will replace a corresponding dash (-) in the word.

3. Drawing Hangman: Each incorrect guess will contribute to drawing the hangman.

4. Success Condition: The game ends successfully if all letters of the word are correctly guessed before the hangman is fully drawn.

5. Failure Condition: The game ends in failure if the hangman is fully drawn before the word is guessed.

6. Timer: The timer starts at the beginning of each game and stops when the game ends. The time taken affects the user's score and ranking on the leaderboard.


## Development Setup Instructions

### For Unix-based Systems (e.g., macOS, Linux)

1. First, set up the virtual environment using the command:

    ```
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

3. Install all the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Deactivate and reactivate the virtual environment to ensure proper activation:

    ```
    deactivate
    source venv/bin/activate
    ```

5. Run the Flask app:

    ```
    flask run
    ```

    This will provide you with a link to the app running on localhost:5000, which you can then open in a web browser.

### For Windows Systems

1. First, set up the virtual environment using the command:

    ```
    python -m venv venv
    ```

2. Activate the virtual environment:

    ```
    venv\Scripts\activate
    ```

3. Install all the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Deactivate and reactivate the virtual environment to ensure proper activation:

    ```
    deactivate
    venv\Scripts\activate
    ```

5. Run the Flask app:

    ```
    flask run
    ```

    This will provide you with a link to the app running on localhost:5000, which you can then open in a web browser.

## Testing Setup Instructions
"Will add them"