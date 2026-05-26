console.log("UPLOAD JS LOADED")

document
.getElementById("uploadForm")


.addEventListener("submit", async (e) => {

    e.preventDefault()

    console.log("FORM SUBMITTED")

    const fileInput = document
        .getElementById("fileInput")

    if (!fileInput.files.length) {

        alert("Please select a file")

        return
    }

    const formData = new FormData()

    formData.append(

        "file",

        fileInput.files[0]
    )

    try {

        const response = await fetch(

            "http://localhost:5000/api/v1/upload/",

            {

                method: "POST",

                body: formData,

                credentials: "include"
            }
        )

        console.log("STATUS:", response.status)

        const data = await response.json()

        console.log(data)

        if (!response.ok) {

            throw new Error(
                data.error || "Upload failed"
            )
        }

        document
            .getElementById("uploadStatus")

            .innerHTML = `

            <div class="alert alert-success">

                Job Created:
                ${data.job_id}

            </div>
            `

    } catch (error) {

        console.error(error)

        document
            .getElementById("uploadStatus")

            .innerHTML = `

            <div class="alert alert-danger">

                Upload Failed:
                ${error.message}

            </div>
            `
    }
})

