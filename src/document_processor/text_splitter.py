from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextSplitter:

    def __init__(
        self,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    ):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=chunk_size,

            chunk_overlap=chunk_overlap,

            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):

        print("=" * 50)
        print("Splitting documents into chunks...")
        print("=" * 50)

        chunks = self.splitter.split_documents(documents)

        print(f"Total Chunks Created : {len(chunks)}")

        return chunks