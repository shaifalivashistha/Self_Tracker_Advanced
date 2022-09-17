from flask import Flask, render_template, request, redirect, url_for, flash, session
from application.database import db
from application.models import *
from application.validation import *
from flask_cors import CORS, cross_origin
from flask_restful import Api
from flask_security import current_user, login_required


from application.api import *

app = Flask(__name__)
api = Api(app)
app.app_context().push()

CORS(app, origins="http://localhost:8080")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trackerdb.sqlite3"
app.config["SECRET_KEY"] = "Th1s1sas3cr3tk3y"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECURITY_PASSWORD_HASH"] = "bcrypt"
app.config["SECURITY_PASSWORD_SALT"] = "S3cr3tPassword"
app.config["SECURITY_REGISTERABLE"] = True
app.config["SECURITY_CONFIRMABLE"] = False
app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
app.config["SECURITY_UNAUTHORIZED_VIEW"] = None
app.config["SECURITY_POST_LOGIN_VIEW"] = "/dashboard/email"
app.config["WTF_CSRF_ENABLED"] = False
app.config["SECURITY_REDIRECT_HOST"] = "localhost:8080"
db.init_app(app)
api.init_app(app)


@app.before_first_request
def database():
    db.create_all()


@app.route("/")
def home():
    return "The Tracker App is Running"


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        print(request.headers)
        data = request.get_json()
        print("DATA: ", data)
        uname = data["username"]
        email = data["email"]
        pwd = data["password"]
        print(uname, email, pwd)

        user_data = User.query.filter_by(email=email).first()

        if user_data:
            flash("Email is Registered for another User!!! Try another Email.")
            return redirect(url_for("register"))

        else:
            new_user = User(username=uname, email=email, password=pwd)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration Successful")
            return redirect(url_for("login"))
    else:
        return render_template("/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.get_json()
        session["email"] = data["email"]
        session["pwd"] = data["password"]

        user_data = User.query.filter_by(email=session["email"]).first()
        if not user_data:
            flash("User Does not Exist!!")
            return redirect(url_for("login"))

        else:
            pswd = user_data.password
            email = user_data.email
            if pswd == session["pwd"]:
                return redirect(url_for("dashboard", email=str(email)))
            else:
                flash("Incorrect Password. Try again!!")
                return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))


@app.route("/dashboard/<email>", methods=["POST", "GET"])
# @auth_required
def dashboard(email):
    if request.method == "POST":
        return redirect(url_for("create_tracker"))
    else:
        return redirect(url_for("dashboard", email=email))


api.add_resource(UserAPI, "/api/users/", "/api/users/<int:id>")
api.add_resource(
    TrackerAPI, "/api/trackers/", "/api/trackers/<int:tracker_id>/"
)  #'/api/users/<int:user_id>/trackers/', '/api/users/<int:user_id>/trackers/<int:tracker_id>')
api.add_resource(
    LogAPI,
)  #'/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/', '/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/<int:log_id>')

if __name__ == "__main__":
    app.run(debug=True)
