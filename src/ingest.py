from src.config.settings import DATA_DIR, VECTOR_DB_DIR

from src.document_loader.pdf_loader import PDFLoader
from src.splitter.text_splitter import TextSplitter
from src.embeddings.embedding_manager import EmbeddingManager
from src.vector_store.vector_store_manager import VectorStoreManager


def main():

    print("=" * 70)
    print("PDF RAG INGESTION")
    print("=" * 70)

    # ---------------------------------------
    # Step 1 : Load PDFs
    # ---------------------------------------

    print("\nLoading PDF documents...")

    loader = PDFLoader(DATA_DIR)

    documents = loader.load_documents()

    print(f"Loaded {len(documents)} pages.")

    # ---------------------------------------
    # Step 2 : Split Documents
    # ---------------------------------------

    print("\nSplitting documents...")

    splitter = TextSplitter()

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # ---------------------------------------
    # Step 3 : Embeddings
    # ---------------------------------------

    print("\nLoading embedding model...")

    embedding_manager = EmbeddingManager()

    embeddings = embedding_manager.load_embeddings()

    # ---------------------------------------
    # Step 4 : Vector Store
    # ---------------------------------------

    print("\nCreating FAISS vector database...")

    vector_store = VectorStoreManager(
        VECTOR_DB_DIR,
        embeddings,
    )

    vector_store.create_vector_store(chunks)

    vector_store.save()

    print("\nVector database saved successfully.")

    print("\nIngestion completed successfully.")


if __name__ == "__main__":
    main()