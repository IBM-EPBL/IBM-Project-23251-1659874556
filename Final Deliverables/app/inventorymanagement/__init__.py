from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '82e65b56c16931a98ff8341e28059a89'

#################User Login SQLAlchemy#################

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')
db = SQLAlchemy(app)

#################Products MySQL#################

app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
mysql = MySQL(app)
print("Connection done")
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from inventorymanagement import routes #to avoid circular imports issue