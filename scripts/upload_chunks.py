#Purpose: Generate embeddings for all chunks and upload them into Azure AI Search.
#Chunks → Embeddings → Azure AI Search Index
import os
from dotenv import load_dotenv

from pypdf import PdfReader
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

load_dotenv()

# ----- OpenAI -----

openai_endpoint = (
    "https://name-resource.services.ai.azure.com/openai/v1"
)

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

openai_client = OpenAI(
    base_url=openai_endpoint,
    api_key=token_provider
)

# ----- AI Search -----

search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="nvidia-rag-index",
    credential=AzureKeyCredential(
        os.getenv("AZURE_SEARCH_ADMIN_KEY")
    )
)

# ----- Read PDF -----

reader = PdfReader("nvidia-training.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

# ----- Chunking -----

chunk_size = 1000

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

# ----- Create Documents -----

documents = []

for i, chunk in enumerate(chunks):

    embedding = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )

    documents.append({
        "id": str(i + 1),
        "content": chunk,
        "contentVector": embedding.data[0].embedding
    })

# ----- Upload -----

result = search_client.upload_documents(
    documents=documents
)

print(f"Uploaded: {len(result)} documents")
