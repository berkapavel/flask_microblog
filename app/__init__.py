from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# flask configs
app = Flask(__name__)
app.config.from_object(Config)
# db config
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# login manager
login = LoginManager(app)
login.login_view = 'login'

# app router
from app import routes

