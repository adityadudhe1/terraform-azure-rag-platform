#3 Purpose: Extract text from the NVIDIA certification PDF.
#PDF → Text Extraction

from pypdf import PdfReader
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

reader = PdfReader("nvidia-training.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

chunk_size = 1000

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

endpoint = "https://name-resource.services.ai.azure.com/openai/v1"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

for i, chunk in enumerate(chunks):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )

    print(
        f"Chunk {i+1}: {len(response.data[0].embedding)} dimensions"
    )
