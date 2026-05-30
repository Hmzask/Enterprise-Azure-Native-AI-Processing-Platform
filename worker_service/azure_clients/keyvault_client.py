
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os


class KeyVaultClient:

    def __init__(self):

        vault_url = os.getenv("KEY_VAULT_URL")

        if not vault_url:
            raise ValueError(
                "KEY_VAULT_URL environment variable is missing"
            )

        credential = DefaultAzureCredential()

        self.client = SecretClient(
            vault_url=vault_url,
            credential=credential
        )

    def get_secret(self, secret_name):

        try:
            return self.client.get_secret(
                secret_name
            ).value

        except Exception as e:
            raise RuntimeError(
                f"Failed to retrieve secret '{secret_name}': {str(e)}"
            )

