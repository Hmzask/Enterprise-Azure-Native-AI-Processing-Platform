from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def login():

    return render_template(
        "login.html"
    )


@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html"
    )


@app.route("/upload")
def upload():

    return render_template(
        "upload.html"
    )


@app.route("/jobs")
def jobs():

    return render_template(
        "jobs.html"
    )


@app.route("/results/<job_id>")
def results(job_id):

    return render_template(
        "results.html",
        job_id=job_id
    )


@app.route("/admin")
def admin():

    return render_template(
        "admin.html"
    )


@app.route("/audit-logs")
def audit_logs():

    return render_template(
        "audit_logs.html"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )