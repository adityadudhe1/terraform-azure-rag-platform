#2 Purpose: Validate Azure OpenAI deployment connectivity using the gpt-4.1-mini model.
#Azure Authentication → GPT Model → Response

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://name-resource.services.ai.azure.com/openai/v1"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider,
)

response = client.responses.create(
    model="gpt-4.1-mini-1",
    input="Explain RAG in one sentence."
)

print(response.output_text)
