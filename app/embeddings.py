from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_STORE_PATH = Path("vector_store")

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings()

    # 1️⃣ If FAISS index already exists → LOAD it
    if VECTOR_STORE_PATH.exists():
        print("🔁 Loading existing FAISS index from disk...")
        return FAISS.load_local(
            VECTOR_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    # 2️⃣ Else → create FAISS and SAVE it
    print("🆕 Creating new FAISS index...")
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_STORE_PATH)

    print("💾 FAISS index saved to disk.")
    return vector_store
