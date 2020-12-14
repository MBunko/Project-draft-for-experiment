from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = "put secret key here"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.38.250/games'

db = SQLAlchemy(app)

from application import routes