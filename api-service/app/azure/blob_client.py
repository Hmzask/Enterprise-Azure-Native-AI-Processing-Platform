from azure.storage.blob import BlobServiceClient

from flask import current_app


class AzureBlobService:

    def __init__(self):

        connection_string = current_app.config[
            "AZURE_STORAGE_CONNECTION_STRING"
        ]

        self.container_name = current_app.config[
            "AZURE_STORAGE_CONTAINER"
        ]

        self.blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

    def upload_file(
        self,
        file_data,
        blob_name
    ):

        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name,
            blob=blob_name
        )

        blob_client.upload_blob(
            file_data,
            overwrite=True
        )

        return blob_client.url