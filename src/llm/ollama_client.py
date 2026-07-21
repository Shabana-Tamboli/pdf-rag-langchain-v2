from langchain_ollama import ChatOllama

from src.config.settings import OLLAMA_MODEL


class OllamaClient:
    """
    Wrapper around the Ollama LLM.

    Responsibilities
    ----------------
    - Load the configured model
    - Return the LLM instance
    - Support normal and streaming responses
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            temperature=0,
            streaming=True,
        )

    # ---------------------------------------------------------
    # Return LangChain LLM
    # ---------------------------------------------------------

    def get_llm(self):

        return self.llm

    # ---------------------------------------------------------
    # Standard Response
    # ---------------------------------------------------------

    def invoke(self, prompt: str):

        return self.llm.invoke(prompt)

    # ---------------------------------------------------------
    # Streaming Response
    # ---------------------------------------------------------

    def stream(self, prompt: str):

        for chunk in self.llm.stream(prompt):
            yield chunk