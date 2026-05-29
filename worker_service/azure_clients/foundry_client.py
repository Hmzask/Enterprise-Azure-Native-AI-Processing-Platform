import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()


class AzureFoundryClient:
    def __init__(self):

        self.client = AzureOpenAI(
            api_key=os.getenv(
                "AZURE_OPENAI_API_KEY"
            ),
            api_version=os.getenv(
                "AZURE_OPENAI_API_VERSION"
            ),
            azure_endpoint=os.getenv(
                "AZURE_OPENAI_ENDPOINT"
            )
        )
        
        self.deployment = os.getenv(
            "AZURE_OPENAI_DEPLOYMENT"
        )

    def summarize_text(self,text):

        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an enterprise AI assistant "
                        "that summarizes uploaded documents."
                    )
                },

                {
                    "role": "user",
                    "content": (
                        f"Summarize this content:\n\n{text}"
                    )
                }
            ],

            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content