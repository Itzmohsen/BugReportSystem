from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)  # Add points column to track user points
    badges = db.relationship('Badge', backref='user', lazy=True)  # Establish relationship to Badge model

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link to a User

class BugReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Open', index=True)  # Ensure this matches your form/options handling
    severity = db.Column(db.String(50), index=True)  # No default value specified, consider adding if applicable
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('bugs', lazy=True))
    screenshot_path = db.Column(db.String(255), nullable=True)
    screen_recording_path = db.Column(db.String(255), nullable=True)
