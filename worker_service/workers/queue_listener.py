import json
from datetime import datetime
import os
import time
import os


from azure.servicebus import ServiceBusClient
from worker_service.azure.blob_client import AzureBlobDownloader

from worker_service.ai.ai_orchestrator import AIOrchestrator
from worker_service.workers.worker_db import create_worker_app
from worker_service.workers.worker_db import db
from worker_service.workers.models import Job
from worker_service.logger import logger


from dotenv import load_dotenv
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(BASE_DIR, "../../.env")

load_dotenv(dotenv_path=env_path)


CONNECTION_STRING = os.getenv(
    "AZURE_SERVICE_BUS_CONNECTION_STRING"
)

QUEUE_NAME = os.getenv(
    "AZURE_SERVICE_BUS_QUEUE"
)

app = create_worker_app()

def process_message(message_data):

    job_id = message_data["job_id"]
    logger.info(
        f"Starting processing for job {job_id}"
        )

    with app.app_context():
        job = db.session.get(Job, job_id)

        if not job:
            logger.warning(
                f"Job {job_id} not found"
                )
            return

        try:
            # Update status
            job.status = "PROCESSING"
            db.session.commit()

            logger.info(
                f"Job {job_id} status updated to PROCESSING"
                )

            # Create temp folder
            os.makedirs("temp_processing", exist_ok=True)

            logger.info(
                "Temporary processing directory verified"
                )

            # Download blob
            blob_downloader = AzureBlobDownloader()

            blob_name = message_data["blob_name"]

            temp_file_path = os.path.join(
                "temp_processing",
                blob_name
            )

            logger.info(
                f"Downloading blob '{blob_name}' "
                f"for job {job_id}"
            )

            blob_downloader.download_blob(
                blob_name,
                temp_file_path
            )

            logger.info(
                f"Blob downloaded successfully to "
                f"{temp_file_path}"
            )
            

            logger.info(
                f"Starting AI orchestration for job {job_id}"
            )


            # Run AI pipeline
            orchestrator = AIOrchestrator()

            results = orchestrator.process(
                message_data["file_type"],
                temp_file_path
            )

            logger.info(
                f"AI processing completed for job {job_id}"
            )

            # Simulate AI work
            time.sleep(5)

            # Store AI results
            job.ai_result = json.dumps(results)

            logger.info(
                f"AI results stored for job {job_id}"
            )

            
            # Update status
            job.status = "COMPLETED"
            job.completed_at = datetime.now()

            db.session.commit()

            logger.info(
                f"Job {job_id} completed successfully"
            )

            if os.path.exists(temp_file_path):

                os.remove(temp_file_path)
                logger.info(
                    f"Temporary file removed: "
                    f"{temp_file_path}"
                )



        except Exception as error:
            logger.exception(
                f"Worker failed while processing "
                f"job {job_id}: {str(error)}"
            )

            job.status = "FAILED"
            job.retry_count += 1
            job.error_message = str(error)
            db.session.commit()

            raise error



def listen_to_queue():
    logger.info(
        "Initializing Azure Service Bus client"
    )

    client = ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STRING
    )

    with client:

        receiver = client.get_queue_receiver(
            queue_name=QUEUE_NAME,
            max_wait_time=5
        )

        logger.info(
            f"Listening to queue: {QUEUE_NAME}"
        )

        with receiver:

            print("Listening for messages...\n")
            for message in receiver:

                try:
                    logger.info(
                        "New message received from queue"
                    )
                    # Converting messege into JSON Format
                    body = str(message)
                    data = json.loads(body)

                    logger.info(
                        f"Received job message "
                        f"for job {data['job_id']}"
                    )

                    process_message(data)

                    # Complete message
                    receiver.complete_message(message)

                    logger.info(
                        f"Queue message completed "
                        f"for job {data['job_id']}"
                    )

                except Exception as error:

                    logger.exception(
                        f"Queue processing failed: "
                        f"{str(error)}"
                    )
                    receiver.abandon_message(message)

                    logger.warning(
                        "Message abandoned back to queue"
                    )


if __name__ == "__main__":
        
        logger.info("Worker service started")

        listen_to_queue()