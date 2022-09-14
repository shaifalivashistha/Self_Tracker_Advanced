from flask import Flask, render_template, request, redirect, url_for
from application.database import db
from flask_cors import CORS, cross_origin
from flask_restful import Api
import  json

from application.api import *

app = Flask(__name__)
CORS(app)



api = Api(app)

app.app_context().push()

app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livesess.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api.init_app(app)

@app.before_first_request
def database():
    db.create_all()


@app.route('/')
@cross_origin()
def home():
    return "The Tracker App is Running"

if __name__ == '__main__':
    app.run(debug=True)



api.add_resource(UserAPI, '/api/users/', '/api/users/<int:user_id>')
api.add_resource(TrackerAPI, '/api/trackers/','/api/trackers/<int:tracker_id>/')#'/api/users/<int:user_id>/trackers/', '/api/users/<int:user_id>/trackers/<int:tracker_id>')
api.add_resource(LogAPI, )#'/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/', '/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/<int:log_id>')
