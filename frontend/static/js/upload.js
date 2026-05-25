document
    .getElementById("uploadForm")

    .addEventListener("submit", async (e) => {

        e.preventDefault()

        const fileInput = document
            .getElementById("fileInput")

        const formData = new FormData()

        formData.append(
            "file",
            fileInput.files[0]
        )

        const response = await fetch(

            "/api/v1/upload/",

            {
                method: "POST",
                body: formData
            }
        )

        const data = await response.json()

        document
            .getElementById("uploadStatus")
            .innerHTML = `

            <div class="alert alert-success">

                Job Created:
                ${data.job_id}

            </div>
        `
    })