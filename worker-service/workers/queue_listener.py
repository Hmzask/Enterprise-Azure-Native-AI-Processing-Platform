import json
import time
import os

from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient
load_dotenv()

CONNECTION_STRING = os.getenv(
    "AZURE_SERVICE_BUS_CONNECTION_STRING"
)

QUEUE_NAME = os.getenv(
    "AZURE_SERVICE_BUS_QUEUE"
)


def process_message(message_data):

    print("\n======================")
    print("PROCESSING JOB")
    print("======================")

    print(message_data)

    # Simulate AI processing
    time.sleep(5)

    print("AI Processing Completed")


def listen_to_queue():

    client = ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STRING
    )

    with client:

        receiver = client.get_queue_receiver(
            queue_name=QUEUE_NAME,
            max_wait_time=5
        )

        with receiver:

            print("Listening for messages...\n")
            for message in receiver:

                try:

                    body = str(message)
                    data = json.loads(body)
                    process_message(data)

                    # Complete message
                    receiver.complete_message(message)
                    print("Message completed\n")

                except Exception as error:

                    print("Error:", error)
                    receiver.abandon_message(message)


if __name__ == "__main__":
    listen_to_queue()