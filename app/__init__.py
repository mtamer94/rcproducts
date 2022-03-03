from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'rocketchips1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


#login instance
login = LoginManager(app)
login.login_view = 'login'

# authorized_users = {1:'mtamer@rocketchips.com',2:'jpierce@rocketchips.com',3:'tjwhitney@rocketchips.com',4:'awong@fusionww.com'}

