from azure.foundry_client import AzureFoundryClient


client = AzureFoundryClient()

text = """
What is the meaning of Slacker
"""

result = client.summarize_text(text)

print("\nSUMMARY:\n")
print(result)