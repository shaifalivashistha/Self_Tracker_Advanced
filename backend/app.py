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
from matplotlib.figure import Figure
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
            password=hash_password("1602RSsv"),
            sec_ques="Your Fav food",
            sec_ans="Rajma Chawal",
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
        sec_Q = data["sec_que"]
        sec_A = data["sec_ans"]
        print(uname, email, pwd)

        user_data = User.query.filter_by(email=email).first()

        if user_data:
            print(user_data)
            flash("Email is Registered for another User!!! Try another Email.")
            return redirect(url_for("register"))

        else:
            user_datastore.create_user(
                email=email,
                username=uname,
                password=hash_password(pwd),
                sec_ques=sec_Q,
                sec_ans=sec_A,
            )
            # new_user = User(username=uname, email=email, password=pwd)
            # new_user = User(username="uname", email=email, password=pwd)
            # db.session.add(new_user)
            db.session.commit()
            flash("Registration Successful")
            return redirect(url_for("login"))
            # return jsonify("abc")
    else:
        # print("RegisterPage")
        # return redirect(url_for("register"))
        return jsonify("Register Page")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.get_json()
        session["id"] = data["id"]
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
        # return redirect(url_for("login"))
        return "Login Page"


@app.route("/dashboard/<email>")
# @auth_required
def dashboard(email):
    print("App Dashboard")

    user_data = User.query.filter_by(email=email).first()
    username = user_data.username
    trackers = user_data.trackers
    print(user_data)
    print(trackers)
    # return redirect(
    #     url_for("dashboard", email=email, tracekrs=trackers, username=username)
    # )
    tr_list = []
    for tracker in trackers:
        tr_list.append(tracker)

    trck_dict = {}
    count = 0
    for i in tr_list:
        count += 1
        Dtrack = {
            "id": i.id,
            "name": i.name,
            "description": i.description,
            "type": i.type,
            "date_created": i.date_created,
        }
        trck_dict[count] = Dtrack
    print(trck_dict)

    return jsonify(trck_dict)


@app.route("/logout")
def logout():
    session["user"] = None
    return redirect(url_for("login"))


@app.route("/dashboard/<email>/create_tracker", methods=["POST", "GET"])
def create_tracker(email):
    if request.method == "POST":
        data = request.get_json()
        print("DATA :", data)
        Name = data["tracker_name"]
        Description = data["tracker_des"]
        Tracker_type = data["tracker_type"]

        new_tracker = Tracker(name=Name, description=Description, type=Tracker_type)
        print()
        user = User.query.filter_by(email=email).first()
        user.trackers.append(new_tracker)
        db.session.add(new_tracker)
        db.session.commit()
        print("Tracker Added Successfully")
        return redirect(url_for("dashboard", email=email))
    else:
        return jsonify(email)


@app.route("/<email>/update/<int:id>", methods=["GET", "POST"])
def update(email, id=None):

    trackers = Tracker.query.filter_by(id=id).first()
    if request.method == "POST":
        if trackers:
            Tracker_type = trackers.tracker_type
            db.session.delete(trackers)
            db.session.commit()
            data = request.json()
            name = data["tracker_name"]
            description = data["tracker_des"]

            new_tracker = Tracker(name=name, description=description, type=Tracker_type)
            user = User.query.filter_by(email=email).first()
            user.trackers.append(new_tracker)
            db.session.add(new_tracker)
            db.session.commit()
            flash("User Added Successfully!")
            return redirect(f"/dashboard/{email}")
    return render_template("update.html", trackers=trackers, email=email)


@app.route("/<string:email>/<int:id>/logs", methods=["GET", "POST"])
def log(email, id):
    print(data)
    str = ""
    parent_tracker = Tracker.query.filter_by(id=id).first()
    if request.method == "GET":
        all_logs = parent_tracker.logs
        if parent_tracker.tracker_type == "Numeric":
            data = {x.timestamp: x.value for x in all_logs}
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(data.keys(), data.values())
            axis.set(xlabel="Time Stamp", ylabel="Value")
            fig.savefig("static/graph.png")
            return render_template(
                "numerical.html",
                tracks=all_logs,
                str=str,
                src="static/graph.png",
                parent_tracker=parent_tracker,
                email=email,
            )
        if parent_tracker.tracker_type == "Boolean":
            return render_template(
                "boolean.html",
                tracks=all_logs,
                str=str,
                parent_tracker=parent_tracker,
                email=email,
            )

    elif request.method == "POST":
        Timestamp = Logs.query.get("timestamp")
        data = request.json()
        name = data["name"]
        value = data["value"]
        note = data["note"]
        timestamp = data["note"]

        new_log = Logs(log=name, value=value, note=note, timestamp=timestamp)
        parent_tracker.logs.append(new_log)
        db.session.add(new_log)
        db.session.commit()
        str = "Log Added Successfully"

        return redirect(f"/{email}/{id}/logs")


@app.route("/<email>/<int:id>/delete", methods=["GET", "POST"])
def delete(id, email):
    print("in app delete request")
    new_tracker = Tracker.query.get_or_404(id)
    print(new_tracker)

    try:
        db.session.delete(new_tracker)
        db.session.commit()
        return redirect(url_for("dashboard"), email=email)
    except:

        return "There was a problem deleting that task."


@app.route("/<string:email>/<int:tid>/<int:id>/delete", methods=["GET"])
def delete_log(username, tracker_id, log_id):
    log_needed = Logs.query.get_or_404(log_id)

    try:
        db.session.delete(log_needed)
        db.session.commit()
        return redirect(f"/{username}/{tracker_id}/logs")
    except:

        return "There was a problem deleting that task."


@app.route("/<string:email>/<int:id>/<int:log_id>/update", methods=["GET", "POST"])
def update_log(username, tracker_id, log_id):
    log_needed = Logs.query.filter_by(id=log_id).first()
    if request.method == "POST":
        if log_needed:
            Tracker_type = log_needed.log
            db.session.delete(log_needed)
            db.session.commit()
            val = request.form.get("_value_")
            note = request.form.get("_note_")

            new_log = Logs(log=Tracker_type, value=val, note=note)
            parent_tracker = Tracker.query.filter_by(id=tracker_id).first()
            parent_tracker.logs.append(new_log)
            db.session.add(new_log)
            db.session.commit()
            flash("Log updated Successfully!")
            return redirect(f"/{username}/{tracker_id}/logs")
    return render_template(
        "update_log.html", log=log_needed, tracker_id=tracker_id, username=username
    )


api.add_resource(UserAPI, "/api/users/", "/api/users/<int:id>")
api.add_resource(
    TrackerAPI, "/api/trackers/", "/api/trackers/<int:tracker_id>/"
)  #'/api/users/<int:user_id>/trackers/', '/api/users/<int:user_id>/trackers/<int:tracker_id>')
api.add_resource(
    LogAPI,
)  #'/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/', '/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/<int:log_id>')

if __name__ == "__main__":
    app.run(debug=True)
