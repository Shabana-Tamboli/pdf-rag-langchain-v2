import time
from typing import List

from langchain_core.documents import Document

from src.chains.rag_chain import build_chain
from src.llm.ollama_client import OllamaClient
from src.memory.conversation_memory import ConversationMemory
from src.prompts.rag_prompt import RAG_PROMPT
from src.retriever.retriever import Retriever


class RAGService:
    """
    Main service responsible for answering user questions.

    Responsibilities:
    -----------------
    1. Retrieve documents
    2. Maintain conversation history
    3. Build prompt variables
    4. Invoke the LLM
    5. Return answer + metadata
    """

    def __init__(
        self,
        retriever: Retriever,
        llm_client: OllamaClient,
    ):
        self.retriever = retriever

        self.llm = llm_client.get_llm()

        self.memory = ConversationMemory()

        # Generation chain only
        self.chain = build_chain(
            prompt=RAG_PROMPT,
            llm=self.llm,
        )

    # ---------------------------------------------------------
    # Ask Question
    # ---------------------------------------------------------

    def ask(self, question: str):

        # Save user question
        self.memory.add_user_message(question)

        # -------------------------------
        # Retrieve documents
        # -------------------------------

        retrieval_start = time.time()

        documents = self.retriever.search(question)

        retrieval_time = time.time() - retrieval_start

        # -------------------------------
        # Build prompt variables
        # -------------------------------

        context = self._format_documents(documents)

        history = self._format_chat_history()

        # -------------------------------
        # Generate answer
        # -------------------------------

        generation_start = time.time()

        answer = self.chain.invoke(
            {
                "context": context,
                "chat_history": history,
                "question": question,
            }
        )

        generation_time = time.time() - generation_start

        # Save assistant response
        self.memory.add_ai_message(answer)

        return {
            "question": question,
            "answer": answer,
            "documents": documents,
            "retrieval_time": retrieval_time,
            "generation_time": generation_time,
            "total_time": retrieval_time + generation_time,
        }

    # ---------------------------------------------------------
    # Stream Response
    # ---------------------------------------------------------

   # ---------------------------------------------------------
    # Stream Response
    # ---------------------------------------------------------

    def stream(self, question: str):

        # Store user message
        self.memory.add_user_message(question)

        # Retrieve relevant documents
        documents = self.retriever.search(question)

        # Prepare prompt variables
        context = self._format_documents(documents)
        history = self._format_chat_history()

        # Store complete response while streaming
        complete_answer = ""

        for chunk in self.chain.stream(
            {
                "context": context,
                "chat_history": history,
                "question": question,
            }
        ):
            complete_answer += chunk
            yield chunk

        # Save assistant response after streaming completes
        self.memory.add_ai_message(complete_answer)
    # ---------------------------------------------------------
    # Format Retrieved Documents
    # ---------------------------------------------------------

    def _format_documents(
        self,
        documents: List[Document],
    ) -> str:

        if not documents:
            return "No relevant documents found."

        context = []

        for index, doc in enumerate(documents, start=1):

            context.append(
                f"Document {index}\n"
                f"{doc.page_content}"
            )

        return "\n\n".join(context)

    # ---------------------------------------------------------
    # Format Conversation History
    # ---------------------------------------------------------

    def _format_chat_history(self):

        if self.memory.is_empty():
            return "No previous conversation."

        history = []

        for message in self.memory.get_last_messages(10):

            role = "User"

            if message.type == "ai":
                role = "Assistant"

            history.append(
                f"{role}: {message.content}"
            )

        return "\n".join(history)

    # ---------------------------------------------------------
    # Conversation Memory
    # ---------------------------------------------------------

    def clear_memory(self):
        self.memory.clear()

    def get_memory(self):
        return self.memory.get_messages()

    def print_memory(self):
        self.memory.print_memory()