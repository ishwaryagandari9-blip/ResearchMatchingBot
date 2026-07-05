import chromadb
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

# Create ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_store")
collection = chroma_client.get_or_create_collection(name="faculty")

DATA_FOLDER = "data"

def get_embedding(text):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[text]
    )
    return response.embeddings[0].values


# Read ALL .txt files in data folder
file_count = 0

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".txt"):
        file_path = os.path.join(DATA_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        embedding = get_embedding(content)

        # unique id per file
        doc_id = filename.replace(".txt", "")

        collection.add(
            ids=[doc_id],
            documents=[content],
            embeddings=[embedding],
            metadatas=[{"source": filename}]
        )

        file_count += 1
        print(f"Added: {filename}")

print(f"\nTotal files stored: {file_count}")