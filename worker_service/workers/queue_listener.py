import json
from datetime import datetime
import os
import time

from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient


from worker_service.ai.ai_orchestrator import AIOrchestrator
from worker_service.workers.worker_db import create_worker_app
from worker_service.workers.worker_db import db
from worker_service.workers.models import Job

load_dotenv()


CONNECTION_STRING = os.getenv(
    "AZURE_SERVICE_BUS_CONNECTION_STRING"
)

QUEUE_NAME = os.getenv(
    "AZURE_SERVICE_BUS_QUEUE"
)

app = create_worker_app()

def process_message(message_data):

    job_id = message_data["job_id"]

    with app.app_context():

        job = db.session.get(Job, job_id)

        if not job:
            print("Job not found")
            return

        try:
            # Update status
            job.status = "PROCESSING"
            db.session.commit()
            print(f"Processing job: {job_id}")


            orchestrator = AIOrchestrator()
            results = orchestrator.process(
            message_data["file_type"],
                "dummy_path"
            )   

            # Simulate AI work
            time.sleep(5)

            job.ai_result = json.dumps(results)

            # Mark complete
            job.status = "COMPLETED"

            job.completed_at = datetime.now()

            db.session.commit()

            print("Job completed")

        except Exception as error:

            job.status = "FAILED"

            job.retry_count += 1

            job.error_message = str(error)

            db.session.commit()

            raise error



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