from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MYTODO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) 

    from .models import Task
    from website.views import views
    app.register_blueprint(views, url_prefix='/')

    try:
        with app.app_context():
            db.create_all()
            print("db created")
    except Exception as e:
        print(f"Database not created: {e}")

    return app


