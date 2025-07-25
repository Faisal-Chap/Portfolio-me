# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    github_link = db.Column(db.String(255))
    likes = db.Column(db.Integer, default=0)
    is_featured = db.Column(db.Boolean, default=False)
