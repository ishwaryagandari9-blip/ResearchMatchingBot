import streamlit as st
import chromadb
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

chroma_client = chromadb.PersistentClient(path="chroma_store")
collection = chroma_client.get_or_create_collection(name="faculty")

def get_embedding(text):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[text]
    )
    return response.embeddings[0].values

st.title("🎓 Research Faculty Matching System")

query = st.text_input("Enter student interest (e.g., NLP, AI, Cybersecurity)")

if st.button("Find Match") and query:

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    best_match = results["documents"][0][0]

    prompt = f"""
    Student Interest: {query}

    Faculty Profile:
    {best_match}

    Explain why this faculty is the best match.
    """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    st.subheader("🎯 Best Match")
    st.write(best_match)

    st.subheader("💡 Explanation")
    st.write(response.text)

    st.subheader("📊 Distance Score")
    st.write(results["distances"][0][0])