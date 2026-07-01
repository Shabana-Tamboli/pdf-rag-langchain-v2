from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader

from src.config.settings import DATA_DIR


class PDFLoader:

    def __init__(self, data_directory: Path = DATA_DIR):
        self.data_directory = data_directory

    def load_documents(self):
        """
        Loads every PDF inside the data folder.
        Returns a list of LangChain Document objects.
        """

        print("=" * 50)
        print("Loading PDF documents...")
        print("=" * 50)

        loader = PyPDFDirectoryLoader(
            str(self.data_directory)
        )

        documents = loader.load()

        print(f"Total Pages Loaded : {len(documents)}")

        return documents