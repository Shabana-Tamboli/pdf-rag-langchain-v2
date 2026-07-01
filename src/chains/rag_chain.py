from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def build_chain(
    retriever,
    prompt,
    llm
):
    """
    Builds the complete RAG chain.

    Flow:

    Question
        │
        ▼
    Retriever
        │
        ▼
    Context
        │
        ▼
    Prompt
        │
        ▼
    LLM
        │
        ▼
    String Output
    """

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain