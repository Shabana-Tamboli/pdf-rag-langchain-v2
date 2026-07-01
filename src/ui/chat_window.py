import streamlit as st

from src.ui.message import (
    render_chat_history,
    render_user_message,
    render_assistant_message,
    render_thinking,
    render_welcome,
    render_error,
)


class ChatWindow:
    """
    Handles the complete chat interaction.
    """

    def __init__(self, rag_service):

        self.rag = rag_service

    # ==========================================================
    # Initialize Session
    # ==========================================================

    def initialize(self):

        if "messages" not in st.session_state:

            st.session_state.messages = []

    # ==========================================================
    # Render Chat Window
    # ==========================================================

    def render(self):

        self.initialize()

        st.title("🤖 QA AI Assistant")

        st.caption("Ask questions from your PDF knowledge base.")

        # ------------------------------------------
        # Welcome Screen
        # ------------------------------------------

        if len(st.session_state.messages) == 0:

            render_welcome()

        # ------------------------------------------
        # Previous Conversation
        # ------------------------------------------

        render_chat_history(st.session_state.messages)

        # ------------------------------------------
        # Chat Input
        # ------------------------------------------

        question = st.chat_input(
            "Ask anything about your PDFs..."
        )

        if question:

            self.process_question(question)

    # ==========================================================
    # Process Question
    # ==========================================================

    def process_question(self, question):

        # --------------------------
        # Store User Message
        # --------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        render_user_message(question)

        # --------------------------
        # Ask LLM
        # --------------------------

        try:

            with render_thinking():

                response = self.rag.ask(question)

            render_assistant_message(response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response["answer"],
                }
            )

        except Exception as ex:

            render_error(str(ex))