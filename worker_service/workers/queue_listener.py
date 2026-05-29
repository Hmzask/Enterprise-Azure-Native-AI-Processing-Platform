import json
import os
import time
from datetime import datetime

from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient

from worker_service.azure.blob_client import (
    AzureBlobDownloader
)

from worker_service.ai.ai_orchestrator import (
    AIOrchestrator
)

from worker_service.workers.worker_db import (
    create_worker_app,
    db
)

from worker_service.workers.models import Job
from worker_service.logger import logger


# =========================================================
# ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

CONNECTION_STRING = os.getenv(
    "AZURE_SERVICE_BUS_CONNECTION_STRING"
)

QUEUE_NAME = os.getenv(
    "AZURE_SERVICE_BUS_QUEUE"
)


# =========================================================
# FLASK APP CONTEXT
# =========================================================

app = create_worker_app()


# =========================================================
# PROCESS MESSAGE
# =========================================================

def process_message(message_data, delivery_count=0):

    job_id = message_data["job_id"]

    logger.info(
        f"Starting processing for job {job_id}"
    )
    temp_file_path = None

    with app.app_context():

        job = None

        # -------------------------------------------------
        # Retry DB fetch
        # -------------------------------------------------

        for attempt in range(3):

            job = db.session.get(Job, job_id)

            if job:
                break

            logger.warning(
                f"Job {job_id} not found "
                f"(attempt {attempt + 1}/3)"
            )

            time.sleep(2)

        if not job:

            raise Exception(
                f"Job {job_id} missing in database "
                f"after retries"
            )

        try:

            # -------------------------------------------------
            # Update Job Status
            # -------------------------------------------------

            job.status = "PROCESSING"

            db.session.commit()

            logger.info(
                f"Job {job_id} status updated "
                f"to PROCESSING"
            )

            # -------------------------------------------------
            # Create Temp Directory
            # -------------------------------------------------

            os.makedirs(
                "temp_processing",
                exist_ok=True
            )

            logger.info(
                "Temporary processing directory verified"
            )

            # -------------------------------------------------
            # Download Blob
            # -------------------------------------------------

            blob_downloader = (
                AzureBlobDownloader()
            )

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

            # -------------------------------------------------
            # AI PROCESSING
            # -------------------------------------------------

            logger.info(
                f"Starting AI orchestration "
                f"for job {job_id}"
            )

            orchestrator = AIOrchestrator()

            results = orchestrator.process(
                message_data["file_type"],
                temp_file_path
            )

            logger.info(
                f"AI processing completed "
                f"for job {job_id}"
            )

            # -------------------------------------------------
            # Store Results
            # -------------------------------------------------

            job.ai_result = json.dumps(results)

            logger.info(
                f"AI results stored "
                f"for job {job_id}"
            )

            # -------------------------------------------------
            # COMPLETE JOB
            # -------------------------------------------------

            job.status = "COMPLETED"

            job.completed_at = datetime.utcnow()

            job.retry_count = 0
            job.error_message = None

            db.session.commit()

            logger.info(
                f"Job {job_id} completed successfully"
            )

            logger.info(
                f"Result: {results}"
            )

        except Exception as error:

                logger.exception(
                    f"Worker failed while processing "
                    f"job {job_id}: {str(error)}"
                )

                db.session.rollback()

                job = db.session.get(Job, job_id)

                if not job:
                    raise Exception(
                        f"Job {job_id} disappeared from DB"
                    )

                # =========================================
                # RETRY TRACKING
                # =========================================

                job.retry_count += 1

                job.error_message = str(error)

                # =========================================
                # STATUS MANAGEMENT
                # =========================================

                if delivery_count >= 3:

                    job.status = "FAILED"

                    logger.error(
                        f"Job {job_id} permanently failed"
                    )

                else:

                    job.status = "RETRYING"

                    logger.warning(
                        f"Job {job_id} scheduled for retry"
                    )

                db.session.commit()

                raise error
        finally:

            # ---------------------------------------------
            # CLEAN TEMP FILES
            # ---------------------------------------------

            if (temp_file_path and os.path.exists(temp_file_path)):

                os.remove(temp_file_path)

                logger.info(
                    f"Temporary file removed: "
                    f"{temp_file_path}"
                )


# =========================================================
# LISTEN TO QUEUE
# =========================================================

def listen_to_queue():

    logger.info(
        "Initializing Azure Service Bus client"
    )

    client = (
        ServiceBusClient.from_connection_string(
            conn_str=CONNECTION_STRING
        )
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

            logger.info(
                "Listening for messages..."
            )

            while True:

                messages = receiver.receive_messages(
                    max_message_count=1,
                    max_wait_time=5
                )

                if not messages:
                    continue

                for message in messages:

                    try:

                        logger.info(
                            "New message received "
                            "from queue"
                        )

                        # ---------------------------------
                        # PARSE MESSAGE
                        # ---------------------------------

                        body = b"".join(
                            [b for b in message.body]
                        ).decode("utf-8")

                        data = json.loads(body)

                        logger.info(
                            f"Received job message "
                            f"for job {data['job_id']}"
                        )

                        # ---------------------------------
                        # PROCESS MESSAGE
                        # ---------------------------------

                        process_message(
                            data,
                            delivery_count=
                            message.delivery_count
                        )

                        # ---------------------------------
                        # COMPLETE MESSAGE
                        # ---------------------------------

                        receiver.complete_message(
                            message
                        )

                        logger.info(
                            f"Queue message completed "
                            f"for job {data['job_id']}"
                        )

                    except Exception as error:

                        logger.exception(
                            f"Queue processing failed: "
                            f"{str(error)}"
                        )

                        # ---------------------------------
                        # DEAD LETTER LOGIC
                        # ---------------------------------

                        if message.delivery_count >= 3:

                            receiver.dead_letter_message(
                                message,
                                reason="ProcessingFailed",
                                error_description=
                                str(error)
                            )

                            logger.warning(
                                "Message moved to "
                                "dead letter queue"
                            )

                        else:

                            receiver.abandon_message(
                                message
                            )

                            logger.warning(
                                "Message abandoned "
                                "back to queue"
                            )


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    logger.info(
        "Worker service started"
    )

    listen_to_queue()