from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from app.loaders import load_documents
from app.chunking import chunk_documents
from app.embeddings import create_vector_store
from app.rag_chain import build_rag_chain
from app.summary_store import load_summaries, save_summaries
from app.summarizer import summarize_document
from app.intent_router import is_document_level_question



def main():
    # 1️⃣ Load documents
    docs = load_documents("data/documents")
    chunks = chunk_documents(docs)

    # 2️⃣ Vector store
    vector_store = create_vector_store(chunks)
    rag = build_rag_chain(vector_store)

    # 3️⃣ Document-level summary (persisted)
    summaries = load_summaries()

    doc_path = Path("data/documents/IJCA_Research_Paper_2.pdf")
    doc_id = doc_path.name

    if doc_id not in summaries:
        summaries[doc_id] = summarize_document(docs)
        save_summaries(summaries)

    DOCUMENT_SUMMARY = summaries[doc_id]

    print("\n🔹 Open Document Intelligence System")
    print("Type 'exit' to quit\n")

    # 4️⃣ Interactive loop
    while True:
        question = input("Ask a question: ")

        if question.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        if is_document_level_question(question):
            print("\nANSWER (Document Summary):\n")
            print(DOCUMENT_SUMMARY)
        else:
            answer = rag.invoke(question)
            print("\nANSWER:\n")
            print(answer)

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
