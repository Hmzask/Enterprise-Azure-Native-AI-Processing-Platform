from flask import Blueprint


health_bp = Blueprint(
    "health",
    __name__,
    url_prefix="/api/v1/health"
)


@health_bp.route("/", methods=["GET"])
def health_check():

    return {
        "status": "healthy",
        "service": "enterprise-ai-platform"
    }, 200