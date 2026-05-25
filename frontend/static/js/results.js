async function loadResults() {

    const jobId = window.location.pathname
        .split("/")
        .pop()

    const response = await fetch(`http://localhost:5000/api/v1/jobs/${jobId}`)

    const data = await response.json()

    const result = JSON.parse(
        data.ai_result
    )

    document.getElementById(
        "summary"
    ).innerText = result.summary

    document.getElementById(
        "extractedText"
    ).innerText =
        result.extracted_text
}


loadResults()