# Research Matching Bot

A Retrieval-Augmented Generation (RAG) based system that helps students find faculty members whose research interests match their own using semantic search powered by Google Gemini Embeddings and ChromaDB.

---

## Problem Statement

Students often spend a lot of time manually searching through faculty profiles to find professors whose research interests align with their own. Traditional keyword-based searches may miss relevant matches because they cannot understand the meaning of the text.

This project solves this problem by using semantic search with Retrieval-Augmented Generation (RAG). It converts faculty profiles into vector embeddings using Google Gemini Embeddings and stores them in ChromaDB. When a student enters a research interest, the system retrieves the most relevant faculty profile based on semantic similarity.

---

## Features

* Stores faculty research profiles in text format.
* Generates semantic embeddings using Google Gemini.
* Stores embeddings in ChromaDB.
* Accepts student research interests as input.
* Performs semantic similarity search.
* Returns the most relevant faculty profile.
* Faster and more accurate than keyword-based search.

---

## Tech Stack

* Python
* Google Gemini Embeddings API
* ChromaDB
* python-dotenv
* Git
* GitHub

---

## Project Structure

```text
ResearchMatchingBot/
│
├── app.py
├── create_db.py
├── search_faculty.py
├── list_models.py
├── requirements.txt
├── README.md
├── data/
│   ├── Anita_Reddy.txt
│   ├── Meena_Sharma.txt
│   ├── Naveen_Kumar.txt
│   ├── Priya_Rao.txt
│   └── Rahul_Sharma.txt
│
└── chroma_store/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ishwaryagandari9-blip/ResearchMatchingBot.git
```

Move into the project folder:

```bash
cd ResearchMatchingBot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project folder and add your Gemini API key:

```env
GEMINI_KEY=your_api_key_here
```

**Note:** Never upload your `.env` file or API key to GitHub.

---

## How to Run

Generate the embeddings and create the vector database:

```bash
python create_db.py
```

Search for the most relevant faculty:

```bash
python search_faculty.py
```

---

## Sample Output

**Student Research Interest**

```
Natural Language Processing
```

**Best Matching Faculty**

```
Priya Rao

Research Interests:
- Natural Language Processing
- Machine Learning
- Deep Learning
```

---

## Future Improvements

* Develop a web-based interface.
* Support multiple universities.
* Upload faculty profiles in PDF format.
* Improve ranking using Large Language Models (LLMs).
* Integrate real-time faculty profile updates.

---

## Contributors

**Team ThinkByte**

* Ishwarya Gandari
* Add your teammates' names here

---

## Acknowledgements

This project was developed as part of a hackathon to demonstrate how Retrieval-Augmented Generation (RAG) can improve research guidance by matching students with faculty members based on semantic similarity.
