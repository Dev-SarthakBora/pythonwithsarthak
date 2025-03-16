
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from . import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=datetime.today()) 
