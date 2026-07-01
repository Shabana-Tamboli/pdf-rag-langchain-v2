from langchain_core.documents import Document

from src.vector_store.vector_store_manager import VectorStoreManager
from src.config.settings import TOP_K_RESULTS


class Retriever:
    """
    Handles document retrieval from the vector database.
    """

    def __init__(self, vector_store: VectorStoreManager):
        self.vector_store = vector_store

    # ---------------------------------------------------------
    # LangChain Retriever
    # ---------------------------------------------------------

    def get_retriever(self, k: int = TOP_K_RESULTS):
        """
        Returns LangChain Retriever.
        """

        return self.vector_store.get_retriever(k)

    # ---------------------------------------------------------
    # Similarity Search
    # ---------------------------------------------------------

    def search(
        self,
        question: str,
        k: int = TOP_K_RESULTS,
    ) -> list[Document]:

        return self.vector_store.similarity_search(
            query=question,
            k=k,
        )

    # ---------------------------------------------------------
    # Similarity Search With Score
    # ---------------------------------------------------------

    def search_with_scores(
        self,
        question: str,
        k: int = TOP_K_RESULTS,
    ):

        return self.vector_store.similarity_search_with_score(
            query=question,
            k=k,
        )

    # ---------------------------------------------------------
    # Print Results
    # ---------------------------------------------------------

    def print_results(
        self,
        question: str,
        k: int = TOP_K_RESULTS,
    ):

        results = self.search_with_scores(question, k)

        print("\n" + "=" * 80)
        print("RETRIEVED DOCUMENTS")
        print("=" * 80)

        for i, (doc, score) in enumerate(results, start=1):

            print(f"\nDocument {i}")
            print(f"Score : {score:.4f}")
            print("-" * 60)

            print(doc.page_content)

            print("\nMetadata")
            print(doc.metadata)

        return results