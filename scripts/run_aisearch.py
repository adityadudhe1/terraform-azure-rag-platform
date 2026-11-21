#Purpose: Validate Azure OpenAI embedding generation using the text-embedding-3-small model.
#Text → Embedding → 1536-Dimensional Vector

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://name-resource.services.ai.azure.com/openai/v1"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="This is a test document"
)

print(len(response.data[0].embedding))
