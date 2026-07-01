import streamlit as st

from src.config.settings import (
    OLLAMA_MODEL,
    EMBEDDING_MODEL,
)


class Sidebar:
    """
    Handles the complete application sidebar.

    Features:
    - Project information
    - New Chat
    - Clear Chat
    - Model Information
    - Session Statistics
    - Future placeholders
    """

    def __init__(self):
        pass

    # ==========================================================
    # Render Sidebar
    # ==========================================================

    def render(self):

        with st.sidebar:

            # --------------------------------------------------
            # Header
            # --------------------------------------------------

            st.title("🤖 QA AI Assistant")

            st.caption("Powered by LangChain + Ollama + FAISS")

            st.divider()

            # --------------------------------------------------
            # Chat Controls
            # --------------------------------------------------

            st.subheader("💬 Chat")

            if st.button(
                "➕ New Chat",
                use_container_width=True,
            ):
                st.session_state.messages = []
                st.rerun()

            if st.button(
                "🗑 Clear Chat",
                use_container_width=True,
            ):
                st.session_state.messages = []
                st.rerun()

            st.divider()

            # --------------------------------------------------
            # Model Information
            # --------------------------------------------------

            st.subheader("🤖 Models")

            st.markdown(
                f"""
**LLM**

`{OLLAMA_MODEL}`

**Embedding Model**

`{EMBEDDING_MODEL}`
"""
            )

            st.divider()

            # --------------------------------------------------
            # Session Statistics
            # --------------------------------------------------

            st.subheader("📊 Session")

            total_messages = len(
                st.session_state.get("messages", [])
            )

            user_messages = len(
                [
                    msg
                    for msg in st.session_state.get("messages", [])
                    if msg["role"] == "user"
                ]
            )

            assistant_messages = len(
                [
                    msg
                    for msg in st.session_state.get("messages", [])
                    if msg["role"] == "assistant"
                ]
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "User",
                user_messages,
            )

            col2.metric(
                "AI",
                assistant_messages,
            )

            st.metric(
                "Total Messages",
                total_messages,
            )

            st.divider()

            # --------------------------------------------------
            # Knowledge Base
            # --------------------------------------------------

            st.subheader("📚 Knowledge Base")

            st.success("Vector Database Loaded")

            st.info("Retriever Ready")

            st.info("LLM Connected")

            st.divider()

            # --------------------------------------------------
            # Future Features
            # --------------------------------------------------

            st.subheader("🚀 Coming Soon")

            st.checkbox(
                "Conversation Memory",
                value=False,
                disabled=True,
            )

            st.checkbox(
                "Streaming Response",
                value=False,
                disabled=True,
            )

            st.checkbox(
                "Upload PDF",
                value=False,
                disabled=True,
            )

            st.checkbox(
                "Multi Chat",
                value=False,
                disabled=True,
            )

            st.checkbox(
                "Dark Mode",
                value=False,
                disabled=True,
            )

            st.divider()

            # --------------------------------------------------
            # Footer
            # --------------------------------------------------

            st.caption("Version 2.0")

            st.caption("Developed using")

            st.markdown(
                """
- LangChain
- Ollama
- FAISS
- Streamlit
- HuggingFace Embeddings
"""
            )