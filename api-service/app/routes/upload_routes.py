import uuid

from flask import Blueprint, request

from app.extensions import db
from app.models.job_model import Job

from app.azure.blob_client import AzureBlobService
from app.azure.servicebus_client import AzureServiceBusService


upload_bp = Blueprint(
    "upload",
    __name__,
    url_prefix="/api/v1/upload"
)


@upload_bp.route("/", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return {
            "error": "No file uploaded"
        }, 400

    file = request.files["file"]

    if file.filename == "":
        return {
            "error": "Empty filename"
        }, 400

    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    # Upload to Azure Blob
    blob_service = AzureBlobService()

    blob_url = blob_service.upload_file(
        file,
        unique_filename
    )

    # Save job metadata
    job = Job(
        file_name=file.filename,
        file_type=file.content_type,
        uploaded_by="hamza@Footballer.com",
        status="UPLOADED",
        blob_url=blob_url
    )

    db.session.add(job)
    db.session.commit()

    # Send message to queue
    service_bus = AzureServiceBusService()
    service_bus.send_message({
        "job_id": job.id,
        "blob_url": blob_url,
        "file_name": file.filename,
        "file_type": file.content_type,
        "uploaded_by": job.uploaded_by,
        "status": job.status
    })

    return {
        "message": "File uploaded successfully",
        "job_id": job.id,
        "blob_url": blob_url
    }, 201