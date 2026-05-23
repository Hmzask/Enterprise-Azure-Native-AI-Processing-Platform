from worker_service.azure.foundry_client import AzureFoundryClient


def generate_summary(text):

    client = AzureFoundryClient()

    return client.summarize_text(text)