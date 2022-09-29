from flask import jsonify
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import fields
from flask_restful import marshal_with
from flask_restful import abort
from .task import *

from .models import *

api = Api()

# -------------------------------------------USER API-------------------------------------------------#


user_data_req = reqparse.RequestParser()
user_data_req.add_argument("username", type=str, required=True)
user_data_req.add_argument("email", type=str, required=True)
user_data_req.add_argument("password", type=str, required=True)


user_field = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "password": fields.String,
    "url": fields.Url(absolute=True),
}


class UserAPI(Resource):
    @marshal_with(user_field)
    def get(self, id=None):
        print(id)
        if id:
            user = User.query.get(id)
            if user:
                return user
            else:
                abort(404, message="Invalid user id")
        else:
            user = User.query.all()
            return user

    def post(self):
        user_data = user_data_req.parse_args()
        user = User(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            sec_ques=user_data.sec_que,
            sec_ans=user_data.sec_ans,
        )
        db.session.add(user)

        db.session.commit()
        return user

    def put(self, id=None):
        if id:
            user_data = User.query.get(id)
            new_user_data = user_data_req.parse_args()
            new_user = User(
                email=new_user_data.email,
                username=new_user_data.username,
                password=new_user_data.password,
                sec_ques=new_user_data.sec_que,
                sec_ans=new_user_data.sec_ans,
            )
            if user_data:
                try:
                    db.session.delete(user_data)
                    db.session.commit()
                    db.session.add(new_user)
                    db.session.commit()
                except:
                    abort(500, message="Something went")
                return new_user
            else:
                db.session.add(new_user)
                db.session.commit()
                return new_user
        else:
            abort(404, message="user ID Required")

    def delete(self, id=None):
        if id:
            user = User.query.get(id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return "Id removed successfully"
            else:
                abort(400, message="User does not exist")
        else:
            abort(404, message="user id required")


# -----------------------------------------TRACKER API--------------------------------------------------#


tracker_data_req = reqparse.RequestParser()
tracker_data_req.add_argument("tracker_name", type=str, required=True)
tracker_data_req.add_argument("description", type=str, required=True)
tracker_data_req.add_argument("tracker_type", type=str, required=True)

tracker_field = {
    "tracker_id": fields.Integer,
    "tracker_name": fields.String,
    "description": fields.String,
    "tracker_type": fields.String,
    "url": fields.Url(absolute=True),
}


class TrackerAPI(Resource):
    @marshal_with(tracker_field)
    def get(self, id=None):
        tracker_data = Tracker.query.get(id)
        if tracker_data:
            return tracker_data
        else:
            return "Invalid tracker id"

    @marshal_with(tracker_field)
    def post(self):
        tracker_data = tracker_data_req.parse_args()
        tracker = Tracker(
            tracker_name=tracker_data.name,
            description=tracker_data.description,
            tracker_type=tracker_data.type,
        )
        db.session.add(tracker)
        db.session.commit()
        return tracker

    @marshal_with(tracker_field)
    def put(self, id=None):
        if id:
            tracker_data = Tracker.query.get(id)
            old_tracker_type = tracker_data.type
            new_tracker_data = tracker_data_req.parse_args()
            new_tracker = Tracker(
                tracker_name=new_tracker_data.name,
                description=new_tracker_data.description,
                tracker_type=old_tracker_type,
            )
            if tracker_data:
                try:
                    db.session.delete(tracker_data)
                    db.session.commit()
                    db.session.add(new_tracker)
                    db.session.commit()
                except:
                    abort(500, message="Something went wrong")
                return new_tracker
            else:
                db.session.add(new_tracker)
                db.session.commit()
                return new_tracker
        else:
            abort(400, message="BAD REQUEST, tracker ID required")

    def delete(self, tracker_id=None):
        if tracker_id:
            tracker = Tracker.query.get(tracker_id)
            if tracker:
                db.session.delete(tracker)
                db.session.commit()
                return "tracker removed successfully"
            else:
                abort(404, message="tracker data not found")
        else:
            abort(400, message="BAD REQUEST, tracker ID required")


# -----------------------------------------LOG API--------------------------------------------------#


logs_data_req = reqparse.RequestParser()
logs_data_req.add_argument("log_name", type=str, required=True)
logs_data_req.add_argument("log_value", type=int, required=True)
logs_data_req.add_argument("log_note", type=str, required=True)

logs_field = {
    "log_id": fields.Integer,
    "log_name": fields.String,
    "log_value": fields.Integer,
    "log_note": fields.String,
    "url": fields.Url(absolute=True),
}


class LogAPI(Resource):
    @marshal_with(logs_field)
    def get(self, log_id=None):
        logs_data = Logs.query.get(log_id)
        if logs_data:
            return logs_data
        else:
            return "Invalid Log id"

    @marshal_with(logs_field)
    def post(self, log_id=None):
        logs_data = logs_data_req.parse_args()
        logs = Logs(
            log_name=logs_data.log_name,
            log_value=logs_data.log_value,
            log_note=logs_data.log_note,
        )
        db.session.add(logs)
        db.session.commit()
        return logs

    @marshal_with(logs_field)
    def put(self, log_id=None):
        if log_id:
            logs_data = Logs.query.get(log_id)
            new_logs_data = tracker_data_req.parse_args()
            new_log = Logs(
                log_name=new_logs_data.log_name,
                log_value=new_logs_data.log_value,
                log_note=new_logs_data.log_note,
            )
            if logs_data:
                try:
                    db.session.delete(logs_data)
                    db.session.commit()
                    db.session.add(new_log)
                    db.session.commit()
                except:
                    abort(500, message="Something went wrong")
                return new_log
            else:
                db.session.add(new_log)
                db.session.commit()
                return new_log
        else:
            abort(400, message="BAD REQUEST, log ID required")

    def delete(self, log_id=None):
        if log_id:
            log = Logs.query.get(log_id)
            if log:
                db.session.delete(log)
                db.session.commit()
                return "log removed successfully"
            else:
                abort(404, message="log data not found")
        else:
            abort(400, message="BAD REQUEST, log ID required")


# -----------------------------------------------------------------------------------------#


def generate_csv(input):
    with open("~/Downloads/Mad2_Project/TrackerInfo.csv", "w") as file:
        myWriter = csv.writer(file)
        writeHeader = True
        for i in input.values():
            if writeHeader:
                myWriter.writerow(i.keys())
                writeHeader = False
            myWriter.writerow(i.values())
        file.close()

    # with open(
    #     "/Downloads/Mad2_Project/TrackerInfo.csv", "w", encoding="utf8", newline="\n"
    # ) as output_file:
    #     output = csv.DictWriter(output_file, fieldnames=input[0].keys(), restval="")
    #     output.writeheader()
    #     output.writerows(input)
    # return


# -----------------------TRACKER EXPORT API------------------------#


class ExportTrackerAPI(Resource):
    def get(self, email):
        user_data = User.query.filter_by(email=email).first()
        trackers = user_data.trackers
        tracker_list = []
        for tracker in trackers:
            tracker_list.append(tracker)

        tracker_dict = {}
        idx = 0
        for trck in tracker_list:
            idx += 1
            DictTrack = {
                "id": trck.id,
                "name": trck.name,
                "description": trck.description,
                "type": trck.type,
                "date_created": trck.date_created,
            }
            tracker_dict[idx] = DictTrack
        JDictTrck = jsonify(tracker_dict)
        tracker_csv = generate_csv(JDictTrck)
        return "Tracker Export job start", 200


# -----------------------LOG EXPORT API------------------------#


class ExportLogAPI(Resource):
    def get(self, email, id):
        trackers = Tracker.query.filter_by(id=id).first()
        all_logs = trackers.logs
        log_list = []
        for log in all_logs:
            log_list.append(log)

        log_dict = {}
        idx = 0
        for log in log_list:
            idx += 1
            Dlog = {
                "log": log.log,
                "log_id": log.id,
                "value": log.value,
                "note": log.note,
                "timestamp": log.timestamp,
            }
            log_dict[idx] = Dlog

        JDict_Logs = jsonify(log_dict)
        generate_csv.delay(JDict_Logs)
        return "Log Export job start", 200
