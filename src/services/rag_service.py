import time

from src.retriever.retriever import Retriever
from src.llm.ollama_client import OllamaClient
from src.prompts.rag_prompt import RAG_PROMPT
from src.chains.rag_chain import build_chain


class RAGService:
    """
    Main service responsible for answering user questions
    using Retrieval-Augmented Generation (RAG).
    """

    def __init__(
        self,
        retriever: Retriever,
        llm_client: OllamaClient,
    ):

        self.retriever = retriever

        self.llm = llm_client.get_llm()

        self.chain = build_chain(
            self.retriever.get_retriever(),
            RAG_PROMPT,
            self.llm,
        )

    # --------------------------------------------------
    # Ask Question
    # --------------------------------------------------

    def ask(self, question: str):

        retrieval_start = time.time()

        docs = self.retriever.search(question)

        retrieval_time = time.time() - retrieval_start

        generation_start = time.time()

        answer = self.chain.invoke(question)

        generation_time = time.time() - generation_start

        return {

            "question": question,

            "answer": answer,

            "documents": docs,

            "retrieval_time": retrieval_time,

            "generation_time": generation_time,

            "total_time": retrieval_time + generation_time,

        }

    # --------------------------------------------------
    # Print Retrieved Docs
    # --------------------------------------------------

    def print_sources(self, docs):

        print("\n")
        print("=" * 80)
        print("RETRIEVED DOCUMENTS")
        print("=" * 80)

        for index, doc in enumerate(docs, start=1):

            print(f"\nDocument {index}")

            print("-" * 60)

            print(doc.page_content)

            print("\nMetadata")

            print(doc.metadata)

    # --------------------------------------------------
    # Streaming (Future Streamlit UI)
    # --------------------------------------------------

    def stream(self, question):

        return self.chain.stream(question)