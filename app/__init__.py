from flask import Flask
from app.models import db
from app.extensions import migrate
from app.blueprints.api import create_api

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@db/database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    create_api(app)

    return app
