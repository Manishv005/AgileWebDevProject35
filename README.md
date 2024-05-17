# Project : AgileWebDevProject : PuzzleMe

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

* Unit Testing: Pytest & Selenium 

* Code Repository: GIT

* Issue Management: GIT/Issues


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

## PuzzleMe Architecture Summary

PuzzleMe is a dynamic online platform that allows users to create, search, and play puzzles. The platform is built using a combination of frontend and backend technologies to provide a seamless user experience. With a user-friendly interface, robust backend logic, and efficient deployment, PuzzleMe provides an enjoyable experience for puzzle enthusiasts and creators alike.


### Frontend Architecture
The frontend of PuzzleMe is designed to provide an interactive and intuitive user interface. It utilizes HTML5, CSS, Bootstrap, and jQuery for layout, styling, and dynamic content generation. AJAX and Flask is used for asynchronous communication with the backend, enabling seamless updates and interactions without page reloads.

#### Key Components:
* HTML5: Provides the structure of web pages.
* CSS & Bootstrap: Handle styling and layout of the web application, ensuring a responsive design across different devices.
* jQuery: Enables dynamic and interactive elements on the frontend, such as form validation and event handling.
* AJAX: Facilitates asynchronous communication with the backend server, allowing for real-time updates without full page reloads.

 ### Backend Architecture
The backend of PuzzleMe is powered by Flask, a lightweight web framework for Python. It handles user authentication, puzzle creation, search functionality, and gameplay logic. The backend also interacts with a SQLite database through the SQLAlchemy package for data storage and retrieval.

#### Key Components:
* Flask: Provides the foundation for building web applications in Python, handling routing, request handling, and response generation.
* SQLite & SQLAlchemy: Utilized for database management, storing user information, puzzle data, and leaderboard scores.
* Websockets: Used for real-time communication between the client and server, particularly during gameplay to update the puzzle status and timer.
* Unit Testing (Pytest): Ensures the reliability and correctness of the backend codebase through automated testing.

### Deployment Architecture
PuzzleMe is deployed on local server which can be accessed after running the application as per getting started instruction below.

#### Key Components:
* Server Environment: Provides the infrastructure for hosting the PuzzleMe application.
* Database Server: Hosts the SQLite database containing user profiles, puzzle data, and leaderboard scores.
* Issue Management (GIT/Issues): Tracks and manages bugs, pull request, team intrecation, feature requests, and tasks related to the project's development and maintenance.
* Code Repository (GIT): Stores the source code of PuzzleMe, allowing for version control and collaboration among developers.


## Getting Started for contribution 

* Clone the repository from GIT Repository : https://github.com/Manishv005/AgileWebDevProject35

* Create a new branch ( Example : git checkout -b feature/new-feature).
* Make your changes and commit them ( Example : git commit -am 'Add new feature').
* Push to the branch (Example : git push origin feature/new-feature).
* Create a new Pull Request.
* Run the application on your local machine.

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
Selenium Testing:

Run the Flask app in one terminal window:
```
flask run

```
Run the tests in another terminal window:
```
pytest app/selenium_tests/
```
This will execute all the tests located in the app/selenium_tests/ directory and provide a report of the test results.

