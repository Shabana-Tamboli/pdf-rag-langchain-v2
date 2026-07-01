import streamlit as st

from src.ui.components import (
    render_metrics,
    render_sources,
)


# ==========================================================
# User Message
# ==========================================================

def render_user_message(message: str):
    """
    Render a user chat message.
    """

    with st.chat_message("user"):

        st.markdown(message)


# ==========================================================
# Assistant Message
# ==========================================================

def render_assistant_message(response: dict):
    """
    Render AI response.
    """

    with st.chat_message("assistant"):

        # ----------------------------
        # Answer
        # ----------------------------

        st.markdown(response["answer"])

        st.write("")

        # ----------------------------
        # Metrics
        # ----------------------------

        render_metrics(response)

        st.write("")

        # ----------------------------
        # Sources
        # ----------------------------

        render_sources(response["documents"])


# ==========================================================
# Thinking Indicator
# ==========================================================

def render_thinking():
    """
    Spinner shown while the LLM is generating.
    """

    return st.spinner("🤖 Thinking...")


# ==========================================================
# Error Message
# ==========================================================

def render_error(message: str):

    with st.chat_message("assistant"):

        st.error(message)


# ==========================================================
# Welcome Screen
# ==========================================================

def render_welcome():

    st.markdown(
        """
# 🤖 QA AI Assistant

Welcome!

You can ask questions from your PDFs.

### Example Questions

- What is Selenium?

- Explain Explicit Wait.

- Difference between Implicit and Explicit Wait?

- Explain StaleElementReferenceException.

- What is Page Object Model?

- What is XPath?

---

Start typing below 👇
"""
    )


# ==========================================================
# Chat History
# ==========================================================

def render_chat_history(messages):
    """
    Render all previous messages.
    """

    for message in messages:

        if message["role"] == "user":

            render_user_message(message["content"])

        else:

            with st.chat_message("assistant"):

                st.markdown(message["content"])