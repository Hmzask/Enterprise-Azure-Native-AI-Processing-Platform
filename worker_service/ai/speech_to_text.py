import os
import subprocess
import uuid

import azure.cognitiveservices.speech as speechsdk


class AzureSpeechService:

    def convert_audio_to_wav(self, input_path):

        output_path = (
            f"temp_processing/{uuid.uuid4()}.wav"
        )

        subprocess.run([
            "ffmpeg",
            "-y",
            "-i", input_path,
            "-ar", "16000",
            "-ac", "1",
            "-c:a", "pcm_s16le",
            output_path
        ], check=True)

        return output_path

    def transcribe_audio(self, input_file):

        wav_file = self.convert_audio_to_wav(
            input_file
        )

        speech_config = speechsdk.SpeechConfig(
            subscription=os.getenv(
                "AZURE_SPEECH_KEY"
            ),
            region=os.getenv(
                "AZURE_SPEECH_REGION"
            )
        )

        audio_config = (
            speechsdk.audio.AudioConfig(
                filename=wav_file
            )
        )

        recognizer = (
            speechsdk.SpeechRecognizer(
                speech_config=speech_config,
                audio_config=audio_config
            )
        )

        result = recognizer.recognize_once()

        return result.text