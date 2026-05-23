import os

from azure.storage.blob import BlobServiceClient

from dotenv import load_dotenv

load_dotenv()


class AzureBlobDownloader:

    def __init__(self):

        self.connection_string = os.getenv(
            "AZURE_STORAGE_CONNECTION_STRING"
        )

        self.container_name = os.getenv(
            "AZURE_STORAGE_CONTAINER"
        )

        self.client = BlobServiceClient.from_connection_string(
            self.connection_string
        )

    def download_blob(self,blob_name,download_path):

        blob_client = self.client.get_blob_client(

            container=self.container_name,

            blob=blob_name
        )

        with open(download_path, "wb") as file:

            download_stream = blob_client.download_blob()

            file.write(
                download_stream.readall()
            )

        return download_path