import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )


    # Azure DB
    AZURE_SQL_CONNECTION_STRING = os.getenv(
        "AZURE_SQL_CONNECTION_STRING"
    )


    # Azure Blob storage
    AZURE_STORAGE_CONNECTION_STRING = os.getenv(
        "AZURE_STORAGE_CONNECTION_STRING"
    )

    AZURE_STORAGE_CONTAINER = os.getenv(
        "AZURE_STORAGE_CONTAINER"
    )

    # Service Bus (Queue)
    AZURE_SERVICE_BUS_CONNECTION_STRING = os.getenv(
    "AZURE_SERVICE_BUS_CONNECTION_STRING"
    )
    
    AZURE_SERVICE_BUS_QUEUE = os.getenv(
        "AZURE_SERVICE_BUS_QUEUE"
    )



class DevelopmentConfig(Config):

    DEBUG = True


class ProductionConfig(Config):

    DEBUG = False