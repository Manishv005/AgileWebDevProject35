# Monday, 22 April 2024

from app import flask_app
# here we import the Flask instance object flask_app from the app package(app directory)

# The routes for / and index using the view function index()
# A decorator modifies the function that follows it.

@flask_app.route('/')
@flask_app.route('/index')

# View function for the index page
def index():
    return 'Agile Web Development Group Project'