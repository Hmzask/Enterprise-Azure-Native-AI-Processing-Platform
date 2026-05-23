import os

from azure.ai.vision.imageanalysis import ImageAnalysisClient

from azure.ai.vision.imageanalysis.models import VisualFeatures

from azure.core.credentials import AzureKeyCredential


class AzureOCRService:

    def __init__(self):

        self.client = ImageAnalysisClient(

            endpoint=os.getenv(
                "AZURE_VISION_ENDPOINT"
            ),

            credential=AzureKeyCredential(
                os.getenv("AZURE_VISION_KEY")
            )
        )

    def extract_text(self,image_path):

        with open(image_path, "rb") as image_file:

            result = self.client.analyze(

                image_data=image_file,

                visual_features=[
                    VisualFeatures.READ
                ]
            )

        extracted_text = ""

        if result.read:

            for block in result.read.blocks:

                for line in block.lines:

                    extracted_text += line.text + "\n"

        return extracted_text