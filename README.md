# Open Document Intelligence System 📄

A **Retrieval-Augmented Generation (RAG)** based document intelligence system that can read PDFs, understand their content, and answer user questions using **semantic search + Large Language Models**.

This project is designed as a **long-term, scalable GenAI system**, not just a demo.

---

## 🚀 Features (Current)

- 📄 **PDF Ingestion**
  - Automatically loads all PDFs from a documents directory
  - Supports multiple real-world documents

- ✂️ **Smart Chunking**
  - Breaks documents into manageable semantic chunks

- 🔢 **Embeddings + Vector Search**
  - Uses HuggingFace embeddings
  - Stores vectors in **FAISS** for fast semantic retrieval
  - FAISS index is **persisted to disk** (no recomputation on restart)

- 🧠 **Retrieval-Augmented Generation (RAG)**
  - Retrieves relevant chunks
  - Passes grounded context to the LLM
  - Prevents hallucination

- 🔀 **Intent Routing**
  - Distinguishes between:
    - Document-level questions (summary/overview)
    - Fact-based questions (RAG)
  - Uses semantic similarity instead of keywords

- 📝 **Document-Level Summaries**
  - Generates and stores summaries per document
  - Summaries are reused for overview-type questions

- 🌐 **FastAPI Backend**
  - Exposes the RAG pipeline as an API
  - Ready for UI and frontend integration
    


Open-Intelligence-document/
│
├── app/
│ ├── loaders.py # PDF loading
│ ├── chunking.py # Text chunking
│ ├── embeddings.py # Embedding + FAISS logic
│ ├── retriever.py # Vector retrieval
│ ├── rag_chain.py # RAG pipeline
│ ├── intent_router.py # Summary vs RAG routing
│ ├── summarizer.py # Document summarization
│ ├── summary_store.py # Persist summaries
│
├── data/
│ ├── documents/ # PDF documents
│ └── summaries.json # Stored summaries
│
├── vector_store/
│ ├── index.faiss # FAISS vectors
│ └── index.pkl # FAISS metadata
│
├── api/
│ └── main.py # FastAPI entrypoint
│
├── main.py # CLI entrypoint
├── README.md
├── pyproject.toml
└── .gitignore
---


---

## ▶️ How It Works (High-Level)

1. PDFs are loaded and chunked  
2. Chunks are converted into embeddings  
3. Embeddings are stored in FAISS  
4. User question is analyzed:
   - **Overview question** → document summary
   - **Factual question** → RAG pipeline
5. LLM generates a grounded answer using retrieved context  

---

## 🧪 Run Locally

### 1️⃣ Install dependencies
```bash
uv sync

2️⃣ Activate environment
.venv\Scripts\activate   # Windows

3️⃣ Run CLI version
python main.py

4️⃣ Run API
uvicorn api.main:app --reload


Visit:

http://127.0.0.1:8000/docs

🔐 Security

Secrets are managed via environment variables

.env is excluded using .gitignore

No sensitive keys are committed to GitHub

🛣️ Roadmap (Planned)

Incremental indexing for new documents

Source attribution in answers

Confidence-based fallback responses

UI integration

Deployment

🎤 Interview Summary

“I built a RAG-based document intelligence system using LangChain, FAISS, and FastAPI.
It supports semantic retrieval, document-level summaries, persistent vector storage, and API-based access.”

📌 Tech Stack

Python

LangChain

FAISS

HuggingFace Embeddings

Ollama (Local LLM)

FastAPI

🧠 Author

Manisha Sen
BE Computer Engineering
Focused on Data & GenAI Systems

## 🏗️ Project Structure

