from langchain_ollama import ChatOllama

from src.config.settings import OLLAMA_MODEL


class OllamaClient:
    """
    Wrapper class for Ollama LLM.

    Responsible for:
    - Loading the model
    - Configuring parameters
    - Returning a reusable LLM instance
    """

    def __init__(
        self,
        model: str = OLLAMA_MODEL,
        temperature: float = 0.2,
        num_predict: int = 1024,
        streaming: bool = True,
    ):

        self.model = model
        self.temperature = temperature
        self.num_predict = num_predict
        self.streaming = streaming

        self.llm = None

    # -------------------------------------------------------
    # Load Model
    # -------------------------------------------------------

    def load_model(self):

        if self.llm is None:

            self.llm = ChatOllama(

                model=self.model,

                temperature=self.temperature,

                num_predict=self.num_predict,

                streaming=self.streaming,

            )

        return self.llm

    # -------------------------------------------------------
    # Getter
    # -------------------------------------------------------

    def get_llm(self):

        return self.load_model()

    # -------------------------------------------------------
    # Invoke
    # -------------------------------------------------------

    def invoke(self, prompt: str):

        llm = self.load_model()

        return llm.invoke(prompt)

    # -------------------------------------------------------
    # Stream
    # -------------------------------------------------------

    def stream(self, prompt: str):

        llm = self.load_model()

        return llm.stream(prompt)