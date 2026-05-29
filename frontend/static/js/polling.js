async function loadJobs() {

    try {

        const response = await fetch(
            "http://localhost:5000/api/v1/jobs",
            {
                credentials: "include"
            }
        )

        if (!response.ok) {

            console.error(
                "Jobs API failed:",
                response.status
            )

            return
        }

        const jobs = await response.json()

        let rows = ""

        if (jobs && jobs.length > 0) {

            jobs.forEach(job => {

                rows += `

                <tr>

                    <td>

                        <a href="/results/${job.id}">

                            ${job.id}

                        </a>

                    </td>

                    <td>

                        ${job.file_name}

                    </td>

                    <td>

                        <span class="badge bg-${
                            getStatusColor(job.status)
                        }">

                            ${job.status}

                        </span>

                    </td>

                </tr>
                `
            })

        } else {

            rows = `

            <tr>

                <td colspan="3" class="text-center">

                    No jobs available

                </td>

            </tr>
            `
        }

        document
            .getElementById("jobsTable")
            .innerHTML = rows

    } catch (error) {

        console.error(
            "Failed to load jobs:",
            error
        )
    }
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


// AUTO REFRESH EVERY 3 SECONDS
setInterval(loadJobs, 3000)

loadJobs()