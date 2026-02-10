from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "dhab72898q2iwjdiwj22"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

dataBase = SQLAlchemy(app)
