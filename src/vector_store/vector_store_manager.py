from pathlib import Path

from langchain_community.vectorstores import FAISS


class VectorStoreManager:
    """
    Handles all vector database operations.

    Responsibilities:
    1. Create FAISS vector database
    2. Save vector database
    3. Load vector database
    4. Perform similarity search
    5. Return LangChain Retriever
    """

    def __init__(self, db_path: str, embeddings):
        self.db_path = Path(db_path)
        self.embeddings = embeddings
        self.vector_store = None

    # ---------------------------------------------------------
    # Create FAISS database from documents
    # ---------------------------------------------------------

    def create_vector_store(self, documents):
        """
        Creates FAISS vector store from document chunks.
        """

        print("=" * 60)
        print("Creating FAISS Vector Store...")
        print("=" * 60)

        self.vector_store = FAISS.from_documents(
            documents=documents,
            embedding=self.embeddings
        )

        print("FAISS Vector Store Created Successfully.")

    # ---------------------------------------------------------
    # Save FAISS database
    # ---------------------------------------------------------

    def save(self):
        """
        Saves FAISS database to disk.
        """

        if self.vector_store is None:
            raise ValueError("Vector store has not been created.")

        self.db_path.mkdir(parents=True, exist_ok=True)

        self.vector_store.save_local(str(self.db_path))

        print(f"Vector Store saved to: {self.db_path}")

    # ---------------------------------------------------------
    # Load FAISS database
    # ---------------------------------------------------------

    def load(self):
        """
        Loads FAISS database from disk.
        """

        print("=" * 60)
        print("Loading FAISS Vector Store...")
        print("=" * 60)

        self.vector_store = FAISS.load_local(
            folder_path=str(self.db_path),
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

        print("Vector Store Loaded Successfully.")

        return self.vector_store

    # ---------------------------------------------------------
    # Similarity Search
    # ---------------------------------------------------------

    def similarity_search(self, query: str, k: int = 4):
        """
        Returns top-k similar documents.
        """

        if self.vector_store is None:
            raise ValueError("Vector store is not loaded.")

        return self.vector_store.similarity_search(
            query=query,
            k=k
        )

    # ---------------------------------------------------------
    # Similarity Search with Score
    # ---------------------------------------------------------

    def similarity_search_with_score(self, query: str, k: int = 4):
        """
        Returns top-k similar documents with similarity scores.
        """

        if self.vector_store is None:
            raise ValueError("Vector store is not loaded.")

        return self.vector_store.similarity_search_with_score(
            query=query,
            k=k
        )

    # ---------------------------------------------------------
    # LangChain Retriever
    # ---------------------------------------------------------

    def get_retriever(self, k: int = 4):
        """
        Returns LangChain Retriever.
        """

        if self.vector_store is None:
            raise ValueError("Vector store is not loaded.")

        return self.vector_store.as_retriever(
            search_kwargs={"k": k}
        )