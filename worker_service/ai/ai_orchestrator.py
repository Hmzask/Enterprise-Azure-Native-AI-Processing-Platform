from worker_service.ai.summarizer import generate_summary

from worker_service.ai.image_ocr import AzureOCRService

from worker_service.ai.speech_to_text import AzureSpeechService

from worker_service.ai.pdf_extractor import PDFExtractor


class AIOrchestrator:

    def process(self,file_type,file_path):

        extracted_text = ""

        # IMAGE OCR
        if "image" in file_type:

            ocr_service = AzureOCRService()
            extracted_text = ocr_service.extract_text(
                file_path
            )

        # AUDIO TRANSCRIPTION
        elif "audio" in file_type:

            speech_service = AzureSpeechService()
            extracted_text = speech_service.transcribe_audio(
                file_path
            )

        # PDF EXTRACTION
        elif "pdf" in file_type:

            pdf_service = PDFExtractor()
            extracted_text = pdf_service.extract_text(
                file_path
            )

        else:

            extracted_text = (
                "Unsupported file type"
            )

        # GPT Summary
        summary = generate_summary(
            extracted_text
        )

        return {
            "extracted_text": extracted_text,
            "summary": summary
        }