from flask import Flask

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_worker_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:////home/a/Programming/ENTERPRISE-AI-PLATFORM/api_service/instance/enterprise_ai.db"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app