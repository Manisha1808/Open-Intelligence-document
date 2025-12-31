from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="gemma:2b")

PROMPT = PromptTemplate.from_template(
    """
    Summarize the document below in 3–4 sentences.
    Focus on its main topic and purpose.

    Document:
    {text}

    Summary:
    """
)

def summarize_document(pages):
    text = "\n".join(p.page_content for p in pages)[:4000]
    return llm.invoke(PROMPT.format(text=text))
