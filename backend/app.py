from flask import Flask, render_template, request, redirect, url_for, flash, session
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

@app.route('/register', methods=["POST", "GET"])
@cross_origin
def register():
    if request.method == "POST":
        uname = request.form['username']
        email = request.form['email']
        pwd = request.form['password']

        user_data = User.query.filter_by(email=email).first()

        if user_data:
            flash("Email is Registered for another User!!! Try another Email.")
            return redirect(url_for('register'))

        else:
            new_user = User(username= uname, email=email, password=pwd)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration Successful")
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['POST, GET'])
@cross_origin
def login():
    if request.method== "POST":
        session['email'] = request.form['email']
        session['pwd'] = request.form['password']

        user_data = User.query.filter_by(email=session['email']).first()
        if not user_data:
            flash('User Does not Exist!!')
            return redirect(url_for("login"))

        else:
            pswd = user_data.password
            email = user_data.email
            if pswd == session['pwd']:
                url = '/dashboard'+ str(email)
                return redirect(url)
            else:
                flash("Incorrect Password. Try again!!")
    else:
        return render_template('login.html')


api.add_resource(UserAPI, '/api/users/', '/api/users/<int:user_id>')
api.add_resource(TrackerAPI, '/api/trackers/','/api/trackers/<int:tracker_id>/')#'/api/users/<int:user_id>/trackers/', '/api/users/<int:user_id>/trackers/<int:tracker_id>')
api.add_resource(LogAPI, )#'/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/', '/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/<int:log_id>')

if __name__ == '__main__':
    app.run(debug=True)
