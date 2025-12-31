from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings()

DOC_INTENT_EXAMPLES = [
    "what is this document about",
    "summarize the pdf",
    "overall topic of the document",
    "main focus of this paper",
    "give an overview of the document"
]

def is_document_level_question(question: str, threshold: float = 0.6) -> bool:
    q_emb = embeddings.embed_query(question)
    intent_embs = embeddings.embed_documents(DOC_INTENT_EXAMPLES)

    similarities = cosine_similarity([q_emb], intent_embs)[0]
    return max(similarities) >= threshold
