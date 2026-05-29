async function loadJobs() {

    const response = await fetch("http://localhost:5000/api/v1/jobs")
    
    const jobs = await response.json()
    let rows = ""

   rows += `

<tr>

    <td>

        <a href="/results/${job.id}">

            ${job.id}

        </a>

    </td>

    <td>${job.file_name}</td>

    <td>

        <span class="badge bg-${
            getStatusColor(job.status)
        }">

            ${job.status}

        </span>

    </td>

</tr>
`

    document
        .getElementById("jobsTable")
        .innerHTML = rows
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


setInterval(loadJobs, 3000)

loadJobs()