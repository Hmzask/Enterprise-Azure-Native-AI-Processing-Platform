console.log("UPLOAD JS LOADED")

document
.getElementById("uploadForm")

.addEventListener("submit", async (e) => {

    e.preventDefault()

    console.log("FORM SUBMITTED")

    const fileInput =
        document.getElementById("fileInput")

    const uploadStatus =
        document.getElementById("uploadStatus")

    const loader =
        document.getElementById("uploadLoader")

    const submitButton =
        e.target.querySelector("button")

    if (!fileInput.files.length) {

        alert("Please select a file")

        return
    }

    const file = fileInput.files[0]

    // =====================================
    // FILE TYPE VALIDATION
    // =====================================

    const allowedTypes = [

        "application/pdf",

        "image/png",

        "image/jpeg",

        "audio/mpeg",

        "audio/wav",

        "audio/ogg",

        "video/mp4",

        "text/plain"
    ]

    if (!allowedTypes.includes(file.type)) {

        alert("Unsupported file type")

        return
    }

    // =====================================
    // FILE SIZE VALIDATION
    // =====================================

    const maxSize = 50 * 1024 * 1024

    if (file.size > maxSize) {

        alert(
            "File size exceeds 50MB"
        )

        return
    }

    const formData = new FormData()

    formData.append("file", file)

    try {

        loader.classList.remove("d-none")

        submitButton.disabled = true

        const response = await fetch(

            "http://localhost:5000/api/v1/upload/",

            {

                method: "POST",

                body: formData,

                credentials: "include"
            }
        )
        console.log(await response.text())

        console.log(
            "STATUS:",
            response.status
        )

        let data = {}

        try {

            data = await response.json()

        } catch {

            data = {
                error:
                "Invalid server response"
            }
        }

        console.log(data)

        if (!response.ok) {

            throw new Error(
                data.error ||
                "Upload failed"
            )
        }

        uploadStatus.innerHTML = `

        <div class="alert alert-success">

            Job Created:
            ${data.job_id}

        </div>
        `

    } catch (error) {

        console.error(error)

        uploadStatus.innerHTML = `

        <div class="alert alert-danger">

            Upload Failed:
            ${error.message}

        </div>
        `

    } finally {

        loader.classList.add("d-none")

        submitButton.disabled = false
    }
})