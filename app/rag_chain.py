from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

def build_rag_chain(vector_store):
    llm = Ollama(model="gemma:2b")

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    prompt = PromptTemplate.from_template(
        """
        Answer the question using ONLY the context below.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return rag_chain
