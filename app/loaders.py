from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def load_documents(folder_path: str):
    documents = []
    for file in Path(folder_path).glob("*.pdf"):
        loader = PyPDFLoader(str(file))
        documents.extend(loader.load())
    return documents
