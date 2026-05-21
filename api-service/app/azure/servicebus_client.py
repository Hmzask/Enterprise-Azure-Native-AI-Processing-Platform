import json

from flask import current_app

from azure.servicebus import ServiceBusClient
from azure.servicebus import ServiceBusMessage


class AzureServiceBusService:

    def __init__(self):

        self.connection_string = current_app.config[
            "AZURE_SERVICE_BUS_CONNECTION_STRING"
        ]

        self.queue_name = current_app.config[
            "AZURE_SERVICE_BUS_QUEUE"
        ]

        self.client = ServiceBusClient.from_connection_string(
            conn_str=self.connection_string
        )

    def send_message(self, payload):

        with self.client:

            sender = self.client.get_queue_sender(
                queue_name=self.queue_name
            )

            with sender:
                message = ServiceBusMessage(
                    json.dumps(payload)
                )

                sender.send_messages(message)