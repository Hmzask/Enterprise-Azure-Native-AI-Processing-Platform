async function loadMetrics() {

    const response = await fetch(
        "/api/v1/dashboard/metrics"
    )

    const data = await response.json()

    document.getElementById(
        "totalJobs"
    ).innerText = data.total_jobs

    document.getElementById(
        "processingJobs"
    ).innerText = data.processing_jobs

    document.getElementById(
        "completedJobs"
    ).innerText = data.completed_jobs

    document.getElementById(
        "failedJobs"
    ).innerText = data.failed_jobs
}


setInterval(loadMetrics, 3000)

loadMetrics()