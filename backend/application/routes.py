from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask import current_app as app
from application.models import *
from flask_security import login_required, roles_accepted, roles_required


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


# @app.route("dashboard/<user>/create_tracker", methods = ["POST", "GET"])
# def create_tracker(user):
#     if request.method == 'GET':

#         return render_template('create_tracker.html',username=user)
#     if request.method=="POST":
#         Name=request.form.get("_name_")
#         Description=request.form.get("_description_")
#         Tracker_type=request.form.get("_type_")

#         new_tracker=tracker(name=Name, description=Description, tracker_type=Tracker_type)
#         user = user_model.query.filter_by(username=username).first()
#         user.trackers.append(new_tracker)
#         db.session.add(new_tracker)
#         db.session.commit()
#         return redirect(f"/{username}/dashboard")
