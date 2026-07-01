from langchain_community.embeddings import HuggingFaceEmbeddings

from src.config.settings import EMBEDDING_MODEL


class EmbeddingManager:
    """
    Creates and returns the embedding model used by the application.
    """

    def __init__(self):
        self.embedding_model = None

    def load_embeddings(self):
        """
        Loads the HuggingFace embedding model.
        """

        if self.embedding_model is None:

            print("=" * 50)
            print("Loading Embedding Model...")
            print("=" * 50)

            self.embedding_model = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL
            )

            print("Embedding Model Loaded Successfully.")

        return self.embedding_model