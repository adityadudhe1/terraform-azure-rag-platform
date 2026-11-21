#7 Purpose: Combine retrieved chunks with the user question and generate a contextual answer using GPT.
#Question + Retrieved Chunks - GPT-4.1-mini - Answer
import os

from dotenv import load_dotenv

from openai import OpenAI
from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider
)

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

load_dotenv()

# ------------------------
# Configuration
# ------------------------

OPENAI_ENDPOINT = (
    "https://name-resource.services.ai.azure.com/openai/v1"
)

CHAT_MODEL = "gpt-4.1-mini-1"
EMBEDDING_MODEL = "text-embedding-3-small"

# ------------------------
# OpenAI Client
# ------------------------

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

openai_client = OpenAI(
    base_url=OPENAI_ENDPOINT,
    api_key=token_provider
)

# ------------------------
# Search Client
# ------------------------

search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="nvidia-rag-index",
    credential=AzureKeyCredential(
        os.getenv("AZURE_SEARCH_ADMIN_KEY")
    )
)

# ------------------------
# User Question
# ------------------------

question = input("Ask a question: ")

# ------------------------
# Question Embedding
# ------------------------

embedding_response = openai_client.embeddings.create(
    model=EMBEDDING_MODEL,
    input=question
)

query_vector = embedding_response.data[0].embedding

# ------------------------
# Retrieve Top Chunks
# ------------------------

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

context = ""

for result in results:
    context += result["content"] + "\n\n"

# ------------------------
# RAG Prompt
# ------------------------

prompt = f"""
Answer the question using ONLY the supplied context.

Context:
{context}

Question:
{question}

Answer:
"""

# ------------------------
# GPT Generation
# ------------------------

response = openai_client.responses.create(
    model=CHAT_MODEL,
    input=prompt
)

print("\n========== ANSWER ==========\n")
print(response.output_text)
