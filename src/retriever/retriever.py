from typing import List

from langchain_core.documents import Document

from src.vector_store.vector_store_manager import VectorStoreManager


class Retriever:
    """
    Wrapper around the vector store.

    Responsibilities
    ----------------
    - Retrieve relevant documents
    - Return LangChain retriever
    - Support future Hybrid Search
    """

    def __init__(
        self,
        vector_store: VectorStoreManager,
        top_k: int = 4,
    ):
        self.vector_store = vector_store
        self.top_k = top_k

    # ---------------------------------------------------------
    # Retrieve Documents
    # ---------------------------------------------------------

    def search(
        self,
        question: str,
    ) -> List[Document]:
        """
        Returns the most relevant documents.
        """

        return self.vector_store.similarity_search(
            query=question,
            k=self.top_k,
        )

    # ---------------------------------------------------------
    # Retriever Interface
    # ---------------------------------------------------------

    def get_retriever(self):
        """
        Returns LangChain Retriever.
        """

        return self.vector_store.get_retriever(
            k=self.top_k
        )

    # ---------------------------------------------------------
    # Search With Scores
    # ---------------------------------------------------------

    def search_with_scores(
        self,
        question: str,
    ):
        """
        Returns retrieved documents
        along with similarity scores.
        """

        return self.vector_store.similarity_search_with_score(
            query=question,
            k=self.top_k,
        )