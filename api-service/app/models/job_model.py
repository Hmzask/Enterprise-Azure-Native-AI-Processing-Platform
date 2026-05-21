import uuid
from datetime import datetime
from app.extensions import db


class Job(db.Model):

    __tablename__ = "jobs"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    file_type = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="UPLOADED"
    )

    uploaded_by = db.Column(
        db.String(255),
        nullable=False
    )

    blob_url = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    
    retry_count = db.Column(
    db.Integer,
    default=0
    )

    error_message = db.Column(
        db.Text,
        nullable=True
    )

    completed_at = db.Column(
        db.DateTime,
        nullable=True
    )