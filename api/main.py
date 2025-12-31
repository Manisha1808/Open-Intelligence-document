from fastapi import FastAPI
from pydantic import BaseModel

from app.loaders import load_documents
from app.chunking import chunk_documents
from app.embeddings import create_vector_store
from app.rag_chain import build_rag_chain
from app.summary_store import load_summaries
from app.intent_router import is_document_level_question

app = FastAPI(title="Open Document Intelligence API")

# ---------- Startup (runs once) ----------
docs = load_documents("data/documents")
chunks = chunk_documents(docs)

vector_store = create_vector_store(chunks)
rag = build_rag_chain(vector_store)

summaries = load_summaries()
DOCUMENT_SUMMARY = next(iter(summaries.values()))  # single-doc for now


# ---------- Request model ----------
class QueryRequest(BaseModel):
    question: str


# ---------- API endpoint ----------
@app.post("/query")
def query_doc(req: QueryRequest):
    question = req.question

    if is_document_level_question(question):
        return {
            "type": "document_summary",
            "answer": DOCUMENT_SUMMARY
        }

    answer = rag.invoke(question)
    return {
        "type": "rag_answer",
        "answer": answer
    }
