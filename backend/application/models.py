from flask_security import UserMixin, RoleMixin
from datetime import datetime
from .database import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    sec_ques = db.Column(db.String(300), nullable=False)
    sec_ans = db.Column(db.String(300), nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    trackers = db.relationship(
        "Tracker", secondary="UserTracker", backref="User", cascade="all,delete"
    )
    roles = db.relationship(
        "Role", secondary="roles_users", backref=db.backref("User", lazy=True)
    )


class Tracker(db.Model):
    __tablename__ = "tracker"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    logs = db.relationship(
        "Logs", secondary="TrackerLog", backref="tracker", cascade="all,delete"
    )


class Logs(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    log = db.Column(db.String(300))
    value = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(300), nullable=True)
    # setting = db.Column(db.String(255), nullable = True)


class UserTracker(db.Model):
    __tablename__ = "UserTracker"
    UserTrackerID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    uID = db.Column(db.Integer(), db.ForeignKey("user.id"))
    tID = db.Column(db.Integer(), db.ForeignKey("tracker.id"))


class TrackerLog(db.Model):
    __tablename__ = "TrackerLog"
    TrackerLogID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tID = db.Column(db.Integer(), db.ForeignKey("tracker.id"))
    lID = db.Column(db.Integer(), db.ForeignKey("logs.id"))


class Role(db.Model, RoleMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(300))


class RolesUsers(db.Model):
    __tablename__ = "roles_users"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column("user_id", db.Integer(), db.ForeignKey("user.id"))
    role_id = db.Column("role_id", db.Integer(), db.ForeignKey("role.id"))


# class User(db.Model, UserMixin):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     email = Column(String(255), unique=True)
#     username = Column(String(255), unique=True, nullable=True)
#     password = Column(String(255), nullable=False)
#     active = Column(Boolean())
#     fs_uniquifier = Column(String(255), unique=True, nullable=False)
#     trackers = db.relationship(
#         "tracker", secondary="UserTracker", backref="user", cascade="all,delete"
#     )
#     roles = db.relationship(
#         "Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic")
#     )


# class Tracker(db.Model):
#     __tablename__ = "tracker"
#     id = Column(Integer(), primary_key=True, autoincrement=True)
#     name = Column(String(300), nullable=False)
#     description = Column(String, nullable=False)
#     type = Column(String(300), nullable=False)
#     time_created = Column(DateTime(timezone=True), default=datetime.utcnow)
#     logs = db.relationship(
#         "logs", secondary="TrackerLog", backref="tracker", cascade="all,delete"
#     )


# class Logs(db.Model):
#     __tablename__ = "logs"
#     id = Column(Integer(), primary_key=True, autoincrement=True)
#     timestamp = Column(DateTime(), default=datetime.utcnow)
#     name = Column(String(300))
#     value = Column(String(300), nullable=False)
#     note = Column(String(300), nullable=False)


# user_trackers = db.Table(
#     "user_trackers",
#     db.Column("user_ID", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
#     db.Column(
#         "tracker_ID", db.Integer, db.ForeignKey("Tracker.tracker_id"), primary_key=True
#     ),
# )


# class UserTracker(db.Model):
#     __tablename__ = "UserTracker"
#     UserTrackerID = Column(Integer(), primary_key=True, autoincrement=True)
#     uID = Column(Integer(), ForeignKey("user.id"))
#     tID = Column(Integer(), ForeignKey("tracker.id"))


# tracker_logs = db.Table(
#     "tracker_logs",
#     db.Column(
#         "tracker_ID", db.Integer, db.ForeignKey("Tracker.tracker_id"), primary_key=True
#     ),
#     db.Column("log_ID", db.Integer, db.ForeignKey("logs.log_id"), primary_key=True),
# )


# class TrackerLog(db.Model):
#     __tablename__ = "TackerLog"
#     TrackerLogID = Column(Integer(), primary_key=True, autoincrement=True)
#     tID = Column(Integer(), ForeignKey("tracker.id"))
#     lID = Column(Integer(), ForeignKey("logs.id"))


# class Role(db.Model, RoleMixin):
#     __tablename__ = "role"
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(80), unique=True)
#     description = Column(String(255))


# class RolesUsers(db.Model):
#     __tablename__ = "roles_users"
#     id = Column(Integer(), primary_key=True)
#     user_id = Column("user_id", Integer(), ForeignKey("user.id"))
#     role_id = Column("role_id", Integer(), ForeignKey("role.id"))
