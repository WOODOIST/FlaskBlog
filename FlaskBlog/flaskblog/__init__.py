from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from .config import settings as st


app = Flask(__name__)


app.config['SECRET_KEY'] = st.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = st.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = st.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = st.MAIL_SERVER
app.config['MAIL_PORT'] = st.MAIL_PORT
app.config['MAIL_USE_TLS'] = st.MAIL_USE_TLS
app.config['MAIL_USERNAME'] = st.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = st.MAIL_PASSWORD
mail = Mail(app)

from . import routes