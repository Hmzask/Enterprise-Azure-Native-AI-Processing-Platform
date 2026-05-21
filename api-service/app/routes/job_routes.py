from flask import Blueprint

from app.extensions import db
from app.models.job_model import Job

job_bp = Blueprint(
    "jobs",
    __name__,
    url_prefix="/api/v1/jobs"
)


@job_bp.route("/create", methods=["POST"])
def create_job():

    job = Job(
        file_name="sample1.pdf",
        file_type="pdf",
        uploaded_by="hamza@company.com"
    )

    db.session.add(job)
    db.session.commit()

    return {
        "message": "Job created Successfully",
        "job_id": job.id
    }, 201