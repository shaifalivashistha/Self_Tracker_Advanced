from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__='User_Profile'
    user_id=db.Column(db.Integer ,primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(300), nullable=False)
    trackers = db.relationship('Tracker',secondary='user_trackers', lazy=True, backref=db.backref('User',lazy=True))
    

    def __repr__(self):
        return '<User (username = %r)>' %(self.username) 


class Tracker(db.Model):
    __tablename__='Tracker'
    tracker_id=db.Column(db.Integer, primary_key=True,  autoincrement = True)
    tracker_name=db.Column(db.String(255), nullable=False)
    description=db.Column(db.String(255), nullable=False)
    tracker_type=db.Column(db.String(5), nullable=False)     
    date_created=db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    logs=db.relationship('Logs',secondary='tracker_logs', lazy=True, backref=db.backref('Tracker',lazy=True))

    def __repr__(self):
        return '<Tracker (tracker_name = %r)>' %(self.tracker_name)  


class Logs(db.Model):
    __tablename__="logs"
    log_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    timestamp=db.Column(db.DateTime, default=datetime.utcnow) 
    log_name=db.Column(db.String(255))
    log_value=db.Column(db.Integer, nullable=False)
    log_note=db.Column(db.String(255), nullable=True) 
    # setting = db.Column(db.String(255), nullable = True)   

    def __repr__(self):
        return '<Logs (log_name = %r)>' %(self.log_name)  


user_trackers = db.Table('user_trackers',
    db.Column('user_ID', db.Integer, db.ForeignKey('User_Profile.user_id'), primary_key=True),
    db.Column('tracker_ID', db.Integer, db.ForeignKey('Tracker.tracker_id'), primary_key=True)
)

tracker_logs = db.Table('tracker_logs',
    db.Column('tracker_ID', db.Integer, db.ForeignKey('Tracker.tracker_id'), primary_key=True),
    db.Column('log_ID', db.Integer, db.ForeignKey('logs.log_id'), primary_key=True)
)