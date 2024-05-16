from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
# The database is represented in the app by an instance
db = SQLAlchemy(flask_app)
# The database migration engine also has an instance
migrate = Migrate(flask_app, db,render_as_batch=True)
# The login manager for the app using the flask_login package
login = LoginManager(flask_app)
login.login_view = 'login'

from app import routes, models