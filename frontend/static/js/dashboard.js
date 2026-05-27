async function loadDashboard() {

    const response = await fetch(
        "/api/v1/dashboard/metrics"
    )

    const data = await response.json()


    // PLATFORM METRICS
    document.getElementById(
        "totalJobs"
    ).innerText =
        data.platform_metrics.total_jobs

    document.getElementById(
        "processingJobs"
    ).innerText =
        data.platform_metrics.processing_jobs

    document.getElementById(
        "completedJobs"
    ).innerText =
        data.platform_metrics.completed_jobs

    document.getElementById(
        "failedJobs"
    ).innerText =
        data.platform_metrics.failed_jobs


    // LIVE JOBS TABLE
    let jobRows = ""

    data.recent_jobs.forEach(job => {

        jobRows += `

        <tr>

            <td>${job.file_name}</td>

            <td>

                <span class="badge bg-${
                    getStatusColor(job.status)
                }">

                    ${job.status}

                </span>

            </td>

            <td>

                ${formatDate(job.created_at)}

            </td>

        </tr>
        `
    })

    document.getElementById(
        "recentJobsTable"
    ).innerHTML = jobRows


    // AUDIT LOGS
    let auditHtml = ""

    data.recent_audit_logs.forEach(log => {

        auditHtml += `

        <li class="list-group-item">

            <strong>${log.event_type}</strong>

            <br>

            <small>${log.details}</small>

        </li>
        `
    })

    document.getElementById(
        "auditLogsList"
    ).innerHTML = auditHtml
}



function getStatusColor(status) {

    if (status === "COMPLETED")
        return "success"

    if (status === "PROCESSING")
        return "warning"

    if (status === "FAILED")
        return "danger"

    return "primary"
}


function formatDate(dateString) {

    return new Date(dateString)
        .toLocaleString()
}


// AUTO REFRESH EVERY 3 SECONDS
setInterval(loadDashboard, 3000)

loadDashboard()