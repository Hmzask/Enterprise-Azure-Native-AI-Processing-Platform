from worker_service.ai.summarizer import generate_summary
from worker_service.ai.speech_to_text import transcribe_audio
from worker_service.ai.image_ocr import extract_text_from_image


class AIOrchestrator:

    def process(
        self,
        file_type,
        file_path
    ):

        # Audio Pipeline
        if "audio" in file_type:

            transcript = transcribe_audio(file_path)
            summary = generate_summary(transcript)

            return {
                "transcript": transcript,
                "summary": summary
            }

        # Image Pipeline
        elif "image" in file_type:

            extracted_text = extract_text_from_image(file_path)
            summary = generate_summary(extracted_text)

            return {
                "ocr_text": extracted_text,
                "summary": summary
            }

        # Default
        else:
            return {
                "message": "Unsupported file type"
            }