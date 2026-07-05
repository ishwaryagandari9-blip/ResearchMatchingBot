import chromadb
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_store")
collection = chroma_client.get_or_create_collection(name="faculty")

def get_embedding(text):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[text]
    )
    return response.embeddings[0].values

# Take input from user
query = input("Enter student interest: ")

# Convert query to embedding
query_embedding = get_embedding(query)

# Search in database
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print("\n🎯 Best Matching Faculty:\n")

print("Document:\n", results["documents"][0][0])
print("\nSource:", results["metadatas"][0][0])
print("\nDistance Score:", results["distances"][0][0])