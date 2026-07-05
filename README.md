# Research Matching Bot

A Retrieval-Augmented Generation (RAG) based system that helps students find faculty members whose research interests match their own using semantic search powered by Gemini Embeddings and ChromaDB.
## Problem Statement

Students often spend a lot of time manually searching through faculty profiles to find professors whose research interests align with their own. Keyword-based searches frequently miss relevant matches because they cannot understand the meaning of the text.

This project solves that problem by using Retrieval-Augmented Generation (RAG) with semantic embeddings to identify the most relevant faculty members based on a student's research interests.
## Features

- Stores faculty research profiles in a structured format.
- Generates semantic embeddings using Google Gemini.
- Stores embeddings efficiently using ChromaDB.
- Accepts a student's research interest as input.
- Performs semantic similarity search to find the best matching faculty.
- Returns the most relevant faculty profile instead of relying on simple keyword matching.
## Tech Stack

- Python
- Google Gemini Embeddings API
- ChromaDB (Vector Database)
- python-dotenv
- Git & GitHub
