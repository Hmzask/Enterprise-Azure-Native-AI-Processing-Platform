from flask import Flask

from app.config.settings import DevelopmentConfig


def create_app():

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    from app.routes.health_routes import health_bp

    app.register_blueprint(health_bp)

    return app