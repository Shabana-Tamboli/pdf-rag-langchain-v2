import time

from src.retriever.retriever import Retriever
from src.llm.ollama_client import OllamaClient
from src.prompts.rag_prompt import RAG_PROMPT
from src.chains.rag_chain import build_chain
from src.memory.conversation_memory import ConversationMemory


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

        # --------------------------------------
        # Conversation Memory
        # --------------------------------------

        self.memory = ConversationMemory()

        # --------------------------------------
        # RAG Chain
        # --------------------------------------

        self.chain = build_chain(
            self.retriever.get_retriever(),
            RAG_PROMPT,
            self.llm,
        )

    # --------------------------------------------------
    # Ask Question
    # --------------------------------------------------

    def ask(self, question: str):

        self.memory.add_user_message(question)

        retrieval_start = time.time()

        docs = self.retriever.search(question)

        retrieval_time = time.time() - retrieval_start

        generation_start = time.time()

        history = "\n".join(
            [
                f"{msg.type}: {msg.content}"
                for msg in self.memory.get_messages()
            ]
        )

        answer = self.chain.invoke(
            {
                "question": question,
                "chat_history": history,
            }
        )

        generation_time = time.time() - generation_start

        self.memory.add_ai_message(answer)

        return {
            "question": question,
            "answer": answer,
            "documents": docs,
            "retrieval_time": retrieval_time,
            "generation_time": generation_time,
            "total_time": retrieval_time + generation_time,
        }

    # --------------------------------------------------
    # Get Conversation History
    # --------------------------------------------------

    def get_memory(self):

        return self.memory.get_messages()

    # --------------------------------------------------
    # Clear Conversation
    # --------------------------------------------------

    def clear_memory(self):

        self.memory.clear()

    # --------------------------------------------------
    # Print Conversation (Debug)
    # --------------------------------------------------

    def print_memory(self):

        self.memory.print_memory()

    # --------------------------------------------------
    # Streaming (Phase 3)
    # --------------------------------------------------

    def stream(self, question):

        self.memory.add_user_message(question)

        return self.chain.stream(question)