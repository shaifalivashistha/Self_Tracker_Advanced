import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    jsonify,
)
from application.database import db
from application.models import *
from application.validation import *
from flask_restful import Api
from flask_cors import CORS
from flask_security import (
    SQLAlchemyUserDatastore,
    Security,
    auth_required,
    current_user,
    hash_password,
)

import logging


from application.api import *

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


app = Flask(__name__)

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trackerdb.sqlite3"
app.config["SECRET_KEY"] = "Th1s1sas3cr3tk3y"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECURITY_PASSWORD_HASH"] = "bcrypt"
app.config["SECURITY_PASSWORD_SALT"] = "S3cr3tPassword"
app.config["SECURITY_TOKEN_AUTHENTICATION_HEADER"] = "Authentication-Token"
# app.config["SECURITY_REGISTERABLE"] = True
# app.config["SECURITY_CONFIRMABLE"] = False
# app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
# app.config["SECURITY_UNAUTHORIZED_VIEW"] = None
# app.config["SECURITY_POST_LOGIN_VIEW"] = "/dashboard/email"
app.config["WTF_CSRF_ENABLED"] = False
# app.config["SECURITY_REDIRECT_HOST"] = "localhost:8080"
db.init_app(app)
api.init_app(app)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.before_first_request
def database():
    db.create_all()


@app.before_first_request
def create_user():
    if not user_datastore.find_user(email="shaifali@abc.com"):
        user_datastore.create_user(
            email="shaifali@abc.com",
            username="Shaifali",
            password=hash_password("1602RS"),
        )
    db.session.commit()


@app.route("/")
def home():
    return "The Tracker App is Running"


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        print("post in register")
        print(request.headers)
        data = request.get_json()
        print("DATA: ", data)
        uname = data["username"]
        email = data["email"]
        pwd = data["password"]
        print(uname, email, pwd)

        user_data = User.query.filter_by(email=email).first()

        if user_data:
            print(user_data)
            flash("Email is Registered for another User!!! Try another Email.")
            return redirect(url_for("register"))

        else:
            print("no existing user data")
            user_datastore.create_user(
                email=email,
                username=uname,
                password=hash_password(pwd),
            )
            # new_user = User(username=uname, email=email, password=pwd)
            # new_user = User(username="uname", email=email, password=pwd)
            # db.session.add(new_user)
            db.session.commit()
            flash("Registration Successful")
            return redirect(url_for("login"))
            # return jsonify("abc")
    else:
        return redirect(url_for("register"))


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
                print("Sending...")
                return redirect(url_for("dashboard", email=str(email)))
            else:
                flash("Incorrect Password. Try again!!")
                return redirect(url_for("login"))
    else:
        print("Receiving")
        return redirect(url_for("login"))


@app.route("/dashboard/<email>")
# @auth_required
def dashboard(email):
    user_data = User.query.filter_by(email=email).first()
    username = user_data.username
    trackers = user_data.trackers
    print("Here")
    return redirect(
        url_for("dashboard", email=email, tracekrs=trackers, username=username)
    )


@app.route("/logout")
def logout():
    session["user"] = None
    return redirect(url_for("login"))


# @app.route("/dashboard/<email>/create_tracker", methods=["POST", "GET"])
# def create_tracker(email):
#     if request.method == "GET":

#         return redirect(url_for("trackers"))
#     if request.method == "POST":

#         Name = request.form.get("_name_")
#         Description = request.form.get("_description_")
#         Tracker_type = request.form.get("_type_")

#         new_tracker = Tracker(
#             name=Name, description=Description, tracker_type=Tracker_type
#         )
#         user = User.query.filter_by(username=username).first()
#         user.trackers.append(new_tracker)
#         db.session.add(new_tracker)
#         db.session.commit()
#         return redirect(f"/{username}/dashboard")


api.add_resource(UserAPI, "/api/users/", "/api/users/<int:id>")
api.add_resource(
    TrackerAPI, "/api/trackers/", "/api/trackers/<int:tracker_id>/"
)  #'/api/users/<int:user_id>/trackers/', '/api/users/<int:user_id>/trackers/<int:tracker_id>')
api.add_resource(
    LogAPI,
)  #'/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/', '/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/<int:log_id>')

if __name__ == "__main__":
    app.run(debug=True)


# import os
# from flask import Flask
# from flask_restful import Resource, Api
# from application.config import LocalDevelopmentConfig
# from application.database import db
# from sqlalchemy.orm import scoped_session, sessionmaker
# from flask_security import (
#     Security,
#     SQLAlchemySessionUserDatastore,
#     SQLAlchemyUserDatastore,
# )
# from application.models import User, Role
# from flask_login import LoginManager
# from flask_cors import CORS
# from flask_security import utils

# from application.api import *


# import logging


# app = None
# api = None


# def create_app():
#     app = Flask(__name__, template_folder="templates")
#     CORS(app)

#     if os.getenv("ENV", "development") == "production":
#         app.logger.info("Currently no production config is setup.")
#         raise Exception("Currently no production config is setup.")
#     else:
#         app.logger.info("Staring Local Development.")
#         print("Staring Local Development")
#         app.config.from_object(LocalDevelopmentConfig)
#     db.init_app(app)
#     app.app_context().push()
#     app.logger.info("App setup complete")
#     # Setup Flask-Security
#     user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
#     security = Security(app, user_datastore)
#     # user_datastore.create_user(username="thejeshgn",email='i@thejeshgn.com', password=utils.hash_password('password'), active=1)
#     # db.session.commit()
#     api = Api(app)
#     app.app_context().push()
#     return app, api


# app, api = create_app()

# api.add_resource(UserAPI, "/api/users/", "/api/users/<int:id>")
# api.add_resource(TrackerAPI, "/api/trackers/", "/api/trackers/<int:id>/")
# #     "/api/users/<int:id>/trackers/",
# #     "/api/users/<int:id>/trackers/<int:id>",
# # )
# api.add_resource(LogAPI, "/api/logs/", "/api/logs/<int:id>")
# #     "/api/users/<int:id>/trackers/<int:id>/logs/",
# #     "/api/users/<int:id>/trackers/<int:id>/logs/<int:id>",
# # )

# if __name__ == "__main__":
#     app.run(debug=True)
