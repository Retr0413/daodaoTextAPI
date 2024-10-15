from flask import Flask
from flask_migrate import Migrate
from app import create_app
from app.models import db

app = create_app()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
