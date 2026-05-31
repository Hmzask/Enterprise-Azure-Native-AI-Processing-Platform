
from datetime import datetime

from workers.worker_db import db


# =========================================================
# QUEUE METRICS
# =========================================================

class QueueMetrics(db.Model):

    __tablename__ = "queue_metrics"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    job_id = db.Column(
        db.String(100),
        nullable=False
    )

    worker_name = db.Column(
        db.String(100),
        nullable=True
    )

    processing_time = db.Column(
        db.Float,
        nullable=True
    )

    retry_count = db.Column(
        db.Integer,
        default=0
    )

    queue_wait_time = db.Column(
        db.Float,
        nullable=True
    )

    status = db.Column(
        db.String(50),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# =========================================================
# AI USAGE METRICS
# =========================================================

class AIUsage(db.Model):

    __tablename__ = "ai_usage"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    job_id = db.Column(
        db.String(100)
    )

    model_name = db.Column(
        db.String(100)
    )

    tokens_used = db.Column(
        db.Integer,
        default=0
    )

    estimated_cost = db.Column(
        db.Float,
        default=0
    )

    processing_time = db.Column(
        db.Float
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

