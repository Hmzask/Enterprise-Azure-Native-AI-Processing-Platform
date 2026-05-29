async function loadDashboard() {

    const response = await fetch(
        "http://localhost:5000/api/v1/dashboard/metrics",
        {

        credentials: "include"
        }
    )

    const data = await response.json()


    // PLATFORM METRICS
document.getElementById(
    "totalJobs"
).innerText =
    data.total_jobs

document.getElementById(
    "processingJobs"
).innerText =
    data.processing_jobs

document.getElementById(
    "completedJobs"
).innerText =
    data.completed_jobs

document.getElementById(
    "failedJobs"
).innerText =
    data.failed_jobs


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

            <td>${job.retry_count}</td>

            <td>

                ${formatDate(job.created_at)}

            </td>

        </tr>
        `
    })

    document.getElementById(
        "recentJobsTable"
    ).innerHTML = jobRows


const auditLogsList = document.getElementById(
    "auditLogsList"
)

auditLogsList.innerHTML = ""

if (
    data.recent_audit_logs &&
    data.recent_audit_logs.length > 0
) {

    data.recent_audit_logs.forEach((log) => {

        auditLogsList.innerHTML += `

        <li class="list-group-item">

            <strong>
                ${log.event_type}
            </strong>

            <br>

            ${log.details}

            <br>

            <small class="text-muted">

                ${new Date(
                    log.created_at
                ).toLocaleString()}

            </small>

        </li>
        `
    })

} else {

    auditLogsList.innerHTML = `

    <li class="list-group-item">

        No audit logs available

    </li>
    `
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
}

loadDashboard()
