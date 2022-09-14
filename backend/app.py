from flask import Flask, render_template, request, redirect, url_for
from application.api import api
from application.database import db
from flask_cors import CORS
import  json

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livesess.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.init_app(app)
db.init_app(app)

@app.before_first_request
def database():
    db.create_all()


@app.route('/')
def home():
    return "The Tracker App is Running"

if __name__ == '__main__':
    app.run(debug=True)