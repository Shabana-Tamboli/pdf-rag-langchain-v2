from src.config.settings import VECTOR_DB_PATH

from src.embeddings.embedding_manager import EmbeddingManager
from src.vector_store.vector_store_manager import VectorStoreManager
from src.services.rag_service import RAGService


def main():

    print("=" * 70)
    print("PDF RAG Chat")
    print("=" * 70)

    # -----------------------------------------------------
    # Load Embeddings
    # -----------------------------------------------------

    embedding_manager = EmbeddingManager()

    embeddings = embedding_manager.load_embeddings()

    # -----------------------------------------------------
    # Load FAISS
    # -----------------------------------------------------

    vector_store = VectorStoreManager(
        VECTOR_DB_PATH,
        embeddings
    )

    vector_store.load()

    # -----------------------------------------------------
    # Retriever
    # -----------------------------------------------------

    retriever = vector_store.as_retriever()

    # -----------------------------------------------------
    # RAG Service
    # -----------------------------------------------------

    rag = RAGService(retriever)

    print("\nSystem Ready.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You : ").strip()

        if not question:
            print("Please enter a valid question.\n")
            continue

        if question.lower() in ["exit", "quit", "bye"]:
            print("\nGoodbye!\n")
            break

        answer = rag.ask(question)

        print("\nAssistant:\n")
        print(answer)
        print("\n" + "-" * 70 + "\n")


if __name__ == "__main__":
    main()