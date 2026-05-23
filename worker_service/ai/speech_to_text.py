import os

import azure.cognitiveservices.speech as speechsdk


class AzureSpeechService:

    def transcribe_audio(self,audio_path):

        speech_config = speechsdk.SpeechConfig(

            subscription=os.getenv(
                "AZURE_SPEECH_KEY"
            ),

            region=os.getenv(
                "AZURE_SPEECH_REGION"
            )
        )

        audio_config = speechsdk.audio.AudioConfig(
            filename=audio_path
        )

        recognizer = speechsdk.SpeechRecognizer(

            speech_config=speech_config,

            audio_config=audio_config
        )

        result = recognizer.recognize_once()

        return result.text