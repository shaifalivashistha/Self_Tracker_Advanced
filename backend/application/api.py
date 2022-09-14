from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import fields
from flask_restful import marshal_with
from flask_restful import abort



from .models import *

api = Api()


#-------------------------------------------USER API-------------------------------------------------#


user_data_req = reqparse.RequestParser()
user_data_req.add_argument('username', type=str, required=True)
user_data_req.add_argument('name', type=str, required=True)
user_data_req.add_argument('password', type=str, required=True)


user_field = {
    "user_id" : fields.Integer,
    "username" : fields.String,
    "name" : fields.String,
    "password" : fields.String,
    "url": fields.Url(absolute=True)
}


class UserAPI(Resource):
    @marshal_with(user_field)
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                return user
            else:
                abort(404, message= "Invalid user id")
        else:
            user = User.query.all()
            return user
    
    @marshal_with(user_field)
    def post(self):
        user_data = user_data_req.parse_args()
        user = User(username=user_data.username, name= user_data.name ,password=user_data.password)
        db.session.add(user)
        db.session.commit()
        return user

    @marshal_with(user_field)
    def put(self,  user_id=None):
        if user_id:
            user_data = User.query.get(user_id)
            new_user_data = user_data_req.parse_args()
            new_user = User(username = new_user_data.username, name = new_user_data.name, password=new_user_data.password)
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
    
    def delete(self,  user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return "Id removed successfully"
            else:
                abort(400, message="User does not exist")
        else:
            abort(404, message= "user id required")


#-----------------------------------------TRACKER API--------------------------------------------------#


tracker_data_req = reqparse.RequestParser()
tracker_data_req.add_argument('tracker_name', type=str, required=True)
tracker_data_req.add_argument('description', type=str, required=True)
tracker_data_req.add_argument('tracker_type', type=str, required=True)

tracker_field = {
    "tracker_id" : fields.Integer,
    "tracker_name" : fields.String,
    "description" : fields.String,
    "tracker_type" : fields.String,
    "url": fields.Url(absolute=True)
}


class TrackerAPI(Resource):
    @marshal_with(tracker_field)
    def get(self, tracker_id=None):
        tracker_data = Tracker.query.get(tracker_id)
        if tracker_data:
            return tracker_data
        else:
            return "Invalid tracker id"

    @marshal_with(tracker_field)
    def post(self):
        tracker_data = tracker_data_req.parse_args()
        tracker = Tracker(tracker_name=tracker_data.tracker_name, description= tracker_data.description ,tracker_type=tracker_data.tracker_type)
        db.session.add(tracker)
        db.session.commit()
        return tracker

    @marshal_with(tracker_field)
    def put(self,  tracker_id=None):
        if tracker_id:
            tracker_data = Tracker.query.get(tracker_id)
            new_tracker_data = tracker_data_req.parse_args()
            new_tracker = Tracker(tracker_name=new_tracker_data.tracker_name, description=new_tracker_data.description, tracker_type=new_tracker_data.tracker_type)
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
            


    
    def delete(self,  tracker_id=None):
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


#-----------------------------------------LOG API--------------------------------------------------#


logs_data_req = reqparse.RequestParser()
logs_data_req.add_argument('log_name', type=str, required=True)
logs_data_req.add_argument('log_value', type=int, required=True)
logs_data_req.add_argument('log_note', type=str, required=True)

logs_field = {
    "log_id" : fields.Integer,
    "log_name" : fields.String,
    "log_value" : fields.Integer,
    "log_note" : fields.String,
    "url": fields.Url(absolute=True)
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
    def post(self,  log_id=None):
        logs_data = logs_data_req.parse_args()
        logs = Logs(log_name=logs_data.log_name, log_value= logs_data.log_value ,log_note=logs_data.log_note)
        db.session.add(logs)
        db.session.commit()
        return logs

    @marshal_with(logs_field)
    def put(self,  log_id=None):
        if log_id:
            logs_data = Logs.query.get(log_id)
            new_logs_data = tracker_data_req.parse_args()
            new_log = Logs(log_name=new_logs_data.log_name, log_value=new_logs_data.log_value, log_note=new_logs_data.log_note)
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


#-----------------------------------------------------------------------------------------#


api.add_resource(UserAPI, '/api/users/', '/api/users/<int:user_id>')
api.add_resource(TrackerAPI, '/api/trackers/','/api/trackers/<int:tracker_id>/')#'/api/users/<int:user_id>/trackers/', '/api/users/<int:user_id>/trackers/<int:tracker_id>')
api.add_resource(LogAPI, )#'/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/', '/api/users/<int:user_id>/trackers/<int:tracker_id>/logs/<int:log_id>')
