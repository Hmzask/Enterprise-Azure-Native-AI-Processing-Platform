async function loadLogs() {

    const response = await fetch(

        "http://localhost:5000/api/v1/admin/audit-logs",

        {

        credentials: "include"
        }
    )

    const logs = await response.json()

    let rows = ""

    logs.forEach(log => {

        rows += `

        <tr>

            <td>${log.event_type}</td>

            <td>${log.user_email}</td>

            <td>${log.details}</td>

            <td>${log.created_at}</td>

        </tr>
        `
    })

    document
        .getElementById("logsTable")
        .innerHTML = rows
}


loadLogs()