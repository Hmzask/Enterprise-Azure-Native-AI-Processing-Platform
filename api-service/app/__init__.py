from flask import Flask

from app.config.settings import DevelopmentConfig
from app.extensions import db, migrate


def create_app():

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)



    # Health Blueprint
    from app.routes.health_routes import health_bp
    app.register_blueprint(health_bp)

    # Job Blueprint
    from app.routes.job_routes import job_bp
    app.register_blueprint(job_bp)

    # Upload Blueprint
    from app.routes.upload_routes import upload_bp
    app.register_blueprint(upload_bp)

    return app