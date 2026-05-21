import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )

    AZURE_STORAGE_CONNECTION_STRING = os.getenv(
        "AZURE_STORAGE_CONNECTION_STRING"
    )

    AZURE_SQL_CONNECTION_STRING = os.getenv(
        "AZURE_SQL_CONNECTION_STRING"
    )


class DevelopmentConfig(Config):

    DEBUG = True


class ProductionConfig(Config):

    DEBUG = False