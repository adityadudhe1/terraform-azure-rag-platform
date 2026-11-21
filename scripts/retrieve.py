#6 Purpose: Perform vector similarity search and retrieve the most relevant chunks.
#Question → Embedding → Vector Search → Top Matching Chunks
import os
from dotenv import load_dotenv

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

load_dotenv()

question = "Which NVIDIA certifications discuss power and cooling?"

# OpenAI Client
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url="https://name-resource.services.ai.azure.com/openai/v1",
    api_key=token_provider,
)

# Create embedding for question
embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=question
)

query_vector = embedding.data[0].embedding

# Search Client
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="nvidia-rag-index",
    credential=AzureKeyCredential(
        os.getenv("AZURE_SEARCH_ADMIN_KEY")
    )
)

results = search_client.search(
    search_text=None,
    vector_queries=[
        VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=3,
            fields="contentVector"
        )
    ],
    select=["content"]
)

for i, result in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(result["content"][:500])
