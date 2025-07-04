# RAG PDF QA App
A Retrieval-Augmented Generation (RAG) application for any PDF documents. Upload PDF files, build a vector database, and interactively query your knowledge base using Gemini AI.

## Features
- Upload Any PDF:
Place any PDF files (legal, academic, technical, business, etc.) into the data/ folder.
- Automatic Text Chunking & Embedding:
PDFs are split into manageable text chunks and embedded using state-of-the-art models.
- Vector Database with ChromaDB:
All document embeddings are stored in a persistent ChromaDB vector database for fast retrieval.
- RAG-Style Querying:
Query your knowledge base from the command line. The app retrieves the most relevant document chunks and sends them, along with your question, to Gemini (Google Generative AI) for a context-aware answer.
- Domain-Agnostic:
The pipeline works with any PDF content—legal, research, technical, business, and more.

## Technologies Used
- Python – Core scripting
- ChromaDB – Vector database for document embeddings
- LangChain Community – PDF loading and text splitting
- Google Generative AI (Gemini) – LLM for answer generation
- PyPDF – PDF parsing

## How to Use
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Create a .env file and set your Gemini API key:
```bash
GEMINI_API_KEY=your_api_key_here
```
3. Add your PDF files:
Place your PDF files in the data/ directory (or use the default US individual tax file).

4. Build the vector database:
```bash
python build_vector_db.py
```
5. Query your knowledge base:
```bash
python law_query.py
```
Enter your question when prompted and receive an AI-powered answer based on your documents.

## What I Learned
* Building a RAG pipeline for document Q&A
* Integrating document chunking, embedding, and vector search with LLMs
* Managing API keys and environment variables securely
* Practical experience with ChromaDB, LangChain, and Google Gemini