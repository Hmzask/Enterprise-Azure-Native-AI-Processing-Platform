from datetime import datetime

from workers.worker_db import db


class Job(db.Model):

    __tablename__ = "jobs"

    id = db.Column(
        db.String,
        primary_key=True
    )

    status = db.Column(
        db.String
    )

    retry_count = db.Column(
        db.Integer
    )

    error_message = db.Column(
        db.Text
    )

    completed_at = db.Column(
        db.DateTime
    )

    ai_result = db.Column(
        db.Text
    )   

    file_name = db.Column(
    db.String
    )

    created_at = db.Column(
        db.DateTime
    )