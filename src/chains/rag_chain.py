from langchain_core.output_parsers import StrOutputParser


def build_chain(prompt, llm):
    """
    Builds the RAG generation chain.

    Expected input:

    {
        "context": "...",
        "chat_history": "...",
        "question": "..."
    }

    The chain is responsible ONLY for generation.

    Retrieval happens outside this chain.
    """

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain