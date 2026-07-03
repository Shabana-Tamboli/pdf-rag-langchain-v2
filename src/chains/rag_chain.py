from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda


def build_chain(retriever, prompt, llm):
    """
    Builds the conversational RAG chain.
    """

    chain = (
        {
            "context": RunnableLambda(
                lambda x: retriever.invoke(x["question"])
            ),
            "question": RunnableLambda(
                lambda x: x["question"]
            ),
            "chat_history": RunnableLambda(
                lambda x: x["chat_history"]
            ),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain