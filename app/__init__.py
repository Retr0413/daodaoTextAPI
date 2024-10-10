from flask import Flask
from .config import Config
from .extensions import db, migrate, cors
from .blueprints.api import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app